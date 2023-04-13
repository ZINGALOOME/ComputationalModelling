import numpy as np
import time
import string
# print("Importing NLTK module and downloading punkt, stopwords: ")
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import gensim
from gensim import corpora
import csv

pre_processed_lyrics = ['   Doh Doh doh doh doh doh doh Doh doh Doh doh doh doh doh doh Doh doh Doh doh doh doh doh doh Doh doh Doh doh doh aaaaaow This hit that ice cold Michelle Pfeiffer that white gold This one for them hood girls Them good girls straight masterpieces Stylin wildin Livin it up in the city Got Chucks on with Saint Laurent Gotta kiss myself Im so pretty Im too hot hot damn Called a police and a fireman Im too hot hot damn Make a dragon wanna retire man Im too hot hot damn Say my name you know who I am Im too hot hot damn Am I bad bout that money Break it down Girls hit your hallelujah wooh Girls hit your hallelujah wooh Girls hit your hallelujah wooh Cause Uptown Funk gon give it to you wooh Cause Uptown Funk gon give it to you Cause Uptown Funk gon give it to you Saturday night and we in the spot Dont believe me just watch come on Dont believe me just watch Dont believe me just watch Dont believe me just watch Dont believe me just watch Dont believe me just watch Hey hey hey oh  Stop Wait a minute Fill my cup put some liquor in it Take a sip sign a check Julio get the stretch Ride to Harlem Hollywood Jackson Mississippi If we show up we gon show out Smoother than a fresh jar of Skippy Im too hot hot damn Called a police and a fireman Im too hot  hot damn Make a dragon wanna retire man Im too hot hot damn hot damn Bitch say my name you know who I am Im too hot hot damn Am I bad bout that money Break it down Girls hit your hallelujah wooh Girls hit your hallelujah wooh Girls hit your hallelujah wooh Cause Uptown  Funk gon give it to you wooh Cause Uptown Funk gon give it to you Cause Uptown Funk gon give it to you Saturday night and we in the spot Dont believe me just watch come on Dont believe me just watch Dont believe me just watch Dont believe me just watch Dont believe me just watch Dont believe me just watch Hey hey hey oh Before we leave Imma tell yall a lil something Uptown Funk you up Uptown Funk you up Uptown Funk you up Uptown Funk you up I said Uptown Funk you up Uptown Funk you up Uptown Funk you up Uptown Funk you up Come on dance jump on it If you sexy than flaunt it If you freaky then own it Dont brag about it come show me Come on dance jump on it If you sexy than flaunt it Well its Saturday night and we in the spot Dont believe me just watch come on Dont believe me just watch Dont believe me just watch Dont believe me just watch Dont believe me just watch Dont believe me just watch Hey hey hey oh Uptown Funk you up Uptown Funk you up say what Uptown Funk you up Uptown Funk you up Uptown Funk you up Uptown Funk you up say what Uptown Funk you up Uptown Funk you up Uptown Funk you up Uptown Funk you up say what Uptown Funk you up Uptown Funk you up Uptown  Funk you up Uptown Funk you up say what Uptown Funk you up ' ,
'  The club isnt the best place to find a lover So the bar is where I go Me and my friends at the table doing shots Drinking fast and then we talk slow And you come over and start up a conversation with just me And trust me Ill give it a chance now Take my hand stop put Van the Man on the jukebox And then we start to dance and now Im singing like Girl you know I want your love Your love was handmade for somebody like me Come on now follow my lead I may be crazy dont mind me Say boy lets not talk too much Grab on my waist and put that body on me Come on now follow my lead Come come on now follow my lead Im in love with the shape of you We push and pull like a magnet do Although my heart is falling too Im in love with your body And last night you were in my room And now my bedsheets smell like you Every day discovering something brand new Im in love with your body OhIohIohIohI Im in love with your body OhIohIohIohI Im in love with your body OhIohIohIohI Im in love with your body Every day discovering something brand new Im in love with the shape of you One week in we let the story begin Were going out on our first date You and me are thrifty so go all you can eat Fill up your bag and I fill up a plate We talk for hours and hours about the sweet and the sour And how your family is doing okay Leave and get in a taxi then kiss in the backseat Tell the driver make the radio play and Im singing like Girl you know I want your love Your love was handmade for somebody like me Come on now follow my lead I may be crazy dont mind me Say boy lets not talk too much Grab on my waist and put that body on me Come on now follow my lead Come come on now follow my lead Im in love with the shape of you We push and pull like a magnet do Although my heart is falling too Im in love with your body And last night you were in my room And now my bedsheets smell like you Every day discovering something brand new Im in love with your body OhIohIohIohI Im in love with your body OhIohIohIohI Im in love with your body OhIohIohIohI Im in love with your body Every day discovering something brand new Im in love with the shape of you Come on be my baby come on Come on be my baby come on Come on be my baby come on Come on be my baby come on Come on be my baby come on Come on be my baby come on Come on be my baby come on Come on be my baby come on Im in love with the shape of you We push and pull like a magnet do Although my heart is falling too Im in love with your body Last night you were in my room And now my bedsheets smell like you Every day discovering something brand new Im in love with your body Come on be my baby come on Come on be my baby come on Im in love with your body Come on be my baby come on Come on be my baby come on Im in love with your body Come on be my baby come on Come on be my baby come on Im in love with your body Every day discovering something brand new Im in love with the shape of you ' ,
'  Theres a fire starting in my heart Reaching a fever pitch its bringing me out the dark Finally I can see you crystal clear Go ahead and sell me out and Ill lay your ship bare See how Ill leave with every piece of you Dont underestimate the things that I will do Theres a fire starting in my heart Reaching a fever pitch and its bringing me out the dark The scars of your love remind me of us They keep me thinking that we almost had it all The scars of your love they leave me breathless I cant help feeling We couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me And you played it tears are gonna fall To the beat rolling in the deep Baby I have no story to be told But Ive heard one on you now Im gonna make your head burn Think of me in the depths of your despair Make a home down there as mine sure wont be shared The scars of your love never had met me Remind me of us tears are gonna fall They keep me thinking rolling in the deep That we almost had it all youre gonna wish you The scars of your love never had met me They leave me breathless tears are gonna fall I cant help feeling rolling in the deep We couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me And you played it tears are gonna fall To the beat rolling in the deep We couldve had it all Rolling in the deep You had my heart inside of your hand But you played it with a beating Throw your soul through every open door whoa Count your blessings to find what you look for whoa Turn my sorrow into treasured gold whoa You pay me back in kind and reap just what youve sown We couldve had it all tears are gonna fall rolling in the deep We couldve had it all youre gonna wish you never had met me It all it all it all tears are gonna fall rolling in the deep We couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me And you played it tears are gonna fall To the beat rolling in the deep Couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me But you played it you played it you played it You played it to the beat ' ,
' It might seem crazy what I am bout to say Sunshine shes here you can take a break Im a hot air balloon that could go to space With the air like I dont care baby by the way Huh Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do Here come bad news talking this and that Yeah Well give me all you got dont hold back Yeah Well I should probably warn you Ill be just fine Yeah No offense to you dont waste your time Heres why Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do Uh bring me down Cant nothing bring me down My levels too high to bring me down Cant nothing bring me down I said Bring me down cant nothing Bring me down My levels too high to bring me down Cant nothing bring me down I said Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do Uh bring me down Happy happy happy happy Cant nothing Happy happy happy happy Bring me down my levels too high To bring me down Happy happy happy happy Cant nothing Happy happy happy happy Bring me down I said Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you ayy ayy ayy Because Im happy Clap along if you feel like thats what you wanna do Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you hey Because Im happy Clap along if you feel like thats what you wanna do  ' ,
' Now and then I think of when we were together Like when you said you felt so happy you could die Told myself that you were right for me But felt so lonely in your company But that was love and its an ache I still remember You can get addicted to a certain kind of sadness Like resignation to the end always the end So when we found that we could not make sense Well you said that we would still be friends But Ill admit that I was glad it was over But you didnt have to cut me off Make out like it never happened and that we were nothing And I dont even need your love But you treat me like a stranger and that feels so rough No you didnt have to stoop so low Have your friends collect your records and then change your number I guess that I dont need that though Now youre just somebody that I used to know Now youre just somebody that I used to know Now youre just somebody that I used to know Now and then I think of all the times you screwed me over But had me believing it was always something that Id done And I dont wanna live that way Reading into every word you say You said that you could let it go And I wouldnt catch you hung up on somebody that you used to know But you didnt have to cut me off Make out like it never happened and that we were nothing aahooh And I dont even need your love ooh But you treat me like a stranger and that feels so rough aah No you didnt have to stoop so low ooh Have your friends collect your records and then change your number aah I guess that I dont need that though Now youre just somebody that I used to know Somebody I used to know Somebody now youre just somebody that I used to know Somebody I used to know Somebody now youre just somebody that I used to know I used to know That I used to know I used to know Somebody  ' ,
' Everybody get up Everybody get up hey hey hey Hey hey hey uh Hey hey hey haha woo Turn me up If you cant hear what Im trying to say hey girl come here If you cant read from the same page hey Maybe Im going deaf hey hey hey Maybe Im going blind hey hey hey Maybe Im out of my mind mind hey hey hey Okay now he was close Tried to domesticate you But youre an animal Baby its in your nature meow Just let me liberate you hey hey hey You dont need no takers hey hey hey That man is not your maker hey hey hey And thats why Im gon take a good girl everybody get up I know you want it hey I know you want it I know you want it Youre a good girl hey hey Cant let it get past me oh yeah Youre far from plastic alright Talkin bout getting blasted I hate these blurred lines I know you want it hey I know you want it ohohohoh yeahyeah I know you want it But youre a good girl ah hey The way you grab me Must wanna get nasty ah hey hey Go ahead get at me everybody get up come on What do they make dreams for When you got them jeans on Why What do we need steam for You the hottest bitch in this place I feel so lucky hey hey hey You wanna hug me hey hey hey What rhymes with hug me Hey hey hey Hey everybody get up Okay now he was close Tried to domesticate you But youre an animal Baby its in your nature uhhuh Just let me liberate you hey hey hey uhhuh You dont need no takers hey hey hey uhhuh That man is not your maker hey hey hey uhhuh And thats why Im gon take a good girl everybody get up I know you want it I know you want it hey I know you want it Youre a good girl Cant let it get past me hey Youre far from plastic oh Talkin bout getting blasted everybody get up I hate these blurred lines hate them lines I know you want it I hate them lines I know you want it I hate them lines I know you want it But youre a good girl good girl The way you grab me hustle gang homie Must wanna get nasty let go I say Rob Go ahead get at me let me holla at em real quick One thing I ask of you Let me be the one you back that ass up to come on Go from Malibu to Paris boo yeah Had a bitch but she aint bad as you uhuh ayy So hit me up when you pass through oh Ill give you something big enough to tear your ass in two Swag on em even when you dress casual I mean its almost unbearable hey hey hey everybody get up In a hundred years not dare would I Pull a Pharcyde let you pass me by Nothin like your last guy he too square for you He dont smack that ass and pull your hair like that you like it So Im just watchin and waitin For you to salute the true big pimpin Not many women can refuse this pimpin Im a nice guy but dont get it confused get pimpin everybody get up Shake your rump Get down get up Do it like it hurt like it hurt What you dont like work Hey everybody get up Baby can you breathe I got this from Jamaica It always works for me Dakota to Decatur uhhuh No more pretending hey hey hey uhhuh Cause now youre winning hey hey hey uhhuh Heres our beginning hey hey hey uhhuh I always wanted Youre a good girl everybody get up I know you want it hey I know you want it I know you want it Youre a good girl Cant let it get past me oh yeah Youre far from plastic alright Talkin bout getting blasted I hate these blurred lines everybody get up I know you want it hey I know you want it ohohohoh yeahyeah I know you want it But youre a good girl ah hey The way you grab me Must wanna get nasty ah hey hey Go ahead get at me Everybody get up Everybody get up Hey hey hey Hey hey hey Hey hey hey ' ,      
' I threw a wish in the well Dont ask me Ill never tell I looked to you as it fell And now youre in my way I trade my soul for a wish Pennies and dimes for a kiss I wasnt looking for this But now youre in my way Your stare was holdin Ripped jeans skin was showin Hot night wind was blowin Where you think youre going baby Hey I just met you and this is crazy But heres my number so call me maybe Its hard to look right at you baby But heres my number so call me maybe Hey I just met you and this is crazy But heres my number so call me maybe And all the other boys try to chase me But heres my number so call me maybe You took your time with the call I took no time with the fall You gave me nothing at all But still youre in my way I beg and borrow and steal At first sight and its real I didnt know I would feel it But its in my way Your stare was holdin Ripped jeans skin was showin Hot night wind was blowin Where you think youre going baby Hey I just met you and this is crazy But heres my number so call me maybe Its hard to look right at you baby But heres my number so call me maybe Hey I just met you and this is crazy But heres my number so call me maybe And all the other boys try to chase me But heres my number so call me maybe Before you came into my life I missed you so bad I missed you so bad I missed you so so bad Before you came into my life I missed you so bad And you should know that I missed you so so bad Bad bad bad bad bad bad Its hard to look right at you baby But heres my number so call me maybe Hey I just met you and this is crazy But heres my number so call me maybe And all the other boys try to chase me But heres my number so call me maybe Before you came into my life I missed you so bad I missed you so bad I missed you so so bad Before you came into my life I missed you so bad And you should know that So call me maybe ' ,
' Hello its me I was wondering if after all these years youd like to meet To go over everything They say that times supposed to heal ya but I aint done much healing Hello can you hear me Im in California dreaming about who we used to be When we were younger and free Ive forgotten how it felt before the world fell at our feet Theres such a difference between us And a million miles Hello from the other side I mustve called a thousand times To tell you Im sorry for everything that Ive done But when I call you never seem to be home Hello from the outside At least I can say that Ive tried To tell you Im sorry for breaking your heart But it dont matter it clearly doesnt tear you apart anymore Hello how are you Its so typical of me to talk about myself Im sorry I hope that youre well Did you ever make it out of that town where nothing ever happened Its no secret that the both of us Are running out of time So hello from the other side other side I mustve called a thousand times thousand times To tell you Im sorry for everything that Ive done But when I call you never seem to be home Hello from the outside outside At least I can say that Ive tried Ive tried To tell you Im sorry for breaking your heart But it dont matter it clearly doesnt tear you apart anymore Ooh lows lows lows lows anymore Highs highs highs highs Ooh lows lows lows lows anymore Highs highs highs highs Ooh lows lows lows lows anymore Highs highs highs highs Anymore lows lows lows lows Hello from the other side other side I mustve called a thousand times thousand times To tell you Im sorry for everything that Ive done But when I call you never seem to be home Hello from the outside outside At least I can say that Ive tried Ive tried To tell you Im sorry for breaking your heart But it dont matter it clearly doesnt tear you apart anymore ' ,
' Yeah Im gonna take my horse to the old town road Im gonna ride til I cant no more Im gonna take my horse to the old town road Im gonna ride Kio Kio til I cant no more I got the horses in the back Horse tack is attached Hat is matte black Got the boots thats black to match Riding on a horse ha You can whip your Porsche I been in the valley You aint been up off the porch now Cant nobody tell me nothing You cant tell me nothing Cant nobody tell me nothing You cant tell me nothing Riding on a tractor Lean all in my bladder Cheated on my baby You can go and ask her My life is a movie Bull riding and boobies Cowboy hat from Gucci Wrangler on my booty Cant nobody tell me nothing You cant tell me nothing Cant nobody tell me nothing You cant tell me nothing Yeah Im gonna take my horse to the old town road Im gonna ride til I cant no more Im gonna take my horse to the old town road Im gonna ride til I cant no more Hat down crosstown livin like a rockstar Spent a lot of money on my brandnew guitar Babys got a habit diamond rings and Fendi sports bras Ridin down Rodeo in my Maserati sports car Got no stress Ive been through all that Im like a Marlboro Man so I kick on back Wish I could roll on back to that old town road I wanna ride til I cant no more Yeah Im gonna take my horse to the old town road Im gonna ride til I cant no more Im gonna take my horse to the old town road Im gonna ride til I cant no more ' ,
' One two three uh My baby dont mess around Because she loves me so And this I know fo sho uh But does she really wanna But cant stand to see me walk out the door Ah Dont try to fight the feeling Because the thought alone is killin me right now uh Thank God for Mom and Dad For sticking two together Cause we dont know how cmon Hey ya Hey ya Hey ya Hey ya Hey ya Hey ya Hey ya Hey ya You think youve got it Oh you think youve got it But got it just dont get it til theres nothin at all We get together Oh we get together But separates always better when theres feelings involved If what they say is Nothing is forever Then what makes then what makes Then what makes then what makes what makes what makes Love the exception So why oh why oh Why oh why oh why oh Are we so in denial when we know were not happy here Yall dont want to hear me you just want to dance Hey ya Uh oh Hey ya Uh oh Dont want to meet your daddy Hey ya Uh oh Just want you in my Caddy Uh oh Hey ya Uh oh Dont want to meet your mama Hey ya Uh oh Just want to make you cuma Uh oh Hey ya Uh oh Im Im Im just being honest Uh oh Im just being honest Hey Alright now Alright now fellas Yeah Now what cooler than being cool Ice cold I cant hear you I say whats whats cooler than being cool Ice cold Alright alright alright alright alright Alright alright alright alright alright Alright alright alright alright Okay now ladies Yeah Now we gon break this thang down in just a few seconds Now dont have me break this thang down for nothin Now I want to see yall on yall baddest behavior Lend me some sugar I am your neighbor Ah Here we go Shake it shake shake it shake it shake shake it Uh oh Shake it shake shake it shake it shake it Uh oh Shake it like a Polaroid picture hey ya Shake it shake shake it shake it shake shake it Shake it shake it shake it sugar Shake it like a Polaroid picture Now all Beyonces and Lucy Lius And baby dolls Get on the floor Get on the floor you know what to do You know what to do You know what to do Hey ya Uh oh Hey ya Uh oh Hey ya Uh oh Hey ya Uh oh Hey ya Uh oh Hey ya Uh oh Hey ya Uh oh Hey ya Uh oh ' ,
' I got a feeling That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night A feeling That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night A feeling woohoo That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night A feeling woohoo That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night Tonights the night lets live it up I got my money lets spend it up a fee Go out and smash it like Oh my God Jump out that sofa lets kick it off a fee I know that well have a ball If we get down and go out and just lose it all I feel stressed out I wanna let it go Lets go way out spaced out and losin all control Fill up my cup mazel tov Look at her dancin just take it off a fee Lets paint the town well shut it down Lets burn the roof and then well do it again Lets do it lets do it lets do it lets do it And do it and do it lets live it up And do it and do it and do it do it do it Lets do it lets do it lets do it Cause I gotta feeling woohoo That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night A feeling woohoo That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night a fee Tonights the night hey lets live it up lets live it up I got my money Im paid lets spend it up lets spend it up Go out and smash it smash it like Oh my God like Oh my God Jump out that sofa come on lets kick it off a fee Fill up my cup drink mazel tov lchaim Look at her dancing move it move it just take it off a fee Lets paint the town paint the town well shut it down shut it down Lets burn the roof oohwoo and then well do it again Lets do it lets do it lets do it lets do it lets do it And do it do it and do it lets live it up And do it do it and do it and do it And do it do it do it and do it Lets do it and do it lets do it and do it Lets do it hey do it hey do it hey do it Here we come here we go we gotta rock Easy come easy go now we on top Feel the shot body rock rock it dont stop Round and round up and down around the clock Monday Tuesday Wednesday and Thursday do it Friday Saturday Saturday to Sunday do it Get get get get get with us you know what we say say Party every day pppparty every day And Im feeling woohoo That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night A feeling woohoo That tonights gonna be a good night That tonights gonna be a good night That tonights gonna be a good good night ' ,
' Look If you had One shot Or one opportunity To seize everything you ever wanted In one moment Would you capture it Or just let it slip Yo His palms are sweaty knees weak arms are heavy Theres vomit on his sweater already moms spaghetti Hes nervous but on the surface he looks calm and ready To drop bombs but he keeps on forgettin What he wrote down the whole crowd goes so loud He opens his mouth but the words wont come out Hes chokin how everybodys jokin now The clocks run out times up over blaow Snap back to reality ope there goes gravity Ope there goes Rabbit he choked Hes so mad but he wont give up that easy No He wont have it he knows his whole backs to these ropes It dont matter hes dope he knows that but hes broke Hes so stagnant he knows when he goes back to this mobile home thats when its Back to the lab again yo this whole rhapsody Better go capture this moment and hope it dont pass him You better lose yourself in the music the moment You own it you better never let it go You only get one shot do not miss your chance to blow This opportunity comes once in a lifetime You better lose yourself in the music the moment You own it you better never let it go You only get one shot do not miss your chance to blow This opportunity comes once in a lifetime You better His souls escaping through this hole that is gaping This world is mine for the taking Make me king as we move toward a New World Order A normal life is borin but super stardoms close to post mortem It only grows harder only grows hotter He blows its all over these hoes is all on him Coast to coast shows hes known as the Globetrotter Lonely roads God only knows hes grown farther from home hes no father He goes home and barely knows his own daughter But hold your nose cause here goes the cold water These hoes dont want him no mo hes cold product They moved on to the next schmo who flows he nose dove and sold nada So the soap opera is told and unfolds I suppose its old partna but the beat goes on Dadadum dadum dada You better lose yourself in the music the moment You own it you better never let it go You only get one shot do not miss your chance to blow This opportunity comes once in a lifetime You better lose yourself in the music the moment You own it you better never let it go You only get one shot do not miss your chance to blow This opportunity comes once in a lifetime You better No more games Ima change what you call rage Tear this motherfuckin roof off like two dogs caged I was playin in the beginnin the mood all changed I been chewed up and spit out and booed off stage But I kept rhymin and stepped right in the next cypher Best believe somebodys payin the Pied Piper All the pain inside amplified by the Fact that I cant get by with my nine to Five and I cant provide the right type of Life for my family cause man these goddamn food stamps dont buy diapers And its no movie theres no Mekhi Phifer This is my life and these times are so hard And its getting even harder tryna feed and water my seed plus Teeter totter caught up between bein a father and a prima donna Baby mama drama screamin on her too much For me to wanna stay in one spot another day of monotonys Gotten me to the point Im like a snail Ive got To formulate a plot or end up in jail or shot Success is my only motherfuckin option failures not Mom I love you but this trailers got to go I cannot grow old in Salems Lot So here I go is my shot Feet fail me not this may be the only opportunity that I got You better lose yourself in the music the moment You own it you better never let it go You only get one shot do not miss your chance to blow This opportunity comes once in a lifetime You better lose yourself in the music the moment You own it you better never let it go You only get one shot do not miss your chance to blow This opportunity comes once in a lifetime You better You can do anything you set your mind to man ' ,
' Peace up ATown down Yeah yeah Okay okay Usher Usher Usher Usher Lil Jon Yeah yeah yeah yeah yeah yeah Yeah yeah yeah yeah yeah yeah What it do shawty Lets go Up in the club with my homies trying to get a lil VI Keep it down on the lowkey lowkey You should know how it feels hey I saw this shorty she was checking up on me From the game she was spitting in my ear You would think that she know me know me I decided to chill okay Conversation got heavy hey She had me feeling like shes ready to blow watch out Oh watch out Shes saying Come get me come get me So I got up and followed her to the floor She said Baby lets go When I told her lets go I said Yeah Shorty got down low and said Come and get me Yeah Yeah I got so caught up I forgot she told me Yeah Yeah Her and my girl used to be the best of homies Yeah Yeah Next thing I knew she was all up on me screaming Yeah yeah yeah yeah yeah yeah Yeah yeah yeah yeah yeah yeah So shes all up in my head now Got me thinking that it might be a good idea to take her with me Cause shes ready to leave ready to leave now Lets go And I gotta keep it real now Cause on a one to ten shes a certified twenty But that just aint me hey Cause I dont know if I take that chance Just wheres it gonna lead But what I do know is the way she dance Makes shorty alright with me hey hey hey The way she get low Im like Yeah just work that out for me She asks for one more dance and Im like Yeah How the hell am I supposed to leave Lets go bring the beat back And I say Yeah Shorty got down low and said Come and get me Yeah Yeah I got so caught up I forgot she told me Yeah Yeah Her and my girl used to be the best of homies Yeah Yeah Next thing I knew she was all up on me screaming Yeah yeah yeah yeah yeah yeah Yeah yeah yeah yeah yeah yeah hey hey Luda Watch out my outfits ridiculous In the club looking so conspicuous And rraww these women all on the prowl If you hold the head steady Ima milk the cow yeah And forget about game Ima spit the truth what I wont stop til I get em in they birthday suit yeah So gimme the rhythm and itll be off with their clothes Then bend over to the front and touch your toes I left the Jag and I took the Rolls If they aint cutting then I put em on foot patrol lets go How you like me now When my pinkys valued over three hundred thousand Lets drink you the one to please yeah Ludacris fill cups like double Ds yeah Me and Ursh once more and we leaves em dead hey We want a lady in the street but a freak in the bed that say Yeah Shorty got down low and said Come and get me Yeah Yeah I got so caught up I forgot she told me Yeah Yeah Her and my girl used to be the best of homies Yeah Yeah Next thing I knew she was all up on me screaming Yeah yeah yeah yeah yeah yeah Yeah yeah yeah yeah yeah yeah Take that and rewind it back Lil Jon got the beat that make your booty go Take that rewind it back Usher got the voice to make your booty go Take that rewind it back Ludacris got the flow to make your booty go Take that rewind it back Lil Jon got the beat that make your booty go ' ,
' Theres a fire starting in my heart Reaching a fever pitch its bringing me out the dark Finally I can see you crystal clear Go ahead and sell me out and Ill lay your ship bare See how Ill leave with every piece of you Dont underestimate the things that I will do Theres a fire starting in my heart Reaching a fever pitch and its bringing me out the dark The scars of your love remind me of us They keep me thinking that we almost had it all The scars of your love they leave me breathless I cant help feeling We couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me And you played it tears are gonna fall To the beat rolling in the deep Baby I have no story to be told But Ive heard one on you now Im gonna make your head burn Think of me in the depths of your despair Make a home down there as mine sure wont be shared The scars of your love never had met me Remind me of us tears are gonna fall They keep me thinking rolling in the deep That we almost had it all youre gonna wish you The scars of your love never had met me They leave me breathless tears are gonna fall I cant help feeling rolling in the deep We couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me And you played it tears are gonna fall To the beat rolling in the deep We couldve had it all Rolling in the deep You had my heart inside of your hand But you played it with a beating Throw your soul through every open door whoa Count your blessings to find what you look for whoa Turn my sorrow into treasured gold whoa You pay me back in kind and reap just what youve sown We couldve had it all tears are gonna fall rolling in the deep We couldve had it all youre gonna wish you never had met me It all it all it all tears are gonna fall rolling in the deep We couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me And you played it tears are gonna fall To the beat rolling in the deep Couldve had it all youre gonna wish you Never had met me Rolling in the deep tears are gonna fall Rolling in the deep You had my heart inside youre gonna wish you Of your hands never had met me But you played it you played it you played it You played it to the beat ' ,
' I remember when I remember I remember when I lost my mind There was something so pleasant about that place Even your emotions have an echo in so much space And when youre out there without care Yeah I was out of touch But it wasnt because I didnt know enough I just knew too much Does that make me crazy Does that make me crazy Does that make me crazy Possibly And I hope that you are having the time of your life But think twice thats my only advice Come on now who do you who do you who do you Who do you think you are Ha ha ha bless your soul You really think youre in control I think youre crazy I think youre crazy I think youre crazy Just like me My heroes had the heart to lose their lives out on the limb And all I remember is thinking I want to be like them Ever since I was little Ever since I was little it looked like fun And its no coincidence Ive come And I can die when Im done But maybe Im crazy Maybe youre crazy Maybe were crazy Probably ' ,
' All the single ladies all the single ladies All the single ladies all the single ladies All the single ladies all the single ladies All the single ladies Now put your hands up Up in the club we just broke up Im doing my own little thing Decided to dip and now you wanna trip Cause another brother noticed me Im up on him he up on me Dont pay him any attention Just cried my tears for three good years Ya cant be mad at me Cause if you liked it then you should have put a ring on it If you liked it then you shoulda put a ring on it Dont be mad once you see that he want it If you liked it then you shoulda put a ring on it Oh oh oh oh oh oh oh oohh Oh oh oh oh oh oh oh oohh If you liked it then you should have put a ring on it If you liked it then you shoulda put a ring on it Dont be mad once you see that he want it If you liked it then you shoulda put a ring on it I got gloss on my lips a man on my hips Got me tighter in my Dereon jeans Acting up drink in my cup I can care less what you think I need no permission did I mention Dont pay him any attention Cause you had your turn and now you gonna learn What it really feels like to miss me Cause if you liked it then you should have put a ring on it If you liked it then you shoulda put a ring on it Dont be mad once you see that he want it If you liked it then you shoulda put a ring on it Oh oh oh oh oh oh oh If you liked it then you should have put a ring on it If you liked it then you shoulda put a ring on it Dont be mad once you see that he want it If you liked it then you shoulda put a ring on it Oh oh oh oh oh oh oh oh Dont treat me to the things of the world Im not that kind of girl Your love is what I prefer what I deserve Heres a man that makes me then takes me And delivers me to a destiny to infinity and beyond Pull me into your arms say Im the one you own If you dont youll be alone And like a ghost Ill be gone All the single ladies all the single ladies All the single ladies all the single ladies All the single ladies all the single ladies All the single ladies Now put your hands up oh oh oh oh oh oh oh Cause if you liked it then you should have put a ring on it If you liked it then you shoulda put a ring on it Dont be mad once you see that he want it If you liked it then you shoulda put a ring on it Oh oh oh If you liked it then you should have put a ring on it If you liked it then you shoulda put a ring on it Dont be mad once you see that he want it If you liked it then you shoulda put a ring on it Oh oh oh ' ,
' Uh huh uh huh Yeah Rihanna Uh huh uh huh Good girl gone bad Uh huh uh huh Take three action Uh huh uh huh Hov No clouds in my stones Let it rain I hydroplane in the bank Comin down at the Dow Jones When the clouds come we gone We Rocafella We fly higher than weather In G5s or better You know me In anticipation for precipitation stack chips for the rainy day Rain Man is back with little Ms Sunshine Rihanna where you at You have my heart and well never be worlds apart Maybe in magazines but youll still be my star Baby cause in the dark You cant see shiny cars And thats when you need me there With you Ill always share Because When the sun shines well shine together Told you Ill be here forever Said Ill always be your friend Took an oath Ima stick it out til the end Now that its raining more than ever Know that well still have each other You can stand under my umbrella You can stand under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh eh eh eh These fancy things will never come in between Youre part of my entity here for infinity When the world has took its part When the world has dealt its cards If the hand is hard together well mend your heart Because When the sun shines we shine together Told you Ill be here forever Said Ill always be your friend Took an oath Ima stick it out til the end Now that its raining more than ever Know that well still have each other You can stand under my umbrella You can stand under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh eh eh eh You can run into my arms Its okay dont be alarmed Come into me Theres no distance in between our love So gon and let the rain pour Ill be all you need and more Because When the sun shines we shine together Told you Ill be here forever Said Ill always be your friend Took an oath Ima stick it out til the end Now that its raining more than ever Know that well still have each other You can stand under my umbrella You can stand under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh Under my umbrella ella ella eh eh eh eh eh eh Its raining raining Ooh baby its raining raining Baby come into me Come into me Its raining raining Ooh baby its raining raining You can always come into me Come into me Its pouring rain Its pouring rain Come into me Come into me Its pouring rain Its pouring rain ' ,
' Mmmmmmmm Let me talk to em Let me talk to em Let it rain mmmmmm Let me talk to em Cmon Shawty had them apple bottom jeans jeans Boots with the fur with the fur The whole club was lookin at her She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low Them baggy sweat pants and the Reeboks with the straps with the straps She turned around and gave that big booty a slap hey She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low Hey I aint never seen nothin thatll make me go This crazy all night spending my dough Had the million dollar vibe and a body to go Them birthday cakes they stole the show So sexual She was flexible professional Drinkin X and O Hold up wait a minute do I see what I think I whoa Did her thing I seen shawty get low Aint the same when its up that close Make it rain Im makin it snow Work the pole I got the bankroll Ima say that I prefer the no clothes Im into that I love women exposed She threw it back at me I gave her more Cash aint a problem I know where it go She had them apple bottom jeans jeans Boots with the fur with the fur The whole club was lookin at her She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low Them baggy sweat pants and the Reeboks with the straps with the straps She turned around and gave that big booty a slap ayy She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low Hey shawty what I gotta do to get you home My jeans filled with guap and they ready for shones Cadillacs Maybachs for the sexy grown Patron on the rocks thatll make your moan One stack cmon two stacks cmon three stacks cmon Now thats three grand What you think Im playin Babygirl Im the man I invented rubber bands Thats what I told her her legs on my shoulders I knew it was over That Henny and Cola got me like a soldier She ready for Rover I couldnt control her So lucky oh me I was just like a clover Shawty was hot like a toaster Sorry but I had to fold her Like a pornography poster she showed her Apple bottom jeans jeans Boots with the fur with the fur The whole club was lookin at her She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low Them baggy sweat pants and the Reeboks with the straps with the straps She turned around and gave that big booty a slap hey She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low Whoa shawty yeah she was worth the money Lil mama took my cash And I aint want it back The way she bent that back Got all them paper stacks Tattoo above her crack I had to handle that I was on it sexy woman Let me showin and make me want it Two in the morning Im zoned in Them Rosay bottles foaming She wouldnt stop made it drop Shawty did that pop and lock Had to break her off that guap Gal was fly just like my Glock Apple bottom jeans jeans Boots with the fur with the fur The whole club was lookin at her She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low Them baggy sweat pants and the Reeboks with the straps with the straps She turned around and gave that big booty a slap hey She hit the floor she hit the floor Next thing you know Shawty got low low low low low low low low cmon ' ,
' When you left I lost a part of me Its still so hard to believe Come back baby please Cause we belong together Haha remix Desert Storm Uh yo show your respect whenever you hear me or see me This is the emancipation of Mimi Hot like the real fever the real diva So successful yet still so eager No matter what they say its on forever Its our time right now more than ever To the death we gon get it on together And MC you know we belong together come on I lost a part of me When you left boy cant you see Boy come back baby please Cause we belong together Who am I gon lean on when times get rough Whos gon to talk to me til the sun comes up Whos gon take your place there aint nobody there Oh baby baby we belong together I only think of you on two occasions Thats day and night ohoh Id go for broke if I could be with you Only you can make it right make it right make it right We belong together like the sun in the summertime Bounce in a lemon range skip in a hummer lime P and kiss in and out Mariah on the other line Baby Ima come back believe itll come a time We belong together like peanut butter and jelly Februaries and skellies after parties and tellies Feel you in my stomach like you a part of my belly Baby Ima come back with every part of you ready I lost a part of me When you left boy cant you see Boy come back baby please Cause we belong together Who am I gon lean on when times get rough Whos gon to talk to me til the sun comes up Whos gon take your place there aint nobody there Oh baby baby we belong together I cant sleep at night when you are on my mind Bobby Womacks on the radio Saying to me If you think youre lonely now wait until tonight Boy Im feeling all out of my element throwing things crying Tryin to figure out where the hell I went wrong The pain reflected in this song Aint even half of what Im feeling inside I need you need you back in my life baby lets go You gon need a shoulder to cry on Classic Mustang Cobra to ride on Past is the past just let it be bygones Matter of fact I know a fly song that we could vibe on Lets get it straight If its the six or the quarter to eight Then Im throwing Babyface or Shy on Yeah and Kiss Ghost and MC Get close and toast to the diva and MCs Uh the trees will blow Big cups of Pinot Grigio take it easy though We belong together we know that Now I think that its bout time we show that Even though every moment wont be a Kodak naw Sometimes we argue I spaz out grab my bozak Come back not cause I have to I want to And naw I dont just wanna have you I want you uh I lost a part of me When you left boy cant you see Boy come back baby please Cause we belong together Who am I gon lean on when times get rough Whos gon to talk to me til the sun comes up Whos gon take your place there aint nobody there Oh baby baby we belong together This is the Desert Storm remix haha we belong together Oh baby baby we belong together DJ Clue Desert Storm oh come back baby please We belong together MC Oh come back baby please woo Is it so hard to believe We belong together We back baby oh baby baby we belong together We belong together ' ,
' If I should stay I would only be in your way So Ill go but I know Ill think of you every step of the way  Chorus And I Will always love you ooh I Will always love you you PostChorus You my darling you mm  Verse 1 Bittersweet memories That is all Im taking with me So goodbye please dont cry We both know Im not what you you need  Chorus And I I Will always love you ooh I Will always love you you  Verse 2 I hope life treats you kind And I hope you have all youve dreamed of And Im wishing you joy and happiness But above all this I wish you love  Chorus And I I Will always love you ooh I will always love you I will always love you ooh I will always love you ooh I will always love you ooh I I will always love you ' ,
' Load up on guns bring your friends Its fun to lose and to pretend Shes over bored and self assured Oh no I know a dirty word Hello hello hello how low Hello hello hello how low Hello hello hello how low Hello hello hello With the lights out its less dangerous Here we are now entertain us I feel stupid and contagious Here we are now entertain us A mulatto an albino a mosquito my libido Yeah hey Yay Im worse at what I do best And for this gift I feel blessed Our little group has always been And always will until the end Hello hello hello how low Hello hello hello how low Hello hello hello how low Hello hello hello With the lights out its less dangerous Here we are now entertain us I feel stupid and contagious Here we are now entertain us A mulatto an albino a mosquito my libido Yeah hey Yay And I forget just why I taste Oh yeah I guess it makes me smile I found it hard was hard to find Oh well whatever never mind Hello hello hello how low Hello hello hello how low Hello hello hello how low Hello hello hello With the lights out its less dangerous Here we are now entertain us I feel stupid and contagious Here we are now entertain us A mulatto an albino a mosquito my libido A denial a denial a denial a denial a denial A denial a denial a denial a denial ' ,
' Look into my eyes You will see what you mean to me Search your heart search your soul When you find me there youll search no more Dont tell me its not worth trying for You cant tell me its not worth dying for You know its true you know its true Everything I do I do it for you Yeah yeah Look in to your heart you will find There is nothing there to hide Take me as I am take my life I would give it all I would sacrifice Dont tell me its not worth fighting for I cant help it theres nothing I want more You know its true Everything I do I do it for you Theres no love like your love And no other could give me more love Theres nowhere unless youre there All the time all the way You cant tell me its not worth trying for Just cant help it theres nothing I want more Oh I would fight for you yeah Id lie for you Walk the wire for you yeah Id die for you You know its true Everything I do I do for you ' ,
' Its been seven hours and 15 days Since you took your love away I go out every night and sleep all day Since you took your love away Since you been gone I can do whatever I want I can see whomever I choose I can eat my dinner in a fancy restaurant But nothing I said nothing can take away these blues Cause nothing compares Nothing compares to you Its been so lonely without you here Like a bird without a song Nothing can stop these lonely tears from falling Tell me baby where did I go wrong I could put my arms around every boy I see But theyd only remind me of you I went to the doctor guess what he told me Guess what he told me He said Girl you better try to have fun no matter what you do But hes a fool Cause nothing compares nothing compares to you All the flowers that you planted mama In the back yard All died when you went away I know that living with you baby was sometimes hard But Im willing to give it another try Nothing compares Nothing compares to you Nothing compares Nothing compares to you Nothing compares Nothing compares to you ' ,
' Every night in my dreams I see you I feel you That is how I know you go on Far across the distance And spaces between us You have come to show you go on Near far wherever you are I believe that the heart does go on Once more you open the door And youre here in my heart And my heart will go on and on Love can touch us one time And last for a lifetime And never let go til were gone Love was when I loved you One true time Id hold to In my life well always go on Near far wherever you are I believe that the heart does go on why does the heart go on Once more you open the door And youre here in my heart And my heart will go on and on Youre here theres nothing I fear And I know that my heart will go on Well stay forever this way You are safe in my heart and My heart will go on and on ' ,
' Goodbye Norma Jeane Though I never knew you at all You had the grace to hold yourself While those around you crawled They crawled out of the woodwork And they whispered into your brain They set you on the treadmill And they made you change your name And it seems to me you lived your life Like a candle in the wind Never knowing who to cling to When the rain set in And I wouldve liked to know you But I was just a kid Your candle burned out long before Your legend ever did Loneliness was tough The toughest role you ever played Hollywood created a superstar And pain was the price you paid Even when you died Oh the press still hounded you All the papers had to say Was that Marilyn was found in the nude And it seems to me you lived your life Like a candle in the wind Never knowing who to cling to When the rain set in And I wouldve liked to know you But I was just a kid Your candle burned out long before Your legend ever did Goodbye Norma Jeane Though I never knew you at all You had the grace to hold yourself While those around you crawled Goodbye Norma Jeane From the young man in the twenty second row Who sees you as something more than sexual More than just our Marilyn Monroe And it seems to me you lived your life Like a candle in the wind Never knowing who to cling to When the rain set in And I wouldve liked to know you But I was just a kid Your candle burned out long before Your legend ever did Your candle burned out long before Your legend ever did ' ,
' Oh life is bigger Its bigger than you And you are not me The lengths that I will go to The distance in your eyes Oh no Ive said too much I set it up Thats me in the corner Thats me in the spotlight Losing my religion Trying to keep up with you And I dont know if I can do it Oh no Ive said too much I havent said enough I thought that I heard you laughing I thought that I heard you sing I think I thought I saw you try Every whisper of every waking hour Im choosing my confessions Trying to keep an eye on you Like a hurt lost and blinded fool fool Oh no Ive said too much I set it up Consider this Consider this the hint of the century Consider this the slip That brought me to my knees failed What if all these fantasies come Flailing around Now Ive said too much I thought that I heard you laughing I thought that I heard you sing I think I thought I saw you try But that was just a dream That was just a dream Thats me in the corner Thats me in the spotlight Losing my religion Trying to keep up with you And I dont know if I can do it Oh no Ive said too much I havent said enough I thought that I heard you laughing I thought that I heard you sing I think I thought I saw you try But that was just a dream Try cry fly try That was just a dream Just a dream Just a dream dream ' ,
' Today is gonna be the day that theyre gonna throw it back to you And by now you shouldve somehow realised what you gotta do I dont believe that anybody feels the way I do about you now And backbeat the word is on the street that the fire in your heart is out Im sure youve heard it all before but you never really had a doubt I dont believe that anybody feels the way I do about you now And all the roads we have to walk are winding And all the lights that lead us there are blinding There are many things that I would like to say to you but I dont know how Because maybe Youre gonna be the one that saves me And after all Youre my wonderwall Today was gonna be the day but theyll never throw it back to you And by now you shouldve somehow realised what youre not to do I dont believe that anybody feels the way I do about you now And all the roads that lead you there were winding And all the lights that light the way are blinding There are many things that I would like to say to you but I dont know how I said maybe Youre gonna be the one that saves me And after all Youre my wonderwall I said maybe I said maybe Youre gonna be the one that saves me And after all Youre my wonderwall I said maybe I said maybe Youre gonna be the one that saves me saves me Youre gonna be the one that saves me saves me Youre gonna be the one that saves me saves me ' ,
' Verse 1 Is it getting better Or do you feel the same Will it make it easier on you now You got someone to blame  Chorus You say one love one life When its one need in the night One love we get to share it Leaves you baby if you dont care for it Verse 2 Did I disappoint you Or leave a bad taste in your mouth You act like you never had love And you want me to go without  Chorus Well its too late tonight To drag the past out into the light Were one but were not the same We get to carry each other carry each other One  Verse 3 Have you come here for forgiveness Have you come to raise the dead Have you come here to play Jesus To the lepers in your head  Chorus Did I ask too much More than a lot You gave me nothing now its all I got Were one but were not the same Well we hurt each other then we do it again  Bridge You say love is a temple love a higher law Love is a temple love the higher law You ask me to enter but then you make me crawl And I cant be holding on to what you got When all you got is hurt You might also like Kill Bill SZA O Holy Night Christmas Songs With or Without You U2 Chorus One love one blood One life you got to do what you should One life with each other Sisters brothers One life but were not the same We get to carry each other carry each other One One  Outro Oohoohooh Ohooh May we may we may we get Higher Oh higher Ay yeah go higher Oh Higher ' ,
' She was more like a beauty queen from a movie scene I said dont mind but what do you mean I am the one Who will dance on the floor in the round She said I am the one who will dance on the floor in the round She told me her name was Billie Jean as she caused a scene Then every head turned with eyes that dreamed of being the one Who will dance on the floor in the round People always told me be careful of what you do And dont go around breaking young girls hearts And mother always told me be careful of who you love And be careful of what you do cause the lie becomes the truth Billie Jean is not my lover Shes just a girl who claims that I am the one But the kid is not my son She says I am the one but the kid is not my son For forty days and forty nights The law was on her side But who can stand when shes in demand Her schemes and plans Cause we danced on the floor in the round So take my strong advice just remember to always think twice Do think twice do think twice She told my baby wed danced til three then she looked at me Then showed a photo my baby cried his eyes were like mine oh no Cause we danced on the floor in the round baby People always told me be careful of what you do And dont go around breaking young girls hearts She came and stood right by me Just the smell of sweet perfume This happened much too soon She called me to her room Billie Jean is not my lover Shes just a girl who claims that I am the one But the kid is not my son Billie Jean is not my lover Shes just a girl who claims that I am the one But the kid is not my son She says I am the one but the kid is not my son She says I am the one but the kid is not my son Billie Jean is not my lover Shes just a girl who claims that I am the one But the kid is not my son She says I am the one but the kid is not my son She says I am the one You know what you did she says he is my son breaking my heart babe She says I am the one Billie Jean is not my lover Billie Jean is not my lover Billie Jean is not my lover Billie Jean is not my lover dont Billie Jean Billie Jean is not my lover Billie Jean is not my lover ' ,
' Verse 1 Every breath you take And every move you make Every bond you break Every step you take Ill be watching you Every single day And every word you say Every game you play Every night you stay Ill be watching you Chorus Oh cant you see you belong to me How my poor heart aches with every step you take  Verse 2 Every move you make And every vow you break Every smile you fake Every claim you stake Ill be watching you  Bridge Since youve gone Ive been lost without a trace I dream at night I can only see your face I look around but its you I cant replace I feel so cold and I long for your embrace I keep crying baby baby please  MiddleEight Mmm mmm mmm mmm Mmm mmm mmm  Chorus Oh cant you see you belong to me How my poor heart aches with every step you take You might also like Glimpse of Us Joji Grrrls Lizzo Let’s Stay Together Al Green Verse 3 Every move you make And every vow you break Every smile you fake Every claim you stake Ill be watching you Every move you make Every step you take Ill be watching you  Outro Ill be watching you  Every breath you take Every move you make Every bond you break Every step you take Ill be watching you  Every single day Every word you say Every game you play Every night you stay Ill be watching you  Every move you make Every vow you break Every smile you fake Every claim you stake Ill be watching you Every single day Every word you say Every game you play Every night you stay Ill be watching you  Every breath you take Every move you make Every bond you break Every step you take Ill be watching you  Every single day Every word you say Every game you play Every night you stay Ill be watching you  Every move you make Every vow you break Every smile you fake Every claim you stake Ill be watching you  Every single day Every word you say Every game you play Every night you stay Ill be watching you ' ,
' Shes got a smile that it seems to me Reminds me of childhood memories Where everything was as fresh as the bright blue sky Now and then when I see her face She takes me away to that special place And if I stare too long Id probably break down and cry Whoa oh oh Sweet child o mine Whoa oh oh oh Sweet love of mine Shes got eyes of the bluest skies As if they thought of rain Id hate to look into those eyes and see an ounce of pain Her hair reminds me of a warm safe place Where as a child Id hide And pray for the thunder and the rain to quietly pass me by Whoa oh oh Sweet child o mine Whoa whoa oh oh oh Sweet love of mine Whoa yeah Whoa oh oh oh Sweet child o mine Whoa oh whoa oh Sweet love of mine Whoa oh oh oh Sweet child o mine Ooh yeah Ooh sweet love of mine Where do we go Where do we go now Where do we go Ooh oh where do we go Where do we go now Oh where do we go now Where do we go Sweet child Where do we go now Ay ay ay ay ay ay ay ay Where do we go now Ah ah Where do we go Oh where do we go now Oh where do we go Oh where do we go now Where do we go Oh where do we go now Now now now now now now now Sweet child Sweet child of mine ' ,
' Dig if you will the picture Of you and I engaged in a kiss The sweat of your body covers me Can you my darling Can you picture this Dream if you can a courtyard An ocean of violets in bloom Animals strike curious poses They feel the heat The heat between me and you How can you just leave me standing Alone in a world thats so cold So cold Maybe Im just too demanding Maybe Im just like my father too bold Maybe youre just like my mother Shes never satisfied shes never satisfied Why do we scream at each other This is what it sounds like When doves cry Touch if you will my stomach Feel how it trembles inside Youve got the butterflies all tied up Dont make me chase you Even doves have pride How could you just leave me standing Alone in a world so cold World so cold Maybe Im just too demanding Maybe Im just like my father too bold Maybe youre just like my mother Shes never satisfied shes never satisfied Why do we scream at each other This is what it sounds like When doves cry How can you just leave me standing Alone in a world thats so cold A world thats so cold Maybe Im just too demanding maybe maybe Im like my father Maybe Im just like my father too bold you know hes too bold Maybe youre just like my mother maybe youre just like my mother Shes never satisfied shes never never satisfied Why do we scream at each other Why do we scream why This is what it sounds like When doves cry When doves cry doves cry doves cry When doves cry doves cry doves cry Dont cry dont cry ' ,
' I saw him dancin there by the record machine I knew he must a been about seventeen The beat was goin strong Playin my favorite song And I could tell it wouldnt be long Til he was with me yeah me And I could tell it wouldnt be long Til he was with me yeah me singin I love rock n roll So put another dime in the jukebox baby I love rock n roll So come and take your time and dance with me Ow He smiled so I got up and asked for his name That dont matter he said cause its all the same I said Can I take you home where we can be alone And next we were movin on He was with me yeah me Next we were movin on He was with me yeah me singin I love rock n roll So put another dime in the jukebox baby I love rock n roll So come and take your time and dance with me Ow Said Can I take you home where we can be alone Next we were movin on He was with me yeah me And well be movin on And singin that same old song Yeah with me singin I love rock n roll So put another dime in the jukebox baby I love rock n roll So come and take your time and dance with me I love rock n roll So put another dime in the jukebox baby I love rock n roll So come and take your time and dance with I love rock n roll So put another dime in the jukebox baby I love rock n roll So come and take your time and dance with I love rock n roll So put another dime in the jukebox baby I love rock n roll So come and take your time and dance with I love rock n roll So put another dime in the jukebox baby I love rock n roll So come and take your time and dance with me ' ,
' See the stone set in your eyes See the thorn twist in your side Ill wait for you Sleight of hand and twist of fate On a bed of nails she makes me wait And I wait without you With or without you With or without you Through the storm we reach the shore You give it all but I want more And Im waiting for you With or without you With or without you ah ah I cant live With or without you And you give yourself away And you give yourself away And you give And you give And you give yourself away My hands are tied My body bruised she got me with Nothing to win and Nothing left to lose And you give yourself away And you give yourself away And you give And you give And you give yourself away With or without you With or without you oh I cant live With or without you Oh oh Oh oh With or without you With or without you oh I cant live With or without you With or without you ' ,
' Once upon a time not so long ago Tommy used to work on the docks unions been on strike Hes down on his luck its tough so tough Gina works the diner all day working for her man She brings home her pay for love for love She says weve got to hold on to what weve got It doesnt make a difference if we make it or not Weve got each other and thats a lot for love Well give it a shot Woah were half way there Woah livin on a prayer Take my hand well make it I swear Woah livin on a prayer Tommys got his sixstring in hock Now hes holding in what he used to make it talk So tough its tough Gina dreams of running away When she cries in the night Tommy whispers Baby its okay someday Weve got to hold on to what weve got It doesnt make a difference if we make it or not Weve got each other and thats a lot for love Well give it a shot Woah were half way there Woah livin on a prayer Take my hand well make it I swear Woah livin on a prayer Livin on a prayer Oh weve got to hold on ready or not You live for the fight when its all that youve got Woah were half way there Woah livin on a prayer Take my hand well make it I swear Woah livin on a prayer Woah were half way there Woah livin on a prayer Take my hand well make it I swear Woah livin on a prayer Woah were half way there Woah livin on a prayer Take my hand well make it I swear Woah livin on a prayer ' ,
' My love Theres only you in my life The only thing thats right My first love Youre every breath that I take Youre every step I make And I I want to share All my love with you No one else will do And your eyes Your eyes your eyes They tell me how much you care Oh yes you will always be My endless love Two hearts Two hearts that beat as one Our lives have just begun Forever Ohhhhhh Ill hold you close in my arms I cant resist your charms And love Oh love Ill be a fool For you Im sure You know I dont mind Oh you know I dont mind Cause you You mean the world to me Oh I know I know Ive found in you My endless love Ooohwoow Boom boom Oh and love Oh love Ill be that fool For you Im sure You know I dont mind Oh you know I dont mind And I dont mind And yes Youll be the only one Cause no one can deny This love I have inside And Ill give it all to you My love My love my love My endless love ' ,
' I get up and nothin gets me down You got it tough Ive seen the toughest around And I know baby just how you feel You got to roll with the punches and get to whats real Ah cant you see me standin here I got my back against the record machine I aint the worst that youve seen Ah cant you see what I mean Ah might as well jump jump Might as well jump Go ahead and jump jump Go ahead and jump Ow oh hey you Who said that Baby how you been You say you dont know You wont know until you begin So cant ya see me standing here I got my back against the record machine I aint the worst that youve seen Ah cant you see what I mean Ah might as well jump jump Go ahead and jump Might as well jump jump Go ahead and jump Jump Might as well jump jump Go ahead and jump Get it in jump jump Go ahead and jump Jump Jump Jump Jump ' ,
' They told him Dont you ever come around here Dont wanna see your face you better disappear The fires in their eyes and their words are really clear So beat it just beat it You better run you better do what you can Dont wanna see no blood dont be a macho man You wanna be tough better do what you can So beat it but you wanna be bad Just beat it beat it beat it beat it No one wants to be defeated Showin how funky and strong is your fight It doesnt matter whos wrong or right Just beat it beat it Just beat it beat it Just beat it beat it Just beat it beat it uh Theyre out to get you better leave while you can Dont wanna be a boy you wanna be a man You wanna stay alive better do what you can So beat it just beat it You have to show them that youre really not scared Youre playin with your life this aint no truth or dare Theyll kick you then theyll beat you Then theyll tell you its fair So beat it but you wanna be bad Just beat it beat it beat it beat it No one wants to be defeated Showin how funky and strong is your fight It doesnt matter whos wrong or right Just beat it beat it beat it beat it No one wants to be defeated Showin how funky and strong is your fight It doesnt matter whos wrong or right Just beat it beat it beat it beat it Beat it beat it beat it Beat it beat it beat it Beat it beat it beat it Beat it beat it beat it Beat it beat it beat it beat it No one wants to be defeated Showin how funky and strong is your fight It doesnt matter whos wrong or right whos right Just beat it beat it beat it beat it No one wants to be defeated no one Showin how funky and strong is your fight It doesnt matter whos wrong or right Just beat it beat it beat it beat it No one wants to be defeated oh no Showin how funky and strong is your fight It doesnt matter whos wrong or right Just beat it beat it beat it beat it No one wants to be defeated Showin how funky and strong is your fight It doesnt matter whos wrong or right Just beat it beat it beat it beat it ' ,
' Is this the real life Is this just fantasy Caught in a landside No escape from reality Open your eyes Look up to the skies and see Im just a poor boy I need no sympathy Because Im easy come easy go Little high little low Any way the wind blows doesnt really matter to Me to me Mamaaa Just killed a man Put a gun against his head pulled my trigger Now hes dead Mamaaa life had just begun But now Ive gone and thrown it all away Mama oooh Didnt mean to make you cry If Im not back again this time tomorrow Carry on carry on as if nothing really matters Too late my time has come Sends shivers down my spine bodys aching all The time Goodbye everybody Ive got to go Gotta leave you all behind and face the truth Mama oooh I dont want to die I sometimes wish Id never been born at all I see a little silhouetto of a man Scaramouch Scaramouch will you do the Fandango Thunderbolts and lightning very very frightening me Galileo Galileo Galileo Galileo Galileo Figaro  magnificoo Im just a poor boy nobody loves me Hes just a poor boy from a poor family Spare him his life from this monstrosity Easy come easy go will you let me go Bismillah No we will not let you go Let him go Bismillah We will not let you go Let him go Bismillah We will not let you go Let me go Will not let you go Let me goNever Never let you go Let me go Never let you go Let me go Ah No no no no no no no Oh mama mia mama mia mama mia let me go Beelzebub has a devil put aside for me for me For meee So you think you can stop me and spit in my eye So you think you can love me and leave me to die Oh baby cant do this to me baby Just gotta get out just gotta get right outta here Nothing really matters Anyone can see Nothing really matters Nothing really matters to me Any way the wind blows ' ,
' Imagine theres no heaven Its easy if you try No hell below us Above us only sky Imagine all the people Livin for today Ah Imagine theres no countries It isnt hard to do Nothing to kill or die for And no religion too Imagine all the people Livin life in peace You You may say Im a dreamer But Im not the only one I hope someday youll join us And the world will be as one Imagine no possessions I wonder if you can No need for greed or hunger A brotherhood of man Imagine all the people Sharing all the world You You may say Im a dreamer But Im not the only one I hope someday youll join us And the world will live as one ' ,
' Well you can tell by the way I use my walk Im a womans man no time to talk Music loud and women warm Ive been kicked around Since I was born And now its alright its okay And you may look the other way We can try to understand The New York Times effect on man Whether youre a brother or whether youre a mother Youre stayin alive stayin alive Feel the city breakin and everybody shakin And were stayin alive stayin alive Ah ha ha ha stayin alive stayin alive Ah ha ha ha stayin alive Oh when you walk Well now I get low and I get high And if I cant get either I really try Got the wings of Heaven on my shoes Im a dancin man and I just cant lose You know its alright its okay Ill live to see another day We can try to understand The New York Times effect on man Whether youre a brother or whether youre a mother Youre stayin alive stayin alive Feel the city breakin and everybody shakin And were stayin alive stayin alive Ah ha ha ha stayin alive stayin alive oh Ah ha ha ha stayin alive oh Life goin nowhere somebody help me Somebody help me yeah Life goin nowhere somebody help me yeah Im stayin alive Well you can tell by the way I use my walk Im a womans man no time to talk Music loud and women warm Ive been kicked around since I was born And now its all right its okay And you may look the other way We can try to understand The New York Times effect on man Whether youre a brother or whether youre a mother Youre stayin alive stayin alive Feel the city breakin and everybody shakin And were stayin alive stayin alive Ah ha ha ha stayin alive stayin alive Ah ha ha ha stayin alive hey Life goin nowhere somebody help me Somebody help me yeah Life goin nowhere somebody help me yeah Im stayin alive Life goin nowhere somebody help me Somebody help me yeah ah ah ah Life goin nowhere somebody help me yeah Im stayin alive Life goin nowhere somebody help me Somebody help me yeah ah ah ah ay Life goin nowhere somebody help me yeah Im stayin alive Life goin nowhere somebody help me Somebody help me yeah oh Life goin nowhere somebody help me yeah Im stayin alive ' ,
' When youre weary feeling small When tears are in your eyes I will dry Them all Im on your side When times get rough And friends just cant be found Like a bridge over troubled water I will lay me down Like a bridge over troubled water I will lay me down When youre down and out When youre on the street When evening falls so hard I will comfort you Ill take your part When darkness comes And pain is all around Like a bridge over troubled water I will lay me down Like a bridge over troubled water I will lay me down Sail on silver girl Sail on by Your time has come to shine All your dreams are on their way See how they shine If you need a friend Im sailing right behind Like a bridge over troubled water I will ease your mind Like a bridge over troubled water I will ease your mind ' ,
' On a dark desert highway Cool wind in my hair Warm smell of colitas Rising up through the air Up ahead in the distance I saw a shimmering light My head grew heavy and my sight grew dim I had to stop for the night There she stood in the doorway I heard the mission bell And I was thinking to myself This could be Heaven or this could be Hell Then she lit up a candle And she showed me the way There were voices down the corridor I thought I heard them say Welcome to the Hotel California Such a lovely place such a lovely place Such a lovely face Plenty of room at the Hotel California Any time of year any time of year You can find it here Her mind is Tiffanytwisted She got the Mercedes Benz She got a lot of pretty pretty boys That she calls friends How they dance in the courtyard Sweet summer sweat Some dance to remember Some dance to forget So I called up the Captain Please bring me my wine He said We havent had that spirit here Since 1969 And still those voices are calling from far away Wake you up in the middle of the night Just to hear them say Welcome to the Hotel California Such a lovely place such a lovely place Such a lovely face They livin it up at the Hotel California What a nice surprise what a nice surprise Bring your alibis Mirrors on the ceiling The pink champagne on ice And she said We are all just prisoners here Of our own device And in the masters chambers They gathered for the feast They stab it with their steely knives But they just cant kill the beast Last thing I remember I was Running for the door I had to find the passage back To the place I was before Relax  said the night man We are programmed to receive You can check out any time you like But you can never leave ' ,
' Theres a lady whos sure All that glitters is gold And shes buying a stairway to heaven When she gets there she knows If the stores are all closed With a word she can get what she came for Ooh ooh ooh ooh ooh And shes buying a stairway to heaven Theres a sign on the wall But she wants to be sure Cause you know sometimes words have two meanings In a tree by the brook Theres a songbird who sings Sometimes all of our thoughts are misgiven Ooh it makes me wonder Ooh it makes me wonder Theres a feeling I get When I look to the west And my spirit is crying for leaving In my thoughts I have seen Rings of smoke through the trees And the voices of those who stand looking Ooh it makes me wonder Ooh it really makes me wonder And its whispered that soon If we all call the tune Then the piper will lead us to reason And a new day will dawn For those who stand long And the forests will echo with laughter Oh whoawhoawhoa ohoh If theres a bustle in your hedgerow dont be alarmed now Its just a spring clean for the May Queen Yes there are two paths you can go by but in the long run And theres still time to change the road youre on And it makes me wonder Oh whoa Your head is humming and it wont go In case you dont know The pipers calling you to join him Dear lady can you hear the wind blow And did you know Your stairway lies on the whispering wind And as we wind on down the road Our shadows taller than our soul There walks a lady we all know Who shines white light and wants to show How everything still turns to gold And if you listen very hard The tune will come to you at last When all are one and one is all yeah To be a rock and not to roll And shes buying a stairway to heaven ' ,
' Long long time ago I can still remember How that music used to make me smile And I knew if I had my chance That I could make those people dance And maybe theyd be happy for a while But February made me shiver With every paper Id deliver Bad news on the doorstep I couldnt take one more step I cant remember if I cried When I read about his widowed bride But something touched me deep inside The day the music died So byebye Miss American Pie Drove my Chevy to the levee But the levee was dry Them good old boys were drinking whiskey and rye Singing Thisll be the day that I die This will be the day that I die Did you write the Book of Love And do you have faith in God above If the Bible tells you so Do you believe in rock n roll Can music save your mortal soul And can you teach me how to dance real slow Well I know that youre in love with him Cause I saw you dancing in the gym You both kicked off your shoes Then I dig those rhythm and blues I was a lonely teenage broncin buck With a pink carnation and a pickup truck But I knew I was out of luck The day the music died I started singing byebye Miss American Pie Drove my Chevy to the levee But the levee was dry Them good old boys were drinking whiskey and rye Singing Thisll be the day that I die This will be the day that I die Now for ten years weve been on our own And moss grows fat on a rolling stone But thats not how it used to be When the jester sang for the King and Queen In a coat he borrowed from James Dean And a voice that came from you and me Oh and while the King was looking down The jester stole his thorny crown The courtroom was adjourned No verdict was returned And while Lenin read a book of Marx The Quartet practiced in the park And we sang dirges in the dark The day the music died We were singing byebye Miss American Pie Drove my Chevy to the levee But the levee was dry Them good old boys were drinking whiskey and rye Singing Thisll be the day that I die This will be the day that I die Helter skelter in the summer swelter The birds flew off with a fallout shelter Eight miles high and falling fast It landed foul on the grass the players tried for a forward pass With the jester on the sidelines in a cast Now the halftime air was sweet perfume While the sergeants played a marching tune We all got up to dance Oh but we never got the chance Cause the players tried to take the field The marching band refused to yield Do you recall what was revealed The day the music died We started singing byebye Miss American Pie Drove my Chevy to the levee but the levee was dry Them good old boys were drinking whiskey and rye And singing Thisll be the day that I die This will be the day that I die Oh and there we were all in one place A generation lost in space With no time left to start again So come on Jack be nimble Jack be quick Jack Flash sat on a candlestick Cause fire is the devils only friend Oh and as I watched him on the stage My hands were clenched in fists of rage No angel born in Hell Could break that Satans spell And as the flames climbed high into the night To light the sacrificial rite I saw Satan laughing with delight The day the music died He was singing byebye Miss American Pie Drove my Chevy to the levee but the levee was dry Them good old boys were drinking whiskey and rye And singing Thisll be the day that I die This will be the day that I die I met a girl who sang the blues And I asked her for some happy news But she just smiled and turned away I went down to the sacred store Where Id heard the music years before But the man there said the music wouldnt play And in the streets the children screamed The lovers cried and the poets dreamed But not a word was spoken The church bells all were broken And the three men I admire most The Father Son and the Holy Ghost They caught the last train for the coast The day the music died And they were singing byebye Miss American Pie Drove my Chevy to the levee but the levee was dry And them good old boys were drinking whiskey and rye Singing Thisll be the day that I die This will be the day that I die They were singing byebye Miss American Pie Drove my Chevy to the levee but the levee was dry Them good old boys were drinking whiskey and rye Singing Thisll be the day that I die ' ,
' When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be be And when the night is cloudy there is still a light that shines on me Shinin until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be And let it be let it be let it be let it be Whisper words of wisdom let it be And let it be let it be let it be let it be Whisper words of wisdom let it be ' ,
' Very superstitious Writings on the wall Very superstitious Ladders bout to fall Thirteen month old baby Broke the lookin glass Seven years of bad luck The good things in your past When you believe in things That you dont understand Then you suffer Superstition aint the way Hey Very superstitious Wash your face and hands Rid me of the problem Do all that you can Keep me in a daydream Keep me goin strong You dont wanna save me Sad is the soul When you believe in things That you dont understand Then you suffer Superstition aint the way Yeh yeh Very superstitious Nothin more to say Very superstitious The devils on his way Thirteen month old baby Broke the lookin glass Seven years of bad luck Good things in your past When you believe in things That you dont understand Then you suffer Superstition aint the way No no no ' ,
' Whatll you do when you get lonely And nobodys waiting by your side Youve been running and hiding much too long You know its just your foolish pride Layla youve got me on my knees Layla Im begging darling please Layla darling wont you ease my worried mind I tried to give you consolation When your old man had let you down Like a fool I fell in love with you You turned my whole world upside down Layla youve got me on my knees Layla Im begging darling please Layla darling wont you ease my worried mind Make the best of the situation Before I finally go insane Please dont say well never find a way And tell me all my loves in vain Layla youve got me on my knees Layla Im begging darling please Layla darling wont you ease my worried mind Layla youve got me on my knees Layla Im begging darling please Layla darling wont you ease my worried mind ' ,
' I cant get no satisfaction I cant get no satisfaction Cause I try and I try and I try and I try I cant get no I cant get no When Im driving in my car When a man come on the radio Hes telling me more and more About some useless information Supposed to fire my imagination I cant get no oh no no no hey hey hey Thats what I say I cant get no satisfaction I cant get no satisfaction Cause I try and I try and I try and I try I cant get no I cant get no When Im watchin my TV And a man comes on and tells me How white my shirts can be But he cant be a man cause he doesnt smoke The same cigarettes as me I cant get no oh no no no hey hey hey Thats what I say I cant get no satisfaction I cant get no girl reaction Cause I try and I try and I try and I try I cant get no I cant get no When Im ridin round the world And Im doin this and Im signin that And Im tryin to make some girl who tells me Baby better come back maybe next week Cant you see Im on a losing streak I cant get no oh no no no hey hey hey Thats what I say I cant get no I cant get no I cant get no satisfaction no satisfaction No satisfaction no satisfaction I cant get no ' ,
' Hey Jude dont make it bad Take a sad song and make it better Remember to let her into your heart Then you can start to make it better Hey Jude dont be afraid You were made to go out and get her The minute you let her under your skin Then you begin to make it better And anytime you feel the pain hey Jude refrain Dont carry the world upon your shoulders For well you know that its a fool who plays it cool By making his world a little colder Hey Jude dont let me down You have found her now go and get her Remember to let her into your heart Then you can start to make it better So let it out and let it in hey Jude begin Youre waiting for someone to perform with And dont you know that its just you hey Jude youll do The movement you need is on your shoulder Hey Jude dont make it bad Take a sad song and make it better Remember to let her under your skin Then youll begin to make it Better better better better better better oh Na na na nananana nannana hey Jude repeat X number of times fade ' ,
' Ooo I bet youre wonderin how I knew Bout your plans to make me blue With some other guy that you knew before Between the two of us guys You know I loved you more It took me by surprise I must say When I found out yesterday Ooo I heard it through the grapevine Not much longer would you be mine Ooo I heard it through the grapevine And Im just about to lose my mind Honey honey yeah You know that a man aint supposed to cry But these tears I cant hold inside Losin you would end my life you see Cause you mean that much to me You could have told me yourself That you found someone else Instead I heard it through the grapevine Not much longer would you be mine Ooo I heard it through the grapevine And Im just about to lose my mind Honey honey yeah People say you believe half from what you see Non non none from what you hear I cant help being confused If its true wont tell me here Do you plan to let me go For the other guy that you knew before Ooo I heard it through the grapevine Not much longer would you be mine Ooo I heard it through the grapevine And Im just about to loss my mind Honey honey yeah Ooo I heard it through the grapevine Not much longer would you be mine Ooo I heard it through the grapevine And Im just about to lose my mind Ooo I heard it through the grapevine Not much longer would you be mine Ahh I heard it through the grapevine And Im just about to lose my mind honey honey yeah ' ,
' Hey what you want Oo Baby I got Oo What you need Oo Do you know I got it Oo All Im askin Oo Is for a little respect when you come home just a little bit Hey baby just a little bit when you get home Just a little bit mister just a little bit I aint gonna do you wrong while youre gone Aint gonna do you wrong oo cause I dont wanna oo All Im askin oo Is for a little respect when you come home just a little bit Baby just a little bit when you get home just a little bit Yeah just a little bit Im about to give you all of my money And all Im askin in return honey Is to give me my profits When you get home just a just a just a just a Yeah baby just a just a just a just a When you get home just a little bit Yeah just a little bit Do it for me now just a little bit Ooo your kisses oo Sweeter than honey oo And guess what oo So is my money oo All I want you to do oo for me Is give it to me when you get home re re re re Yeah baby re re re re Whip it to me respect just a little bit When you get home now just a little bit RESPECT Find out what it means to me RESPECT Take care TCB Oh sock it to me sock it to me Sock it to me sock it to me A little respect sock it to me sock it to me Sock it to me sock it to me Whoa babe just a little bit A little respect just a little bit I get tired just a little bit Keep on tryin just a little bit Youre runnin out of foolin just a little bit And I aint lyin just a little bit spect When you come home re re re re Or you might walk in respect just a little bit And find out Im gone just a little bit I got to have just a little bit A little respect just a little bit ' ,
' Oh yeah Ill tell you somethin I think youll understand When I say that somethin I want to hold your hand I want to hold your hand I want to hold your hand Oh please say to me Youll let me be your man And please say to me Youll let me hold your hand Youll let me hold your hand I want to hold your hand And when I touch you I feel happy inside Its such a feelin that my love I cant hide I cant hide I cant hide Yeah you got that somethin I think youll understand When I say that somethin I want to hold your hand I want to hold your hand I want to hold your hand And when I touch you I feel happy inside Its such a feelin that my love I cant hide I cant hide I cant hide Yeah you got that somethin I think youll understand When I feel that somethin I want to hold your hand I want to hold your hand I want to hold your hand I want to hold your hand ' ,
' II love the colorful clothes she wears And the way the sunlight plays upon her hair I hear the sound of a gentle word On the wind that lifts her perfume through the air Im pickin up good vibrations Shes giving me the excitations oom bop bop Im pickin up good vibrations good vibrations oom bop bop Shes giving me the excitations excitations oom bop bop Im pickin up good vibrations oom bop bop Shes giving me the excitations excitations oom bop bop Im pickin up good vibrations oom bop bop Shes giving me the excitations excitations Close my eyes shes somehow closer now Softly smile I know she must be kind When I look in her eyes She goes with me to a blossom world Im pickin up good vibrations Shes giving me excitations oom bop bop Im pickin up good vibrations good vibrations oom bop bop Shes giving me excitations excitations oom bop bop Good good good good vibrations oom bop bop Shes giving me excitations excitations oom bop bop Good good good good vibrations oom bop bop Shes giving me excitations excitations Ah ah my my what elation I dont know where but she sends me there Oh my my what a sensation Oh my my what elation Oh my my what Gotta keep those lovin good vibrations ahappenin with her Gotta keep those lovin good vibrations ahappenin with her Gotta keep those lovin good vibrations ahappenin Good good good good vibrations oom bop bop Shes giving me the excitations excitations oom bop bop Im pickin up good vibrations Na na na na na na na na Na na na na na na na na bop bopbopbopbop bop Do do do do do do do do bop bopbopbopbop bop Do do do do do do do do bop bopbopbopbop bop ' ,
' Verse 1 Yesterday All my troubles seemed so far away Now it looks as though theyre here to stay Oh I believe in yesterday  Verse 2 Suddenly Im not half the man I used to be Theres a shadow hanging over me Oh yesterday came suddenly Chorus Why she had to go I dont know she wouldnt say I said something wrong now I long for yesterday  Verse 3 Yesterday Love was such an easy game to play Now I need a place to hide away Oh I believe in yesterday  Chorus Why she had to go I dont know she wouldnt say I said something wrong now I long for yesterday  Verse 3 Yesterday Love was such an easy game to play Now I need a place to hide away Oh I believe in yesterday ' ,
' Once upon a time you dressed so fine Threw the bums a dime in your prime didnt you People call say beware doll youre bound to fall You thought they were all kidding you You used to laugh about Everybody that was hanging out Now you dont talk so loud Now you dont seem so proud About having to be scrounging your next meal How does it feel how does it feel To be without a home Like a complete unknown like a rolling stone Ahh youve gone to the finest schools alright Miss Lonely But you know you only used to get juiced in it Nobodys ever taught you how to live out on the street And now youre gonna have to get used to it You say you never compromise With the mystery tramp but now you realize Hes not selling any alibis As you stare into the vacuum of his eyes And say do you want to make a deal How does it feel how does it feel To be on your own with no direction home A complete unknown like a rolling stone Ah you never turned around to see the frowns On the jugglers and the clowns when they all did tricks for you You never understood that it aint no good You shouldnt let other people get your kicks for you You used to ride on a chrome horse with your diplomat Who carried on his shoulder a Siamese cat Aint it hard when you discovered that He really wasnt where its at After he took from you everything he could steal How does it feel how does it feel To be on your own with no direction home Like a complete unknown like a rolling stone Ahh princess on a steeple and all the pretty people Theyre all drinking thinking that theyve got it made Exchanging all precious gifts But you better take your diamond ring you better pawn it babe You used to be so amused At Napoleon in rags and the language that he used Go to him he calls you you cant refuse When you aint got nothing you got nothing to lose Youre invisible now youve got no secrets to conceal How does it feel ah how does it feel To be on your own with no direction home Like a complete unknown like a rolling stone ' ,
' Sittin in the mornin sun Ill be sittin when the evenin comes Watching the ships roll in Then I watch em roll away again yeah Im sittin on the dock of the bay Watchin the tide roll away ooh Im just sittin on the dock of the bay Wastin time I left my home in Georgia Headed for the Frisco Bay Cause Ive had nothin to live for It look like nothins gonna come my way So Im just gon sittin on the dock of the bay Watchin the tide roll away ooh Im sittin on the dock of the bay wastin time Look like nothins gonna change Everything still remains the same I cant do what ten people tell me to do So I guess Ill remain the same yes Sittin here restin my bones And this loneliness wont leave me alone listen Two thousand miles I roam Just to make this dock my home Now Im just gon sit at the dock of the bay Watchin the tide roll away ooh yeah Sittin on the dock of the bay Wastin time ' ,
' There is a house way down in New Orleans They call the Rising Sun And its been the ruin of many a poor boy And God I know Im one Mother was a tailor yeah yeah Sewed my Levi jeans My father was a gamblin man yeah yeah Down way down in New Orleans Now the only thing a gamblin man ever needs Is a suitcase Lord and a trunk And the only time a fool like him is satisfied Is when hes all stone cold drunk ' ,
' One two three oclock four oclock rock Five six seven oclock eight oclock rock Nine ten eleven oclock twelve oclock rock Were gonna rock around the clock tonight Put your glad rags on and join me hon Well have some fun when the clock strikes one Were gonna rock around the clock tonight Were gonna rock rock rock til broad daylight Were gonna rock gonna rock around the clock tonight When the clock strikes two three and four If the band slows down well yell for more Were gonna rock around the clock tonight Were gonna rock rock rock til broad daylight Were gonna rock gonna rock around the clock tonight When the chimes ring five six and seven Well be right in seventh heaven Were gonna rock around the clock tonight Were gonna rock rock rock til broad daylight Were gonna rock gonna rock around the clock tonight When its eight nine ten eleven too Ill be goin strong and so will you Were gonna rock around the clock tonight Were gonna rock rock rock til broad daylight Were gonna rock gonna rock around the clock tonight When the clock strikes twelve well cool off then Start a rockin round the clock again Were gonna rock around the clock tonight Were gonna rock rock rock til broad daylight Were gonna rock gonna rock around the clock tonight ' ,
' Oh the shark babe has such teeth dear And it shows them pearly white Just a jackknife has old MacHeath babe And he keeps it ah out of sight You know when that shark bites with his teeth babe Scarlet billows start to spread Fancy gloves oh wears old MacHeath babe So theres never never a trace of red Now on the sidewalk huh huh whoo sunny morning un huh Lies a body just oozin life eek And someones sneakin round the corner Could that someone be Mack the Knife Theres a tugboat huh huh down by the river dontcha know Where a cement bags just adrooppin on down Oh that cement is just its there for the weight dear Fivell get ya ten old Mackys back in town Now did ya hear bout Louie Miller He disappeared babe After drawin out all his hardearned cash And now MacHeath spends just like a sailor Could it be our boys done somethin rash Now Jenny Diver ho ho yeah Sukey Tawdry Ooh Miss Lotte Lenya and old Lucy Brown Oh the line forms on the right babe Now that Mackys back in town I said Jenny Diver whoa Sukey Tawdry Look out to Miss Lotte Lenya and old Lucy Brown Yes that line forms on the right babe Now that Mackys back in town Look out old Mackys back ' ,
' Well since my baby left me Well I found a new place to dwell Well its down at the end of Lonely Street At Heartbreak Hotel Where Ill be Ill be so lonely baby Well Im so lonely Ill be so lonely I could die Although its always crowded You still can find some room For broken hearted lovers To cry there in their gloom Be so theyll be so lonely baby They get so lonely Theyre so lonely they could die Now the bellhops tears keep flowin And the desk clerks dressed in black Well theyve been so long on Lonely Street Well theyll never theyll never look back And they get so they get so lonely baby Well they are so lonely Theyre so lonely they could die Well now if your baby leaves you And you got a tale to tell Well just take a walk down Lonely Street To Heartbreak Hotel Where you will be you will be lonely baby Well you will be lonely Youll be so lonely you could die Although its always crowded But you still can find some room For broken hearted lovers To cry there in their gloom Where they get so they get so lonely baby Well theyre so lonely Theyll be so lonely they could die ' ,
' You aint nothin but a hound dog Cryin all the time You aint nothin but a hound dog Cryin all the time Well you aint never caught a rabbit And you aint no friend of mine Well they said you was highclassed Well that was just a lie Yeah they said you was highclassed Well that was just a lie Yeah you aint never caught a rabbit And you aint no friend of mine You aint nothin but a hound dog Cryin all the time You aint nothin but a hound dog Cryin all the time Well you aint never caught a rabbit And you aint no friend of mine Well they said you was highclassed Well that was just a lie Yeah they said you was highclassed Well that was just a lie Well you aint never caught a rabbit And you aint no friend of mine Well they said you was highclassed Well that was just a lie Ya know they said you was highclassed Well that was just a lie Well you aint never caught a rabbit And you aint no friend of mine You aint nothin but a hound dog Cryin all the time You aint nothin but a hound dog Cryin all the time Well you aint never caught a rabbit You aint no friend of mine You aint nothin but a hound dog ' ,
' You know I can be found sittin home all alone If you cant come around a least please telephone Dont be cruel to a heart thats true Baby if I made you mad for somethin I might have said Please lets forget the past the future looks bright ahead Dont be cruel I got a heart so true I dont want no other love honey its just you Im thinkin of Lets walk up to the preacher and let us say I do Then you gonna have me baby I got a little bitty your love too And dont dont dont dont be cruel I dont want no other love honey its just you Im thinkin of Hey dont stop thinkin about me and dont make me feel this way Come on over here and love me you know what I want you to say Dont be cruel to a heart thats true Well I dont want no other love honey its just you Im thinkin of Dont be cruel to a heart thats true dont be cruel to a heart thats true Why should we be apart I really love you baby cross my heart ' ,
' The warden threw a party in the county jail The prison band was there and they began to wail The band was jumpin and the joint began to swing You shouldve heard those knocked out jailbirds sing Lets rock Everybody lets rock Everybody in the whole cell block Was dancin to the Jailhouse Rock Spider Murphy played the tenor saxophone Little Joe was blowin on the slide trombone The drummer boy from Illinois went crash boom bang The whole rhythm section was a purple gang Lets rock Everybody lets rock Everybody in the whole cell block Was dancin to the Jailhouse Rock Number 47 said to number three Youre the cutest jailbird I ever did see I sure would be delighted with your company Come on and do the Jailhouse Rock with me Lets rock Everybody lets rock Everybody in the whole cell block Was dancin to the Jailhouse Rock Rock Rock Sad Sack was sittin on a block of stone Way over in the corner weepin all alone The warden said Hey buddy dont you be no square If you cant find a partner use a wooden chair Lets rock Everybody lets rock Everybody in the whole cell block Was dancin to the Jailhouse Rock Shifty Henry said to Bugs For Heavens sake No ones lookin nows the chance to make a break Bugsy turned to Shifty and he said Nix nix I wanna stick around a while and get my kicks Lets rock Everybody lets rock Everybody in the whole cell block Was dancin to the Jailhouse Rock Dancin to the Jailhouse Rock dancin to the Jailhouse Rock Dancin to the Jailhouse Rock dancin to the Jailhouse Rock Dancin to the Jailhouse Rock ' ,
' Deep down in Louisiana close to New Orleans Way back up in the woods among the evergreens There stood a log cabin made of earth and wood Where lived a country boy named Johnny B Goode Who never ever learned to read or write so well But he could play a guitar just like aringin a bell Go go Go Johnny go go Go Johnny go go Go Johnny go go Go Johnny go go Johnny B Goode He used to carry his guitar in a gunny sack Go sit beneath the tree by the railroad track Oh the engineers would see him sitting in the shade Strumming with the rhythm that the drivers made The people passing by they would stop and say Oh my what that little country boy could play Go go Go Johnny go go Go Johnny go go Go Johnny go go Go Johnny go go Johnny B Goode His mother told him someday you will be a man And you will be the leader of a big old band Many people coming from miles around To hear you play your music when the sun go down Maybe someday your name will be in lights Saying Johnny B Goode tonight Go go Go Johnny go Go go go Johnny go Go go go Johnny go Go go go Johnny go Go Johnny B Goode ' ,
' I was dancing with my darling to the Tennessee Waltz When an old friend I happened to see I Introduced her to my loved one and while they were dancing My friend stole my sweetheart from me  I remember the night and the Tennessee Waltz Now I know just how much I have lost Yes I lost my little darling on the night they were playing The beautiful Tennessee Waltz  I was dancing with my darling to the Tennessee Waltz When an old friend I happened to see I Introduced her to my loved one and while they were dancing My friend stole my sweetheart from me I remember the night and the Tennessee Waltz Now I know just how much I have lost Yes I lost my little darling on the night they were playing The beautiful Tennessee Waltz ' ,
' Hey mama dont you treat me wrong Come and love your daddy all night long all right now Hey hey All right See the girl with the diamond ring She knows how to shake that thing all right now now Hey hey Hey hey Tell your mama tell your pa Im gonna send you back to Arkansas oh yes mam You dont do right Dont do right Oh play it boy When you see me in misery Come on baby see about me now yeah Hey hey All right See the girl with the red dress on She can do the Birdland all night long yeah yeah Whatd I say All right Well tell me whatd I say Tell me whatd I say right now Tell me whatd I say Tell me whatd I say right now Tell me whatd I say Tell me whatd I say And I wanna know Baby I wanna know right now And I wanna know Baby I wanna know right now yeah And I wanna know Baby I wanna know yeah ' ,
' Dream dream dream dream Dream dream dream dream When I want you in my arms When I want you and all your charms Whenever I want you all I have to do is Dream dream dream dream When I feel blue in the night And I need you to hold me tight Whenever I want you all I have to do is Dream I can make you mine taste your lips of wine Anytime night or day Only trouble is gee whiz Im dreamin my life away I need you so that I could die I love you so and that is why Whenever I want you all I have to do is Dream dream dream dream Dream I can make you mine taste your lips of wine Anytime night or day Only trouble is gee whiz Im dreamin my life away I need you so that I could die I love you so and that is why Whenever I want you all I have to do is Dream dream dream dream Dream dream dream dream ' ,
' Im dreaming of a white Christmas Just like the ones I used to know Where the tree tops glisten And children listen To hear sleigh bells in the snow oh the snow I said Im dreaming of a white Christmas With every Christmas card I write May your days be merry and bright And may all your Christmas be white Lets go sticks lets go I said Im dreaming of a white oh Christmas Just like the ones I used to know Where the tree tops glisten And the children listen To hear sleigh bells in the snow Im dreaming of a white Christmas With every Christmas card I write May your days may your days may your days Be merry and bright And may all your Christmas be white Come on now woo Jman up up up Im dreaming of a white Christmas With every Christmas card I write May your days be merry and bright And may all your Christmas be white ' ,
' And now the purple dusk of twilight time Steals across the meadows of my heart High up in the sky the little stars climb Always reminding me that were apart You wandered down the lane and far away Leaving me a song that will not die Love is now the stardust of yesterday The music of the years gone by Sometimes I wonder how I spend The lonely night Dreaming of a song The melody haunts my reverie And I am once again with you When our love was new And each kiss an inspiration But that was long ago And now my consolation Is in the stardust of a song Besides the garden wall When stars are bright You are in my arms The nightingale tells his fairytale Of paradise where roses grew Though I dream in vain In my heart it will remain My stardust melody A memory of loves refrain ' ,
' You know Dasher and Dancer and Prancer and Vixen Comet and Cupid and Donner and Blitzen But do you recall The most famous reindeer of all Rudolph the RedNosed Reindeer Had a very shiny nose And if you ever saw it You would even say it glows All of the other reindeer Used to laugh and call him names They never let poor Rudolph Join in any reindeer games Then one foggy Christmas Eve Santa came to say Rudolph with your nose so bright Wont you guide my sleigh tonight Then how the reindeer loved him As they shouted out with glee Rudolph the RedNosed Reindeer Youll go down in history Rudolph the RedNosed Reindeer Had a very shiny nose And if you ever saw it You would even say it glows All of the other reindeer Used to laugh and call him names They never let poor Rudolph Join in any reindeer games Then one foggy Christmas Eve Santa came to say Rudolph with your nose so bright Wont you guide my sleigh tonight Then how the reindeer loved him As they shouted out with glee Rudolph the RedNosed Reindeer Youll go down in history ' ,
' Hi there Tex what you say Step aside partner its my day Bend an ear  listen to my version Of a really solid Tennesse excursion Pardon me boy Is that the Chattanooga choo choo Yes yes track twentynine Boy you can gimme a shine Can you afford To board the Chattanooga choo choo Ive got my fare And just a trifle to spare You leave the Pennsylvania Station bout a quarter to four Read a magazine and then youre in Baltimore Dinner in the diner Nothing could be finer Then to have your ham an eggs in Carolina When you hear the whistle blowin eight to the bar Then you know that Tennessee is not very far Shovel all the coal in Gotta keep it rollin Woo woo Chattanooga there you are Theres gonna be A certain party at the station Satin and lace I used to call funny face Shes gonna cry Until I tell her that Ill never roam So Chattanooga choo choo Wont you choochoo me home Chattanooga Chattanooga Get aboard Chattanooga Chattanooga All Aboard Chattanooga Chattanooga Chattanooga choo choo Wont you choochoo me home Chatanooga Choo Choo ' ,
' Gonna take a sentimental journey Gonna set my heart at ease Gonna make a sentimental journey To renew old memories Got my bag got my reservation Spent each dime I could afford Like a child in wild anticipation I long to hear that all aboard Seven thats the time we leave at seven Ill be waitin up for heaven Countin every mile of railroad track That takes me back Never thought my heart could be so yearning Why did I decide to roam I gotta take this sentimental journey Sentimental journey home Seven thats the time we leave at seven Ill be waitin up for heaven Countin every mile of railroad track That takes me back Never thought my heart could be so yearning Why did I decide to roam I gotta take this sentimental journey Sentimental journey home Sentimental journey home Sentimental journey home ' ,
' Chestnuts roasting on an open fire Jack Frost nipping at your nose Yuletide carols being sung by a choir And folks dressed up like Eskimos Everybody knows a turkey and some mistletoe Help to make the season bright Tiny tots with their eyes all aglow Will find it hard to sleep tonight They know that Santas on his way Hes loaded lots of toys and goodies on his sleigh And every mothers child is gonna spy To see if reindeers really know how to fly And so Im offering this simple phrase To kids from one to ninetytwo Although its been said many times many ways Merry Christmas to you And so Im offering this simple phrase To kids from one to ninetytwo Although its been said many times many ways Merry Christmas to you ' ,
' Ill never smile again Until I smile at you Ill never laugh again What good would it do For tears would fill my eyes My heart would realize That our romance is through Ill never love again Im so in love with you Ill never thrill again To somebody new Within my heart I know I will never start To smile again Until I smile at you Within my heart I know I will never start To smile again Until I smile at you ' ,
' When you wish upon a star Makes no difference who you are Anything your heart desires Will come to you If your heart is in your dream No request is too extreme When you wish upon a star As dreamers do Like a bolt out of the blue Fate steps in and sees you through When you wish upon a star Your dreams come true ' ,
' You must take the A train To go to Sugar Hill way up in Harlem If you miss the A train Youll find you missed the quickest way to Harlem Hurry get on now its coming Listen to those rails athrumming All aboard get on the A train Soon you will be on Sugar Hill in Harlem ' ,
' You must remember this A kiss is just a kiss A sigh is just a sigh The fundamental things apply As time goes by And when two lovers woo They still say I love you On that you can rely No matter what the future brings As time goes by Moonlight and love songs Never out of date Hearts full of passion Jealousy and hate Woman needs man and man must have his mate That no one can deny Its still the same old story A fight for love and glory A case of do or die The world will always welcome lovers As time goes by Moonlight and love songs Never out of date Hearts full of passion Jealousy and hate Woman needs man and man must have his mate That no one can deny Its still the same old story A fight for love and glory A case of do or die The world will always welcome lovers As time goes by ' ,
' Somewhere over the rainbow way up high Theres a land that I heard of once in a lullaby Somewhere over the rainbow skies are blue And the dreams that you dare to dream Really do come true Someday Ill wish upon a star And wake up where the clouds are far behind me Where troubles melt like lemon drops Away above the chimney tops Thats where youll find me Somewhere over the rainbow Bluebirds fly Birds fly over the rainbow Why then oh why cant I If happy little bluebirds fly Beyond the rainbow Why oh why cant I ' ,        
' Mister whyd you call up what you doin tonight Hope youre in the mood because Im feeling just right Hows about a corner with a table for two Where the musics mellow and some gay rendezvous Theres no chance romancing with a blue attitude Youve got to do some dancing to get in the mood Sister whyd you call him thats a timely idea Somethings ringing dear it will be good to my ear Everybody must agree that dancing has charm When youre in the circle with your love in your arms Stepping out but you wont be a sweet interlude Oh fill the room without me put me in the mood In the mood thats it I got it In the mood youre in the spot and In the mood what a heartache Feel alive I get the jive you got in that hall Hephephep head like a hepper Peppeppep hard as a pepper Stepstepstep step like a stepper Moggin to hug him were in the mood now Mister whyd you call up all you needed was fun You can see the wonders that this evening has done My feet were so happy til my honey could move Now the light is with us and youre right in the groove You were only hungry for some musical food Youre positively absolutely in the mood Sister whyd you call him Im indebted to you It all goes to show what a new rhythm can do Ive never been so happy and so fully alive It seems that jiving jumping is a powerful job Swingeroo has given me a new attitude My heart is followin the rhythm follow the rhythm Follow the rhythm follow the rhythm Follow the rhythm follow the rhythm Follow the rhythm follow the rhythm Im in the mood yeah ' ,
' Like the beat beat beat of the tomtom When the jungle shadows fall Like the tick ticktock of the stately clock As it stands against the wall Like the beat beat beat of the tomtom When the jungle shadows fall Like the tick ticktock of the stately clock As it stands against the wall Like the drip drip drip of the raindrops When the summer shower is through So a voice within me keeps repeating you you you Night and day you are the one Only you beneath the moon and under the sun Whether near to me or far Its no matter darling where you are I think of you Night and say day and night why is it so That this longing for you follows wherever I go In the roaring traffics boom In the silence of my lonely room I think of you Night and day night and day Under the hide of me Theres an oh such a hungry yearning burning inside of me And its torment wont be through Til you let me spend my life making love to you Day and night night and day This torment would never be through Til you let me spend my life making love to you Day and night night and day Day and night night and day Day and night night and day Day and night day and night Day and night night and day ' ,
' Heaven Im in heaven And my heart beats so that I can hardly speak And I seem to find the happiness I seek When were out together dancing cheek to cheek Yes heaven Im in heaven And the cares that hung around me through the week Seem to vanish like a gamblers lucky streak When were out together dancing cheek to cheek Oh I love to climb to mountain And reach the highest peak But it doesnt thrill me half as much As dancing cheek to cheek Oh I love to go out fishing In a river or a creek But I dont enjoy it half as much As dancing cheek to cheek Now mama dance with me I want my arms about you That charm about you Will carry me through Yes heaven Im in heaven And my heart beats so that I can hardly speak And I seem to find the happiness I seek When were out together dancing cheek to cheek Take it Ella swing it Heaven Im in heaven And my heart beats so that I can hardly speak And I seem to find the happiness I seek When were out together dancing cheek to cheek Heaven Im in heaven And the cares that hung around me through the week Seem to vanish like a gamblers lucky streak When were out together dancing cheek to cheek Oh I love to climb a mountain And reach the highest peak But it doesnt thrill me half as much As dancing cheek to cheek Oh I love to go out fishing In a river or a creek But I dont enjoy it half as much As dancing cheek to cheek Come on and dance with me I want my arms about you That charm about you Will carry me through To heaven Im in heaven And my heart beats so that I can hardly speak And I seem to find the happiness I seek When were out together dancing cheek to cheek Dance with me I want my arms about you That charm about you Will carry me through To heaven heaven Im in heaven Im in heaven And my heart beats so that I can hardly speak And I seem to find the happiness I seek When were out together dancing cheek to cheek Cheek to cheek Cheek to cheek Cheek to cheek ' ,
' When they begin the beguine It brings back the sound of music so tender It brings back a night of tropical splendor It brings back a memory ever green Im with you once more under the stars And down by the shore an orchestras playing And even the palms seem to be swaying When they begin the beguine To live it again is past all endeavor Except when that tune clutches my heart And there we are swearing to love forever And promising never never to part What moments divine what rapture serene Till clouds came along to disperse the joys we had tasted And now when I hear people curse the chance that was wasted I know but too well what they mean So dont let them begin the beguine Let the love that was once a fire remain an ember Let it sleep like the dead desire I only remember When they begin the beguine Oh yes let them begin the beguine make them play Till the stars that were there before return above you Till you whisper to me once more Darling I love you And we suddenly know what heaven were in When they begin the beguine ' ,
' … Dont know why Theres no sun up in the sky Stormy weather Since my man and I aint together Keeps raining all the time … Life is bare Gloom and misery everywhere Stormy weather Just cant get my poor old self together Im weary all the time the time So weary all of the time … When he went away The blues walked in and met me If he stays away old rocking chair will get me All I do is pray The lord above will let me Walk in the sun once more … Cant go on Everything I had is gone Stormy weather Since my man and I aint together Keeps raining all the time Keeps raining all of the time … I walk around Heavyhearted and sad Night comes around And Im still feeling bad Rain pourin down Blinding every hope I had This pitter an patter an beatin an spatterin drivin me mad … Love love love love This misery will be the end of me … When he went away The blues walked in and met me If he stays away old rocking chair will get me All I do is pray The lord above will let me Walk in the sun once more … Cant go on Everything I had is gone Stormy weather Since my man and I aint together Keeps raining all the time the time Keeps raining all the time ' ,
' Someday when Im awfully low When the world is cold I will feel a glow just thinking of you And the way you look tonight Yes youre lovely with your smile so warm And your cheeks so soft There is nothing for me but to love you And the way you look tonight With each word your tenderness grows Tearin my fear apart And that laugh wrinkles your nose Touches my foolish heart Lovely never never change Keep that breathless charm Wont you please arrange it Cause I love you Ajust the way you look tonight And that laugh that wrinkles your nose It touches my foolish heart Lovely dont you ever change Keep that breathless charm Wont you please arrange it Cause I love you Ajust the way you look tonight Mmmm mmmm Just the way you look tonight ' ,
' Silent night holy night All is calm all is bright Round yon Virgin Mother and Child Holy infant so tender and mild Sleep in heavenly peace Sleep in heavenly peace Silent night holy night Shepherds quake at the sight Glories stream from Heaven afar Heavenly hosts sing hallelujah Christ the Savior is born Christ the Savior is born ' ,
' Atisket atasket A brown and yellow basket I send a letter to my mommy On the way I dropped it I dropped it I dropped it Yes on the way I dropped it A little girlie picked it up And put it in her pocket She was truckin on down the avenue But not a single thing to do She went peck peck peckin all around When she spied it on the ground She took it she took it My little yellow basket And if she doesnt bring it back I think that I will die Atisket atasket I lost yellow basket And if that girlie dont return it Dont know what Ill do Oh dear I wonder where my basket can be So do we so do we so do we so do we so do we Oh gee I wish that little girl I could see So do we so do we so do we so do we so do we Oh why was I so careless with that basket of mine That ittybitty basket was a joy of mine Atisket atasket I lost my yellow basket Wont someone help me find my basket And make me happy again again no no no no Was it red no no no no Was it blue no no no no Just a little yellow basket A little yellow basket ' ,
' Time and again Ive longed for adventure Something to make my heart beat the faster What did I long for I never really knew Finding your love Ive found my adventure Touching your hand my heart beats the faster All that I want in all of this world is you You are the promised kiss of springtime That makes the lonely winter seem long You are the breathless hush of evening That trembles on the brink of a lovely song You are the angel glow that lights a star The dearest things I know are what you are Some day my happy arms will hold you And some day Ill know that moment divine When all the things you are are mine ' ,
' I hate to see the evening sun go down I hate to see the evening sun go down It makes me think Im on my last go round Feeling tomorrow like I feel today Feeling tomorrow like I feel today Ill pack my dreams and make my get away Saint Louis woman with her diamond rings Pulls dat man around by her apron strings Powder for powder and this storebought hair The man I love wouldnt gone nowhere nowhere I got the Saint Louis Blues just as blue as I can be Hes got a heart like rock I cast in the sea Or else he wouldnt have gone so far from me ' ,
' Ive been away from you a long time I never thought Id miss you so Somehow I feel Your love is real Near you I want to be The birds are singing it is song time The banjos strumming soft and low I know that you Yearn for me too Swannee youre calling me Swanee how I love you how I love you My dear old Swanee I give the world to be Among the folks in DIXI Even though my mammys Waiting for me Praying for me Down by the Swanee The folks up north will see me no more When I get to that Swanee shore I miss the old folks at home Swanee how I love you how I love you My dear old Swanee I give the world to be Among the folks in DIXI Even though my mammys Waiting for me Praying for me Down by the Swanee The folks up north will see me no more When I get to that Swanee shore ' ,
' Two sides twist and then collide Youre calling off the guards Am I coming Im coming through Am I coming Adulteress conditioned to a spin cycled submission You know sometimes it just feels better to give in Sometimes it just feels better to give in And its all too familiar And it happens all the time All the cards begin to stack up Twisting heartache into fine Little pieces that avoid an awful crime But its you I cant deny You I cant deny Dull heat rises from the sheets Im both a patient boy Well and a jealous man Am I coming But double standard of suspicion Is remedied oh my blue heaven Sometimes it just feels better to give in Sometimes it just feels better to give in And its all too familiar And it happens all the time All the cards begin to stack up Twisting heartache into fine Little pieces that avoid an awful crime But its you I cant deny You I cant deny We swing and we sway As this tiny voice in My head starts to sing Youre safe child you are safe Youre safe child you are safe Youre safe child you are safe We swing and we sway As this tiny voice in My head starts to sing Youre safe child you are safe Youre safe child you are Safe safe safe safe You are safe We swing and we sway As this tiny voice in My head starts to sing Youre safe child you are safe Am I coming Youre safe child you are safe Am I  Coming through Is this all too familiar Does it happen all the time Im just asking you to hear me Could you please just once just hear me More then anything you wanted to be right Still its you you its you I cant deny You I cant deny Its you I cant deny ' ,
' No one to talk with All by myself No one to walk with But Im happy on the shelf Aint misbehavin Im savin my love for you I know for certain The one I love Im through with flirtin Its just you Im thinkin of Aint misbehavin Im savin my love for you Like Jack Horner In the corner Dont go nowhere What do I care Your kisses are worth waitin for Believe me I dont stay out late Dont care to go Im home about eight Just me and my radio Aint misbehavin Im savin my love for you Like Jack Horner In the corner Dont go nowhere What do I care Your kisses are worth waitin for Believe me I dont stay out late Dont care to go Im home about eight Just me and my radio Aint misbehavin Im savin my love for you ' ,
' Whispering Hear the ghosts in the moonlight Sorrow doing a new dance Through their bone through their skin Listening To the souls in the fools night Fumbling mutely with their rude hands And theres heartache without end See the father bent in grief The mother dressed in mourning Sister crumbles And the neighbors grumble The preacher issues warnings History Little Miss didnt do right Went and ruined all the true plans Such a shame such a sin Mystery Home alone on a school night Harvest moon over the blue land Summer longing on the wind Had a sweetheart on his knees So faithful and adoring And he touched me And I let him love me So let that be my story Listening For the hope for the new life Something beautiful a new chance Hear its whispering There again ' ,
' Life is not a highway strewn with flowers Still it holds a goodly share of bliss When the sun gives way to April showers Here is the point you should never miss  Though April showers may come your way They bring the flowers that bloom in May So if its raining have no regrets Because it isnt raining rain you know Its raining violets And where you see clouds upon the hills You soon will see crowds of daffodils So keep on looking for a blue bird And listning for his song Whenever April showers come along And where you see clouds upon the hills You soon will see crowds of daffodils So keep on looking for a blue bird And listning for his song Whenever April showers come along ' ,
' Picture you upon my knee Just tea for two and two for tea Just me for you And you for me alone Nobody near us To see us or hear us No friends or relations On weekend vacations We wont have it known dear That we own a telephone dear Day will break and youll awake And start to bake a sugar cake For me to take For all the boys to see We will raise a family A boy for you a girl for me Oh cant you see How happy we would be ' ,
' Oh I wish I had someone to love me Someone to call me their own Oh I wish I had someone to live with Cause Im tired of livin alone Oh please meet me tonight in the moonlight Please meet me tonight all alone For I have a sad story to tell you Its a story thats never been told Ill be carried to the new jail tomorrow Leaving my poor darling all alone With the cold prison bars all around me And my head on a pillow of stone Now I have a grand ship on the ocean All mounted with silver and gold And before my poor darlin would suffer Oh that ship would be anchored and sold Now if I had wings like an angel Over these prison walls I would fly And Id fly to the arms of my poor darlin And there Id be willing to die ' ,
' Oh sweet Dardanella I love your harem eyes Im a lucky fellow to capture such a prize Oh Allah knows my love for you And he tells you to be true Dardanella Oh hear my sigh my Oriental Oh sweet Dardanella prepare the wedding wine Therell be one girl in my harem when youre mine Well build a tent Just like the children of the Orient Oh sweet Dardanella My star of love divine Down beside the Dardanella Bay Where Oriental breezes play There lives a lonesome maid Armenian By the Dardanelles with glowing eyes She looks across the seas and sighs And weaves her love spell so sirenian Soon I shall return to Turkestan I will ask for her heart and hand Oh sweet Dardanella I love your harem eyes Im a lucky fellow to capture such a prize Oh Allah knows my love for you And he tells you to be true Dardanella Oh hear my sigh my Oriental Oh sweet Dardanella prepare the wedding wine Therell be one girl in my harem when youre mine Well build a tent Just like the children of the Orient ' ,
' Why do I do just as you say Why must I just give you your way Why do I sigh why dont I try to forget It must have been that something lovers call fate Kept me saying I have to wait I saw them all just couldnt fall til we met It had to be you It had to be you I wandered around and I finally found The somebody who Could make me be true And could make me be blue And even be glad Just to be sad  thinking of you Some others Ive seen Might never be mean Might never be cross or try to be boss But they wouldnt do For nobody else gave me a thrill With all your faults I love you still It had to be you Wonderful you It had to be you For nobody else gave me a thrill With all your faults I love you still It had to be you Wonderful you It had to be you ' ,
' Come on and hear come on and hear Alexanders Ragtime Band Come on and hear come on and hear Its the best band in the land They can play a bugle call Like you never heard before So natural that you want to go to war Thats just the bestest band what am Honey Lamb Come on along come on along Let me take you by the hand Up to the man up to the man Whos the leader of the band And if you want to hear the Swanee River played in ragtime Come on and hear come on and hear Alexanders Ragtime Band ' ,
' Johnnie get your gun Get your gun get your gun Take it on the run On the run on the run Hear them calling you and me Every son of liberty Hurry right away No delay go today Make your daddy glad To have had such a lad Tell your sweetheart not to pine To be proud her boys in line Over there over there Send the word send the word over there That the Yanks are coming The Yanks are coming The drums rum tumming everywhere So prepare say a prayer Send the word send the word to beware Well be over were coming over And we wont come back till its over over there Johnnie get your gun Get your gun get your gun Johnnie show the Hun Whos a son of a gun Hoist the flag and let her fly Yankee Doodle do or die Pack your little kit Show your grit do your bit Yankee to the ranks From the towns and the tanks Make your mother proud of you And the old red white and blue Over there over there Send the word send the word over there That the Yanks are coming The Yanks are coming The drums rum tumming everywhere So prepare say a prayer Send the word send the word to beware Well be over were coming over And we wont come back till its over over there ' ,
' Let me call you sweetheart Im in love with you Let me hear you whisper That you love me too Keep the love light glowing In your eyes so true Let me call you sweetheart Im in love with you Keep the love light glowing In your eyes so true Let me call you sweetheart Im in love with you ' ,
' You made me love you I didnt want to do it I didnt want to do it You made me want you And all the time you knew it I guess you always knew it You made me happy sometimes Sometimes you made me glad But there were times dear You made me feel so bad You made me sigh for I didnt wanna tell you I didnt want to tell you I want some lovin thats true Yes I do indeed I do you know I do Give me give me give me What I cry for You know ya got the brand o kisses That Id die for You know you made me love you You made me sigh for I didnt want to tell you I didnt wanna tell you I want some lovin thats true Yes I do indeed I do you know I do Give me give me give me What I cry for You know ya got the brand o kisses That Id die for You know you made me love you ' ,
' By the light of the silvery moon I want to spoon To my honey Ill croon loves tune Honey moon keep ashinin in June Your silvery beams will bring loves dreams Well be cuddlin soon By the silvery moon Place park scene dark Silvery moon is shining through the trees Cast two me you Summer kisses floating on the breeze Act one be done Dialog where would ya like to spoon My cue with you Underneath the silvery moon By the light of the silvery moon I wanna spoon To my honey Ill croon loves tune Honey moon keep ashinin in June Your silvery beams will bring loves dreams Well be cuddlin soon By the silvery moon Act two Scene new Roses blooming all around the place Cast three You me Preacher with a solemnlooking face Sings bell rings Preacher you are wed forever more Act two all though Every night the same encore By the light not the dark but the light Of the silvery moon not the sun but the moon I wanna spoon not croon but spoon To my honey Ill croon loves tune Honeymoon honeymoon honeymoon Keep ashinin in June Your silvery beams will bring loves dreams Well be cuddlin soon By the silvery moon The silvery moon ' ,
' We were strolling along Twist and shout On moonlight bay ooh We could hear the voices singing I like it And they seemed to say Keep on Bongo You have borken my heart Oh twist and shout So go away With you big far hairy legs On Moonlight Bay On Moonlight Bay Ooohhh Yeah Ha ha ' ,
' Hold that tiger Hold that tiger Hold that tiger Hold that tiger Hold that tiger Hold that tiger Hold that tiger Wheres that tiger Wheres that tiger Wheres that tiger Wheres that tiger Wheres that tiger Wheres that tiger Wheres that tiger ' ,
' Verse 1 Some of these days Youre gonna miss me honey Some of these days Youre gonna feel so lonely  Youll miss my huggin Gonna miss my kissin Gonna miss me honey When Im away Youll feel so lonely Just want me only But you know honey You had your way  And when you leave me You know itll grieve me Gonna miss your little mama mama mama Some of these days  Scatting  Verse 2 Some of these days Youre gonna miss me honey Some of these days Youre gonna feel so lonely  Youll miss my huggin Gonna miss my kissin Gonna miss me honey When Im away  I feel so lonely For you only But you know honey You had your way You might also like Baby face NURIK SMIT RM  들꽃놀이 Wild Flower ft youjeen English Translation Genius English Translations 10М ОТ ДОМА LOVV66 And when you leave me Gonna grieve me  Outro Youre gonna miss your baby some of these days Youre gonna miss me in a thousand ways Hey daddy remember what I say Some of these days I say when you leave me Gonna grieve me Remember when youre all alone on the shelf Aint got nobody but yourself Cant drink those Bloody Marys by yourself Ah ah I say tell me you leave me I know I know its gonna grieve me Baby some of these days ' ,
' Now wont you listen honey while I say How could you tell me that youre goin away Dont say that we must part Dont break your babys heart You know Ive loved you for these many years Love you night and day Oh honey baby cant you see my tears Listen while I say After youve gone and left me cryin After youve gone theres no denyin Youll feel blue youll feel sad Youll miss the dearest pal youve ever had Therell come a time now dont forget it Therell come a time when youll regret it Oh babe think think what are you doing You know my love for you will drive me to ruin After youve gone after youve gone away After youve gone and left me cryin After youve gone theres no denyin You feel blue you feel sad And youll miss the only pal you ever had Therell come a time now dont forget it Therell come a time when youll regret it Oh babe think think what are you doing You know my love for you will drive me to ruin After youve gone after youve gone away ' ,
' Rock a bye your baby with a dixie melody When you croon croon a tune from the heart of dixie Just hang my cradle mammy mine right on that masoned dixen line And swing it from virginia to tennese with all the love thats in ya Weep no more my lady sing that song again for me Sing on black joe just as though you have me on your knees A Million baby kisses ill deliver if you will only play that swanee river Rock a bye your rock a bye baby with a dixie melody OHWeep no more my lady sing that song again for me Sing on black joe just as though you have me on your knees A Million baby kisses ill deliver if you will only play that swanee river Rock a bye your rock a bye baby with a dixie melody ' ,
' Katie Casey was baseball mad Had the fever and had it bad Just to root for the home town crew Evry sou1 Katie blew On a Saturday her young beau Called to see if shed like to go To see a show but Miss Kate said No Ill tell you what you can do  Chorus  Take me out to the ball game Take me out with the crowd Buy me some peanuts and Cracker Jack I dont care if I never get back Let me root root root for the home team If they dont win its a shame For its one two three strikes youre out At the old ball game  Katie Casey saw all the games Knew the players by their first names Told the umpire he was wrong All along Good and strong When the score was just two to two Katie Casey knew what to do Just to cheer up the boys she knew She made the gang sing this song ' ,
' Theres a feeling comes astealing And it sets my brain areeling When Im listning to the music of a military band Any tune like Yankee Doodle Simply sets me off my noodle Its that patriotic something that no one can understand  Way down South in the land of cotton Melody untiring Aint that inspiring  Hurrah Hurrah Well join the jubilee And thats going some for the Yankees by gum Red White and Blue I am for you Honest youre a grand old flag Youre a grand old flag Youre a highflying flag And forever in peace may you wave Youre the emblem of the land I love The home of the free and the brave Evry heart beats true Neath the Red White and Blue Where theres never a boast or brag But should auld acquaintance be forgot Keep your eye on the grand old flag Im no cranky hanky panky Im a dead square honest Yankee And Im mighty proud of that old flag that flies for Uncle Sam Though I dont believe in raving Evry time I see it waving Theres a chill runs up my back that makes me glad Im what I am  Heres a land with a million soldiers Thats if we should need em Well fight for freedom  Hurrah Hurrah For evry Yankee Tar And old GAR evry stripe evry star Red White and Blue hats off to you Honest youre a grand old flag ' ,    
' Sweet Adeline  In the evening when I sit alone adreaming Of days gone by love to me so dear Theres a picture that in fancy oft appearing Brings back the time love when you were near It is then I wonder where you are my darling And if your heart to me is still the same For the sighing wind and nightingale asinging Are breathing only your own sweet name  cho Sweet Adeline My Adeline      My Adeline My Adeline      At night dear heart At night dear heart      For you I pine For you I pine      In all my dreams In all my dreams      Your fair face beams Your fair face beams      Youre the flower of my heart      Sweet Adeline My Adeline  I can see your smiling face as when we wandered Down by the brookside just you and I And it seems so real at times til I awaken To find all vanished a dream gone by If we must meet sometime in after years my darling I trust that I will find your love still mine Though my heart is sad and clouds above are hovring The sun again love for me would shine ' ,
' Im the kid thats all the candy Im a Yankee Doodle Dandy Im glad I am Sos Uncle Sam Im a real live Yankee Doodle Made my name and fame and boodle Just like Mister Doodle did by riding on a pony I love to listen to the Dixey Dixie strain I long to see the girl I left behind me And that aint a josh Shes a Yankee by gosh Oh say can you see Anything about a Yankee thats a phoney Im a Yankee Doodle Dandy A Yankee Doodle do or die A real live nephew of my Uncle Sam Born on the Fourth of July Ive got a Yankee Doodle sweetheart Shes my Yankee Doodle joy Yankee Doodle came to London Just to ride the ponies I am the Yankee Doodle Boy  Fathers name was Hezikiah Mothers name was Ann Maria Yanks through and through Red white and blue Father was so Yankee hearted When the Spanish War was started He slipped upon his uniform and hopped up on a pony My mothers mother was a Yankee true My fathers father was a Yankee too And thats going some For the Yankees by gum Oh say can you see Anything about my pedigree thats phoney  Im a Yankee Doodle Dandy A Yankee Doodle do or die A real live nephew of my Uncle Sam Born on the Fourth of July Ive got a Yankee Doodle sweetheart Shes my Yankee Doodle joy Yankee Doodle came to London Just to ride the ponies I am the Yankee Doodle Boy ' ,
' One one summers day Sun was shinin fine The lady love of old Bill Bailey Was hangin clothes on the line In her back yard And weepin hard She married a BO brakeman That took and throwed her down Bellerin like a prunefed calf With a big gang hanging round And to that crowd She hollered loud … Wont you come home Bill Bailey Wont you come home She moans the whole day long Ill do the cookin darling Ill pay the rent I know Ive done you wrong member that rainy eve that I threw you out With nothing but a finetooth comb I know Im to blame Well aint that a shame Bill Bailey wont you please come home … Bill drove by that door In an automobile A great big diamond coach and footman Hear that lady squeal Hes all alone I heard her groan She hollered through the door Bill Bailey is you sore Stop a minute listen to me Wont I see you no more Bill winks his eye As he heard her cry … Wont you come home Bill Bailey Wont you come home She moans the whole day long Ill do the cookin darling Ill pay the rent I know Ive done you wrong member that rainy eve that I threw you out With nothing but a finetooth comb I know Im to blame Well aint that a shame Bill Bailey wont you please come home ' ,
' Did you ever see two Yankees part upon a foreign shore When the good ships just about to start for Old New York once more With tear dimmed eye they say goodbye Theyre friends without a doubt When the man on the pier shouts Let them clear As the ship strikes out Give my regards to Broadway Remember me to Herald Square Tell all the gang at Forty Second Street That I will soon be there Whisper of how Im yearning To mingle with the old time throng Give my regards to Old Broadway And say that Ill be there ere long Give my regards to Broadway Remember me to Herald Square Tell all the gang at Forty Second Street That I will soon be there Whisper of how Im yearning To mingle with the old time throng Give my regards to Old Broadway And say that Ill be there ere long ' ,
' Snow time aint no time to stay outdoors and spoon So shine on shine on harvest moon for me n my gal The night was mighty dark so you could hardly see For the moon refused to shine Couples sitting underneath a willow tree For love they pine The little maid was kinda fraid of darkness So she said I guess Ill go Boy began to sigh looked up at the sky Told the moon his little tale of woe Oh shine on shine on harvest moon up in the sky I aint had no lovin since April January June or July Snow time aint no time to stay outdoors and spoon So shine on shine on harvest moon for me n my gal Oh shine on shine on harvest moon way up in the sky I aint had no lovin since April January June or July Snow time aint no time to stay outdoors and spoon So shine on shine on harvest moon for me n my gal ' ,
' In the good old summertime In the good old summertime Strollin through the shady lanes With my baby mine I hold her hand and she holds mine And thats a very good sign That shes my tootsywootsy in A good old summertime In the good old summertime In the good old summertime If I could go Strollin down a shady lane With my baby mine I hold her hand And he holds mine And thats a very good sign That shes your tootsywootsy In the good old summertime Down shady lane In the good old summertime With baby mine In the good old summer time ' ,
' When Louis came home to the flat He hung up his coat and his hat He gazed all around But no wifey he found So he said Where can Flossy be at A note on the table he spied He read it just once then he cried It read Louis dear its toos low for me here So I think I will go for a ride Oh Meet me in St Louis Louis Meet me at the fair Dont tell me the lights are shining Any place but there We will dance the hoochie koochie I will be your tootsie wootsie If you will meet me in st Louis Louis Meet me at the fair Meet me in st Louis Louis Meet me at the fair Dont tell me the lights are shining Any place but there We will dance the hoochie koochie I will be your tootsie wootsie If you will meet me in St Louis Louis Meet me at the fair ' ,
' Nothing to do Nellie Darling Nothing to do you say Lets take a trip on memorys ship Back to the by gone days Sail to the old village school house Anchor outside the school door Look in and see theres you and theres me A couple of kids once more School days school days dear old golden rule days Readin and ritin and rithmetic Taught to the tune of a hickry stick You were my queen in calico I was your bashful barefoot beau And you wrote on my slate I love you Joe When we were a couple of kids Member the hill Nellie Darling And the oak tree that grew on its brow Theyve built forty stories upon that old hill And the oaks an old chestnut now Member the meadows so green dear So fragrant with clover and maize Into new city lots and preferred busness plots Theyve cut them up since those days School days school days dear old golden rule days Readin and ritin and rithmetic Taught to the tune of a hickry stick You were my queen in calico I was your bashful barefoot beau And you wrote on my slate I love you Joe When we were a couple of kids ' , 
' A little maiden climbed an old mans knee Begged for a story—Do Uncle please Why are you single why live alone Have you no babies have you no home I had a sweetheart years years ago Where she is now pet you will soon know List to my story Ill tell it all I found her faithless after the ball After the ball is over After the break of morn— After the dancers leaving After the stars are gone Many a heart is aching If you could read them all Many the hopes that have vanished After the ball Bright lights were flashing in the grand ballroom Softly the music playing sweet tunes There came my sweetheart my love my own— I wish some water leave me alone When I returned dear there stood a man Kissing my sweetheart as lovers can Down fell the glass dear broken thats all Just as my heart was after the ball Long years have passed child Ive never wed True to my lost love though she is dead She tried to tell me tried to explain I would not listen pleadings were vain One day a letter came from that man He was her brother—the letter ran Thats why Im lonely no home at all I broke her heart dear after the ball  ' ,
' song Hello Ma Baby sung by Arthur Collins Hello hello people hello Please dont put me off thatta way Hello hello I said hello Ise got a little baby but shes outta sight I talk to her across the telephone Ise never seen my honey but shes mine alright So take my tip and leave this girl alone Evry single morning you will hear me yell Hey Central fix me up along the line He connects me with my honey then I rings the bell And this is what I say to baby mine Hello ma baby Hello ma honey Hello ma ragtime gal Send me a kiss by wire Ya hear me Baby my hearts on fire If you refuse me honey youll lose me Then youll be left alone Oh baby telephone and tell me Ise your own Hello hello baby hello I guess you dont hear me The wires must be poor somewhere Hello hello I said hello This mornin through the phone she said her name was Bess And now I kind of know where I am at Ise satisfied because Ive got my babes address Here pasted in the linin of my hat I am mighty scared that if the wires get crossed Twill separate me from my baby mine Then some other fool will win her and the game is lost And so each day I shout along the line Hello ma baby Hello ma honey Hello ma ragtime gal Send me a kiss by wire Ya hear me Baby my hearts on fire If you refuse me honey youll lose me Then youll be left alone Oh baby telephone and tell me Ise your own  ' ,
' Im dreaming now of Hallie sweet Hallie sweet Hallie Im dreaming now of Hallie for the thought of her is one that never dies Shes sleeping in the valley the valley the valley Shes sleeping in the valley and the mockingbird shinging where she lies Listen to the mockingbird listen to the mockingbird The mockingbird is singing oer her grave Listen to the mockingbird listen to the mockingbird Still singing where the weeping willows wave Ah well I yet can remember I remember I remember Ah well I yet can remember when we gathered in the cotton side by side Twas in the mild midSeptember in September in September Twas in the mild midSeptember and the mockingbird was singing far and wide When charms of spring are awaken are awaken are awaken When charms of spring are awaken and the mockingbird is singing on the bough I feel like one so forsaken so forsaken so forsaken I feel like one so forsaken since my Hallie is no longer with me now  ' ,
' God of my youth I remember Your call on my life took me oer Your love has seen me through all my days I stand here by Your grace On this altar Ive written my life Tells of a story I have with You my Lord I want the world to know God of my forever and forever Im with You My life is saved with a price Your sacrifice redeemed my soul God of my forever and forever I will sing My greatest honour will always be To serve my Lord and King God of my all Ive surrendered My heart finds rest in Your Word Praises will not be enough to show How my love for You has grown Nothing matters when Youre here with me In the end just to hear You say Well done Bowing before Your throne Forever and ever Jesus You alone in glory reign Forever and ever With You I walk this narrow way  ' ,
' Come along get ready wear your grand brandnew gown For theres going to be a meeting in this good good old town When you know everybody and they all know you And you get a rabbits foot to keep away them hoodoos When you hear the preachin has begin Bend down low for to drive away your sin When you get religion youll wanna shout and sing Therell be a hot time in old town tonight My baby when you hear them bells go dingaling All turn around and sweetly you must sing When the birds dance too and the poets will all join in Therell be a hot time in old town tonight Therell be girls for everybody in this good good old town Theres Miss Gonzola Davis and Miss Gondoola Brown Theres Miss Henrietta Caesar and shes all dressed in red I just hug and kiss her and to me then she said Please oh please oh do not let me fall You are mine and I love you best of all You be my man Ill have no man at all Therell be a hot time in old town tonight My baby when you hear them bells go dingaling All join around and sweetly you must sing When the birds dance too and the poets will all join in Therell be a hot time in old town tonight  ' ,
' Oh beautiful for heroes proved In liberating strife Who more than self their country loved And mercy more than life America America may God thy gold refine Til all success be nobleness And every gain divined And you know when I was in school We used to sing it something like this listen here Oh beautiful for spacious skies For amber waves of grain For purple mountain majesties Above the fruited plain But now wait a minute Im talking about America sweet America You know God done shed his grace on thee He crowned thy good yes he did in brotherhood From sea to shining sea You know I wish I had somebody to help me sing this America America God shed his grace on thee America I love you America you see My God he done shed his grace on thee And you oughta love him for it Cause he he he he crowned thy good He told me he would with brotherhood From sea to shining Sea Oh Lord oh Lord I thank you Lord  ' ,
' A smart and stylish girl you see Belle of good society Not too strict but rather free Yet as right as right can be Never forward never bold Not too hot and not too cold But the very thing Im told That in your arms youd like to hold Tarara Boomdeay Tarara Boomdeay Tarara Boomdeay Tarara Boomdeay Tarara Boomdeay Tarara Boomdeay Tarara Boomdeay Tarara Boomdeay Im not extravagantly shy And when a nice young man is nigh For his heart I have a try And faint away with tearful cry When the good young man in haste Will support me round the waist I dont come to while thus embraced Till of my lips he steals a taste Im a timid flowr of innocence Pa says that I have no sense Im one eternal big expense But men say that Im just immense Ere my verses I conclude Id like it known and understood Tho free as air Im never rude Im not too bad and not too good You should see me out with Pa Prim and most particular The young men say Ah there you are And Pa says Thats peculiar Its like their cheek I say and so Off again with Pa I go Hes quite satisfiedalthough When his backs turnedwell you know When with swells Im out to dine All my hunger I resign Tast the food and sip the wine No such daintiness as mine But when I am all alone For shortcomings I atone No old frumps to stare like stone Chops and chicken on my own Sometimes Pa says with a frown Soon youll have to settle down Have to wear your wedding gown Be the strictest wife in town Well it must come byandby When wed to keep quiet Ill try But till then I shall not sigh I shall still go in for my  ' ,
' I came from ole Virginy from the county Acomac I have no wealth to speak of cept de clothes upon my back I can do the country hoedown I can buck and wing to show down And while Im in the notion just step back and watch my motion Oh go way man I can hypnotize dis nation I can shake the earths foundation wit the Maple Leaf Rag Oh go way man just hold you breath a minute For theres not a stunt thats in it with the Maple Leaf Rag I dropped into the swellest ball the great exclusive it But my face was dead agin me and my trousers didnt fit But when Maple Leaf was started my timidity departed I lost my trepidation you could taste the admiration Oh go way man I can hypnotize this nation I can shake the earths foundation wit the Maple Leaf Rag Oh go way man just hold you breath a minute For theres not a stunt thats in it with the Maple Leaf Rag The men were struck wit jealousy the razors gan to flash But de ladies gathered round me for Id surely made a mash The finest belle she sent a boy to call a coach and four We rode around a season till we both were lost to reason Oh go way man I can hypnotize this nation I can shake the earths foundation wit the Maple Leaf Rag Oh go way man just hold you breath a minute For theres not a stunt thats in it with the Maple Leaf Rag  ' ,
' There is a flower within my heart Daisy Daisy Planted one day by a glancing dart Planted by Daisy Bell Whether she loves me or loves me not Sometimes its hard to tell Yet I am longing to share the lot A beautiful Daisy Bell … Daisy Daisy give me your answer do Im half crazy all for the love of you It wont be a stylish marriage I cant afford a carriage But youll look sweet upon the seat Of a bicycle built for two … Daisy Daisy give me your answer do Im half crazy all for the love of you It wont be a stylish marriage I cant afford a carriage But youll look sweet upon the seat Of a bicycle built for two … We will go tandem as man and wife Daisy Daisy Peddling away down the road of life I and my Daisy Bell … When the roads dark we can both despise Policemen and lamps as well There are bright lights in the dazzling eyes Of beautiful Daisy Bell … Daisy Daisy give me your answer do Im half crazy all for the love of you It wont be a stylish marriage I cant afford a carriage But youll look sweet upon the seat Of a bicycle built for two … Daisy Daisy give me your answer do Im half crazy all for the love of you It wont be a stylish marriage I cant afford a carriage But youll look sweet upon the seat Of a bicycle built for two … I will stand by you in weal or woe Daisy Daisy Youll be the bell witch Ill ring youll know Sweet little Daisy Bell … Youll take the lead in each trip we take Then if I dont do well I will permit you to use the brake My beautiful little Daisy Bell … Daisy Daisy give me your answer do Im half crazy all for the love of you It wont be a stylish marriage I cant afford a carriage But youll look sweet upon the seat Of a bicycle built for two … Daisy Daisy give me your answer do Im half crazy all for the love of you It wont be a stylish marriage I cant afford a carriage But youll look sweet upon the seat Of a bicycle built for two  ' ,
' Oh the moonlights fair tonight along the Wabash From the fields there comes the breath of new mown hay Through the sycamore the candle lights are gleaming On the banks of the Wabash far away Oh the moonlights fair tonight along the Wabash From the fields there comes the breath of new mown hay Through the sycamore the candle lights are gleaming On the banks of the Wabash far away Oh the moonlights fair tonight along the Wabash From the fields there comes the breath of new mown hay Through the sycamore the candle lights are gleaming On the banks of the Wabash far away On the banks of the Wabash far away  ' ]

pre_processed_hpop_lyrics = ["""Strumming my pain with his fingers
Singing my life with his words
Killing me softly with his song
Killing me softly with his song
Telling my whole life with his words
Killing me softly with his song
This is Wyclef, Refugee Camp (L-Boogie up in here)
Praswell (Praswell up in here, haha)
Lil' Base sittin' up here on the bass (Refugees up in here)
While I'm on this, I got my girl L (ah, ah)
One time (one time), one time (one time)
Ayo, L, you know you got the lyrics
I heard he sang a good song, I heard he had a style
And so I came to see him, and listen for a while
And there he was, this young boy, stranger to my eyes
Strumming my pain with his fingers (one time, one time)
Singing my life with his words (two times, two times)
Killing me softly with his song
Killing me softly with his song
Telling my whole life with his words
Killing me softly with his song
I felt all flushed with fever, embarrassed by the crowd
I felt he'd found my letters and read each one out loud
I prayed that he would finish, but he just kept right on
Strumming my pain with his fingers (one time, one time)
Singing my life with his words (two times, two times)
Killing me softly with his song
Killing me softly with his song
Telling my whole life with his words
Killing me softly with his song
Yo, L-Boog, take me to the bridge
Whoa
Woah-oah-ah-ah-ah uh, uh
La-la-la, la, la, la
Whoa, la
Whoa, la (ha, ha, ha, ha)
La-ah-ah-ah-ah
Strumming my pain with his fingers (yes, he was singing my life)
Singing my life with his words
Killing me softly with his song
Killing me softly with his song
Telling my whole life with his words (whole life, with his words)
Killing me softly with his song
Yo, put your hands together for L-Boogie (strumming my pain)
From the Refugee Camp (yeah, yeah)
(Singing my life) up in here, you know how we do, L-Boogie up in here
Wyclef, Praswell, said L-Boogie up in here
Wyclef up in here
My man Lil' Base (Praswell up in here)
Jerry one time
T Rocks up in here, we got Warren up in here
This is how we (Warren up, up in here, Outsiders up here)
We got Fallon up in here, Mulaney, Mulaney's up in here
(Refugee Camp, Refugee Camp, yeah)
Everybody got a breakin' point kid
And they'll rat on you
The family niggas will rat on you
That's why we gotta be prepared to take whoever out we need to""", """Ready or not, here I come, you can't hide
Gonna find you and take it slowly
Ready or not (uh-huh), here I come, you can't hide
Gonna find you and make you want me (yo)
Now that I escape, sleepwalker awake (yeah)
Those who could relate know the world ain't cake
Jail bars ain't golden gates, those who fake, they break
When they meet their four hundred-pound mate
If I could rule the world (if I ruled the world), everyone would have a gun
In the ghetto of course, when giddy-upping on their horse
I kick a rhyme drinking moonshine
I pour a sip on the concrete for the deceased
But, no, don't weep, Wyclef's in a state of sleep
Thinking 'bout the robbery that I did last week
Money in the bag, banker looked like a drag
I want to play with pelicans from here to Baghdad
Gun blast, think fast, I think I'm hit
My girl pinched my hips to see if I still exist
I think not, I'll send a letter to my friends
A born again hooligan only to be king again
Ready or not, here I come, you can't hide
Gonna find you and take it slowly
Ready or not (uh-huh), here I come, you can't hide
Gonna find you and make you want me (yo, yo, yo, yo)
I play my enemies like a game of chess
Where I rest, no stress if you don't smoke sess
Lest I must confess, my destiny's manifest
In some Gore-Tex and sweats, I make treks like I'm homeless
Rap orgies with Porgy and Bess
Capture your bounty like Elliot Ness, yes
Bless you if you represent the Fu
But I'll hex you with some witch's brew if you're doo-doo
Voodoo, I can do what you do, easy
Believe me, fronting n- give me heebie-jeebies (ha)
So while you imitating Al Capone
I'll be Nina Simone and defecating on your microphone
Ready or not, here I come, you can't hide
Gonna find you and take it slowly
You can't run away from these scars I got, oh, baby
Hey, baby, 'cause I got a lot, oh, yeah
And anywhere you go, my whole crew gonna know, oh, baby
Hey, baby, you can't hide from the block, oh, no
Ready or not, refugees taking over
The Buffalo Soldier, dreadlock Rasta
On the twelfth hour, fly by in my bomber (drop bombs)
Crews run for cover, now they're under, pushing up flowers
Superfly, true lies, do or die (he's super fly)
Toss me high, only puff lye with my crew from Lakay
I refugee from Guantanamo Bay
Dance around the border like I'm Cassius Clay (yes, sir)
Ready or not, here I come, you can't hide (ayo, nobody move)
Gonna find you and take it slowly
Ready or not (uh-huh), here I come, you can't hide (ayo, nobody move)
Gonna find you and make you want me (come on)
Ready or not, here I come, you can't hide (you know the)
Gonna find you and take it slowly (you know)
Ready or not (uh-huh), here I come, you can't hide
Gonna find you and make you want me""","""Yeah, yeah
Ayo Black, it's time, word (word, it's time, man)
It's time, man (a'ight, man, begin)
Yeah, straight out the fuckin' dungeons of rap
Where fake niggas don't make it back
I don't know how to start this shit, yo, now
Rappers, I monkey flip 'em with the funky rhythm
I be kickin', musician inflictin' composition of pain, I'm like Scarface sniffin' cocaine
Holdin' an M16, see, with the pen I'm extreme
Now, bullet holes left in my peepholes
I'm suited up with street clothes, hand me a .9, and I'll defeat foes
Y'all know my steelo, with or without the airplay
I keep some E&J, sittin' bent up in the stairway
Or either on the corner bettin' Grants with the cee-lo champs
Laughin' at base-heads, tryna sell some broken amps
G-packs get off quick, forever niggas talk shit
Reminiscin' about the last time the task force flipped
Niggas be runnin' through the block shootin'
Time to start the revolution, catch a body, head for Houston
Once they caught us off-guard, the MAC-10 was in the grass, and
I ran like a cheetah, with thoughts of an assassin
Picked the MAC up, told brothers "Back up!", the MAC spit
Lead was hittin' niggas, one ran, I made him back-flip
Heard a few chicks scream, my arm shook, couldn't look
Gave another squeeze, heard it click, "Yo, my shit is stuck!"
Tried to cock it, it wouldn't shoot, now I'm in danger
Finally, pulled it back and saw three bullets caught up in the chamber
So, now I'm jettin' to the buildin' lobby
And it was full of children, prob'ly couldn't see as high as I be
(So, what you sayin'?) It's like the game ain't the same
Got younger niggas pullin' the triggers, bringin' fame to their name
And claim some corners, crews without guns are goners
In broad daylight, stick-up kids, they run up on us
.45's and gauges, MAC's in fact
Same niggas will catch you back-to-back, snatchin' your cracks in black
There was a snitch on the block gettin' niggas knocked
So hold your stash 'til the coke price drop
I know this crackhead who said she gotta smoke nice rock
And if it's good, she'll bring you customers and measuring pots
But yo, you gotta slide on a vacation
Inside information keeps large niggas erasin' and their wives basin'
It drops deep as it does in my breath
I never sleep, 'cause sleep is the cousin of death
Beyond the walls of intelligence, life is defined
I think of crime when I'm in a New York State of Mind
New York state of mind
New York state of mind
New York state of mind
New York state of mind
Be havin' dreams that I'm a gangsta, drinkin' Moëts, holdin' TEC's
Makin' sure the cash came correct, then I stepped
Investments in stocks, sewin' up the blocks to sell rocks
Winnin' gunfights with mega-cops
Make enough figures until my pockets get bigger
I ain't the type of brother made for you to start testin'
Give me a Smith & Wesson, I'll have niggas undressin'
Thinkin' of cash flow, Buddha, and shelter
Whenever frustrated, I'ma hijack Delta
In the PJ's, my blend tape plays, bullets are strays
Young bitches is grazed, each block is like a maze
Full of black rats trapped, plus the Island is packed
From what I hear in all the stories when my peoples come back black
I'm livin' where the nights is jet-black
The fiends fight to get crack, I just max, I dream I can sit back
And lamp like Capone, with drug scripts sewn
Or the legal luxury life, rings flooded with stones, homes
I got so many rhymes, I don't think I'm too sane
Life is parallel to Hell, but I must maintain
And be prosperous, though we live dangerous
Cops could just arrest me, blamin' us, we're held like hostages
It's only right that I was born to use mics
And the stuff that I write is even tougher than dykes
I'm takin' rappers to a new plateau, through rap slow
My rhymin' is a vitamin held without a capsule
The smooth criminal on beat breaks
Never put me in your box if your shit eats tapes
The city never sleeps, full of villains and creeps
That's where I learned to do my hustle, had to scuffle with freaks
I'm a addict for sneakers, 20's of Buddha and bitches with beepers
In the streets I can greet ya, about blunts I teach ya
Inhale deep like the words of my breath
I never sleep, 'cause sleep is the cousin of death
I lay puzzled as I backtrack to earlier times
Nothing's equivalent to the New York state of mind
New York state of mind
New York state of mind
New York state of mind
New York state of mind""", """Life
I wonder
Will it take me under
I don't know
Imagine smoking weed in the streets without cops harassin'
Imagine going to court with no trial
Lifestyle cruising blue behind my waters
No welfare supporters, more conscious of the way we raise our daughters
Days are shorter, nights are colder
Feeling like life is over, these snakes strike like a cobra
The world's hot my son got not
Evidently, it's elementary, they want us all gone eventually
Troopin' out of state for a plate, knowledge
If coke was cooked without the garbage we'd all have the top dollars
Imagine everybody flashin', fashion
Designer clothes, lacing your click up with diamond vogues
Your people holdin' dough, no parole
No rubbers, go in raw imagine, law with no undercovers
Just some thoughts for the mind
I take a glimpse into time
Watch the blimp read, "The World Is Mine"
If I ruled the world, imagine that
I'd free all my sons, I love 'em love 'em baby
Black diamonds and pearls
Could it be, if you could be mine we'd both shine
If I ruled the world
Still livin' for today, in these last days and times
The way to be, paradise like relaxin', Black, Latino and Anglo-Saxon
Armani, exchange the reins
Cash, Lost Tribe of Shabazz, free at last
Brand new whips to crash then we laugh in the ill'er path
The Villa house is for the crew, how we do
Trees for breakfast, dime sexes and Benz stretches
So many years of depression make me vision
The better livin', type of place to raise kids in
Open they eyes to the lies, history's told foul
But I'm as wise as the old owl, plus the Gold Child
Seeing things like I was controlling, click rollin'
Trickin' six digits on kicks and still holdin'
Trips to Paris, I civilized every savage
Gimme one shot I turn trife life to lavish
Political prisoner set free, stress free
No work release purple M3's and jet skis
Feel the wind breeze in West Indies
I'd make Coretta Scott-King mayor o'the cities and reverse themes to Willies
It sounds foul but every girl I meet to go downtown
I'd open every cell in Attica send em to Africa
If I ruled the world, imagine that
I'd free all my sons, I love 'em love 'em baby
Black diamonds and pearls
Could it be, if you could be mine we'd both shine
If I ruled the world
Still livin' for today, in these last days and times
And then we'll walk right up to the sun
Hand in hand
We'll walk right up to the sun
We won't land
We'll walk right up to the sun
Hand in hand
We'll walk right up to the sun
We won't land
You'd love to hear the story how the thugs live in worry
Duck down in car seats, heat's mandatory
Runnin' from Jake, gettin' chased, hunger for papes
These are the breaks, many mistakes go down out of state
Wait, I had to let it marinate we carry weight
Tryin' to get laced, flip the ace stack, the safe
Millionaire plan to keep the gat with the cock hammer
Makin' moves in Atlanta, back and forth scrambler
'Cause you could have all the chips, be poor or rich
Still nobody want a nigga havin' shit
If I ruled the world and everything in it, sky's the limit
I push a Q-4-5 infinite
It wouldn't be no such thing as jealousies or be felony
Strictly living longevity to the destiny
I thought I'd never see, but reality struck
Better find out before your time's out, what the fuck
If I ruled the world, imagine that
I'd free all my sons, I love 'em love 'em baby
Black diamonds and pearls
Could it be, if you could be mine we'd both shine
If I ruled the world
Still livin' for today, in these last days and times
If I ruled the world, if I ruled, if I ruled
I'd free all my sons, if I ruled, if I ruled
Black diamonds and pearls, black diamonds, black diamonds
Could it be, if you could be mine, we'd both shine
If I ruled the world
Still livin' for today, in these last days and times
If I ruled the world, if I ruled, if I ruled
I'd free all my sons, black diamonds
I love em love em baby
Black diamonds and pearls, if I ruled
If I ruled the world
If I ruled the world
I love em love em baby""", """Ooh, yeah (Ooh)
(Come on, come on)
I see no changes, wake up in the morning and I ask myself
Is life worth livin'? Should I blast myself?
I'm tired of bein' poor and, even worse, I'm black
My stomach hurts so I'm lookin' for a purse to snatch
Cops give a damn about a negro
Pull the trigger, kill a nigga, he's a hero
Give the crack to the kids, who the hell cares?
One less hungry mouth on the welfare
First ship 'em dope and let 'em deal to brothers
Give 'em guns, step back, watch 'em kill each other
"It's time to fight back, " that's what Huey said
Two shots in the dark, now Huey's dead
I got love for my brother
But we can never go nowhere unless we share with each other
We gotta start makin' changes
Learn to see me as a brother instead of two distant strangers
And that's how it's supposed to be
How can the Devil take a brother if he's close to me? Uh
I'd love to go back to when we played as kids
But things change, and that's the way it is
That's just the way it is (Changes)
Things'll never be the same
That's just the way it is (That's the way it is, what?)
Aww, yeah-yeah (Hear me)
(Oh my, oh my, come on, come on)
That's just the way it is (That's just the way it is, the way it is)
Things'll never be the same
(Never be the same, yeah, yeah, yeah, aww, yeah)
That's just the way it is (Way it is)
Aww, yeah (Come on, come on)
I see no changes, all I see is racist faces
Misplaced hate makes disgrace to races
We under, I wonder what it takes to make this
One better place, let's erase the wasted
Take the evil out the people, they'll be actin' right
'Cause both black and white are smokin' crack tonight
And the only time we chill is when we kill each other (Kill each other)
It takes skill to be real, time to heal each other
And although it seems heaven-sent
We ain't ready to see a black president, uh (Oh-ooh)
It ain't a secret, don't conceal the fact
The penitentiary's packed and it's filled with blacks
But some things will never change (Never Change)
Try to show another way, but you stayin' in the dope game (Ooh)
Now tell me, what's a mother to do?
Bein' real don't appeal to the brother in you (Yeah)
You gotta operate the easy way
"I made a G today, " but you made it in a sleazy way
Sellin' crack to the kids (Oh-oh), "I gotta get paid" (Oh)
Well hey, well that's the way it is
That's just the way it is (Changes)
Things'll never be the same
That's just the way it is (That's the way it is, what?)
Aww, yeah (Hear me)
(Oh my, oh my, come on, come on)
That's just the way it is (That's just the way it is, the way it is)
Things'll never be the same
(Never be the same, yeah, yeah, yeah, aww, yeah)
That's just the way it is (Way it is)
Aww, yeah (Aww, yeah, aww, yeah)
We gotta make a change
It's time for us as a people to start makin' some changes
Let's change the way we eat
Let's change the way we live
And let's change the way we treat each other
You see, the old way wasn't workin'
So it's on us to do what we gotta do to survive
And still I see no changes, can't a brother get a little peace?
It's war on the streets and the war in the Middle East (Ooh, yeah)
Instead of war on poverty
They got a war on drugs so the police can bother me
And I ain't never did a crime I ain't have to do
But now I'm back with the facts, givin' it back to you (Ooh)
Don't let 'em jack you up, back you up
Crack you up and pimp-smack you up
You gotta learn to hold your own
They get jealous when they see you with your mobile phone
But tell the cops they can't touch this
I don't trust this, when they try to rush, I bust this
That's the sound of my tool, you say it ain't cool
My mama didn't raise no fool (Oh)
And as long as I stay black, I gotta stay strapped
And I never get to lay back
'Cause I always got to worry 'bout the payback
Some buck that I roughed up way back
Comin' back after all these years
"Rat-a-tat-tat-tat-tat, " that's the way it is, uh
That's just the way it is (Just the way it is, yeah, yeah, yeah)
Things'll never be the same (Yeah)
That's just the way it is (The way it is)
Aww, yeah (Some things will never change, oh my)
(I'm tryna make a change)
(You're my brother, you're my sister, yeah)
That's just the way it is (The way it is, the way it is)
Things'll never be the same (You're my brother, you're my sister)
That's just the way it is, aww, yeah
Some things will never change""", """Uh, hit em with a little ghetto gospel
Those who wish to follow me
My ghetto gospel
I welcome with my hands
And the red sun sinks at last
Into the hills of gold
And peace to this young warrior
Without the sound of guns
If I could recollect before my hood days
I sit and reminisce
Thinking of bliss and the good days
I stop and stare at the younger
My heart goes to 'em
They tested with stress that they under
And nowadays things change
Everyone's ashamed of the youth 'cause the truth look, strange
And for me it's reversed
We left em a world that's cursed
And it hurts
'Cause any day they'll push the button
And all come in like Malcolm X or Bobby Hutton died for nothing
Don't it make you get teary
The world looks dreary
When you wipe your eyes see it clearly
There's no need for you to fear me
If you take your time and hear me
Maybe you can learn to cheer me
It ain't about black or white 'cause we human
I hope we see the light before it's ruined, my ghetto gospel
Those who wish to follow me
My ghetto gospel
I welcome with my hands
And the red sun sinks at last
Into the hills of gold
And peace to this young warrior
Without the sound of guns
Tell me do you see that old lady
Ain't it sad
Living out of bags
Plus she's glad for the little things she has
And over there there's a lady
Crack got her crazy
Guess who's giving birth to a baby
I don't trip or let it fade me
From out of the fryin' pan
We jump into another form of slavery
Even now I get discouraged
Wonder if they take it all back
Will I still keep the courage
I refuse to be a role model
I set goals, take control, drink out my own bottles
I make mistakes but learn from every one
And when it's said and done
I bet this brother be a better one
If I upset you don't stress never forget
That God isn't finished with me yet
I feel his hand on my brain
When I write rhymes I go blind and let the Lord do his thing
But am I less holy
'Cause I chose to puff a blunt and drink a beer with my homies
Before we find world peace
We gotta find peace and end the war in the streets
My ghetto gospel
Those who wish to follow me
My ghetto gospel
I welcome with my hands
And the red sun sinks at last
Into the hills of gold
And peace to this young warrior
Without the sound of guns
Lord can you hear me speak
To pay the price of being hellbound""", """My tea's gone cold, I'm wondering why I
Got out of bed at all
The morning rain clouds up my window
And I can't see at all
And even if I could it'll all be gray
But your picture on my wall
It reminds me, that it's not so bad
It's not so bad
My tea's gone cold, I'm wondering why I
Got out of bed at all
The morning rain clouds up my window (window)
And I can't see at all
And even if I could it'll all be gray
But your picture on my wall
It reminds me, that it's not so bad
It's not so bad
Dear Slim, I wrote you but you still ain't callin'
I left my cell, my pager, and my home phone at the bottom
I sent two letters back in autumn, you must not've got 'em
There probably was a problem at the post office or somethin'
Sometimes I scribble addresses too sloppy when I jot 'em
But anyways, fuck it, what's been up, man? How's your daughter?
My girlfriend's pregnant too, I'm 'bout to be a father
If I have a daughter, guess what I'ma call her?
I'ma name her Bonnie
I read about your uncle Ronnie too, I'm sorry
I had a friend kill himself over some bitch who didn't want him
I know you probably hear this every day, but I'm your biggest fan
I even got the underground shit that you did with Skam
I got a room full of your posters and your pictures, man
I like the shit you did with Rawkus too, that shit was phat
Anyways, I hope you get this, man, hit me back
Just to chat, truly yours, your biggest fan
This is Stan
My tea's gone cold, I'm wondering why I
Got out of bed at all
The morning rain clouds up my window (window)
And I can't see at all
And even if I could it'll all be gray
But your picture on my wall
It reminds me, that it's not so bad
It's not so bad
Dear Slim, you still ain't called or wrote, I hope you have a chance
I ain't mad, I just think it's fucked up you don't answer fans
If you didn't wanna talk to me outside your concert
You didn't have to, but you could've signed an autograph for Matthew
That's my little brother, man, he's only six years old
We waited in the blistering cold for you
For four hours and you just said, "No"
That's pretty shitty, man, you're like his fuckin' idol
He wants to be just like you, man, he likes you more than I do
I ain't that mad though, I just don't like bein' lied to
Remember when we met in Denver, you said if I'd write you you would write back
See, I'm just like you in a way
I never knew my father neither
He used to always cheat on my mom and beat her
I can relate to what you're saying in your songs
So when I have a shitty day, I drift away and put 'em on
'Cause I don't really got shit else, so that shit helps when I'm depressed
I even got a tattoo of your name across the chest
Sometimes I even cut myself to see how much it bleeds
It's like adrenaline, the pain is such a sudden rush for me
See, everything you say is real, and I respect you 'cause you tell it
My girlfriend's jealous 'cause I talk about you 24/7
But she don't know you like I know you Slim, no one does
She don't know what it was like for people like us growin' up, you gotta call me, man
I'll be the biggest fan you'll ever lose
Sincerely yours, Stan
P.S. we should be together too
My tea's gone cold, I'm wondering why I
Got out of bed at all
The morning rain clouds up my window (window)
And I can't see at all
And even if I could it'll all be gray
But your picture on my wall
It reminds me, that it's not so bad
It's not so bad
Dear Mr. I'm Too Good To Call Or Write My Fans
This will be the last package I ever send your ass
It's been six months and still no word, I don't deserve it?
I know you got my last two letters, I wrote the addresses on 'em perfect
So this is my cassette I'm sending you, I hope you hear it
I'm in the car right now, I'm doing ninety on the freeway
Hey Slim, I drank a fifth of vodka
You dare me to drive?
You know the song by Phil Collins, "In the Air of the Night"
About that guy who could have saved that other guy from drowning
But didn't, then Phil saw it all, then at a a show he found him?
That's kinda how this is, you coulda rescued me from drowning
Now it's too late, I'm on a thousand downers now, I'm drowsy
And all I wanted was a lousy letter or a call
I hope you know I ripped all of your pictures off the wall
I love you Slim, we coulda been together, think about it
You ruined it now, I hope you can't sleep and you dream about it
And when you dream I hope you can't sleep and you scream about it
I hope your conscience eats at you and you can't breathe without me
See Slim, shut up bitch, I'm tryna talk
Hey Slim, that's my girlfriend screamin' in the trunk
But I didn't slit her throat, I just tied her up, see I ain't like you
'Cause if she suffocates, she'll suffer more, and then she'll die too
Well, gotta go, I'm almost at the bridge now
Oh shit, I forgot, how am I supposed to send this shit out?
My tea's gone cold, I'm wondering why I
Got out of bed at all
The morning rain clouds up my window (window)
And I can't see at all
And even if I could it'll all be gray
But your picture on my wall
It reminds me, that it's not so bad
It's not so bad
Dear Stan, I meant to write you sooner but I just been busy
You said your girlfriend's pregnant now, how far along is she?
Look, I'm really flattered you would call your daughter that
And here's an autograph for your brother
I wrote it on a Starter cap
I'm sorry I didn't see you at the show, I must've missed you
Don't think I did that shit intentionally just to diss you
But what's this shit you said about you like to cut your wrists too?
I say that shit just clownin', dawg, come on, how fucked up is you?
You got some issues, Stan, I think you need some counseling
To help your ass from bouncing off the walls when you get down some
And what's this shit about us meant to be together?
That type of shit'll make me not want us to meet each other
I really think you and your girlfriend need each other
Or maybe you just need to treat her better
I hope you get to read this letter, I just hope it reaches you in time
Before you hurt yourself, I think that you'll be doin' just fine
If you relax a little, I'm glad I inspire you but Stan
Why are you so mad? Try to understand, that I do want you as a fan
I just don't want you to do some crazy shit
I seen this one shit on the news a couple weeks ago that made me sick
Some dude was drunk and drove his car over a bridge
And had his girlfriend in the trunk, and she was pregnant with his kid
And in the car they found a tape, but they didn't say who it was to
Come to think about, his name was, it was you
Damn!""", """I'm not afraid (I'm not afraid)
Yeah
To take a stand (to take a stand)
It's been a ride
Everybody (everybody)
I guess I had to go to that place
Come take my hand (come take my hand)
To get to this one
We'll walk this road together, through the storm
Now some of you might still be in that place
Whatever weather, cold or warm
If you're tryna get out (just lettin' you know that you're not alone)
Just follow me (holla if you feel like you've been down the same road)
I'll get you there
You can try and read my lyrics off of this paper before I lay 'em
But you won't take the sting out these words before I say 'em
'Cause ain't no way I'ma let you stop me from causin' mayhem
When I say I'm a do somethin', I do it
I don't give a damn what you think
I'm doin' this for me, so fuck the world, feed it beans
It's gassed up, if it thinks it's stoppin' me
I'ma be what I set out to be, without a doubt, undoubtedly
And all those who look down on me, I'm tearin' down your balcony
No if, ands or buts, don't try to ask him why or how can he
From "Infinite" down to the last "Relapse" album he's still shittin'
Whether he's on salary, paid hourly, until he bows out or he shits his bowels out of him
Whichever comes first, for better or worse
He's married to the game, like a fuck you for Christmas
His gift is a curse, forget the Earth, he's got the urge to pull his dick from the dirt
And fuck the whole universe
I'm not afraid (I'm not afraid)
To take a stand (to take a stand)
Everybody (everybody)
Come take my hand come (come take my hand)
We'll walk this road together, through the storm
Whatever weather, cold or warm
Just lettin' you know that you're not alone
Holla if you feel like you've been down the same road
Okay, quit playin' with the scissors and shit, and cut the crap
I shouldn't have to rhyme these words in the rhythm for you to know it's a wrap
You said you was king
You lied through your teeth, for that, fuck your feelings
Instead of gettin' crowned you're gettin' capped, and to the fans
I'll never let you down again, I'm back
I promise to never go back on that promise
In fact, let's be honest, that last "Relapse" CD was eh
Perhaps I ran them accents into the ground
Relax, I ain't goin' back to that now
All I'm tryna say is get back, click-clack, blaow, 'cause I ain't playin' around
There's a game called circle and I don't know how
I'm way too up to back down
But I think I'm still tryna figure this crap out
Thought I had it mapped out but I guess I didn't, this fuckin' black cloud
Still follows me around but it's time to exercise these demons
These muh'fuckers are doin' jumpin' jacks now
I'm not afraid (I'm not afraid)
To take a stand (to take a stand)
Everybody (everybody)
Come take my hand come (come take my hand)
We'll walk this road together, through the storm
Whatever weather, cold or warm
Just lettin' you know that you're not alone
Holla if you feel like you've been down the same road
And I just can't keep living this way
So starting today
I'm breaking out of this cage
I'm standing up, I'ma face my demons
I'm manning up, I'ma hold my ground
I've had enough, now I'm so fed up
Time to put my life back together right now (now)
It was my decision to get clean, I did it for me
Admittedly, I probably did it subliminally for you
So I could come back a brand new me, you helped see me through
And don't realize what you did, ('cause) believe me you
I been through the wringer, but they could do little to the middle finger
I think I got a tear in my eye, I feel like the king of
My world, haters can make like bees with no stingers and drop dead
No more beef lingers, no more drama from now on
I promise to focus solely on handlin' my responsibilities as a father
So I solemnly swear to always treat this roof like my daughters and raise it
You couldn't lift a single shingle on it, 'cause the way I feel
I'm strong enough to go to the club or the corner pub
And lift the whole liquor counter up 'cause I'm raising the bar
I'd shoot for the moon but I'm too busy gazin' at stars, I feel amazing and I'm not
I'm not afraid (I'm not afraid)
To take a stand (to take a stand)
Everybody (everybody)
Come take my hand come (come take my hand)
We'll walk this road together, through the storm
Whatever weather, cold or warm
Just lettin' you know that you're not alone
Holla if you feel like you've been down the same road""", """Yeah, this album is dedicated
To all the teachers that told me I'd never amount to nothin'
To all the people that lived above the buildings that I was hustlin' in front of
Called the police on me when I was just tryin' to make some money to feed my daughter (it's all good)
And all the niggas in the struggle
You know what I'm sayin'? It's all good, baby baby
It was all a dream, I used to read Word Up! magazine
Salt-n-Pepa and Heavy D up in the limousine
Hangin' pictures on my wall
Every Saturday Rap Attack, Mr. Magic, Marley Marl
I let my tape rock 'til my tape popped
Smokin' weed in Bambu, sippin' on Private Stock
Way back, when I had the red and black lumberjack
With the hat to match
Remember Rappin' Duke? Duh-ha, duh-ha
You never thought that hip-hop would take it this far
Now I'm in the limelight 'cause I rhyme tight
Time to get paid, blow up like the World Trade
Born sinner, the opposite of a winner
Remember when I used to eat sardines for dinner
Peace to Ron G, Brucie B, Kid Capri
Funkmaster Flex, Lovebug Starski
I'm blowin' up like you thought I would
Call the crib, same number, same hood
It's all good (it's all good)
And if you don't know, now you know, nigga
You know very well
Who you are
Don't let 'em hold you down
Reach for the stars
You had a goal
But not that many
'Cause you're the only one
I'll give you good and plenty
I made the change from a common thief
To up close and personal with Robin Leach
And I'm far from cheap
I smoke skunk with my peeps all day
Spread love, it's the Brooklyn way
The Moët and Alizé keep me pissy
Girls used to diss me
Now they write letters 'cause they miss me
I never thought it could happen, this rappin' stuff
I was too used to packin' gats and stuff
Now honeys play me close like butter play toast
From the Mississippi down to the East Coast
Condos in Queens, indo for weeks
Sold-out seats to hear Biggie Smalls speak
Livin' life without fear
Puttin' five karats in my baby girl's ear
Lunches, brunches, interviews by the pool
Considered a fool 'cause I dropped out of high school
Stereotypes of a black male misunderstood
And it's still all good
And if you don't know, now you know, nigga
You know very well
Who you are
Don't let 'em hold you down
Reach for the stars
You had a goal
But not that many
'Cause you're the only one
I'll give you good and plenty
Super Nintendo, Sega Genesis
When I was dead broke, man, I couldn't picture this
50-inch screen, money-green leather sofa
Got two rides, a limousine with a chauffeur
Phone bill about two G's flat
No need to worry, my accountant handles that
And my whole crew is loungin'
Celebratin' every day, no more public housin'
Thinkin' back on my one-room shack
Now my mom pimps a Ac' with minks on her back
And she loves to show me off of course
Smiles every time my face is up in The Source
We used to fuss when the landlord dissed us
No heat, wonder why Christmas missed us
Birthdays was the worst days
Now we sip Champagne when we thirsty
Uh, damn right, I like the life I live
'Cause I went from negative to positive
And it's all (It's all good, nigga)
And if you don't know, now you know, nigga
You know very well
Who you are
Don't let 'em hold you down
And if you don't know, now you know, nigga
Reach for the stars
You had a goal
But not that many
'Cause you're the only one
And if you don't know, now you know, nigga
I'll give you good and plenty
Representin' B-Town in the house
Junior Mafia, mad flavor
Uh, uh, yeah, aight
You know very well
Who you are
Don't let 'em hold you down
Reach for the stars
You had a goal
But not that many
'Cause you're the only one
I'll give you good and plenty
Biggie Smalls, it's all good, nigga
Junior Mafia, it's all good, nigga
Bad Boy, it's all good, nigga
It's all good
That's right, '94
And on and on, and on and on
You know very well
Who you are
Don't let 'em hold you down
Reach for the stars""", """I go, on and on and on and
Don't take them to the crib unless they bon'in
Easy, call em on the phone and
Platinum Chanel cologne and
I stay, dressed, to impress
Spark these bitches interest
Sex is all I expect
If they watch TV in the Lex, they know
They know, quarter past fo'
Left the club tipsy, say no mo'
Except how I'm gettin home, tomorrow
Caesar drop you off when he see his P.O.(hey)
Back of my mind, I hope she swallow
Man she spilt a drink on my cream wallows
Reach the gate, hungry just ate
Riffin, she got to be to work by eight
This must mean she ain't tryin to wait
Conversate, sex on the first date I state "You know what you do to me"
She starts off, "Well I don't usually"
Then I, whip it out, rubber no doubt
Step out, show me what you all about
Fingers in your mouth, open up your blouse
Pull your G-string down South, aoowww
Threw that back out, in the parking lot
By a Cherokee and a green drop-top
And I don't stop, until I squirt
Jeans skirt butt-naked it all work
Gotta love ma little nasty girl
U know I love ma little nasty girl
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G
I love ma little nasty girl
All ma women from around the world
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G
I need you to dance
I need you to strip
I need you to shake your little ass 'n' hips
I need you to grind like your working for tips
N give me what I need while we listen to prince
Coz miss you ain't seen the world yet
Rocked la pearl yet
Rocked them pearl sets
Flew in em pearl jets (ooooohhhhh)
In a style make a low profile girl smile
Throw a chick back like a blue print trial
Now you 'n' me can drink some Hennessy
Then we get it on
Mad women wantin to bone Sean combs
Sippin on Patron
Speeding we be leanin
Got em feeling
And when I give it to you throw it right back (right back)
Tell me Diddy 'Yeah I like it like that' (like that)
Lift your shirt
You know how I flirt
Heels and skirt
Let's take it off
Now lets work (lets work)
Gotta love ma little nasty girl
U know I love ma little nasty girl
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G
I love ma little nasty girl
All ma women from around the world
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G
Uh with JE and B.I.G (what, what)
Grab the keys from Diddy (Uh, uh)
The women look-in, no stress
Meet us upstairs in your best yes
Dressed to impress
Spark these bitches interest
Jazze on the beat so sweet
Ladies know you feel me
Grab your titties for the B.I.G
Ok ma what's your preference
Nice and slow
Or fast and breathless
Pull your hair girl, bite your necklace
Let me show you what a nigga from Louis blessed with
Hey, I'm exprained to leave
When I'm done I flip the mattress
Change the sheet (Gotta change them)
I'm like a radical one
I vibrate a little more than your mechanical one
(From your titties to you thong)
Either way mama I'm a make you do it or do it
(Girl I'm about to make you come)
Guaranteed when you fuckin with me
('Cause I go on and on and on, on and on and on, on and on and)
Ladies if you feel me
Grab them Thangs fo Biggie
Gotta love ma little nasty girl
U know I love ma little nasty girl
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G
I love ma little nasty girl
All ma women from around the world
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G
Gotta love ma little nasty girl
U know I love ma little nasty girl
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G
I love ma little nasty girl
All ma women from around the world
I love ma little nasty girl
All the ladies if you hear me
Grab your titties for B.I.G""", """What that nigga want, God?
Word up, look out for the cops though (Wu-Tang five finger shit, fam)
Cash rules-
Word up, two for fives over here, baby
Word up, two for fives, niggas got garbage down the way
Word up, know what I'm sayin'?
Cash rules everything around me, C.R.E.A.M. get-
Yeah, check this old fly shit out, word up
(Cash rules everything around me) take you on a natural joint
(C.R.E.A.M. get the money)
(Dollar dollar bill, y'all) here we, here we go, check this shit, yo
I grew up on the crime side, the New York Times side
Stayin' alive was no jive
Had secondhands, Mom's bounced on old man
So then we moved to Shaolin land
A young youth, yo, rockin' the gold tooth, 'Lo goose
Only way I begin the G off was drug loot
And let's start it like this, son
Rollin' with this one and that one, pullin' out gats for fun
But it was just a dream for the teen
Who was a fiend, started smokin' woolies at 16
And runnin' up in gates and doin' hits for high stakes
Makin' my way on fire escapes
No question, I would speed for cracks and weed
The combination made my eyes bleed
No question, I would flow off and try to get the dough all
Stickin' up white boys in ball courts
My life got no better, same damn 'Lo sweater
Times is rough and tough like leather
Figured out I went the wrong route
So I got with a sick-ass clique and went all out
Catchin' keys from 'cross seas
Rollin' in MPV's, every week we made 40 G's
Yo, nigga, respect mine, or here go the TEC-9
Ch-chick-pow! Move from the gate now
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all
It's been 22 long, hard years, I'm still strugglin'
Survival got me buggin', but I'm alive on arrival
I peep at the shape of the streets
And stay awake to the ways of the world 'cause shit is deep
A man with a dream with plans to make cream
Which failed; I went to jail at the age of 15
A young buck sellin' drugs and such, who never had much
Tryin' to get a clutch at what I could not-
The court played me short, now I face incarceration
Pacin', goin' upstate's my destination
Handcuffed in the back of a bus, 40 of us
Life as a shorty shouldn't be so rough
But as the world turned, I learned life is hell
Livin' in the world no different from a cell
Every day I escape from Jakes givin' chase
Sellin' base, smokin' bones in the staircase
Though I don't know why I chose to smoke sess
I guess that's the time when I'm not depressed
But I'm still depressed, and I ask, "What's it worth?"
Ready to give up so I seek the old Earth
Who explained workin' hard may help you maintain
To learn to overcome the heartaches and pain
We got stick-up kids, corrupt cops, and crack rocks
And stray shots, all on the block that stays hot
Leave it up to me while I be livin' proof
To kick the truth to the young black youth
But shorty's runnin' wild, smokin' sess, drinkin' beer
And ain't tryna hear what I'm kickin' in his ear
Neglected for now, but yo, it gots to be accepted
That what? That life is hectic
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all
Cash rules everything around me (my niggas gots to do what they gotta do)
C.R.E.A.M., get the money
Dollar dollar bill, y'all (to get through, know what I'm sayin'?)
Cash rules everything around me (because you can't just get by no more)
C.R.E.A.M., get the money
Dollar dollar bill, y'all (word up, you gotta get over, straight up and down)
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all
Yeah, yeah
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all
Cash rules everything around me
C.R.E.A.M., get the money
Dollar dollar bill, y'all-all-all, yeah""", """So what's up, man?
Coolin', man
Chillin' chilin'? Yo, you know I had to call, you know why right?
Why?
Because, yo, I never ever call and ask you to play somethin', right?
Yeah
You know what I wanna hear, right?
Whatchu wanna hear?
I wanna hear that Wu-Tang joint
Wu-Tang again?
Ah, yeah, again and again
Wu-Tang Clan comin' at ya
Watch your step, kid
Watch your step, kid (protect ya neck, kid)
Watch your step, kid (so set it off)
Watch your step, kid
Watch your step, kid
Watch your step, kid (de Inspector Deck)
I smoke on the mic like "Smokin' Joe" Frazier
The hell raiser, raisin' hell with the flavor
Terrorize the jam like troops in Pakistan
Swingin' through your town like your neighborhood Spiderman
So uh, tick-tock and keep tickin'
While I get ya flippin' off the sh- I'm kickin'
The Lone Ranger, code red, danger!
Deep in the dark with the art to rip charts apart
The vandal, too hot to handle
Ya battle, you're sayin' "Goodbye" like Tevin Campbell
Roughneck, Inspector Deck's on the set
The Rebel, I make more noise than heavy metal
The way I make the crowd go wild, sit back, relax, won't smile
Rae got it goin' on pal, call me the rap assassinator
Rhymes rugged and built like Schwarzenegger
And I'ma get mad deep like a threat
Blow up your project, then take all your assets
'Cause I came to shake the frame in half
With the thoughts that bomb, shit like math
So if you wanna try to flip, go flip on the next man
'Cause I grab the clip and hit you with 16 shots and more I got
Goin' to war with the meltin' pot, akh
It's the Method Man, for short Mr. Meth
Movin' on your left, ah!
And set it off, get it off, let it off like a gat
I wanna break full, cock me back
Small change, they puttin' shame in the game
I take aim and blow that nigga out the frame
And like Fame, my style'll live forever
Niggas crossin' over, but they don't know no better
But I do, true, can I get a, "soo!"
'Nough respect due to the one-six-oo
I mean oh, yo check out the flow
Like the Hudson or PCP when I'm dustin'
Niggas off because I'm hot like sauce
The smoke from the lyrical blunt makes me, uh
What? Grab my nut, get screwed
(Ow!) Here comes my Shaolin style
True B-A-ba-B-Y-U
To my crew with the, "Soo!"
Watch your step, kid (yeah, yeah, yeah)
Watch your step, kid (c'mon, baby baby, c'mon, baby baby)
Watch your step, kid (c'mon, baby baby, c'mon)
Watch your step, kid (yo, you best protect ya neck)
First things first man you're f- with the worst
I'll be stickin' pins in your head like a f- nurse
I'll attack any nigga who's slack in his mack
Come fully packed with a fat rugged stack
Shame on you when you stepped through to
The Ol' Dirty Bastard straight from the Brooklyn Zoo
And I'll be damned if I let any man
Come to my center, you enter, the winter
Straight up and down that sh- packed jam
You can't slam, don't let me get fool on him man
The Ol' Dirty Bastard is dirty and stinkin'
Ason Unique rollin' with the night of the creeps
Niggas be rollin' with a stash, ain't sayin' cash
Bite my style I'll bite your motherfuckin' ass
For cryin' out loud my style is wild so book me
Not long is how long that this rhyme took me
Ejectin' styles from my lethal weapon
My pen that rocks from here to Oregon
Here's more again, catch it like a psycho flashback
I love gats, if rap was a gun, you wouldn't bust back
I come with sh- that's all types of shapes and sounds
And where I lounge is my stompin' grounds
I give an order to my peeps across the water
To go and snatch up props all around the border
And get far like a shootin' star
'Cause who I are is livin' the life of Pablo Escobar
Point-blank as I kick the square biz
There it is, you're fuckin' with pros, and there it goes
Yo, chill with the feedback, black we don't need that
It's ten o'clock, hoe, where the fuck's your seed at?
Feelin' mad hostile, ran the apostle
Flowin' like Christ when I speaks the gospel
Stroll with the holy roll, then attack the globe with the buckus style
The ruckus, ten times ten men committin' mad sin
Turn the other cheek and I'll break your f- chin
Slayin' boom-bangs like African drums (we'll be)
Comin' around the mountain when I come
Crazy flamboyant for the rap enjoyment
My clan increase like black unemployment
Yeah, another one dare, G-Gka-Genius
Take us the f- outta here
The Wu is too slammin' for these Cold Killin' labels
Some ain't had hits since I seen Aunt Mabel
Be doin' artists in like Cain did Abel
Now they money's gettin' stuck to the gum under the table
That's what ya get when ya misuse what I invent
Your empire falls and you lose every cent
For tryin' to blow up a scrub
Now that thought was just as bright as a 20-watt light bulb
Should've pumped it when I rocked it
Niggas so stingy they got short arms and deep pockets
This goes on in some companies
With majors, they're scared to death to pump these
First of all, who's your A&R?
A mountain climber who plays an electric guitar?
But he don't know the meanin' of dope
When he's lookin' for a suit-and-tie-rap
That's cleaner than a bar of soap
And I'm the dirtiest thing in sight
Matter of fact, bring out the girls, and let's have a mud fight
You best protect ya neck
You best protect ya neck
You best protect ya neck
You best protect ya neck""", """Every second, every minute, man I swear that she can get it
Say if you a bad bitch put your hands up high, hands up high, hands up high
Tell 'em dim the lights down right now, put me in the mood
I'm talking 'bout dark room, perfume
Go, go
I recognize your fragrance (hol' up)
You ain't never gotta say shit (woo)
And I know your taste is
A little bit (mmm) high maintenance (ooh)
Everybody else basic
You live life on an everyday basis
With poetic justice, poetic justice
If I told you that a flower bloomed in a dark room, would you trust it?
I mean I write poems in these songs dedicated to you
When you're in the mood for empathy, there's blood in my pen
Better yet where your friends and them?
I really wanna know you all
I really wanna show you off
Fuck that, pour up plenty of champagne
Cold nights when you curse this name
You called up your girlfriends and
Y'all curled in that little bitty Range I heard that
She wanna go and party, she wanna go and party
Nigga don't approach her with that Atari
Nigga that ain't good game, homie, sorry
They say conversation, rule a nation, I can tell
But I could never right my wrongs
'Less I write it down for real, P.S
You can get it, you can get it
You can get it, you can get it
And I know just, know just, know just, know just, know just what you want
Poetic justice, put it in a song
You can get it, you can get it
You can get it, you can get it
And I know just, know just, know just, know just, know just what you want
Poetic justice, put it in a song
I really hope you play this
'Cause ol' girl you test my patience
With all these seductive photographs and all these one off vacations
You've been taken
Clearly a lot for me to take in
It don't make sense
Young East African Girl, you too busy fucking with your other man
I was trying to put you on game, put you on a plane
Take you and your mama to the motherland
I could do it, maybe one day
When you figure out you're gonna need someone
When you figure out it's all right here in the city
And you don't run from where we come from
That sound like poetic justice, poetic justice
You were so new to this life but God damn you got adjusted
I mean I write poems in these songs, dedicated to the fun sex
Your natural hair and your soft skin, and your big ass in that sundress (ooh)
Good God, what you doing that walk for?
When I see that thing move, I just wish we would fight less
And we would talk more
And they say communication save relations, I can tell
But I can never right my wrongs unless I write them down for real
P.S
You can get it, you can get it
You can get it, you can get it
And I know just, know just, know just, know just, know just what you want
Poetic justice, put it in a song
Every time I write these words they become a taboo
Making sure my punctuation curve, every letter here's true
Living my life in the margin and that metaphor was proof
I'm talking poetic justice, poetic justice
If I told you that a flower bloomed in a dark room, would you trust it?
I mean you need to hear this
Love is not just a verb, it's you looking in the mirror
Love is not just a verb, it's you looking for a maybe
Call me crazy, we can both be insane
A fatal attraction is common
And what we have common is pain
I mean you need to hear this
Love is not just a verb and I can see power steering
Sex drive when you swerve, I want that interference
It's coherent, I can hear it, mmhm
That's your heartbeat
It either caught me or it called me, mmhm
Breathe slow and you'll find gold mines in these lines
Sincerely, yours truly
And right before you go blind
P.S
You can get it, you can get it
You can get it, you can get it
And I know just, know just, know just, know just, know just what you want
Poetic justice, put it in a song
I'm gon' ask you one more time, homie
Where is you from? Or it is a problem (ask him if he here for Sherane)
Ayy, you over here for Sherane, homie?
I don't care who this nigga over here for
If he don't tell me where he from, it's a wrap I'm sorry
Hol' up, hol' up, hol' up, we gon' do it like this, okay?
I'ma tell you where I'm from, okay?
You gon' tell me where you from, okay?
Or where your grandma stay, where your mama stay
Or where your daddy stay, okay? Fuck with all this talkin'
As a matter of fact, get out the van, homie
Get out the car before I snatch you out that motherfucker, homie""", """I got, I got, I got, I got
Loyalty, got royalty inside my DNA
Cocaine quarter piece, got war and peace inside my DNA
I got power, poison, pain and joy inside my DNA
I got hustle though, ambition, flow inside my DNA
I was born like this, since one like this, immaculate conception
I transform like this, perform like this, was Yeshua new weapon
I don't contemplate, I meditate, then off your fucking head
This that put-the-kids-to-bed
This that I got, I got, I got, I got
Realness, I just kill shit 'cause it's in my DNA
I got millions, I got riches buildin' in my DNA
I got dark, I got evil, that rot inside my DNA
I got off, I got troublesome heart inside my DNA
I just win again, then win again like Wimbledon, I serve
Yeah, that's him again, the sound that engine in is like a bird
You see fireworks and Corvette tire skrrt the boulevard
I know how you work, I know just who you are
See, you's a, you's a, you's a
Bitch, your hormones prolly switch inside your DNA
Problem is, all that sucker shit inside your DNA
Daddy prolly snitched, heritage inside your DNA
Backbone don't exist, born outside a jellyfish, I gauge
See, my pedigree most definitely don't tolerate the front
Shit I've been through prolly offend you, this is Paula's oldest son
I know murder, conviction, burners, boosters
Burglars, ballers, dead, redemption
Scholars, fathers dead with kids and
I wish I was fed forgiveness
Yeah, yeah, yeah, yeah, soldier's DNA
Born inside the beast, my expertise checked out in second grade
When I was 9, on cell, motel, we didn't have nowhere to stay
At 29, I've done so well, hit cartwheel in my estate
And I'm gon' shine like I'm supposed to, antisocial, extrovert
And excellent mean the extra work
And absentness what the fuck you heard
And pessimists never struck my nerve
And Nazareth gonna plead his case
The reason my power's here on earth
Salute the truth, when the prophet say
I got loyalty, got royalty inside my DNA (this is why I say that hip hop)
I got loyalty, got royalty inside my DNA (has done more damage to young African Americans)
I live a better life, I'm rollin' several dice, fuck your life (than racism in recent years)
I got loyalty, got royalty inside my DNA (I live a be-, fuck your life)
This is my heritage, all I'm inheritin' (5, 4, 3, 2, 1)
Money and power, the mecca of marriages
Tell me somethin'
You motherfuckers can't tell me nothin'
I'd rather die than to listen to you
My DNA not for imitation
Your DNA an abomination
This how it is when you're in the Matrix
Dodgin' bullets, reapin' what you sow
And stackin' up the footage, livin' on the go
And sleepin' in a villa
Sippin' from a Grammy and walkin' in the buildin'
Diamond in the ceilin', marble on the floors
Beach inside the window, peekin' out the window
Baby in the pool, godfather goals
Only Lord knows I've been goin' hammer
Dodgin' paparazzi, freakin' through the cameras
Eat at Four Daughters, Brock wearin' sandals
Yoga on a Monday, stretchin' to Nirvana
Watchin' all the snakes, curvin' all the fakes
Phone never on, I don't conversate
I don't compromise, I just penetrate
Sex, money, murder, these are the breaks
These are the times, level number 9
Look up in the sky, 10 is on the way
Sentence on the way, killings on the way
Motherfucker, I got winners on the way
You ain't shit without a body on your belt
You ain't shit without a ticket on your plate
You ain't sick enough to pull it on yourself
You ain't rich enough to hit the lot and skate
Tell me when destruction gonna be my fate
Gonna be your fate, gonna be our faith
Peace to the world, let it rotate
Sex, money, murder, our DNA""", """If you're having girl problems I feel bad for you son
I got ninety-nine problems but a bitch ain't one
I got the rap patrol on the gat patrol
Foes that want to make sure my casket's closed
Rap critics that say he's "Money Cash Hoes"
I'm from the hood, stupid, what type of facts are those?
If you grew up with holes in your zapatos
You'd celebrate the minute you was having dough
I'm like, "Fuck critics" you can kiss my whole asshole
If you don't like my lyrics, you can press fast forward
Got beef with radio if I don't play they show
They don't play my hits, well, I don't give a shit, so
Rap mags try and use my black ass
So advertisers can give 'em more cash for ads, fuckers
I don't know what you take me as
Or understand the intelligence that Jay-Z has
I'm from rags to riches, niggas I ain't dumb
I got ninety nine problems but a bitch ain't one, hit me
Ninety nine problems but a bitch ain't one
If you having girl problems I feel bad for you son
I got ninety nine problems but a bitch ain't one, hit me
The year's '94 and my trunk is raw
In my rearview mirror is the motherfucking law
I got two choices y'all, pull over the car or
Bounce on the devil, put the pedal to the floor
Now I ain't trying to see no highway chase with Jake
Plus I got a few dollars I can fight the case
So I, pull over to the side of the road
I heard, "Son, do you know why I'm stopping you for?"
"Cause I'm young and I'm black and my hat's real low"
Do I look like a mind reader, sir? I don't know
Am I under arrest or should I guess some more?
"Well you was doing fifty-five in a fifty-four" (uh huh)
"License and registration and step out of the car"
"Are you carrying a weapon on you, I know a lot of you are"
I ain't stepping out of shit, all my papers legit
"Well do you mind if I look around the car a little bit?"
Well my glove compartment is locked, so is the trunk in the back
And I know my rights so you goin' need a warrant for that
"Aren't you sharp as a tack? You some type of lawyer or something?"
"Somebody important or something?"
Well, I ain't passed the bar, but I know a little bit
Enough that you won't illegally search my shit
"Well we'll see how smart you are when the K-9 come"
I got ninety nine problems but a bitch ain't one, hit me
Ninety nine problems but a bitch ain't one
If you having girl problems I feel bad for you son
I got ninety nine problems but a bitch ain't one, hit me
Ninety nine problems but a bitch ain't one
If you having girl problems I feel bad for you son
I got ninety nine problems but a bitch ain't one, hit me
Now once upon a time not too long ago
A nigga like myself had to strong-arm a ho
This is not a ho in the sense of having a pussy
But a pussy having no goddamn sense try and push me
I tried to ignore 'em, talk to the Lord
Pray for 'em, 'cause some fools just love to perform
You know the type, loud as a motorbike
But wouldn't bust a grape in a fruit fight
The only thing that's goin' happen is I'ma get to clapping and
He and his boys goin' be yapping to the Captain
And there I go trapped in the Kit-Kat again
Back through the system with the riff-raff again
Fiends on the floor scratching again
Paparazzi's with they cameras, snapping 'em
D.A. tried to give a nigga shaft again
Half a mil' for bail 'cause I'm African
All because this fool was harassing them
Trying to play the boy like he's saccharine
But ain't nothing sweet 'bout how I hold my gun
I got ninety-nine problems being a bitch ain't one, hit me
Ninety-nine problems but a bitch ain't one
If you having girl problems I feel bad for you son
I got ninety-nine problems but a bitch ain't one, hit me
Ninety-nine problems but a bitch ain't one
If you having girl problems I feel bad for you son
I got ninety-nine problems but a bitch ain't one, hit me
Having girl problems I feel bad for you son
I got ninety-nine problems and a bitch ain't one
You're crazy for this one, Rick, it's your boy""", """We're gonna skate to one song and one song only
(Ball so hard, motherfuckers wanna fine me)
So I ball so hard, motherfuckers wanna fine me
But first niggas gotta find me
What's fifty grand to a motherfucker like me?
Can you please remind me?
Ball so hard, this shit crazy
Y'all don't know that don't shit faze me
The Nets could go 0 for 82
And I look at you like this shit gravy
Ball so hard, this shit weird
We ain't even 'posed to be here
Ball so hard, but since we here
It's only right that we'd be fair
Psycho, I'm liable
To go Michael, take your pick
Jackson, Tyson, Jordan, Game 6
Ball so hard, got a broke clock
Rollies that don't tick-tock
Audemars that's losing time
Hidden behind all these big rocks
B-Ball so hard, I'm shocked too
I'm supposed to be locked up too
You escaped what I escaped
You'd be in Paris getting fucked up too
B-Ball so hard, let's get faded
Le Meurice for like six days
Gold bottles, scold models
Spillin' Ace on my sick J's
B-Ball so hard, bitch, behave
Just might let you meet 'Ye
Chi-Towns, D. Rose
I'm moving the Nets, BK
Ball so hard motherfuckers wanna fine me
That shit cray
That shit cray
That shit cray
B-Ball so hard motherfuckers wanna fine me
That shit cray
That shit cray
That shit cray
She said, "Ye, can we get married at the mall?"
I said, "Look, you need to crawl 'fore you ball
Come and meet me in the bathroom stall
And show me why you deserve to have it all"
Ball so hard
That shit cray (that shit cray)
Ain't it Jay?
B-Ball so hard
What she order? (What she order?)
Fish fillet?
B-Ball so hard
Yo' whip so cold (whip so cold)
This old thing?
Ball so hard
Act like you'll never be around motherfuckers like this again
Bougie girl, grab her hand
Fuck that bitch, she 'on't wanna dance
'Scuse my French, but I'm in France
Hehe, I'm just sayin'
Prince William's ain't do it right if you ask me
'Cause I was him, I would've (married Kate and Ashley)
What's Gucci, my nigga?
What's Louis, my killer?
What's drugs, my dealer?
What's that jacket, Margiela?
Doctors say I'm the illest
'Cause I'm suffering from realness
Got my niggas in Paris and they going gorillas, huh?
I don't even know what that means
No one knows what it means
But it's provocative
No, it's not, it's gross
Gets the people going
Ball so hard motherfuckers wanna fine me
B-Ball so hard motherfuckers wanna fine me
You are now watching the throne
Don't let me get in my zone
Don't let me get in my zone
Don't let me get in my zone
These other niggas is lyin'
Actin' like the summer ain't mine
I got that hot bitch in my home
You know how many hot bitches I own?
Don't let me get in my zone
Don't let me get in my zone
Don't let me get in my zone
Don't let me get in my zone
The Stars is in the building
They hands is to the ceiling
I know I'm 'bout to kill it
How you know I got that feeling?
You are now watching the throne
Don't let me into my zone
Don't let me into my zone
I'm definitely in my zone""", """Yeah, nigga
I'm still fucking with you
Still waters run deep
Still Snoop Dogg and D-R-E, '99 nigga
Guess who's back?
Still, doing that shit Andre?
(Oh for sho', check me out)
It's still Dre Day nigga, AK nigga
Though I've grown a lot, can't keep it home a lot
'Cause when I frequent the spots that I'm known to rock
You hear the bass from the truck when I'm on the block
Ladies they pay homage, but haters say Dre fell off
How nigga? My last album was The Chronic (Nigga)
They want to know if he still got it
They say rap's changed
They wanna know how I feel about it
(If you ain't up on thangs)
Dr. Dre is the name
I'm ahead of my game
Still puffing my leafs
Still fuck with the beats, still not loving police
Still rock my khakis with a cuff and a crease
Still got love for the streets, reppin' 213 (For life)
Still the beats bang, still doing my thang
Since I left ain't too much changed, still
I'm representing for them gangstas all across the world
(Still) Hitting them corners in them low-lows, girl
Still taking my time to perfect the beat
And I still got love for the streets, it's the D-R-E
I'm representing for them gangstas all across the world
(Still) Hitting them corners in them low-lows, girl
Still taking my time to perfect the beat
And I still got love for the streets, it's the D-R-E
Since the last time you heard from me, I lost some friends
Well, hell, me and Snoop, we dippin' again
Kept my ear to the streets, signed Eminem
He's triple platinum, doing 50 a week
Still, I stay close to the heat
And even when I was close to defeat, I rose to my feet
My life's like a soundtrack I wrote to the beat
Treat rap like Cali' weed, I smoke 'til I sleep
Wake up in the a.m., compose a beat
I bring the fire 'til you're soaking in your seat
It's not a fluke, it's been tried, I'm the truth
Since "Turn Out the Lights" from the World Class Wreckin Cru
I'm still at it, after-mathematics
In the home of drive-bys and ak-matics
Swap meets, sticky green, and bad traffic
I dip through, then I give you (Still) D-R-E
I'm representing for them gangstas all across the world
(Still) Hitting them corners in them low-lows, girl
Still taking my time to perfect the beat
And I still got love for the streets, it's the D-R-E
I'm representing for them gangstas all across the world
(Still) Hitting them corners in them low-lows, girl
Still taking my time to perfect the beat
And I still got love for the streets, it's the D-R-E
It ain't nothing but more hot shit
Another classic CD for y'all to vibe with
Whether you're cooling on the corner with your fly bitch (Biatch)
Laid back in the shack, play this track
I'm representing for the gangstas all across the world
Still (Hittin' them corners in them low-lows, girl)
I'll break your neck, damn near put your face in your lap
Niggas try to be the king but the ace is back
So if you ain't up on thangs
Dr. Dre be the name still running the game
Still, got it wrapped like a mummy
Still ain't tripping, love to see young blacks get money
Spend time out the hood, take they moms out the hood
Hit my boys off with jobs, no more living hard
Barbeques every day, driving fancy cars
Still gon' get mine regardless
I'm representing for them gangstas all across the world
(Still) Hitting them corners in them low-lows, girl
Still taking my time to perfect the beat
And I still got love for the streets, it's the D-R-E
I'm representing for them gangstas all across the world
(Still) Hitting them corners in them low-lows, girl
Still taking my time to perfect the beat
And I still got love for the streets, it's the D-R-E
I'm representing for them gangstas all across the world
(Still) Hitting them corners in them low-lows, girl
Still taking my time to perfect the beat
And I still got love for the streets, it's the D-R-E
Right back up in your motherfuckin' ass
Nine-five plus four pennies, add that shit up
D.R.E. right back up on top of thangs
Smoke some wit' your Dogg
No stress, no seeds, no stems, no sticks!
Some of that real sticky-icky-icky
Ooh wee! Put it in the air!
Well, you's a fool, D-R, ha-ha""", """Snoop
Snoop
When the pimp's in the crib ma
Drop it like it's hot
Drop it like it's hot
Drop it like it's hot
When the pigs try to get at you
Park it like it's hot
Park it like it's hot
Park it like it's hot
And if a nigga get a attitude
Pop it like it's hot
Pop it like it's hot
Pop it like it's hot
I got the Rollie on my arm and I'm pouring Chandon
And I roll the best weed 'cause I got it going on
Uh! I'm a nice dude, with some nice dreams
See these ice cubes, see these ice creams?
Eligible bachelor, million dollar boat
That's whiter than what's spilling down your throat
The Phantom, exterior like fish eggs
The interior like suicide-wrist red
I can exercise you, this can be your Phys. Ed
Cheat on your man ma, that's how you get ahizzead
Killer wit the beat, I know killers in the street
Wit' the steel that'll make you feel like Chinchilla in the heat
So don't try to run up on my ear talking all that raspy shit
Trying to ask me shit
When my niggas fill ya vest they ain't gon' pass me shit
You should think about it, take a second
Matter fact, you should take four, B
And think before you fuck wit lil' skateboard P
When the pimp's in the crib ma
Drop it like it's hot
Drop it like it's hot
Drop it like it's hot
When the pigs try to get at you
Park it like it's hot
Park it like it's hot
Park it like it's hot
And if a nigga get a attitude
Pop it like it's hot
Pop it like it's hot
Pop it like it's hot
I got the Rollie on my arm and I'm pouring Chandon
And I roll the best weed 'cause I got it going on
I'm a gangsta, but y'all knew that
Da Big Boss Dogg, yeah I had to do that
I keep a blue flag hanging out my backside
But only on the left side, yeah that's the Crip side
Ain't no other way to play the game the way I play
I cut so much you thought I was a DJ
Two, one, yep, three
S-N double O-P, D-O double G
I can't fake it, just break it, and when I take it
See I specialize in making all the girls get naked
So bring your friends, all of y'all come inside
We got a world premiere right here, now get live (so)
So don't change the dizzle, turn it up a little
I got a living room full of fine dime brizzles
Waiting on the Pizzle, the Dizzle and the Shizzle
G's to the bizzack, now ladies here we gizzo
When the pimp's in the crib ma
Drop it like it's hot
Drop it like it's hot
Drop it like it's hot
When the pigs try to get at you
Park it like it's hot
Park it like it's hot
Park it like it's hot
And if a nigga get a attitude
Pop it like it's hot
Pop it like it's hot
Pop it like it's hot
I got the Rollie on my arm and I'm pouring Chandon
And I roll the best weed 'cause I got it going on
I'm a Bad Boy, with a lotta hoes
Drive my own cars, and wear my own clothes
I hang out tough, I'm a real boss
Big Snoop Dogg, yeah he's so sharp
On the TV screen and in the magazines
If you play me close, you're on a red beam
Oh you got a gun so you want to pop back?
AK-47 now nigga, stop that
Cement shoes, now I'm on the move
You're family's crying, now you on the news
They can't find you and now they miss you
Must I remind you I'm only here to twist you
Pistol whip you, dip you then flip you
Then dance to this motherfucking music we Crip to
Subscribe nigga, get yo' issue
Baby, come close, let me see how you get loose
When the pimp's in the crib ma
Drop it like it's hot
Drop it like it's hot
Drop it like it's hot
When the pigs try to get at you
Park it like it's hot
Park it like it's hot
Park it like it's hot
And if a nigga get a attitude
Pop it like it's hot
Pop it like it's hot
Pop it like it's hot
I got the Rollie on my arm and I'm pouring Chandon
And I roll the best weed 'cause I got it going on
Snoop
Snoop""", """She take my money when I'm in need
Yeah, she's a triflin' friend indeed
Oh, she's a gold digger way over town
That digs on me (uh)
Now I ain't sayin' she a gold digger
But she ain't messin' with no broke niggas
Now I ain't sayin' she a gold digger
But she ain't messin' with no broke niggas
Get down girl, go'n 'head get down
Get down girl, go'n 'head get down
Get down girl, go'n 'head get down
Get down girl, go'n 'head
Cutie the bomb, met her at a beauty salon
With a baby Louis Vuitton under her underarm
She said, "I can tell you rock, I can tell by your charm
Far as girls you got a flock
I can tell by your charm and your arm"
But I'm lookin' for the one, have you seen her?
My psychic told me she have a ass like Serena
Trina, Jennifer Lopez, four kids
And I gotta take all they bad ass to ShowBiz?
Okay, get yo' kids, but then they got their friends
I pulled up in the Benz, they all got a pen
We all went to din' and then I had to pay
If you fuckin' with this girl then you better be paid
You know why?
It take too much to touch her
From what I heard she got a baby by Busta
My best friend say she used to fuck with Usher
I don't care what none of y'all say I still love her
Now I ain't sayin' she a gold digger, uh
But she ain't messin' with no broke niggas, uh
Now I ain't sayin' she a gold digger, uh
But she ain't messin' with no broke niggas, uh
Get down girl, go'n 'head get down
Get down girl, go'n 'head get down
Get down girl, go'n 'head get down
Get down girl, go'n 'head
18 years, 18 years
She got one of yo' kids, got you for 18 years
I know somebody payin' child support for one of his kids
His baby momma car and crib is bigger than he is
You will see him on TV any given Sunday
Win the Super Bowl and drive off in a Hyundai
She was supposed to buy your shorty Tyco with your money
She went to the doctor, got lipo with your money
She walkin' around lookin' like Michael with your money
Shoulda got that insured, Geico for your money (money)
If you ain't no punk holla, "We want prenup"
"We want prenup!", yeah
It's something that you need to have
'Cause when she leave yo' ass she gone leave with half
18 years, 18 years
And on her 18th birthday, he found out it wasn't his
Now I ain't sayin' she a gold digger, uh
But she ain't messin' with no broke niggas, uh
Now I ain't sayin' she a gold digger, uh
But she ain't messin' with no broke niggas, uh
Get down girl, go'n 'head get down, uh
Get down girl, go'n 'head get down
Get down girl, go'n 'head get down, uh
Get down girl, go'n 'head
Now I ain't sayin' you a gold digger, you got needs
You don't want a dude to smoke, but he can't buy weed
You go out to eat, he can't pay, y'all can't leave
There's dishes in the back, he gotta roll up his sleeves
But while y'all washin', watch him
He gon' make it to a Benz out of that Datsun
He got that ambition, baby, look at his eyes
This week he moppin' floors, next week it's the fries
So, stick by his side
I know there's dudes ballin', and yeah, that's nice
And they gone keep callin' and tryin'
But you stay right girl
And when he get on, he'll leave yo' ass for a white girl
Get down girl, go'n head get down
Get down girl, go'n 'head get down
Get down girl, go'n 'head get down
Get down girl, go'n head
Let me hear that back""", """I'm living in that 21st century
Doing something mean to it
Do it better than anybody you ever seen do it
Screams from the haters, got a nice ring to it
I guess every superhero need his theme music
No one man should have all that power
The clock's ticking, I just count the hours
Stop tripping, I'm tripping off the power
(21st-century schizoid man)
The system broken, and the school's closed, the prisons open
We ain't got nothin' to lose, ma'fucka, we rollin'
Huh? Ma'fucka, we rollin'
With some light-skinned girls and some Kelly Rowlands
In this white man's world, we the ones chosen
So goodnight, cruel world, I'll see you in the mornin'
Huh? I'll see you in the mornin'
This is way too much, I need a moment
No one man should have all that power
The clock's ticking, I just count the hours
Stop tripping, I'm tripping off the power
'Til then, fuck that, the world's ours
And they say, and they say
And they say, and they say
And they say, and they say
(21st-century schizoid man)
Fuck SNL and the whole cast
Tell 'em Yeezy said they can kiss my whole ass
More specifically, they can kiss my asshole
I'm an asshole? You niggas got jokes
You short-minded niggas thoughts is Napoleon
My furs is Mongolian, my ice brought the goalies in
Now I embody every characteristic of the egotistic
He knows he so fuckin' gifted
I just needed time alone, with my own thoughts
Got treasures in my mind but couldn't open up my own vault
My childlike creativity, purity and honesty
Is honestly being crowded by these grown thoughts
Reality is catching up with me
Taking my inner child, I'm fighting for custody
With these responsibilities that they entrusted me
As I look down at my diamond encrusted piece
Thinkin', no one man should have all that power
The clock's ticking, I just count the hours
Stop tripping, I'm tripping off the powder
'Til then, fuck that, the world's ours
And they say, and they say
And they say, and they say
And they say, and they say
(21st-century schizoid man)
Colin Powells, Austin Powers
Lost in translation with a whole fuckin' nation
They say I was the abomination of Obama's nation
Well that's a pretty bad way to start the conversation
At the end of the day, goddammit, I'm killin' this shit
I know damn well y'all feeling this shit
I don't need your pussy, bitch, I'm on my own dick
I ain't gotta power trip, who you goin' home with?
How 'Ye doing? I'm surviving
I was drinking earlier, now I'm driving
Where the bad bitches, huh? Where y'all hiding?
I got the power make your life so exciting
Now this will be a beautiful death
I'm jumping out the window
I'm letting everything go
I'm letting everything go
Mmm, now this will be a beautiful death
I'm jumping out the window
I'm letting everything go
I'm letting everything go
Now this will be a beautiful death
Jumping out the window
Letting everything go
Letting everything go
You got the power to let power go?
(21st-century schizoid man)""", """It may not mean nothing to y'all,
Understand nothing was done for me,
So i don't plan on stopping at all,
I want this sh-t forever man, ever man, ever man,
I'm shutting sh-t down in the mall,
And telling every girl she the one for me,
And i aint even planning to call,
I want this sh-t forever man, ever man, ever man
Last name ever,
First name greatest,
Like a sprained ankle boy I ain't nuttin to play with,
Started off local, but thanks to all the haters,
I know G4 pilots on a first name basis,
And your city faded off the brown, Nino,
She insists she got more class, we know!
Swimming in the money come and find me, Nemo,
If i was at the club you know I ball'd, chemo,
Drop the mixtape that sh-t sounded like an album
Who'd have thought a country wide tour would be the outcome
Labels want my name beside the X like Malcolm
Everybody got a deal, I did it without one,
Yeah n-gga i'm about my business,
Killing all these rappers you would swear I had a hit list,
Everyone who doubted me is asking for forgiveness,
If you aint been a part of it at least you got to witness,
B-tches,
It may not mean nothing to y'all,
Understand nothing was done for me,
So i don't plan on stopping at all,
I want this sh-t forever man, ever man, ever man,
I'm shutting sh-t down in the mall,
And telling every girl she the one for me,
And i aint even planning to call,
I want this sh-t forever man, ever man, ever man
Ever ever, Mr West is in the Building,
Aint no question who about to kill em,
I used to have hood dreams,
Big fame, big chains,
I stuck my d-ck inside this life until that b-tch came,
I went hard all Fall like the ball teams,
Just so I can make it rain all spring,
Y'all seen my story my glory,
I had raped the game young,
You can call it statutory,
When a n-gga blow up they gon build statues of me
Old money Benjamin Button, whaat, nuttin,
Now superbad chicks giving me McLovin,
You would think I ran the world like Michelle's husband,
You would think these n-ggas would know me when they really doesn't
Like they was down with the old me, no you f-cking wasn't,
Your'e such a f-cking loser,
He didn't even go to class Bueller,
Trade the Grammy plaques just to have my granny back,
Lyrics courtesy of killerhiphop.com
Remember she had that bad hip like a fanny pack,
Chasing that stardom would turn you into a maniac,
All the way in Hollywood and I can't even act,
They pull their cameras out and God damn he snapped,
I used to want this thing forever y'all can have it back,
It may not mean nothing to y'all,
Understand nothing was done for me,
So i don't plan on stopping at all,
I want this sh-t forever man, ever man, ever man,
I'm shutting sh-t down in the mall,
And telling every girl she the one for me,
And i aint even planning to call,
I want this sh-t forever man, ever man, ever man
Ok, hello its da martian,
Space jam Jordan's,
I want this sh-t forever wake up and smell the Garden,
Fresher than the harvest
Step up to the target,
If i had one guess than I guess im just New Orleans,
And I will never stop like i'm running from the cops,
Hopped up in my car and told my chauffeur "to the top",
Life is such a f-cking roller coaster then it drops,
But what should I scream for this is my theme park,
My minds shine even when my thoughts seem dark,
Pistol on my side you don't wanna hear that thing talk,
Let the King talk, check the price and pay attention,
Lil Wayne thats what they got to say or mention,
Lyrics courtesy of killerhiphop.com
Im like Nevada in the middle of the summer,
I'm resting in the lead I need a pillow and a cover,
Ssshhh, my foots sleeping on the gas,
No brake pads no such thing as last- huh,
It may not mean nothing to y'all,
Understand nothing was done for me,
So i don't plan on stopping at all,
I want this sh-t forever man, ever man, ever man,
I'm shutting sh-t down in the mall,
And telling every girl she the one for me,
And i aint even planning to call,
I want this sh-t forever man, ever man, ever man
There they go, packin' stadiums
As Shady spits his flow,
Nuts they go, macadamian they go so ballistic whoa,
We can make them look like bozo's,
He's wondering if he should spit this slow,
F-ck no go for broke,
His cup just runneth over oh no
He aint had a buzz like this since the last time that he overdosed,
They've been waiting patiently for Pinnochio to poke his nose,
Back into the game and they know,
Rap will never be the same as before,
Bashin' in the brains of these hoes,
And establishing a name as he goes,
The passion and the flame is ignited,
You can't put it out once we light it,
This sh-t is exactly what the f-ck that i'm talking about when we riot,
You dealin with a few true villians
Who stand inside of the booth truth spillin,
Lyrics courtesy of killerhiphop.com
And spit true feelings, until our tooth fillings come flying up out of our mouths
Now rewind it
Payback muthaf-cka for the way that you doubted me so how's it taste?
When I slap the taste out your mouth with the bass so loud that it shakes the place,
I'm hannibal lecter so just in case your thinking of saving face,
You aint gonna have no face to save by the time Im through with this place,
So Drake...
It may not mean nothing to y'all,
Understand nothing was done for me,
So i don't plan on stopping at all,
I want this sh-t forever man, ever man, ever man,
I'm shutting sh-t down in the mall,
And telling every girl she the one for me,
And i aint even planning to call,
I want this sh-t forever man, ever man, ever man""", """Hold on, hold on, fuck that
Fuck that shit
Hold on, I got to start this motherfuckin' record over again
Wait a minute
Fuck that shit
Still on this motherfuckin' record
I'ma play this motherfucka for y'all
Ayy, y'all get some more drinks goin' on
I'll sound a whole lot better
Listen
Seeing you got ritualistic
Cleansin' my soul of addiction for now
'Cause I'm fallin' apart
Yeah, tension
Between us just like picket fences
You got issues that I won't mention for now
'Cause we're fallin' apart
Passionate from miles away
Passive with the things you say
Passin' up on my old ways
I can't blame you, no, no
Passionate from miles away
Passive with the things you say
Passin' up on my old ways
I can't blame you, no, no
Listen
Harder buildin' trust from a distance
I think we should rule out commitment for now
'Cause we're fallin' apart
Leavin'
You're just doing that to get even
Don't pick up the pieces, just leave it for now
They keep fallin' apart
Passionate from miles away
Passive with the things you say
Passin' up on my old ways
I can't blame you, no, no
Passionate from miles away
Passive with the things you say
Passin' up on my old ways
I can't blame you, no, no
Um, trying to think of the right thing to say""", """Baby you summertime fine, I let you get on top, I be the underline
I'm trying to get beside you like the number 9, dime
You fine as hell, I guess I met you for a reason, only time can tell
But well, I'm wondering what type of shit you wantin'
Do you like the finer things or you a simple woman
Would you drink with a nigga, do you smoke weed
Don't be ashamed, it ain't no thing, I used to blow trees
Gettin lifted, I quit but shit, I might get high with you
It's only fitting 'cause I'm looking super fly with you
A flower, you are powerful, you do something to me
'Cause, girl, I caught the vibe like you threw something to me
So I threw 'em back, now all my niggas hollerin, who was that
Oh boy, she bad nigga, what you 'bout do with that
I'm finna take you home, just sip a little patron
Now we zonin', baby you so fine
And can I hit it in the morning
And can I hit it in the morning
And can I hit it in the morning
The sun rising while you moanin'
And can I hit it in the morning
And can I hit it in the morning
And can I hit it in the morning
The sun rising while you moanin'
Uh, baby you winter time cold
The night is still young, drink that dinner wine slow
I'm trying to make the goose bumps on your inner thigh show
I'll let you beat me there as far as finish lines go
Yeah, and if you gotta leave for work,
I'll be right here in the same bed that you left me in
I love thick women 'cause my aunt, she rode equestrian
I used to go to the stables and get those kids to bet me
And I would always ride the stallions whenever she let me
I'm joking, I mean that thing is poking
I mean you kinda like that girl that's in the US Open
I mean I got this hidden agenda that you provoking
I got bath water that you can soak in
Things I could do with lotion
Don't need a towel, we could dry off in the covers
And when you think you like it, I promise you gon' love it
Yeah, when lights coming through the drapes and we both yawning
I roll over and ask if
I hit it in the morning
Can I hit it in the morning
Can I hit it in the morning
The sun rising while you moanin'
Can I hit it in the morning
Can I hit it in the morning
Can I hit it in the morning
The sun rising while you moanin'
Hey, hey, God Bless the child that can hold his own
God Bless the woman that can hold patron
God Bless the homegirl that drove us home
No strings attached, like a cordless phone
You see my intentions with you is clear
I'm learning not to judge a woman by the shit that she wears
Therefore, you shouldnt judge a nigga off of the shit that you hear
Get all defensive, apprehensive, all because my career
To be fair, I know we barely know each other and yeah
Somehow I wound up in your bed so where we headin' from here
Just say you're scared if you're scared but if you through frontin' we can do somethin'
And you know just what I'm talking about, tomorrow you'll be calling out
'Cause tonight we getting right into the wee morn'
Cooking nigga breakfast after sex is like a reward
Then I go my way and you think about me all day, that's just a warning
And can I hit it in the morning
And can I hit it in the morning
And can I hit it in the morning
The sun rising while you moanin'
And can I hit it in the morning
And can I hit it in the morning
And can I hit it in the morning
The sun rising while you moanin'""", """You good, T-Minus?
Niggas been countin' me out
I'm countin' my bullets, I'm loadin' my clips
I'm writin' down names, I'm makin' a list
I'm checkin' it twice and I'm gettin' 'em hit
The real ones been dyin', the fake ones is lit
The game is off balance, I'm back on my shit
The Bentley is dirty, my sneakers is dirty
But that's how I like it, you all on my dick
I'm all in my bag, this hard as it get
I do not snort powder, I might take a sip
I might hit the blunt, but I'm liable to trip
I ain't poppin' no pill, but you do as you wish
I roll with some fiends, I love 'em to death
I got a few mil' but not all of them rich
What good is the bread if my niggas is broke?
What good is first class if my niggas can't sit?
That's my next mission, that's why I can't quit
Just like LeBron, get my niggas more chips
Just put the Rollie right back on my wrist
This watch came from Drizzy, he gave me a gift
Back when the rap game was prayin' I'd diss
They act like two legends cannot coexist
But I'd never beef with a nigga for nothin'
If I smoke a rapper, it's gon' be legit
It won't be for clout, it won't be for fame
It won't be 'cause my shit ain't sellin' the same
It won't be to sell you my latest lil' sneakers
It won't be 'cause some nigga slid in my lane
Everything grows, it's destined to change
I love you lil' niggas, I'm glad that you came
I hope that you scrape every dollar you can
I hope you know money won't erase the pain
To the OGs, I'm thankin' you now
Was watchin' you when you was pavin' the ground
I copied your cadence, I mirrored your style
I studied the greats, I'm the greatest right now
Fuck if you feel me, you ain't got a choice
Now I ain't do no promo, still made all that noise
This shit gon' be different, I set my intentions
I promise to slap all that hate out your voice
Niggas been countin' me out
I'm countin' my bullets, I'm loadin' my clips
I'm writin' down names, I'm makin' a list
I'm checkin' it twice and I'm gettin' 'em hit
The real ones been dyin', the fake ones is lit
The game is off balance, I'm back on my shit
The Bentley is dirty, my sneakers is dirty
But that's how I like it, you all on my dick
I just poured somethin' in my cup
I've been wantin' somethin' I can feel
Promise I am never lettin' up
Money in your palm don't make you real
Foot is on they neck, I got 'em stuck
I'ma give 'em somethin' they can feel
If it ain't 'bout the squad, don't give a fuck
Pistol in your hand don't make you real
I'm dead in the middle of two generations
I'm little bro and big bro all at once
Just left the lab with young 21 Savage
I'm 'bout to go and meet Jigga for lunch
Had a long talk with the young nigga Kodak
Reminded me of young niggas from 'Ville
Straight out the projects, no fakin', just honest
I wish that he had more guidance, for real
Too many niggas in cycle of jail
Spending they birthdays inside of a cell
We coming from a long bloodline of trauma
We raised by our mamas, Lord we gotta heal
We hurting our sisters, the babies as well
We killing our brothers, they poisoned the well
Distorted self image, we set up to fail
I'ma make sure that the real gon' prevail, nigga
I just poured somethin' in my cup
I've been wantin' somethin' I can feel
Promise I am never lettin' up
Money in your palm don't make you real
Foot is on they neck, I got 'em stuck
I'ma give 'em somethin' they can feel
If it ain't 'bout the squad, don't give a fuck
Pistol in your hand don't make you real
Money in your palm don't make you real
Pistol in your hand don't make you real
Money in your palm don't make you real"""]

artists = ["Lauryn Hill", "Nas", "Tupac", "Eminem", "Biggie", "Wu-Tang", "Kendrick", "Jay-Z", "Snoop", "Kanye", "Drake", "J-Cole"]



new_process = False  # Change to True if we need to download nltk modules and change withing the "if new_process" code block

if new_process:

  nltk.download('punkt')
  nltk.download('stopwords')
  nltk.download('WordNetLemmatizer')
  nltk.download('PorterStemmer')

########################################################### START OF FUNCTION CODE BLOCK #########################################################################

# Function for removing any newline characters from corpus
def remove_newlines(strings):
    for i, s in enumerate(strings):
        
        # Replace all newline characters with nothing
        s = s.replace("\n", " ")
        strings[i] = s

    return strings

# Function for removing all escape characters from corpus
def remove_escape_characters(strings):
    for i, s in enumerate(strings):
        # Use the `translate()` method to remove all escape characters
        s = s.translate(str.maketrans('', '', string.punctuation))
        strings[i] = s
    return strings


def tokenize_and_remove_stop_words(lyricals):
    # Split the lyrics into individual words
    
    words = nltk.word_tokenize(lyricals)
    
    # Remove any punctuation characters from the words
    words = [word for word in words if word.isalpha()]
    
    # Get a list of stop words

    stop_words = [gensim.parsing.preprocessing.remove_stopwords(lyrics) for lyrics in words] # nltk.corpus.stopwords.words("english")
    ll = []
    for wordss in stop_words:
        if wordss != '':
          ll.append(wordss)

    return ll

# tokenized_lyrics[0]
# remove_lyrics = ['doh','aaaaaow','ta','na','wan']

# Function for removing words in a song
def remove_words(array, words_to_remove):

    # Create a new list to store the modified words
    modified_words = []

    # Iterate through the list of words
    for word in array:
        # If the word is not in the list of words to remove, add it to the modified list
        if word not in words_to_remove:
            modified_words.append(word)

    # Join the modified words into a single string and return it
    return modified_words


def tag_parts_of_speech(word_array):
    
    # Use the nltk library to perform POS tagging
    tagged_words = nltk.pos_tag(word_array)

    # Return the list of tagged words
    return tagged_words

def lematize_and_stem(lyrics):

  #nltk.download('wordnet')
  lemmatizer = WordNetLemmatizer()
  stemmer = PorterStemmer()
  preprocessed_lyrics = []
  for lyric in lyrics:
      lemmatized_lyric = [lemmatizer.lemmatize(word) for word in lyric]
      stemmed_lyric = [stemmer.stem(word) for word in lemmatized_lyric]
      preprocessed_lyrics.append(stemmed_lyric)

  return preprocessed_lyrics

# It's all well and good that we have counted the number of times these different parts of speech have appeared but we need to see if there is a chnage in the amount of times these POS appear each decade
# Index position 0 and 2 have 1 less song therefore 2010s -> [0:8], 1990s -> [19: 27]

# Decade indecies must be in acending order. So the affected indecies list cannot have a later decade come before an earlier decade

def decade_pos_tagger(array, decade_length=[]):

  # array for storing the songs in each decade
  song_decade = []
  
  # n is just the number of songs in "array"
  # x is just the number of decades we have considered -> 0 - the xth decade 
  n = 0
  x = 0
  
  # Add the starting decade's array slot to the container
  song_decade.append([])

  # While we have not considered all the songs in the list, keep going.
  while n < (len(array) - 1):

    
    for i in range(decade_length[x]):
      
      # Add the song to the relevant list of songs in the correct decade
      song_decade[x].append(array[n])
      n += 1
    
    # Increment x so that we are considering the next decade at the beginning of the next itteration
    x += 1


    # So long as we haven't already considered the last song we will need to add another array for the next decade
    if n < (len(array) - 1):

      # Add that slot to the list
      song_decade.append([])

  # Array to store pos distribution
  pos_dist = []

  for decades in song_decade:

    pos_dist.append([])

  return(song_decade)

# Function should return the number of each type present within a 2d array where
# the first dimension is the songs persent in passed deacade and the second is the song lyrics of each song
def pos_tag_decade(lyrics=[], decade_separated=True, artists_names = ["Lauryn Hill", "Nas", "Tupac", "Eminem", "Biggie", "Wu-Tang", "Kendrick", "Jay-Z", "Snoop", "Kanye", "Drake", "J-Cole"], n_songs=2):
  
  pos_dict = {}
  part_type = []
  part_of_speech = [] 
  # word = []
  index = 0
  m = 0

  list_of_tagged_words = []

  for songs in lyrics:

   list_of_tagged_words.append(tag_parts_of_speech(songs))
  # Firstly we need to track the POS distribution and the frequency of specific words

  if decade_separated:

    for songs in  list_of_tagged_words:

      for words in songs:

        # if we have this type of part of speech in the list then increment the count of this type of part of speech
        if words[1] in part_type:
          index = part_type.index(words[1])
          part_of_speech[index] += 1
          
      
        # Else we need to append a value of 1 to the POS count list since this is the first time it is appearing 
        else:
          
          # Add the type of part of speech to the list
          part_type.append(words[1])

          # append 1 the POS count list
          part_of_speech.append(1)
      
      # 
      # part_type -> stores type of POS present in list
      # part_of_speech -> keeps track how many times pos[n] appears where n is some arbitrary index within the indecies that exist in the list
      # index -> the index value of part of speech being considered
      for i  in range(len(part_type)):

        pos_dict[f"{part_type[i]}"] = part_of_speech[i]

  else:
    
    artist_dict = {}
    temp_array = []
    
    x = 0
    
    for songs in list_of_tagged_words:

      for pos in songs:
        
        # if the POS is already in the pos array
        if pos[1] in part_type:
          index = part_type.index(pos[1])
          part_of_speech[index] += 1
          
        else:

          # Add the type of part of speech to the list
          part_type.append(pos[1])

          # append 1 the POS count list
          part_of_speech.append(1)

      
      for i in range(len(part_type)):

        # creating a log of number of part types in dict
        pos_dict[f"{part_type[i]}"] = part_of_speech[i]
      
      # now we need to log it as a specific artists part type and delete the endties 

      
      x  += 1
      
      if (x % n_songs) == 0 and (x != 0):
        # then we are onto the next artist 
        artist_dict[f"{artists_names[m]}"] = [pos_dict]

        # clear variables for next artist
        pos_dict = {}
        part_type = []
        part_of_speech = [] 
        m += 1
      

    ###### at the end have artists store a dictionary of what their pos distribution looks like
    
  if decade_separated:
    return pos_dict 

  else: 

    return artist_dict

def topic_model(n_topics=10, process=True, dictionary1=pre_processed_hpop_lyrics, dictionary2=pre_processed_lyrics):

  if process:
    cleaned_lyrics1 = remove_escape_characters(dictionary1)
    cleaned_lyrics2 = remove_escape_characters(dictionary2)

    cleaned_lyrics1 = remove_newlines(dictionary1)
    cleaned_lyrics2 = remove_newlines(dictionary2)

  else:
    cleaned_lyrics1 = dictionary1
    cleaned_lyrics2 = dictionary2


  processed_lyrics1 = []
  processed_lyrics2 = []
  tokenized_lyrics1 = []
  tokenized_lyrics2 = []

  for songs in dictionary1:
    tokenized_lyrics1.append(tokenize_and_remove_stop_words(songs))
    
  for songs in dictionary2:
    tokenized_lyrics2.append(tokenize_and_remove_stop_words(songs))


  processed_lyrics1.append(lematize_and_stem(tokenized_lyrics1))


  processed_lyrics2.append(lematize_and_stem(tokenized_lyrics2))

  from gensim import corpora
  from gensim.models import LdaModel

  topics1 = []
  topics2 = []
  
  for i in range(len(processed_lyrics1)):
    topics1.append([])
  # Create a dictionary from the preprocessed lyrics
    dictionary = corpora.Dictionary(processed_lyrics1[i])
    # Create a bag of words representation of the lyrics
    
    bow_corpus = [dictionary.doc2bow(lyric) for lyric in processed_lyrics1[i]]

    # Fit the LDA model to the bag of words representation
    lda_model = LdaModel(bow_corpus, num_topics=n_topics, id2word=dictionary)
    
    # Print the topics
    for topic_id, topic in lda_model.print_topics():
      topics1[i].append("Topic {}: {}".format(topic_id, topic))

  for j in range(len(processed_lyrics2)):
    topics2.append([])
  # Create a dictionary from the preprocessed lyrics
    dictionary = corpora.Dictionary(processed_lyrics2[j])

    # Create a bag of words representation of the lyrics
    bow_corpus = [dictionary.doc2bow(lyric) for lyric in processed_lyrics2[j]]

    # Fit the LDA model to the bag of words representation
    lda_model = LdaModel(bow_corpus, num_topics=n_topics, id2word=dictionary)

    # Print the topics
    for topic_id, topic in lda_model.print_topics():
      topics2[j].append("Topic {}: {}".format(topic_id, topic))
      # print("Topic {}: {}".format(topic_id, topic))

  return topics1, topics2

def sentiment_analyse(N_songs_per_artist=2,decade_separated=True, decade_length=[9,10,9,10,10,10,10,10,10,10,10,10,8],artists=artists, decades = ["2010s","2000s", "1990s", "1980s", "1970s","1960s", "1950s", "1940s", "1930s", "1920s", "1910s", "1900s", "1890s"],process=True, dictionary1=pre_processed_hpop_lyrics, dictionary2=pre_processed_lyrics):

  def return_keys(key_type, array):
      x = 0
      n = 0
      
      key_list = []
      for decade in array: # for decade
        t_l = []
        for songs in decade: # For songs in decade
          
          t_l.append(songs[f"{key_type}"])

        
        key_list.append(t_l)

      
      return key_list

########################## DO NOT CHANGE CODE UNLESS YOU ARE EDITING DECADE SENTIMENT ANALYSIS ##################################################################
  if decade_separated:
    if process:
      cleaned_lyrics1 = remove_escape_characters(dictionary1)
      cleaned_lyrics2 = remove_escape_characters(dictionary2)

      cleaned_lyrics1 = remove_newlines(dictionary1)
      cleaned_lyrics2 = remove_newlines(dictionary2)

    else:
      cleaned_lyrics1 = dictionary1
      cleaned_lyrics2 = dictionary2


    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    analyzer = SentimentIntensityAnalyzer()
   
    decade_songs = {}
    x = 0
    n = 0
    for i in range(len(decades)):

      decade_songs[f"{decades[i]}"] = []

    for songs in dictionary2:

      if (x % 10) == 0 and (x != 0):
         n += 1
        
      decade_songs[f"{decades[n]}"].append(songs)
      x += 1

    x = 0
    n = 0

    for i in range(13):
      decade_songs[f"{decades[i]}"] = [dictionary2[x + 10*n] for x in range(decade_length[i])]
      n += 1
    # KEYS FOR LIST IS DECADES (DICT1) OR ARTIST (DICT2) NAMES
    decades_scores = {}
  
    for decades in decade_songs:
      equal = False
      while not equal:

        if len(decade_songs[f"{decades}"]) < 10:
 
          decade_songs[f"{decades}"].append("null")

        else:
          equal = True

    t_2 = []
    x = 0
    for decade in list(decade_songs.keys()):
      temp_list = []
      t_2.append([])
    
      for i in range(len(decade_songs[f"{decade}"])):

        song = decade_songs[f"{decade}"][i]
        score = analyzer.polarity_scores(song)    
        temp_list.append(score)

      
      for items in temp_list:
        t_2[x].append(items)
      x += 1

      decades_scores[f"{decade}"] = temp_list


    p_key = return_keys("pos", t_2)
    n_key = return_keys("neg", t_2)
    neu_key = return_keys("neu", t_2)
    comp_key = return_keys("compound", t_2)
    comp_key2 = []
    
    p_key = np.array(p_key)
    n_key = np.array(n_key)
    neu_key = np.array(neu_key)
    comp_key = np.array(comp_key)

    

    labels = decades_scores.keys()

    fig, ax = plt.subplots()
    width = 0.4
    colors = ["crimson", "purple", "limegreen", "gold", "blue", "red", "black", "brown", "yellow", "pink","teal" ,"silver" ,"orange" ]
    
    
    for i, l in enumerate(labels):
  

      x = np.ones(10) * i + (np.random.rand(10)*width-width/2.)
     
      ax.scatter(x, comp_key[i], color=colors[i], s=25)
      mean = comp_key[i].mean()
      ax.plot([i-width/2., i+width/2.], [mean,mean], color="k")

    
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)

    plt.show()

    exit()

########################## END OF DECADE SENTIMENT ANALYSIS #####################################################################################################
  
########################## DO NOT CHANGE CODE UNLESS YOU ARE EDITING ARTIST SENTIMENT ANALYSIS ##################################################################
  else:


    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    analyzer = SentimentIntensityAnalyzer()
   
    decade_songs = {}
    x = 0
    n = 0
    for i in range(len(artists)):

      decade_songs[f"{artists[i]}"] = []

    for songs in dictionary1:

      if (x % N_songs_per_artist) == 0 and (x != 0):
         n += 1
        
      decade_songs[f"{artists[n]}"].append(songs)
      x += 1

    x = 0
    n = 0

    for i in range(len(artists)):
      decade_songs[f"{artists[i]}"] = [dictionary1[x + N_songs_per_artist*n] for x in range(N_songs_per_artist)]
      n += 1
    # KEYS FOR LIST IS DECADES (DICT1) OR ARTIST (DICT2) NAMES
    decades_scores = {}
    
    for decades in decade_songs:
      equal = False
      while not equal:

        if len(decade_songs[f"{decades}"]) < N_songs_per_artist:
 
          decade_songs[f"{decades}"].append("null")

        else:
          equal = True

    t_2 = []
    x = 0
    for decade in list(decade_songs.keys()):
      temp_list = []
      t_2.append([])
    
      for i in range(len(decade_songs[f"{decade}"])):

        song = decade_songs[f"{decade}"][i]
        score = analyzer.polarity_scores(song)    
        temp_list.append(score)

      
      for items in temp_list:
        t_2[x].append(items)
      x += 1

      decades_scores[f"{decade}"] = temp_list


    p_key = return_keys("pos", t_2)
    n_key = return_keys("neg", t_2)
    neu_key = return_keys("neu", t_2)
    comp_key = return_keys("compound", t_2)
    comp_key2 = []
    
    comp_key = np.array(comp_key)
    
    labels = decades_scores.keys()
    for songs in comp_key:
      print(songs[0], " & ", songs[1] )
    fig, ax = plt.subplots()
    width = 0.4
    colors = ["crimson", "purple", "limegreen", "gold", "blue", "red", "black", "brown", "yellow", "pink","teal" ,"silver" ,"orange" ]
    
    
    for i, l in enumerate(labels):

      x = np.ones(N_songs_per_artist) * i + (np.random.rand(N_songs_per_artist)*width-width/2.)
     
      ax.scatter(x, comp_key[i], color=colors[i], s=25)
      mean = comp_key[i].mean()
      ax.plot([i-width/2., i+width/2.], [mean,mean], color="k")

    
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)

    plt.show()

    exit()
      
def process_music(pre_processed_data=pre_processed_lyrics, process=True, print_dist=False, decade_length=None, decade_separated=True, print_process=False):

  if (decade_separated==True) & (decade_length is None):
    print("Please set decade_separated to False or specify the number of songs in each deacade")
    raise TypeError
    

  if process:
    cleaned_lyrics = remove_escape_characters(pre_processed_data)

    cleaned_lyrics = remove_newlines(pre_processed_data)

    
  
    if print_process:
      for songs in cleaned_lyrics:
      
        print("'", songs ,"'", ",")


    time.sleep(10)

  else:

    cleaned_lyrics = pre_processed_data

  time.sleep(2)

  tokenized_lyrics = []
  
  for songs in cleaned_lyrics:

    tokenized_songs = tokenize_and_remove_stop_words(songs) # returns a list of tokenized lyrics
    tokenized_lyrics.append(tokenized_songs) # We then create a list of lists where the inner list is a list of tokenized lyrics
    

  if decade_separated:
    try:
      decade_separated = decade_pos_tagger(tokenized_lyrics, decade_length)
    except TypeError:
      print("Invalid value specified for decade length. Please provide a list of lengths for the number of songs in each decade. \nExited with status 0")
      exit()

  else:
    # in this code block we need to skip the decade separation step and just do pos tagging for each song, re-organize the distribution and return that. 
    i = 0
    
    pos_dist1 = pos_tag_decade(tokenized_lyrics, decade_separated=False)

    sorted_pos_dist1 = []

    # print(pos_dist1["Lauryn Hill"][0].items())
    # exit()


    for entries in pos_dist1:
      sorted_pos_dist1.append(sorted(pos_dist1[f"{entries}"][0].items(), key=lambda item: item[1]))
      # sorted_pos_dist1.append(sorted(entries[0].items(), key=lambda item: item[1]))

    # now we have a sorted list of POS for each artist so now we need to put it back into dict form

    artist_dict = {}
    pos_dict = {} # Needs reseting for every artist
    artist_list = []
    i = 0         # Must be itteratively increased 

    for entries in pos_dist1:

      artist_list.append(entries)


    for artists in sorted_pos_dist1:

      # Create a log of the number of occurences of specific pos for this artist
      for pos in artists:

        pos_dict[f"{pos[0]}"] = pos[1]

      artist_dict[f"{artist_list[i]}"] = [pos_dict]

      i += 1
      pos_dict = {}

    return(artist_dict)

  pos_dist = []
  i = 0
  for decades in decade_separated:
    pos_dist.append(pos_tag_decade(decades))
    # print(pos_dist)
    # print(len(list(pos_dist[i].keys())))
    i += 1

  sorted_pos_dist = []

  for entries in pos_dist:

    sorted_pos_dist.append(sorted(entries.items(), key=lambda item: item[1]))

  # free up memory
  del tokenized_lyrics
  del pos_dist
  del decade_separated
  del pre_processed_data

  pos_dist = []
  i = 0

  for decades in sorted_pos_dist:
    temp_dict = {}
    for pos in decades:
      temp_dict[f"{pos[0]}"] = pos[1]

    pos_dist.append(temp_dict)

   
  if print_dist:
    for decades in pos_dist:
      print(decades)

  return pos_dist


  

############################################### END OF FUNCTION CODE BLOCK #######################################################################################






############################################### START OF DATA MANIPULATION ########################################################################################





# proc1 = process_music(pre_processed_data=pre_processed_hpop_lyrics, print_dist=False,decade_separated=False, process=True)


# proc2 = process_music(pre_processed_data=pre_processed_lyrics,print_dist=False,process=False,decade_separated=True, decade_length=[9,10,9,10,10,10,10,10,10,10,10,10,10] )

# h, p =topic_model(n_topics=20)
# print(process_music(decade_length=[9,10,9,10,10,10,10,10,10,10,10,10,10]))

# print("hip hop topic modeling: ",h,"\n", "\n", "Decade topic modelling: ", p, "\n", "\n")

# print(process_music(pre_processed_data=pre_processed_hpop_lyrics, decade_separated=False,decade_length=[9,10,9,10,10,10,10,10,10,10,10,10,10]))
# sentiment_analyse(decade_separated=False)





