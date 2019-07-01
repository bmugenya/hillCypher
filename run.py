from flask import Flask,jsonify,render_template,request
from encrypt import Cipher


app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Get the message to
        # be encrypted
        message = request.form['message']

        # Get the key
        key = request.form['key']


        ans = Cipher().HillCipher(message, key)

        return render_template('index.html',ans=ans)

    return render_template('index.html')




    if __name__ == "__main__":
        app.run()


