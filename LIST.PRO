

DOMAINS
    ilist = integer*

PREDICATES
    sumlist(ilist, integer)
    lengthlist(ilist, integer)
    concatlist(ilist, ilist, ilist)
    memberlist(integer, ilist)
    displaylist(ilist)
    deleteitem(integer, ilist, ilist)

CLAUSES
    sumlist([], 0).
    sumlist([H|T], S) :-
        sumlist(T, R),
        S = H + R.

    lengthlist([], 0).
    lengthlist([_|T], N) :-
        lengthlist(T, R),
        N = R + 1.

    concatlist([], L, L).
    concatlist([H|T], L, [H|R]) :-
        concatlist(T, L, R).

    memberlist(X, [X|_]).
    memberlist(X, [_|T]) :-
        memberlist(X, T).

    displaylist([]).
    displaylist([H|T]) :-
        write(H), write(" "),
        displaylist(T).

    deleteitem(_, [], []).
    deleteitem(X, [X|T], R) :-
        deleteitem(X, T, R).
    deleteitem(X, [H|T], [H|R]) :-
        X <> H,
        deleteitem(X, T, R).

GOAL
    sumlist([1,2,3,4,5], S),
    write("Sum = "), write(S), nl,

    lengthlist([1,2,3,4,5], N),
    write("Length = "), write(N), nl,

    concatlist([1,2], [3,4], C),
    write("Concatenated List = "),
    displaylist(C), nl,

    memberlist(3, [1,2,3,4]),
    write("3 is present"), nl,

    write("Original List = "),
    displaylist([1,2,3,4,5]), nl,

    deleteitem(3, [1,2,3,4,5], D),
    write("After Deletion = "),
    displaylist(D).
