from flask import Flask, request, jsonify
import ask_llm as al


app = Flask(__name__)


@app.route('/LLM', methods = ['POST'])
def Ask_LLM():
    if request.method == 'POST':
        request_data = request.get_json()
        query = request_data['Question']
        index_name = request_data['Client']
        result = al.llm_response(query,index_name)
        return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)