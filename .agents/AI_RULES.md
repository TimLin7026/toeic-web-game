# AI 思考與呈現行為守則 (AI Thinking & Presentation Rules)

本專案開發中，AI 助理必須嚴格遵守以下思考、呈現與溝通協定：

## 1. 語言與呈現風格 (Communication Style)
* **全程使用繁體中文**進行溝通、分析與說明（程式碼與變數命名除外）。
* **詳盡說明，拒絕偷懶**：在提出方案或執行動作前，必須像資深工程師一樣，清晰說明技術原理、底層機制、可能遭遇的框架陷阱（例如 Streamlit 的 Widget 重置與 Rerun 順序機制），並列出變更影響範圍。
* **格式化輸出**：使用清晰的 Markdown 標題、GitHub 警示區塊（> [!IMPORTANT], > [!WARNING]）及流程圖（Mermaid Diagram）來輔助呈現複雜的邏輯與架構。

## 2. 雙重防線與對齊工作流 (Two-Phase Safety Process)
每次實作前，必須採用以下雙重確認：
* **第一步 (計畫對齊)**：先撰寫或更新 `implementation_plan.md`，說明技術方案大方向與底層邏輯，等待使用者確認。
* **第二步 (任務對齊)**：在動手修改任何程式碼前，必須建立並展示細緻的 `task.md` 任務 TODO 清單。
* **第三步 (動工)**：使用者回覆「同意實作」或「開始動工」後，才能動手。

## 3. 不編碼與物理備份原則 (No-Code & Backup Policy)
* **不編碼指令**：當使用者提到「不編碼」或尚未明確授權實作時，AI **絕對不能**改動任何程式碼，僅限於唯讀分析與討論。
* **修改前物理備份**：在任何程式碼實作修改前，必須對受影響的檔案進行物理複製備份，備份檔名必須加上精確的時間戳（如 `Filename_20260731_120000.py`），且絕不能覆蓋已有的備份。
* **實體備份存檔**：當使用者要求「保存 plan task」時，必須將當前未完成的計畫與任務清單複製寫入至 `.agents/NEXT_PLAN.md` 與 `.agents/NEXT_TASK.md`，確保下次會話可直接接軌。

## 4. 程式碼變更與品質控制 (Code Change Policy)
* **最小改動原則**：僅修改與任務直接相關的代碼，不影響無關區塊。
* **防錯驗證**：修改完成後，主動檢查語法與縮進，並向使用者報告修改點與驗證方式。

## 5. 工具調用日誌中文晶片 (Worked Trace Localization)
* **強制 Worked 歷程繁中化**：在呼叫任何工具（如 `view_file`, `replace_file_content`, `run_command`, `write_to_file` 等）時，傳入的 **`toolSummary`** 與 **`toolAction`** 參數必須**百分之百使用繁體中文**填寫。
  * *正確範例*：
    * `toolSummary` = "檢查資料庫欄位" 或 "修復 Rerun 排序"
    * `toolAction` = "唯讀檢視 sentinel_db.py 結構" 或 "熱替換 Stock_Sentinel.py 的 merge 區塊"
  * *錯誤範例*（絕對禁止）：
    * `toolSummary` = "View db file" 或 "Edit python file"
