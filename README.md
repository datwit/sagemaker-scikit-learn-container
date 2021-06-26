# Custom Sagemaker SKLean image

This version include `spacy`, `gensim` and `nltk`

## How to create the image

- Make any change necesary to the requirements or dependencies in `requirements.txt`
- Create a SageMaker notebook instance
  - Use a instance type of `ml.m5.xlarge` or superior.
  - In **IAM Role** create a new one or reuse any of the `AmazonSageMaker-ExecutionRole-YYYYMMDDTHHmmSS`, in any case copy it for later.
  - For Root Access, choose Enable
  - After the status of the notebook instance changes to InService, choose Open JupyterLab
- Open a new terminal, clone this repository and run the script

  ```sh
  get clone https://github.com/datwit/sagemaker-scikit-learn-container
  cd sagemaker-scikit-learn-container
  ./upload-custom-image.sh
  ```

  :warning: **Note**
  This bash shell script may raise a permission issue similar to the following error message:

  ```txt
  "denied: User: [ARN] is not authorized to perform:ecr:InitiateLayerUpload on resource:arn:aws:ecr:us-east-1:[id]:repository/.."
  ```

  If this error occurs, you need to attach the **AmazonEC2ContainerRegistryFullAccess** policy to your IAM role. Go to the [IAM console](https://console.aws.amazon.com/iam/home), choose **Roles** from the left navigation pane, look up the IAM role you used for the Notebook instance. Under the **Permission** tab, choose the **Attach policies** button, and search the **AmazonEC2ContainerRegistryFullAccess** policy. Mark the check box of the policy, and choose **Attach policy** to finish.

After you push the container, you can call the Amazon ECR image from anywhere in the SageMaker environment. For example

```python
import boto3

account_id = boto3.client('sts').get_caller_identity().get('Account')
ecr_repository = 'custom-sklearn'
tag = ':0.23-1-cpu-py3'

region = boto3.session.Session().region_name

uri_suffix = 'amazonaws.com'
if region in ['cn-north-1', 'cn-northwest-1']:
    uri_suffix = 'amazonaws.com.cn'

image_uri = '{}.dkr.ecr.{}.{}/{}'.format(account_id, region, uri_suffix, ecr_repository + tag)

# image_uri should contain something like
# 111122223333.dkr.ecr.us-east-2.amazonaws.com/custom-sklearn:0.23-1-cpu-py3
```

See original README in https://github.com/aws/sagemaker-scikit-learn-container
