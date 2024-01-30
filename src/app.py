from flask import Flask, request, jsonify
import ask_llm as al


app = Flask(__name__)


@app.route('/LLM', methods = ['POST'])
def Ask_LLM():
    if request.method == 'POST':
        request_data = request.get_json()
        query = request_data['Question']
        result = al.llm_response(query)
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)