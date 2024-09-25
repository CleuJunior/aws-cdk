#!/usr/bin/env python3

import aws_cdk as cdk

from py_starter.py_handler_stack import PyHandlerStack
from py_starter.py_starter_stack import PyStarterStack

app = cdk.App()

starter_stack = PyStarterStack(app, "PyStarterStack")
PyHandlerStack(app, "PyHandlerStack", bucket=starter_stack.cool_bucket)

app.synth()
