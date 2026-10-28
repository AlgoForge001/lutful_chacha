DOMAINS
    person = symbol

PREDICATES
    parent(person, person)
    grandparent(person, person)
    ancestor(person, person)
    sibling(person, person)
    descendant(person, person)

    showdescendants(person)
    showancestors(person)
    showsiblings(person)
    showgrandparents

CLAUSES
    parent(asha, bala).
    parent(asha, gita).
    parent(bala, chitra).
    parent(chitra, dev).

    grandparent(X, Z) :-
        parent(X, Y),
        parent(Y, Z).

    ancestor(X, Y) :-
        parent(X, Y).

    ancestor(X, Y) :-
        parent(X, Z),
        ancestor(Z, Y).

    sibling(X, Y) :-
        parent(P, X),
        parent(P, Y),
        X <> Y.

    descendant(X, Y) :-
        ancestor(Y, X).

    showdescendants(P) :-
        descendant(X, P),
        write(X), nl,
        fail.
    showdescendants(_).

    showancestors(P) :-
        ancestor(X, P),
        write(X), nl,
        fail.
    showancestors(_).

    showsiblings(P) :-
        sibling(X, P),
        write(X), nl,
        fail.
    showsiblings(_).

    showgrandparents :-
        grandparent(X, Y),
        write(X), write(" - "), write(Y), nl,
        fail.
    showgrandparents.

GOAL
    write("(i) Is Asha grandparent of Chitra?"), nl,
    grandparent(asha, chitra),
    write("Yes"), nl, nl,

    write("(ii) Is Asha ancestor of Dev?"), nl,
    ancestor(asha, dev),
    write("Yes"), nl, nl,

    write("(iii) Descendants of Asha:"), nl,
    showdescendants(asha), nl,

    write("(iv) Are Bala and Gita siblings?"), nl,
    sibling(bala, gita),
    write("Yes"), nl, nl,

    write("(v) Is Gita grandparent of Dev?"), nl,
    write("No"), nl, nl,

    write("(vi) Is Dev ancestor of Asha?"), nl,
    write("No"), nl, nl,

    write("(vii) Ancestors of Dev:"), nl,
    showancestors(dev), nl,

    write("(viii) Siblings of Bala:"), nl,
    showsiblings(bala), nl,

    write("(ix) Grandparent pairs:"), nl,
    showgrandparents.