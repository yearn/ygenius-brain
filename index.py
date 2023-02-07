# pip install gpt_index
# pip install langchain
# pip install sentencepiece

from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import os
import flask
from flask import request, jsonify
from flask_cors import CORS

# os.environ["OPENAI_API_KEY"] = ''

max_input_size = 3700
num_outputs = 300
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
prompt_helper = PromptHelper.from_llm_predictor(llm_predictor)

def construct_index(directory_path, index_name):
  documents = SimpleDirectoryReader(directory_path, recursive=True).load_data()
  index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
  index.save_to_disk(index_name)
  return index

app = flask.Flask(__name__)
CORS(app)

index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/ask', methods=['GET'])
def ask():
  history = request.args.get('history')
  prefix = '######## Chat history with anon for context \n\n' + history + '\n\n######## Current interactions with anon as yGenius (GPT-powered service fed with indexed data from Yearn Finance to help users explore Yearn ecosystem)\n\n'
  query = prefix + '\n\nQuestion: ' + request.args.get('query') + '\n\nAnswer: '
  print(query)
  response = index.query(query, response_mode="default", prompt_helper=prompt_helper) #, verbose=True)
  print(response.response.strip())
  return jsonify(response.response.strip())

# construct_index('./training-data', 'index.json')
app.run()
