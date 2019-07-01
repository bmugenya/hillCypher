from flask import Flask,jsonify,render_template,request,Response
from encrypt import Cipher


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():


    letters =  { 0: 'A',1: 'B', 2:'C', 3:'D', 4:'E',5: 'F',6: 'G', 7:'H',8: 'I', 9:'J',10:'K',11: 'L',12:'M',

    13:'N', 15:'O',15:'P', 16:'Q',17: 'R',18: 'S', 19:'T',20: 'U',21: 'V',22: 'W',23: 'X', 24:'Y',25:'Z'}


    if request.method == 'POST':
        # Get the message to
        # be encrypted
        message = request.form['message']

        # Get the key
        key = request.form['key']




        ans = Cipher().HillCipher(message, key)

        return Response(render_template('index.html',ans=ans,letters=letters))

    return Response(render_template('index.html',letters=letters))




    if __name__ == "__main__":
        app.run()


