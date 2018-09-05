/*Please add ; after each select statement*/
CREATE PROCEDURE projectsTeam()
BEGIN
	select DISTINCT name from projectLog order by name; 
END