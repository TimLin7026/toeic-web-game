# 如何取得 Google Client ID 設定指南

本專案採用 Google Drive API 將您的學習進度同步至使用者自己的 Google 雲端硬碟。為了在網頁上啟用 Google 登入功能，您需要取得一串 **Google Client ID**。請跟著以下步驟完成免費設定：

---

## 第一步：建立 Google Cloud 專案

1. 開啟瀏覽器，進入 [Google Cloud Console (控制台)](https://console.cloud.google.com/)。
2. 登入您的 Google 帳號。
3. 點擊頁面上方導覽列左側的 **「專案選取器」**（如果沒有專案，通常會顯示一個預設專案或「選取專案」下拉選單）。
4. 點擊彈出視窗右上角的 **「新增專案」(New Project)**。
5. 設定專案名稱（例如：`TOEIC Web Game`），組織與位置保持預設，然後點擊 **「建立」(Create)」**。
6. 建立完成後，確保頁面上方的專案選取器切換至您剛剛建立的專案。

---

## 第二步：啟用 Google Drive API

1. 點擊左上角選單（三條橫線），選擇 **「API 和服務」(APIs & Services) ➡️ 「庫」(Library)**。
2. 在搜尋欄輸入 **「Google Drive API」** 並搜尋。
3. 點擊搜尋結果中的 **Google Drive API**。
4. 點擊藍色的 **「啟用」(Enable)** 按鈕。

---

## 第三步：設定 OAuth 同意畫面 (OAuth Consent Screen)

因為是讓任何使用者用自己的 Google 帳號登入，需要先設定登入時的同意畫面。

1. 點擊左側選單的 **「OAuth 同意畫面」(OAuth consent screen)**。
2. 使用者類型 (User Type) 選擇 **「外部」(External)**。
3. 點擊 **「建立」(Create)」**。
4. **填寫應用程式基本資訊**：
   * **App name (應用程式名稱)**：例如 `Unit 17 單字訓練營`。
   * **User support email (使用者支援電子郵件)**：選擇您自己的 Gmail。
   * **Developer contact information (開發人員聯絡資訊)**：填寫您的 Gmail。
   * 其他欄位（標誌、網域等）可暫時留空。
5. 點擊最下方的 **「儲存並繼續」(Save and Continue)**。
6. **Scopes (範圍) 設定**：
   * 點擊 **「新增或移除範圍」(Add or remove scopes)**。
   * 在清單中搜尋並勾選：`.../auth/drive.appdata`（非必選，如果列表中沒出現，請在最下方的手動輸入欄輸入：`https://www.googleapis.com/auth/drive.appdata` 然後點擊新增）。
   * 勾選完成後點擊儲存並繼續。
7. **Test users (測試使用者)**：
   * 由於應用程式尚未正式通過 Google 審核，處於「測試狀態」。
   * 點擊 **「Add Users」**，**輸入您自己以及您想要用來測試的其他 Google 帳號信箱**，然後點擊儲存並繼續。

---

## 第四步：建立 OAuth 客戶端 ID (Client ID)

1. 點擊左側選單的 **「憑證」(Credentials)**。
2. 點擊上方的 **「+ 建立憑證」(Create Credentials)** ➡️ 選擇 **「OAuth 客戶端 ID」(OAuth client ID)**。
3. **Application type (應用程式類型)**：選擇 **「網頁應用程式」(Web application)**。
4. **名稱 (Name)**：可以使用預設值或自訂（例如 `TOEIC Web Client`）。
5. **已授權的 JavaScript 來源 (Authorized JavaScript origins)**：
   * 點擊 **「+ 新增 URI」(ADD URI)**，並輸入以下兩個網址：
     1. **`http://localhost:8000`** *(本機測試用)*
     2. **`https://timlin7026.github.io`** *(您發佈在 GitHub Pages 的線上網址)*
   * ⚠️ *注意：Google OAuth 不支援直接開啟本機檔案 (`file:///`) 進行登入驗證。因此本機測試時，必須使用本機伺服器 (`http://localhost:8000`) 才能成功登入。*
6. **已授權的重新導向 URI (Authorized redirect URIs)**：
   * 此處暫時**不用填寫**（因為本專案使用的是前端彈出視窗登入機制）。
7. 點擊最下方的 **「建立」(Create)」**。

---

## 🏆 第五步：取得 Client ID

1. 建立成功後，畫面會彈出一個 **「OAuth 客戶端已建立」** 的視窗。
2. 複製其中的 **「您的客戶端 ID」(Your Client ID)**。
   * 它會是一長串像這樣的文字：`123456789-abcdefg.apps.googleusercontent.com`
3. 請把這串 Client ID 妥善保存，並提供給我。

我們將把它嵌入到程式碼中，使用者就可以安全地使用自己的 Google 帳號跨設備儲存與讀取進度了！
