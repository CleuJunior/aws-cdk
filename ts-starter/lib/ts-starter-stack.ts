import * as cdk from 'aws-cdk-lib';
import {aws_s3} from 'aws-cdk-lib';
import {Construct} from 'constructs';

export class TsStarterStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        new aws_s3.Bucket(this, "TsBucket", {
            lifecycleRules: [
                {
                    expiration: cdk.Duration.days(45)
                }
            ]
        })

    }
}
