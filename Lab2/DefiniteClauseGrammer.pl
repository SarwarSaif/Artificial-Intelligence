s --> np, vp.
np --> person.
vp --> tpv,( p;t;person  ).
vp --> tpv,( p;t;person  ),adv.
vp --> av,pre,p.
vp--> av,cv,( p;t;person  ).
vp--> av,cv,( p;t;person  ),adv.
vp -->fv,rv,( p;t;person  ).
vp -->fv,rv,( p;t;person  ),adv.
vp --> av,adj.
person --> [thanos];['captain america'];['peter parker']
    ;['tony stark'];[nebula];[drax];[thor].
p --> [titan];[brooklyn];[queens];[manhattan]
    ;[xander];[asgard].
t --> ['infinity gaunlet'];[shield];['his fingers']
    ;[webs].
adj --> [young];[obsessive];[narcissist];[vengeful]
    ;[worthy];[red];[blue].
adv --> [vigorously];[anxiously].
fv --> [will].
rv --> [destroy];[snap];[wield];[weave];[fight].
tpv --> [destroys];[snaps];[wields];[weaves];[fights].
av --> [is].
cv --> [destroying];[snapping];[wielding];[weaving];[fighting].
pre --> [form];[in].
%Wrapper predicate
isValidSentence(X):- s(X,[]).