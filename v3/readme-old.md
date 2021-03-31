





Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

Log in as administrator:
  Username: kubeadmin
  Password: Iwbxk-REmdE-xUz9A-7YNrF

Log in as user:
  Username: developer
  Password: developer

Use the 'oc' command line interface:
  $ eval $(crc oc-env)
  $ oc login -u developer https://api.crc.testing:6443



oc create -f n-bc.yml
oc create imagestream nginx
oc start-build nginx --from-dir=./ --follow
oc get imagestream nginx  

oc create -f n-dep.yml
oc get deployment nginx

oc get route nginx

oc login -u kubeadmin https://api.crc.testing:6443
oc whoami
oc create -f psgr-pv-4-kubeadmin.yaml
oc get pv
oc get pv example
oc describe pv example

oc login -u developer https://api.crc.testing:6443
oc get templates -n openshift -o custom-columns=NAME:.metadata.name|grep -i ^postgres
oc process -o yaml openshift//postgresql-persistent > ./postgresql-persistent.yaml
    edit kind: secret (DB name, ID/password)
    edit kind: PersistentVolumeClaim
        metadata:
            labels:
            template: postgresql-persistent-template
            app: postgres
            name: postgresql

oc whoami
oc create -f postgresql-persistent.yaml
oc rsh pod/postgresql-1-qlzsg /bin/bash
psql -U admin myapp

edit setting.py     HOST=postgresql based on service/postgresql
podman-compose -f docker-compose.yml build
podman tag localhost/mysite_3_web:latest default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web

as kubeadmin
oc login -u kubeadmin https://api.crc.testing:6443
podman login -u kubeadmin -p $(oc whoami -t) default-route-openshift-image-registry.apps-crc.testing --tls-verify=false
podman push default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web:latest --tls-verify=false
podman push default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web:latest --tls-verify=false
oc get is
oc set image-lookup mysite_3_web

oc login -u developer https://api.crc.testing:6443
oc create -f web-dep.yaml,web-svc.yaml
    [uWSGI] getting INI configuration from /mycode/mysite_3/uwsgi.ini
    open("/mycode/mysite_3/uwsgi.log"): Permission denied [core/logging.c line 288]

oc login -u kubeadmin https://api.crc.testing:6443
oc adm policy add-scc-to-user anyuid -z runasanyuid --as system:admin
oc patch deployment/web --patch '{"spec":{"template":{"spec":{"serviceAccountName": "runasanyuid
oc rollout latest deployment/web

oc create configmap confnginx --from-file=./mysite_nginx.conf
oc process -o yaml openshift//nginx-example > ./nginx-example.yaml





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
cd mysite_3/v2
kubectl apply -f psgr-config.yml,psgr-pv-pvc.yml,psgr-service.yml,psgr-stateful.yml
cd ..
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

