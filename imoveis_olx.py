from flask import Flask, redirect, request

app = Flask(__name__)
app.secret_key = ""

url_redirecionamento = []

@app.route("/")
def index():
    return "Bem Vindo!"

@app.route("/register_redirect_uri", methods=['POST'])
def register_redirect_uri():
    uri = request.form.get('redirect_uri')
    url_redirecionamento.append(uri)
    return "URI de redirecionamento registrada com sucesso"

@app.route("/redirect_to_olx")
def redirect_to_olx():
    if url_redirecionamento:
        return redirect(url_redirecionamento[0])
    else:
        return "Nenhuma URI de redirecionamento registrada ainda."

if __name__ == "__main__":
    app.run(debug=True)

