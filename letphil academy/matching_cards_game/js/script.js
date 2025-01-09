/*
1. create and array for cards 
  cards = src, id, matched etc.. 

2. if card is clicked 
  every 2 actions = turn count ++ 
  card flips over 
    check if cards match other card
    if cards src is the same carsdd stay flipped
    if cards src is not the same cards flip back over

3. win condition 
    if all cards are matched end game 

4. new game button 
  if clicked 
    reshuffles cards 
    re render page 
*/ 

const cards = [
  src: '', 
  matched: 
  {}, 
] 

const shuffeledcards = [] 