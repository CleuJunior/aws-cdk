from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    CfnOutput, Fn
)
from constructs import Construct


class PyStarterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = s3.Bucket(self, "PyBucket",
                           bucket_name=f"variant-name-{self.__initialize_suffix}",
                           lifecycle_rules=[
                               s3.LifecycleRule(
                                   expiration=Duration.days(30)
                               )
                           ])
        CfnOutput(self, "PyBucketName", value=bucket.bucket_name)

    def __initialize_suffix(self) -> str:
        short_stack_id = Fn.select(2, Fn.split('/', self.stack_id))
        return Fn.select(4, Fn.split('-', short_stack_id))
