Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

Log in as administrator:
  Username: kubeadmin
  Password: v7Si3-D7vss-c9AXA-DgfkG
  kubeadmin:v7Si3-D7vss-c9AXA-DgfkG

Log in as user:
  Username: developer
  Password: developer

Use the 'oc' command line interface:
  $ eval $(crc oc-env)
  $ oc login -u developer https://api.crc.testing:6443

eval $(crc oc-env)
oc login -u developer https://api.crc.testing:6443
oc new-project myproject


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

podman-compose -f docker-compose.yml build
podman tag localhost/mysite_3_web:latest default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web

podman images

oc create -f web-dep.yaml,web-svc.yaml

oc login -u kubeadmin https://api.crc.testing:6443
oc adm policy add-scc-to-user anyuid -z runasanyuid --as system:admin

oc rollout latest deployment/web





    podman login -u kubeadmin -p $(oc whoami -t) default-route-openshift-image-registry.apps-crc.testing --tls-verify=false
podman push default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web:latest --tls-verify=false
podman push default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web:latest --tls-verify=false
oc get is
oc set image-lookup mysite_3_web

oc login -u developer https://api.crc.testing:6443
oc create -f web-dep.yaml,web-svc.yaml
    [uWSGI] getting INI configuration from /mycode/mysite_3/uwsgi.ini
    open("/mycode/mysite_3/uwsgi.log"): Permission denied [core/logging.c line 288]
