nohup python flask-ip.py &
sleep 2
curl http://localhost:5000/
curl http://localhost:5000/get_my_ip
