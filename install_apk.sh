#!/bin/bash
echo "Установка мобильного обхода..."
pkg update && pkg install python -y
pip install requests
git clone https://github.com/OnelifeOnedeath/Zepret-White-List
cd Zepret-White-List
python mobile_proxy.py &
echo "Туннель запущен. Настройте прокси в WiFi на IP этого устройства"
