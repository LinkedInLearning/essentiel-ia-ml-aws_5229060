# [Choice] Ubuntu version (use ubuntu-22.04 or ubuntu-18.04 on local arm64/Apple Silicon): ubuntu-22.04, ubuntu-20.04, ubuntu-18.04
ARG VARIANT=ubuntu-24.04
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

COPY requirements.txt /tmp/pip-tmp/

# Ensure the package lists are updated
# Add deadsnakes PPA and install Python 3.11
# Install build-essential and dependencies for Python package compilation
# Install system dependencies for Python


RUN apt-get update && apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:deadsnakes/ppa && \
  apt-get update && \
  apt-get install -y python3.10 python3.10-venv python3.10-dev python3-pip



# Upgrade pip to ensure it's the latest version

RUN python3.10 -m ensurepip --upgrade
RUN python3.10 -m pip install --upgrade pip
RUN python3.10 -m pip install html5lib
# Install your requirements
RUN python3.10 -m pip install -r /tmp/pip-tmp/requirements.txt
RUN ln -sf $(which python3.10) /usr/local/bin/python


RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install

RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

