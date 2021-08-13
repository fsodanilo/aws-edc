import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

'''
s3_client.download_file("datalake-brx-edc", 
                        "data/AC2016.7Z", 
                        "aws-edc/data/AC2016.7Z")

df = pd.read_csv("RR2015.csv", sep=';')
print(df.head(10))
'''
s3_client.upload_file("aws-edc/data/RR2016.7Z",
                    "datalake-brx-edc",
                    "data/teste")

print("upload concluido")