# -*- coding: utf-8 -*-
root = ['random_answer', 'Deepwarrior', 'kstera']
deep_chat = 150029429 #need to check it on release version

seconds_in_day = 86000

hi_stickers = ['CAADAgADWwQAAm4y2AABD38IAooC_j4C', 'CAADAgADhAEAAjZ2IA7YnALZRRvJMwI']
hi_citrus = ['/DELITAPELSIN', 'ГРЕЙПФРУКТ!', 'ОПРИВЕТ', 'ЦИТРУС!', 'Я ЗНАЮ ЭТУ ДЕВЧОНКУ!', 'ЧТО НОВЕНЬКОГО', 'СПОЙ ПЕСЕНКУ!', 'НУ МАААААМ!']

help_list = ['см. /donate', 'А ЧТО ТУТ НЕПОНЯТНОГО?', 'АЙ НИД СОМБАДИ', '8-800-555-35-35', ';)', 'ХОДЯТ СЛУХИ, ЧТО ВЗЯТКА СОЗДАТЕЛЯМ ПОМОГАЕТ В ПРОХОЖДЕНИИ ЗАДАНИЯ', "ХОЧЕШЬ МНЕ ПОМОЧЬ? У МЕНЯ КАК РАЗ ЕСТЬ ДЛЯ ТЕБЯ ЗАДАНИЕ!",
             "ТЫ НЕ ПОЛУЧИШЬ ЗАДАНИЕ ЧАЩЕ ЧЕМ РАЗ В СУТКИ", "ЕСЛИ ЧОТ НЕ НРАВИТСЯ - ТАК И ПИШИ", "СЛАБО БЕЗ ПОДСКАЗОК?", "ГАЙДЫ ЕСТЬ НА ЮТУБЕ", "ЕСЛИ НОВЫЙ ДЕНЬ НЕ НАЧАЛСЯ - ПОДОЖДИ ДО ЗАВТРА", "ЗАДАНИЕ РЕДКО ДЛИТСЯ ДОЛЬШЕ ТРЁХ ЧАСОВ.",
             "Я ВЕРЮ, У ТЕБЯ ВСЁ ПОЛУЧИТСЯ!", "НЕ ТА КНОПКА", "ХВАТИТ ТЫКАТЬ", "ЗАДАНИЕ СТАНЕТ ДОСТУПНО НА ЧАС ПОЗЖЕ.", "ХОТИТЕ СПОЙЛЕРЫ?", "Взять задание получится только в чате. А МАЙТАСКНУТЬ МОЖНО И В ЛИЧКЕ С БОТОМ"]
donate_list = ['С ТЕБЯ ПИВО', 'С ТЕБЯ ЛИМЕРИК', 'С ТЕБЯ ФОТОЧКА', "С ТЕБЯ ГОЛОС", 'С ТЕБЯ ОБНИМАШКИ^^', 'ПРИШЛИ СВОЙ ВАРИАНТ ЗАДАНИЯ', 'Поздравляю! Вы подключили услугу VIP-VIP-VIP. Теперь все задания для Вас платные.', '/donate',
               "ОТПРАВЬ ЗАРЯДЫ: ДИПУ - 30% ЗА БОТА, ЦИТРУСУ - 30% ЗА ЗАДАНИЯ И #зелёныйаксолотль (тм), ЛИИРЕ И СУПЕРУ ПО 10% ЗА СТИКЕРЫ, ШЬЮЗЕН - 20% ЗА СЕРВЕР", "НЕ ЗАБУДЬ ПОКОРМИТЬ СОЗДАТЕЛЕЙ НА БЛИЖАЙШЕЙ РАКОНОСХОДКЕ",
               "ТЕПЕРЬ ТЫ ПОПЛАТИШЬСЯ!", "ОТ РАСПЛАТЫ НЕ УЙДЁШЬ!", "РАБОТАЮ ЗА СПАСИБУ. А ПАПА С МАМОЙ - НЕТ", "Я ТЕБЯ ЗАПОМНИЛ!", "ПРОИГРАЛ"]

bonus_20 = ['CAADAgADRwADg8cnEQnjFdN51tf-Ag', 'CAADAgADSAADg8cnEUsVYGZANO6ZAg', 'CAADAgADSQADg8cnEah9k-_q1qH1Ag', 'CAADAgADSgADg8cnES219ZCNMV1_Ag', 'CAADAgADSwADg8cnEYi0EfNZVz9OAg', 'CAADAgADVAADg8cnEcm03ptpBsCDAg', 'CAADAgADXwADg8cnEYHrjnqlQhTxAg']
#format: sticker + task
tasks = [['CAADAgADSgADP_vRD6EHNhBBV7W_Ag', 'ТЫ ДИП. ИСПОЛЬЗУЙ ДИПЯНКУ БЛИЖАЙШИЕ 300 СООБЩЕНИЙ.', 0, 300],
         ['CAADAgADSAADP_vRDxb1PT65ZcS8Ag', 'ТЫ ЦИТРУС. СПОЙ ПЕСЕНКУ.', 0, 0], 
         ['CAADAgADQgADP_vRDyRMg2vP6pd8Ag', 'ТЫ АРЕАТАНГЕНТ. ОТПРАВЛЯЙ КАЖДУЮ КАРТИНКУ И СТИКЕР ДИСТОРШН БОТУ БЛИЖАЙШИЕ 100 СООБЩЕНИЙ И ПОКАЗЫВАЙ НАМ.', 0, 100],
         ['CAADAgADWAADP_vRD8CYBmhcMhZxAg', 'ТЫ ЧЕТЫРЕ)))) ТРИ ЧАСА ПИШИ СО СКОБОЧКАМИ))))', 3, 0],
         ['CAADAgADWgADP_vRD_VQ9Woa3bIOAg', 'ТЫ ЗЛОЙ АДМИН. ПОПРОСИ АДМИНА КОГО-НИБУДЬ ЗАБАНИТЬ НА ПАРУ ЧАСОВ ИЛИ СДЕЛАЙ ЭТО САМ, ЕСЛИ У ТЕБЯ ЕСТЬ БАНХАММЕР.', 23, 0],
         ['CAADAgADVAADP_vRD-VGSEORarUwAg', 'ТЫ НОРМАЛЬ. ПРОБЕЙСЯ В ТОП-3 ПО ФЛУДУ ЗА ДЕНЬ.', 23, 0], 
         ['CAADAgADXwADP_vRD-j0lU68FiFsAg', 'ТЫ ГОДВИЛЛЬ. ЭКОНОМЬ ВИРТУАЛЬНОЕ ПРОСТРАНСТВО, ПИШИ БЗ ГЛСНХ.', 3, 300],
         ['CAADAgADdQADP_vRDwPTSwahmq5oAg', 'ТЫ ИИОО. НЕ СДЕРЖИВАЙ СВОЮ НЕНАВИСТЬ К СОГЛАСНЫМ, ПИШИ ИХ НЕ БОЛЕЕ ДВУХ ШТУК В СЛОВЕ.', 3, 300], 
         ['CAADAgADWQADP_vRDxArNUvEnLZiAg', 'ТЫ БАГ. СЛОМАЙ ГОДВИЛЛЬ, МЕНЯ ИЛИ ЛЮБОГО ДРУГОГО БОТА.', 23, 0],
         ['CAADAgADagADP_vRDy9WxzZxe_NUAg', 'ТЫ ЭЛЕКСОРИЕН. ПЕРЕИМЕНУЙСЯ НА ВЕСЬ ДЕНЬ И ПОМЕНЯЙ ПОЛ.', 23, 0], 
         ['CAADAgADbAADP_vRD6Xn7qb5y-9YAg', 'ТЫ АНАЛЕПТИК. ПОСТАВЬ КОМУ-НИБУДЬ АНАЛИЗ ПО АВАТАРКЕ.', 23, 0],
         ['CAADAgADSwADP_vRD5Fg55OC3EGYAg', 'ТЫ ПУШИСТЫЙ ТРИББЛ. ставь точки. и не забывай писать всё с маленькой буквы.', 3, 300], 
         ['CAADAgADRgADP_vRD5ypDI2RyuAxAg', 'ТЫ СИЛЬФУР. НАДЕНЬ МАСКУ ДРУГОГО ИГРОКА И ВЫПОЛНИ ЕГО ЗАДАНИЕ БЫСТРЕЕ ИЛИ ЛУЧШЕ', 23, 0],
         ['CAADAgADQAADP_vRD85Bwdr_xrWpAg', 'ТЫ СУПЕР ТРУПЕР. ИСПОЛЬЗУЙ КАКИЕ-НИБУДЬ НЕОБЫЧНЫЕ СИМВОЛЫ.', 3, 300], 
         ['CAADAgADUQADP_vRD60coEpglSQTAg', 'ТЫ ЭЛЛИОТТ. ОТВЕДИ КОГО-НИБУДЬ НА ВЫХОД, ЛОГ В СТУДИЮ.', 23, 0],
         ['CAADAgADVQADP_vRD3lc6Dt9R8B_Ag', 'ТЫ ЛЕОНАРДО. СПИЛИ ТРОИХ В ОДНОМ ПОДЗЕМЕЛЬЕ, ЛОГ В СТУДИЮ.', 23, 0], 
         ['CAADAgADTwADP_vRD3-aLVhdSKPhAg', 'ТЫ ШЕНМАН. ОТПРАВЬ АУДИОСООБЩЕНИЕ ДЛИНОЙ В МИНУТУ ИЛИ БОЛЕЕ.', 23, 0],
         ['CAADAgADbwADP_vRD5PpTSaCriwYAg', 'ТЫ ШИЗИК. ПИШИ ПРО ВСЕХ ГАДОСТИ, НО УДАЛЯЙ ЧЕРЕЗ ПАРУ СООБЩЕНИЙ', 3, 300],
         ['CAADAgADQQADP_vRD5i0jEorKyN1Ag', 'ТЫ ЛИИРА. НАРИСУЙ КРАСИВУЮ КАРТИНКУ И ПОКАЖИ НАМ', 23, 0],
         ['CAADAgADcgADP_vRD2nt1nzmOx8JAg', 'ТЫ О ЖИ. БУМАГА! НАЙДИ, КОГО ТЫ ЕЮ МОЖЕШЬ ПОБЕДИТЬ!', 23, 0],
         ['CAADAgADYAADP_vRD1pLEzSHlvVlAg', 'ТЫ МИХЕЙ. ТЫ ПОЙМАЛ САЧКОМ КАМЕНЬ. НАЙДИ, КОГО ТЫ ИМ МОЖЕШЬ ПОБЕДИТЬ!', 23, 0],
         ['CAADAgADAQEAAjZ2IA6wVfmQOycjlwI', 'ТЫ СДЕЛАЛ РУКАМИ НОЖНИЦЫ, ПОТОМУ ЧТО НИКТО НЕ РИСУЕТ АКСОЛОТЛЕЙ С НИМИ. НАЙДИ, КОГО ТЫ ИМИ МОЖЕШЬ ПОБЕДИТЬ.', 23, 0],
         ['CAADAgADRAADP_vRD1MBUKl5_67DAg', 'ТЫ ФИЛАШТЕКЬЮ. ПИШИ TRANSLITOM.', 3, 300],
         ['CAADAgADcwADP_vRD2eyQ2jFa1PFAg', 'ТЫ ХЕЛЕНАК. ЗАПИРАТЬ КОГО-ТО В МОРЕ И ПОКИНЬ ЕГО С СОКРОВИЩЕМ. ЛОГ В СТУДИЮ.', 23, 0],
         ['CAADAgADWwADP_vRD-3zlimm1gABOwI', 'ТЫ КАПЛЯ ЯНТАРЯ. ИШИП ЁСВ АВОЛС ТОРОБОАН.', 3, 300],
         ['CAADAgADcQADP_vRD7RRN9-SsTcAAQI', 'ТЫ АЙСБРЕХЕР. ПОСЛЕ ТАБЛЕТОК У ТЕБЯ В ЧАТЕ ЕСТЬ ВООБРАЖАЕМЫЙ ДРУГ', 23, 0],
         ['CAADAgADYgADP_vRDwhMWn-LcpW1Ag', 'ТЫ ПОЛИНОМ ГАУССА. ПОПРОСИ У МИШИ ЗАДАЧКУ ПО МАТАНУ И РЕШИ ЕЁ', 23, 0],
         ['CAADAgADTQADP_vRD9M3gnprJHMsAg', 'ТЫ ФОБЕР. ПОЯВЛЯЙСЯ В ЧАТЕ НЕ ПОЗЖЕ ЧЕМ ЧЕРЕЗ 5 МИНУТ ПОСЛЕ УПОМИНАНИЯ О ТЕБЕ', 10, 0],
         ['CAADAgADRwADP_vRD7PXCM29pqK2Ag', 'ТЫ ДЛИНОМОЗГ. С Т А В Ь  П Р О Б Е Л  П О С Л Е  К А Ж Д О Й  Б У К В Ы .', 3, 300],
         ['CAADAgADZwADP_vRD1eol4dMSWiYAg', 'ТЫ ВЕЗУНЧИК. ПОПРОБУЙ ДОБИТЬСЯ У ПУШКА 100% ВЕРОЯТНОСТИ ЗА 5 ПОПЫТОК.', 23, 0],
         ['CAADAgADiAADP_vRD7m6NPkFdD5AAg', 'ТЫ ФАЛЛИК СИМБОЛ. ПОСТАВЬ СЕБЕ НА АВАТАРКУ ПОСЛЕДНЮЮ ПРИСЛАННУЮ В ЧАТ КАРТИНКУ.', 23, 0],
         ['CAADAgADYwADP_vRDyRf9XlT7-wAAQI', 'ТЫ МАЛЕФИКА. ПРЕДСКАЖИ, КАКОЕ ИЗ СЕЙЧАС ВЗЯТЫХ ЗАДАНИЙ НЕ БУДЕТ ВЫПОЛНЕНО.', 23, 0],
         ['CAADAgADbQADP_vRD9OhnOLMd_0SAg', 'ТЫ АНДАРЧ. ДОВЕДИ ЧАТ ДО РУГАНИ И ИСТЕРИК', 23, 0],
         ['CAADAgADVgADP_vRD3SPhVKzmhepAg', 'ТЫ ДЖЕЙ ДЖИ. СПИЛИ ОДНОЧАТОВЦА И НАПИШИ ЕМУ ПИТАФЬЮ', 23, 0],
         ['CAADAgADUgADP_vRD9IDWofQEWenAg', 'ТЫ КАТИССА. МОЛЧИ В ЧАТЕ ДО ЗАСЧИТЫВАНИЯ  ЭТОГО ЗАДАНИЯ', 6, 0],
         ['CAADAgADQwADP_vRDwwu0nJlgL--Ag', 'ТЫ МУХА-ХА. ДОПИСЫВАЙ-ВАЙ К КАЖДОМУ-МУ СЛОВУ-ВУ ПОСЛЕДНИЙ-НИЙ СЛОГ-СЛОГ ЧЕРЕЗ-РЕЗ ДЕФИС-ФИС', 3, 0],
         ['CAADAgADXAADP_vRDzfiKs97z6teAg', 'ТЫ ВАЛИНОР. СДЕЛАЙ ИНТЕРЕСНУЮ ПОДЕЛКУ СВОИМИ РУКАМИ', 23, 0],
         ['CAADAgADbgADP_vRD9aHxI_AWtYXAg', 'ТЫ МЕДИА. ПШИ ВЕС СЛВОА С ОЩТБКАМТ', 3, 0],
         ['CAADAgADZQADP_vRD56tnWbB-VQxAg', 'ТЫ ПАТРИСИЯ. ПОМОГИ ДРУГИМ ПОЗНАТЬ СИЛУ ЧТЕНИЯ, ПИШИ В КАЖДОМ СООБЩЕНИИ, ДАЖЕ В САМОМ МАЛЕНЬКОМ, БОЛЬШЕ ДВАДЦАТИ СЛОВ ИЛИ ХОТЯ БЫ СТОЛЬКО', 3, 0],
         ['CAADAgADXgADP_vRD3BPWr6Hatf3Ag', 'ТЫ АЛФОРЧУ. УБЕЙ СВОИМ СООБЩЕНИЕМ ЧЯТИК ХОТЯ БЫ НА ПОЛЧАСИКА', 23, 0],
         ['CAADAgADSQADP_vRD70FjV4JQZgtAg', 'ТЫ НАРЕЗНОЙ. НАПИШИ ПРОВЕРЯТОРАМ БОТА ТАЙНЫЕ ДОНОСЫ НА ТРЁХ ИГРОКОВ, ПРОВАЛИВШИХ ЗАДАНИЕ', 23, 0],
         ['CAADAgADXQADP_vRD-iDlwPCIpAAAQI', 'ТЫ ТОТО РО. ПРИШЛИ СВОЁ ФОТО, ЗАМЕНИВ ГЛАЗА НА ОНЕМЕШНЫЕ', 23, 0],
         ['CAADAgADYQADg8cnEaHZyTdEZp_CAg', 'ТЫ САРАСТИ. КОГДА ЭТО ЗАДАНИЕ ВИДИТ ДИП, ОН ПИШЕТ ПРОИГРАЛ, КОГДА ЗАДАНИЕ ВИДЯТ УХИ - ОНА ПИШЕТ МОЛОДЕЦ! САРАСТИ!', 23, 0]
        ]  

whitelist = [311689962, 265419583, 150029429, 360910213, 171108866, 325898595, 183217512, 270769101, 53316498, 287819651]