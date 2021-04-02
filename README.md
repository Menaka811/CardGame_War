# CardGame_War
Python implementation of card game (War)

## Assumptions: 
1. CardGame_War.py considers only two players are playing the game
2. Deck of 52 cards is used for playing the game of 4 different suites
2. No one suite is treated as higher. All the 4 suites are treated equal
3. Player with higher rank faced up card wins the round
3. The cards won in the round are added to the bottom of deck of cards of the player that won the round
4. WAR is when both players turn over cards of same rank
5. Game continues till one player holds all the cards. That player is declared as winner.

## Corner Cases
1. During WAR, each player has to place three cards off the top of their deck face down on the table. And fourth card is used to play the round.
2. If WAR happens during WAR, need to repeat the process until there is a decisive victory
3. If a player runs out of cards or does not have mininum number of cards to play in WAR. The player's last card is used to play the round.

## If Given More time
