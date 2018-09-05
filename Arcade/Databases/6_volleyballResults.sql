/*Please add ; after each select statement*/
CREATE PROCEDURE volleyballResults()
BEGIN
	select name,country,scored,missed,wins from results order by wins;
END