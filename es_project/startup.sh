ip=`ifconfig wlan0 |grep "inet addr" | cut -d ':' -f 2|cut -d ' ' -f 1`
if [[ $ip = *[!\ ]* ]]; then
    1+1
else 
    ip=`ifconfig wlan1 |grep "inet addr" | cut -d ':' -f 2|cut -d ' ' -f 1`
    
fi

echo "Trying to start server at =>  "$ip":2"
sudo python /home/pi/Desktop/es_project/manage.py runserver $ip:2
