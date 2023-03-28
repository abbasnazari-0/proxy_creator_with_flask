from flask import Flask, render_template, request
import subprocess
import os
app = Flask(__name__)
# 14ba08eef1d6e9293390a1969023cd1e
# generate random string for secret key
def generate_secret_key():
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

@app.route('/', methods=['GET', 'POST'])
def rootPage():
    return render_template('root.html')

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
    args = ['bash', 'mtp_install.sh', '-p', '4425', '-s', generate_secret_key(), '-t', 'bffb6a3d571717bd2bb14b11145d2a50', '-a', 'dd', '-a', 'tls', '-d', 'dl1.pubgtool.world', '-y']
    
    subprocess.run(args)
    return args


if __name__ == '__main__':
  app.run(host='0.0.0.0',  port=4000)