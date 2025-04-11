import streamlit as st
import boto3
import json

st.title("Shakespeare LLM Generator 🎭")
user_input = st.text_input("Enter a prompt:", "To be or not to be")

if st.button("Generate"):
    runtime = boto3.client('sagemaker-runtime')

    response = runtime.invoke_endpoint(
        EndpointName='your-endpoint-name',
        ContentType='application/json',
        Body=json.dumps({'inputs': user_input})
    )

    result = response['Body'].read().decode()
    st.markdown(f"**Generated Text:**\n\n{result}")