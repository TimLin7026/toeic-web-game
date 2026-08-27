import json
import sys

file_path = r'd:\工具開發區\多益網頁遊戲專案\data\books\high_school_L3_20.json'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print('Error reading:', e)
    sys.exit(1)

new_examples = {
    1: [
        {'en': 'Winning the lottery was a chance of a lifetime for the struggling artist.', 'zh': '中樂透對這位苦苦掙扎的藝術家來說是一生難得的機會。'},
        {'en': 'The internship at the renowned tech company is truly a chance of a lifetime.', 'zh': '在這家知名科技公司實習真是一生難得的機會。'}
    ],
    2: [
        {'en': 'The fireworks exploded with a massive bang.', 'zh': '煙火伴隨著巨大的砰聲爆炸了。'},
        {'en': 'He banged his knee against the edge of the desk.', 'zh': '他的膝蓋猛撞到了書桌的邊緣。'}
    ],
    3: [
        {'en': 'She accidentally spilled coffee on her favorite white blouse.', 'zh': '她不小心把咖啡灑在最喜歡的白色女襯衫上。'},
        {'en': 'The boutique sells a variety of elegant blouses for women.', 'zh': '這家精品店販售各種優雅的女裝襯衫。'}
    ],
    4: [
        {'en': 'The soldier was honored for his remarkable bravery in battle.', 'zh': '這名士兵因在戰鬥中的非凡勇氣而受到表揚。'},
        {'en': 'It requires bravery to speak the truth in difficult situations.', 'zh': '在困難的情況下說出真相需要勇氣。'}
    ],
    5: [
        {'en': 'The pine tree dropped several cones onto the lawn.', 'zh': '松樹掉落了幾個松果在草坪上。'},
        {'en': 'The dog had to wear a plastic cone after its surgery.', 'zh': '這隻狗在手術後必須戴上塑膠頸圈（伊莉莎白圈）。'}
    ],
    6: [
        {'en': 'He spent his Sunday afternoon playing cricket with his friends.', 'zh': '他星期天下午和朋友們一起打板球。'},
        {'en': 'The silent night was only disturbed by a lone cricket.', 'zh': '寧靜的夜晚只被一隻孤獨的蟋蟀打擾。'}
    ],
    7: [
        {'en': 'The dog tried to drag the heavy branch across the yard.', 'zh': '狗試圖把沉重的樹枝拖過院子。'},
        {'en': 'I had to drag myself out of bed this morning because I was so tired.', 'zh': '今天早上我太累了，只好硬把自己從床上拖起來。'}
    ],
    8: [
        {'en': 'If you keep dragging your feet, we will miss the train.', 'zh': '如果你繼續拖拖拉拉，我們就會錯過火車。'},
        {'en': 'The committee dragged its heels in making a final decision.', 'zh': '委員會在做出最終決定時拖泥帶水。'}
    ],
    9: [
        {'en': 'Whip the egg whites until stiff peaks form.', 'zh': '將蛋白攪打至挺立起泡。'},
        {'en': 'She used only egg whites to make a healthier omelet.', 'zh': '她只用蛋白來做更健康的歐姆蛋。'}
    ],
    10: [
        {'en': 'The movie was very enjoyable and kept me entertained throughout.', 'zh': '這部電影非常有趣，讓我從頭到尾都覺得很享受。'},
        {'en': 'We had an enjoyable conversation over a cup of tea.', 'zh': '我們喝著茶，進行了愉快的交談。'}
    ],
    11: [
        {'en': 'The painting turned out to be a clever fake rather than an original.', 'zh': '這幅畫結果是一件巧妙的贗品，而不是真跡。'},
        {'en': 'She wore fake eyelashes to make her eyes look bigger.', 'zh': '她戴了假睫毛讓眼睛看起來更大。'}
    ],
    12: [
        {'en': 'The grasshopper blended perfectly with the green leaves.', 'zh': '這隻蚱蜢與綠葉完美地融為一體。'},
        {'en': 'A swarm of grasshoppers destroyed the entire crop.', 'zh': '一群蚱蜢摧毀了整片農作物。'}
    ],
    13: [
        {'en': 'The celebrity arrived at the premiere with her entourage in tow.', 'zh': '這位名流帶著她的隨從一起來到首映會。'},
        {'en': 'He walked into the office with a huge pile of documents in tow.', 'zh': '他走進辦公室，隨後拖著一大疊文件。'}
    ],
    14: [
        {'en': 'The birth of their first child was a highly joyful event.', 'zh': '他們第一個孩子的出生是一件非常喜悅的事。'},
        {'en': 'The children greeted their grandparents with joyful shouts.', 'zh': '孩子們用歡樂的叫聲迎接他們的祖父母。'}
    ],
    15: [
        {'en': 'She spent a lifetime fighting for women\'s rights.', 'zh': '她花了一生的時間為女權奮鬥。'},
        {'en': 'This sturdy leather bag is guaranteed to last a lifetime.', 'zh': '這款堅固的皮包保證能用一輩子。'}
    ],
    16: [
        {'en': 'The beam from the lighthouse cut through the thick fog.', 'zh': '燈塔的光束穿透了濃霧。'},
        {'en': 'The lighthouse keeper lived a lonely but peaceful life.', 'zh': '燈塔看守人過著孤獨但平靜的生活。'}
    ],
    17: [
        {'en': 'The elegant lily is often associated with funerals in some cultures.', 'zh': '在某些文化中，優雅的百合花常與葬禮有關。'},
        {'en': 'She planted tiger lilies along the garden fence.', 'zh': '她沿著花園圍欄種植了卷丹百合。'}
    ],
    18: [
        {'en': 'The doctor carefully examined her injured limb.', 'zh': '醫生仔細檢查了她受傷的肢體。'},
        {'en': 'A large limb snapped off the oak tree during the fierce storm.', 'zh': '在猛烈的暴風雨中，橡樹上的一根大樹枝折斷了。'}
    ],
    19: [
        {'en': 'He unwrapped a large, colorful lollipop at the carnival.', 'zh': '他在嘉年華上拆開了一支五顏六色的大棒棒糖。'},
        {'en': 'The little girl dropped her lollipop in the dirt and started crying.', 'zh': '小女孩把棒棒糖掉在泥土裡，開始哭了起來。'}
    ],
    20: [
        {'en': 'I spent hours looking for the missing document on my desk.', 'zh': '我花了幾個小時在桌上尋找那份遺失的文件。'},
        {'en': 'Two climbers went missing after an avalanche hit the mountain.', 'zh': '雪崩襲擊山脈後，兩名登山者失蹤了。'}
    ],
    21: [
        {'en': 'His peers nicknamed him "Brain" because of his incredible intelligence.', 'zh': '他的同儕因為他驚人的聰明才智給他取了個綽號叫「大腦」。'},
        {'en': 'The city is affectionately known by its nickname, the Big Apple.', 'zh': '這座城市以其綽號「大蘋果」而為人所熟知。'}
    ],
    22: [
        {'en': 'He placed a heating pad on his sore back to relieve the pain.', 'zh': '他把加熱護墊放在痠痛的背上以緩解疼痛。'},
        {'en': 'She jotted down the phone number on a small scratch pad.', 'zh': '她在一個小巧的便簽本上草草記下了電話號碼。'}
    ],
    23: [
        {'en': 'You should not crush the pill before swallowing it.', 'zh': '你在吞嚥藥丸之前不應該把它壓碎。'},
        {'en': 'The bitter pill was hard for the child to swallow.', 'zh': '這顆苦藥丸讓小孩很難吞下。'}
    ],
    24: [
        {'en': 'He threw a powerful punch that knocked his opponent down.', 'zh': '他揮出一記有力的重拳，將對手擊倒。'},
        {'en': 'Please punch a hole in the top left corner of the paper.', 'zh': '請在紙的左上角打一個洞。'}
    ],
    25: [
        {'en': 'The abandoned house had a queer atmosphere that made everyone uneasy.', 'zh': '這棟廢棄的房子有一種古怪的氣氛，讓每個人都感到不安。'},
        {'en': 'He gave me a queer look when I suggested the unusual idea.', 'zh': '當我提出這個不尋常的主意時，他用一種奇怪的眼神看著我。'}
    ],
    26: [
        {'en': 'My mother prepared a delicious roast pork for the family gathering.', 'zh': '我媽媽為家庭聚會準備了美味的烤豬肉。'},
        {'en': 'We bought a bag of freshly roasted coffee beans.', 'zh': '我們買了一包新鮮烘焙的咖啡豆。'}
    ],
    27: [
        {'en': 'Resources were scarce, so everyone had to ration their supplies.', 'zh': '資源稀少，所以每個人都必須配給他們的物資。'},
        {'en': 'Genuine empathy seems to be a scarce commodity these days.', 'zh': '如今，真誠的同理心似乎是一種稀缺的特質。'}
    ],
    28: [
        {'en': 'She knitted a long red scarf for her boyfriend.', 'zh': '她為男朋友織了一條長長的紅圍巾。'},
        {'en': 'The wind blew her scarf away while she was walking on the bridge.', 'zh': '她走在橋上時，風把她的圍巾吹走了。'}
    ],
    29: [
        {'en': 'The rollercoaster ride was a bit too scary for my younger sister.', 'zh': '搭雲霄飛車對我妹妹來說有點太可怕了。'},
        {'en': 'He told a scary ghost story around the campfire.', 'zh': '他在營火旁講了一個嚇人的鬼故事。'}
    ],
    30: [
        {'en': 'The talent scout discovered her singing in a small local bar.', 'zh': '星探在當地一家小酒吧發現了正在唱歌的她。'},
        {'en': 'They scouted the area for a suitable place to set up camp.', 'zh': '他們在該地區偵察，尋找適合紮營的地方。'}
    ],
    31: [
        {'en': 'She took a tentative sip of the hot soup to see if it was too spicy.', 'zh': '她試探性地啜飲了一小口熱湯，看是否太辣。'},
        {'en': 'He sipped his cold beer slowly on the sunny terrace.', 'zh': '他在陽光明媚的露臺上慢慢啜飲著冷啤酒。'}
    ],
    32: [
        {'en': 'He accidentally sliced his finger while cutting onions.', 'zh': '他切洋蔥時不小心切到了手指。'},
        {'en': 'Could you cut me a thin slice of bread, please?', 'zh': '請你幫我切一片薄薄的麵包好嗎？'}
    ],
    33: [
        {'en': 'He was so nervous that he spilled his drink on the floor.', 'zh': '他緊張到把飲料灑在地板上。'},
        {'en': 'Tears spilled down her cheeks as she read the emotional letter.', 'zh': '當她讀那封感人的信時，眼淚滑落了她的臉頰。'}
    ],
    34: [
        {'en': 'A drop of paint splashed onto his crisp white shirt.', 'zh': '一滴油漆濺到了他挺括的白襯衫上。'},
        {'en': 'The news of their sudden marriage made quite a splash in the media.', 'zh': '他們突然結婚的消息在媒體上引起了不小的轟動。'}
    ],
    35: [
        {'en': 'We had to push our bicycles up the steep hill.', 'zh': '我們不得不把腳踏車推上陡峭的山坡。'},
        {'en': 'The steep rise in housing prices makes it hard for young people to buy a home.', 'zh': '房價的急劇上漲讓年輕人很難買房。'}
    ],
    36: [
        {'en': 'The car struggled to climb the steep slope due to the icy road.', 'zh': '由於路面結冰，車子很難爬上這個陡坡。'},
        {'en': 'The house was built on a gentle slope overlooking the sea.', 'zh': '這棟房子建在一個俯瞰大海的緩坡上。'}
    ],
    37: [
        {'en': 'The alcohol on the wound caused a sharp sting.', 'zh': '酒精碰到傷口引起了一陣劇烈的刺痛。'},
        {'en': 'Jellyfish can sting swimmers who get too close.', 'zh': '水母會刺痛靠得太近的游泳者。'}
    ],
    38: [
        {'en': 'She dropped a stitch while knitting the sweater.', 'zh': '她織毛衣時漏了一針。'},
        {'en': 'He laughed so hard that he got a stitch in his side.', 'zh': '他笑得太厲害，以至於肚子抽痛。'}
    ],
    39: [
        {'en': 'The stormy sea tossed the small boat around like a toy.', 'zh': '暴風雨肆虐的海洋把這艘小船像玩具一樣拋來拋去。'},
        {'en': 'The meeting ended after a stormy debate over the new policy.', 'zh': '會議在對新政策進行了激烈的辯論後結束。'}
    ],
    40: [
        {'en': 'The mosquito landed on his arm to suck his blood.', 'zh': '蚊子停在他的手臂上吸血。'},
        {'en': 'It sucks to be stuck in traffic for two hours.', 'zh': '塞車塞了兩個小時真是太糟糕了。'}
    ],
    41: [
        {'en': 'He felt like a sucker for believing the salesman\'s lies.', 'zh': '他覺得自己相信推銷員的謊言真是個容易受騙的傻瓜。'},
        {'en': 'The toy has rubber suckers that stick to the window.', 'zh': '這個玩具有能黏在窗戶上的橡膠吸盤。'}
    ],
    42: [
        {'en': 'He swallowed a pain relief tablet with a glass of water.', 'zh': '他配著一杯水吞下了一片止痛藥片。'},
        {'en': 'Tablets are convenient for watching movies while traveling.', 'zh': '平板電腦在旅行時用來看電影很方便。'}
    ],
    43: [
        {'en': 'The lion at the zoo seemed surprisingly tame and lazy.', 'zh': '動物園裡的獅子看起來出奇地馴服且慵懶。'},
        {'en': 'She tried to tame her frizzy hair with various hair products.', 'zh': '她試著用各種美髮產品來撫平她毛躁的頭髮（使馴服）。'}
    ],
    44: [
        {'en': 'I am thankful for the opportunity to work with such a great team.', 'zh': '我很感激有機會與這麼棒的團隊合作。'},
        {'en': 'The rescued hikers were thankful to be alive.', 'zh': '獲救的登山客對能活著感到感激。'}
    ],
    45: [
        {'en': 'Being an umpire is often a thankless task, as fans always complain.', 'zh': '當裁判通常是個不討好的工作，因為球迷總是抱怨。'},
        {'en': 'She resigned from the committee, exhausted by the thankless nature of the role.', 'zh': '她辭去了委員會的職務，對這個職位吃力不討好的性質感到疲憊。'}
    ],
    46: [
        {'en': 'They wandered the desert, desperate with hunger and thirst.', 'zh': '他們在沙漠中徘徊，飢渴難耐。'},
        {'en': 'Her thirst for adventure led her to travel the world.', 'zh': '她對冒險的渴望驅使她環遊世界。'}
    ],
    47: [
        {'en': 'The long hike left us hot, tired, and incredibly thirsty.', 'zh': '長途跋涉讓我們感到炎熱、疲憊，而且極度口渴。'},
        {'en': 'The ambitious politician was thirsty for power.', 'zh': '這位野心勃勃的政治家渴望權力。'}
    ],
    48: [
        {'en': 'The tractor was used to tow the stuck vehicle out of the mud.', 'zh': '牽引機被用來把卡住的車輛從泥淖中拖出來。'},
        {'en': 'He got a parking ticket and his car was towed.', 'zh': '他收到了一張違規停車罰單，而且車子被拖走了。'}
    ],
    49: [
        {'en': 'The tow truck driver carefully hooked up the damaged car.', 'zh': '拖吊車司機小心翼翼地掛上受損的汽車。'},
        {'en': 'We waited on the side of the road for the tow truck to arrive.', 'zh': '我們在路邊等待拖吊車的到來。'}
    ],
    50: [
        {'en': 'You must promise to be truthful when you answer my questions.', 'zh': '當你回答我的問題時，你必須答應要說實話。'},
        {'en': 'The documentary provided a truthful representation of the historical event.', 'zh': '這部紀錄片真實地呈現了這個歷史事件。'}
    ],
    51: [
        {'en': 'The flowers in the vase began to wilt after a few days.', 'zh': '花瓶裡的花幾天後開始枯萎。'},
        {'en': 'He filled the crystal vase with water before adding the tulips.', 'zh': '他在加上鬱金香之前，先把水晶花瓶裝滿了水。'}
    ],
    52: [
        {'en': 'A bright yellow reflective vest is required for construction workers.', 'zh': '建築工人必須穿著亮黃色的反光背心。'},
        {'en': 'He unbuttoned his vest after eating a large meal.', 'zh': '吃了一頓大餐後，他解開了背心的釦子。'}
    ],
    53: [
        {'en': 'The sunset painted the sky in shades of pink and violet.', 'zh': '夕陽將天空染成了粉紅色和藍紫色的色調。'},
        {'en': 'She gently watered the potted violets on the windowsill.', 'zh': '她輕輕地為窗台上的盆栽紫羅蘭澆水。'}
    ],
    54: [
        {'en': 'The recipe uses three egg yolks to make the rich custard.', 'zh': '這份食譜使用三個蛋黃來製作濃郁的卡士達醬。'},
        {'en': 'He prefers his fried eggs with a runny yolk.', 'zh': '他喜歡吃蛋黃未熟透的煎蛋。'}
    ],
    55: [
        {'en': 'Make sure to zip the tent tightly to keep the bugs out.', 'zh': '一定要把帳篷的拉鍊拉緊，以防止蟲子飛進來。'},
        {'en': 'She unzipped her purse to find her keys.', 'zh': '她拉開錢包的拉鍊尋找鑰匙。'}
    ],
    56: [
        {'en': 'The zipper got stuck halfway down the jacket.', 'zh': '拉鍊卡在外套一半的地方。'},
        {'en': 'He asked the tailor to replace the broken zipper on his pants.', 'zh': '他請裁縫師更換他褲子上壞掉的拉鍊。'}
    ]
}

for item in data:
    word_id = item.get('id')
    ordered_item = {
        'id': item.get('id'),
        'word': item.get('word'),
        'part_of_speech': item.get('part_of_speech'),
        'meaning': item.get('meaning'),
        'examples': item.get('examples', [])
    }
    if word_id in new_examples:
        current_len = len(ordered_item['examples'])
        if current_len < 5:
            needed = 5 - current_len
            ordered_item['examples'].extend(new_examples[word_id][:needed])
    item.clear()
    item.update(ordered_item)

try:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('Successfully updated', file_path)
except Exception as e:
    print('Error writing:', e)
