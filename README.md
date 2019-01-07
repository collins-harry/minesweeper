# Minesweeper
Minesweeper game and AI player. Game built using model, view, controller perspective. 

## Game

### Model
- [X] Initialise mine board
- [X] Initialise viewer board
- [ ] Flag Toggle function
- [ ] Clear single tile function
  - [ ] Mine checker (single tile)

### Viewer 
- [X] Text view for mines on board
- [X] Text view for player visible board 
- [ ] GUI viewer for board

### Controller
- [ ] Text based control for AI player
- [ ] GUI based control for human player (possible same as GUI viewer)

## AI Player
Will initially make several random clearances, later on I will refine guesses to maximise information return (ie. corners might be a bad idea but the might have a higher probability of a 'cascade')

The player will then iteratively alternate between basic logic clearing and flagging.
There is a second more advanced logic technique for select circumstances when simple adjacent logic technique fails. 

When player is stuck it will resort to analytical probabilistic techniques.

I may attempt machine learning techniques later.

### Initialisation
- [ ] Random guessing
- [ ] Refined guessing

### Logic methods
- [ ] Simple clearing function (board level)
- [ ] Flagging function (board level)
- [ ] Add second additional logic technique

### Probabilistic method
- [ ] Guessing probabilistic function
- [ ] Refined probabilistic function


