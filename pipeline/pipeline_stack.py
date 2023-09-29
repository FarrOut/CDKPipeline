from aws_cdk import (
    # Duration,
    Stack,pipelines,
    # aws_sqs as sqs,
)
from constructs import Construct

class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = pipelines.CodePipeline(self, "Pipeline",
            synth=pipelines.ShellStep("Synth",
                # Use a connection created using the AWS console to authenticate to GitHub
                # Other sources are available.
                input=pipelines.CodePipelineSource.git_hub("FarrOut/CDKPipeline", "main"),

                commands=["pip install -r requirements.txt", "npm install -g aws-cdk", "cdk synth"]
            )
        )
