from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json  # JSON olarak gönderilen veriyi al
        print("Alınan Veri:", data)
        
        # İşleme veya veritabanına kaydetme gibi işlemler burada yapılabilir
        
        return jsonify({"message": "Veri başarıyla alındı"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
