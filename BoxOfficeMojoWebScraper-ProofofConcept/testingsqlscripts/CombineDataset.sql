USE DSC540MidTerm
GO

update WidestRelease
set URL = WidestRelease, WidestRelease = URL  --Got these backwards in my python script


update Worldwide
set URL = Worldwide, Worldwide = URL  --Got these backwards in my python script too

select RIGHT(URL, Len(URL)-7) AS URL, ReleaseDate into ReleaseDateCleaned from ReleaseDate
select RIGHT(URL, Len(URL)-9) AS URL, Domestic + LEFT(URL, 7) AS Domestic into DomesticCleaned from Domestic
select RIGHT(URL, Len(URL)-9) AS URL, OpeningWeekendGross + LEFT(URL, 7) AS OpeningWeekendGross
into OpeningWeekendGrossCleaned 
from OpeningWeekendGross
where OpeningWeekendGross is not null
and URL is not null
and len(url) >= 10

update OpeningWeekendGrossCleaned
set URL = 'http' + URL
where URL like 's://%'

update OpeningWeekendGrossCleaned
set URL = 'https:/' + '/w' + URL
where URL like 'ww.%'

select RIGHT(URL, Len(URL)-9) AS URL, ForeignGrosses + LEFT(URL, 7) AS ForeignGrosses
into ForeignGrossesCleaned 
from ForeignGrosses
where ForeignGrosses is not null
and URL is not null
and len(url) >= 10

update ForeignGrossesCleaned
set URL = 'http' + URL
where URL like 's://%'

update ForeignGrossesCleaned
set URL = 'https:/' + '/w' + URL
where URL like 'ww.%'

select Title
, Distributor
, Genre
, MPAARating
, ProductionBudget
, ReleaseDate
, Domestic
, Genres
, WidestRelease
, Worldwide
, Runtime
, OpeningWeekendTheaters
, OpeningWeekendGross
, ForeignGrosses
, Distributor.URL
from Distributor
join Titles on Distributor.URL = Titles.URL
join Genre on Distributor.URL = Genre.URL
join MPAARating on Distributor.URL = MPAARating.URL
join ProductionBudget on Distributor.URL = ProductionBudget.URL
join ReleaseDateCleaned on Distributor.URL = ReleaseDateCleaned.URL
join DomesticCleaned on Distributor.URL = DomesticCleaned.URL
join ForeignGrossesCleaned on Distributor.URL = ForeignGrossesCleaned.URL
join OpeningWeekendGrossCleaned on Distributor.URL = OpeningWeekendGrossCleaned.URL
join OpeningWeekendTheaters on Distributor.URL = OpeningWeekendTheaters.URL
join Runtime on Distributor.URL = Runtime.URL
join Worldwide on Distributor.URL = Worldwide.URL
join Genres on Distributor.URL = Genres.URL
join WidestRelease on Distributor.URL = WidestRelease.URL
where Title not like '%PageMissing%'
Order BY Titles.Title


