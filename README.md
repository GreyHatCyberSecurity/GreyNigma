# ENGLISH DOCUMENTATION
### Welcome to GreyNigma documentation page.


##### GreyNigma is a free online encryption machine that lets you convert plaintext into ciphertext by replacing the input characters with {digits}.
**GreyNigma** consists of the number encryption module and the **Gipher** module - letter-by-letter shifting of all characters of the string by a certain order (up or down).

**Examples of encrypted messages: {68446788}{333831545}{912483291}{972471385}{807134099}{964078423} <- Encrypted with GreyNigma + Gipher (standard module).**
*Hejkv! <- Encrypted with Gipher, without digit module.

The values are generated using an arbitrary **SeedKey**, a kind of **password** that must be kept in the strictest secret.
This password should be known only to the interlocutors.
The SeedKey sets the first number in the random generation, thus creating the same values with the same SeedKey value.

#### The encryption is done as follows:
1. **First, if the string contains digits, they are replaced by eigenvalues**
For example, 1 turns into (oone), 2 turns into (twoo) and so on.
The values in brackets are purposely written incorrectly; this is done to bring the length of all the digits in the alphabetic version to 4.
Thus, in encrypted form, there will be no difference in length between 1 and, say, 8.

2. **Next, there is a letter-by-letter shift of all the characters using the Gipher module.**
Gipher works like this:
 - **SeedKey** is used to create a list of numbers 10,000 numbers long.
 - Each character of the entered string is shifted accordingly with the created number.
 - For example, the input message **Hello**, the first 5 numbers generated are: 0, 0, -2, -1, 7
 - **'H'** is shifted by **0**, **'e'** is shifted by **0**, **'l'** is shifted by **-2** positions, **'l'** is shifted by **-1** position and **'o'** is shifted by **7** positions
 - The output is an encrypted message: **Hejkv**.
 - The decryption process happens, oddly enough, in the exact opposite way: **numbers are taken the same**, but the sign before the shift is the opposite.
The reliability of this module is that:
 - When it is used, the frequency analysis becomes completely meaningless, as the letters are not replaced by any special letters.
 - The number of variations of the message is equal to its length. This means that the word **Hello** has **26^5** (26 - number of letters in the English alphabet, 5 - message length) variations of how the message can look like, and only one correct one, which makes the common crude search process virtually meaningless, because just imagine how many words can be from 5 letters. Not bad, is it?

3. After encryption by the Gipher module, **the message can be reversed "mirrored"**, or it can remain as it is. This is controlled by the same randomly generated parameter.

4. **Each character in the message is replaced by its corresponding numeric value in curly brackets.**
Example:
 - We have a message Hejkv, let's say it was expanded and turned into vkjeH
 - The letter **H** is set to **15**, the letter **e** to **2**, the letter **j** to **8**, the letter **k** to **14**, and the letter **v** to **81**
 - After swapping, we get the message : **{81}{14}{8}{2}{15}**
 - Such values are generated in the same way, using the **SeedKey**.

I think we don't need to explain that the decryption happens in exactly the same way, only in the exact opposite order :)
In case the SeedKey is entered incorrectly - the decryption will fail and the wrong values will be printed.

#### GreyNigma is equipped with a number of powerful protection algorithms:
1. **Separate strings**.
There are 3 string variations for a complete message : 1st fake string, original string and 2nd fake string.
How does it work?
 - Each string has its own 225 values ((26 small letters + 26 capital letters + 23 characters) * 3 random variations), which cannot be the same as the other string.
 - You can write really important data into the first "fake" line, and you can write messages with useless information into the rest (original and second fake lines), or leave them empty (in case a line is empty, a random character set is generated instead, for example Y!NJP??U#*&!, which will obviously confuse an intruder).

2. **Salts and delimiters**.
Salts are so called "ballast" characters, which are added to every full-fledged message. They are random {digits}, which create the illusion of the presence of any other characters in the message, however, if decrypted correctly - evaporate. A full 10-character message on each line can turn into a 50-character, or even 70-character encrypted message.

3. **Separators** are a special character that separates the strings (first fake, original and second fake) from each other in order to make it easier to read when decrypting correctly. Just like a salt, it has its own unique meaning, which, if deciphered incorrectly, may inadvertently turn into some letter, confusing the hacker.

### USAGE:
GreyNigma is presented as an online service (API) that accepts requests with message and seedKey parameters and returns the value of the encrypted/decrypted message.
The repository includes a console version (universal) and a graphical version that runs on systems with a graphical interface. It depends on the Python library Tkinter.
The interface of both versions has been made as accessible and understandable as possible for both beginners and experienced users.
Note that both graphical and console versions of GreyNigma accept SeedKey values of STRING data type!


# ANSWERS TO FREQUENTLY ASKED QUESTIONS
---------------------
### 1. Is it safe?
---------------------
It's hard to answer unequivocally.
Nothing in the world is perfect, especially now, in the age of information technology
Anything can be hacked, even the most secure algorithms are not immune to multiple brute
by supercomputers.
This does not mean, however, that the algorithm is not secure.
Information is considered secure when its theft costs more than the information itself.
There are two sides to this coin:
One person will spend a lot of time and effort to hack a one-page site
Another person, with quantum supercomputers, won't even bother to hack a government website.
It's all relative.
GreyNigma is, first of all, a technology that gives you unlimited imagination in terms of improving it
You can create your own lines, add "empty" elements, increasing the total length of the message, everything is limited only by your imagination :)
GreyNigma is initially equipped with a good level of reliability, which you can improve with your knowledge and imagination by customizing it to your own needs.
---------------------
### 2. Where can I use GreyNigma? There is strong message encryption, so what's the point?
---------------------
Nowadays, during a big surveillance, it's hard to say how reliable this or that service is.
If you read the privacy policies, you realize that the encryption offered is a very relative thing.
On the one hand, yes, the conditional viber/whatsapp are secure, but their policies imply the "release" of your messages at the request of, say, law enforcement.
Consequently, your messages can be magically decrypted contrary to all oaths of end-to-end encryption, which precludes third-party decryption of messages no matter what.

With GreyNigma, you can exchange messages even with untrustworthy services, even if they explicitly say that they will leak your messages to everyone. Let them leak the numbers to GreyNigma :)
It's a kind of steganography, which will save your messages from being leaked to any scoundrels who are encroaching on your legal right to privacy and confidentiality of personal correspondence, guaranteed by any law.
---------------------
### 3. What characters are supported?
---------------------
All English letters are supported, as well as !@'#%^:;&?*()-_=+[]/,
Support for numbers is ambiguous here.
Digits are converted to letters, i.e. 1 is replaced by 'oone', 2 by 'twoo' and so on.
This is done because if digits were converted to digits then there would be a complete collapse when encoding because digit values of the characters would be changed to the same digits, then after that to more digits and so on.
---------------------
### 4. What is the maximum message length?
---------------------
The maximum length of a single line is 10,000 characters. Accordingly, for a full message, 30,000 characters.

---------------------
### 5. I found a bug/vulnerability/I have questions, where do I go?
---------------------
If you have found any bug, vulnerability, don't understand any aspect of the work, or have ideas/suggestions, feel free to contact us:
Email: **greyhatfeedback@protonmail.com**
Telegram: **@greyhatfdbot**


The API (https://greynigma.herokuapp.com/) manual is laid out in a separate document API_DOCS in two languages - English and Russian.





# РУССКАЯ ДОКУМЕНТАЦИЯ
### Добро пожаловать на страницу документации GreyNigma.


##### GreyNigma - это бесплатная онлайновая шифровальная машина, позволяющая преобразовывать открытый текст в шифрованный путем замены входных символов на {цифры}.
**GreyNigma** состоит из модуля шифрования чисел и модуля **Gipher** - побуквенного сдвига всех символов строки на определенный порядок (вверх или вниз).

**Примеры зашифрованных сообщений: {68446788}{333831545}{912483291}{972471385}{807134099}{964078423} <- Зашифровано с помощью GreyNigma + Gipher (стандартный модуль).**.
*Hejkv! <- Зашифровано с помощью Gipher, без циферного модуля.

Значения генерируются с помощью произвольного **SeedKey**, своего рода **пароля**, который должен храниться в строжайшем секрете.
Этот пароль должны знать только собеседники.
SeedKey задаёт первое число в случайной генерации, таким образом, создавая одни и те же значения при одном и том же значении SeedKey.

#### Шифрование осуществляется следующим образом:
1. **Сначала, если строка содержит цифры, они заменяются собственными значениями**.
Например, 1 превращается на (oone), 2 превращается в (twoo) и так далее.
Значения в скобках специально записаны неправильно, это сделано для приведения длины всех цифр в буквенном варианте на 4.
Таким образом, в шифрованном виде не будет различия в длине между 1 и, допустим, 8.

2. **Следующий шаг - побуквенный сдвиг всех символов с помощью модуля Gipher**.
Gipher работает следующим образом:
 - **SeedKey** используется для создания списка чисел длиной 10 000 цифр.
 - Каждый символ введенной строки сдвигается соответственно созданному числу.
 - Например, при вводе сообщения **Hello**, первые 5 сгенерированных чисел будут такими: 0, 0, -2, -1, 7
 - **'H'** сдвигается на **0**, **'e'** сдвигается на **0**, **'l'** сдвигается на **-2** позиции, **'l'** сдвигается на **-1** позицию и **'o'** сдвигается на **7** позиций.
 - На выходе получается зашифрованное сообщение: **Hejkv**.
 - Процесс расшифровки происходит, как ни странно, прямо противоположным образом: **числа берутся те же**, но знак перед сдвигом противоположный.
Надежность этого модуля заключается в следующем:
 - При его использовании частотный анализ становится совершенно бессмысленным, так как буквы не заменяются никакими специальными буквами.
 - Количество вариаций сообщения равно его длине. Это означает, что слово **Hello** имеет **26^5** (26 - количество букв в английском алфавите, 5 - длина сообщения) вариантов того, как может выглядеть сообщение, и только один правильный, что делает обычный грубый процесс перебора практически бессмысленным, ведь только представьте, сколько слов может быть из 5 букв. Неплохо, правда?

3. После шифрования модулем Gipher, **сообщение может быть перевернуто "зеркально "**, или может остаться таким, как есть. Это контролируется тем же случайно сгенерированным параметром.

4. **Каждый символ в сообщении заменяется соответствующим ему числовым значением в фигурных скобках*.
Пример:
 - У нас есть сообщение Hejkv, допустим, оно было расширено и превратилось в vkjeH.
 - Буква **H** устанавливается в **15**, буква **e** в **2**, буква **j** в **8**, буква **k** в **14**, а буква **v** в **81**.
 - После замены мы получим сообщение : **{81}{14}{8}{2}{15}**
 - Такие значения генерируются аналогичным образом, используя **SeedKey**.

Думаю, не нужно объяснять, что расшифровка происходит точно так же, только в прямо противоположном порядке :)
Если SeedKey введен неверно - расшифровка будет неудачной и будут выведены неверные значения.

#### GreyNigma оснащена рядом мощных алгоритмов защиты:
1. **Отдельные строки**.
Для полного сообщения существует 3 варианта строк: 1-я фейковая строка, оригинальная строка и 2-я фейковая строка.
Как это работает?
 - Каждая строка имеет свои 225 значений ((26 маленьких букв + 26 больших букв + 23 символа) * 3 случайные вариации), которые не могут совпадать с другой строкой/какими-либо другими значениями. Все значения уникальны.
 - В первую "фейковую" строку можно записать действительно важные данные, а в остальные (оригинальную и вторую фейковые строки) - сообщения с бесполезной информацией, либо оставить их пустыми (в случае, если строка пуста, вместо нее генерируется случайный набор символов, например Y!NJP??U#*&!, что явно запутает злоумышленника).

2. **Соли и разделители**.
Соли - это так называемые "балластные" символы, которые добавляются в каждое полноценное сообщение. Это случайные {цифры}, которые создают иллюзию присутствия в сообщении каких-либо других символов, однако, при правильной расшифровке - испаряются. Полное 10-символьное сообщение на каждой строке может превратиться в 50- или даже 70-символьное зашифрованное сообщение.

3. **Сепараторы** - это специальный символ, который отделяет строки (первую поддельную, оригинальную и вторую поддельную) друг от друга, чтобы облегчить чтение при правильной расшифровке. Как и соль, он имеет свое уникальное значение, которое при неправильной расшифровке может случайно превратиться в какую-нибудь букву, запутав злоумышленника.

### ИСПОЛЬЗОВАНИЕ:
GreyNigma представлена в виде онлайн-сервиса (API), который принимает запросы с параметрами message и seedKey и возвращает значение зашифрованного/расшифрованного сообщения.
Репозиторий включает консольную версию (универсальную) и графическую версию, которая работает на системах с графическим интерфейсом. Она зависит от Python-библиотеки Tkinter.
Интерфейс обеих версий сделан максимально доступным и понятным как для новичков, так и для опытных пользователей.
Обратите внимание, что и графическая, и консольная версии GreyNigma принимают значения SeedKey типа данных STRING!

Так же доступна консольная версия в виде Docker-контейнера.


# ОТВЕТЫ НА ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ
---------------------
### 1. Безопасно ли это?
---------------------
Сложно ответить однозначно.
В мире нет ничего совершенного, тем более сейчас, в век информационных технологий
Взломать можно всё что угодно, даже самые надёжные алгоритмы не защищены от множественного перебора с помощью
суперкомпьютеров.
Однако это не говорит о том, что алгоритм не надёжен.
Информация считается защищённой, когда её похищение стоит больше, чем сама эта информация.
Тут же две стороны медали :
Один человек потратит кучу времени и сил, чтобы взломать одностраничный сайт
Другой человек, имеющий квантовые суперкомпьютеры, не будет даже напрягаться, чтобы взломать правительственные сайты
Всё относительно.
GreyNigma - это в первую очередь технология, дарующая безграничную фантазию в плане её же усовершенствования
Вы можете создавать свои строки, добавлять “пустые” элементы, увеличивающие общую длину сообщения, всё ограничено лишь вашей фантазией :)
GreyNigma изначально оснащена неплохим уровнем надёжности, который вы можете улучшить своими знаниями и фантазией, кастомизировав под себя.
---------------------
### 2. Где я могу использовать GreyNigma? Существует надежное шифрование сообщений, так в чем же смысл?
---------------------
На сегодняшний день, во время большой слежки, тяжело говорить о том, насколько надёжен тот или иной сервис
Вчитываясь в политики конфиденциальности, можно понять, что предлагаемое шифрование - очень относительная штука.
С одной стороны да, условный viber/whatsapp безопасны, однако, их политики предполагают “выдачу” ваших сообщений по запросу, допустим, правоохранителей.
Следственно, ваши сообщения могут быть волшебным образом расшифрованы вопреки всем клятвам о сквозном шифровании, исключающее расшифровку сообщений третьими лицами как ни крути.

С помощью GreyNigma, вы можете обмениваться сообщениями даже в ненадёжных сервисах, даже если они прямым текстом говорят, что будут сливать ваши сообщения всем кому не лень. Пусть сливают циферки GreyNigma :)
Это своего рода стеганография, которая спасёт ваши сообщения от их слива любым негодяям, замахнувшимся на ваше законное право о конфиденциальности и тайне личной переписки, гарантированное любым законодательством.
---------------------
### 3. Какие символы поддерживаются?
---------------------
Поддерживаются абсолютно все английские буквы, а так же символы !@’#%^:;&?*()-_=+[]/.,
Поддержка цифр здесь же неоднозначная.
Цифры конвертируются в буквы, то есть 1 заменяется на ‘one’, 2 на ‘two’ и так далее.
Это сделано из-за того, что если бы цифры менялись бы на цифры, то при шифровании происходил бы полный коллапс из-за того, что циферные значения символов менялись бы на такие же цифры, после этого ещё на цифры и так далее…
---------------------
### 4. Какова максимальная длина сообщения?
---------------------
Максимальная длина одной строки - 10.000 символов. Соответственно, для полноценного сообщения - 30.000 символов.

---------------------
### 5. Я нашел ошибку/уязвимость/У меня есть вопросы, куда мне обратиться?
---------------------
Если вы нашли какую-либо ошибку, уязвимость, не понимаете какого-либо аспекта работы или у вас есть идеи/предложения, чувствуйте себя свободно, обращаясь к нам:
E-Mail: greyhatfeedback@protonmail.com
Telegram: @greyhatfdbot

Руководство по API (https://greynigma.herokuapp.com/) выведено отдельным документом API_DOCS на двух языках - английском и русском.
