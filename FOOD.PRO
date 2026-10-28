DOMAINS
    person, food = symbol

PREDICATES
    likes(person, food)
    fooditem(food)
    eats(person, food)
    alive(person)
    showfoods


CLAUSES
    % 1. John likes all food
    likes(john, X) :-
        fooditem(X).

    % 2. Basic food items
    fooditem(apple).
    fooditem(vegetable).
    fooditem(mango).
    fooditem(grape).
    fooditem(peanuts).
    fooditem(rice).

    % 3. Anil eats these foods
    eats(anil, burger).
    eats(anil, cheese).
    eats(anil, poha).
    eats(anil, oatmeal).
    eats(anil, barley).
    eats(anil, carrot).

    % 4. What a living person eats is food
    fooditem(F) :-
        eats(P, F), alive(P).

    % 5. Chicken is food
    fooditem(chicken).

    % 6. Whatever Anil eats is food
    fooditem(F) :-
        eats(anil, F).

    % 7. Anil is alive
    alive(anil).

    % 8. Harry eats whatever Anil eats
    eats(harry, F) :-
        eats(anil, F).

    % 9. Display all foods
    showfoods :-
        fooditem(F),
        write(F), nl,
        fail.

    showfoods.


GOAL
    write("a) John likes peanuts: "),
    likes(john, peanuts),
    write("YES"), nl,

    write("b) Food items:"), nl,
    showfoods,

    write("c) Harry eats barley: "),
    eats(harry, barley),
    write("YES"), nl.