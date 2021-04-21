# CPD Coursework Prep | Madani Napaul

## Content 

### 1. Introduction

Welcome to this Cloud Platform Development's Coursework Prep! We are exciting to have you here, and hope that you find    
this relevant and insightful for the courseork. 

We assumed you already set up your AWS Account and have your environment set up while creating this coursework prep.     
Additionally, we will not be covering IAM Roles & Policies. Please refer to the AWS Documentations for further information     
regarding policies for each function. Ensure you are using the most restrictive policies and roles. 

### 2. Creating an S3 Bucket with Python3

In this section, we will write a script in Python3 which will create an S3 Bucket. Ensure you have your environment set up     
with your credentials, or specify your credentials within the script (Not recommended). 

This bucket will be used to upload the '.txt' files later on, and SQS will be notified every time a file with the '.txt'     
suffix is uploaded. 

### 3. Creating an SQS Queue with Python3

In this section, we will create a script in Python3 which create the SQS Queue. The queue will be notified whenever a new     
'.txt' file is uploaded in S3. A lambda function will be triggered to capture the relevant data from the response (for e.g,     
the file name).

Appropriate access policies should be attached to allow SQS to receive notifications from S3, as well trigger Lambda. 

### 4. Setting S3 Event Notification 

Once the SQS Queue has been set up with the appropriate access policies, we will set up an 'Event Notification' in S3.      
This will send a notification every time we upload a '.txt' file in S3. We will configure the event notification only for PUT. 

### 5. Uploading '.txt' files to S3 with Python3

In this section, we will write a script which can iterated through '.txt' files in a local directory on your machine. Each '.txt'     
file will be uploaded to the specified S3 bucket. 

### 6. Creating a table in DynamoDB with Python3

In this section, we will write a script to create a table in DynamoDB which will be later used to store relevant data from the     
'.txt' files uploaded in S3. 

### 7. Building a Lambda function with Boto3

In this section, we will create a Lambda function which will be trigged by the SQS Queue to:

* Read the response from the SQS Queue
* Extract relevant data from the response 
* Read the data from the file names returned in the SQS response
* Manipulate and prepare the data to be stored in the DynamoDB Table 

## Author 

This tutorial was created by Madani Napaul. I hope you find it useful. 

Feel free to reach out to me if you have any questions, or comment your questions below. Thank you Yovin Poorun for    
providing me with the opportunity to create this tutorial. 

Cheers & Happy Coding!
