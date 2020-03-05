# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Хиро")
define a = Character("Рассказчик")

# The game starts here.
image bg starting room = im.Scale("bg starting room.jpg", 1600, 900)
image bg forest trail = im.Scale("bg forest.jpg", 1600, 900)

label start:
    play music "audio/forest_song.mp3"

    scene bg black screen

    a "Караван нашего героя "
    a "Юный герой путешествует с родителями в повозке по дороге в родную деревню Ривервуд."
    a "Сквозь сон он слышит звуки боя."

    play sound "audio/female_scream.mp3"
    "Женский голос" "АААААА!"

    scene bg forest trail
    show anthony_1 with fade

    a "Герой быстро выпрыгивает из повозки и видит разбойников. Среди толпы "
    a "Времени на раздумья нет."

    menu:
           "Попробовать убежать":
                a "Герой бежит изо всех сил в сторону деревни. После многочасового бега герой достигает деревни, но от ужасной усталости, теряет сознание"
                jump home
           "Попробовать напасть на разбойников":
                a "Герой пытается найти что-нибудь, что может сойти за оружие. Его глаз падает на палку, лежащую в углу повозке."
                a "Пытаясь дотянуться, он чувствует резкую боль в голове"
                jump hunters_house

image bg town center = im.Scale("images/bg town center.jpg", 1600, 900)
define elder = Character("Элайджа")

label home:

    scene bg starting  room

    a "Проснувшись, герой оглядывается..."
    a "В углу комнаты герой замечает старика. Он узнает старейшину деревни."
    elder "Проснулся? Тебя нашел стражник, патрулировавший улицу. Расскажи, что произошло."
    e "На нас напали разбойники."
    elder "Первое - твоих родителей не удалось спасти. Второе - все имущество, что у тебя осталось, это этот дом."

image bg tavern = im.Scale("images/bg tavern.jpg", 1600, 900)

label tavern:

    scene bg tavern

    show anthony_1 with fade

    "You see a group of men drinking. The barman is wiping a mug"

    menu:
        "Return"

        "Return":
            return

label noticeboard:

    scene bg notice board

    "You see some notices on the board"

    menu:
            "Return"

            "Return":
                return