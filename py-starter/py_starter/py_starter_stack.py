from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    CfnOutput
)
from constructs import Construct


class PyStarterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = s3.Bucket(self, "PyBucket", lifecycle_rules=[
            s3.LifecycleRule(
                expiration=Duration.days(30)
            )
        ])
        CfnOutput(self, "PyBucketName", value=bucket.bucket_name)
