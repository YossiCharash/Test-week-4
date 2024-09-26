

select count(air_force)as max,air_force
from mission top
group by air_force
order by max desc limit 1;

-- זה מביא את חיל האויר שמביא שעשה את מספר התקיפות בשנה הגדול ביותר
select count(air_force)as max,air_force
from mission top
where date_part('year', mission_date) = 1944
group by air_force
order by max desc limit 1;

-- כאן בדקתי את האינדק ומה הוא מביא לי
CREATE INDEX air_index
ON mission(air_force);

CREATE INDEX location_and_detels
ON mission(location_and_city_id);


explain analyse select missions_wwii.public.mission.location_and_city_id
from mission
where missions_wwii.public.mission.location_and_city_id = 35

