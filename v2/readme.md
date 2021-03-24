kubectl apply -f psgr-config.yml,psgr-pv-pvc.yml,psgr-service.yml,psgr-stateful.yml
kubectl exec -it pod/postgres-statefulset-0 -- /bin/bash
psql -U admin -d myapp
myapp=# \l
myapp=# \q

kubectl delete pod dnsutils
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml

kubectl apply -f web-dep.yaml


kubectl create configmap confnginx --from-file=./mysite_nginx.conf

kubectl apply -f nginx-deployment.yaml  
kubectl apply -f nginx_loadbalancer_service.yaml

worked with sqlite

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

