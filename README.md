# dragonmoneyscript
https://t.me/drgn_script

Софт больше не актуален, способ фарма промокодов на DragonMoney пофикшен
софт скорее всего больше не работает

всем пака


инструкция по установке? софта который больше не работает? ну ладно

git clone https://github.com/trcmzng/dragonmoneyscript.git
cd dragonmoneyscript
pip install -r requirements.txt
python drgn1.5.2.py

он запустится и закроется

надо открыть конфиг в блокноте и делать все дальше по инструкции
4. зайди на my.telegram.org залогинься в свой ТГ, потом клик по API development tools
5. там нужно создать приложение, в App title и Short name = script, платформа Desktop
6. save changes, появится api id и  api hash, скопировать их и вставить в нужные поля в файле config.ini (api_id , api_hash)
7. channels = каналы через запятую, которые будут просматриваться скриптом,   например берем ссылку на канал (https://t.me/kanal25253),  и убираем часть "https://t.me/",  чтобы получилось например: channels = kanal25253,drgn,итд  без пробелов!
8. user_id брать тут https://t.me/getmyid_bot
9. profile = путь до профиля (чтоб получить переходим в хроме по ссылке chrome://version там появится Путь к профилю его надо скопировать и заменить последний символ "\" на запятую пример: profile = C:\\Users\\Администратор\\AppData\\Local\\Google\\Chrome\\User Data,Default)
10. mode не менять
11 . @drgn_scr_bot нажать старт

python drgn1.5.2.py

