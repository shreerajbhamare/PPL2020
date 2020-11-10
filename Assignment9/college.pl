teaches_subject(tm1,math,div1,comp_dept).
teaches_subject(tm2,math,div2,comp_dept).
teaches_subject(tm3,math,div1,mech_dept).
teaches_subject(tm4,math,div2,mech_dept).
teaches_subject(tm5,math,entc_dept).

teaches_subject(t3,dsa,div1).
teaches_subject(t4,dsa,div2).
teaches_subject(t5,ppl,div1).
teaches_subject(t6,dld,div1).
teaches_subject(t7,dtl,div1).
teaches_subject(t8,ppl,div2).
teaches_subject(t9,dld,div2).
teaches_subject(t10,dtl,div2).

teaches_subject(t11,som,div1).
teaches_subject(t12,som,div2).
teaches_subject(t13,tom,div1).
teaches_subject(t14,dom,div1).
teaches_subject(t15,em,div1).
teaches_subject(t16,tom,div2).
teaches_subject(t17,dom,div2).
teaches_subject(t18,em,div2).


has_subject(math_dept,math).

has_subject(comp_dept,dsa).
has_subject(comp_dept,ppl).
has_subject(comp_dept,dtl).

has_subject(mech_dept,som).
has_subject(mech_dept,tom).
has_subject(mech_dept,dom).
has_subject(mech_dept,em).

has_subject(entc_dept,sa).
has_subject(entc_dept,edc).
has_subject(entc_dept,nsaf).

has_student(comp_dept,s1).
has_student(comp_dept,s2).
has_student(comp_dept,s3).
has_student(comp_dept,s4).
has_student(comp_dept,s5).

has_student(mech_dept,s6).
has_student(mech_dept,s7).
has_student(mech_dept,s8).
has_student(mech_dept,s9).
has_student(mech_dept,s10).

has_student(entc_dept,s11).
has_student(entc_dept,s12).
has_student(entc_dept,s13).
has_student(entc_dept,s14).
has_student(entc_dept,s15).

is_in_div(s1,div1).
is_in_div(s2,div1).
is_in_div(s3,div2).
is_in_div(s4,div1).
is_in_div(s5,div2).

is_in_div(s6,div1).
is_in_div(s7,div2).
is_in_div(s8,div2).
is_in_div(s9,div1).
is_in_div(s10,div2).

has_faculty(D,F) :- teaches_subject(F,S) , has_subject(D,S).
studies_subject(ST,SB) :- has_student(D,ST) , has_subject(D,SB).
studies_subject(ST,SB) :- has_student(D,ST),has_subject(D,SB).
studies_under(S,F) :- studies_subject(S,SB) , teaches_subject(F,SB,DEPT) , has_student(DEPT,S).
studies_under(S,F) :- studies_subject(S,SB) , is_in_div(S,DIV) , teaches_subject(F,SB,DIV,DEPT), has_student(DEPT,S).