#!/bin/bash
#
export LLAMA_CPP_LIB=$(pwd)/venv/lib/python3.10/site-packages/llama_cpp_cuda/libllama.so
export LD_LIBRARY_PATH=$(pwd)/venv/lib/python3.10/site-packages/nvidia/cuda_runtime/lib:/home/llanphar/src/mallhark/venv/lib/python3.10/site-packages/nvidia/cublas/lib:$LD_LIBRARY_PATH

echo $LD_LIBRARY_PATH

gradio server.py
