% a) Write a predicate to remove all occurrences of a certain atom from a list.

%removeOccurencesElem(L - list, E - int, R - list)
%flow model: (i, i, o), (i, i, i)
%L - the initial list
%E - the element we want to remove
%R - the list after removing all occurences of the element E

removeOccurencesElem([], _, []).
removeOccurencesElem([], _, R).
removeOccurencesElem([H|T], E, R):-
    H =:= E,
    removeOccurencesElem(T, E, R).
removeOccurencesElem([H|T], E, [H|R]):-
    H =\= E,
    removeOccurencesElem(T, E, R).

% b) b. Define a predicate to produce a list of pairs (atom n) from an initial list of atoms. In this initial list atom has n occurrences. 
% Eg.: numberatom([1, 2, 1, 2, 1, 3, 1], X) => X = [[1, 4], [2, 2], [3, 1]]. 


%countOcc(L - list, E - int, R - int)
%flow model: (i, i, o), (i, i, i)
%L - the list in which we want to search the element
%E - the element we want to search
%R - the number of occurences of that element
countOcc([], _, 0).
countOcc([H|T], E, R1):-
    H == E,
    countOcc(T, E ,R),
    R1 is R+1.


countOcc([H|T], E, R):-
    H \== E,
    countOcc(T, E ,R).


%occurencesElements(L - list, C -list, R - list)
%flow model: (i, i, o), (i, i, i)
%L - the list we want to calculate the frequency of
%C - list of the elements for which we have already computed the frequency
%R - the list containing the frequency of the elements
occurencesElements([],_,[]).
occurencesElements([H|T], CountedElems, [[H,Count]|Result]) :-
    countOcc(CountedElems,H,IsCounted),
    IsCounted =:= 0,
    countOcc([H|T],H,Count),
    occurencesElements(T, [H|CountedElems],Result).
occurencesElements([H|T], [H1|T1], Result) :-
    countOcc([H1|T1],H,IsCounted),
    IsCounted =\= 0,
    occurencesElements(T,[H1|T1],Result).

occurencesElements(List,Result) :- occurencesElements(List, [], Result).


