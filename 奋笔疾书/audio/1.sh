#!/bin/bash

# 遍历当前目录下的所有文件
for file in *; do
    # 检查是否为普通文件
    if [ -f "$file" ]; then
        new_file="${file//_/ }"
        mv "$file" "$new_file"
    fi
done
