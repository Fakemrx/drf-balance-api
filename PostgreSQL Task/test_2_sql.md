 # Тестовое задание SQL   
Вам дана база данных ноутбуков, которая содержит две таблицы. Таблица notebooks\_brand содержит данные о наименовании брендов ноутбуков. Таблица notebooks\_notebook содержит данные о наименовании ноутбука, его диагонали, ширине, глубине и высоте, а также имеет ссылку на бренд, к которому относится данная модель.   
   
Задание:   
1. Напишите запрос, который подсчитает какое количество ноутбуков представлено в каждом бренде. Отсортируйте данные по убыванию.
(PSQL сам чуток реформатнул)

 SELECT notebooks_brand.title,
    count(notebooks_notebook.brand_id) AS count
   FROM notebooks_brand
     JOIN notebooks_notebook ON notebooks_brand.id = notebooks_notebook.brand_id
  GROUP BY notebooks_brand.title
  ORDER BY (- count(notebooks_notebook.brand_id));
   
2. Вам необходимо выделить группы ноутбуков по размерам. Для этого размеры предварительно нужно округлить в большую сторону до ближайшего 0 или 5 и затем сгруппировать по одинаковым размерам, подсчитав количество ноутбуков в каждой группе. Отсортируйте данные по размерам.   
(PSQL сам чуток реформатнул)

 SELECT
        CASE
            WHEN (ceiling(notebooks_notebook.width::numeric) % 10::numeric) >= 1::numeric AND (ceiling(notebooks_notebook.width::numeric) % 10::numeric) <= 4::numeric THEN round(notebooks_notebook.width::numeric, '-1'::integer) + 5::numeric
            WHEN (ceiling(notebooks_notebook.width::numeric) % 10::numeric) >= 6::numeric AND (ceiling(notebooks_notebook.width::numeric) % 10::numeric) <= 9::numeric THEN round(notebooks_notebook.width::numeric, '-1'::integer)
            ELSE ceiling(notebooks_notebook.width::numeric)
        END AS width_result,
        CASE
            WHEN (ceiling(notebooks_notebook.depth::numeric) % 10::numeric) >= 1::numeric AND (ceiling(notebooks_notebook.depth::numeric) % 10::numeric) <= 4::numeric THEN round(notebooks_notebook.depth::numeric, '-1'::integer) + 5::numeric
            WHEN (ceiling(notebooks_notebook.depth::numeric) % 10::numeric) >= 6::numeric AND (ceiling(notebooks_notebook.depth::numeric) % 10::numeric) <= 9::numeric THEN round(notebooks_notebook.depth::numeric, '-1'::integer)
            ELSE ceiling(notebooks_notebook.depth::numeric)
        END AS depth_result,
        CASE
            WHEN (ceiling(notebooks_notebook.height::numeric) % 10::numeric) >= 1::numeric AND (ceiling(notebooks_notebook.height::numeric) % 10::numeric) <= 4::numeric THEN round(notebooks_notebook.height::numeric, '-1'::integer) + 5::numeric
            WHEN (ceiling(notebooks_notebook.height::numeric) % 10::numeric) >= 6::numeric AND (ceiling(notebooks_notebook.height::numeric) % 10::numeric) <= 9::numeric THEN round(notebooks_notebook.height::numeric, '-1'::integer)
            ELSE ceiling(notebooks_notebook.height::numeric)
        END AS height_result,
    count(notebooks_notebook.title) AS count_result
   FROM notebooks_notebook
  GROUP BY width_result, depth_result, height_result
  ORDER BY width_result, depth_result, height_result, count_result;
   
СУБД: PostgreSQL   
Дамп БД: test\_db.dump   
В качестве решения принимаются SQL запросы, которые можно разместить в отдельном файле в репозитории, вместе с первой частью тестового задания. Дамп базы и пример ответов размещать не нужно.   
