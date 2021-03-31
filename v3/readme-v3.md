Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

To login as a regular user, run 'oc login -u developer -p developer https://api.crc.testing:6443'.
To login as an admin, run 'oc login -u kubeadmin -p rQyHq-PQiCI-hiptk-CM3Vb https://api.crc.testing:6443'


Use the 'oc' command line interface:
  $ eval $(crc oc-env)
  $ oc login -u developer https://api.crc.testing:6443

eval $(crc oc-env)
oc login -u developer https://api.crc.testing:6443
oc new-project myproject


CREATE PERSISTENT VOLUME
  spec:
    capacity:
      storage: 20Gi
    flexVolume:
    accessModes:
      - ReadWriteOnce
    claimRef:
      kind: PersistentVoumeClaim
      namespace: myproject
      name: postgresql

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

cd ..
podman-compose -f docker-compose.yml build
podman login -u kubeadmin -p $(oc whoami -t) default-route-openshift-image-registry.apps-crc.testing --tls-verify=false

podman tag localhost/mysite_3_web:latest default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web

podman push  --tls-verify=false default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web:latest 

oc get is
oc set image-lookup mysite_3_web
cd v3
oc create -f web-dep.yaml,web-svc.yaml

oc rsh PODNAME /bin/bash
  python manage.py makemigrations
  python manage.py sqlmigrate app1 0001
  python manage.py migrate 
  python manage.py createsuperuser


https://docs.olcf.ornl.gov/services_and_applications/slate/use_cases/nginx_hello_world.html

cd crc
oc login -u developer https://api.crc.testing:6443
oc create -f n-bc.yml
oc create imagestream nginx
oc start-build nginx --from-dir=./ --follow
oc get imagestream nginx

oc set image-lookup nginx

oc create -f n-dep.yml

oc create -f n-svc.yml,n-rot.yml

oc get route nginx






oc adm policy add-scc-to-user anyuid -z runasanyuid --as system:admin
oc rollout latest deployment/web





