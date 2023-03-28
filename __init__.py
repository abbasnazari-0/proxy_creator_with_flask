from flask import Flask, render_template, request
import subprocess
import os
app = Flask(__name__)
import random

def get_random_port():
    used_ports = []
    if os.path.exists('usedport.txt'):
        with open('usedport.txt', 'r') as f:
            used_ports = f.read().splitlines()
    while True:
        port = random.randint(1024, 65535)
        if str(port) not in used_ports:
            used_ports.append(str(port))
            with open('usedport.txt', 'w') as f:
                f.write('\n'.join(used_ports))
            return port
# 14ba08eef1d6e9293390a1969023cd1e
# generate random string for secret key
def generate_secret_key():
    # Generate a 16-byte secret key
    secret_key = os.urandom(16)

    # Convert the secret key to hex format
    secret_hex = secret_key.hex()
    return secret_hex

@app.route('/', methods=['GET', 'POST'])
def rootPage():
    return render_template('root.html')


@app.route('/re', methods=['GET', 'POST'])
def re():
     return str(get_random_port()) + ' is your port, please save it for later use.'
    
@app.route('/create', methods=['GET', 'POST'])
def create_user():
    # get arg from 
    withAd = request.args.get('withAd', default = None, type = str)
    
    if os.path.isfile('mtp_install.sh') == False:
        # run this script curl -L -o mtp_install.sh https://git.io/fj5ru -y
        install = ['curl', '-L', '-o', 'mtp_install.sh', 'https://git.io/fj5ru']
        # run bash script and wait for finish
        subprocess.run(install)
        
        
    # run bash script
    # if( withAd != None):
    #     args = ['bash', 'mtp_install.sh', '-p', '4425', '-s', generate_secret_key(), '-a', 'dd', '-a', 'tls', '-d', 'dl1.pubgtool.world', '-y']
    # else:
    
    secret = generate_secret_key()
    args = ['bash', 'mtp_install.sh', '-p', get_random_port(), '-s', secret, '-t', 'bffb6a3d571717bd2bb14b11145d2a50', '-a', 'dd', '-a', 'tls', '-d', 'dl1.pubgtool.world', '-y']
    
    # run args and return output 
    data = subprocess.run(args, stdout=subprocess.PIPE)
     
    return "dd" + secret  +  " is your secret key, please save it for later use."


if __name__ == '__main__':
  app.run(host='0.0.0.0',  port=4000)
