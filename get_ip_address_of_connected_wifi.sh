ip=`ifconfig wlan0 |grep "inet addr" | cut -d ':' -f 2|cut -d ' ' -f 1`
if [[ $ip = *[!\ ]* ]]; then
    1+1
else 
    ip=`ifconfig wlan1 |grep "inet addr" | cut -d ':' -f 2|cut -d ' ' -f 1`
    
fi

echo $ip
