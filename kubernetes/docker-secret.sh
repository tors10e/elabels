# MIT License
#
# Copyright (c) 2016 Samuel Rounce
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#For windows you can simply run a modified version of this on the cmd prompt:
# kubectl create secret docker-registry vessel-energy-secret --docker-server "https://gcr.io" --docker-username _json_key --docker-email not@val.id --docker-password=C:\Users\torsten\Downloads\vesselenergy.json

#!/usr/bin/env sh

SPATH="$(cd $(dirname "$0") && pwd -P)"
DEFAULT_SECRET_NAME=docker-registry-secret
DEFAULT_CONFIG_PATH=$SPATH/localkube.json


usage() {
  cat <<EOF
Usage: docker-secret.sh [secret name] [service account key] [arguments ...]

  secret name - The name of the ImagePullSecret to be created
    (default: ${DEFAULT_SECRET_NAME})
  service account key - The path to your GCP service account JSON keyfile
    (default: ${DEFAULT_CONFIG_PATH})
  arguments - Additional arguments to be passed to kubectl
EOF
}

if [  $# -le 1 ]
then
  usage
  exit 1
fi

if [[ ( $# == "--help") ||  $# == "-h" ]]
then
  usage
  exit 0
fi

SECRET_NAME=${1:-$DEFAULT_SECRET_NAME}
CONFIG_PATH=${2:-$DEFAULT_CONFIG_PATH}
if [[ ! -f $CONFIG_PATH ]]; then
  echo "Unable to locate service account config JSON: $CONFIG_PATH";
  exit 1;
fi

kubectl create secret docker-registry $SECRET_NAME  \
  --docker-server "https://gcr.io" \
  --docker-username _json_key \
  --docker-email not@val.id \
  --docker-password="`cat $CONFIG_PATH`" ${@:3}
