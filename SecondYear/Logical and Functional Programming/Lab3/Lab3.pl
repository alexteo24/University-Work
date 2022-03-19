replaceOccurences([], _, _, []).
replaceOccurences([H|T], E, X, [X|R]):-
    H == E, !,
    replaceOccurences(T, E, X, R).

replaceOccurences([H|T], E, X, [H|R]):-
    H \== E,
    replaceOccurences(T, E, X, R).


getMaximum([M], M).
getMaximum([H|T], M):-
    is_list(H), !,
    getMaximum(T, M).
getMaximum([H|T], H):-
    getMaximum(T, M),
    H > M, !.
getMaximum([H|T], M):-
    getMaximum(T, M),
    H =< M.

replaceInSublists([], _, []).
replaceInSublists([H|T], Max, [R|Res]) :- 
    is_list(H), !,
    getMaximum(H, MaxSub),
    replaceOccurences(H, Max, MaxSub, R),
    replaceInSublists(T, Max, Res).
replaceInSublists([H|T], Max, [H|Res]) :-
    replaceInSublists(T, Max, Res).

replaceInSublists(List, ResultList) :-
    getMaximum(List, Max),
    replaceInSublists(List, Max, ResultList), !.