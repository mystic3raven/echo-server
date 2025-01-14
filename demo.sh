
# Tag the <img src="
docker tag flask-echo-server:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/flask-echo-server:latest

# push the image 
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/flask-echo-server:latest

# ECS Cluster Creation

aws ecs create-cluster --cluster-name flask-echo-cluster

# ECS Task Definition Creation
aws ecs register-task-definition --cli-input-json file://task-definition.json

# create  ECS Service
aws ecs create-service --cluster flask-echo-cluster --service-name flask-echo-service --task-definition flask-echo-task --desired-count 1 \


# verify the service
aws ecs describe-services --cluster flask-echo-cluster --services flask-echo-service

# describe the service

aws ecs describe-services --cluster flask-echo-cluster --services flask-echo-service

# get the public IP of the service
aws ecs list-tasks --cluster flask-echo-cluster
aws ecs describe-tasks --cluster flask-echo-cluster --tasks <TASK_ID>


# Access the service using the public IP
curl http://<PUBLIC_IP>:5000/echo



# Cleanup
aws ecs delete-service --cluster flask-echo-cluster --service flask-echo-service

# delete the cluster
aws ecs delete-cluster --cluster flask-echo-cluster

# Deregsiter the task definition
aws ecs deregister-task-definition --task-definition flask-echo-task


# Scale the ECS service to 3 tasks

aws ecs update-service --cluster flask-echo-cluster --service flask-echo-service --desired-count 3

# verify the scaling
aws ecs describe-services \
  --cluster flask-echo-cluster \
  --services flask-echo-service


# Scale the service down 
aws ecs update-service --cluster flask-echo-cluster --service flask-echo-service --desired-count 1

# Now we  didi the scaling up and down manually, we can use the ECS AutoScaling to scale the service based on the CPU utilization or the memory utilization


# Create Auto Scaling Policy
# aws application-autoscaling put-scaling-policy --service-namespace ecs --scalable-dimension ecs:service:DesiredCount --resource-id service/flask-echo-cluster/flask-echo-service --policy-name flask-echo-service-cpu-scaling --policy-type TargetTrackingScaling --target-tracking-scaling-policy-configuration file://scaling-policy.json

aws application-autoscaling register-scalable-target \
  --service-namespace ecs \
  --resource-id service/flask-echo-cluster/flask-echo-service \
  --scalable-dimension ecs:service:DesiredCount \
  --min-capacity 2 \
  --max-capacity 3

# Define the scaling policy
# aws application-autoscaling put-scaling-policy \
# --service-namespace ecs \
# --scalable-dimension ecs:service:DesiredCount \
# --resource-id service/flask-echo-cluster/flask-echo-service \
# --policy-name flask-echo-service-cpu-scaling \
# --policy-type TargetTrackingScaling \
# --target-tracking-scaling-policy-configuration file://scaling-policy.json

aws application-autoscaling put-scaling-policy \
  --service-namespace ecs \
  --resource-id service/flask-echo-cluster/flask-echo-service \
  --scalable-dimension ecs:service:DesiredCount \
  --policy-name cpu-utilization-scaling-policy \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration "{
    \"TargetValue\": 50.0,
    \"PredefinedMetricSpecification\": {
      \"PredefinedMetricType\": \"ECSServiceAverageCPUUtilization\"
    },
    \"ScaleInCooldown\": 60,
    \"ScaleOutCooldown\": 60
  }"


# Delete the scaling policy
aws application-autoscaling delete-scaling-policy \
  --service-namespace ecs \
  --resource-id service/flask-echo-cluster/flask-echo-service \
  --scalable-dimension ecs:service:DesiredCount \
  --policy-name cpu-utilization-scaling-policy


# Delete the ECS Service
aws ecs delete-service --cluster flask-echo-cluster --service flask-echo-service

# Delete the ECS Cluster
aws ecs delete-cluster --cluster flask-echo-cluster

# Deregister the Task Definition
aws ecs deregister-task-definition --task-definition flask-echo-task

# Delete the ECR Repository
aws ecr delete-repository --repository-name flask-echo-server --force
