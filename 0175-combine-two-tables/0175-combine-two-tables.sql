# Write your MySQL query statement below
SELECT firstName,lastName,city,state FROM  person LEFT Join address on Person.personId=Address.personId;