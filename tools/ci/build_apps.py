# SPDX-FileCopyrightText: 2026 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0
import os
import json
import sys
import subprocess

folders = set()
for root, dirs, files in os.walk('.'):
    if 'main' in dirs:
            folders.add(root)

failed = set()
for folder in folders:
    p = subprocess.run(['idf.py', '--ccache', 'build'], cwd=folder)
    if p.returncode != 0:
        failed.add(folder)

with open(os.getenv('GITHUB_STEP_SUMMARY'), 'a+') as f:
    if len(failed) > 0:
        f.write(f"# Failed builds ({len(failed)}):\n")
        for failed_dir in failed:
            f.write(f"- {failed_dir}\n")
        sys.exit(1)
    else:
        f.write(f"All {len(folders)} builds succeeded")
