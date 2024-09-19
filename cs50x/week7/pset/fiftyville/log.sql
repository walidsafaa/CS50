-- Keep a log of any SQL queries you execute as you solve the mystery.
-- SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2021 AND street = 'Humphrey Street';

--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--Interviews were conducted today with three witnesses who were present at the time –
--each of their interview transcripts mentions the bakery.

--SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2021;
--259 | 2021 | 7     | 28  | 10   | 14     | entrance | 13FNH73
--260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95


--Interviews:
--| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and
-- drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

 --| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning,
 --before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = 'Leggett Street';

 --| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
 --In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
 --The thief then asked the person on the other end of the phone to purchase the flight ticket. |
 -- SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;



SELECT DISTINCT(people.name), phone_calls.caller
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN phone_calls ON phone_calls.caller = people.phone_number
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE
people.phone_number IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60)
AND
people.id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = 'Leggett Street'))
AND
people.passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND
people.license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute > 15 AND minute < 30)
