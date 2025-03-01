% Define the domain
#const max_row = 10.
#const max_col = 10.
row(1..max_row).
col(1..max_col).

% A cell can either be crossed out or not
{ crossedout(R, C) } :- cell(R, C, _).

% Ensure at least one cell is crossed out
:- not 1 { crossedout(R, C) }.

% Ensure no duplicate symbols remain in any row/column
:- cell(R, C1, S), cell(R, C2, S), C1 != C2, not crossedout(R, C1), not crossedout(R, C2).
:- cell(R1, C, S), cell(R2, C, S), R1 != R2, not crossedout(R1, C), not crossedout(R2, C).

% Ensure no adjacent crossed-out cells
:- crossedout(R, C), crossedout(R+1, C).
:- crossedout(R, C), crossedout(R, C+1).

% Define a valid starting point to ensure connectivity
start(R, C) :- cell(R, C, _), not crossedout(R, C).

% Ensure all non-crossed-out cells remain connected
reachable(R, C) :- start(R, C).
reachable(R, C) :- reachable(R-1, C), cell(R, C, _), not crossedout(R, C).
reachable(R, C) :- reachable(R+1, C), cell(R, C, _), not crossedout(R, C).
reachable(R, C) :- reachable(R, C-1), cell(R, C, _), not crossedout(R, C).
reachable(R, C) :- reachable(R, C+1), cell(R, C, _), not crossedout(R, C).

:- cell(R, C, _), not crossedout(R, C), not reachable(R, C).

% Define `crossedout/3` to include the symbol being crossed out
crossedout(R, C, S) :- cell(R, C, S), crossedout(R, C).

% Optimization: Minimize unnecessary cross-outs
#minimize { R+C : crossedout(R, C) }.

% Show only the `crossedout/3` predicate
#show crossedout/3.
