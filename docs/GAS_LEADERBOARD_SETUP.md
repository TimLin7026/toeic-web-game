# Google Apps Script (GAS) 天梯排行榜後端部署教學

這份教學將指引您在 30 秒內建立並部署專屬的「天梯排行榜」Google 試算表後端 API。

---

## 🛠️ 3 步極簡部署指南

### 步驟 1：建立 Google 試算表
1. 打開瀏覽器，前往 **[sheets.new](https://sheets.new)** 建立一張全新的空白 Google 試算表。
2. 將試算表左上角命名為：`多益天梯榜`（或任何您喜歡的名稱）。

### 步驟 2：貼上 Apps Script 程式碼
1. 點選試算表頂部選單的 **「擴充功能」 > 「Apps Script」**。
2. 將編輯器內原有的程式碼清空，**完整複製並貼上下方的「GAS 後端完整程式碼」**。
3. 點擊上方的 **「儲存」 💾** 按鈕（或按 `Ctrl + S`）。

### 步驟 3：部署為網頁應用程式 (Web App)
1. 點擊右上角藍色的 **「部署」 > 「新增部署」**。
2. 在「選取類型」齒輪圖示點選 **「網頁應用程式」**。
3. 填寫部署設定：
   * **說明**：`天梯排行榜 API`
   * **執行身分**：`我 (您的 Gmail)`
   * **誰可以存取**：**`任何人`**（⚠️ 務必選「任何人」，這樣家人的遊戲端才能上傳與讀取成績）
4. 點擊 **「部署」**（首次部署若出現授權畫面，點「審查權限」> 選擇帳號 > 點「進階」>「前往...（不安全）」> 點「允許」）。
5. 複製最後產生的 **「網頁應用程式網址 (Web App URL)」**（格式類似 `https://script.google.com/macros/s/AKfycb.../exec`）。
6. 將該網址貼入遊戲設定或提供給開發助理即可！

---

## 💻 GAS 後端完整程式碼 (複製貼入 Apps Script)

```javascript
/**
 * 多益網頁遊戲 - 天梯排行榜後端 (Google Apps Script)
 * 支援全自動表頭建立、使用者成績 Upsert 與三大維度排序查詢
 */

const HEADERS = [
  "Email", 
  "自訂暱稱", 
  "Google顯示名稱", 
  "頭像網址", 
  "總積分", 
  "掌握單字數", 
  "連續天數", 
  "最後更新時間"
];

function getOrCreateSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("Leaderboard");
  if (!sheet) {
    sheet = ss.insertSheet("Leaderboard");
  }
  // 檢查表頭
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold").setBackground("#EEF2FF");
    sheet.setFrozenRows(1);
  }
  return sheet;
}

// 處理 GET 請求：取得天梯榜名單
function doGet(e) {
  try {
    const sheet = getOrCreateSheet();
    const data = sheet.getDataRange().getValues();
    const type = (e && e.parameter && e.parameter.type) || "points"; // points | words | streak
    
    if (data.length <= 1) {
      return createJsonResponse({ status: "success", type: type, data: [] });
    }
    
    // 解析資料列
    let players = [];
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      const email = String(row[0] || "").trim();
      if (!email) continue;
      
      const customNick = String(row[1] || "").trim();
      const gName = String(row[2] || "").trim();
      const photoUrl = String(row[3] || "").trim();
      const points = Number(row[4]) || 0;
      const masteredCount = Number(row[5]) || 0;
      const streakDays = Number(row[6]) || 0;
      const updatedAt = String(row[7] || "");
      
      // 生成遮罩 Email (例如: tin***26@gmail.com)
      const parts = email.split("@");
      let maskedEmail = email;
      if (parts.length === 2) {
        const namePart = parts[0];
        if (namePart.length > 3) {
          maskedEmail = namePart.substring(0, 3) + "***" + (namePart.length > 5 ? namePart.slice(-2) : "") + "@" + parts[1];
        } else {
          maskedEmail = namePart.substring(0, 1) + "***@" + parts[1];
        }
      }
      
      players.push({
        email: email,
        maskedEmail: maskedEmail,
        displayName: customNick || gName || maskedEmail,
        googleName: gName,
        photoUrl: photoUrl,
        points: points,
        masteredCount: masteredCount,
        streakDays: streakDays,
        updatedAt: updatedAt
      });
    }
    
    // 依指定維度排序
    if (type === "words") {
      players.sort((a, b) => b.masteredCount - a.masteredCount || b.points - a.points);
    } else if (type === "streak") {
      players.sort((a, b) => b.streakDays - a.streakDays || b.points - a.points);
    } else {
      // 預設: 總積分
      players.sort((a, b) => b.points - a.points || b.masteredCount - a.masteredCount);
    }
    
    return createJsonResponse({
      status: "success",
      type: type,
      totalCount: players.length,
      data: players.slice(0, 50) // 最多回傳前 50 名
    });
  } catch (err) {
    return createJsonResponse({ status: "error", message: err.toString() });
  }
}

// 處理 POST 請求：上報/更新玩家成績
function doPost(e) {
  try {
    let body = {};
    if (e.postData && e.postData.contents) {
      body = JSON.parse(e.postData.contents);
    } else if (e.parameter) {
      body = e.parameter;
    }
    
    const email = String(body.email || "").trim().toLowerCase();
    if (!email) {
      return createJsonResponse({ status: "error", message: "Email is required" });
    }
    
    const sheet = getOrCreateSheet();
    const data = sheet.getDataRange().getValues();
    const nowStr = Utilities.formatDate(new Date(), "Asia/Taipei", "yyyy-MM-dd HH:mm:ss");
    
    const nickname = String(body.nickname || body.displayName || "").trim();
    const googleName = String(body.googleName || body.displayName || "").trim();
    const photoUrl = String(body.photoUrl || "").trim();
    const points = Number(body.points) || 0;
    const masteredCount = Number(body.masteredCount) || 0;
    const streakDays = Number(body.streakDays) || 0;
    
    let rowIndex = -1;
    for (let i = 1; i < data.length; i++) {
      if (String(data[i][0]).toLowerCase().trim() === email) {
        rowIndex = i + 1; // 1-based index
        break;
      }
    }
    
    if (rowIndex > -1) {
      // 更新現有玩家
      const currentNick = sheet.getRange(rowIndex, 2).getValue();
      const finalNick = nickname || currentNick || googleName;
      sheet.getRange(rowIndex, 1, 1, HEADERS.length).setValues([[
        email,
        finalNick,
        googleName || sheet.getRange(rowIndex, 3).getValue(),
        photoUrl || sheet.getRange(rowIndex, 4).getValue(),
        points,
        masteredCount,
        streakDays,
        nowStr
      ]]);
    } else {
      // 新增玩家
      sheet.appendRow([
        email,
        nickname || googleName,
        googleName,
        photoUrl,
        points,
        masteredCount,
        streakDays,
        nowStr
      ]);
    }
    
    return createJsonResponse({ status: "success", message: "Score updated successfully" });
  } catch (err) {
    return createJsonResponse({ status: "error", message: err.toString() });
  }
}

function createJsonResponse(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
```
