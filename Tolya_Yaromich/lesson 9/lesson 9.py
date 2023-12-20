1
SELECT name  FROM passenger 
2
SELECT name FROM company 
3
SELECT *
FROM Trip
WHERE Trip.town_from  = 'Москва';  !!!!!!!
4
SELECT  Passenger.name 
FROM  Passenger
WHERE name  LIKE '%man%';

5
SELECT COUNT(*) as count
FROM Trip
WHERE plane = 'TU-134'; !!!!!!!
6
SELECT DISTINCT  Company.name 
FROM Trip
JOIN Company ON Trip.company  = Company.id
WHERE Trip.plane   = 'Boeing';
7
SELECT DISTINCT plane 
FROM Trip
WHERE town_to  = 'Moscow';
8
SELECT town_to ,TIME_FORMAT(TIMEDIFF(time_in , time_out ), '%H:%i:%s') AS flight_time
FROM Trip
WHERE town_from = 'Paris';
9
SELECT DISTINCT  Company.name 
FROM Trip
JOIN Company ON Trip.company  = Company.id
WHERE Trip.town_from = 'Vladivostok';
10
SELECT * 
FROM Trip
WHERE time_out  >= '1900-01-01T10:00:00.000Z'
    AND time_out  <=  '1900-01-01T14:00:00.000Z'
11
SELECT name
FROM Passenger
WHERE LENGTH(name) = (SELECT MAX(LENGTH(name)) FROM Passenger);
12
SELECT Pass_in_trip.trip, COUNT(Pass_in_trip.passenger) AS count
FROM Pass_in_trip
JOIN Trip ON Trip.id = Pass_in_trip.trip 
WHERE Trip.time_in < NOW()
GROUP BY Pass_in_trip.trip;
13
SELECT DISTINCT  name
FROM Passenger
GROUP BY name
HAVING COUNT(*) > 1;
14
SELECT DISTINCT Trip.town_to
FROM Trip
JOIN Pass_in_trip ON Pass_in_trip.trip =Trip.id
JOIN Passenger ON Passenger.id  = Pass_in_trip.passenger  
WHERE Passenger.name = 'Bruce Willis';

15
SELECT time_in 
FROM Trip
JOIN Pass_in_trip ON Pass_in_trip.trip =Trip.id
JOIN Passenger ON Passenger.id  = Pass_in_trip.passenger  
WHERE Passenger.name = 'Steve Martin' AND 
Trip.town_to = 'London'
16
SELECT Passenger.name, COUNT(Pass_in_trip.trip) AS count
FROM Trip
JOIN Pass_in_trip ON Pass_in_trip.trip = Trip.id
JOIN Passenger ON Passenger.id = Pass_in_trip.passenger
GROUP BY Passenger.name
HAVING count > 0
ORDER BY count DESC, Passenger.name ASC;
17 
SELECT FamilyMembers.member_name, FamilyMembers.status, SUM(Payments.unit_price*Payments.amount ) as costs
FROM FamilyMembers
JOIN Payments ON FamilyMembers.member_id = Payments.family_member
WHERE YEAR(Payments.date) = 2005
GROUP BY FamilyMembers.member_name, FamilyMembers.status
HAVING costs > 0;

18
SELECT member_name
FROM FamilyMembers
ORDER BY birthday ASC
LIMIT 1;
19
SELECT DISTINCT FamilyMembers.status 
FROM FamilyMembers
JOIN Payments ON FamilyMembers.member_id = Payments.family_member
JOIN Goods ON Goods.good_id = Payments.good
WHERE Goods.good_name = "potato"
20
SELECT FamilyMembers.status ,FamilyMembers.member_name ,SUM(Payments.unit_price*Payments.amount ) as costs
FROM FamilyMembers
JOIN Payments ON FamilyMembers.member_id = Payments.family_member
JOIN Goods ON Goods.good_id = Payments.good
JOIN GoodTypes ON GoodTypes.good_type_id  = Goods.type
WHERE GoodTypes.good_type_name = 'entertainment'
GROUP BY FamilyMembers.status, FamilyMembers.member_name;
21
SELECT DISTINCT Goods.good_name 
FROM FamilyMembers
JOIN Payments ON FamilyMembers.member_id = Payments.family_member
JOIN Goods ON Goods.good_id = Payments.good
GROUP BY Goods.good_name
HAVING COUNT(Payments.good) > 1;

22
SELECT member_name 
FROM FamilyMembers
WHERE status = "mother"
23
SELECT Goods.good_name ,unit_price 
FROM FamilyMembers
JOIN Payments ON FamilyMembers.member_id = Payments.family_member
JOIN Goods ON Goods.good_id = Payments.good
JOIN GoodTypes ON GoodTypes.good_type_id  = Goods.type
WHERE GoodTypes.good_type_name = 'delicacies' 
ORDER BY unit_price  DESC
LIMIT 1;

24
SELECT FamilyMembers.member_name, SUM(Payments.unit_price * Payments.amount) as costs
FROM FamilyMembers
JOIN Payments ON FamilyMembers.member_id = Payments.family_member
WHERE YEAR(Payments.date) = 2005 AND MONTH(Payments.date) = 06
GROUP BY FamilyMembers.member_name;

25
SELECT DISTINCT Goods.good_name
FROM Goods
WHERE Goods.good_id NOT IN (
    SELECT DISTINCT Payments.good
    FROM Payments
    WHERE YEAR(Payments.date) = 2005
);
