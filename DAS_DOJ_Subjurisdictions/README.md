# Differential Privacy Analysis: DOJ Subjurisdictions
***
The Electoral Innovation Lab at Princeton analyzed the epsilon = 12.2 Census DAS demonstration dataset in 62 local jurisdictions critical to VRA cases across the country. These were in Arizona, California, Florida, South Dakota, and Texas. This analysis is summarized in this [memo](https://docs.google.com/document/d/1c3GubCNHRPeJgrtF0z_TiC3eaMxC4WakZarx_PzoL3Q/edit)
***

## DOJ Jurisdictions
### Code
* DAS_jurisdictions.py: python code for processing files in /Data/Joined DP 2010 Block Data.zip into files in /Data/Subjurisdictions folder.
* Census Relative Distance for MVAP_DOJ_memo.py: python script to aggregate files from /Data/Subjurisdictions folder into tables and figures in /Figures and /Output folders.

### Data
* Joined DP 2010 Block Data.zip: census block tables for each state with subjurisdiction data.
* Subjurisdictions.zip: individual CSV files for each jurisdiction at both the district and block level.

### Figures
* TotPop_difference: relative distance, or difference from 2010 census, figure for the total population of each subjurisdiction.
* TotPop_difference_zoomed: the above figure zoomed in on only subjurisdictions with less than 20,000 people.
* BVAP_difference: relative distance, or difference from 2010 census, figure for the black voting age population of each subjurisdiction.
* BVAP_difference_zoomed: the above figure zoomed in on only subjurisdictions with less than 20,000 people.
* HVAP_difference: relative distance, or difference from 2010 census, figure for the hispanic voting age population of each subjurisdiction.
* HVAP_difference_zoomed: the above figure zoomed in on only subjurisdictions with less than 20,000 people.
* AVAP_difference: relative distance, or difference from 2010 census, figure for the asian voting age population of each subjurisdiction.
* AmInVAP_difference:relative distance, or difference from 2010 census, figure for the american indian voting age population of each subjurisdiction.


### Output
* DOJ_jurisdictions_extended_table.csv: jurisdiction by jurisdiction table detailing:
  - jurisdiction: jurisdiction name
  - state: state abreviation
  - district type: subjurisdiction type
  - num of districts: total number of subjurisdictions
  - num of blocks: number of blocks in jurisdiction
  - mean blocks per dist: average number of blocks per district
  - max blocks per dist: largest number of blocks in any district
  - num of pop blocks: number of blocks with non-zero population
  - pct blocks populated: percent of blocks woth non-zero population
  - mean pop blocks per dist: average population of blocks in jurisdiction
  - max pop blocks per dist: maximum number of blocks in any district
  - max abs difference: maximum of the absolute value of difference between the 2010 census and DAS demonstration product
  - mean abs difference: average absolute value of this difference
  -m ean Difference: average difference without taking absolute value
  - abs standard deviation: standard deviation of absolute value of district differences
  - standard deviation: standard deviation of district differences
  - total map pop 2010: total population of jurisdiction in 2010 census
  - mean pop per dist 2010: average population of districts in 2010 census
  - max pop per dist 2010: largest district population in 2010 census
  - stdev pop per dist 2010: standard deviation of district population from 2010 census

* DOJ_jurisdictions_memo_table.csv: similar table as above, but with only the fields used in our memo. Specifically: jurisdiction, state, district type, num of districts, mean blocks per dist, max abs difference, mean abs difference, abs standard deviation, and mean pop per dist 2010.
* HVAP_devs.csv: district by district table with specifics about each district in all jurisdictions that had a difference in HVAP of more than 1%
  - map: jurisdiction name
  - local_id: district number
  - state: state abreviation
  - dist_type: type of subjurisdiction
  - tot: total population from 2010 census
  - totDP: total population from DAS demonstration product
  - totVAP: total voting age population from 2010 census
  - totVAPDP: total voting age population from DAS demonstration product
  - HVAP: hispanic voting age population from 2010 census
  - HVAPDP: hispanic voting age population from DAS demonstration product
  - NHbla_alo_VAP: non-hispanic black voting age population from 2010 census
  - NHBVAP_aloDP:non-hispanic black voting age population from DAS demonstration product
  - pNHWVAP:% Nonhispanic White VAP (out of total VAP)
  - pHVAP: Hispanic VAP (out of total VAP)
  - pNHBVAP:% Nonhispanic Black VAP (out of total VAP)
  - rHVAP: relative distance for hispanic VAP -> ( (HVAP (DP) - HVAP (2010)) / total VAP (2010) ) * 100
  - rNHBVAP: relative distance for nonhispanic Black VAP -> ( (NHBVAP (DP) - NHBVAP (2010)) / total VAP (2010) ) * 100

* NHBVAP_devs.csv: district by district table with specifics about each district that had more than 1% difference in BVAP. It has the same fields as the file above.
