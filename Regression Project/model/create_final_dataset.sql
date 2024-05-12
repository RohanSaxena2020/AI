SELECT 
    a.PLAYER_ID,
    a.PLAYER_NAME,
    a.scoring_average,
    b.SG_OTT,
    c.SG_APP,
    d.SG_ATG,
    e.SG_PUTTING
FROM 
    scoring_averages a
JOIN 
    sg_off_the_tee b ON a.PLAYER_ID = b.PLAYER_ID
JOIN
	sg_approach c ON a.PLAYER_ID = c.PLAYER_ID
JOIN 
    sg_around_the_green d ON a.PLAYER_ID = d.PLAYER_ID
JOIN 
    sg_putting e ON a.PLAYER_ID = e.PLAYER_ID;
