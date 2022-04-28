# Adventure Game: Treasure Island

# Game where the player makes choices through out the story and depending on their choices they will advance to the next stage or win a game over.


print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
player_choice1 = input("left or right?").lower()


gg = str("Game Over")

if player_choice1 == str("right"):
    print(gg)
else:
    print("moving forward")

player_choice2 = input("swim or wait?").lower()

if player_choice2 == str("swim"):
    print(gg)
elif player_choice2 == str("wait"):
    print("Moving forward")

print("Which door do you open?")
player_choice3 = input("Red, blue, or yellow?").lower()
if player_choice3 == str("red"):
    print(gg)
elif player_choice3 == str("blue"):
    print(gg)
elif player_choice3 == str("yellow"):
    print("You Win!")

#     ..gaspp!!!... you perv!
#             .d$$S$$S$$Sb.
#            dS$$S$$S$PS$$Sb
#           :$$S$S^^'";TSS$$; ;
#           SSP'      : T$$SS/;
#           $$         \ `^^'/
#           :$          `-ggd:
#            :.=-.    .-=.:SSS
#            ; <@>`   <@> $$$$
#            :            SS$$
#            '     -.     $$S;
#             '   .--.   s$$S
#        _     `. `--' .$$S$;
#    .-"" "-._.-'`.__.' $$$S;
#   :                   :S$$S
#   ;    :l   "-.       '^S$$b
#  /`-.  ;:      "   .--""""""^-.
# :"-. "" :                   /) ;
# ;`-     :                  /:  :
# :`-      `.     \         / '-.t
#  `+.__     `.    ;/    .-'    -.;
#   ;   "-.    "-. :  .-"       --:
#   ;      ;.     "^:"    .-""-.`.;
#   :     -^"`.      "-.+'      \/
#    ;         `.        "-     ;
#    :          .^.            /
#     \      .-"   "-.       .'
#      `._.-"         "-._.-":
#       ;          :         ;
#       :          :        :
#        ; \       ;        ;
#        :  ;      ;       :
#         ; :      :     / ;
#     bug :  \             ;
#         ;                :
#        :                  ;
#        ;    :             :
#       :     ;              ;
#       ;     ;    c         :
#      :      :          :    ;
#     /""--..__          ;    :
#    :         ""--..__        ;
#    ;   "-.    --..__ ""--..__:
#   :`-._   "-._      ""       _;
#   ;    "-._   """---...---""" :
# anime style death by nose bleed lol
