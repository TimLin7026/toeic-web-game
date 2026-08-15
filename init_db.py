import sqlite3
import os

DB_PATH = 'toeic_vocab.db'

def init_database():
    # 確保原本的 DB 被刪除重新建立，保持乾淨
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. 建立資料表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE NOT NULL,
            meaning TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_words (
            book_id TEXT,
            word_id INTEGER,
            unit_number INTEGER,
            PRIMARY KEY (book_id, word_id, unit_number),
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (word_id) REFERENCES words(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sentences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_id INTEGER,
            sentence_en TEXT NOT NULL,
            sentence_zh TEXT NOT NULL,
            sentence_index INTEGER NOT NULL,
            FOREIGN KEY (word_id) REFERENCES words(id)
        )
    ''')

    # 2. 插入教材資訊
    cursor.execute("INSERT INTO books (id, name) VALUES (?, ?)", 
                   ('high_school_level_3_5', '高中英文核心字彙Level3-5'))

    # 3. 準備 Unit 17 與 Unit 18 的單字與例句數據
    # 格式: (word, meaning, unit, [ (sentence_en, sentence_zh), ... ])
    vocab_data = [
        # =========================================================================
        # UNIT 17 (1-40)
        # =========================================================================
        ("spoil", "破壞；寵壞、溺愛；腐敗", 17, [
            ("He tried not to let the bad news spoil his party.", "他盡量不讓那個壞消息毀了他的派對。"),
            ("Parents spoil their children by doing everything for them.", "父母若什麼事都親力親為會寵壞孩子。"),
            ("Food will spoil in the fridge, too, only more slowly.", "冰箱裡的食物也會腐敗，只是較慢罷了。")
        ]),
        ("novel", "小說；新奇的", 17, [
            ("His latest novel is selling really well.", "他最新出版的小說十分暢銷。"),
            ("Everything is novel to a two-year-old child.", "對一個兩歲小孩而言，一切事物都是新奇的。"),
            ("The novelty of these toys soon wore off.", "這些玩具的新鮮感很快就消失了。")
        ]),
        ("constant", "持續的、經常的；恆定不變的事物；常數", 17, [
            ("There are constant complaints about the noise from our neighbors.", "不斷有人向我們抱怨鄰居的噪音。"),
            ("Her friendship is the one and only constant in his life.", "她的友誼是他生命中唯一不變的事。"),
            ("It rains constantly in May.", "五月經常下雨。")
        ]),
        ("invent", "發明", 17, [
            ("The first safety razor was invented by King C. Gillette.", "金・坎普・吉列發明第一把安全刮鬍刀。"),
            ("Franklin was a scientist, inventor, and statesman.", "富蘭克林是科學家、發明家也是政治家。"),
            ("Necessity is the mother of invention.", "需要為發明之母。") # 補充相關衍生
        ]),
        ("ray", "光線；X光", 17, [
            ("Your skin needs protection from the sun's rays.", "你的皮膚需要防曬。"),
            ("I still have a ray of hope that he'll recover.", "我仍抱一絲希望他會復原。"),
            ("All baggage aboard must be examined by x-ray first.", "所有登機行李需先經過 X 光的檢驗。")
        ]),
        ("cheer", "鼓舞、使高興；歡呼；喝采；乾杯", 17, [
            ("My mother always cheers me (up) when I am down.", "母親總是在我失意時鼓勵我。"),
            ("The crowd cheered the Olympic medal winners.", "群眾為奧運得獎選手歡呼。"),
            ("My brother remained cheerful and energetic throughout the trip.", "我弟弟整趟旅途都很興高采烈、精力旺盛。")
        ]),
        ("gossip", "閒聊、八卦；閒聊、談論是非", 17, [
            ("They sat in the café having a good gossip about their friends.", "他們坐在咖啡廳裡盡情聊朋友們的八卦。"),
            ("It is a stereotype that all housewives like to gossip.", "家庭主婦都喜歡聊八卦是刻板印象。"),
            ("Don't spread gossip about others.", "不要傳播關於他人的閒言閒語。")
        ]),
        ("dump", "傾倒；甩掉；垃圾堆、垃圾場", 17, [
            ("Tons of garbage are dumped daily into the ocean.", "每天都有好幾噸的垃圾被倒入海裡。"),
            ("He has been in a bad mood since he was dumped by his girlfriend.", "自從他被女友甩掉後心情很不好。"),
            ("The locals voted against the plan to build a dump in their town.", "當地居民投票反對在鎮上興建垃圾場。")
        ]),
        ("dairy", "酪農場；乳製品販賣店；乳製品", 17, [
            ("Local dairies let their cows graze freely on pastures.", "當地的酪農場讓牛自在地在牧場上吃草。"),
            ("You can buy all kinds of cheese in the dairy.", "你可以在乳製品專賣店裡買到各式各樣的乳酪。"),
            ("Most dairy products are made from cows' milk.", "大部分乳製品原料來自牛乳。")
        ]),
        ("stuff", "事物、東西；填塞；塞滿的", 17, [
            ("He has bought all the stuff we need for camping.", "他已經買了我們露營所需的所有東西。"),
            ("They stuffed the pillows with cotton.", "他們在枕頭裡塞棉花。"),
            ("I am stuffed. I can't eat another bite.", "我吃得好飽啊！我一口也吃不下了。")
        ]),
        ("jar", "廣口瓶、罐子", 17, [
            ("Please buy me a big jar of pickles when you go to the store.", "你去商店時，請幫我買一大罐泡菜。"),
            ("She put the flower seeds in a small glass jar.", "她把花種子放進一個小玻璃罐裡。"),
            ("The jam jar is hard to open.", "果醬罐很難打開。")
        ]),
        ("stick", "黏貼；刺入；堅持；卡住；棍子、手杖", 17, [
            ("You have to stick your picture on the form.", "你必須把照片貼在表格上。"),
            ("Stick to your goal. Never give up.", "堅持目標，不要放棄。"),
            ("I am stuck in the traffic jam.", "我身陷車陣中。")
        ]),
        ("drain", "排(水)、流乾；消耗掉；排水管", 17, [
            ("We drained the pool and filled it with fresh water.", "我們放掉水池的水重新注滿乾淨的水。"),
            ("Constant war drained the country of people and money.", "連年戰爭耗損這個國家的人力與金錢。"),
            ("All my time and money went down the drain.", "我所有的時間跟金錢都白費了。")
        ]),
        ("awake", "醒著的；醒來；喚起、喚醒", 17, [
            ("Are you awake? Breakfast is ready.", "你醒了嗎？早餐準備好了。"),
            ("When I awoke this morning, it was already eight o'clock.", "當我今天早上醒來時已經八點了。"),
            ("Revisiting his hometown awoke his childhood memories.", "返鄉喚起他的兒時回憶。")
        ]),
        ("chip", "碎片、渣；晶片；薄片；切下、打掉小片", 17, [
            ("Chips of glass from a broken window are difficult to clean up.", "窗戶的玻璃碎片很難清理。"),
            ("It is now a must for pet-keepers to put chips in their pets.", "現在的飼主都必須為寵物植入晶片。"),
            ("She chipped a piece off her mother's favorite plate by accident.", "她不小心將母親最喜歡的盤子弄破一小角。")
        ]),
        ("alley", "巷子；巷道；車道", 17, [
            ("The alley led to the railway station.", "這條巷子通往火車站。"),
            ("This is a quiet country lane.", "這是條安靜的鄉間巷道。"),
            ("He changed lanes without giving any signals.", "他沒有打方向燈就變換車道。")
        ]),
        ("bacteria", "細菌", 17, [
            ("UV rays can kill bacteria.", "紫外線可殺菌。"),
            ("Bacteria play a big role in food decomposition.", "細菌在食物分解中扮演重要角色。"),
            ("Yogurt contains bacteria that are good for health.", "優格含有對健康有益的細菌。")
        ]),
        ("bait", "餌；逗弄；引誘", 17, [
            ("We used worms as bait when we went fishing.", "我們釣魚時以蟲做餌。"),
            ("I knew he was baiting me, so I ignored him.", "我知道他故意惹我生氣，所以不理他。"),
            ("There are all kinds of advertisements baiting prospective buyers.", "各式各樣的廣告誘惑潛在買家。")
        ]),
        ("beast", "野獸 (大型獸類)", 17, [
            ("I was lucky that the beast didn't bite my arm off.", "算我命大，那隻野獸沒咬斷我的手臂。"),
            ("The lion is known as the king of beasts.", "獅子被稱為百獸之王。"),
            ("Beauty and the Beast is a famous fairy tale.", "美女與野獸是著名的童話故事。")
        ]),
        ("berry", "莓果類、漿果；草莓、藍莓、蔓越莓", 17, [
            ("There are lots of berries in the field.", "原野上有很多漿果。"),
            ("The cake is decorated with strawberries, blueberries and mulberries.", "這個蛋糕用草莓、藍莓和桑葚裝飾。"),
            ("Cranberries and raspberries contain lots of antioxidants.", "蔓越莓與覆盆子富含抗氧化物。")
        ]),
        ("brake", "煞車", 17, [
            ("When you want to slow down, step on the brake.", "當你想放慢車速時就踩煞車。"),
            ("I don't like to drive very fast and then brake (the car) hard.", "我不喜歡開快車，然後再緊急踩煞車。"),
            ("My bicycle brakes need to be repaired.", "我的腳踏車煞車需要修理。")
        ]),
        ("bud", "嫩芽、花苞；萌芽、開始發展", 17, [
            ("Insects love to feed on the buds of trees most.", "昆蟲最喜歡吃樹葉的嫩芽。"),
            ("The roses are budding.", "這些玫瑰正在萌芽。"),
            ("Flowers in bud are most beautiful.", "含苞待放的花朵最美。")
        ]),
        ("buffet", "歐式自助餐；自助餐廳", 17, [
            ("The price includes a buffet breakfast.", "這個價格包括自助式早餐。"),
            ("I had my dinner at a cafeteria.", "我在自助餐廳吃晚餐。"),
            ("The hotel offers a rich buffet dinner.", "飯店提供豐盛的自助晚餐。")
        ]),
        ("bump", "撞擊；腫塊；路面突起；碰撞；不期而遇", 17, [
            ("We all felt the bump when the boat hit the dock.", "船撞到船塢時我們都感受到撞擊。"),
            ("I hit the cupboard in the head and got a bump.", "我的頭撞到碗櫃腫了起來。"),
            ("I bumped into an old friend of mine the other day.", "前幾天我碰到一位老朋友。")
        ]),
        ("carpenter", "木匠", 17, [
            ("Carpenters can make and repair wooden furniture.", "木匠會製造或修繕木製傢俱。"),
            ("He hired a carpenter to make a dining table.", "他雇用了一位木匠來製作一張餐桌。"),
            ("The carpenter is measuring the length of the wood.", "木匠正在測量木頭的長度。")
        ]),
        ("chat", "閒聊、聊天", 17, [
            ("Let's have a chat.", "我們聊一聊吧！"),
            ("We were just chatting about what we did last weekend.", "我們正在閒聊上個週末做了些什麼。"),
            ("Online chat rooms are popular among teenagers.", "線上聊天室在青少年間很受歡迎。")
        ]),
        ("cherry", "櫻桃；櫻桃口味的；櫻花", 17, [
            ("The girls are picking cherries.", "女孩們正在摘櫻桃。"),
            ("Cherry yogurt is my favorite.", "櫻桃口味的優格是我的最愛。"),
            ("The cherry blossom is the national flower of Japan.", "櫻花是日本的國花。")
        ]),
        ("porcelain", "瓷器", 17, [
            ("The museum is holding a special exhibition of porcelain.", "博物館正在舉辦瓷器特展。"),
            ("Bone china is lighter and costlier.", "骨瓷較輕也較貴。"),
            ("She collected exquisite porcelain teacups.", "她收集精緻的瓷茶杯。")
        ]),
        ("chop", "劈、砍、剁；帶骨肉排", 17, [
            ("Tom was chopping wood for fire.", "湯姆正在劈柴生火。"),
            ("We will have pork chops and mushroom soup for dinner.", "我們晚餐要吃豬排與蘑菇湯。"),
            ("He gave the tree several chops of an ax before it fell down.", "他用斧頭砍了好幾次，樹才倒下。")
        ]),
        ("circus", "馬戲團；小丑", 17, [
            ("Children love being taken to the circus.", "小孩喜歡被帶去看馬戲團。"),
            ("Without clowns, a circus is not a circus.", "馬戲團沒有小丑就不成馬戲團了。"),
            ("Ben likes to make her laugh by clowning (around).", "班喜歡扮小丑逗她笑。")
        ]),
        ("clinic", "診所；臨床教學", 17, [
            ("Patients with minor disorders should go to local clinics.", "身體輕微不適的病人應在當地診所看診。"),
            ("Clinics and ward rounds are important in practical training.", "在實際訓練上臨床研究與病房巡診很重要。"),
            ("The dental clinic is closed on Sundays.", "牙科診所星期日休診。")
        ]),
        ("cradle", "搖籃；溫柔抱著；孕育地", 17, [
            ("The mother rocked the cradle where her baby was lying.", "媽媽搖著寶寶躺著的搖籃。"),
            ("The woman cradled the baby in her arms.", "那位婦人將寶寶溫柔地抱在懷中。"),
            ("The Nile Valley is the cradle of the Egyptian civilization.", "尼羅河谷是埃及文明的發源地。")
        ]),
        ("dam", "水壩；築壩攔水；壓抑情緒", 17, [
            ("The Aswan High Dam is on the Nile in Egypt.", "亞斯文高壩位於埃及的尼羅河上。"),
            ("Once a river is dammed up, the biological communities in it will be affected.", "一旦河流受堤壩攔堵，該區的生物聚落將受到連帶影響。"),
            ("It is unhealthy to dam up your anger.", "壓抑怒氣是不健康的。")
        ]),
        ("darling", "親愛的人；親愛的；迷人的", 17, [
            ("Oh darling, I do love you.", "哦！親愛的，我真的愛你。"),
            ("Happy birthday to my darling daughter.", "我親愛的女兒，生日快樂！"),
            ("We just moved into our darling little apartment.", "我們剛搬進自己的迷人小公寓。")
        ]),
        ("depth", "深度；(情感或知識的) 深度；加深", 17, [
            ("Plant the seeds at a depth of about six inches.", "將這些種子種在約六英吋深的地方。"),
            ("Have you ever thought about why your presentation lacked depth?", "你有沒有想過為何你的報告欠缺深度呢？"),
            ("They deepened the well to get more water.", "他們把井加深以獲取更多水。")
        ]),
        ("quarter", "四分之一；一刻鐘；季度；二十五分錢硬幣；一角/一分硬幣", 17, [
            ("She alone ate a quarter of the turkey.", "她一個人吃了四分之一的火雞。"),
            ("It's a quarter past ten.", "現在的時間是十點十五分。"),
            ("You need to have at least a quarter to make a local call.", "打一通市內電話至少要一枚二角五分硬幣。")
        ]),
        ("dip", "沾、浸；沾醬", 17, [
            ("Dip the fish in the batter, and then drop it into the hot oil.", "將魚浸在麵糊裡然後丟進熱油。"),
            ("Mexicans love to eat corn chips with salsa dip.", "墨西哥人喜歡吃玉米片配莎莎 (酸甜) 醬。"),
            ("Dip your pen in the ink.", "把你的筆沾上墨水。")
        ]),
        ("ditch", "壕溝、渠道；丟棄；甩掉", 17, [
            ("I fell asleep on the way home and drove my car into a ditch.", "我在回家途中睡著，因而把車開進大水溝裡。"),
            ("The suspect ditched the car and ran into the woods.", "嫌犯棄車逃進樹林裡去。"),
            ("He ditched his wife of twenty years for a younger woman.", "他為了一個年輕女子而拋棄結縭二十年的妻子。")
        ]),
        ("harbor", "港口；心懷、懷有；碼頭；停靠", 17, [
            ("Many ships took shelter from the storm in the harbor.", "許多船隻入港躲避暴風雨。"),
            ("The two men harbor hatred toward each other.", "這兩人彼此仇視。"),
            ("A crowd was waiting at the dock to greet them.", "一大群人在碼頭等著迎接他們。")
        ]),
        ("envy", "羨慕、嫉妒；令 N 羨慕的對象", 17, [
            ("She has a lifestyle which most people would envy.", "她過著一種多數人都嫉妒的生活方式。"),
            ("He watched the others with envy.", "他用羨慕的眼光看著其他人。"),
            ("Our health insurance system is the envy of the world.", "我們的健保制度舉世稱羨。")
        ]),

        # =========================================================================
        # UNIT 18 (1-40)
        # =========================================================================
        ("erase", "擦掉、消除", 18, [
            ("The computer crashed, and all our records were erased.", "電腦當機了，我們所有的紀錄都被消除。"),
            ("It is impossible to erase those memories from my mind.", "要在我的腦海中消除那些回憶是不可能的。"),
            ("You can use an eraser to erase the pencil marks.", "你可以用橡皮擦把鉛筆痕跡擦掉。")
        ]),
        ("fancy", "昂貴的、豪華的；花俏精緻的；幻想；喜歡；幻想", 18, [
            ("I had dinner at a fancy restaurant.", "在一本豪華的餐廳享用晚餐。"), # 配合課本上的微瑕語句
            ("He bought a fancy sports car.", "他買了一輛很炫的跑車。"),
            ("The boy often fancies himself as a superhero.", "這個男孩時常幻想自己是超級英雄。")
        ]),
        ("flock", "(鳥、羊)群；成群聚集", 18, [
            ("It's easy to spot flocks of geese as they migrate.", "當成群的野雁遷徙時，很容易發現牠們的蹤跡。"),
            ("Thirty million tourists flock to New York every year.", "每年都有三千萬遊客湧入紐約。"),
            ("Birds of a feather flock together.", "物以類聚 (同一種羽毛的鳥會聚集在一起)。")
        ]),
        ("grocery", "雜貨；雜貨商；雜貨店", 18, [
            ("I usually do grocery shopping on weekends.", "我通常在週末採買生活用品。"),
            ("John bought some eggs at the grocer's.", "約翰在雜貨店買了一些蛋。"),
            ("There is a grocery store around the corner from the hostel.", "青年旅社的附近有一家雜貨店。")
        ]),
        ("headline", "新聞標題；以~為標題；段落標題", 18, [
            ("I just read through the headlines of the paper.", "我只瀏覽報紙的標題。"),
            ("The article is headlined \"Listen to your heart.\"", "這篇文章的標題是「傾聽內在的聲音」。"),
            ("The heading of each chapter in this book has been carefully written.", "書中每章的標題都是審慎撰寫的。")
        ]),
        ("helmet", "頭盔、安全帽", 18, [
            ("Be sure to wear a safety helmet when you ride a motorcycle.", "騎乘機車一定要戴安全帽。"),
            ("The construction worker wore a hard helmet.", "建築工人戴著堅固的安全帽。"),
            ("Soldiers wear helmets to protect their heads in battle.", "士兵在戰鬥中戴頭盔以保護頭部。")
        ]),
        ("homesick", "思鄉的、想家的；故鄉", 18, [
            ("As I read my mother's letter, I felt more and more homesick.", "當我讀母親的信時，想家的心情愈來愈強烈。"),
            ("His hometown is a small town in the middle of France.", "他的家鄉是法國中部的一座小鎮。"),
            ("He felt homesick during his first week at college.", "他在上大學的第一個星期感到很想家。")
        ]),
        ("outdoor", "戶外的；在戶外；室內的；在室內", 18, [
            ("He likes outdoor activities.", "他喜歡戶外活動。"),
            ("Most children like to play outdoors rather than stay indoors.", "大部分的小孩喜歡在戶外玩耍勝過待在室內。"),
            ("The indoor flower market is a big tourist attraction.", "這個室內花卉市場是一個很大的觀光景點。")
        ]),
        ("jealous", "妒忌的", 18, [
            ("He has always been very jealous of his brother's good looks.", "他一直都非常忌妒哥哥俊俏的外表。"),
            ("She felt jealous when she saw her boyfriend talking to another girl.", "當她看到男友與另一個女孩聊天時，她感到忌妒。"),
            ("His success made his colleagues jealous.", "他的成功讓他的同事感到忌妒。")
        ]),
        ("jelly", "果凍；果醬", 18, [
            ("I've made a strawberry jelly for the children.", "我做了草莓果凍給小朋友。"),
            ("Americans love peanut butter and jelly sandwich.", "美國人愛吃花生果醬三明治。"),
            ("The jelly is set and ready to eat.", "果凍已經凝固可以吃了。")
        ]),
        ("jewel", "寶石、首飾；珠寶", 18, [
            ("She loved dressing up and wearing priceless jewels.", "她愛盛裝打扮並穿戴一些價值不斐的珠寶首飾。"),
            ("The burglar stole all the jewelry.", "竊賊偷走所有珠寶。"),
            ("Diamonds are the most precious of all jewels.", "鑽石是所有寶石中最珍貴的。")
        ]),
        ("junk", "垃圾、沒用東西；垃圾食品；破壞", 18, [
            ("The garage is full of junk.", "車庫裡頭塞滿了廢物。"),
            ("Eating too much junk food is not good for your health.", "吃太多垃圾食物對你的健康有害。"),
            ("Many shops were trashed during the riot.", "許多商店在暴動中被砸爛。")
        ]),
        ("lung", "肺；肝臟；腎臟", 18, [
            ("He died of lung cancer.", "他死於肺癌。"),
            ("Drinking too much alcohol does harm to your liver.", "酒喝多了對肝臟不好。"),
            ("The patient badly needs a kidney transplant.", "這位病人急需腎臟移植。")
        ]),
        ("meter", "公尺；儀表；公分；公里", 18, [
            ("The desk is one meter long, half a meter wide.", "這桌子長一公尺寬半公尺。"),
            ("I am 172 centimeters tall.", "我的身高有一百七十二公分。"),
            ("They are now a kilometer from the castle.", "他們現在離城堡有一公里遠。")
        ]),
        ("knot", "繩結；打結", 18, [
            ("Are you good at tying knots?", "你擅長綁繩結嗎？"),
            ("Do you know how to knot a bow tie?", "你知道如何打蝴蝶結嗎？"),
            ("He tied a tight knot in the rope.", "他在繩子上打了個緊緊的結。")
        ]),
        ("litter", "隨手丟棄垃圾；亂丟垃圾", 18, [
            ("People who drop litter can be fined in some cities.", "在某些城市亂丟垃圾的人會被罰款。"),
            ("The sign says, \"Please Don't litter.\"", "告示上寫著「請勿亂丟垃圾」。"),
            ("The park is littered with rubbish.", "公園裡滿地垃圾。")
        ]),
        ("mall", "大型購物中心", 18, [
            ("Let's meet at the mall.", "我們在購物中心碰面吧！"),
            ("The new mall has over two hundred shops.", "新購物中心有超過兩百家商店。"),
            ("She spent the whole afternoon shopping at the mall.", "她整個下午都在購物中心逛街。")
        ]),
        ("marvelous", "令人驚嘆的、不可思議的", 18, [
            ("The Great Wall is a marvelous architectural feat.", "萬里長城是個令人驚嘆的建築。"),
            ("We had a marvelous time at the party.", "我們在派對上玩得很痛快。"),
            ("The weather today is just marvelous.", "今天的天氣真是太棒了。")
        ]),
        ("medal", "獎牌；銀/銅牌", 18, [
            ("She won a gold medal at the last Olympics.", "她在上屆奧運贏得一面金牌。"),
            ("The silver medal and the bronze medal go to Jane and Jack respectively.", "銀牌與銅牌得主分別為珍與傑克。"),
            ("He proudly displayed his military medals.", "他驕傲地展示他的軍事勳章。")
        ]),
        ("merry", "歡樂的；旋轉木馬", 18, [
            ("I wish you a merry Christmas.", "祝你耶誕快樂。"),
            ("We went for a ride on the merry-go-round.", "我們去坐旋轉木馬。"),
            ("The sound of merry laughter filled the room.", "歡樂的笑聲充滿了整個房間。")
        ]),
        ("microphone", "麥克風", 18, [
            ("She spoke confidently into the microphone.", "她自信地對著麥克風說話。"),
            ("The singer adjusted the microphone stand.", "歌手調整了麥克風架。"),
            ("Please speak into the microphone so everyone can hear you.", "請對著麥克風說話，這樣大家才能聽見。")
        ]),
        ("microwave", "微波；微波加熱", 18, [
            ("I always heat up my lunch in the microwave oven.", "我都用微波爐加熱便當。"),
            ("Some foods taste terrible after they are microwaved.", "有些食物微波之後很難吃。"),
            ("Microwave cooking is fast and convenient.", "微波爐烹調快速又便利。")
        ]),
        ("nap", "小睡", 18, [
            ("I often take a nap after lunch.", "我常在午餐後小睡片刻。"),
            ("Children under two nap both in the morning and in the afternoon.", "兩歲以下的小孩早上和下午都會小睡一下。"),
            ("The old man is napping in his armchair.", "老人正在他的扶手椅上打盹。")
        ]),
        ("collar", "衣領；領帶；白領/藍領", 18, [
            ("The wind was so cold that he turned his coat collar up.", "風太冷了，所以他把外套的領子立起來。"),
            ("Our general manager always wears a necktie at work.", "我們總經理總是打著領帶上班。"),
            ("Government statistics show that hourly earnings of white-collar workers are about 30% higher than those of blue-collar workers.", "政府統計資料顯示，白領階級的時薪比藍領階級高三成。")
        ]),
        ("pal", "朋友、哥兒們", 18, [
            ("I am so happy to see my old pal Martin.", "我高興要與老友馬丁碰面了。"),
            ("Hi, pal, please keep your voice down.", "嗨，兄弟，說話請小聲點。"),
            ("They have been best pals since childhood.", "他們從小就是最好的朋友。")
        ]),
        ("pancake", "煎薄餅、鬆餅；甜甜圈", 18, [
            ("Would you like your pancake with syrup or cream?", "你的鬆餅要配糖漿還是奶油？"),
            ("Most Americans like to eat doughnuts.", "大部分的美國人喜歡吃甜甜圈。"),
            ("She made a stack of pancakes for breakfast.", "她做了疊鬆餅當早餐。")
        ]),
        ("parcel", "包裹；打包", 18, [
            ("The parcel was wrapped in plain brown paper.", "那個包裹用普通的牛皮紙包著。"),
            ("She parceled the letters and put them in the drawer.", "她將信件紮好並放進抽屜。"),
            ("He parceled some food for the picnic in the afternoon.", "他為了下午的野餐包了一些食物。")
        ]),
        ("passport", "護照", 18, [
            ("He was a German, traveling on a Swiss passport.", "他是德國人，持瑞士護照旅行。"),
            ("You must show your passport at the border crossing.", "你必須在過境時出示護照。"),
            ("She applied for a new passport last week.", "她上週申請了新護照。")
        ]),
        ("pity", "同情；遺憾的事；自憐；可憐的", 18, [
            ("I pity her for having to work while we are on vacation.", "我同情她在我們度假的時候必須工作。"),
            ("It's a pity that I cannot attend this conference.", "很遺憾，我不能參加這場學術研討會。"),
            ("Stop indulging in self-pity for yourself.", "別沉浸在自艾自憐中了。")
        ]),
        ("pollute", "汙染；汙染物", 18, [
            ("His mind is polluted by hatred.", "仇恨汙染了他的心智。"),
            ("Air pollution is a serious problem in modern cities.", "現代城市中的空氣汙染損害大。"),
            ("Exhaust fumes from vehicles are the major air pollutant.", "車輛排放的廢氣是最主要的空氣汙染物。")
        ]),
        ("rot", "腐壞；爛到底", 18, [
            ("Rain has got in and rotted the woodwork.", "雨水滲進來，腐蝕了木造的部分。"),
            ("Remove decaying vegetables to prevent rot from spreading.", "移除腐爛的蔬菜，以防腐壞情況擴散。"),
            ("He is rotten to the core.", "他真是壞到骨子裡了。")
        ]),
        ("rust", "鐵鏽；生鏽", 18, [
            ("The spade was covered with rust.", "那鏟子上布滿鐵鏽。"),
            ("Iron rusts easily.", "鐵容易生鏽。"),
            ("The old gate has rusted shut.", "舊鐵門生鏽卡住關不上了。")
        ]),
        ("sack", "大袋子", 18, [
            ("The corn was stored in large sacks.", "玉米被存放在大袋子裡。"),
            ("He carried a heavy sack of potatoes on his back.", "他背上背著一大袋沉重的馬鈴薯。"),
            ("The workers filled the sacks with sand to block the flood.", "工人用沙填滿袋子來防洪。")
        ]),
        ("shampoo", "洗髮精；洗頭；肥皂劇", 18, [
            ("You need a gentle shampoo for your baby's fine hair.", "你需要溫和的洗髮精來清潔寶寶柔細的頭髮。"),
            ("We should wash hands with soap before eating.", "我們吃東西前應該用肥皂洗手。"),
            ("Many housewives enjoy watching soap operas.", "許多家庭主婦喜歡看肥皂劇。")
        ]),
        ("shepherd", "牧羊人；牧羊犬", 18, [
            ("The shepherd herds his sheep down the mountain.", "牧羊人驅趕綿羊下山。"),
            ("A sheepdog can do twenty shepherds' job.", "一隻牧羊犬可以做二十個牧羊人的工作。"),
            ("The Lord is my shepherd; I shall not want.", "耶和華是我的牧者，我必不致缺乏。")
        ]),
        ("slip", "滑倒；滑落；溜走；紙片；拖鞋；滑的", 18, [
            ("The ground was so wet that I almost slipped.", "地上很溼，我差一點滑倒。"),
            ("The glass slipped out of my hand and smashed on the floor.", "玻璃杯從我手中滑落，碎了一地。"),
            ("Even when walking on the carpet, I still have my slippers on.", "我即使走在地毯上，還是穿著拖鞋。")
        ]),
        ("sorrow", "悲傷", 18, [
            ("He expressed his sorrow at my father's death.", "他對我父親的去世表達哀悼之情。"),
            ("She hid her sorrow behind a forced smile.", "她用強顏歡笑掩飾她的悲傷。"),
            ("Time heals all sorrows.", "時間會撫平所有的悲傷。")
        ]),
        ("spy", "間諜；監視；看見", 18, [
            ("He was suspected of having been a spy during the war.", "他遭懷疑曾在戰時擔任間諜。"),
            ("The woman hired a private detective to spy on her husband.", "這名女子僱用一名私家偵探監視丈夫。"),
            ("I spied my sister in the crowd at the entrance.", "我在入口處的人群中看到我妹妹。")
        ]),
        ("stadium", "運動場；體育館；健身房", 18, [
            ("Thousands of football fans packed into the stadium to watch the game.", "幾千名球迷擠進運動場來看球賽。"),
            ("We played basketball in the gymnasium.", "我們在體育館打籃球。"),
            ("I work out in the gymnasium every day.", "我每天都上健身房健身。")
        ]),
        ("stool", "凳子；糞便", 18, [
            ("The man fetched a stool and sat with the others.", "那個人拿了一把凳子和其他人坐在一起。"),
            ("A stool test can help diagnose problems in the digestive tract.", "糞便檢查有助於診斷消化道的問題。"),
            ("The piano stool is adjustable.", "琴凳是可以調整高度的。")
        ])
    ]

    # 4. 寫入資料
    for word, meaning, unit, sentences in vocab_data:
        # 寫入單字
        cursor.execute("INSERT OR IGNORE INTO words (word, meaning) VALUES (?, ?)", (word, meaning))
        cursor.execute("SELECT id FROM words WHERE word = ?", (word,))
        word_id = cursor.fetchone()[0]

        # 寫入教材關聯
        cursor.execute("INSERT OR REPLACE INTO book_words (book_id, word_id, unit_number) VALUES (?, ?, ?)", 
                       ('high_school_level_3_5', word_id, unit))

        # 寫入例句
        for idx, (en, zh) in enumerate(sentences):
            cursor.execute("""
                INSERT INTO sentences (word_id, sentence_en, sentence_zh, sentence_index)
                VALUES (?, ?, ?, ?)
            """, (word_id, en, zh, idx))

    conn.commit()
    conn.close()
    print("Database init_db.py executed successfully. Created toeic_vocab.db with 80 words.")

if __name__ == '__main__':
    init_database()
