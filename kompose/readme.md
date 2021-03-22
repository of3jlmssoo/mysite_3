 Alt+Ctrl+Shift+R

docker --version
minikube version
kubectl version

docker images | grep myc

kubectl get all

ファイルを見せる
cat nginx_loadbalancer_service.yaml
kubectl apply -f nginx_loadbalancer_service.yaml

kubectl get all

アドレスとポートをコピペ

データ入力2件

2件目は保守金額を更新

サーチを実行

kubectl delete service nginx
アクセスできない

kubectl apply -f nginx_nordport_service.yaml
kubectl get service nginx
kubectl cluster-info
192.168.59.2:31740


kubectl logs pod/nginx-d76f669fc-qkwnf

kubectl exec -it pod/web-555fd95954-ps6fc -- /bin/bash
cd mysite_3 && cat uwsgi.log

minikube dashboard

Alt+Ctrl+Shift+R
kubectl delete -f nginx-deployment.yaml,nginx_loadbalancer_service.yaml,web-deployment.yaml,web-service.yaml,my-network-networkpolicy.yaml
kubectl apply -f nginx-deployment.yaml,nginx_loadbalancer_service.yaml,web-deployment.yaml,web-service.yaml,my-network-networkpolicy.yaml
kubectl apply -f nginx-deployment.yaml,nginx_nordport_service.yaml,web-deployment.yaml,web-service.yaml,my-network-networkpolicy.yaml


kubectl expose deployment nginx-deployment --type=LoadBalancer
kubectl apply -f psgr-config.yml,psgr-pv-pvc.yml,psgr-service.yml,psgr-stateful.yml
docker tag mysite_3_web:latest mycontainer-uwsgi:v1.0.0
docker tag nginx:latest mycontainer-nginx:v1.0.0

docker tag mycontainer-uwsgi:v1.0.0 of3jlmssoo/mycontainer-uwsgi:v1.0.0
docker tag mycontainer-nginx:v1.0.0 of3jlmssoo/mycontainer-nginx:v1.0.0
docker push of3jlmssoo/mycontainer-uwsgi:v1.0.0
docker push of3jlmssoo/mycontainer-nginx:v1.0.0


kubectl delete -f nginx-deployment.yaml
kubectl delete -f web-deployment.yaml
kubectl apply -f web-deployment.yaml
kubectl apply -f nginx-deployment.yaml
kubectl exec -it    -- cat config/settings.py
kubectl exec -it    -- cat mysite_3/uwsgi.log


sudo apt install postgresql-client-common
sudo apt-get install postgresql-client

psql -h localhost -U admin --password -p 32467 myapp


minikube service nginx

export APPLICATION_DB_NAME=quick_start_db
export APPLICATION_DB_USER=app_user
export APPLICATION_DB_INITIAL_PASSWORD=app_user_password

export SECURITY_ADMIN_USER=security_admin_user
export SECURITY_ADMIN_PASSWORD=security_admin_password
export REMOTE_DB_HOST=$(minikube ip)    192.168.59.2
export REMOTE_DB_PORT=30001

docker run --rm -it -e PGPASSWORD=${SECURITY_ADMIN_PASSWORD} postgres:9.6 \
  psql -U security_admin_user "postgres:172.17.0.7//:3001/postgres" -c "\du"


psql -U security_admin_user "postgres://${REMOTE_DB_HOST}:${REMOTE_DB_PORT}/postgres" \



https://medium.com/@suyashmohan/setting-up-postgresql-database-on-kubernetes-24a2a192e962
kubectl apply -f psgr-config.yml,psgr-pv-pvc.yml,psgr-service.yml,psgr-stateful.yml
kubectl exec -it postgres-statefulset-0  -- /bin/bash
psql -U admin myapp

myapp=# \l
                             List of databases
   Name    | Owner | Encoding |  Collate   |   Ctype    | Access privileges 
-----------+-------+----------+------------+------------+-------------------
 myapp     | admin | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | admin | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | admin | UTF8     | en_US.utf8 | en_US.utf8 | =c/admin         +
           |       |          |            |            | admin=CTc/admin
 template1 | admin | UTF8     | en_US.utf8 | en_US.utf8 | =c/admin         +
           |       |          |            |            | admin=CTc/admin
(4 rows)

 
kubectl get pods --namespace=kube-system -l k8s-app=kube-dns
cat /etc/resolv.conf

curl -I http://

kubectl get pod -o wide

docker login
docker tagでof3jlmssoo/をあたまにつける
docker push of3jlmssoo/mycontainer-uwsgi:v1.0.0
docker tag mycontainer-nginx:v1.0.0  of3jlmssoo/mycontainer-nginx:v1.0.0
docker push of3jlmssoo/mycontainer-nginx:v1.0.0


docker image prune

kubectl delete -f nginx-deployment.yaml,web-deployment.yaml,nginx_nordport_service.yaml,web-service.yaml

kubectl apply -f nginx-deployment.yaml,web-deployment.yaml,nginx_nordport_service.yaml,web-service.yaml
kubectl apply -f psgr-config.yml,psgr-pv-pvc.yml,psgr-service.yml,psgr-stateful.yml

docker-compose down -v --rmi all
docker-compose build --no-cache

docker-compose 
docker-compose build --no-cache
docker-compose build 
docker-compose up

docker images | head -10

docker tag nginx:latest mycontainer-nginx:v1.0.0
docker tag mysite_3_web:latest mycontainer-uwsgi:v1.0.0



docker images | more
docker image rm -f 
docker tag nginx:latest mycontainer-nginx:v1.0.0

192.168.59.2:31740

kubectl exec my-nginx-3800858182-e9ihh -- printenv | grep SERVICE

kubectl get services kube-dns --namespace=default




# install1
sudo apt-get install dnsmasq
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved

sudo nano /etc/NetworkManager/NetworkManager.conf
# add under [main]
# dns=dnsmasq

sudo cp /etc/resolv.conf /etc/resolv.conf.bak
sudo rm /etc/resolv.conf; sudo ln -s /var/run/NetworkManager/resolv.conf /etc/resolv.conf

sudo systemctl start dnsmasq
sudo systemctl restart NetworkManager

# 戻す


sudo cp /etc/resolv.conf.bak $HOME/

sudo systemctl stop dnsmasq
sudo systemctl disable dnsmasq

sudo systemctl stop NetworkManager
sudo systemctl disable NetworkManager

sudo rm /etc/resolv.conf; sudo cp /etc/resolv.conf.bak /etc/resolv.conf

sudo systemctl enable systemd-resolved 
sudo systemctl start systemd-resolved
sudo systemctl restart NetworkManager     こいつは必要

# install2
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved

sudo rm /etc/resolv.conf 

cp /etc/resolv.conf $HOME/resolv.con-backup2
echo nameserver 8.8.8.8 | sudo tee /etc/resolv.conf
cat /etc/resolv.conf

sudo vim /etc/dnsmasq.conf
  port=53
  domain-needed
  bogus-priv
  strict-order
  expand-hosts
  #domain=thekelleys.org.uk
  domain=mypridomain.com
  listen-address=127.0.0.1 # Set to Server IP for network responses

sudo dnssec

sudo systemctl restart dnsmasq
sudo vim /etc/hosts
  10.1.3.4 server1.mypridomain.com
  10.1.4.4 erp.mypridomain.com 

sudo systemctl restart dnsmasq

sudo cp  /etc/resolv.conf $HOME/resolv.conf-backup22
cat /etc/resolv.conf
sudo vim /etc/resolv.conf
  nameserver 127.0.0.1
  nameserver 8.8.8.8
dig A erp.mypridomain.com  


kubectl get storageclass
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml
kubectl get pods --namespace=kube-system -l k8s-app=kube-dns
kubectl -n kube-system edit configmap coredns --save-config
kubectl apply /tmp/kubectl-edit-hfieq.yaml
minikube --vm-driver=none start --extra-config=kubelet.resolv-conf=/run/systemd/resolve/resolv.conf

sudo systemctl start dnsmasq
sudo systemctl restart NetworkManager
kubectl run   --image busybox bbox
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml

wget -qO- 10.244.0.38



