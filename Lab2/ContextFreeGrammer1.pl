%List Predicates
member(X,[X|_]).
member(X,[_|T]):-member(X,T).
append([],L,L).
append(A,B,C):- [H|T] = A, [H|T1]= C, append(T,B,T1).
%Grammar rules
isDeterminant(X):- member(X,[a,the]).
isPerson(X):- member(X,["Thanos", "Captain America", 
                     "Peter Parker", "Tony Stark", 
                     nebula, drax, thor]).
isPlace(X):- member(X,[titan, brooklyn, queens,
                    manhattan, xander, asgard]).
isThing(X):-member(X,["Infinity Gauntlet", shield,
                   "his fingers", webs]).
isAdj(X):- member(X,[young, obsessive, narcissist, 
                    vengeful, worthy, red, blue]).
isAdv(X):- member(X,[vigorously, anxiously]).
isFutureVerb(X):- member(X,[will]).
isRootVerb(X):- member(X,[destroy, snap, 
                         wield, weave, fight]).
is3rdPersonVerb(X):- member(X,[destroys, snaps,
                                wields, weaves, fights]).
isAuxiliaryVerb(X):- member(X,[is]).
isContinuousVerb(X):-member(X,[destroying, snapping, 
                              wielding, weaving, fighting]).
isPre(X):- member(X,[from,in]).
isNounPhrase([H]):- isPerson(H).
isVerbPhrase([H,T]):- is3rdPersonVerb(H),(   
                         isPerson(T);isPlace(T);isThing(T)
                                         ).
isVerbPhrase([H,T,S]):- is3rdPersonVerb(H),(   
                         isPerson(T);isPlace(T);isThing(T)
                                         ),isAdv(S).
isVerbPhrase([H,T,S]):- isAuxiliaryVerb(H),isContinuousVerb(T),(   
                         isPerson(S);isPlace(S);isThing(S)
                                         ).
isVerbPhrase([H,T,S,R]):- isAuxiliaryVerb(H),isContinuousVerb(T),(   
                         isPerson(S);isPlace(S);isThing(S)
                                         ),isAdv(R).
isVerbPhrase([H,T,S]):- isFutureVerb(H),isRootVerb(T),(   
                         isPerson(S);isPlace(S);isThing(S)
                                         ).
isVerbPhrase([H,T,S,R]):- isFutureVerb(H),isRootVerb(T),(   
                         isPerson(S);isPlace(S);isThing(S)
                                         ),isAdv(R).
isVerbPhrase([H,T,S]):- isAuxiliaryVerb(H),isPre(T),   
                         isPlace(S).
isVerbPhrase([H,T]):- isAuxiliaryVerb(H),isAdj(T).
isValidSentence(L):- isNounPhrase(A),isVerbPhrase(B),append(A,B,L).







