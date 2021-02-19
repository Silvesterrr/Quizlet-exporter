# Quizlet-exporter
Quizlet-exproter is a python command-line program designed to download and export sets to .txt format.

If you want to download few quizlet sets at once you can use this program.
# Usage
`Quizlet-exporter.py [link] [username] [password] [before_word] [number] [separator] [save_file_path]` <br><br>
If you don't have `before_word` replace it with `null`
# Example
For example if you want to have all words from Unit 12 with comma as a separator
![alt text](https://github.com/Silvesterrr/Quizlet-exporter/blob/main/example.PNG?raw=true)
You can do something like this <br>
`Quizlet-exporter.py https://quizlet.com/MacmillanPolska/folders/repetytorium-osmoklasisty/sets username password Unit 12 , ./`<br>
And you get something like this:<br>
```
być samotnym,be lonely
mieć z czymś związek,be related to sth
starszy,elderly
zgłoszenie (np. w konkursie),entry
odłożyć coś na następny dzień,leave sth until tomorrow
być rzeczą powszechnie znaną,be common knowledge
zgadzać się z czymś,be on board with sth
być w toku,be work in progress
udzielać jasnych wskazówek,give explicit instructions
wyjawiać,give sth away
utrudniać,hamper
trafić na pierwsze strony gazet,hit the headlines
wymagać poprawek,need refinements
wzajemne oskarżenia,recriminations
niechęć,reluctance
bez sięgania po coś,without recourse to sth
---,---
stosować technologię,apply technology
doświadczać czegoś w prawdziwym życiu,experience things hands-on
przeprowadzać skomplikowane operacje,perform complex surgeries
wydłużać ludzkie życie,prolong human life
być zdolnym do czegoś,be capable of something
być przed czymś postawionym,be faced with sth
wykrywać oznaki przyszłych chorób,detect signs of oncoming diseases
powstrzymywać rozwój czegoś,deter sth from developing
dorównywać poprzednim pokoleniom,emulate the past generations
polepszać geny,enhance genes
urzeczywistnić wizję,materialise a vision
dążyć do czegoś,strive for sth
z zadowoleniem przyjmować osiągnięcie,welcome a development
bardzo czegoś pragnąć,yearn for sth
---,---
być zepsutym,be out of order
zepsuć się,break down 
...
```
# Requirements and Other
Make sure that you have installed selenium ( `pip install selenium` ), and chrome browser. If the chromedriver added in the files won't work download it from this webside https://chromedriver.chromium.org/downloads (version equal to your chrome version). Chromedriver have to be in desame folder as the python file.  
If you worried about me 'stealing' your account you can just make a fake one. unfortunately quizlet shows only about half of all 'words' if you're not logged in.  
Hope You like it. If you have any problems please contact me at: `sylwesterjarosz50@gmail.com`
