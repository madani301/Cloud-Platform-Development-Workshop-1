#!/usr/local/bin/python3

"""

This script was made by Madani Napaul. 

Please use this only as a reference while working on your Cloud Platform
Development Coursework. 

Most of the material here are from AWS Documentations. Go to AWS Documentations
for further information. 

Thank you!

"""
# Import the required libraries
import json
import boto3

# This is the function which is executed when Lambda is triggered
def lambda_handler(event, context):

    # Create the S3 resource or client here, depending on your usage
    s3_client = boto3.resource("s3")

    # Load the message from SQS by reading the content under 'Records'
    # 'body' contains all the useful information about the file(s) uploaded in S3
    # json.loads() is used to parse a valid JSON string and convert it into a Python Dictionary
    for msg in event["Records"]:
        msg_payload = json.loads(msg["body"])

        # Start this part only if the message from SQS has content
        if "Records" in msg_payload:

            # Use the fist index of 'Records' to access the list S3 dict
            # Extract the bucket name from the dict and the key which is the file's name
            bucket = msg_payload["Records"][0]["s3"]["bucket"]["name"]
            key = msg_payload["Records"][0]["s3"]["object"]["key"].replace("+", " ")

            # Create an empty dict which we will later use to append the data we require
            result = []

            # Access the files in the S3 Bucket by specifying the bucket's name and file's name
            # The data for each file in the specified bucket is read and stored in the variable 'content'
            obj = s3_client.Object(bucket, key)
            content = obj.get()["Body"].read().decode("utf-8")

            # We prepare the data we read from above to output to a file or store in a database
            file_details = {"File_Content": str(content)}

            # From the empty result dictionary above, we append the data we prepared from the step before
            # Now the data is ready to be stored in the database in the format we specified
            result.append(file_details)

            # Create the resource for dynamodb and set the table in which we want to store the data
            # File_Name here is the primary key we declared whilst creating the table, and it's required
            # 'Body' contains the content which belong to that primary key
            table = boto3.resource("dynamodb").Table("dynamodb-cpd-2021")
            table.put_item(Item={"File_Name": key, "Body": result})