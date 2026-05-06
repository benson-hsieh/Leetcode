import os

def generate_guide():
    # 1. 設定排除資料夾
    exclude = ['.git', '.github', '_image', '.vscode', '__pycache__']
    output_file = "README.md" # 根據你的截圖，你目前是直接更新 README
    
    table_rows = []
    seen_ids = set() # 【新增】用來記錄已經處理過的題號
    
    # 2. 遍歷資料夾
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude and d != "Tree" and not d.startswith('.')]
        category = os.path.basename(root)
        
        for file in files:
            if file.endswith(".md") and file not in ["README.md", "LEETCODE_GUIDE.md"]:
                try:
                    # 解析檔名格式: [Difficulty] ID. Title
                    name = file.replace(".md", "")
                    diff = name.split(']')[0].replace('[', '').strip()
                    rest = name.split(']')[1].strip()
                    prob_id_str = rest.split('.')[0].strip()
                    prob_id = int(prob_id_str) # 轉成整數方便排序與檢查
                    title = rest.split('.')[1].strip()
                    
                    # 【新增】重複檢查邏輯
                    if prob_id in seen_ids:
                        print(f"ℹ️ 跳過重複題號: {prob_id} ({category})")
                        continue
                    seen_ids.add(prob_id)
                    
                    # 【修正】超連結路徑處理
                    # 資料夾名稱 (category) 和 檔案名稱 (file) 都要處理空白鍵
                    safe_category = category.replace(' ', '%20')
                    safe_file = file.replace(' ', '%20')
                    path = f"./{safe_category}/{safe_file}"
                    
                    row = f"| {prob_id} | {title} | {diff} | {category} | [View]({path}) |"
                    table_rows.append((prob_id, row))
                except Exception as e:
                    # 如果格式不符就跳過
                    continue

    # 3. 按題號排序
    table_rows.sort(key=lambda x: x[0])
    
    # 4. 寫入檔案
    header = "# LeetCode Master Guide\n\n| # | Title | Difficulty | Category | Note |\n| :--- | :--- | :--- | :--- | :--- |\n"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header + "\n".join([r[1] for r in table_rows]))
            
    print(f"✅ 已更新 {len(table_rows)} 題至 {output_file}")

if __name__ == "__main__":
    generate_guide()