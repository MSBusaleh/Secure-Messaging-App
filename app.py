from flask import Flask, render_template, request
from crypto.aes_gcm import encrypt_aes_gcm, decrypt_aes_gcm, generate_key
from crypto.utils import display_message, parse_message

app = Flask(__name__)

@app.route('/')
def main():
    print("Rendering main page")
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    print("Received encryption request")
    plaintext = request.form['message'].encode('utf-8')
    
    key = generate_key()
    ciphertext, iv = encrypt_aes_gcm(plaintext, key)
    ciphertext_str = display_message(ciphertext)
    print(f"Ciphertext (base64): {ciphertext_str}")
    
    return render_template(
        'index.html',
        ciphertext=ciphertext_str,
    )
