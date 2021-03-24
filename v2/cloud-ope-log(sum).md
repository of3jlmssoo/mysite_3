414  git clone https://github.com/of3jlmssoo/mysite_3.git
  415  cd mysite_3
  417  docker-compose -f ./docker-compose.yml build
  418  docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.
  419  docker login
  420  docker images
  424  docker images | grep site
  433  docker tag mysite_3_web:latest of3jlmssoo/cloudsite_3_web:v1.0.0
  434  docker push of3jlmssoo/cloudsite_3_web:v1.0.0
  435  cd v2
  437  vi web-dep.yaml
                image: of3jlmssoo/cloudsite_3_web:v1.0.0
  440  kubectl apply -f web-dep.yaml,web-svc.yaml
  445  kubectl create configmap confnginx --from-file=./mysite_nginx.conf
  448  kubectl apply -f nginx-deployment.yaml  
  453  kubectl apply -f nginx_loadbalancer_service.yaml
  456  kubectl exec -it pod/web-6694cd7775-x4jhk -- /bin/bash
container-labs$ 