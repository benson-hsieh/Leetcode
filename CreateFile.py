import os
from datetime import datetime

def create_new_problem():
    print("--- 🆕 LeetCode New Note Generator ---")
    
    # 1. 詢問題目資訊
    category = input("請輸入題目類別 (例如 Tree, Array): ").strip()
    difficulty = input("請輸入難度 (Easy, Medium, Hard): ").strip()
    # 格式建議: 100. Same Tree
    raw_title = input("請輸入 題號. 題目 (例如 100. Same Tree): ").strip()

    # 2. 處理檔名
    # 產生的檔名格式: [Easy] 100. Same Tree.md
    file_name = f"[{difficulty}] {raw_title}.md"
    
    # 自動產生 LeetCode 連結 (將 "100. Same Tree" 轉為 "same-tree")
    title_part = raw_title.split('.', 1)[-1].strip()
    title_slug = title_part.lower().replace(' ', '-')
    lc_link = f"https://leetcode.com/problems/{title_slug}/description/"

    # 3. 確保資料夾存在
    if not os.path.exists(category):
        os.makedirs(category)
        print(f"📁 已建立新資料夾: {category}")

    file_path = os.path.join(category, file_name)

    # 4. 定義 Markdown 模板內容
    # 注意：這裡結尾一定要有 """
    today = datetime.now().strftime("%Y-%m-%d")
    
    template = (
        f"| Category | {category} |\n"
        f"| :--- | :--- |\n"
        f"| **Subcategory** | |\n"
        f"| **Title** | [{raw_title}]({lc_link}) |\n"
        f"| **Date** | {today} |\n"
        f"| **Difficulty** | {difficulty} |\n"
        f"| **Status** | Accepted |\n"
        f"\n---\n\n"
        f"## Description\n\n"
        f"## Approach\n\n"
        f"## Complexity Analysis\n"
        f"* **Time Complexity**: \n"
        f"* **Space Complexity**: \n"
        f"\n---\n\n"
        f"## Solution (Java)\n"
        f"```java\n\n"
        f"```\n"
    )

    # 5. 寫入檔案
    if os.path.exists(file_path):
        print(f"⚠️ 檔案已存在: {file_path}，已取消。")
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"✅ 成功建立: {file_path}")

if __name__ == "__main__":
    create_new_problem()