import json
import os

file_path = r"d:\工具開發區\多益網頁遊戲專案\data\books\high_school_L3_18.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

examples_dict = {
    "a slip of the tongue / pen": [
        {"en": "I didn't mean to insult her; it was just a slip of the tongue.", "zh": "我無意侮辱她；那只是口誤。"},
        {"en": "His slip of the pen caused a misunderstanding in the contract.", "zh": "他的筆誤導致了合約上的誤會。"},
        {"en": "Please forgive my slip of the tongue during the presentation.", "zh": "請原諒我在簡報時的口誤。"},
        {"en": "A slip of the pen can sometimes have serious legal consequences.", "zh": "筆誤有時會產生嚴重的法律後果。"},
        {"en": "She quickly apologized for her slip of the tongue.", "zh": "她為自己的口誤迅速道了歉。"}
    ],
    "bench": [
        {"en": "We sat on a wooden bench in the park to rest.", "zh": "我們坐在公園的木長凳上休息。"},
        {"en": "The coach benched his best player due to an injury.", "zh": "教練因為受傷而讓最好的球員坐冷板凳。"},
        {"en": "There is a stone bench under the large oak tree.", "zh": "大橡樹下有一張石長凳。"},
        {"en": "She left her jacket on the park bench.", "zh": "她把外套忘在了公園長凳上。"},
        {"en": "The old man feeds the pigeons from his favorite bench every morning.", "zh": "老人每天早上都在他最喜歡的長凳上餵鴿子。"}
    ],
    "blue-collar": [
        {"en": "Many blue-collar workers are demanding better working conditions.", "zh": "許多藍領階級要求更好的工作條件。"},
        {"en": "He is proud of his blue-collar background and hard work.", "zh": "他為自己的藍領背景和辛勤工作感到自豪。"},
        {"en": "The town's economy relies heavily on blue-collar jobs in manufacturing.", "zh": "這個城鎮的經濟很大程度上依賴於製造業的藍領工作。"},
        {"en": "Blue-collar employees often face higher risks of workplace injuries.", "zh": "藍領員工通常面臨較高的工傷風險。"},
        {"en": "My father spent his entire life doing blue-collar work in a factory.", "zh": "我父親一輩子都在工廠做藍領工作。"}
    ],
    "centimeter": [
        {"en": "The caterpillar is about three centimeters long.", "zh": "這條毛毛蟲大約三公分長。"},
        {"en": "Please move the painting a few centimeters to the left.", "zh": "請把畫向左移幾公分。"},
        {"en": "A centimeter is a unit of length in the metric system.", "zh": "公分是公制中的長度單位。"},
        {"en": "The water level rose by several centimeters after the heavy rain.", "zh": "大雨過後水位上升了幾公分。"},
        {"en": "She is only a few centimeters taller than her younger sister.", "zh": "她只比她妹妹高幾公分。"}
    ],
    "collar": [
        {"en": "He wore a shirt with a stiff white collar.", "zh": "他穿著一件有硬白領的襯衫。"},
        {"en": "The dog managed to slip out of its collar and run away.", "zh": "那隻狗成功掙脫了項圈跑掉了。"},
        {"en": "Please turn down your collar; it looks messy.", "zh": "請把你的衣領翻下來；看起來很亂。"},
        {"en": "She bought a leather collar with a silver tag for her new puppy.", "zh": "她為新小狗買了一個帶有銀色吊牌的皮項圈。"},
        {"en": "The police collared the thief before he could escape the building.", "zh": "警察在小偷逃出大樓前逮捕了他。"}
    ],
    "doughnut": [
        {"en": "I bought a chocolate doughnut and a cup of coffee for breakfast.", "zh": "我買了一個巧克力甜甜圈和一杯咖啡當早餐。"},
        {"en": "The bakery is famous for its freshly baked doughnuts.", "zh": "這家麵包店以其剛出爐的甜甜圈聞名。"},
        {"en": "He took a bite of the sugary doughnut and smiled.", "zh": "他咬了一口撒滿糖的甜甜圈，笑了起來。"},
        {"en": "Eating too many doughnuts can lead to weight gain.", "zh": "吃太多甜甜圈會導致體重增加。"},
        {"en": "They sell doughnuts with various fillings, like strawberry and custard.", "zh": "他們賣各種餡料的甜甜圈，像是草莓和卡士達。"}
    ],
    "erase": [
        {"en": "Please use a pencil so you can erase any mistakes easily.", "zh": "請使用鉛筆，這樣你可以輕易擦掉錯誤。"},
        {"en": "He tried to erase the painful memories from his mind.", "zh": "他試圖將痛苦的記憶從腦海中抹去。"},
        {"en": "The teacher erased the notes on the blackboard after the class.", "zh": "老師下課後擦掉了黑板上的筆記。"},
        {"en": "Make sure you don't accidentally erase all the important files on your computer.", "zh": "確保你不會意外刪除電腦上所有重要的檔案。"},
        {"en": "Time cannot erase the impact she had on my life.", "zh": "時間無法抹滅她對我人生的影響。"}
    ],
    "fancy": [
        {"en": "They had dinner at a fancy restaurant to celebrate their anniversary.", "zh": "他們在一家高級餐廳吃晚餐慶祝紀念日。"},
        {"en": "I don't fancy going out tonight; I'd rather stay home.", "zh": "我今晚不想出門；我寧願待在家。"},
        {"en": "She was wearing a very fancy dress at the party.", "zh": "她在派對上穿著一件非常華麗的洋裝。"},
        {"en": "Do you fancy a cup of tea before we start working?", "zh": "我們開始工作前你想喝杯茶嗎？"},
        {"en": "He bought a fancy new sports car with his bonus.", "zh": "他用獎金買了一輛酷炫的新跑車。"}
    ],
    "flock": [
        {"en": "A flock of birds flew across the sunset sky.", "zh": "一群鳥飛過日落的天空。"},
        {"en": "Tourists flock to the island every summer for its beautiful beaches.", "zh": "每年夏天遊客成群結隊來到這座島嶼，因為這裡有美麗的海灘。"},
        {"en": "The shepherd guided his flock of sheep back to the barn.", "zh": "牧羊人引導他的羊群回到穀倉。"},
        {"en": "Thousands of fans flocked to the stadium to see the pop star.", "zh": "成千上萬的粉絲湧入體育場看這位流行巨星。"},
        {"en": "They saw a flock of geese resting near the lake.", "zh": "他們看到一群鵝在湖邊休息。"}
    ],
    "grocer": [
        {"en": "The local grocer knows most of his customers by name.", "zh": "當地的雜貨商能叫出大部分顧客的名字。"},
        {"en": "My grandfather worked as a grocer for over forty years.", "zh": "我祖父做了四十多年的雜貨商。"},
        {"en": "The grocer arranged the fresh vegetables neatly on the shelves.", "zh": "雜貨商將新鮮蔬菜整齊地擺放在架子上。"},
        {"en": "We buy our daily supplies from the grocer at the corner.", "zh": "我們向轉角的雜貨商購買日常用品。"},
        {"en": "The grocer warned us that the price of eggs would rise soon.", "zh": "雜貨商警告我們雞蛋的價格很快就會上漲。"}
    ],
    "grocery": [
        {"en": "I need to buy some groceries for dinner tonight.", "zh": "我需要買些雜貨來做今晚的晚餐。"},
        {"en": "She spent fifty dollars on groceries at the supermarket.", "zh": "她在超市花了五十美元買雜貨。"},
        {"en": "Carrying heavy bags of groceries up the stairs is exhausting.", "zh": "提著沉重的雜貨袋上樓梯很累人。"},
        {"en": "They usually do their grocery shopping on Saturday mornings.", "zh": "他們通常在星期六早上採買雜貨。"},
        {"en": "The delivery boy left the groceries at our front door.", "zh": "外送員把雜貨留在了我們的前門。"}
    ],
    "grocery store": [
        {"en": "There is a small grocery store just down the street.", "zh": "沿著這條街往下走有一家小雜貨店。"},
        {"en": "He stopped by the grocery store to pick up some milk.", "zh": "他順路去雜貨店買些牛奶。"},
        {"en": "The grocery store is open 24 hours a day for your convenience.", "zh": "為了您的方便，這家雜貨店24小時營業。"},
        {"en": "She works part-time as a cashier at a local grocery store.", "zh": "她在當地的一家雜貨店兼職當收銀員。"},
        {"en": "They decided to open a new grocery store in the neighborhood.", "zh": "他們決定在附近開一家新的雜貨店。"}
    ],
    "gymnasium": [
        {"en": "The graduation ceremony will be held in the school gymnasium.", "zh": "畢業典禮將在學校體育館舉行。"},
        {"en": "Students gather in the gymnasium every morning for assembly.", "zh": "學生每天早上在體育館集合開朝會。"},
        {"en": "The new gymnasium features a modern basketball court and a swimming pool.", "zh": "新體育館設有現代化的籃球場和游泳池。"},
        {"en": "He spends an hour in the gymnasium lifting weights after work.", "zh": "他下班後在健身房花一小時舉重。"},
        {"en": "During the storm, the gymnasium served as a temporary shelter.", "zh": "風暴期間，體育館被當作臨時避難所。"}
    ],
    "have / take pity on sb.": [
        {"en": "She took pity on the stray cat and brought it home.", "zh": "她可憐那隻流浪貓並把它帶回家。"},
        {"en": "The judge took pity on the young offender and gave him a lighter sentence.", "zh": "法官同情這名年輕的罪犯，判了他較輕的刑罰。"},
        {"en": "Please have pity on the homeless people in this freezing weather.", "zh": "在這種嚴寒天氣裡，請同情一下無家可歸的人。"},
        {"en": "He refused to ask for help because he didn't want anyone to take pity on him.", "zh": "他拒絕尋求幫助，因為他不想讓任何人同情他。"},
        {"en": "Taking pity on the lost child, the police officer bought him an ice cream.", "zh": "警察同情這個迷路的孩子，給他買了一個冰淇淋。"}
    ],
    "head": [
        {"en": "He nodded his head to show that he agreed with me.", "zh": "他點點頭表示同意我的看法。"},
        {"en": "She was appointed as the head of the marketing department.", "zh": "她被任命為行銷部門的主管。"},
        {"en": "They decided to head south for the winter to escape the cold.", "zh": "他們決定往南走過冬以避寒。"},
        {"en": "The principal will head the committee responsible for the new curriculum.", "zh": "校長將領導負責新課程的委員會。"},
        {"en": "Make sure to protect your head when you ride a motorcycle.", "zh": "騎機車時務必保護好你的頭部。"}
    ],
    "heading": [
        {"en": "Please write the main topic under the bold heading.", "zh": "請將主旨寫在粗體標題下方。"},
        {"en": "The chapter has a short heading that summarizes its content.", "zh": "這一章有一個簡短的標題來總結其內容。"},
        {"en": "She looked for her name under the heading 'Accepted Candidates'.", "zh": "她在「錄取名單」的標題下尋找自己的名字。"},
        {"en": "Each paragraph should have a clear heading to guide the reader.", "zh": "每個段落都應該有一個清晰的標題來引導讀者。"},
        {"en": "He quickly scanned the headings in the report before the meeting.", "zh": "開會前他快速瀏覽了報告中的標題。"}
    ],
    "headline": [
        {"en": "The news of the royal wedding dominated the front-page headline.", "zh": "皇家婚禮的新聞占據了頭版頭條。"},
        {"en": "She glanced at the headline of the newspaper but didn't read the article.", "zh": "她瞥了一眼報紙的頭條，但沒有閱讀文章。"},
        {"en": "His shocking statement immediately made headlines around the world.", "zh": "他令人震驚的聲明立刻成為全世界的頭條新聞。"},
        {"en": "The editor decided to change the headline to make it more catchy.", "zh": "編輯決定更改頭條，使其更吸引人。"},
        {"en": "Yesterday's headline about the economic crisis worried many investors.", "zh": "昨天關於經濟危機的頭條新聞讓許多投資者感到擔憂。"}
    ],
    "helmet": [
        {"en": "You must wear a helmet when riding a bicycle for safety.", "zh": "為了安全起見，騎自行車時必須戴安全帽。"},
        {"en": "The construction worker took off his yellow helmet to wipe his sweat.", "zh": "建築工人摘下黃色安全帽擦汗。"},
        {"en": "The helmet protected his head during the severe crash.", "zh": "在嚴重的車禍中，安全帽保護了他的頭部。"},
        {"en": "She strapped her helmet on tightly before climbing the rock wall.", "zh": "在攀岩之前，她緊緊繫好安全帽的帶子。"},
        {"en": "Motorcycle helmets come in various designs and colors.", "zh": "機車安全帽有各種設計和顏色。"}
    ],
    "homesick": [
        {"en": "As a freshman living in the dorm, he often felt homesick.", "zh": "作為一個住在宿舍的大一新生，他經常想家。"},
        {"en": "Looking at old family photos made her incredibly homesick.", "zh": "看著舊家庭照片讓她無比思鄉。"},
        {"en": "The exchange student burst into tears because she was too homesick.", "zh": "這名交換學生因為太想家而哭了出來。"},
        {"en": "Calling her parents every weekend helps ease her homesick feelings.", "zh": "每週末打電話給父母有助於緩解她思鄉的情緒。"},
        {"en": "It is completely normal to feel homesick when you first study abroad.", "zh": "剛出國留學時感到想家是完全正常的。"}
    ],
    "hometown": [
        {"en": "He returned to his hometown after working in the city for ten years.", "zh": "在城市工作十年後，他回到了故鄉。"},
        {"en": "My hometown is famous for its delicious street food and night markets.", "zh": "我的故鄉以美味的街頭小吃和夜市而聞名。"},
        {"en": "She always speaks proudly of her small, peaceful hometown.", "zh": "她總是自豪地談論她那寧靜的小故鄉。"},
        {"en": "The mayor gave a speech to celebrate the history of their hometown.", "zh": "市長發表演說慶祝他們故鄉的歷史。"},
        {"en": "Many young people leave their hometowns to seek better opportunities.", "zh": "許多年輕人離開故鄉尋求更好的機會。"}
    ],
    "indoor": [
        {"en": "Due to the rain, the event was moved to an indoor stadium.", "zh": "因為下雨，活動移至室內體育館舉行。"},
        {"en": "Indoor plants can improve the air quality in your home.", "zh": "室內植物可以改善你家中的空氣品質。"},
        {"en": "Swimming in an indoor pool is perfect for winter exercises.", "zh": "在室內游泳池游泳非常適合冬季運動。"},
        {"en": "They set up an indoor playground for the children to enjoy.", "zh": "他們為孩子們建立了一個室內遊樂場。"},
        {"en": "Indoor lighting plays a crucial role in interior design.", "zh": "室內照明在室內設計中扮演著至關重要的角色。"}
    ],
    "indoors": [
        {"en": "Let's stay indoors today since it's freezing outside.", "zh": "外面太冷了，我們今天就待在室內吧。"},
        {"en": "The dog was kept indoors during the fireworks display.", "zh": "放煙火時，那隻狗被關在室內。"},
        {"en": "It started pouring, so we quickly ran indoors.", "zh": "開始傾盆大雨了，所以我們趕快跑進室內。"},
        {"en": "Most of the children prefer playing video games indoors to playing outside.", "zh": "大多數孩子寧願在室內玩電動遊戲也不願在外面玩。"},
        {"en": "Please leave your wet umbrella near the door when you come indoors.", "zh": "進來室內時，請把濕雨傘放在門口附近。"}
    ],
    "jealous": [
        {"en": "He felt jealous when he saw his girlfriend talking to another man.", "zh": "當他看到女友和另一個男人說話時，他感到嫉妒。"},
        {"en": "She is naturally jealous of her sister's success and talent.", "zh": "她天生嫉妒姊姊的成功和才華。"},
        {"en": "Don't be jealous of others; focus on your own goals.", "zh": "不要嫉妒別人；專注於你自己的目標。"},
        {"en": "His jealous remarks revealed his true feelings about the promotion.", "zh": "他嫉妒的言辭透露了他對升職的真實感受。"},
        {"en": "A jealous attitude can ruin a perfectly good relationship.", "zh": "嫉妒的態度可能會毀掉一段美好的關係。"}
    ],
    "jelly": [
        {"en": "I made a peanut butter and jelly sandwich for lunch.", "zh": "我做了一個花生醬果凍三明治當午餐。"},
        {"en": "The children love eating fruit jelly as a dessert.", "zh": "孩子們喜歡吃水果果凍當甜點。"},
        {"en": "She bought a jar of strawberry jelly from the supermarket.", "zh": "她從超市買了一罐草莓果醬。"},
        {"en": "His legs felt like jelly after the rigorous marathon.", "zh": "跑完嚴格的馬拉松後，他的腿軟得像果凍。"},
        {"en": "The baker spread some jelly over the surface of the cake.", "zh": "麵包師傅在蛋糕表面塗了一些果醬。"}
    ],
    "jewel": [
        {"en": "The queen wore a crown decorated with sparkling jewels.", "zh": "女王戴著一頂裝飾著閃亮寶石的皇冠。"},
        {"en": "This antique vase is the crown jewel of the museum's collection.", "zh": "這個古董花瓶是博物館收藏中的瑰寶。"},
        {"en": "Thieves broke into the shop and stole several precious jewels.", "zh": "小偷闖入商店並偷走了幾件珍貴的首飾。"},
        {"en": "She kept a hidden jewel in a small wooden box.", "zh": "她把一顆隱藏的寶石放在一個小木盒裡。"},
        {"en": "He is highly valued by the company and considered a real jewel.", "zh": "他深受公司重視，被認為是真正的人才（瑰寶）。"}
    ],
    "jewelry": [
        {"en": "She inherited a large collection of gold and silver jewelry.", "zh": "她繼承了一大批金銀珠寶。"},
        {"en": "The jewelry store on the corner was robbed last night.", "zh": "轉角那家珠寶店昨晚被搶劫了。"},
        {"en": "He bought her a piece of expensive jewelry for their anniversary.", "zh": "他買了一件昂貴的珠寶給她作為紀念日禮物。"},
        {"en": "Please store all your valuable jewelry in the hotel safe.", "zh": "請將您所有貴重的珠寶存放在飯店保險箱中。"},
        {"en": "Making handmade jewelry has become her new favorite hobby.", "zh": "製作手工珠寶成了她最新的愛好。"}
    ],
    "junk": [
        {"en": "The garage is full of old junk that we need to throw away.", "zh": "車庫裡滿是我們需要丟掉的舊垃圾。"},
        {"en": "He spent the weekend clearing out the junk from the attic.", "zh": "他花了整個週末清理閣樓裡的沒用東西。"},
        {"en": "Don't believe what you read in that magazine; it's mostly junk.", "zh": "別相信你在那本雜誌上讀到的東西；大部分都是廢話。"},
        {"en": "I found some valuable antiques hidden among the junk at the flea market.", "zh": "我在跳蚤市場的破爛中發現了一些有價值的古董。"},
        {"en": "He decided to sell his junk car to a scrap yard.", "zh": "他決定把他的報廢老爺車賣給廢料場。"}
    ],
    "junk food": [
        {"en": "Eating too much junk food can lead to health problems like obesity.", "zh": "吃太多垃圾食品會導致肥胖等健康問題。"},
        {"en": "Parents should limit the amount of junk food their children consume.", "zh": "父母應該限制孩子攝取的垃圾食品數量。"},
        {"en": "She decided to cut out junk food and start eating healthy meals.", "zh": "她決定戒掉垃圾食品，開始吃健康的餐點。"},
        {"en": "Chips, soda, and candy are classic examples of junk food.", "zh": "洋芋片、汽水和糖果是垃圾食品的典型例子。"},
        {"en": "He grabbed some junk food from the convenience store on his way home.", "zh": "他在回家的路上從便利商店買了一些垃圾食品。"}
    ],
    "kidney": [
        {"en": "She had to undergo surgery to remove a stone from her kidney.", "zh": "她必須接受手術取出腎臟裡的結石。"},
        {"en": "Drinking plenty of water is essential for maintaining healthy kidneys.", "zh": "喝大量的水對維持健康的腎臟至關重要。"},
        {"en": "He generously donated a kidney to save his brother's life.", "zh": "他慷慨地捐出一個腎臟來拯救他兄弟的生命。"},
        {"en": "Kidney failure can be a life-threatening condition if left untreated.", "zh": "如果不加以治療，腎衰竭可能是危及生命的疾病。"},
        {"en": "The doctor ordered a blood test to check the patient's kidney function.", "zh": "醫生要求驗血以檢查患者的腎功能。"}
    ],
    "kilometer": [
        {"en": "The next gas station is about ten kilometers away.", "zh": "下一個加油站大約在十公里外。"},
        {"en": "He runs five kilometers every morning to stay fit.", "zh": "他每天早上跑五公里以保持健康。"},
        {"en": "The speed limit on this highway is one hundred kilometers per hour.", "zh": "這條高速公路的速限是每小時一百公里。"},
        {"en": "We hiked for several kilometers before reaching the mountain peak.", "zh": "我們徒步走了幾公里才到達山頂。"},
        {"en": "A kilometer is equivalent to one thousand meters.", "zh": "一公里等於一千公尺。"}
    ],
    "knot": [
        {"en": "Make sure you tie a tight knot so the boat doesn't drift away.", "zh": "務必打個緊結，以免船漂走。"},
        {"en": "She struggled to untie the knot in her shoelaces.", "zh": "她費力地解開鞋帶上的結。"},
        {"en": "His stomach tied in a knot before he gave the speech.", "zh": "他在演講前緊張得胃揪成一團。"},
        {"en": "The boy learned how to knot a tie from his father.", "zh": "男孩從父親那裡學會了如何打領帶。"},
        {"en": "You need to master several basic knots for sailing.", "zh": "為了航海，你需要掌握幾個基本的繩結。"}
    ],
    "litter": [
        {"en": "People who leave litter in the park should be fined heavily.", "zh": "在公園裡亂丟垃圾的人應該受到重罰。"},
        {"en": "Please use the trash cans and do not litter on the streets.", "zh": "請使用垃圾桶，不要在街上亂丟垃圾。"},
        {"en": "The beach was covered with plastic bottles and other litter.", "zh": "海灘上佈滿了塑膠瓶和其他隨手丟棄的垃圾。"},
        {"en": "The sign clearly reminds visitors not to litter the camping area.", "zh": "標誌清楚地提醒遊客不要在露營區亂丟垃圾。"},
        {"en": "A group of volunteers spent the morning picking up litter along the river.", "zh": "一群志工花了一個上午在河岸邊撿垃圾。"}
    ],
    "liver": [
        {"en": "Drinking excessive alcohol can cause severe damage to your liver.", "zh": "過度飲酒會對你的肝臟造成嚴重損害。"},
        {"en": "The liver is the largest internal organ in the human body.", "zh": "肝臟人體內最大的內部器官。"},
        {"en": "She was diagnosed with a rare liver disease and needs a transplant.", "zh": "她被診斷出患有罕見的肝病，需要進行移植。"},
        {"en": "Certain medications must be processed by the liver.", "zh": "某些藥物必須由肝臟處理。"},
        {"en": "Eating a balanced diet helps keep your liver functioning properly.", "zh": "均衡飲食有助於保持肝臟正常運作。"}
    ],
    "lung": [
        {"en": "Smoking is one of the leading causes of lung cancer.", "zh": "抽菸是肺癌的主要原因之一。"},
        {"en": "He took a deep breath, filling his lungs with fresh mountain air.", "zh": "他深吸了一口氣，讓肺部充滿新鮮的山區空氣。"},
        {"en": "The doctor listened carefully to her lungs with a stethoscope.", "zh": "醫生用聽診器仔細聽她的肺部。"},
        {"en": "Regular aerobic exercise can significantly improve your lung capacity.", "zh": "規律的有氧運動可以顯著改善你的肺活量。"},
        {"en": "The infection spread to his right lung, causing severe coughing.", "zh": "感染蔓延到他的右肺，引起嚴重的咳嗽。"}
    ],
    "mall": [
        {"en": "We spent the entire afternoon shopping at the new mall.", "zh": "我們整個下午都在新購物中心逛街。"},
        {"en": "The mall features a large cinema and various restaurants.", "zh": "這家購物中心設有大型電影院和各種餐廳。"},
        {"en": "Teenagers often hang out with their friends at the mall.", "zh": "青少年經常和朋友在購物中心閒逛。"},
        {"en": "Parking at the mall can be quite difficult on weekends.", "zh": "週末在購物中心停車可能會相當困難。"},
        {"en": "They opened a small clothing boutique in the local mall.", "zh": "他們在當地的購物中心開了一家小型服裝精品店。"}
    ],
    "marvelous": [
        {"en": "The chef prepared a marvelous feast for the wedding guests.", "zh": "廚師為婚禮賓客準備了一場極好的盛宴。"},
        {"en": "We had a marvelous time exploring the ancient ruins in Rome.", "zh": "我們在探索羅馬古蹟時度過了令人驚嘆的美好時光。"},
        {"en": "What a marvelous idea it is to host a surprise party for him!", "zh": "為他舉辦驚喜派對真是個極好的主意！"},
        {"en": "The view of the city from the top of the tower is simply marvelous.", "zh": "從塔頂俯瞰城市的景色簡直令人驚嘆。"},
        {"en": "She did a marvelous job organizing the charity event all by herself.", "zh": "她獨自一人把這場慈善活動組織得極好。"}
    ],
    "medal": [
        {"en": "He proudly displayed the gold medal he won at the Olympics.", "zh": "他驕傲地展示他在奧運會上贏得的金牌。"},
        {"en": "The soldier was awarded a medal of honor for his bravery in battle.", "zh": "這名士兵因在戰鬥中的英勇表現而被授予榮譽勳章。"},
        {"en": "She came in second place and received a silver medal.", "zh": "她獲得了第二名並獲得了一枚銀牌。"},
        {"en": "The marathon finishers were all given a commemorative medal.", "zh": "馬拉松完賽者都獲得了一枚紀念獎牌。"},
        {"en": "Her dream is to earn a medal in the upcoming swimming championship.", "zh": "她的夢想是在即將到來的游泳錦標賽中贏得獎牌。"}
    ],
    "merry": [
        {"en": "We wish you a merry Christmas and a happy New Year.", "zh": "我們祝你聖誕快樂，新年快樂。"},
        {"en": "The children's merry laughter echoed through the playground.", "zh": "孩子們歡樂的笑聲在遊樂場迴盪。"},
        {"en": "They had a merry evening singing and dancing around the campfire.", "zh": "他們在營火旁唱歌跳舞，度過了一個愉快的夜晚。"},
        {"en": "After a few glasses of wine, he became quite merry and talkative.", "zh": "喝了幾杯酒後，他變得相當愉快且健談。"},
        {"en": "The villagers organized a merry celebration for the successful harvest.", "zh": "村民們為豐收舉辦了一場歡樂的慶祝活動。"}
    ],
    "merry-go-round": [
        {"en": "The little girl wanted to ride the merry-go-round one more time.", "zh": "小女孩想再坐一次旋轉木馬。"},
        {"en": "The colorful horses on the merry-go-round moved up and down to the music.", "zh": "旋轉木馬上色彩鮮豔的馬匹隨著音樂上下移動。"},
        {"en": "He feels like his busy life is a never-ending merry-go-round.", "zh": "他覺得自己忙碌的生活就像永無止境的旋轉木馬。"},
        {"en": "The carnival featured a giant Ferris wheel and a vintage merry-go-round.", "zh": "嘉年華設有巨大的摩天輪和復古的旋轉木馬。"},
        {"en": "She waved to her parents as the merry-go-round spun around.", "zh": "旋轉木馬轉動時，她向父母揮手。"}
    ],
    "meter": [
        {"en": "The athlete broke the world record in the 100-meter dash.", "zh": "這名運動員打破了100公尺短跑的世界紀錄。"},
        {"en": "Please insert coins into the parking meter before you leave.", "zh": "離開前請將硬幣投入停車計時器。"},
        {"en": "The fabric is sold by the meter at the local market.", "zh": "這布料在當地市場是按公尺出售的。"},
        {"en": "The taxi driver turned on the meter as soon as we got in the car.", "zh": "我們一上車，計程車司機就打開了計程表。"},
        {"en": "He installed a smart meter to monitor the household's electricity usage.", "zh": "他安裝了一個智慧電表來監控家庭的用電量。"}
    ]
}

for item in data:
    word = item["word"]
    if word in examples_dict:
        item["examples"] = examples_dict[word]

    # Reorder keys
    new_item = {
        "id": item["id"],
        "word": item["word"],
        "part_of_speech": item["part_of_speech"],
        "meaning": item["meaning"],
        "examples": item["examples"]
    }
    item.clear()
    item.update(new_item)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Part 1 updated!")
