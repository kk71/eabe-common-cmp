#!/bin/sh

prod_user="root"
prod_ip="192.168.11.35"

rm -rf ./dist
pnpm run build
echo "now, sending to the server ..."

sftp $prod_user@$prod_ip << eeooff
cd /tmp
rm -r cmp-fe
put -r dist cmp-fe
eeooff

ssh $prod_user@$prod_ip << eeooff
cd /root/cmp
rm -rf frontend
mv /tmp/cmp-fe ./frontend
eeooff

echo "successfully updated."
