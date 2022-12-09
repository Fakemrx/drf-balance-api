# xone-test-project

"Менеджер учёта расходов"   
Необходимо реализовать API для учета расходов пользователя.   

* В приложении, в файле settings.py была включена 'rest_framework.authentication.SessionAuthentication' для того, чтобы можно было увидеть, что при входе в
аккаунт пользователю в выпадающем списке категорий доступны только его собственные, а не все категории.

Рекомендация к использованию/проверке: Действия лучшк тестировать через Postman, там можно указать токен юзера.

Минимальные требования:   
- Регистрация пользователя /auth/users/ *Djoser
- Авторизация пользователя (по токену) /auth/token/login/ *Djoser - Через Postman так можно создавать транзакции, токен можно получить и в браузере
- Транзакции пользователя - CRUD /transactions/create - создание; /transactions/rud/ID - просмотр транзакции, изменение, удаление
- С помощью транзакций происходит списание, начисление баланса пользователя. *Учтено, однако для пополнения баланса пользователя надо это делать через админку, либо
создавать транзакции с отрицательным балансом (не было четких критериев по этому поводу).
- Транзакция должна содержать в себе: сумму\*, время\*, категорию\*, организацию\*, описание. *Учтено
- Пользователь должен иметь возможность сортировать, фильтровать транзакции по времени, сумме, дате. *Учтено, фильтрация и отображение всех транзакций (текущего 
пользователя) /transactions/list/ , для сортировки по указанным параметрам надо указать доп параметр /transactions/list/?sort=<payment_amount/date/time>, если
надо сортировку в обратную сторону, то перед названием поля надо поставить '-' /transactions/list/?sort=-<payment_amount/date/time>

Дополнительные требования:
- При регистрации пользователь получает набор стандартных категорий:
"Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина", "Образование", "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд".
- Просмотр профиля пользователя (информация о текущем балансе)  /auth/users/me/ 
- Статистика пользователя. /auth/users/me/

Нефункциональные требования:   
- Язык программирования: Python 3.10+   
- DRF 3+   
- Соответствие исходного кода PEP 8   
