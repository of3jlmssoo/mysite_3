# django on openshift

djangoをopenshiftの上で動かす。まずCRCで動かして、その後IBM Cloud(labs)の上で動かす。

## pod構成
- pod1 : postgresql
- pod2 : django(+uwsgi)
- pod3 : nginx
  
## メモ

- CRCの場合developerで作業を行う。IBM Cloudの場合labsのlogin系インストラクションで設定されるIDで作業を行う。ただし、podmanはkubeadminでログインする
- postgresqlについてはOpenShiftのtemplateを使う
- postgresqlのpersistent volumeについてはOpenShiftに任せてしまう。CRCの場合デフォルトで割り振られているpersistent volumesの一つに自動的に割り当てられる。IBM Cloudの場合、自動的にpersistent volumeが作成される
- djangoはCRC上でpodmanでbuildする。IBM Cloudのlabsの環境にはpodmanが導入されていないのでCRC上で作成したイメージをdocker-daemon、docker.hub経由でロードする
- nginxについては[OAK RIDGE][16]さん(人ではないが)を参考に build configからのimagestreamを経てのstart-build

### 初期作業
CRCについてはRed Hat社の導入インストラクションに従い特に問題なく稼働。DNSとかdnsmasqとか心配したが問題なかった。
IBM Cloudの場合IBM Cloudとocのログインを実行
<!-- 


Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

To login as a regular user, run 'oc login -u developer -p developer https://api.crc.testing:6443'.
To login as an admin, run 'oc login -u kubeadmin -p rQyHq-PQiCI-hiptk-CM3Vb https://api.crc.testing:6443'


Use the 'oc' command line interface:
  $ eval $(crc oc-env)
  $ oc login -u developer https://api.crc.testing:6443 -->

CRC(IBM Cloudのケースは省略)
```text
eval $(crc oc-env)
oc login -u developer https://api.crc.testing:6443
```

共通
```text
alias c="clear"; set -o vi

oc new-project myproject
oc whoami
oc get all

git clone https://github.com/of3jlmssoo/mysite_3.git
cd mysite_3/v3
```
<!-- CHANGE PAGE!!! -->
### postgresql
<!-- CRC上でpersisistent volumeを作る場合。
CREATE PERSISTENT VOLUME (IBM Cloudでは実施しない。自動作成を使う)
oc create -f psgr-pv-4-postgres.yaml
  spec:
    capacity:
      storage: 20Gi
    flexVolume:
    accessModes:
      - ReadWriteOnce
    claimRef:
      kind: PersistentVoumeClaim
      namespace: myproject
      name: postgresql -->
CRCとlabsのケースを分けているが深い意味は無い。      
```text
oc get templates -n openshift -o custom-columns=NAME:.metadata.name|grep -i ^postgres
(crc) oc process -o yaml openshift//postgresql-persistent > ./postgresql-persistent.yaml
(lab) oc process -o yaml openshift//postgresql-persistent > ./postgresql-persistent2.yaml
(lab) vi ./postgresql-persistent2.yaml
    edit kind: secret (DB name, ID/password)
    edit kind: PersistentVolumeClaim
        metadata:
            labels:
              template: postgresql-persistent-template
              app: postgres
            name: postgresql
(lab) diff ./postgresql-persistent.yaml ./postgresql-persistent2.yaml

oc create -f postgresql-persistent.yaml

oc rsh PODNAME /bin/bash
psql -U admin myapp
\l
\q
exit
```
### django
まずCRCケース。

```texdt
cd ..
podman-compose -f docker-compose.yml build
podman login -u kubeadmin -p $(oc whoami -t) default-route-openshift-image-registry.apps-crc.testing --tls-verify=false

podman tag localhost/mysite_3_web:latest default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web

podman push  --tls-verify=false default-route-openshift-image-registry.apps-crc.testing/myproject/mysite_3_web:latest 

oc get is
oc set image-lookup mysite_3_web

cd v3
```
podmanからdockerへ。
```text
podman images
podman push localhost/mysite_3_web docker-daemon:localhost/mysite_3_web:latest
docker images
docker tag localhost/mysite_3_web:latest of3jlmssoo/mysite_3_web:latest
docker images
docker login
docker push of3jlmssoo/mysite_3_web:latest
```
labsの場合、docker.hubからロードされるようにする。web-dep.yamlのimageにof3jlmssoo/を追加する。
```text
vi web-dep.yaml
     imageにof3jlmssoo/ を追加
```     
CRC、labs共通
```text
oc create -f web-dep.yaml,web-svc.yaml

oc rsh PODNAME /bin/bash
  python manage.py makemigrations
  python manage.py sqlmigrate app1 0001
  python manage.py migrate 
  python manage.py createsuperuser
exit
```

### nginx
<!-- CHANGE PAGE!!! -->
```text
cd crc
oc create -f n-bc.yml
oc create imagestream nginx
oc start-build nginx --from-dir=./ --follow
oc get imagestream nginx

oc set image-lookup nginx

oc create -f n-dep.yml

oc create -f n-svc.yml,n-rot.yml

oc get route nginx
```
<!-- CHANGE PAGE!!! -->




<!-- sudo yum -y install podman
oc adm policy add-scc-to-user anyuid -z runasanyuid --as system:admin
oc rollout latest deployment/web -->





[16]:https://github.com/olcf/olcf-user-docs/blob/master/services_and_applications/slate/use_cases/nginx_hello_world.rst