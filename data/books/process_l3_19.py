import json

file_path = r"d:\工具開發區\多益網頁遊戲專案\data\books\high_school_L3_19.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

extra_examples = {
    1: [
        {"english": "I ordered a bacon and cheese sandwich for lunch.", "chinese": "我午餐點了一份培根起司三明治。"},
        {"english": "Eating too much bacon is not good for your health.", "chinese": "吃太多培根對你的健康不好。"}
    ],
    2: [
        {"english": "The barber chatted with his customer while shaving his beard.", "chinese": "理髮師在幫客人刮鬍子時與他聊天。"},
        {"english": "My father learned to cut hair from an experienced barber.", "chinese": "我父親向一位經驗豐富的理髮師學習剪髮。"}
    ],
    3: [
        {"english": "These energy-saving bulbs last much longer than the old ones.", "chinese": "這些節能燈泡比舊的耐用得多。"},
        {"english": "The room went dark suddenly when the bulb shattered.", "chinese": "燈泡碎裂時，房間瞬間變暗了。"}
    ],
    4: [
        {"english": "The pilot announced that the cabin pressure was normal.", "chinese": "機長宣布機艙壓力正常。"},
        {"english": "We rented a small cabin near the lake for our summer vacation.", "chinese": "我們租了一間湖畔的小木屋度暑假。"}
    ],
    5: [
        {"english": "The strong wind blew down the chimney of the old house.", "chinese": "強風吹倒了老房子的煙囪。"},
        {"english": "Birds sometimes build their nests near the warm chimney.", "chinese": "鳥兒有時會在溫暖的煙囪附近築巢。"}
    ],
    6: [
        {"english": "The teacher used a paper clip to hold the test papers together.", "chinese": "老師用迴紋針把考卷夾在一起。"},
        {"english": "He was watching a short video clip on his smartphone.", "chinese": "他正在智慧型手機上看一段短片。"}
    ],
    7: [
        {"english": "In English, 'furniture' is an uncountable noun, while 'chair' is a countable one.", "chinese": "在英文中，'furniture'是不可數名詞，而'chair'是可數名詞。"},
        {"english": "Are there any countable benefits to this new policy?", "chinese": "這項新政策有任何具體可數的益處嗎？"}
    ],
    8: [
        {"english": "The story is about a young boy who befriends a magical fairy.", "chinese": "這個故事講述一個小男孩與一位神奇仙子做朋友的經歷。"},
        {"english": "She bought a beautiful fairy costume for Halloween.", "chinese": "她為萬聖節買了一套美麗的仙子服裝。"}
    ],
    9: [
        {"english": "The movie is based on a classic German fairy tale.", "chinese": "這部電影改編自經典的德國童話故事。"},
        {"english": "Sometimes reality is much more complex than a fairy tale.", "chinese": "有時現實比童話故事複雜得多。"}
    ],
    10: [
        {"english": "The city government spent millions on the National Day fireworks.", "chinese": "市政府在國慶煙火上花費了數百萬。"},
        {"english": "The loud bang of the firework scared the dog.", "chinese": "煙火巨大的爆炸聲嚇到了那隻狗。"}
    ],
    11: [
        {"english": "The school nurse took a bandage from the first-aid kit.", "chinese": "學校護理師從急救箱裡拿出一塊繃帶。"},
        {"english": "Every home should have a well-stocked first-aid kit.", "chinese": "每個家庭都應該準備一個物品齊全的急救箱。"}
    ],
    12: [
        {"english": "He bought two gallons of paint to decorate his bedroom.", "chinese": "他買了兩加侖的油漆來裝飾他的臥室。"},
        {"english": "The car gets about thirty miles to the gallon.", "chinese": "這輛車每加侖大約能跑三十英里。"}
    ],
    13: [
        {"english": "The nurse was very gentle when giving the injection.", "chinese": "護理師打針時非常溫柔。"},
        {"english": "A gentle touch on the shoulder gave him a lot of comfort.", "chinese": "肩膀上溫柔的觸碰給了他許多安慰。"}
    ],
    14: [
        {"english": "Plants grow faster in a greenhouse because of the trapped heat.", "chinese": "植物在溫室裡因為熱量被困住而生長得更快。"},
        {"english": "The university built a large greenhouse for agricultural research.", "chinese": "大學建造了一個大型溫室用於農業研究。"}
    ],
    15: [
        {"english": "Reducing carbon emissions can help slow down the greenhouse effect.", "chinese": "減少碳排放有助於減緩溫室效應。"},
        {"english": "The greenhouse effect traps the sun's heat in the Earth's atmosphere.", "chinese": "溫室效應將太陽的熱量困在地球大氣層中。"}
    ],
    16: [
        {"english": "I went to the salon to get a haircut before the job interview.", "chinese": "我在面試前去髮廊剪了頭髮。"},
        {"english": "His terrible haircut made him the laughingstock of the class.", "chinese": "他那糟糕的髮型讓他成了班上的笑柄。"}
    ],
    17: [
        {"english": "The hairdresser styled her hair beautifully for the prom.", "chinese": "美髮師為她的舞會做了一個漂亮的髮型。"},
        {"english": "A good hairdresser knows exactly what look suits their client best.", "chinese": "一位優秀的美髮師非常清楚什麼造型最適合他們的客戶。"}
    ],
    18: [
        {"english": "She flipped through a magazine to find a trendy hairstyle.", "chinese": "她翻閱雜誌尋找時髦的髮型。"},
        {"english": "Changing your hairstyle is an easy way to refresh your look.", "chinese": "改變髮型是煥然一新的簡單方法。"}
    ],
    19: [
        {"english": "The tiny turtles hatched and immediately crawled toward the ocean.", "chinese": "小海龜孵化後立刻爬向海洋。"},
        {"english": "They hatched a plot to overthrow the current government.", "chinese": "他們策劃了一場推翻現任政府的陰謀。"}
    ],
    20: [
        {"english": "The owl made its nest inside the hollow trunk of an old oak.", "chinese": "貓頭鷹在一棵老橡樹的空心樹幹裡築巢。"},
        {"english": "His apology rang hollow because he repeated the same mistake.", "chinese": "他的道歉顯得十分虛偽，因為他又犯了同樣的錯誤。"}
    ],
    21: [
        {"english": "The hotel housekeeper changed the bed sheets and provided fresh towels.", "chinese": "飯店房務員更換了床單並提供了乾淨的毛巾。"},
        {"english": "We need an honest housekeeper to manage our daily chores.", "chinese": "我們需要一位誠實的管家來處理日常家務。"}
    ],
    22: [
        {"english": "They exchanged a warm hug at the airport before parting ways.", "chinese": "他們在機場分道揚鑣前給了彼此一個溫暖的擁抱。"},
        {"english": "The frightened puppy hugged my leg and refused to let go.", "chinese": "那隻受驚的小狗緊緊抱住我的腿不肯放開。"}
    ],
    23: [
        {"english": "The fishermen built a simple hut on the beach to store their gear.", "chinese": "漁夫們在海灘上建了一個簡陋的小屋來存放裝備。"},
        {"english": "We found an empty hut deep in the forest during our hike.", "chinese": "在健行期間，我們在森林深處發現了一間空無一人的棚屋。"}
    ],
    24: [
        {"english": "The cartoon featured a boxing kangaroo with giant gloves.", "chinese": "這部卡通裡有一隻戴著巨大手套的拳擊袋鼠。"},
        {"english": "Kangaroos use their thick tails for balance when hopping.", "chinese": "袋鼠在跳躍時利用粗壯的尾巴來保持平衡。"}
    ],
    25: [
        {"english": "The emergency survival kit includes a flashlight and some rations.", "chinese": "緊急求生包裡包含一個手電筒和一些口糧。"},
        {"english": "He bought a drum kit and practiced playing it every evening.", "chinese": "他買了一套爵士鼓，並在每天傍晚練習。"}
    ],
    26: [
        {"english": "The koala's thick fur keeps it warm during cold nights.", "chinese": "無尾熊厚實的毛皮能讓牠在寒冷的夜晚保暖。"},
        {"english": "Habitat loss is a major threat to the survival of the koala.", "chinese": "棲息地喪失是無尾熊生存的一大威脅。"}
    ],
    27: [
        {"english": "Please carefully read the label on the medicine bottle before taking it.", "chinese": "服用前請仔細閱讀藥瓶上的標籤。"},
        {"english": "The media unfairly labeled him as a troublemaker.", "chinese": "媒體不公平地將他貼上麻煩製造者的標籤。"}
    ],
    28: [
        {"english": "Her vintage dress featured delicate lace around the collar.", "chinese": "她的復古洋裝領口周圍有精緻的蕾絲。"},
        {"english": "He stooped down to tie his shoelace before the race started.", "chinese": "比賽開始前，他彎下腰來綁鞋帶。"}
    ],
    29: [
        {"english": "I forgot my detergent, so I had to buy some at the laundromat.", "chinese": "我忘了帶洗衣精，只好在自助洗衣店買一些。"},
        {"english": "The old laundromat was closed down and replaced by a cafe.", "chinese": "那間舊的自助洗衣店倒閉了，取而代之的是一間咖啡館。"}
    ],
    30: [
        {"english": "She sorted the laundry into whites and colors before washing.", "chinese": "她在洗衣服前將衣物分為白色和彩色。"},
        {"english": "I have to do the laundry this weekend because I've run out of clean shirts.", "chinese": "這週末我必須洗衣服，因為我已經沒有乾淨的襯衫了。"}
    ],
    31: [
        {"english": "The plumber came to fix a severe leak in our bathroom.", "chinese": "水電工來修理我們浴室裡嚴重的漏水問題。"},
        {"english": "The company fired the employee who leaked the confidential report.", "chinese": "公司開除了那位洩漏機密報告的員工。"}
    ],
    32: [
        {"english": "The strong magnet easily picked up the scattered nails.", "chinese": "這塊強力磁鐵輕鬆吸起了散落的釘子。"},
        {"english": "The beautiful scenery makes this town a magnet for tourists.", "chinese": "美麗的風景使這個小鎮對遊客極具吸引力。"}
    ],
    33: [
        {"english": "I couldn't find my nail clipper, so I had to use small scissors.", "chinese": "我找不到我的指甲剪，只好用小剪刀。"},
        {"english": "The hotel provided complimentary toiletries, including a tiny nail clipper.", "chinese": "飯店提供了免費的盥洗用品，包括一把小小的指甲剪。"}
    ],
    34: [
        {"english": "The panda slowly munched on bamboo shoots in the enclosure.", "chinese": "貓熊在圍欄裡慢慢咀嚼著竹筍。"},
        {"english": "The birth of the twin pandas was celebrated all over the country.", "chinese": "全國上下都在慶祝這對雙胞胎貓熊的誕生。"}
    ],
    35: [
        {"english": "The hikers were exhausted when they finally reached the peak.", "chinese": "登山客最終抵達山頂時已經筋疲力盡了。"},
        {"english": "The hotel rates are much higher during the peak season.", "chinese": "飯店的房價在旺季時高出許多。"}
    ],
    36: [
        {"english": "She received a pair of elegant pearl earrings for her anniversary.", "chinese": "她收到了一副優雅的珍珠耳環作為週年紀念禮物。"},
        {"english": "The divers risk their lives searching for precious pearls in the ocean.", "chinese": "潛水員冒著生命危險在海洋中尋找珍貴的珍珠。"}
    ],
    37: [
        {"english": "He drank a pint of water to quench his thirst.", "chinese": "他喝了一品脫的水來解渴。"},
        {"english": "Would you like to join us for a pint after work?", "chinese": "下班後你想跟我們一起去喝杯啤酒嗎？"}
    ],
    38: [
        {"english": "They printed a thousand posters to promote the school fair.", "chinese": "他們印了一千張海報來宣傳學校園遊會。"},
        {"english": "Her room is decorated with posters of her favorite pop bands.", "chinese": "她的房間裡裝飾著她最喜歡的流行樂團的海報。"}
    ],
    39: [
        {"english": "He accidentally cut his chin while shaving with a dull razor.", "chinese": "他用鈍刮鬍刀刮鬍子時不小心割傷了下巴。"},
        {"english": "The barber used a straight razor to give him a precise shave.", "chinese": "理髮師用一把直剃刀為他精準地刮鬍子。"}
    ],
    40: [
        {"english": "You should dispose of used razor blades safely in a proper container.", "chinese": "你應該將用過的刮鬍刀片安全地丟棄在合適的容器中。"},
        {"english": "A rusty razor blade can cause a serious infection.", "chinese": "生鏽的刮鬍刀片可能會引起嚴重的感染。"}
    ],
    41: [
        {"english": "The tennis player reached her peak when she won the grand slam.", "chinese": "這位網球選手在贏得大滿貫時達到了她的巔峰。"},
        {"english": "Economic growth is expected to reach its peak next quarter.", "chinese": "經濟成長預計將在下個季度達到巔峰。"}
    ],
    42: [
        {"english": "These ready-made curtains perfectly match the color of my room.", "chinese": "這些現成的窗簾和我的房間顏色完美搭配。"},
        {"english": "He submitted a ready-made business plan he found online.", "chinese": "他提交了一份在網路上找到的現成商業企劃書。"}
    ],
    43: [
        {"english": "The newspaper revealed the scandal involving the corrupt politician.", "chinese": "報紙揭露了那位腐敗政客的醜聞。"},
        {"english": "The curtain was drawn back to reveal a magnificent painting.", "chinese": "拉開窗簾後，展示出一幅宏偉的畫作。"}
    ],
    44: [
        {"english": "I bought some spicy Italian sausage for tonight's pasta dish.", "chinese": "我買了一些辣味義大利香腸來做今晚的義大利麵。"},
        {"english": "The factory produces tons of pork sausage every single day.", "chinese": "這家工廠每天生產數噸的豬肉香腸。"}
    ],
    45: [
        {"english": "The shopkeeper chased away the stray dog that entered his store.", "chinese": "店主把跑進他店裡的流浪狗趕走了。"},
        {"english": "An honest shopkeeper always returns the exact change to his customers.", "chinese": "誠實的商店老闆總是會找給顧客正確的零錢。"}
    ],
    46: [
        {"english": "She twirled the spaghetti on her fork like a professional.", "chinese": "她像個專業人士一樣用叉子捲起義大利麵。"},
        {"english": "This restaurant is famous for its authentic homemade spaghetti.", "chinese": "這家餐廳以道地的手工義大利麵聞名。"}
    ],
    47: [
        {"english": "Nutmeg is a popular spice used in many traditional recipes.", "chinese": "肉豆蔻是許多傳統食譜中常用的熱門香料。"},
        {"english": "She tries to spice up her daily routine by learning new hobbies.", "chinese": "她試圖透過學習新嗜好來為日常作息增添情趣。"}
    ],
    48: [
        {"english": "Without food and water, the lost explorer would surely starve.", "chinese": "沒有食物和水，迷路的探險家肯定會餓死。"},
        {"english": "The long drought caused the cattle to starve in the fields.", "chinese": "長期的乾旱導致牛隻在田野中餓死。"}
    ],
    49: [
        {"english": "The starving refugees gratefully accepted the bread and water.", "chinese": "飢餓的難民滿懷感激地接受了麵包和水。"},
        {"english": "We rushed to the cafeteria because we were absolutely starving.", "chinese": "我們衝向自助餐廳，因為我們實在快餓扁了。"}
    ],
    50: [
        {"english": "The expedition team finally planted their flag at the summit.", "chinese": "探險隊終於在山峰上插上了他們的旗幟。"},
        {"english": "The upcoming summit will focus on environmental protection policies.", "chinese": "即將舉行的高峰會將著重於環境保護政策。"}
    ],
    51: [
        {"english": "She forgot to remove the price tag before wrapping the gift.", "chinese": "她在包裝禮物前忘了撕下價格標籤。"},
        {"english": "The scientists tagged the wild dolphins to track their migration.", "chinese": "科學家在野生海豚身上附上標籤以追蹤牠們的遷徙。"}
    ],
    52: [
        {"english": "He decided to tag along when we went grocery shopping.", "chinese": "當我們去買日常用品時，他決定跟著去。"},
        {"english": "I don't mind if you tag along to the library.", "chinese": "我不介意你跟著去圖書館。"}
    ],
    53: [
        {"english": "The royal tailor crafted an exquisite gown for the princess.", "chinese": "皇家裁縫為公主製作了一件精美的禮服。"},
        {"english": "My grandfather always went to the same tailor for his trousers.", "chinese": "我爺爺總是去同一位裁縫那裡訂做褲子。"}
    ],
    54: [
        {"english": "The software was tailor-made to meet the specific needs of our company.", "chinese": "這套軟體是為滿足我們公司的特定需求而量身打造的。"},
        {"english": "He proudly wore his newly arrived tailor-made jacket.", "chinese": "他驕傲地穿著剛收到的訂做夾克。"}
    ],
    55: [
        {"english": "It's cruel to tease an animal that is locked in a cage.", "chinese": "取笑被關在籠子裡的動物是很殘忍的。"},
        {"english": "Her older brothers would constantly tease her about her crush.", "chinese": "她的哥哥們經常拿她暗戀的對象來取笑她。"}
    ],
    56: [
        {"english": "The chicken was slow-cooked until it became perfectly tender.", "chinese": "雞肉經過慢火燉煮，直到變得非常軟嫩。"},
        {"english": "He sang a tender lullaby to help his daughter fall asleep.", "chinese": "他唱了一首溫柔的搖籃曲，哄女兒入睡。"}
    ],
    57: [
        {"english": "She was touched by the unexpected tenderness in his voice.", "chinese": "他聲音中出乎意料的溫柔讓她很感動。"},
        {"english": "The tenderness of this roasted beef is simply unbelievable.", "chinese": "這塊烤牛肉的軟嫩度簡直令人難以置信。"}
    ],
    58: [
        {"english": "Surviving in the desert requires a tough mindset and preparation.", "chinese": "在沙漠中生存需要堅強的心智和準備。"},
        {"english": "The boss is known for his tough negotiation skills.", "chinese": "這位老闆以他強硬的談判技巧聞名。"}
    ],
    59: [
        {"english": "His former math tutor helped him pass the difficult entrance exam.", "chinese": "他的前數學家教幫他通過了困難的入學考試。"},
        {"english": "She volunteers to tutor disadvantaged children in the community.", "chinese": "她自願為社區裡的弱勢兒童提供個別指導。"}
    ],
    60: [
        {"english": "The concept of 'information' is considered an uncountable noun.", "chinese": "「資訊」這個概念被視為不可數名詞。"},
        {"english": "Words like 'music' and 'love' are usually uncountable.", "chinese": "像「音樂」和「愛」這樣的詞彙通常是不可數的。"}
    ],
    61: [
        {"english": "The floor was shining brightly after the janitor waxed it.", "chinese": "工友打蠟後，地板閃閃發亮。"},
        {"english": "She dripped some hot wax to seal the envelope completely.", "chinese": "她滴了一些熱蠟將信封完全封住。"}
    ],
    62: [
        {"english": "The strict exam is designed to weed out unqualified applicants.", "chinese": "這項嚴格的考試旨在淘汰不合格的申請者。"},
        {"english": "The garden is overgrown with weeds and needs a lot of work.", "chinese": "花園裡長滿了雜草，需要花很多功夫整理。"}
    ],
    63: [
        {"english": "Whole wheat bread is generally considered healthier than white bread.", "chinese": "全麥麵包通常被認為比白麵包更健康。"},
        {"english": "The local economy relies heavily on the production of wheat.", "chinese": "當地經濟嚴重依賴小麥的生產。"}
    ],
    64: [
        {"english": "The guard blew his whistle to warn the approaching hikers.", "chinese": "守衛吹響哨子警告正在靠近的登山客。"},
        {"english": "She taught her little brother how to whistle using his fingers.", "chinese": "她教她弟弟如何用手指吹口哨。"}
    ],
    65: [
        {"english": "The knight fought bravely to defeat the wicked dragon.", "chinese": "騎士英勇奮戰以打敗邪惡的龍。"},
        {"english": "Spreading such false rumors is a truly wicked thing to do.", "chinese": "散布這樣的虛假謠言真是一件邪惡的事。"}
    ]
}

keys_order = ["id", "word", "part_of_speech", "meaning", "examples"]
out_data = []

for item in data:
    word_id = item["id"]
    if word_id in extra_examples:
        for ex in extra_examples[word_id]:
            if len(item["examples"]) < 5:
                item["examples"].append(ex)
    
    new_item = {k: item[k] for k in keys_order if k in item}
    out_data.append(new_item)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=4)

print("Done processing L3_19.json")
