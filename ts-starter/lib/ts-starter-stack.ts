import * as cdk from 'aws-cdk-lib';
import {aws_s3, Fn} from 'aws-cdk-lib';
import {Construct} from 'constructs';

export class TsStarterStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const bucket = new aws_s3.Bucket(this, "TsBucket", {
            bucketName: this.suffix(),
            lifecycleRules: [
                {
                    expiration: cdk.Duration.days(45)
                }

            ]
        })

        new cdk.CfnOutput(this, "TsBucketName", {
            value: bucket.bucketName
        })
    }

    private suffix(): string {
        const shortStackId = Fn.select(2, Fn.split('/', this.stackId))
        return Fn.select(4, Fn.split('-', shortStackId))
    }
}
