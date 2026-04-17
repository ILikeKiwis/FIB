%% ----------- [3 points] ---------- %%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% We want to partition a list of integers L = [x_1, x_2, ..., x_n]
%% into consecutive (non-empty) subsequences L_1, ..., L_k such that
%% the concatenation of all L_i is equal to L.
%% The number k of subsequences in the partition is said to be its "size".
%%
%% Let S_i denote the sum of the elements of the subsequence L_i.
%% The following additional constraints must be fulfilled to be a "valid" partition:
%%   C_incre: S_i >= S_{i-1}, for 1 < i <= k, 
%%   C_first: S_1 >= x_1,     where x_1 is the first element of L
%%
%% For example, if L = [4,7,-2,8,8], seven partitions satisfy these constraints.
%% The predicate sortedPartitions(+L) writes them in decreasing order of "size"
%% NOTE: the order among partitions of the same size is unspecified
%%     ?- sortedPartitions([4,7,-2,8,8]).
%%     4->[[4],[7,-2],[8],[8]]    %% 1 partition  with 4 subsequences (k = 4)
%%     3->[[4],[7],[-2,8,8]]      %% 2 partitions with 3 subsequences (k = 3)
%%     3->[[4],[7,-2],[8,8]]      %%                   3
%%     2->[[4],[7,-2,8,8]]        %% 3 partitions with 2 subsequences (k = 2)
%%     2->[[4,7],[-2,8,8]]        %%                   2
%%     2->[[4,7,-2],[8,8]]        %%                   2
%%     1->[[4,7,-2,8,8]]          %% 1 partition  with 1 subsequence  (k = 1)
%%     true.
%% Some lists, for example [5,-3,2], cannot be partitioned under these constraints.
%%
%% COMPLETE the predicates subseqs/2, subseqsGE/3, and sortedPartitions/1.
%% The predicate sum_list/2 can be used.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% subseqs(+L, ?LS)
%%     given a list of integers L,
%%     it holds if LS is a partition of L satisfying constraints C_incre and C_first.
%%     If L is empty, then LS is also the empty list.
%%     It can also be used to generate, under backtracking, all valid partitions.
%%     NOTE: in any order, and without repetitions.
subseqs([], []).
subseqs([X|L], LS) :-        %% TO BE COMPLETED
    
    subseqsGE(...).


%% subseqsGE(+N, +L, ?LS)
%%     Given an integer N and a list of integers L,
%%     it holds if LS is a partition of L such that
%%       * the constraint C_incre holds (S_i >= S_{i-1}, for 1 < i <= k),
%%       * S_1 >= N (the first subsequence in LS must have sum >= N).
%%     If L is empty, then LS is also the empty list.
%%     It can also be used to generate, under backtracking, all valid partitions.
%%     NOTE: in any order, and without repetitions.
subseqsGE(_, [], []) :- !.
subseqsGE(N, L, ...) :-      %% TO BE COMPLETED
    append(L1, L2, L),
    ...

%% sortedPartitions(+L) 
%%     Writes all "valid" partitions of the list of integers L in decreasing
%%     order of size (decreasing number of subsequences): if the lenght of L is N,
%%     it first writes the partition with N subsequences (if it is valid), then 
%%     those with N-1, ..., and finally, the partition with only 1 subsequence.
%%   This predicate always succeeds.
%%   NOTE: The order among partitions of the same size is unspecified.
sortedPartitions(L) :-       %% TO BE COMPLETED
    length(L, N),
    between(1, N, K),
    NK1 is ...,
    ...
    write(NK1->LS), nl,
    ...
...

