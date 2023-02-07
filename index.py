from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>dis is working ser!</h1>"

@app.route('/ask', methods=['GET'])
def ask():
    history = request.args.get('history')

    prefix = '######## Chat history with anon for context \n\n' + history + ' ######## Instructions:\n\n' + 'You will be provided indexed context about the DeFi yield protocol Yearn Finance (aka Yearn) to help answer a question. Don\'t invent links that don\'t exist outside the information provided. NEVER MENTION NAMES OF OTHER PEOPLE WHEN SUGGESTING SUPPORT ON OTHER CHANNELS.'
    query = prefix + '\n\nQuestion:\n' + request.args.get('query') + '\n\nAnswer:\n'

    index = GPTSimpleVectorIndex.load_from_disk('index-full.json')
    # index = GPTListIndex.load_from_disk('index.json')

    print(query)

    response = index.query(query, response_mode="default") #, verbose=True)
    
    print(response.response.strip())

    return jsonify(response.response.strip())

def construct_index(directory_path, index_name):
  max_input_size = 4096
  num_outputs = 800
  max_chunk_overlap = 20
  chunk_size_limit = 600

  llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))
  prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

  documents = SimpleDirectoryReader(directory_path, recursive=True).load_data()

  # use vector for cheaper search parts of the index to do operation, use list for expensive refinement operation with entire index

  index = GPTSimpleVectorIndex(
  # index = GPTListIndex(
      documents,  llm_predictor=llm_predictor, prompt_helper=prompt_helper, verbose=True
  )

  index.save_to_disk(index_name)

  return index

if __name__ == "__main__":
    app.run(debug=True)
# construct_index('./training-data', 'index-full.json')

# app.run()

# ask('', 'index.json')
