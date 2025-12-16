#!/usr/bin/env python3
"""
Clear corrupted Hugging Face cache before server starts
"""
import os
import shutil
import sys

def clear_transformers_cache():
    """Remove ALL Hugging Face and transformers cache"""
    cache_dirs = [
        os.path.expanduser("~/.cache/huggingface"),
        os.path.expanduser("~/.cache/torch"),
        os.path.expanduser("~/.cache/pip"),
        "/tmp/.cache/huggingface",
        "/tmp/.cache/torch",
        "/tmp/clip_temp",
        "/root/.cache/huggingface",
        "/root/.cache/torch",
        "/root/.cache/pip"
    ]
    
    print("=" * 60, file=sys.stderr)
    print("CLEARING ALL MODEL CACHES (prevents corruption)", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    
    cleared = 0
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            try:
                print(f"Removing {cache_dir}...", file=sys.stderr)
                shutil.rmtree(cache_dir)
                print(f"✓ Cleared {cache_dir}", file=sys.stderr)
                cleared += 1
            except Exception as e:
                print(f"✗ Failed to clear {cache_dir}: {e}", file=sys.stderr)
    
    if cleared == 0:
        print("No caches found to clear (fresh start)", file=sys.stderr)
    else:
        print(f"✓ Cleared {cleared} cache directories", file=sys.stderr)
    
    print("=" * 60, file=sys.stderr)
    print("Cache clearing complete. Models will download fresh.", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

if __name__ == "__main__":
    clear_transformers_cache()
