#!/usr/bin/env python3
"""
Clear corrupted Hugging Face cache before server starts
"""
import os
import shutil
import sys

def clear_transformers_cache():
    """Remove corrupted CLIP model cache"""
    cache_dirs = [
        os.path.expanduser("~/.cache/huggingface"),
        os.path.expanduser("~/.cache/torch"),
        "/tmp/.cache/huggingface",
        "/tmp/.cache/torch"
    ]
    
    print("Clearing Hugging Face cache to fix corruption...", file=sys.stderr)
    
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            try:
                print(f"Removing {cache_dir}...", file=sys.stderr)
                shutil.rmtree(cache_dir)
                print(f"✓ Cleared {cache_dir}", file=sys.stderr)
            except Exception as e:
                print(f"Warning: Could not clear {cache_dir}: {e}", file=sys.stderr)
    
    print("Cache cleared. Models will be re-downloaded fresh.", file=sys.stderr)

if __name__ == "__main__":
    clear_transformers_cache()
