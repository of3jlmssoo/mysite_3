cd mysite_3
read -p "Press [Enter] key to resume." 
clear
docker-compose -f ./docker-compose.yml build
read -p "Press [Enter] key to resume." 
clear
docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.
read -p "Press [Enter] key to resume." 
clear
docker login
read -p "Press [Enter] key to resume." 
clear
docker images
read -p "Press [Enter] key to resume." 
clear
docker images | grep site
read -p "Press [Enter] key to resume." 
clear
docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.0
read -p "Press [Enter] key to resume." 
clear
docker push of3jlmssoo/cloudsite_3_web:v1.0.0
read -p "Press [Enter] key to resume." 
clear
cd v2
read -p "Press [Enter] key to resume." 
clear
vi web-dep.yaml
read -p "Press [Enter] key to resume." 
clear
image: of3jlmssoo/cloudsite_3_web:v1.0.0
read -p "Press [Enter] key to resume." 
clear
kubectl apply -f web-dep.yaml,web-svc.yaml
read -p "Press [Enter] key to resume." 
clear
kubectl create configmap confnginx --from-file=./mysite_nginx.conf
read -p "Press [Enter] key to resume." 
clear
kubectl apply -f nginx-deployment.yaml  
read -p "Press [Enter] key to resume." 
clear
kubectl apply -f nginx_loadbalancer_service.yaml
read -p "Press [Enter] key to resume. See the external Site!!!" 
clear
kubectl exec -it pod/web-6694cd7775-x4jhk -- /bin/bash
read -p "Press [Enter] key to resume. See the external Site again!!!" 
clear
