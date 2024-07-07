define config.rollback_enabled = False
define config.has_autosave = False
image footer = "footer.png"

init python:

    renpy.music.register_channel("mp3",mixer="voice",loop=True)

    # Configuration
    timer_range = 0
    cs = 1
    config.keymap['accessibility'].remove("K_a")
    config.keymap['screenshot'].remove('s')
    quick_menu = False

    # BGM settings
    bgmname = ""
    bgmstartpoint = 0.0
    bgmvolume = 0.4

    # Unrated / quicklist
    unratedlist = [

    ]
    #quicklist = [

    #]

    # Game settings
    timelimit = 10
    reveallimit = 4.5
    timerskip = 0.04

    # Category names / values
        # To disable a category: insert a value >= 100 AND set text to NULL (cannot be empty.)
        # Adjust category font size by changing the default +0 (e.g. +12, -6) --- your text goes inside the quotes of text_transform("")

    # cat1 - easy1.jpg
    cat1_lowerbound = 100
    cat1_name = "{size=+0} EASY {/size}"
    cat1_color = "#87ff87"

    # cat2 - easy2.jpg
    cat2_lowerbound = 70
    cat2_name = "{size=+0} EASY {/size}"
    cat2_color = "#38fd70"

    # cat3 - medium1.jpg
    cat3_lowerbound = 50
    cat3_name = "{size=+0} MEDIUM {/size}"
    cat3_color = "#40E0D0"

    # cat4 - medium2.jpg
    cat4_lowerbound = 35
    cat4_name = "{size=-12} ADVANCED {/size}"
    cat4_color = "#6198fc"

    # cat5 - hard1.jpg
    cat5_lowerbound = 20
    cat5_name = "{size=+0} OTAKU {/size}"
    cat5_color = "#ffc494"

    # cat6 - hard2.jpg
    cat6_lowerbound = 0
    cat6_name = "{size=+0} LUNATIC {/size}"
    cat6_color = "#ffa65e"

    # cat7 - expert1.jpg
    cat7_lowerbound = 100
    cat7_name = "{size=+0} {/size}"
    cat7_color = "#fc62f2"

    # cat8 - expert2.jpg
    cat8_lowerbound = 100
    cat8_name = "{size=+0} {/size}"
    cat8_color = "#9208c4"

    # cat9 - impossible.jpg
    cat9_lowerbound = 100
    cat9_name = "{size=-21} {/size}"
    cat9_color = "#C0C0C0"

    songlist = [ 
        # 0 Anime name
        # 1 Anime sub-title
        # 2 Sample length
        # 3 Song name
        # 4 Artist name
        # 5 Opening number
        # 6 Release - Season (Format)
        # 7 Studio
        # 8 Genres
        # 9 MAL Score
        # 10 Sample start time (Video)
        # 11 Sample start time (Audio)
        # 11 Volume
        # 12 Filename (Video)
        # 13 Filename (Audio)

        #  ・  •
        
    ]
   
    listsize = len(songlist)

label start:

    $ _preferences.set_volume('music', 0)

    play mp3 "<from " + str(bgmstartpoint) + ">audio/00bgm.mp3" fadein 2.0 volume bgmvolume
    $ renpy.notify("♪ " + bgmname)

    scene infoscreen1 with Dissolve(1.5)
    $ renpy.pause(4)

    scene infoscreen2 with Dissolve(0.4)
    $ renpy.pause(3)

    scene infoscreen3 with Dissolve(0.4)
    $ renpy.pause(1.5)

    scene infoscreen4 with Dissolve(0.4)
    $ renpy.pause(2.5)

    stop mp3 fadeout 1.0
    call roundinit()
    
    play mp3 "<from " + str(bgmstartpoint) + ">audio/00bgm.mp3" fadein 2.0 fadeout 1.0 volume bgmvolume

    scene endscreen with fade
    $ renpy.pause(15)

    stop mp3 fadeout 1.0
    scene black with fade
    
    return

label roundinit():

    scene black with fade

    while cs <= listsize:
        python:
            mainans = songlist[cs-1][0].upper()
            subans = songlist[cs-1][1]
            variable = songlist[cs-1][2]
            songname = songlist[cs-1][3]
            artistname = songlist[cs-1][4]
            songtype = songlist[cs-1][5]
            release = songlist[cs-1][6]
            studio = songlist[cs-1][7]
            genres = songlist[cs-1][8]
            rating = songlist[cs-1][9]
            video_sample = songlist[cs-1][10]
            audio_sample = songlist[cs-1][12]
            loudness = songlist[cs-1][11]
            video_filename = songlist[cs-1][13]
            audio_filename = songlist[cs-1][14]


            if variable >= cat2_lowerbound:
                category = cat2_name
                # category_subtext = ""
                gamebg = "images/bg easy2.jpg"
                categorycolor = cat2_color
                bordertype = "e2"
            elif variable >= cat3_lowerbound:
                category = cat3_name
                # category_subtext = ""
                gamebg = "images/bg medium1.jpg"
                categorycolor = cat3_color
                bordertype = "m1"
            elif variable >= cat4_lowerbound:
                category = cat4_name
                # category_subtext = ""
                gamebg = "images/bg medium2.jpg"
                categorycolor = cat4_color
                bordertype = "m2"
            elif variable >= cat5_lowerbound:
                category = cat5_name
                # category_subtext = ""
                gamebg = "images/bg hard1.jpg"
                categorycolor = cat5_color
                bordertype = "h1"
            elif variable >= cat6_lowerbound:
                category = cat6_name
                # category_subtext = ""
                gamebg = "images/bg hard2.jpg"
                categorycolor = cat6_color
                bordertype = "h2"

            sizeplus = 65 if len(mainans) <= 10 else 50 if len(mainans) <= 20 else 40 if len(mainans) <= 30 else 35 if len(mainans) <= 38 else 25 if len(mainans) <= 48 else 18 #if len(mainans) <= 60 else 8
            genretext_offset = int((len(genres) - 47) / 3) + 5 if len(genres) > 58 else int((len(genres) - 47) / 3) + 4 if len(genres) > 47 else 3

            currentvideo = "<from " + str(video_sample+timelimit+1) + " loop 0>audio/" + video_filename + ".webm"
            currentaudio = "<from " + str(audio_sample) + " loop 0>audio/" + audio_filename + ".mp3"

            tl = timelimit
            revealtime = reveallimit

        image gamebg = "[gamebg]"
        scene gamebg with Dissolve(0.3)

        stop mp3 fadeout 1.0
        show screen revealhider()
        show screen guessingphase() with Dissolve(0.3)

        play mp3 currentaudio volume (loudness) fadein 1.5
        call screen countdown() with dissolve

        show footer:
            xpos 1491 ypos 953
        show expression "images/divider.png":
            ypos 305 xysize(1920, 630)
        show expression "images/border_[bordertype].png":
            xpos 27 ypos 327 xysize (1030, 582)

        show expression Movie(size=(1280*0.8, 720*0.8), play=currentvideo, channel="movie") with dissolve:
            xpos 30 ypos 330 

        $ renpy.pause(0.1)

        hide screen guessingphase
        hide screen revealhider with dissolve

        show screen reveal() with Dissolve(0.2)
        show screen revealbar with Dissolve(0.2)

        $ renpy.pause(reveallimit)

        hide screen reveal with Dissolve(0.2)
        hide screen revealbar with Dissolve(0.2)
        $ cs += 1
    stop mp3 fadeout 1.0
    return


transform alpha_dissolve:
    alpha 0.0
    linear 0.4 alpha 1.0
    on hide:
        linear 0.4 alpha 0

screen revealhider():
    add "[gamebg]"

screen guessingphase():
    fixed:
        text "{color=[categorycolor]}{b}{size=+40}SONG {/size}{size=+120}[cs]{/size}{/b}   OF [listsize]{/color}":
            xpos 1100 ypos 130 outlines [ (6, "#00000044", 0, 0), (4, "#19191988", 0, 0),  (2, "#1f1f1fcc", 0, 0) ]
        text "{color=[categorycolor]}{b}{size=+75}[category]{/size}{/b}{/color}":
            xalign 0.03 ypos -50 vertical True
        text "{color=#fff}{size=+10}{b}SONG GUESS RATE{/b}{/size}{/color}":
            xpos 1382 ypos 850
        if mainans in unratedlist:
            text "{color=[categorycolor]}{b}{size=+70}Unrated{/size}{b}{/color}":
                xpos 1362 ypos 900 text_align 1
        elif variable >= 10:
            text "{color=[categorycolor]}{b}{size=+80}[variable]%{/size}{b}{/color}":
                xpos 1432 ypos 900 text_align 1
        else:
            text "{color=[categorycolor]}{b}{size=+80}[variable]%{/size}{b}{/color}":
                xpos 1515 ypos 900 text_align 1

screen countdown():
    fixed:
        text "{color=#fff}{b}Time left:{/b}{/color}":
            xpos 1105 ypos 300 size 40 outlines [ (3, "#00000044", 0, 0), (2, "#19191988", 0, 0),  (1, "#1f1f1fcc", 0, 0) ]
    timer 1 repeat True action If(tl > 0, true=SetVariable('tl', tl - 1), false=[Return()])
    if tl <= 2:
        text str(tl) xpos 1340 ypos 290 color "#ff4444" size 340 font "Uni Sans Heavy.otf" outlines [ (10, "#00000044", 0, 0), (5, "#19191988", 0, 0),  (3, "#1f1f1fcc", 0, 0) ] at alpha_dissolve 
    elif tl <= 5:
        text str(tl) xpos 1340 ypos 290 color "#ffc354" size 340 font "Uni Sans Heavy.otf" outlines [ (10, "#00000044", 0, 0), (5, "#19191988", 0, 0),  (3, "#1f1f1fcc", 0, 0) ] at alpha_dissolve 
    else:
        text str(tl) xpos 1340 ypos 290 color "#69ff7a" size 340 font "Uni Sans Heavy.otf" outlines [ (10, "#00000044", 0, 0), (5, "#19191988", 0, 0),  (3, "#1f1f1fcc", 0, 0) ] at alpha_dissolve

screen reveal():
    fixed:
        text "{color=#ffdd75}{b}{size=+[sizeplus]}[mainans]{/size}{/b}{/color}\n{color=#ffdd75}{i}{size=+8}[subans]{/size}{/i}{/color}":
            xalign 0.5 ypos 105 text_align 0.5 outlines [ (4, "#00000044", 0, 0), (3, "#19191988", 0, 0),  (2, "#1f1f1fcc", 0, 0) ]
        text "{color=#fff}{b}{u}{size=+7}[songtype]{/size}{/u}{/b}{/color}":
            xpos 1080 ypos 340 
        text "{color=#fff}{size=+15}[songname]{/size}{/color}\n{color=#d9f5ff}{size=-7}{i}by  {/i}{/color}{color=#fff}[artistname]{/color}{/size}":
            xpos 1080 ypos 390 xmaximum 800

        add "images/div1.png" xpos 1080 ypos 590 xzoom 0.2 yzoom 0.2
        add "images/div2.png" xpos 1080 ypos 670 xzoom 0.2 yzoom 0.2
        add "images/div3.png" xpos 1080 ypos 750 xzoom 0.2 yzoom 0.2
        add "images/div4.png" xpos 1080 ypos 830 xzoom 0.2 yzoom 0.2

        text "{color=#AFDC7E}{size=-9}{b}STUDIO{/b}{/size}{/color}":
            xpos 1103 ypos 590
        text "{color=#53D2FF}{size=-9}{b}RELEASE{/b}{/size}{/color}":
            xpos 1103 ypos 670
        text "{color=#FF9B9B}{size=-9}{b}GENRES{/b}{/size}{/color}":
            xpos 1103 ypos 750
        text "{color=#DFDDDD}{size=-9}{b}MAL SCORE{/b}{/size}{/color}":
            xpos 1103 ypos 830

        text "{color=#fff}{size=-3}[studio]{/size}{/color}":
            xpos 1103 ypos 617
        text "{color=#fff}{size=-3}[release]{/size}{/color}":
            xpos 1103 ypos 697
        text "{color=#fff}{size=-[genretext_offset]}[genres]{/size}{/color}":
            xpos 1103 ypos 777
        text "{color=#fff}{size=-3}[rating]{/size}{/color}":
            xpos 1103 ypos 857
    
screen revealbar():
    fixed:
        text "{color=[categorycolor]}{b}SONG [cs] - ANSWER{/b}{/color}":
            xalign 0.5 ypos 37
        timer timerskip repeat True action If(revealtime >= 0.0, true=SetVariable('revealtime', revealtime - timerskip), false=[NullAction()])
        bar value revealtime range reveallimit xalign 0.5 ypos 80 xmaximum 1350 at alpha_dissolve 
