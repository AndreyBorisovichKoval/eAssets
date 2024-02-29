##### _____________________________________
 
* Содержимое файла README.md будет полностью изменено после завершения проекта...

* Содержащийся в настоящий момент текст не имеет никакого отношения к данному приложению и является неким шаблоном для последующего формирования необходимого контекста...

##### _____________________________________

## Приложение

# **eAssets**

##### _____________________________________

***Примечание***:

Проект был создан в процессе трехмесячного обучения в **Alif Академии** под руководством преподавателя курса, **Рахимова Некруза**.
В разработке и реализации проекта были вложены усилия и использованы полученные в процессе обучения знания и навыки для достижения поставленной цели.

Проект был разработан с учетом поставленных задач в процессе обучения.

Клонирование этого проекта с GitHub позволит сохранить и распространить результаты работы, а также даст возможность другим людям изучить детали проекта, внести свои вклады или использовать его в качестве основы для своих собственных проектов.

Проект не является коммерческим и был реализован в ограниченные (сжатые) сроки.

##### _____________________________________

## Описание проекта

* **eAssets** - это эффективное приложение для регистрации и учета основных средств (активов) организации. Оно предоставляет удобный инструмент для управления активами в вашей организации, сфокусированный на бэкэнд-разработке.

* **eAssets** разработан для обеспечения надежного хранения и управления данными об основных средствах. С помощью этого приложения вы можете легко добавлять, обновлять и удалять записи об активах, включая информацию о номере инвентаря, наименовании, идентификаторе, дате приобретения, сроке службы, стоимости и других важных атрибутах.

* **eAssets** предоставляет чистый и понятный API для взаимодействия с данными об активах. Он обеспечивает возможность выполнения различных операций, таких как получение списка активов, поиск по определенным критериям и получение детальной информации о каждом активе. Приложение также обладает надежной системой авторизации и аутентификации, чтобы гарантировать безопасность ваших данных.

* Хотя **eAssets** фокусируется на бэкэнд-разработке и не включает фронтэнд-интерфейс, он предоставляет мощный и гибкий фундамент для разработки пользовательского интерфейса в соответствии с вашими потребностями. Вы можете создать собственный фронтэнд или интегрировать eAssets в существующий фронтэнд для обеспечения полноценного пользовательского приложения.

* **eAssets** - это незаменимый инструмент для организаций, которые хотят эффективно управлять и отслеживать свои основные средства. Он предоставляет надежную и масштабируемую платформу для учета активов.

##### _____________________________________

## Стек проекта

### Django
* **Django** - веб-фреймворк, написанный на языке программирования **Python**. Он предоставляет набор инструментов и функциональность для разработки эффективных, масштабируемых и повторно используемых веб-приложений.
### Django REST Framework
* **Django REST Framework** - фреймворк для разработки веб-сервисов и **API** (Application Programming Interface) на основе архитектуры **REST** (Representational State Transfer). Он обеспечивает удобные инструменты и классы для создания и управления **RESTful API** в Django.
### База данных - PostgreSQL
* **PostgreSQL** ("***Postgres***") - мощная и расширяемая объектно-реляционная система управления базами данных (**СУБД**). Она отличается надежностью, высокой производительностью и соответствием стандартам. **PostgreSQL** предоставляет широкий набор возможностей и функциональности, что делает его одним из наиболее популярных выборов для хранения данных в различных приложениях.

##### _____________________________________

_-=*=-_

- Это **бекендная часть приложения**, которая предоставляет API и обрабатывает бизнес-логику. Здесь нет **фронтендной** части, так как это отдельный компонент, который может быть (и возможно будет) разработан.
Приложение служит интерфейсом для обмена данными с другими приложениями или компонентами. Оно предоставляет набор эндпоинтов ***(URL-адресов)***, по которым другие приложения или клиенты **могут отправлять запросы** и **получать ответы**.

##### _____________________________________

## Выполняемые задачи проекта:

### Управление департаментами и отделами

1. Создание, изменение и удаление отделов и подразделений.
2. Отслеживание информации о дате создания и удаления отделов/подразделений.
3. Учет авторства создания и удаления отделов/подразделений.

### Управление должностями

1. Создание, изменение и удаление должностей.
2. Отслеживание информации о дате создания и удаления должностей.
3. Учет авторства создания и удаления должностей.

### Управление сотрудниками

1. Ведение информации о сотрудниках, таких как фамилия, имя, отчество.
2. Привязка сотрудников к подразделениям и должностям.
3. Отслеживание информации о дате создания и удаления сотрудников.
4. Учет авторства создания и удаления сотрудников.

### Управление активами

1. Создание, изменение и удаление активов (например, оборудования).
2. Отслеживание информации о дате приобретения и списания активов.
3. Учет авторства создания и списания активов.
4. Учет стоимости активов и текущей стоимости.
5. Описание активов и информация об их типе.

### Назначение активов сотрудникам

1. Связывание активов с конкретными сотрудниками.
2. Отслеживание информации о дате назначения и возврате активов.

### Журнал действий пользователей

1. Отслеживание действий пользователей в системе.
2. Запись информации о действиях пользователей и временной метке их действий.

### Проверочные точки задач

1. Создание и управление контрольными точками задач.
2. Отслеживание даты последней обработки контрольной точки.
3. Отметка успешного выполнения контрольной точки.

##### _____________________________________

## Основная задача проекта:

### **Ежемесячный перерасчет стоимости основных средств** 
- это процесс обновления и пересмотра стоимости активов, которые являются основными средствами организации.
- Основные средства включают в себя такие активы, как здания, оборудование, транспортные средства и другие долговечные активы, используемые для производственной или коммерческой деятельности.

##### Шаги, которые обычно включены в процесс ежемесячного перерасчета стоимости основных средств

**Обновление информации об активах:**
* Перед перерасчетом стоимости основных средств необходимо обновить информацию о каждом активе. Это включает в себя проверку актуальности данных, таких как стоимость приобретения, дата приобретения, срок службы и другие связанные с активами параметры.

**Расчет амортизации:**
* Амортизация: это процесс распределения стоимости актива на протяжении его срока службы.
* В процессе ежемесячного перерасчета стоимости основных средств производится расчет амортизации для каждого актива в соответствии с установленными правилами и методами амортизации.
* Это может включать линейную амортизацию (**реализована** в настоящем проекте), амортизацию по методу уменьшающегося остатка или другие методы, определенные в соответствии с правилами бухгалтерии.

**Обновление бухгалтерских записей:**
* После расчета амортизации необходимо обновить бухгалтерские записи, связанные с каждым активом. Это включает в себя регистрацию амортизационных расходов и изменение балансовых счетов, связанных с активами. Обновленные бухгалтерские записи отражают актуальную стоимость активов после перерасчета.

**Отчетность и анализ:**
* После завершения перерасчета стоимости основных средств, составляются отчеты, которые отражают результаты перерасчета.
* Это может включать отчеты о суммарной амортизации, отчеты о стоимости активов и другую финансовую информацию, которая может быть полезна для анализа финансового состояния организации.

Процесс ежемесячного перерасчета (***обычно производится ежемесячно***) стоимости основных средств позволяет поддерживать актуальность и точность информации ***об остаточной стоимости активов***, а также соответствовать правилам бухгалтерии и стандартам финансовой отчетности.
Это помогает организации управлять своими активами и принимать обоснованные решения на основе актуальной финансовой информации.

##### _____________________________________

## Структура проекта (таблицы)

**Модель Department:**

* title: поле типа CharField с максимальной длиной 100 символов, представляющее название департамента.
* is_deleted: поле типа BooleanField со значением по умолчанию False, указывающее, удален ли департамент.
* created_at: поле типа DateTimeField с auto_now_add=True, автоматически заполняющееся текущей датой и временем при создании записи.
* created_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, создавшего департамент.
* deleted_at: поле типа DateTimeField, позволяющее указать дату и время удаления департамента.
* deleted_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, осуществившего удаление департамента.

**Модель Division:**

* department: поле типа ForeignKey, связанное с моделью Department, указывающее на департамент, к которому относится подразделение.
* title: поле типа CharField с максимальной длиной 100 символов, представляющее название подразделения.
* is_deleted: поле типа BooleanField со значением по умолчанию False, указывающее, удалено ли подразделение.
* created_at: поле типа DateTimeField с auto_now_add=True, автоматически заполняющееся текущей датой и временем при создании записи.
* created_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, создавшего подразделение.
* deleted_at: поле типа DateTimeField, позволяющее указать дату и время удаления подразделения.
* deleted_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, осуществившего удаление подразделения.

**Модель Position:**

* title: поле типа CharField с максимальной длиной 100 символов, представляющее название должности.
* is_deleted: поле типа BooleanField со значением по умолчанию False, указывающее, удалена ли должность.
* created_at: поле типа DateTimeField с auto_now_add=True, автоматически заполняющееся текущей датой и временем при создании записи.
* created_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, создавшего должность.
* deleted_at: поле типа DateTimeField, позволяющее указать дату и время удаления должности.
* deleted_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, осуществившего удаление должности.

**Модель Staff:**

* last_name: поле типа CharField с максимальной длиной 100 символов, представляющее фамилию сотрудника.
* first_name: поле типа CharField с максимальной длиной 100 символов, представляющее имя сотрудника.
* patronymic: поле типа CharField с максимальной длиной 100 символов, представляющее отчество сотрудника.
* division: поле типа ForeignKey, связанное с моделью Division, указывающее на подразделение, к которому относится сотрудник.
* position: поле типа ForeignKey, связанное с моделью Position, указывающее на должность сотрудника.
* memo: поле типа TextField, представляющее дополнительные замечания о сотруднике.
* is_deleted: поле типа BooleanField со значением по умолчанию False, указывающее, удален ли сотрудник.
* created_at: поле типа DateTimeField с auto_now_add=True, автоматически заполняющееся текущей датой и временем при создании записи.
* created_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, создавшего запись о сотруднике.
* deleted_at: поле типа DateTimeField, позволяющее указать дату и время удаления сотрудника.
* deleted_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, осуществившего удаление сотрудника.

**Модель Asset:**

* inventory_number: поле типа CharField с максимальной длиной 100 символов, представляющее инвентарный номер актива.
* title: поле типа CharField с максимальной длиной 100 символов, представляющее название актива.
* identifier: поле типа CharField с максимальной длиной 120 символов, представляющее идентификатор актива.
* acquisition_date: поле типа DateField, представляющее дату приобретения актива.
* created_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, создавшего актив.
* service_life: поле типа IntegerField, представляющее срок службы актива.
* cost: поле типа DecimalField с максимальным числом цифр 10 и количеством знаков после запятой 2, представляющее стоимость актива.
* current_cost: поле типа DecimalField с максимальным числом цифр 10 и количеством знаков после запятой 2, представляющее текущую стоимость актива.
* last_recalculation_date: поле типа DateField, позволяющее указать последнюю дату переоценки актива.
* description: поле типа TextField, представляющее описание актива.
* asset_type: поле типа ForeignKey, связанное с моделью AssetType, указывающее на тип актива.
* is_written_off: поле типа BooleanField со значением по умолчанию False, указывающее, списан ли актив.
* written_off_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, осуществившего списание актива.
* written_off_at: поле типа DateTimeField, позволяющее указать дату и время списания актива.

**Модель AssetType:**

* title: поле типа CharField с максимальной длиной 100 символов, представляющее название типа актива.
* is_deleted: поле типа BooleanField со значением по умолчанию False, указывающее, удален ли тип актива.
* created_at: поле типа DateTimeField с auto_now_add=True, автоматически заполняющееся текущей датой и временем при создании записи.
* created_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, создавшего тип актива.
* deleted_at: поле типа DateTimeField, позволяющее указать дату и время удаления типа актива.
* deleted_by: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, осуществившего удаление типа актива.

**Модель AssetAssignment:**

* asset: поле типа ForeignKey, связанное с моделью Asset, указывающее на актив, который был назначен.
* staff: поле типа ForeignKey, связан8. Модель UserAction:
* user: поле типа ForeignKey, связанное с моделью User, указывающее на пользователя, совершившего действие.
* action: поле типа TextField, содержащее описание действия, которое было выполнено пользователем.
* timestamp: поле типа DateTimeField с auto_now_add=True, автоматически заполняющееся текущей датой и временем при создании записи.

**Модель TaskCheckPoint:**

* title: поле типа CharField с максимальной длиной 100 символов, представляющее название контрольной точки задачи.
* last_processed_date: поле типа DateTimeField, позволяющее указать дату и время последней обработки контрольной точки задачи.
* is_successful: поле типа BooleanField со значением по умолчанию False, указывающее, успешно ли выполнена контрольная точка задачи.

**Модель UserAction:**

* user: поле, связанное с моделью User через внешний ключ (ForeignKey). Оно указывает на пользователя, который выполнил действие.
* action: текстовое поле (TextField), которое содержит описание действия пользователя.
* timestamp: поле типа DateTimeField с атрибутом auto_now_add=True, которое автоматически записывает дату и время создания записи.

**Модель User:**

* Для необходимых целей проекта также использовалась встроенная модель **User**.

##### _____________________________________

## Структура проекта по файлам (модулям):

### main

* Данный код представляет собой простое приложение **Flask**, которое запускает веб-сервер и определяет маршруты для обработки HTTP-запросов.

* Первым шагом импортируется класс Flask из модуля flask. Затем импортируется переменная **app** из модуля **routes** (это модуль, содержащий определения маршрутов для приложения).

* Далее создается **экземпляр класса** Flask и присваивается переменной **app**. В качестве аргумента конструктору передается __name__, что указывает Flask на то, что это основной модуль или пакет.

* Затем вызывается метод register_blueprint() на объекте **app**, чтобы зарегистрировать маршруты из модуля routes. Регистрация маршрутов позволяет приложению знать, каким образом обрабатывать входящие HTTP-запросы.

* Наконец, проверяется, является ли текущий модуль **основным** модулем, вызывая **__name__ == '__main__'**. Если это так, то приложение запускается с помощью метода run() объекта **app**. В данном случае, включен режим отладки (debug=True) и сервер будет слушать порт 7000.

*   Таким образом, этот код создает ***Flask-приложение***, регистрирует маршруты и запускает сервер для обработки ***HTTP-запросов***.

### connection

* Данный код относится к работе с базой данных в приложении, используя ***SQLAlchemy***.

* Сначала импортируются всё необходимые: dbname_app, user_app, password_app, host_app, port_app из модуля **security**, а также **sessionmaker** и **create_engine** из модуля ***sqlalchemy***.

* Далее определяется строка подключения к базе данных **DATABASE_URL** с использованием значений, полученных из user_app, password_app, host_app, port_app и dbname_app. Эта строка будет содержать информацию, необходимую для установления соединения с базой данных **PostgreSQL**.

* Затем создается экземпляр класса **Engine** из модуля **create_engine** и передается ему **DATABASE_URL** в качестве аргумента. Этот объект (**engine**) представляет собой основной интерфейс к базе данных и будет использоваться для выполнения ***SQL-запросов***.

* Наконец, создается класс **Session** с использованием **sessionmaker**, который связывается с **engine**. Этот класс будет использоваться для создания отдельных сессий (экземпляров) для каждого подключения к базе данных. Сессии позволяют выполнять ***операции чтения и записи данных*** в базу данных.

* Таким образом, данный код устанавливает соединение с базой данных ***PostgreSQL*** с помощью ***SQLAlchemy*** и создает класс **Session**, который будет использоваться для управления подключениями к базе данных в приложении.

### models

Содержит архитетктуру базы данных со всеми ей таблицами и атрибутами таблиц.

**Классы** отражают ***структуру таблиц*** базы данных и связи между ними с использованием ***SQLAlchemy***.
Они предоставляют объектно-реляционное отображение **(ORM)**, которое позволяет взаимодействовать с данными в базе данных с помощью объектов и методов классов.

Таким образом эти таблицы хранят всю необходимую информацию.

### roules

Данный модуль представляет собой набор маршрутов (routes) для веб-приложения, созданного с использованием **Flask**, фреймворка для разработки веб-приложений на языке Python.
В данном модуле используется модуль ***repository***, содержащим функции для работы с базой данных и хранения данных. Код определяет различные маршруты (эндпоинты) для обработки ***HTTP-запросов*** и вызывает соответствующие функции из модуля ***repository*** для обработки запросов и возврата данных в формате JSON.

Общая структура кода соответствует парадигме **RESTful API**, где каждому ***URL-адресу*** соответствует определенный **HTTP-метод (GET, POST и т.д.)** и функция для обработки запроса и возврата данных. **Flask** облегчает создание и настройку веб-приложения, предоставляя удобные инструменты для определения маршрутов и обработки запросов.

### repository

Данный модуль представляет собой набор функций для взаимодействия с базой данных с использованием ***SQLAlchemy***.
В коде импортируются необходимые модули и классы, а также создается соединение с базой данных.

Каждая **функция** использует контекстные менеджеры ***Session*** и ***with*** для обеспечения **корректного управления сессией** и **соединением с базой данных**, выполняет необходимые запросы и сохраняет изменения с помощью метода **commit()**. Это позволяет обеспечить целостность данных и корректное управление сессией и соединением с базой данных.

##### _____________________________________

### readme

* Файл __README.md__ - это текущий файл, который может быть изменен по мере необходимости, включая сам **"код"**. В процессе разработки и обновления проекта, **README.md** может подвергаться изменениям, чтобы отражать ***актуальную информацию о проекте***, его ***функциональности***, ***инструкции по установке*** и ***использованию***, а также другую полезную информацию для **разработчиков** и **пользователей**. Это важный компонент документации, который помогает улучшить понимание проекта и содействует его успешному использованию.

##### _____________________________________


### Структура базы данных:
![0001.jpg](image%2F0001.jpg)
