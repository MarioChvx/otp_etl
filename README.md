# OTP-analysis

This is a personal project with multiple steps:

1. **First** extract historical information about the matches of some players using `Riot's API` and `RiotWatcher` library, then store it temporally as a `DataFrame` then save the sorted information in a `PostgreSQL` database. This information start form June 16 2021 and will end to the current day and will be updated daily.
2. **Second** the historical data will be analyzed and interpreted. Searching insights.
3. **Third** the data and insights will be used to model and train an IA that predicts witch team will win just with the information you can get by the time loading screen is showed.

## Consulting Riot's API

### RiotWathcer

For the **1. First step** 'spectator'
**Returns** current game info
'champion_mastery'
**Returns** champion masteri info