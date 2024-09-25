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
        self.bucket = s3.Bucket(self, "PyBucket", lifecycle_rules=[
            s3.LifecycleRule(
                expiration=Duration.days(30)
            )
        ])
        CfnOutput(self, "PyBucketName", value=self.bucket.bucket_name)

    def __initialize_suffix(self) -> str:
        short_stack_id = Fn.select(2, Fn.split('/', self.stack_id))
        return Fn.select(4, Fn.split('-', short_stack_id))

    @property
    def cool_bucket(self):
        return self.bucket
