#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import {TsStarterStack} from '../lib/ts-starter-stack';
import {TsHandlerStack} from "../lib/ts-handler-stack";

const app = new cdk.App();
const tsStack = new TsStarterStack(app, 'TsStarterStack');
new TsHandlerStack(app, 'TsHandlerStack', {
    coolBucket: tsStack.coolBucket
});