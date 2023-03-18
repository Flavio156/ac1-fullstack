from flask import Flask, request

app = Flask(__name__)

@app.route('/media', methods=['POST'])
def media():
    nota1 = request.form['nota1']
    nota2 = request.form['nota2']
    media = (float(nota1) + float(nota2)) / 2
    return str(media)

if __name__ == '__main__':
    app.run()