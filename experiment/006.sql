CREATE DEFINER=`skip-grants user`@`skip-grants host` FUNCTION `check_num`(book_name varchar(20)) RETURNS char(11) CHARSET utf8mb4 COLLATE utf8mb4_vietnamese_ci
BEGIN
declare singer int;
set singer = (select sum(num) from t_book where book_name = book_name);
-- RETURN singer;
if singer > 0 then
return 'YES';
else
return 'NO';
end if;
END