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
6. This code can not simulate exactly as the real life game , because it depends on the order in which user adds the cards won to the bottom of deck.It is not mentioned by game rules

## Corner Cases
1. During WAR, each player has to place three cards off the top of their deck face down on the table. And fourth card is used to play the round.
2. If WAR happens during WAR, need to repeat the process until there is a decisive victory
3. If a player runs out of cards or does not have mininum number of cards to play in WAR. The player's last card is used to play the round.
4. If the game is running for more than 1000 times, i am exiting the game to prevent from infinite loop

## If Given More time
1. I have used List for peforming pop() and append() operation. This might cause an issue when the number of players grow and game should run on large scale. 
With more time, I could like to implement using Queue data structure imported from Queue library.
2. I have defined Player Class but I have not used it. If even more time , I would create each player using the Player class.
3. Genelarizing the game for N players . Currently , only two players can play the game. I would like to extend the current functionality for N players. I have thought about the implementation.I would love to try this 
4. My current code doesnt have any interaction with the user, becuase the game was running for many rounds . So, I did not implement interaction. But I would like to add that feature to this using cool animation.

