<h1 style='color:purple' align='center'>Data Science Regression Project: Predicting Golfer's Scoring Average</h1>

<p> This model is designed to predict a golfer's scoring average based on 4 inputs <p> 
 
 <h3 style='color:purple' align='left'>Background Part 1</h3>

<p> The PGA tour (which is the highest level of professional golf similar to the NFL or MLB) has an 8 month season.
 
 Throughout the 8 month season, players work to accumulate Fedex Cup points by winning or finishing well at different tournaments.
 
 The season ends with a final tournament, called the Tour Championship. 
 
 The Tour Championship works different that most golf tournaments.
 
 In most golf tournaments, all players start at the same score (Even Par or E)

However, the Tour Championship features a strokes-based system that was started in 2019.

Under this system, the player with the most Fedex Cup points prior to the Tour Champtionship starts at -10 (Ten Under Par), while second place starts at -8, third place starts at -7, all the way down to players 26-30 starting at E. 

Meaning that if you have more Fedex Cup points prior to starting the tournament, you have a big advantage over the rest of the field.

And if you win the Tour Championship, you get a hefty amount of money ($25 Million as of 2024).

Therefore, it's not just important to win on the PGA tour, but it's also important to do well throughout the season so that you can get a lot of Fedex Cup points and give yourself the best chance of winning. 

One of the best measures of how consistently well a player is playing is their Scoring Average (i.e. the average score they shoot).

<h3 style='color:purple' align='left'>Background Part 2</h3>

The PGA tour does a great job keeping detailed statistics. \n",
    "\n",
    "One of the measures they used is called \"Strokes Gained,\" which breaks down into multiple categories:\n",
    "\n",
    "- Strokes Gained Off the Tee (aka the first shot you hit)\n",
    "- Strokes Gained Approach (aka after you hit your first shot, the shot(s) you hit onto the green)\n",
    "- Strokes Gained Around the Green (when you miss the green, how well do you do)\n",
    "- Strokes Gained Putting (how well do you putt)\n",
    "\n",
    "How Strokes Gained works is that for each shot a player hits, they will compare that shot to if the average PGA tour player hit that shot. \n",
    "\n",
    "Meaning that if the player did better than the PGA tour average, they will \"gain strokes.\"\n",
    "\n",
    "And if they did worse than the PGA tour aver, they will \"lose strokes.\"\n",
    "\n",
    "The easiest example to explain this is a simple 3 foot putt.  \n",
    "\n",
    "On average, PGA tour players make 96% of 3 foot putts (according to research by Columbia University professor Mark Broadie). \n",
    "\n",
    "Meaning that if a player makes a 3 foot putt, they gain 0.04 strokes on the field. \n",
    "\n",
    "And if they miss a 3 foot putt, they lose .96 strokes. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hope that makes sense. Now on to coding!!"
   ]
  },

