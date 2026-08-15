import json
import os

HTML_PATH = 'index.html'
BOOKS_LIST_PATH = 'data/books_list.json'
BOOKS_DIR = 'data/books'

def inject_fallback():
    # 1. 讀取 books_list.json
    with open(BOOKS_LIST_PATH, 'r', encoding='utf-8') as f:
        books_list = json.load(f)

    # 2. 讀取每個單元的 JSON
    words_map = {}
    for book in books_list:
        book_id = book['id']
        for unit in book['units']:
            unit_file = os.path.join(BOOKS_DIR, f"{book_id}_{unit}.json")
            if os.path.exists(unit_file):
                with open(unit_file, 'r', encoding='utf-8') as f:
                    words_map[f"{book_id}_{unit}"] = json.load(f)
            else:
                print(f"Warning: {unit_file} not found.")

    # 3. 格式化為 JS 變數字串
    js_content = f"""// === FALLBACK DATA START ===
        const FALLBACK_BOOKS_LIST = {json.dumps(books_list, ensure_ascii=False, indent=8)};
        const FALLBACK_WORDS_MAP = {json.dumps(words_map, ensure_ascii=False, indent=8)};
        // === FALLBACK DATA END ==="""

    # 4. 讀取並替換 index.html
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()

    start_tag = '// === FALLBACK DATA START ==='
    end_tag = '// === FALLBACK DATA END ==='

    start_idx = html_content.find(start_tag)
    end_idx = html_content.find(end_tag)

    if start_idx == -1 or end_idx == -1:
        print("Error: Fallback placeholders not found in index.html.")
        return

    # 包含結尾標籤
    end_idx_total = end_idx + len(end_tag)

    new_html = html_content[:start_idx] + js_content + html_content[end_idx_total:]

    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"Successfully injected fallback data into {HTML_PATH}!")

if __name__ == '__main__':
    inject_fallback()
