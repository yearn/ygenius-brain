from gpt_index import GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import flask
from flask import request, jsonify
from flask_cors import CORS

max_input_size = 3700
num_outputs = 300
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
prompt_helper = PromptHelper.from_llm_predictor(llm_predictor)

app = flask.Flask(__name__)
CORS(app)

index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/ask', methods=['GET'])
def ask():
  history = request.args.get('history')
  prefix = '######## Below is chat history with anon (just for context)\n\n' + history + '\n\n######## Below is current interaction with anon as yGenius (GPT-powered bot that can do everything GPT does and also uses indexed data from Yearn Finance). When not provided with information to answer a question then say "I guess..." and proceed normally.\n\n'
  query = prefix + 'Prompt:\n' + request.args.get('query') + '\n\nResult:\n'
  print(query)
  response = index.query(query, response_mode="default", prompt_helper=prompt_helper)
  print(response.response.strip())
  return jsonify(response.response.strip())

def create_app():
    return app