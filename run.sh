#!/bin/bash

if [ -z $PORT ]; then
    export PORT=5000
fi

uvicorn app.main:app --port $PORT --reload