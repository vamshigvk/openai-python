from flask import Flask, request
from flask_restx import Api, Resource
from helper import *
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
app = Api(app=application, title="Jake")
App = app.namespace('applications', title="OpenAI", description = "applications")


@App.route('/qna', methods=['GET'])
class Main1(Resource):
    @app.doc(responses={200:'OK', 400:'Client-side error', 500:'Server-side error'}, 
            params={'prompt':'Enter your question to get the answer. ex: what is an encyclopedia?'})
    
    def get(self):
        print('Hi from QnA')
        prompt = request.args.get('prompt')
        result_qna = qna(prompt)
        return {
            "prompt": prompt,
            "result_qna": result_qna
        }




if __name__=="__main__":
    application.run()

