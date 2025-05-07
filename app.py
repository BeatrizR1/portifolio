from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o frontend acesse a API

@app.route('/receita')
def receita():
    return jsonify({
        "titulo": "Bolo de Morango",
        "ingredientes": [
            "2 xícaras de farinha de trigo",
            "1 xícara de açúcar",
            "1/2 xícara de óleo",
            "3 ovos",
            "1 xícara de leite",
            "1 colher de sopa de fermento em pó",
            "1 colher de chá de essência de baunilha",
            "1 xícara de morangos picados"
        ],

        "modo_de_preparo": [
            "Pré-aqueça o forno a 180°C.",
            "Bata os ovos e o açúcar até formar um creme fofo.",
            "Adicione o óleo, o leite e a essência de baunilha, misturando bem.",
            "Acrescente a farinha peneirada aos poucos, misturando delicadamente.",
            "Adicione os morangos picados e misture suavemente.",
            "Por último, incorpore o fermento em pó.",
            "Despeje a massa em uma forma untada e enfarinhada.",
            "Asse por aproximadamente 35 minutos ou até dourar.",
            "Deixe esfriar antes de servir."
        ]

 })

if __name__ == "__main__":
    app.run(debug=True)