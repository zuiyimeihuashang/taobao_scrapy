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