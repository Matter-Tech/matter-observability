#!/bin/bash
echo Setting env variables...
source .env
export $(cut -d= -f1 .env)
echo Done setting env variables.ls
