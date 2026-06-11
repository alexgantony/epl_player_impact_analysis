To-Do:

1. List every column available after merging.
2. Group them into:
    - Attack Output
    - Creativity
    - Ball Progression
    - Defense Impact
    - Possession
    - Team Impact
    - Availability
    - Consistency
3. Create a Feature List table.
4. Mark each feature as:
    - Existing
    - Per90
    - Percentage Share
    - Derived Metric
5. Only then start coding.

**What makes a Player of season?**
Attack Output, Creativity, Ball Progression, Defence Impact - Outfield Players, Defence Impact - Goalkeeper, Possession, Team Impact, Availability, Consistency, Discipline

**Which columns belong to each dimension?**

|  Category | Metrics|
|--- |--- |
|  Attack Output | bigChancesMissed, totalShots, goalConversionPercentage, goals, expectedGoals, nonPenaltyGoals, touchesInOppBox  	|
| Creativity  	|  bigChancesCreated, keyPasses, assists, expectedAssists, chancesCreated 	|
|   Ball Progression	|   finalThirdPassesSuccessful, accurateFinalThirdPassPerc, progressiveCarries	|
|   Defense Impact - Outfield Players	|  interceptions, clearances, errorLeadToGoal, tackles, outfielderBlocks, penaltyConceded, possessionWon, tacklesWon, shotsBlocked, ballRecoveries, groundDuelsWon, aerialDuelsWon	|
| Defence Impact - Goalkeeper | saves, cleanSheet, penaltySave, savedShotsFromInsideTheBox,  runsOut, goalsConceded, savesMade, savePerc, goalsPrevented, savesMadeOutsideBox, savesMadeInsideBox   |
|   Possession	|  accuratePasses, successfulDribbles, accuratePassesPercentage, touches 	|
|   Team Impact	|  potm_wins, teamPosition,  teamPoints, teamGoalsScored, teamGoalsConceded, teamGoalDiffPer90, teamOnOffImpactPer90	|
|   Availability	| matchesPlayed, matchesStarted,  minutesPlayed, squadMinutesShare  	|
|   Consistency	|  sofascoreRating 	|
| Discipline | yellows, reds, fouls | 



|Feature Name 	|  Category 	|   Source Columns	|   Formula / Logic	|   Type	|  Why It Matters 	|  Candidate for Final Score? 	|   
|---	|---	|---	|---	|---	|---	|---	|
|  goalsPer90 	|   	|   	|   	|   	|   	|   	|   
|  assistsPer90 	|   	|   	|   	|   	|   	|   	|   
|   goalInvolment	|   	|   	|   	|   	|   	|   	|   
|  goalInvolmentPer90 	|   	|   	|   	|   	|   	|   	|   
|   teamGoalContributionPct	|   	|   goals+assists, teamGoalsScored	|   	|   	|   	|   	|   
|   	|   	|   	|   	|   	|   	|   	|   
|   	|   	|   	|   	|   	|   	|   	|   
|   	|   	|   	|   	|   	|   	|   	|   
|   	|   	|   	|   	|   	|   	|   	|   