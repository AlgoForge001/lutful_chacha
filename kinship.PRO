
DOMAINS
    person = symbol

PREDICATES
    male(person)
    female(person)
    parent(person, person)
    father(person, person)
    mother(person, person)
    sibling(person, person)
    brother(person, person)
    sister(person, person)
    cousin(person, person)
    uncle(person, person)
    aunt(person, person)
    ancestor(person, person)
    grandchild(person, person)
    secondcousin(person, person)
    relative(person, person)

    showcousins(person)
    showancestors(person)
    showsecondcousins(person)
    showrelatives(person)
    showgrandchildren(person)
    showsiblings(person)
    showauntedpersons(person)

CLAUSES
    % Gender facts
    male(ali).
    male(umar).
    male(ahmed).
    male(raza).

    female(fatima).
    female(aisha).
    female(sara).
    female(nadia).
    female(zoya).

    % Parent facts
    parent(ali, umar).
    parent(ali, fatima).

    parent(umar, ahmed).
    parent(umar, aisha).

    parent(fatima, sara).
    parent(fatima, raza).

    parent(ahmed, zoya).
    parent(sara, nadia).

    % Father and mother
    father(X, Y) :-
        male(X), parent(X, Y).

    mother(X, Y) :-
        female(X), parent(X, Y).

    % Siblings
    sibling(X, Y) :-
        parent(P, X),
        parent(P, Y),
        X <> Y.

    brother(X, Y) :-
        male(X), sibling(X, Y).

    sister(X, Y) :-
        female(X), sibling(X, Y).

    % First cousins
    cousin(X, Y) :-
        parent(P1, X),
        parent(P2, Y),
        sibling(P1, P2),
        X <> Y.

    % Uncle and aunt
    uncle(X, Y) :-
        male(X),
        sibling(X, P),
        parent(P, Y).

    aunt(X, Y) :-
        female(X),
        sibling(X, P),
        parent(P, Y).

    % Ancestors
    ancestor(X, Y) :-
        parent(X, Y).

    ancestor(X, Y) :-
        parent(X, Z),
        ancestor(Z, Y).

    % Grandchildren
    grandchild(X, Y) :-
        parent(Y, Z),
        parent(Z, X).

    % Second cousins: children of first cousins
    secondcousin(X, Y) :-
        cousin(P1, P2),
        parent(P1, X),
        parent(P2, Y),
        X <> Y.

    % Relatives: ancestors, descendants, siblings,
    % cousins, aunts and uncles in both directions
    relative(X, Y) :-
        ancestor(X, Y).

    relative(X, Y) :-
        ancestor(Y, X).

    relative(X, Y) :-
        sibling(X, Y).

    relative(X, Y) :-
        cousin(X, Y).

    relative(X, Y) :-
        uncle(X, Y).

    relative(X, Y) :-
        uncle(Y, X).

    relative(X, Y) :-
        aunt(X, Y).

    relative(X, Y) :-
        aunt(Y, X).

    % Display cousins
    showcousins(P) :-
        cousin(X, P),
        write(X), nl,
        fail.

    showcousins(_).

    % Display ancestors
    showancestors(P) :-
        ancestor(X, P),
        write(X), nl,
        fail.

    showancestors(_).

    % Display second cousins
    showsecondcousins(P) :-
        secondcousin(X, P),
        write(X), nl,
        fail.

    showsecondcousins(_).

    % Display relatives
    showrelatives(P) :-
        relative(X, P),
        write(X), nl,
        fail.

    showrelatives(_).

    % Display grandchildren
    showgrandchildren(P) :-
        grandchild(X, P),
        write(X), nl,
        fail.

    showgrandchildren(_).

    % Display siblings
    showsiblings(P) :-
        sibling(X, P),
        write(X), nl,
        fail.

    showsiblings(_).

    % Display persons of whom P is an aunt
    showauntedpersons(P) :-
        aunt(P, X),
        write(X), nl,
        fail.

    showauntedpersons(_).

GOAL
    write("a) Cousins of Ahmed:"), nl,
    showcousins(ahmed),

    write("b) Ancestors of Sara:"), nl,
    showancestors(sara),

    write("c) Second cousins of Nadia:"), nl,
    showsecondcousins(nadia),

    write("d) Relatives of Sara:"), nl,
    showrelatives(sara),

    write("e) Grandchildren of Ali:"), nl,
    showgrandchildren(ali),

    write("f) Siblings of Sara:"), nl,
    showsiblings(sara),

    write("g) Persons of whom Aisha is an aunt:"), nl,
    showauntedpersons(aisha).
