# 第一次
+ 
```
SELECT book_name 
    FROM 
	    (
            SELECT t_book.book_name,c.num FROM 
                (SELECT book_id,COUNT(*) as num 
                        FROM t_borrow 
                        LEFT JOIN t_reader 
                        on t_borrow.reader_id=t_reader.reader_id 
                        WHERE gender='女' 
                        GROUP BY book_id
                )as c 
            left join t_book on c.book_id=t_book.book_id
        ) as d 
	WHERE d.num = 
        (
            SELECT MAX(e.num) FROM 
                (SELECT book_id,COUNT(*) as num 
                        FROM t_borrow 
                        LEFT JOIN t_reader 
                        on t_borrow.reader_id=t_reader.reader_id 
                        WHERE gender='女' 
                        GROUP BY book_id
                )as e 
        )
; 
```
```
SELECT book_name 
    FROM 
	    (
            SELECT t_book.book_name,c.num FROM 
                (SELECT book_id,COUNT(*) as num 
                        FROM t_borrow 
                        LEFT JOIN t_reader 
                        on t_borrow.reader_id=t_reader.reader_id 
                        WHERE gender='女' 
                        GROUP BY book_id
                )as c 
            left join t_book on c.book_id=t_book.book_id
        ) as d 
	WHERE d.num = 
        (
            SELECT MAX(e.num) FROM 
                (SELECT book_id,COUNT(*) as num 
                        FROM t_borrow 
                        LEFT JOIN t_reader 
                        on t_borrow.reader_id=t_reader.reader_id 
                        WHERE gender='男' 
                        GROUP BY book_id
                )as e 
        )
;
```
+
```
SELECT * FROM t_book WHERE book_id = (SELECT d.book_id from (SELECT book_id,COUNT(*) as num  FROM t_borrow GROUP BY book_id) as d
WHERE d.num = (SELECT max(c.num) FROM (SELECT book_id,COUNT(*) as num  FROM t_borrow GROUP BY book_id) as c));
``` 
+
```
SELECT reader_id from (select reader_id,count(*) as num  from t_borrow GROUP BY reader_id) as c 
WHERE c.num = (SELECT max(num) FROM (select reader_id,count(*) as num  from t_borrow GROUP BY reader_id) as d);
```
+ 
``` 
SELECT publisher from (select publisher,count(*) as num  from t_book GROUP BY publisher) as c 
WHERE c.num = (SELECT max(num) FROM (select publisher,count(*) as num  from t_book GROUP BY publisher) as d);
```
+ 
``` 
ELECT gender as num FROM t_borrow LEFT JOIN t_reader on t_borrow.reader_id=t_reader.reader_id GROUP BY gender ORDER BY num LIMIT 1;
```
+ 
```
SELECT name FROM t_reader
WHERE reader_id=
(SELECT reader_id FROM (SELECT reader_id,COUNT(*) as num  FROM t_borrow GROUP BY reader_id) as d 
WHERE d.num = (SELECT MAX(num) FROM (SELECT reader_id,COUNT(*) as num  FROM t_borrow GROUP BY reader_id) as c)) 
```
+ 
``` 
SELECT tc.classification_name,count(*) as num  FROM t_book_classification as tc LEFT JOIN t_book
on tc.classification_symbol=t_book.classification_symbol GROUP BY tc.classification_symbol;
```
+ 
``` 
SELECT name,publisher FROM (SELECT reader_id,publisher FROM t_borrow LEFT JOIN t_book on t_borrow.book_id=t_book.book_id)  as c LEFT JOIN t_reader on c.reader_id=t_reader.reader_id; 
```
+ 
```
SELECT type_name FROM
(SELECT reader_type_id,count(*) as num FROM t_borrow LEFT JOIN t_reader on t_borrow.reader_id=t_reader.reader_id GROUP BY reader_type_id) as c LEFT JOIN t_reader_type on c.reader_type_id=t_reader_type.reader_type_id ORDER BY num DESC LIMIT 1;
```