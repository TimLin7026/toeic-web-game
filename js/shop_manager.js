/**
 * ShopManager.js - 積分、每日/連續任務、獎金挑戰賽與安全防護管理器
 */
(function() {
    const PRESETS = {
        PASS_CODE: '6666',
        COOLDOWN_MS: 15 * 60 * 1000 // 15 分鐘冷卻
    };

    const ShopManager = {
        data: {
            points: 0,
            streakDays: 0,
            lastActiveDate: '',
            newBox1Count: 0,
            challengedWordIds: [], // 已參與挑戰的單字ID列表，防重複利用
            redemptionHistory: [],
            cooldownUntil: 0,
            // 任務相關
            todayDate: '',
            todayLearnedWordIds: [], // 今天新掌握的單字ID
            todayMockPerfect: false, // 今天是否完美通過模擬考
            claimedQuests: {
                basic: false,      // 每日基本背詞 (50分)
                mock: false,       // 每日模擬考滿分 (20分)
                intensity: false   // 每日高強度背詞 (30分)
            }
        },

        init() {
            this.loadFromLocalStorage();
            this.checkAndResetDaily();
            this.saveToLocalStorage();
        },

        loadFromLocalStorage() {
            const saved = localStorage.getItem('toeic_shop_data');
            if (saved) {
                try {
                    this.data = { ...this.data, ...JSON.parse(saved) };
                } catch (e) {
                    console.error("載入 ShopManager 資料失敗:", e);
                }
            }
        },

        saveToLocalStorage() {
            localStorage.setItem('toeic_shop_data', JSON.stringify(this.data));
            // 兼容性寫法，方便前端直接抓取點數
            localStorage.setItem('toeic_points', this.data.points.toString());
        },

        getTodayDateString() {
            const d = new Date();
            const year = d.getFullYear();
            const month = String(d.getMonth() + 1).padStart(2, '0');
            const day = String(d.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
        },

        getYesterdayDateString() {
            const d = new Date();
            d.setDate(d.getDate() - 1);
            const year = d.getFullYear();
            const month = String(d.getMonth() + 1).padStart(2, '0');
            const day = String(d.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
        },

        checkAndResetDaily() {
            const today = this.getTodayDateString();
            this.data.todayDate = today;

            if (this.data.lastActiveDate !== today) {
                const yesterday = this.getYesterdayDateString();
                
                // 檢查昨天的基本每日任務是否達標以維繫連續天數
                const yesterdayLearnedCount = this.data.todayLearnedWordIds ? this.data.todayLearnedWordIds.length : 0;
                
                if (this.data.lastActiveDate === yesterday && yesterdayLearnedCount >= 15) {
                    // 昨天有達標，且是昨天活躍，連續天數 + 1
                    this.data.streakDays = (this.data.streakDays || 0) + 1;
                } else if (this.data.lastActiveDate !== today) {
                    // 中斷了（昨天沒達成，或者空了兩天以上），連續天數歸零
                    this.data.streakDays = 0;
                }

                // 重置每日狀態
                this.data.todayLearnedWordIds = [];
                this.data.todayMockPerfect = false;
                this.data.claimedQuests = {
                    login: false,
                    learn5: false,
                    learn10: false,
                    basic: false,
                    mock: false,
                    intensity: false
                };
                
                this.data.lastActiveDate = today;
                this.saveToLocalStorage(); // 確保重置狀態實體存檔
                
                // 如果今天剛好是連續第 7 天達標，在之後完成基本任務時會發放連續獎勵
            }

            // 每日登入檢驗 (必須連結 Google)
            const isGoogleConnected = localStorage.getItem('g_connected') === 'true';
            if (isGoogleConnected && (!this.data.claimedQuests || !this.data.claimedQuests.login)) {
                if (!this.data.claimedQuests) {
                    this.data.claimedQuests = {
                        login: false,
                        learn5: false,
                        learn10: false,
                        basic: false,
                        mock: false,
                        intensity: false
                    };
                }
                this.data.claimedQuests.login = true;
                this.data.points += 20; // 獲得 20 積分
                this.saveToLocalStorage();
                if (typeof window.saveProgressToCloud === 'function') {
                    window.saveProgressToCloud();
                } else if (typeof window.uploadProgressToCloud === 'function') {
                    window.uploadProgressToCloud();
                }
            }
        },

        // 當單字首次從 Box 0 升級到 Box 1 以上時觸發
        onWordNewLearned(wordId) {
            this.checkAndResetDaily();

            // 防刷：必須未曾被挑戰過且今天還沒算進去
            if (!this.data.challengedWordIds.includes(wordId) && !this.data.todayLearnedWordIds.includes(wordId)) {
                this.data.todayLearnedWordIds.push(wordId);
                this.data.newBox1Count++;
                
                this.updateQuestStatus();
                this.saveToLocalStorage();
            }
        },

        // 更新並發放每日任務積分
        updateQuestStatus() {
            const learnedCount = this.data.todayLearnedWordIds.length;
            let changed = false;

            if (!this.data.claimedQuests) {
                this.data.claimedQuests = {
                    login: false,
                    learn5: false,
                    learn10: false,
                    basic: false,
                    mock: false,
                    intensity: false
                };
            }

            // 1. 每日新學 5 個單字 (10分)
            if (learnedCount >= 5 && !this.data.claimedQuests.learn5) {
                this.data.claimedQuests.learn5 = true;
                this.data.points += 10;
                changed = true;
            }

            // 2. 每日新學 10 個單字 (15分)
            if (learnedCount >= 10 && !this.data.claimedQuests.learn10) {
                this.data.claimedQuests.learn10 = true;
                this.data.points += 15;
                changed = true;
            }

            // 3. 每日基本任務：新學 15 個單字 (25分)
            if (learnedCount >= 15 && !this.data.claimedQuests.basic) {
                this.data.claimedQuests.basic = true;
                this.data.points += 25;
                changed = true;
                
                // 檢查是否達成連續 7 天任務 (150分)
                if (this.data.streakDays >= 6) {
                    this.data.points += 150;
                    alert("🎉 恭喜！連續 7 天每日學習達標，獲得額外 +150 連續挑戰積分！");
                }
            }

            // 4. 進階任務一：模擬考滿分 (20分)
            if (this.data.todayMockPerfect && !this.data.claimedQuests.mock) {
                this.data.claimedQuests.mock = true;
                this.data.points += 20;
                changed = true;
            }

            // 5. 進階任務二：高強度背詞 25 個單字 (30分)
            if (learnedCount >= 25 && !this.data.claimedQuests.intensity) {
                this.data.claimedQuests.intensity = true;
                this.data.points += 30;
                changed = true;
            }

            if (changed) {
                this.saveToLocalStorage();
                if (typeof window.saveProgressToCloud === 'function') {
                    window.saveProgressToCloud();
                } else if (typeof window.uploadProgressToCloud === 'function') {
                    window.uploadProgressToCloud();
                }
            }
        },

        // 完成模擬考
        completeMockExam(isPerfect) {
            this.checkAndResetDaily();
            if (isPerfect) {
                this.data.todayMockPerfect = true;
                this.updateQuestStatus();
                this.saveToLocalStorage();
            }
        },

        // 檢查是否可進行挑戰賽
        checkTournamentEligibility(isDouble) {
            const requiredPoints = isDouble ? 150 : 100;
            
            // 1. 檢查 Google 帳號連動
            const isGoogleConnected = window.accessToken || localStorage.getItem('g_connected') === 'true';
            if (!isGoogleConnected) {
                return { eligible: false, reason: "請先連結 Google 帳號，連動雲端進度後方可參賽。" };
            }

            // 2. 檢查積分
            if (this.data.points < requiredPoints) {
                return { eligible: false, reason: `積分不足！需要 ${requiredPoints} 積分，目前僅有 ${this.data.points} 積分。` };
            }

            // 3. 檢查新單字量是否滿 15 個
            if (this.data.newBox1Count < 15) {
                return { eligible: false, reason: `新學習單字量不足！本輪已累積 ${this.data.newBox1Count}/15 個新單字。請先去學習新字。` };
            }

            // 4. 檢查冷卻時間
            const now = Date.now();
            if (now < this.data.cooldownUntil) {
                const diffMin = Math.ceil((this.data.cooldownUntil - now) / 60000);
                return { eligible: false, reason: `挑戰賽冷卻中！請等待 ${diffMin} 分鐘後再試。` };
            }

            return { eligible: true };
        },

        completeTournament(isDouble, isSuccess) {
            this.checkAndResetDaily();
            const requiredPoints = isDouble ? 150 : 100;

            if (isSuccess) {
                // 只有挑戰成功才會扣除積分
                this.data.points = Math.max(0, this.data.points - requiredPoints);
                
                // 重置新掌握單字計數器
                this.data.newBox1Count = 0;

                // 將今日學到的新字與目前進度中的單字 ID 加入 challengedWordIds，標記為已挑戰
                if (window.wordList) {
                    window.wordList.forEach(w => {
                        if (w.box > 0 && !this.data.challengedWordIds.includes(w.id)) {
                            this.data.challengedWordIds.push(w.id);
                        }
                    });
                }

                // 產生兌換紀錄
                const prizeAmount = isDouble ? 200 : 100;
                const record = {
                    id: 'redempt_' + Date.now(),
                    date: this.getTodayDateString(),
                    item: `$${prizeAmount} 零用錢現金`,
                    pointsUsed: requiredPoints,
                    status: '待領取'
                };
                this.data.redemptionHistory.unshift(record);

                alert(`🎉 恭喜通過挑戰賽！已扣除 ${requiredPoints} 參賽積分，並生成 $${prizeAmount} 零用錢兌換紀錄。進度已同步！`);

                this.saveToLocalStorage();
                if (typeof window.saveProgressToCloud === 'function') {
                    window.saveProgressToCloud();
                } else if (typeof window.uploadProgressToCloud === 'function') {
                    window.uploadProgressToCloud();
                }
            } else {
                // 挑戰失敗，不扣除積分，不寫入冷卻
                alert(`😢 遺憾！本次挑戰未達 100% 答對，挑戰失敗。未獲得獎勵，不扣除任何積分。加油，下次一定能成功！`);
            }
        },

        // 二次確認核銷兌換
        claimPrize(recordId) {
            const record = this.data.redemptionHistory.find(r => r.id === recordId);
            if (record && record.status === '待領取') {
                const confirmed = confirm(`⚠️ 二次確認：\n\n您確定已經拿到家長發放的「${record.item}」現金了嗎？\n核銷後此筆紀錄將被永久標記為 [已領取]，點數不會退回！`);
                if (confirmed) {
                    record.status = '已領取';
                    this.saveToLocalStorage();
                    // 同步雲端
                    if (typeof window.saveProgressToCloud === 'function') {
                        window.saveProgressToCloud();
                    } else if (typeof window.uploadProgressToCloud === 'function') {
                        window.uploadProgressToCloud();
                    }
                    return true;
                }
            }
            return false;
        },

        // 雙重重置邏輯
        resetProgress(wordList, isComplete, onConfirmCallback) {
            if (isComplete) {
                // 完全重置需家長密碼
                const password = prompt("⚠️ 完全重置警告：\n這會將此單元的所有單字進度與「歷史最高紀錄(maxBox)」全面清空，重新背誦可再次累積積分。\n\n請輸入家長密碼以確認執行：");
                if (password === PRESETS.PASS_CODE) {
                    // 清空 box 與 maxBox
                    wordList.forEach(w => {
                        w.box = 0;
                        w.maxBox = 0;
                        // 從已挑戰列表中移出
                        const idx = this.data.challengedWordIds.indexOf(w.id);
                        if (idx > -1) {
                            this.data.challengedWordIds.splice(idx, 1);
                        }
                    });
                    this.saveToLocalStorage();
                    onConfirmCallback();
                } else if (password !== null) {
                    alert("❌ 密碼錯誤，拒絕完全重置！");
                }
            } else {
                // 一般重置不需密碼，但 maxBox 保持不變，不能洗分
                const confirmed = confirm("確定要「一般重置」此單元進度嗎？\n此操作會將單字回歸 Box 0 方便複習，但「不會」清除歷史最高學習紀錄，再次學習無法重複獲得積分。");
                if (confirmed) {
                    wordList.forEach(w => {
                        w.box = 0;
                    });
                    this.saveToLocalStorage();
                    onConfirmCallback();
                }
            }
        }
    };

    window.ShopManager = ShopManager;
})();
