kubectl apply -f psgr-config.yml,psgr-pv-pvc.yml,psgr-service.yml,psgr-stateful.yml
kubectl exec -it pod/postgres-statefulset-0 -- /bin/bash
psql -U admin -d myapp
myapp=# \l
myapp=# \q

kubectl delete pod dnsutils
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml


docker-compose -f ./docker-compose.yml build --no-cache


!!!cloud site!!!
docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.0
docker push of3jlmssoo/cloudsite_3_web:v1.0.0

!!!local site!!!
docker tag mysite_3_web:latest of3jlmssoo/mysite_3_web:v1.0.0
docker push of3jlmssoo/mysite_3_web:v1.0.0

kubectl delete deploy web
kubectl apply -f v2/web-dep.yaml

docker login
docker push of3jlmssoo/cloudsite_3_web:v1.0.0


kubectl apply -f web-dep.yaml
kubectl apply -f web-svc.yaml


kubectl create configmap confnginx --from-file=./mysite_nginx.conf

kubectl apply -f nginx-deployment.yaml  
kubectl apply -f nginx_loadbalancer_service.yaml

worked with sqlite

















git clone https://github.com/of3jlmssoo/mysite_3.git
cd mysite_3
docker-compose -f ./docker-compose.yml build
docker images | grep site
docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.0
docker login
docker push of3jlmssoo/cloudsite_3_web:v1.0.0
cd v2
kubectl apply -f web-dep.yaml,web-svc.yaml
kubectl get all
kubectl create configmap confnginx --from-file=./mysite_nginx.conf
kubectl apply -f nginx-deployment.yaml  
kubectl apply -f nginx_loadbalancer_service.yaml
kubectl get all

kubectl exec -it PODNAME!!!!!! -- /bin/bash
    pod name
python manage.py migrate
python manage.py createsuperuser

2021-07-01,2021-12-31
2021-01-01,2021-06-30


postgres-service.default.svc.cluster.local
10.107.177.226

kubectl delete deploy web
docker-compose -f docker-compose.yml build 
docker tag mysite_3_web:latest of3jlmssoo/mysite_3_web:v1.0.0
docker push of3jlmssoo/mysite_3_web:v1.0.0
kubectl apply -f v2/web-dep.yaml






























####
kubectl describe configmaps  confnginx
kubectl apply -f back-dep.yaml,back-svc.yaml
    backendを先に作る(helloが必要)


$ kubectl get service frontend
    NAME       TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
    frontend   LoadBalancer   10.97.124.188   10.97.124.188   80:30834/TCP   35s
$ curl 10.97.124.188
    {"message":"Hello"}

kubectl delete configmap confnginx
kubectl create configmap confnginx --from-file=./front-nginx.conf
kubectl describe configmaps  confnginx

## clear 
kubectl delete deploy backend
kubectl delete deploy frontend
kubectl delete service hello
kubectl delete service frontend

