% facts

at(monkey, room).
at(banana, ceiling).
at(box, room).
on(monkey, floor).
has(monkey, nothing).

% rules

can_reach_banana :-
    at(monkey, room),
    at(box, room),
    push(box, banana_position),
    climb(box),
    grab(banana).

push(box, banana_position) :-
    write('Monkey pushes the box under the banana.'), nl.

climb(box) :-
    write('Monkey climbs onto the box.'), nl.

grab(banana) :-
    write('Monkey grabs the banana!'), nl.
