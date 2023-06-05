# Kvocenshik
https://kvocenshik.herokuapp.com/

<img src="/project.gif" alt="project"/>

<b>About the project:</b>
<br>The project is intended for everyone who wants to make an assessment of the market value of the apartment.
<br>At the moment, the service works only for apartments in Moscow.
<br>In order to get a prediction, you need to enter the main parameters of the apartment: address, nearest metro station, number of rooms and area.
<br>For a more accurate calculation, you can fill in additional parameters. By clicking on the "Calculate" button, all the magic happens, and we see the prediction of the cost of the apartment and a map with the location of the house that was indicated.

<b>Project step by step:</b>

<b>1. Parsing.</b>
<br>No data - no Data Science, so the first step is to collect data. Turning to the most popular real estate aggregator "Cyan", using the Selenium library and a special driver, a code was written that sorted through the pages with apartments, changing two parameters: metro and the number of rooms in the apartment. Thus, after 4 hours of code operation, about 4 thousand excel files with apartment data were downloaded.

<b>2.</b> Data processing and analysis.</b>
<br>Next, the process began, which takes 70% of the time of work on the project. Unnecessary columns were removed, missing values were filled in, new values were added based on those that already exist. During the execution of these tasks, many difficulties arose:<br>a) it was necessary to write a function that converts the cost from currency to rubles;<br>b) a function with regular expressions for processing strings with an address, necessary for the correct format of string values for address translation to coordinates;<br>c) the function of converting the address to coordinates using the geocoder library, in which it was necessary to register timing errors, and if the address was not found, then fill in the NaN value.
<br> <br> Further, more precise work was carried out on emissions and the addition of new parameters:
<br>а) based on the coordinates, the distance from the house to the center of Moscow was added;
<br>b) based on the distance, the circle in which the apartment is included;
<br>c) based on metro stations: district and administrative district.
<br><br>The addition of new parameters had a positive effect on the result of predictions. Next, it was necessary to convert all categorical features, replacing them with numbers for a more convenient format for working on the backend. Then standard procedures: normalization, train/test split and training.

<b>3. Training.</b>
<br>Thus, we come to the most important thing - training. To begin with, several models were made without parameters: LogisticRegression, Lasso, Ridge, GradientBoostingRegressor, CatBoost, XGBoost. The best result without parameters was shown by XGBoost, which is what we chose. Having selected the best model settings and trained the model, we got the result for the MAPE metric (average absolute error in percent) of 10-11%. After saving the model, we start creating the site.
  
<b>4. Site creation.</b>
<br>Backend implemented using the Flask library. To implement the model on the site, code was written that accepted and converted the input data entered by the user into the form that the model takes. The front is implemented using HTML/CSS and the Bootstrap library.

<b>О проекте:</b>
<br>Проект предназначен для всех желающих, кто хочет сделать оценку рыночной стоимости квартиры.
<br>На данный момент сервис работает только по квартирам в Москве.
<br>Для того, чтобы получить предсказание необходимо ввести основные параметры квартиры: адрес, ближайшее метро, количество комнат и площадь.
<br>Для более точного расчета можно заполнить дополнительные параметры. Нажав на кнопку "Рассчитать", происходит вся магия, и мы видим предсказание стоимости квартиры и карту с месторасположением дома, который был указан.

<b>Пошаговое выполнение проекта:</b>

<b>1. Парсинг.</b> 
<br>Нет данных - нет Data Science, поэтому первым делом необходимо собрать данные. Обратившийсь к самому популярному агрегатору недвижимости "Циан", с помощью библиотеки Selenium и специального драйвера был написан код, который перебирал страницы с квартирами, изменяя два параметра: метро и количество комнат в квартире. Таким образом, спустя 4 часа работы кода было скачено около 4 тысяч excel файлов с данными о квартирах. 

<b>2. Обработка и анализ данных.</b>
<br>Далее начался процесс, занимающий 70% времени работы над проектом. Были удалены ненужные столбики, заполнены пропущеные значения, добавлены новые значения на основе тех, что уже есть. В ходе выполнения данных задач возникло много трудностей:<br>а) было необходимо написать функцию конвертирующую стоимость из валюты в рубли;<br>б) функцию с регулярмыми выражениями, для обработки строк с адресом, необходимую для правильного формата строковых значений для перевода адреса в координаты;<br>в) функцию преобразования адреса в координаты с помощью библиотеки geocoder, в которой было необходимо прописать ошибки по таймингу, и в случае если адрес не найден, то заполнить значение NaN. 
<br> <br> Далее была проведена более точная работа над выбросами и добавление новых параметров: 
<br>а) на основе координат было добавлено расстояние от дома до центра Москвы; 
<br>б) на основе расстояния, окружность в которую входит квартира; 
<br>в) на основе станций метро: район и административный округ. 
<br><br>Добавление новых параметров положительно повлияло на результат предсказаний. Далее было необходимо преобразовать все категориальные фичи, заменив их на числа для более удобного формата работы на backend. Затем стандартные процедуры: нормализация, train/test split и обучение.

<b>3. Обучение.</b>
<br>Таким образом, мы подошли к самому главному - обучению. Для начала было сделано несколько модлелей без параметров: LogisticRegression, Lasso, Ridge, GradientBoostingRegressor, CatBoost, XGBoost. Наилучший результат без параметров показал XGBoost, на чем мы и остановили свой выбор. Подобрав наилучшие параметры настройки модели и обучив модель, мы получили результат по метрике MAPE (среднее абсолютная ошибка в процентах) 10-11%. Сохранив модель приступаем к созданию сайта.
  
<b>4. Создание сайта.</b>
<br>Backend осуществлен с помощью библиотеки Flask. Для реализации модели на сайте был написан код, который принимал и преобразовывал входные данные, введеные пользователем в тот вид, который принимает модель. Фронт осуществлен с помощью HTML/CSS и библиотеки Bootstrap. 
