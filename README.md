##### _____________________________________
 
* Содержимое файла README.md будет полностью изменено после завершения проекта...
* Содержащийся в настоящий момент текст не имеет никакого отношения к данному приложению и является неким шаблоном для последующего формирования необходимого контекста...

##### _____________________________________

## Приложение

# **eAsseTs**

##### _____________________________________

***Примечание***:

Проект был создан по завершению процесса трехмесячного обучения в **Alif Академии** под руководством преподавателя курса, **Рахимова Некруза**.
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

**Модель UserSettings:**

* user: поле OneToOneField, которое связывает модель User (встроенную модель Django) с моделью UserSettings. Это поле указывает на пользователя, к которому относятся эти настройки.
* setting1: поле CharField с максимальной длиной 120 символов. Оно предназначено для хранения настройки 1.
* setting2: поле IntegerField, предназначенное для хранения настройки 2, которая является целым числом.
* setting3: поле BooleanField, которое хранит значение настройки 3, представляющейся логическим (True/False) значением.
* setting4: поле CharField с максимальной длиной 120 символов. Оно предназначено для хранения настройки 4.
* setting5: поле CharField с максимальной длиной 120 символов. Оно предназначено для хранения настройки 5.
- (поля данной таблицы можно изменить в зависимости от требований front-end-а.  

**Модель User:**

* Для необходимых целей проекта также использовалась встроенная в ***Django*** модель **User**.

##### _____________________________________

### Функции:

Также, например, в проекте реализована отчётность, включая функцию: **create_and_export_report**.

Функция **create_and_export_report** генерирует отчет и экспортирует его в формате **CSV** (в основном для аналитиков данных) или **XLSX** (для окончательных пользователей), в зависимости от параметра ***format***, переданного в запросе. Она использует данные из базы данных, создает DataFrame из этих данных и преобразует даты в нужный формат. Затем функция объединяет несколько DataFrame и, в зависимости от формата экспорта, сохраняет отчет в соответствующем формате (CSV или XLSX) и отправляет его в ответе HTTP. Если формат экспорта не указан или некорректен, функция возвращает сообщение об ошибке.

Технологии, используемые в функции **create_and_export_report**, включают:

* Python: Функция написана на языке программирования Python, который является основным языком разработки.
* Django: Функция является частью веб-приложения, основанного на фреймворке Django. Django предоставляет удобные инструменты для разработки веб-приложений, включая обработку HTTP-запросов, работу с базами данных и генерацию HTTP-ответов.
* Pandas: При обработке данных функция использует библиотеку Pandas. Pandas предоставляет высокоуровневые структуры данных и инструменты для анализа и манипуляции табличных данных.
* NumPy: NumPy используется вместе с Pandas для эффективной обработки и анализа данных. Он предоставляет многомерные массивы и функциональность для работы с ними.
* xlsxwriter: Библиотека xlsxwriter используется для создания и записи данных в файлы формата XLSX (Excel).
* JWTAuthentication: Функция использует JWT-аутентификацию (JSON Web Token) для аутентификации пользователей. JWT позволяет генерировать и проверять токены, используемые для аутентификации и авторизации веб-приложения.
* JWT: В функции использовано JWT для аутентификации пользователей. JWT - это открытый стандарт (RFC 7519) для создания токенов доступа, которые могут передаваться между двумя сторонами в компактном и безопасном виде.
* HTTP: Для взаимодействия с клиентом функция использует протокол HTTP (Hypertext Transfer Protocol) для передачи данных.
* CSV: Функция может экспортировать отчет в формате CSV (Comma-Separated Values), который представляет табличные данные в виде текстового файла, разделенного запятыми.
* XLSX: Функция может экспортировать отчет в формате XLSX (Microsoft Excel), который представляет табличные данные в виде электронной таблицы, создаваемой приложением Microsoft Excel.

##### _____________________________________

### Readme.md

* Файл __README.md__ - это текущий файл, который может быть изменен по мере необходимости, включая сам **"код"**.
* В процессе разработки и возможного обновления проекта, **README.md** может подвергаться изменениям, чтобы отражать ***актуальную информацию о проекте***, его ***функциональности***, ***инструкции по установке*** и ***использованию***, а также другую полезную информацию для **разработчиков** и **пользователей**.
* Это важный компонент документации, который помогает улучшить понимание проекта и содействует его успешному использованию.

##### _____________________________________


### Структура базы данных:

![0001 _ 00.png](image%2F0001%20_%2000.png)

##### _____________________________________

а также "облегченная" версия (without User table):

![0001.png](image%2F0001.png)

##### _____________________________________

## P.S.

#### Та часть курса, которую каждый из нас понял по своему:

![photo_2024-02-28_09-33-12.jpg](image%2Fphoto_2024-02-28_09-33-12.jpg)

* :-)

##### _____________________________________

**Create** by: **Andrey Koval** (57)

**Date**: 2024-02-29

**Version**: 01.00

##### _____________________________________
