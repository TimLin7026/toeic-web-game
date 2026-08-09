# 多益自主學習網頁遊戲 — GitHub Pages 部署與跨設備使用手冊

本專案為純前端單頁應用程式（SPA），不需要任何後端伺服器或資料庫。您可以將它免費部署在 **GitHub Pages** 上，方便在電腦、手機、平板等各種設備上隨時進行多益學習與測驗。

---

## 🛠️ 第一部分：上架至 GitHub Pages 步驟

### 步驟 1：準備您的 GitHub 帳號
如果您還沒有 GitHub 帳號，請先至 [GitHub 官網](https://github.com/) 免費註冊一個帳號。

### 步驟 2：建立新的儲存庫 (Repository)
1. 登入 GitHub 後，點擊右上角的 **「+」** 按鈕，選擇 **New repository**。
2. 進行以下設定：
   * **Repository name (儲存庫名稱)**：輸入一個英文名稱，例如 `toeic-web-game`。
   * **Public/Private**：請務必選擇 **Public (公開)**。*(免費版的 GitHub Pages 必須是公開儲存庫才能啟用)*。
   * 其他選項（Add a README file 等）保持預設不勾選即可。
3. 點擊最下方的 **Create repository** 按鈕。

### 步驟 3：上傳 `index.html` 檔案
您可以選擇以下兩種方式之一來上傳檔案：

#### 方法 A：使用網頁瀏覽器直接拖曳上傳（最簡單，免安裝工具）
1. 在剛建立好的儲存庫頁面中，點擊中間的 **「uploading an existing file」** 連結。
2. 將您本機電腦中的 [`index.html`](file:///d:/工具開發區/多益網頁遊戲專案/index.html) 檔案拖曳到網頁的框框中。
3. 等待上傳完成後，在下方的 Commit 訊息欄位輸入 `Initial commit`。
4. 點擊 **Commit changes** 按鈕。

#### 方法 B：使用 Git 命令列上傳
如果您熟悉 Git，可以在本機專案目錄下執行以下指令：
```bash
git init
git add index.html
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/您的帳號/您的儲存庫名稱.git
git push -u origin main
```

---

## 🌐 第二部分：啟用 GitHub Pages 網頁託管

1. 在 GitHub 儲存庫頁面上方，點擊 **Settings (設定)** 按鈕（齒輪圖示）。
2. 在左側選單中，找到並點擊 **Pages**（位於 Code and automation 區塊下）。
3. 在 **Build and deployment** 下的 **Branch** 區塊：
   * 將預設的 `None` 切換為 **`main`**（或 `master`，依您上傳的分支而定）。
   * 後方的資料夾保持選擇 **`/ (root)`**。
4. 點擊 **Save** 存檔。
5. **等待 1 到 2 分鐘**，重新整理此頁面。您會在最上方看到一行綠色提示框，顯示您的專案網址，格式如下：
   👉 `https://您的帳號.github.io/您的儲存庫名稱/`
6. 點擊該網址即可直接打開您的多益英文學習遊戲！

---

## 📱 第三部分：如何跨設備/平台使用

部署完成後，只要在任何有網路的設備上開啟瀏覽器，輸入剛才的 GitHub Pages 網址，就能開始使用。以下是不同設備的推薦使用方式：

### 1. 電腦端（Windows / Mac）
* 建議使用 Google Chrome、Microsoft Edge 或 Safari 瀏覽器。
* 狀態儲存：玩家登入的名稱與測驗進度會儲存在該瀏覽器的 `LocalStorage` 中。只要不清除瀏覽器快取，下次打開網址就會自動載入。

### 2. 行動端設備（iOS / Android 手機與平板）
為了獲得像手機 App 一樣的無邊框沉浸式體驗，建議將網頁「加入主畫面」：

#### 🍏 iPhone / iPad (iOS Safari)
1. 使用 **Safari** 瀏覽器打開您的 GitHub Pages 網址。
2. 點擊瀏覽器下方工具列的 **「分享」** 按鈕（向上箭頭的方塊圖示）。
3. 往下滑動選單，點擊 **「加入主畫面」(Add to Home Screen)**。
4. 命名為「多益學習遊戲」，點擊右上角 **「新增」**。
5. 您的手機桌面就會出現一個遊戲圖示，點擊它即可像啟動 App 一樣全螢幕遊玩！

#### 🤖 Android 手機 (Chrome)
1. 使用 **Chrome** 瀏覽器打開您的 GitHub Pages 網址。
2. 點擊右上角的 **「三點」選單** 按鈕。
3. 點擊 **「安裝應用程式」** 或 **「新增至主畫面」**。
4. 確認新增後，即可從手機桌面快速啟動。

---

## ⚠️ 跨設備使用重要注意事項

1. **進度不同步**：由於本專案為「免帳號純前端」設計，您的學習紀錄與名字是保存在**該台設備的瀏覽器本機 (LocalStorage)**。因此，在 iPhone 上的測驗分數**不會**同步到電腦或 Android 手機上。若未來需要跨設備同步，需要升級系統以串接雲端資料庫（如 Firebase）。
2. **語音發音 (TTS)**：
   * 行動裝置有嚴格的隱私安全限制，語音發音（TTS）**無法在網頁剛載入時自動播放**，必須經由玩家「手動點擊」發音按鈕才會發聲。目前專案的發音設計已符合此安全規範。
   * 若行動裝置點擊語音按鈕沒有聲音，請確認手機是否處於**靜音模式**，或嘗試將音量放大。
