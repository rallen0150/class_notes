SELECT carrot_ball_team.city from carrot_ball_player
inner join carrot_ball_team
  on carrot_ball_player.team = carrot_ball_team.id
where carrot_ball_player.name = 'Robbie Allen';


select cbp.* from carrot_ball_player cbp
INNER JOIN carrot_ball_team cbt
  on cbp.team = cbt.id
where cbt.city = 'Chicago';

select * from carrot_ball_player
where number < 20;

update carrot_ball_team
set champion = FALSE;

update carrot_ball_team
set champion = TRUE
where id = 4;

UPDATE carrot_ball_team
set champion = True
where city = 'Chicago';

DELETE from carrot_ball_player
where name = 'Bill Walsh';