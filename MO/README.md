# Missouri cleaning and gerrychain

__Sources__

On March 19th, downloaded VEST's precinct shapefile with election data matched from here: 
https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/NH5S2I/ZL99CI

On March 22nd, downloaded Missouri state legislative district lines from here: 
https://catalog.data.gov/dataset/tiger-line-shapefile-2016-state-missouri-current-state-legislative-district-sld-upper-chamber-s

On March 22nd, downloaded Missouri U.S. congressional district lines from here: 
https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.2016.html

On March 23rd, downloaded census block-level population from here:
https://www2.census.gov/geo/tiger/TIGER2010BLKPOPHU/ 

__Metadata__

* `loc_prec`: Unique precinct identifier, "county name,precinct name" 
* `HOUSING10`: 2010 Census Housing Unit Count
* `POP10`:  2010 Census Population Count
* `COUNTYFP`: County Name
* `NAME`: Precinct Name
* `CD115FP`: U.S. Congressional District (2016)
* `SLDUST`: Missouri State Legislative District - Upper Chamber
* `G16PREDCLI`: General 2016 President Democratic Party Candidate
* `G16PRERTRU`: General 2016 President Republican Party Candidate
* `G16PRELJOH`: General 2016 President Libertarian Party Candidate
* `G16PREGSTE`:  General 2016 President Green Party Candidate`: 
* `G16PRECCAS`: General 2016 President Constitutional Party Candidate
* `G16USSDKAN`: General 2016 U.S. Senate Democratic Party Candidate
* `G16USSRBLU`: General 2016 U.S. Senate Rebublican Party Candidate
* `G16USSLDIN`: General 2016 U.S. Senate Libertarian Party Candidate
* `G16USSGMCF`: General 2016 U.S. Senate Green Party Candidate
* `G16USSCRYM`: General 2016 U.S. Senate Constitution Party Candidate
* `G16GOVDKOS`: General 2016 Governor Democratic Party Candidate
* `G16GOVRGRE`: General 2016 Governor Rebublican Party Candidate
* `G16GOVLSPR`: General 2016 Governor Libertarian Party Candidate
* `G16GOVGFIT`: General 2016 Governor Green Party Candidate
* `G16GOVITUR`: General 2016 Governor Independent Party Candidate
* `G16LTGDCAR`: General 2016 Lt. Governor Democratic Party Candidate
* `G16LTGRPAR`: General 2016 Lt. Governor Rebublican Party Candidate
* `G16LTGLHED`: General 2016 Lt. Governor Libertarian Party Candidate
* `G16LTGGLEA`: General 2016 Lt. Governor Green Party Candidate
* `G16ATGDHEN`: General 2016 Attorney General Democratic Party Candidate
* `G16ATGRHAW`: General 2016 Attorney General Rebublican Party Candidate
* `G16TREDBAK`: General 2016 Treasurer Democratic Party Candidate
* `G16TRERSCH`: General 2016 Treasurer Rebublican Party Candidate
* `G16TRELOTO`: General 2016 Treasurer Libertarian Party Candidate
* `G16TREGHEX`: General 2016 Treasurer Green Party Candidate
* `G16SOSDSMI`: General 2016 Sect. of State Democratic Party Candidate
* `G16SOSRASH`: General 2016 Sect. of State Rebublican Party Candidate
* `G16SOSLMOR`: General 2016 Sect. of State Libertarian Party Candidate
* `geometry`: 

__Pre-processing__

To avoid topology errors, we used the census block-level file and added precinct labels to every census block. Then, we dissolved census blocks by precinct labels. We joined this file with the precinct votes file from VEST. The `POP10` and `HOUSING10` variables are the result of this census-block aggregation. 

__Documentation__

From VEST's documentation for the precinct-level shapefile with election results: 

Missouri
--------
Election results from the Secretary of State's office via OpenElections (https://github.com/openelections/openelections-sources-mo/tree/master/2016). Results for Attorney General from Butler County and for Lt. Governor from Linn County were corrected with the Statement of Votes Cast from the respective counties.

Precinct shapefiles primarily from the U.S. Census Bureau's 2020 Redistricting Data Program Phase 2 release, with the following exceptions and alterations.

The following were based on maps received from the county governments: Audrain, Benton, Bollinger, Buchanan, Butler, Caldwell, Callaway, Cape Girardeau, Cedar, Christian, Cooper, Jackson, Jefferson, Johnson, Laclede, Lafayette, Marion, McDonald, Miller, Morgan, Nodaway, Osage, Ray, Texas, Worth, Wright.

Monroe County comes from the 2010 Census VTD release.

Precinct mergers were made in the following counties to match county reporting units: Andrew, Audrain, Barry, Benton, Bollinger, Boone, Camden, Cape Girardeau, Carter, Cass, Christian, Clark, Cole, Cooper, Crawford, Dallas, Dekalb, Douglas, Dunklin, Franklin, Gentry, Greene, Grundy, Howard, Howell, Jackson, Jasper, Jefferson, Linn, Livingston, Marion, Mercer, Mississippi, Moniteau, Morgan, New Madrid, Oregon, Osage, Pemiscot, Pettis, Phelps, Platte, Polk, Putnam, Ralls, Randolph, Ripley, St. Clair, St. Louis, Schuyler, Shannon, Shelby, Stone, Sullivan, Warren, Wayne, Webster, Worth.

Additional modifications to reflect how election results were reported:

Audrain: Added Vandalia City
Barry: Added Monett City
Cooper: Merged city/rural Boonville wards
Dallas: Split Benton Outside City Limits from Benton North
Dent: Split Boss precinct from R-4 precinct
Franklin: Dry Branch split between Stanton & St. Clair Out of Town
Howard: Split Old Franklin & New Franklin
Jasper: Added Webb City wards from county GIS
Jefferson: Split Festus 4 precinct into P1 & P2
Linn: Split N/S Benton & Brookfield 1&2/3&4
Marion: The 2 polling places that report separately for Fabius Township do not have a defined boundary; voters are given the choice to register for either polling place
New Madrid: Added New Madrid City wards; Big Prairie 4 precinct
Pemiscot: Added Caruthersville City wards
Pike: Calumet GH split between Calumet F/Prairieville I
Polk: Split Campbell/Jefferson precincts by school district
Putnam: Split Union Twp into NE/SW precincts
Ralls: Center/Liberty precinct lines from the 2010 VTDs
Randolph: Added Moberly City wards; Huntsville City
Saline: Split Nelson precinct from Hardeman precinct
St. Louis: Added UNV044 precinct; Revised QUE047 precinct
Warren: Added Lakeview Estates precinct

Some votes were reported countywide in nearly every county; these were distributed by candidate to precincts based on their share of the precinct-level reported vote.

G16PREDCLI - Hillary Clinton (Democratic Party)
G16PRERTRU - Donald Trump (Republican Party)
G16PRELJOH - Gary Johnson (Libertarian Party)
G16PREGSTE - Jill Stein (Green Party)
G16PRECCAS - Darrell Castle (Constitution Party)

G16USSDKAN - Jason Kander (Democratic Party)
G16USSRBLU - Roy Blunt (Republican Party)
G16USSLDIN - Jonathan Dine (Libertarian Party)
G16USSGMCF - Johnathan McFarland (Green Party)
G16USSCRYM - Fred Ryman (Constitution Party)

G16GOVDKOS - Chris Koster (Democratic Party)
G16GOVRGRE - Eric Greitens (Republican Party)
G16GOVLSPR - Cisse Spragins (Libertarian Party)
G16GOVGFIT - Don Fitz (Green Party)
G16GOVITUR - Lester Turilli Jr. (Independent)

G16LTGDCAR - Russ Carnahan (Democratic Party)
G16LTGRPAR - Mike Parson (Republican Party)
G16LTGLHED - Steven Hedrick (Libertarian Party)
G16LTGGLEA - Jennifer Leach (Green Party)

G16ATGDHEN - Teresa Hensley (Democratic Party)
G16ATGRHAW - Josh Hawley (Republican Party)

G16TREDBAK - Judy Baker (Democratic Party)
G16TRERSCH - Eric Schmitt (Republican Party)
G16TRELOTO - Sean O'Toole (Libertarian Party)
G16TREGHEX - Carol Hexem (Green Party)

G16SOSDSMI - Robin Smith (Democratic Party)
G16SOSRASH - Jay Ashcroft (Republican Party)
G16SOSLMOR - Chris Morrill (Libertarian Party)