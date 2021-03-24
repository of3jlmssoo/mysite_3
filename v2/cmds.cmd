kubectl apply -f web-dep.yaml,web-svc.yaml
read -p "Press [Enter] key to resume." 
clear
kubectl get all
read -p "Press [Enter] key to resume." 
clear
kubectl create configmap confnginx --from-file=./mysite_nginx.conf
read -p "Press [Enter] key to resume." 
clear
kubectl apply -f nginx-deployment.yaml  
read -p "Press [Enter] key to resume." 
clear
kubectl apply -f nginx_loadbalancer_service.yaml
read -p "Press [Enter] key to resume." 
clear
kubectl get all
read -p "Press [Enter] key to resume. See the external Site!!!" 
clear
kubectl exec -it pod/web-6694cd7775-x4jhk -- /bin/bash
read -p "Press [Enter] key to resume. See the external Site again!!!" 
clear
