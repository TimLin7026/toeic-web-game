import sqlite3
import json
import os

DB_PATH = 'toeic_vocab.db'
OUTPUT_DIR = 'data/books'

def export_database_to_json():
    # 建立輸出目錄
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. 取得所有教材
    cursor.execute("SELECT id, name FROM books")
    books = cursor.fetchall()

    books_list = []

    for book_id, book_name in books:
        # 2. 取得該教材的所有單元列表
        cursor.execute("""
            SELECT DISTINCT unit_number 
            FROM book_words 
            WHERE book_id = ?
            ORDER BY unit_number ASC
        """, (book_id,))
        units = [row[0] for row in cursor.fetchall()]

        books_list.append({
            "id": book_id,
            "name": book_name,
            "units": units
        })

        # 3. 針對每個單元，導出該單元的單字與例句
        for unit in units:
            cursor.execute("""
                SELECT w.id, w.word, w.meaning
                FROM words w
                JOIN book_words bw ON w.id = bw.word_id
                WHERE bw.book_id = ? AND bw.unit_number = ?
                ORDER BY w.id ASC
            """, (book_id, unit))
            words = cursor.fetchall()

            unit_words_data = []

            for word_id, word_text, meaning in words:
                # 取得該單字的 3 個例句
                cursor.execute("""
                    SELECT sentence_en, sentence_zh, sentence_index
                    FROM sentences
                    WHERE word_id = ?
                    ORDER BY sentence_index ASC
                """, (word_id,))
                sentences = cursor.fetchall()

                # 初始化預設空例句以防資料不齊全
                ex1_en, ex1_zh = "", ""
                ex2_en, ex2_zh = "", ""
                ex3_en, ex3_zh = "", ""

                for sen_en, sen_zh, sen_idx in sentences:
                    if sen_idx == 0:
                        ex1_en, ex1_zh = sen_en, sen_zh
                    elif sen_idx == 1:
                        ex2_en, ex2_zh = sen_en, sen_zh
                    elif sen_idx == 2:
                        ex3_en, ex3_zh = sen_en, sen_zh

                unit_words_data.append({
                    "id": word_id,
                    "word": word_text,
                    "meaning": meaning,
                    "mastered": False, # 前端預設未掌握
                    "ex1En": ex1_en,
                    "ex1Zh": ex1_zh,
                    "ex2En": ex2_en,
                    "ex2Zh": ex2_zh,
                    "ex3En": ex3_en,
                    "ex3Zh": ex3_zh
                })

            # 寫入單元 JSON 檔案 (例如: data/books/high_school_level_3_5_17.json)
            output_file_path = os.path.join(OUTPUT_DIR, f"{book_id}_{unit}.json")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                json.dump(unit_words_data, f, ensure_ascii=False, indent=4)
            print(f"Exported: {output_file_path} ({len(unit_words_data)} words)")

    # 4. 寫入教材目錄索引檔案
    books_list_path = 'data/books_list.json'
    with open(books_list_path, 'w', encoding='utf-8') as f:
        json.dump(books_list, f, ensure_ascii=False, indent=4)
    print(f"Exported directory index: {books_list_path}")

    conn.close()

if __name__ == '__main__':
    export_database_to_json()
