absoluteDifference(A, B, R):-
    A > B,!,
    R is A - B.
absoluteDifference(A, B, R):-
    R is B - A.

%checkSequence([_],_).
checkSequence([H1, H2], M):-
    absoluteDifference(H1, H2, R),
    R >= M, !.
checkSequence([H1, H2|T], M) :-
    absoluteDifference(H1, H2, R),
    R >= M,
    checkSequence([H2|T], M).

% generateSequences(N, _, I, []) :- I =:= N + 1, !.
% generateSequences(N, M, I, [I|R]) :-
%     I =< N,
%     J is I + 1,
%     generateSequences(N, M, J, R),
%     checkSequence([I|R], M).
% generateSequences(N, M, I, R) :-
%     I =< N,
%     J is I + 1,
%     generateSequences(N, M, J, R).
% this also gets the 1 element solutions, which i think it's not ok

generateSequence(N, I, []) :- I =:= N + 1, !.
generateSequence(N, I, [I|R]) :-
    I =< N,
    J is I + 1,
    generateSequence(N, J, R).
generateSequence(N, I, R):-
    I =< N,
    J is I + 1,
    generateSequence(N, J, R).

onesolution(N, M, R) :-
    generateSequence(N, 1, R),
    checkSequence(R, M).

allsolutions(N, M, R) :-
    findall(RPartial, onesolution(N, M, RPartial), R).
