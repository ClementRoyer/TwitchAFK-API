<h1 align="center">

  <br>

  <img src="https://thumbs.gfycat.com/ThankfulFearlessHochstettersfrog-max-1mb.gif" alt="Work in progress" width="200">
  <br>
  Twitch AFK API
  <br>
</h1>

<h4 align="center">My small <a href="" target="_blank">Description</a>.</h4>

<div align="center"><sub> Version <a href="version">TOO EARLY</a></sub></div>
<br>
<div align="center"><sub>Because this application use personal information like Twitch token, this is not destined to public deployment. It's better to use it on a private server.</sub></div>

<br>

<div align="center">

[![0](https://img.shields.io/badge/Home-black.svg?style=flat&logo=Markdown&logoColor=white&labelColor=black&color=black)][Main-Readme] [![0](https://img.shields.io/badge/Online-Documentation-black.svg?style=flat&logo=Postman&logoColor=FF6C37&labelColor=black&color=black)][Postman-Doc] [![0](https://img.shields.io/badge/Changelog-black.svg?style=flat&logo=MarkDown&labelColor=black&color=black)][ChangeLog]

<!-- TOC -->
<p align="center">
  <a href="#todo">Todo</a>
  <!-- • <a href="#proof"></a> -->
</p>

<!-- omit in toc -->
## 

</div>


## Todo

- viewer bot
  - [x] argv[1] = streamer argv[2] = token
  - [x] Create file `$token_$streamer.log` (could be a filename too long)
    - To get current bot logs.
  - [x] Create file `$token_$streamer_log.log` (could be a filename too long)
    - To get only the last log of the current bot.
  - [ ] to json {coins: , bet_placed: , bet_won: , bet_balance: , auto_collect_balance: }
  - [ ] View stream
  - [ ] Collect coins & chest
  - [ ] Find bet & place bet
    - [ ] sleep until last moment to make sure bet on the best odd
  - [ ] Find when a bet end, get stats

- API
  - [ ] Login/Create account, route.
    - [ ] Generate JWT
    - [ ] Check if username already taken
  - [ ] Set/Refresh user's twitch token, route.
  - [x] Start viewing, route.
    - [ ] streamer's channel in url.
  - [x] Get last update of the bot, route.
  - [x] Get full log of the bot.
    - [ ] Maybe extract it to CSV
  - [ ] Stop the bot.

- Database (using tinydb (json file))
  - [ ] User table
    - username
    - password
    - twitch token

- Cool feature
  - [ ] Emergency stop, click on button and stop all bots of the server.
    - Dont have any use case, just feal like could be helpfull.
  - [ ] Bet able to set different key for different viewer
    - In case someone is ban one stream and use an other account to watch it he cas put both in this app.
  - [ ] Be able to get usable stats out of the bot
    - [ ] View count
    - [ ] Stream title
    - [ ] all bets logs
    - [ ] bet balance over time
    - [ ] more
  - [ ] Be able to chose the bet strategy
    - [ ] Greedy : bet x% of your balance to highest odd
    - [ ] Greedy-fix : bet X coins to highest odd (take balance if X > balance)
    - [ ] moderate : bet x% of your balance to lower odd
    - [ ] moderate-fix : bet X coins to lower odd (take balance if X > balance)


<!-- footer -->

<!-- omit in toc -->
#

<div align="center"> 
  <sub>Built with ❤︎ by
  <a href="https://www.linkedin.com/in/cl%C3%A9ment-royer/">Clément ROYER</a> and
  <a href="https://github.com/ClementRoyer/markdown-template/graphs/contributors">
    contributors
  </a>

<br><br>

[![0](https://img.shields.io/badge/Usage_Policy-black.svg?style=flat&logo=Markdown&logoColor=white&labelColor=black&color=black)][Policy] [![0](https://img.shields.io/badge/Usefull_link-black.svg?style=flat&logo=Postman&logoColor=FF6C37&labelColor=black&color=black)][Postman-Doc] [![0](https://img.shields.io/badge/ciemrnt-black.svg?style=flat&logo=Twitter&labelColor=black&color=black)][twitter] [![0](https://img.shields.io/badge/Clément_royer-black.svg?style=flat&logo=Linkedin&labelColor=black&color=black)][Linkedin] 
</div>

<!-- omit in toc -->
# 

![0](https://img.shields.io/badge/Author(s):-black.svg?style=flat&logoColor=white&labelColor=gray&color=gray) ![0](https://img.shields.io/badge/Clément_ROYER-black.svg?style=flat&logoColor=white&labelColor=black&color=black)


<!-- links -->
[Main-Readme]: .
[Policy]: ./LICENSE
[Postman-Doc]: .
[ChangeLog]: .
[Twitter]: https://www.twitter.com/ciemrnt
[Linkedin]: https://www.linkedin.com/in/cl%C3%A9ment-royer/