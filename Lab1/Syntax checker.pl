person(Thanos).
person("Captain America").
person("Peter Parker").
person("Tony Stark").
person(Nebula).
person(Drax).
person(Thor).
place(Titan).
place(Brooklyn).
place(Queens).
place(Manhattan).
place(Xander).
place(Asgard).
thing("Infinity Gaunlet").
thing(shield).
thing("his fingers").
thing(web).
adjective(young).
adjective(obsessive).
adjective(narcissist).
adjective(vengeful).
adjective(worthy).
adjective(red).
adjective(blue).
adverb(vigorously).
adverb(anxious).
verb(destroy).
verb(snap).
verb(wield).
verb(weave).
verb(fight).
verb3rd(destroys).
verb3rd(snaps).
verb3rd(wields).
verb3rd(weaves).
verb3rd(fights).
auxverbIs(is).
auxverbWill(will).
contverb(destroying).
contverb(snapping).
contverb(wielding).
contverb(weaving).
contverb(fighting).
preposition(from).
preposition(in).

isValidSentence(A,B,C,D,E):-(   (person(A),auxverbIs(B),contverb(C),
                                (place(D);thing(D);person(D)),adverb(E)
                                );
                            (   (person(A),auxverbWill(B),verb(C),
                                (place(D);thing(D);person(D)),adverb(E)
                            	)
                        	)
                            ).

isValidSentence(A,B,C,D):-	(   (   person(A),verb3rd(B),(place(C);thing(C);person(C)),
                          adverb(D)	);
    					(   (person(A),auxverbIs(B),contverb(C),
                                (place(D);thing(D);person(D))
                            )
                        );
    					(   (person(A),auxverbWill(B),verb(C),
                                (place(D);thing(D);person(D))
                            )
                        );
                            (   (person(A),auxverbIs(B),preposition(C),
                                (place(D))
                            )
                        )
                          	).
isValidSentence(A,B,C):-(   person(A),(   verb3rd(B);auxverbIs(B)),
                            (   (place(C);thing(C);person(C));adjective(C))).




    
    
    