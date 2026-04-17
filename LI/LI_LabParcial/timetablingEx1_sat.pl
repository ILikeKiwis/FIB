%% There are 2 days: 1 and 2.
numDays(2).

%% There are 3 venues: 1, 2 and 3.
numVenues(3).

%% There are 4 activities.
%% E.g., activity 1 needs at least 3 people and can take place from day 1 to day 2 at venues 2 or 3.
activity(1, 3, 1, 2, [2, 3]).
activity(2, 2, 1, 1, [2, 3]).
activity(3, 1, 1, 2, [1, 3]).
activity(4, 2, 2, 2, [1, 2]).

%% There are 5 people.
%% E.g., person 1 can do activities 1, 2, 3.
person(1, [1, 2, 3]).
person(2, [2]).
person(3, [2, 3]).
person(4, [1, 4]).
person(5, [1, 2, 3, 4]).
