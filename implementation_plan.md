# 多益英文自主學習網頁遊戲 — 專案實作計畫 (Implementation Plan)

## 一、 專案概述 (Project Overview)
本專案為一款多益（TOEIC）英文自主學習與測驗網頁遊戲，採用 RWD 響應式介面設計，能直接部署於免費平台（如 GitHub Pages）。

---

## 二、 系統架構與技術選型 (System Architecture)

```
[前端界面 Front-end] (HTML5 / CSS3 / Vanilla JS - SPA 單頁應用)
       │
       ├── 1. 玩家登入介面 (Login) ──── 儲存名稱至 LocalStorage
       ├── 2. 單字自主學習區 (Vocab) ── 語意介紹、Web Speech TTS 發音、中/英UI切換
       ├── 3. 閱讀文章練習區 (Reading) ─ 全文TTS朗讀、中文翻譯開關切換
       └── 4. 全英文測驗區 (Quiz) ───── 克漏字選擇題 (10抽5)、閱讀理解題 (5題)
       
[資料庫與狀態管理 Database & State]
       └── 內建 JSON 結構 (10組單字庫、10題克漏字題庫、2篇閱讀文章與10題閱讀選擇題)
```

---

## 三、 功能模組詳細規範 (Detailed Functional Specs)

### 1. 登入模組 (Login System)
- **玩家名稱輸入**：支援自訂名稱，並永久記憶於瀏覽器 `localStorage`。
- **快速進入**：無須伺服器驗證，實現免帳號純前端流暢體驗。

### 2. 單字自主學習模組 (Vocabulary Learning)
- **資料庫規模**：預設 10 組多益核心單字（例如：*analyze*, *strategy*, *innovative*, *negotiate* 等）。
- **互動功能**：
  - 展示詞性（POS）、英文釋義與中文定義。
  - 整合 **Web Speech API (`window.speechSynthesis`)**，提供單字與例句標準美式英語語音發音。
  - 支援 **中/英文介面即時切換**。

### 3. 閱讀文章練習模組 (Reading Practice)
- **文章數量**：預設 2 篇多益短文（主題：科技研討會、全球供應鏈）。
- **互動功能**：
  - 提供全文 **Web Speech API 語音朗讀**。
  - 提供 **「顯示中文翻譯」開關 (Toggle Switch)**，可依學習需求開關中文比對。

### 4. 全英文測驗模組 (Full-English Quiz Engine)
- **單字克漏字測驗**：
  - 題庫池：10 題多益單字克漏字選擇題。
  - 抽題機制：每次測驗**隨機抽取 5 題**。
  - 呈現方式：全英文題幹、上下文語境與選項 (A/B/C/D)。
- **閱讀理解測驗**：
  - 抽題機制：**一次隨機選擇 1 篇文章**。
  - 題目規模：配合文章提供 5 題全英文閱讀理解選擇題。
  - 即時結算：測驗結束後即時顯示得分（滿分 100）與重測按鈕。

---

## 四、 檔案目錄與備份策略 (Directory & Backup Strategy)

### 1. 專案目錄結構
`d:\工具開發區\多益網頁遊戲專案\`
- 📄 `index.html` （主要可執行網頁程式碼）
- 📝 `implementation_plan.md` （專案實作計畫書）
- 📝 `README_專案說明文件`
- 📁 `bak/` （版本備份資料夾）
  - 📄 `index_old_202608061629.html`

### 2. 版本備份與版控機制 (Version Backup & Git Control Policy)
- **Git 版本控制**：本專案採用 Git 進行本機版本控制，所有功能階段性開發完成後，均須進行 Commit 記錄。
- **自動實體備份原則**：凡更新 `index.html` 程式碼時，除了 Git 提交外，系統會先將前一版本複製移動至 `bak/` 資料夾，做為雙重保險。
- **命名規範**：`*_YYYYMMDDHHMM.html`（例如：`index_202608061830.html`）。

---

## 五、 開發里程碑與時程 (Milestones & Roadmap)

| 里程碑 (Milestone) | 內容說明 (Scope) | 狀態 (Status) |
| :--- | :--- | :---: |
| **Phase 1: 原型機制驗證** | 五大學習理論（Leitner、i+1、翻轉學習、損失規避、家族樹）測試 | 已完成 |
| **Phase 2: 簡化架構與 UI 重構** | 登入介面、單字區、閱讀區、全英文 5 題測驗區、中/英切換 | 已完成 |
| Phase 2.5: GitHub Pages 部署與相容性檢查 | 檢查 `index.html` 靜態部署相容性，並編寫跨平台操作手冊 | 已完成 |
| **Phase 2.6: XS 窄螢幕 RWD 行動端適配優化** | 修正極小螢幕（如 iPhone XS / SE）下按鈕與單字卡片撐寬跑版問題 | 已完成 |
| **Phase 2.7: 單字發音按鈕佈局微調** | 將單字「發音」按鈕由右上角調整至緊跟在單字與詞性的後方 | 已完成 |
| **Phase 2.8: 整合新版代碼檔案** | 備份並使用 `code_artifact.html` 取代舊的 `index.html` | **進行中 (本次任務)** |
| **Phase 3: 自動化時事文章擴充** | GitHub Actions 定時抓取新聞 RSS，經 Python 標註自動更新題庫 | 規劃中 |
| **Phase 4: 音效與數據持久化** | 加入遊戲音效、成就徽章與歷次測驗分數歷史紀錄圖表 | 規劃中 |

---

## 六、 部署計畫與跨平台相容驗證 (Deployment & Compatibility Verification)

### 1. 部署方案
* 本專案為 100% 純前端（HTML/CSS/JS）SPA 應用，無須任何後端伺服器與資料庫建置。
* 將 `index.html` 作為專案根目錄的首頁，直接託管於 GitHub 儲存庫（Repository），並啟用 **GitHub Pages** 免費靜態網站託管服務。

### 2. 跨設備/平台相容性優化與注意事項
* **螢幕適配 (RWD)**：確認 Flexbox 與 Grid 佈局能在 iOS (Safari/Chrome) 及 Android 行動端完美呈現，無跑版問題。
* **發音系統 (Web Speech API - TTS)**：
  * 行動裝置瀏覽器通常限制「必須由使用者點擊按鈕或手動點擊觸發」才可發音。本專案目前皆使用點擊發音按鈕觸發，符合安全政策。
* **狀態保存 (LocalStorage)**：
  * 玩家進度與登入名稱會綁定在部署後的 GitHub Pages 專域下（例如 `https://<username>.github.io/<repo-name>/`），確保該設備的瀏覽器重新整理或關閉後，再次打開仍能保存。

## 七、 驗證計畫 (Verification Plan)

### 本機相容性驗證
* 確保 `index.html` 內無任何硬編碼的本機絕對路徑（如 `C:\...` 或 `D:\...`），均為相對路徑或 CDN 連結。
* 檢查外部引入的庫（目前全為原生 API，無外部載入庫，可斷網運作）。

### 部署後人工驗證
* 使用電腦、iOS (iPhone/iPad) 及 Android 系統手機測試：
  1. 能否正常登入並顯示玩家名稱。
  2. TTS 單字與文章發音是否正常運作。
  3. 測驗功能（單字與閱讀）是否能正常作答與結算分數。

