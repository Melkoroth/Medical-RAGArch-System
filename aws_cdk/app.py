
#!/usr/bin/env python3
import aws_cdk as core
from cdk_stack import MedicalRAGArchStack

app = core.App()
MedicalRAGArchStack(app, "MedicalRAGArchStack")
app.synth()
