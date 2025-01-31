from flask import Flask, render_template, request

app = Flask(__name__)

# Função para gerar assinatura com ícones e certificações
def gerar_assinatura(nome, cargo, email, telefone, agencia, certificacao):
    return f"""
    <div style="font-family: Arial, sans-serif; line-height: 1.5; color: #333;">
        <p>Atenciosamente,</p>
        <p>
            <strong>{nome}</strong><br>
            Comercial<br>
            {cargo}
        </p>
        <p>
            <img src="https://cdn-icons-png.flaticon.com/16/732/732200.png" width="16"> 
            <a href="mailto:{email}" style="text-decoration: none; color: #333;">{email}</a><br>

            <img src="https://cdn-icons-png.flaticon.com/16/159/159832.png" width="16"> 
            {telefone}<br>

            <img src="https://cdn-icons-png.flaticon.com/16/535/535239.png" width="16"> 
            {agencia}
        </p>

        {f'<p><strong>Certificação:</strong> {certificacao}</p>' if certificacao else ''}
        
        <p style="font-size: 10px; color: gray;">
            O conteúdo deste e-mail é confidencial e destinado exclusivamente ao destinatário especificado apenas na mensagem. 
            É estritamente proibido compartilhar qualquer parte desta mensagem com terceiros, sem o consentimento por escrito do remetente.
        </p>
    </div>
    """

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        cargo = request.form["cargo"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        agencia = request.form["agencia"]
        certificacao = request.form.get("certificacao", "")

        assinatura = gerar_assinatura(nome, cargo, email, telefone, agencia, certificacao)
        return render_template("index.html", assinatura=assinatura)
    
    return render_template("index.html", assinatura=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Deixa disponível na rede local
