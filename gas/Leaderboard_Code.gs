const SHEET_NAME = "Leaderboard";
const HEADERS = ["Email", "Nickname", "DisplayName", "PhotoUrl", "Points", "MasteredCount", "StreakDays", "LastUpdated"];

function getOrCreateSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold").setBackground("#EEF2FF");
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function doGet(e) {
  try {
    const sheet = getOrCreateSheet();
    const type = (e && e.parameter && e.parameter.type) ? e.parameter.type : "points";
    const data = sheet.getDataRange().getValues();
    if (data.length <= 1) {
      return ContentService.createTextOutput(JSON.stringify({ status: "success", count: 0, data: [] })).setMimeType(ContentService.MimeType.JSON);
    }
    const players = [];
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      const email = String(row[0] || "").trim();
      if (!email) continue;
      const nickname = String(row[1] || "").trim();
      const displayName = String(row[2] || "").trim() || nickname || email.split("@")[0];
      const photoUrl = String(row[3] || "").trim();
      const points = Number(row[4]) || 0;
      const masteredCount = Number(row[5]) || 0;
      const streakDays = Number(row[6]) || 0;
      const lastUpdated = row[7] ? String(row[7]) : "";
      players.push({
        email: email,
        maskedEmail: email.includes("@") ? email.replace(/(.{2})(.*)(?=@)/, "$1***") : email,
        nickname: nickname,
        displayName: nickname || displayName,
        googleName: displayName,
        photoUrl: photoUrl || ("https://api.dicebear.com/7.x/bottts/svg?seed=" + encodeURIComponent(displayName)),
        points: points,
        masteredCount: masteredCount,
        streakDays: streakDays,
        lastUpdated: lastUpdated
      });
    }
    if (type === "words") {
      players.sort((a, b) => b.masteredCount - a.masteredCount || b.points - a.points);
    } else if (type === "streak") {
      players.sort((a, b) => b.streakDays - a.streakDays || b.points - a.points);
    } else {
      players.sort((a, b) => b.points - a.points || b.masteredCount - a.masteredCount);
    }
    return ContentService.createTextOutput(JSON.stringify({ status: "success", type: type, count: players.length, data: players })).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "No post data received." })).setMimeType(ContentService.MimeType.JSON);
    }
    const payload = JSON.parse(e.postData.contents);
    const email = String(payload.email || "").trim().toLowerCase();
    if (!email) {
      return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Email is required." })).setMimeType(ContentService.MimeType.JSON);
    }
    const sheet = getOrCreateSheet();
    const data = sheet.getDataRange().getValues();
    const nowStr = Utilities.formatDate(new Date(), "Asia/Taipei", "yyyy-MM-dd HH:mm:ss");
    const nickname = String(payload.nickname || "").trim();
    const displayName = String(payload.displayName || "").trim();
    const photoUrl = String(payload.photoUrl || "").trim();
    const points = Number(payload.points) || 0;
    const masteredCount = Number(payload.masteredCount) || 0;
    const streakDays = Number(payload.streakDays) || 0;
    
    let targetRow = -1;
    for (let i = 1; i < data.length; i++) {
      if (String(data[i][0] || "").trim().toLowerCase() === email) {
        targetRow = i + 1;
        break;
      }
    }
    const rowValues = [email, nickname, displayName, photoUrl, points, masteredCount, streakDays, nowStr];
    if (targetRow > -1) {
      sheet.getRange(targetRow, 1, 1, HEADERS.length).setValues([rowValues]);
    } else {
      sheet.appendRow(rowValues);
    }
    return ContentService.createTextOutput(JSON.stringify({ status: "success", action: targetRow > -1 ? "updated" : "inserted", email: email, updatedAt: nowStr })).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() })).setMimeType(ContentService.MimeType.JSON);
  }
}
