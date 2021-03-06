﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Semen")
define a = Character("Рассказчик")

# The game starts here.
image bg starting room = im.Scale("bg starting room.jpg", 1600, 900)
image bg forest trail = im.Scale("bg forest.jpg", 1600, 900)
image bg village night2 = im.Scale("bg village night2.jpg", 1920, 1080)

define hasFought = 0

label start:
    #renpy.movie_cutscene("On_Your_Mark.webm")
    play music "audio/forest_song.mp3"

    scene bg black screen

    a "Торговый караван нашего героя в течении нескольких месяцев путешествовал по соседним городам."
    a "Юный герой путешествует с родителями в повозке, возвращаясь в родную деревню Ривервуд."
    a "Сквозь сон он слышит звуки боя."

    play sound "audio/female_scream.mp3"
    "Женский голос" "АААААА!"

    scene bg forest trail
    show anthony_1 with fade

    a "Герой быстро выпрыгивает из повозки и видит разбойников. Среди толпы он замечает, как его отец сражается с разбойником."
    a "Герой обращает внимание на уродливый шрам на щеке разбойника."
    a "Времени на раздумья нет."

    menu:
           "Попробовать убежать":
                scene bg village night2
                a "Герой бежит изо всех сил в сторону деревни. После многочасового бега он достигает деревни."
                a "Герой видит знакомые дома, в которых горит свет, как вдруг в глазах все темеет." 
                a "Герой теряет сознание от усталости."
                jump home

           "Попробовать напасть на разбойников":
                a "Герой пытается найти что-нибудь, что может сойти за оружие. Его взгляд падает на палку, лежащую в углу повозке."
                a "Пытаясь дотянуться, он чувствует резкую боль в голове"
                $hasFought = 1
                jump hunters_house

#image bg town center = im.Scale("images/bg town center.jpg", 1600, 900)
define elder = Character("Элайджа")
define seekHouse = 0
define hasWeapon = 0
define money = 0

label home:

    scene bg home morning

    if hasFought == 0:
        show anthony_1 at right with fade
        a "Проснувшись, герой оглядывается..."
        show elder at left with fade 
        a "В углу комнаты герой замечает старика. Он узнает старейшину деревни."
        elder "Проснулся? Тебя нашел стражник, патрулировавший улицу. Расскажи, что произошло."
        e "На нас напали разбойники."
        elder "Ты запомнил кого-то из нападавших?"
        e "Я помню как вышел из повозки... Отец..."
        e "Кто-то вернулся из каравана?"
        elder "К сожалению, до сих пор никто не вернулся. Нашу деревню уже долгое время терроризирует шайка разбойников. Они называют себя \"Кровавый клык\""
    else:
        show anthony_1 with fade
        a "Герой приходит домой." 

    menu: 
        "Осмотреть дом":
            "Дом кажется совсем пустым. Каждая вещь в доме напонимает герою о родителях. Взяв себя в руки, он решает осмотреть дом. "
            "Потратив на это немного времени, герой находит ржавый меч, оставленный отцом, и пару золотых монет."
            $money = 3
            $hasWeapon = 1
            $seekHouse = 1
            "После этого герой решает выйти из дома."
            jump village

        "Отправиться в деревню":
            jump village

image bg village day = im.Scale("bg village day.jpg", 1920, 1080)
image bg backstreet = im.Scale("bg backstreet.jpg", 1920, 1080)
define veteran = Character("Фуджитора")
label village:

    play music "audio/village_day.mp3"

    scene bg village day

    show anthony_1

    a "Наш герой решает отправиться в таверну, чтобы распросить про выживших из каравана."

    if(seekHouse == 0):
        hide anthony_1
        show anthony_1 at left
        show veteran at right with fade
        a "По дороге в таверну герой встречает ветерана войны Ирвина Фуджитора."
        if hasFought == 0:
            a "Фуджитора встречает его с крайним пренебрежением."
            veteran "Я удивлен, что такой слабак как ты смог выжить в этой бойне. Все уже говорят о твоем побеге."
            veteran "Во время войны за такое тебя бы пустили под трибунал или казнили бы на месте!"
            a "Герой знал, что Ирвин недолюбливает слабых, но не ожидал, что тот не проявит никакого сочувствия."
            e "Я потерял все, что у меня было в этой бойне и не намерен выслушивать замечания старика, вышедшего из ума!"
            a "Герой проходит мимо Ирвина и слышит в свою сторону: "
            veteran "В той бойне лучше бы умер ты, а не твои родители!"
            hide veteran with fade
            show anthony_1 at center
            a "Сокрушенный этими словами герой бредет в сторону таверны"
        else:
            a "Фуджитора встречает его с крайним пренебрежением."
            veteran "Ты слаб. Твоя попытка помочь своим родителям ни к чему не привела. Но похвально то, что ты хотя бы попытался."
            veteran "В тебе есть зародыш сильного бойца. Малец, я готов тебе помочь с этим, если ты выполнишь одну мою просьбу."
            veteran "Я как вижу, кишка у тебя не тонка."
            a "Герой был удивлен, как старик решил воспользоваться ситуацией для своей выгоды."
            a "Но в тот же момент он решил, что нет смысла сдавать назад. Если он поинтересуется, в чем состоит задание, то ничего не потеряет."
            e "Старик, ты очень \"тактичен\". Что же у тебя за просьба такая?"
            veteran "На деревенском кладбище похоронены мои товарищи, мои братья по мечу, но их души не упокоены."
            veteran "И каждую ночь, смотря в стороу кладбища, мое сердце обливается кровью."
            e "Очень печальная история, но чем я могу помочь?"
            veteran "Попробуй упокоить их души. Если преуспеешь, я тебе дам знание, которое ни в одной книжке не описаны."

            menu:
                "Согласиться":
                    e "Хорошо, я попытаюсь. С чего же мне начать?"
                    veteran "Кишка у тебя все таки не тонка. Малец, пойди в местную церквушку. Священник что-то должен об этом знать."
                    jump church
    
    scene bg backstreet
    show anthony_1
    play sound "audio/battle_sound1.mp3"
    a "Пройдя несколько домов, в переулке Хиро замечает людей, которые избивают молодого человека."

    menu:
        "Какое решение примет герой?"

        "Помочь молодому человеку":
            jump patrick_battle

        "Не обращать внимания и равнодушно идти в таверну":
            jump tavern

define bandicut = Character("Бандикут")
image bg tavern = im.Scale("bg tavern2.jpg", 1920, 1080)
image bg village night2 = im.Scale("bg village night2.jpg", 1920, 1080)

label tavern:

    play music "audio/tavern_music.mp3"

    scene bg tavern

    show anthony_1 with fade

    a "Зайдя в таверну, герой замечает, что все взгляды направлены к нему. Все начали перешептываться."
    a "Герой замечает за дальным столом друга семьи, стражника Бандикута. Подойдя к нему ближе, герой понял, что тот пьян."
    a "Бандикут заметил его и с лицом полным печали сказал:"
    bandicut "Ну что, мальчик-который-выжил, присаживайся, поговорим."
    a "Герой садится напротив старого друга семьи."
    bandicut "Я рад тебя видеть в здравии. Эй! Вы там! Налейте пива мне и моему другу тоже!"
    e "Я тоже рад тебя видеть. В караване есть выжившие кроме меня?"
    a "Официантка кладет на стол 2 бокала пенного"
    bandicut "Наши люди прочесывают тракт, но до сих пор ни следа выживших. Караван разграблен под чистую."
    e "Ты знаешь, кто стоит за нападением?"
    bandicut "Элайджа утверждает что это Кровавые клыки, во главе с Осфальдом. Они поселились в нашем лесу пару месяцев назад. Грабят всех без разбору."
    e "Так нужно их найти и наказать. Куда смотрит стража?"
    bandicut "Стража тут бессильна. Лес вне нашей юрисдикции. Только ты сейчас можешь что-то изменить."
    bandicut "Ты обязан найти Осфальда и отомстить за свою семью."
    e "Я не уверен, что я смогу что-то сделать. Мне нужно время, чтобы оклиматься. Но я обещаю, что подумаю над этим."
    a "Весь остальной вечер герой и Бандикут напивались пивом и вспоминали былые времена."
    scene bg village night2
    a "Поздно ночью герой отправляется домой."
    jump homecoming

define patrick = Character("Патрик")

label patrick_battle:
    
    if (hasWeapon == 1):
        a "Герой без колебаний бросается в бой."
        "Алкаш 1" "Ты кто такой? Уходи по хорошему."
        a "Герой бьет ближнего обидчика ржавым мечом, сбивая его с ног."
        a "В это же время второй алкаш пытается ударить героя кулаком. Герой не обладая ловкостью пропускает удар в лицо"
        a "Пошатнувшись, но удержав равновесие, герой снова наносит удар, ошеломив противника. Следующим ударом отправляет противника в нокаут."
        a "Третий обидчик, испугавшись увиденного, убегает в страхе."
        a "Герой протягивает руку молодому парню, лежащему на земле."
        patrick "Я бы и сам справился."
        e "Оно и видно. За что они тебя так?"
        patrick "Придурки приняли меня за мошенника, а я всего то выиграл их в кости."
        patrick "Меня зовут Патрик. Будем знакомы. Если буду нужен, ищи меня в таверне \"Три кабана\""
        jump tavern

    else:
        a "Герой, взяв волю в кулак, бровается в бой"
        "Громила 1" "Ты кто такой? Уходи по хорошему."
        a "Герой пытается ударить ближнего обидчика кулаком. Бесполезно..."
        a "Громила одним прямым ударом в лицо отправляет героя в нокаут."
        a "Очнувшись, герой не увидел ни молодого человека, ни громил." 
        a "Герой отряхивается и заходит в таверну."
        jump tavern

image bg home night = im.Scale("bg home night.jpg", 1920, 1080)

label homecoming:

    play music "audio/nightmare_song.mp3"

    a "Идя домой герой думал лишь о том что его ждет в будущем." 
    a "Он остался совсем один терзаемый страхом неизведанного и не пониманием того что ему нужно делать. Лишь слова друга семьи Бандикута вселяли в него хоть какую то надежду и какой либо смысл жить дальше."
    scene bg home night
    a "Придя в свой дом, пропитанный холодом и одиночеством, сев на кровать он заметил портрет своих родителей."
    a "Но во тьме ,их лица, будто были смазаны, а с другой же стороны, казалось что их взгляд направлен на героя и он полон презрения. Это ужаснуло героя, но присмотревшись - он понял, что протрет свовсем обычный и ничего в нем нет."
    a "Лежа в постели герой пытался уснуть, но сон все не приходил. Да и ужасы пережитые пару дней назад давали о себе знать. Пролежав несколько часов герой все же с трудом но провалился в сон."
    scene bg fog
    a "Герой очнулся, но вокруг себя он увидел лишь туман. С разных сторон разнолись крики радости, плач, мольбы о пощаде и все в таком духе. Это было странно и жутко одновременно."
    a "Стоять на месте было нельзя ибо все время казалось будто кто то за нами наблюдает."
    a "Герой побрел сквозь туман, искать выход из этого места."
    a "Сколько бы герой не шел все это было беспалезно, выхода все так же не было видно. Да и казалось что он все время ходит по кругу."
    a "А атмосфера все нагнеталась да и крики стали какими то непонятными. Однако через буквально несколько мгновений героя оклинули по имени и позвал его до боли знакомы голос."
    a "Обернувшись он увидел два силуэта..."
    show mother at right    
    show father at left
    a "Мужчина среднего роста, средней мускалоторы но с небольшим животом присущий всем купцам и женщина ростом чуть ниже мужчины с длиными серыми волосами."
    a "Это были его родители и выглядели они точно так же какими он видел их перед их смертью."
    a "Он побежал что есть сил к ним, горькие слезы текли по глазам и он не мог вымолвить и слова. Чем ближе он к ним подходил тем меньше тумана было вокруг и через пару секунд он увидел их."
    a "Однако, лица родителей не выражали радость а наоборот они были полны злости их взгляд был пропитан гневом который пронизал до глубины души."
    a "Герой был ошарашен и даже вздохнуть не мог толи от страха толи от того что чувство вины не дает трезво мыслить."
    a "Наступила гробовая тишина."
    a "Первыми ее нарушили родители. Полные злобы и желчи они начали словами острыми как ножи резать души героя."
    a "Он лишь слышал унижения и то какой он бесполезный что даже не смог помочь родителям в столь критический момент и именно из за него они погибли."
    a "Герой не верил что это происходит в реальности и умолял всех богов чтоб он наконец проснулся от этого ужасного сна. И его молитвы были услышаны."
    a "Проснувшись в холодном поту герой осмотрелся, эта была все таже комната холодная и пустая."
    a "Этот сон стал каким то провиденьем для героя он понял что пока он не отомстит души его родителей не упокоятся и будут терзать его по ночам."
    a "Именно в эту ночь в нашем герое что то сломалось, барьер каких то устоев был сломлен."

    return

define sylvana = Character("Сильвана")
image sylvana = im.Scale("sylvana.png", 400, 700)

label hunters_house:
    
    a "Герой очнулся в незнакомом доме. На стенах висит множество охотничьих трофеев: оленьи рога, медвежьи шкуры."
    a "В углу комнаты прислонен длинный лук."
    sylvana "Наконец-то ты очнулся. Тебе очень повезло, что они не заметили, что ты жив."
    sylvana "Я перевязала твою рану."
    e "Ужасно болит голова. Где я?"
    sylvana "Меня зовут Сильвана. Я охотница и это мой дом."
    hide anthony_1
    show anthony_1 at left with fade
    show sylvana at right with fade
    a "Герой внимательно начал изучать собеседника. Перед ним стояла эльфийка в расцвете своей красоты."
    a "Ее изумрудные волосы сверкали в лучах солнца."
    sylvana "Чего ты пялишься, извращенец? После такого удара тебе вообще все мозги выбило?"
    sylvana "Ты думаешь, хоть иногда, прежде чем принимать какие-то решения?"
    a "Герой, посмотрев ей прямо в глаза, ответил"
    e "У меня не было выбора, это была ситуация жизни и смерти. Мои близкие были под угрозой. Я не мог стоять сложа руки"
    a "Эльфийка была в крайнем недоумении от этих слов"
    sylvana "Надо было думать сначала о себе, а затем о других."
    e "Возможно, но тогда я об этом не думал"
    a "Герой пытается встать с кровати, но от резкого головокружения обратно падает в постель"
    sylvana "Лучше отлежись и потом поговорим."
    a "Наступает вечер..."

    a "Проснувшись, герой увидел охотницу недалеко от своей кровати. Она приводила свое снаряжение в порядок."
    e "Привет."
    a "Сильвана, вздрогнув, резко обернулась."
    sylvana "Ты меня напугал. Я была уверена, что ты спишь."
    e "Ну как видишь..."
    sylvana "Знаешь, я много думала о том, что ты сделал. Я удивлена твоему мужеству и храбростью."
    sylvana "Однако твои навыки оставляют желать лучшего. Мечем махать я тебя не научу, но стрельбой из лука смогу."
    e "Я не знаю, что ответить. Слишком много мыслей в голове. Дай мне немного прийти в себя и я дам тебе знать."
    sylvana "Торопить я тебя не буду. И что ты будешь делать дальше?"
    e "Хочу пройтись до дома, и потом загляну в таверну."
    sylvana "Ну тогда я тебя не буду задерживать."

    jump home

define priest = Character("Священник")

label church:

    return