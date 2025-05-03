#!/bin/bash

echo "Telefon Soğutucu Başlatılıyor..."

# Arka planda çalışan gereksiz süreçleri listele
ps aux | grep -E 'Safari|YouTube|Instagram' | awk '{print $2}' | xargs kill -9

echo "Gereksiz süreçler kapatıldı!"
