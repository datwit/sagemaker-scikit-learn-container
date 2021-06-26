#!/bin/sh

account=$(aws sts get-caller-identity --query Account --output text)

# Get the region defined in the current configuration (default to us-west-2 if none defined)
region=$(aws configure get region)
region=${region:-us-west-2}

fullname="${account}.dkr.ecr.${region}.amazonaws.com/custom-sklearn:0.23-1-cpu-py3"

# If the repository doesn't exist in ECR, create it.

aws ecr describe-repositories --repository-names custom-sklearn > /dev/null 2>&1
if [ $? -ne 0 ]
then
aws ecr create-repository --repository-name custom-sklearn > /dev/null
fi

# Get the login command from ECR and execute it directly

$(aws ecr get-login --region ${region} --no-include-email)

# Build the docker image locally with the image name and then push it to ECR
# with the full name.
docker build -t sklearn-base:0.23-1-cpu-py3 -f docker/0.23-1/base/Dockerfile.cpu .
docker build -t custom-sklearn:0.23-1-cpu-py3 -f docker/0.23-1/final/Dockerfile.cpu .
docker tag custom-sklearn:0.23-1-cpu-py3 ${fullname}

docker push ${fullname}
