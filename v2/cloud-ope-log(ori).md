414  git clone https://github.com/of3jlmssoo/mysite_3.git
  415  cd mysite_3
  416  ls
  417  docker-compose -f ./docker-compose.yml build
  418  docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.
  419  docker login
  420  docker images
  421  docker images | grep my
  422  docker images | grep site
  423  clear
  424  docker images | grep site
  425  set -o vi
  426  docker push of3jlmssoo/cloudsite_3_web:v1.0.
  427  pwd
  428  cd v2
  429  ls
  430  vi nginx-dep*
  431  vi web-dep*
  432  cd ..
  433  docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.0
  434  docker push of3jlmssoo/cloudsite_3_web:v1.0.0
  435  cd v2
  436  ls
  437  vi web-dep.yaml
  438  cat web-dep.yaml
  439  kubectl get all
  440  kubectl apply -f web-dep.yaml,web-svc.yaml
  441  kubectl get all
  442  ls
  443  cat nginx-dep*
  444  pwd
  445  kubectl create configmap confnginx --from-file=./mysite_nginx.conf
  446  kubectl get configmaps 
  447  kubectl describe  configmaps  confnginx
  448  kubectl apply -f nginx-deployment.yaml  
  449  kubectl get all
  450  clear
  451  kubectl get all
  452  clear & kubectl get all
  453  kubectl apply -f nginx_loadbalancer_service.yaml
  454  clear & kubectl get all
  455  dwkubectl kubectl exec -it pod/web-6694cd7775-x4jhk -- /bin/bash
  456  kubectl exec -it pod/web-6694cd7775-x4jhk -- /bin/bash
  457  history
container-labs$ 