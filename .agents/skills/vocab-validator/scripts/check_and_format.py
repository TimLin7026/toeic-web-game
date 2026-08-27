# -*- coding: utf-8 -*-
import json
import os
import sys

def check_and_format_json(file_path):
    print(f"[*] 正在開始檢測檔案: {file_path}")
    if not os.path.exists(file_path):
        print(f"[!] 錯誤: 找不到指定的檔案: {file_path}")
        return False
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[!] 錯誤: JSON 解析失敗: {e}")
        return False

    if not isinstance(data, list):
        print("[!] 錯誤: JSON 根節點必須是 Array 列表格式！")
        return False

    issues_found = 0
    formatted_data = []

    for idx, item in enumerate(data):
        word = item.get("word", "unknown")
        
        # 1. 檢查並處理 id
        if "id" not in item:
            item["id"] = idx + 1
            
        # 2. 檢查 part_of_speech 詞性
        pos = item.get("part_of_speech", "").strip()
        if not pos:
            print(f"[?] 提示: 單字 '{word}' (ID: {item['id']}) 缺少 'part_of_speech' 詞性標記。")
            issues_found += 1
            item["part_of_speech"] = "unknown"
            
        # 3. 檢查 meaning
        if not item.get("meaning", "").strip():
            print(f"[!] 警告: 單字 '{word}' (ID: {item['id']}) 缺少 'meaning' 中文釋義！")
            issues_found += 1

        # 4. 檢查 examples 例句數量是否為 5 句
        examples = item.get("examples", [])
        if not isinstance(examples, list):
            print(f"[!] 錯誤: 單字 '{word}' 的 examples 必須是 Array 格式！")
            examples = []
            issues_found += 1
            
        if len(examples) != 5:
            print(f"[!] 警告: 單字 '{word}' (ID: {item['id']}) 的例句數量為 {len(examples)} 句 (標準為 5 句)！")
            issues_found += 1
            
        cleaned_examples = []
        for ex_idx, ex in enumerate(examples):
            if isinstance(ex, dict):
                # 相容並自動轉換 english -> en, chinese -> zh 鍵名
                en_val = ex.get("en", ex.get("english", "")).strip()
                zh_val = ex.get("zh", ex.get("chinese", "")).strip()
                if en_val and zh_val:
                    cleaned_examples.append({"en": en_val, "zh": zh_val})
                    continue
            print(f"[!] 錯誤: 單字 '{word}' 第 {ex_idx + 1} 句例句格式不合規 (需包含 en 與 zh)。")
            issues_found += 1
            cleaned_examples.append(ex)
        examples = cleaned_examples

        # 5. 標準化屬性排序: id, word, part_of_speech, meaning, examples
        sorted_item = {
            "id": item["id"],
            "word": item["word"],
            "part_of_speech": item.get("part_of_speech", "unknown"),
            "meaning": item.get("meaning", ""),
            "examples": examples
        }
        formatted_data.append(sorted_item)

    # 寫回格式化後的 JSON 檔案
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(formatted_data, f, ensure_ascii=False, indent=4)
        print(f"[+] 格式化與標準化完成！成功寫回檔案: {file_path}")
    except Exception as e:
        print(f"[!] 錯誤: 寫入檔案失敗: {e}")
        return False

    if issues_found > 0:
        print(f"[i] 檢測完成。共發現 {issues_found} 處需要注意或補全的格式/內容問題（已盡可能自動修復架構與排序）。")
        return False
    else:
        print("[+] 檢測完成！所有單字格式合規，詞性完整，例句均足額 5 句！")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用說明: python check_and_format.py <JSON檔案路徑>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    success = check_and_format_json(target_file)
    sys.exit(0 if success else 1)
