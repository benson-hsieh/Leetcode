#!/bin/bash

# 1. 執行 Python 腳本產生目錄
python Generation.py

# 2. 自動化 Git 上傳流程
git add .
git commit -m "update: leetcode notes $(date +'%Y-%m-%d')"
git push origin main

echo "Done! 資料已同步至 GitHub。"
read -p "按任意鍵結束..."