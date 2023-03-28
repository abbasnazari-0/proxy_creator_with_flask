[Step 1] first install apps [Step 1]

    apt-get install python3 python3-pip unzip  nginx  gunicorn -y

[Step 2] download scripts

    wget https://github.com/abbasnazari-0/proxy_creator_with_flask/archive/refs/tags/v3.zip &&  unzip v3.zip -d . && mkdir superproxy && mv proxy_creator_with_flask-3/* superproxy/ && mv superproxy/servermanager  /etc/nginx/sites-enabled/servermanager && unlink /etc/nginx/sites-enabled/default && unlink v3.zip && nginx -s reload 

[Step 3] install python settings

    pip3 install flask  

[Step 4] run flask server

    nohup gunicorn -w 3 superproxy:app --bind 0.0.0.0:3000 &
