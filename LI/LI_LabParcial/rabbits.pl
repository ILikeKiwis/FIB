%% ----------- [2 points] ---------- %%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% We want to visually represent the Fibonacci numbers as mating rabbit pairs
% in the following way: 'y' represents a young rabbit pair not yet able
% to mate (this only happens its first month).
% From the second month on, this pair becomes adult and is represented by 'a'.
% Each available adult pair produces a young pair every month.
% No rabbit ever dies in this scheme.
%
% In the base case, the first month only one young pair exists, it is
% represented with the sequence [y], and in the second month the same pair
% would be now adult, with the sequence [a].
% By default, adult pairs are listed first in these sequences.
% As an example, the only correct sequence corresponding to the 5th month
% would be [a,a,a,y,y].
%
% Define a predicate f(+N,?S) that, given a positive integer N, succeeds
% if S is the sequence corresponding to the N-th month, or, if S is
% a variable, generates the sequence corresponding to the N-th month
% with the adult pairs first and then any young pairs.
%
%   ?- f(1, S).
%   S = [y].
%
%   ?- f(2, S).
%   S = [a].
%
%   ?- f(5, S).
%   S = [a, a, a, y, y].

% 1 -> y  2 -> a   3 -> a y 4 -> a a y  5 -> a a a y y  6 -> y y y a a a a a 
%
% Hint: you can know how many young and adult pairs are in each generation by
% counting previous Fibonacci numbers.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% fib(+N, ?F) holds if F is the N-th number in the fibbonacci sequence
fib(1, 1):- !.
fib(2, 1):- !.
fib(N, F) :-
    N > 2,
    N1 is N-1,
    N2 is N-2,
    fib(N1, F1),
    fib(N2, F2),
    F is F1 + F2.
% listOf(+X, +N, ?L)
%      given an arbitrary element X and an integer number N,
%      holds if L is a list of length N full of elements X.
%      It can check if L is such a list, or instantiate L.
%      The predicate must fail if N is negative.
listOf(_, 0, []) :- !.
listOf(X, N1, [H|T]) :-
    N1 > 0,
    N is N1-1, 
    H = X,
    listOf(X, N, T).  


% f(+N, ?S)
%       succeeds if S is the sequence corresponding to the N-th month, or, if S
%       is not instantiated (is a variable), generates that sequence with the
%       adult pairs first and then any young pairs.
f(1, [y]) :- !.
f(2, [a]) :- !.
f(N, S) :- 
    N > 2, 
    N1 is N-1,
    N2 is N-2,
    fib(N1, F1),    %% Num adults
    fib(N2, F2),    %% Num fills
    listOf(a, F1, H),
    listOf(y, F2, T),
    append(H, T, S).



