--create database DSC540MidTermProject

USE DSC540MidTermProject
GO

create table Titles
(
	Num Varchar(Max)
	, Title Varchar(Max)
	, URL Varchar(Max)
)

bulk insert Titles
from 'E:\BulkInsert\dfTitleDataset.csv'
with
(
rowterminator='\n',
fieldterminator=',',
firstrow=2
)

create table Genre
(
	Num Varchar(Max)
	, Genre Varchar(Max)
	, URL Varchar(Max)
)

bulk insert Genre
from 'E:\BulkInsert\dfGenreDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table MPAARating
(
	Num Varchar(Max)
	, MPAARating Varchar(Max)
	, URL Varchar(Max)
)

bulk insert MPAARating
from 'E:\BulkInsert\dfMPAARatingDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table ProductionBudget
(
	Num Varchar(Max)
	, ProductionBudget Varchar(Max)
	, URL Varchar(Max)
)

bulk insert ProductionBudget
from 'E:\BulkInsert\dfProductionBudgetDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table ReleaseDate
(
	Num Varchar(Max)
	, ReleaseDate Varchar(Max)
	, URL Varchar(Max)
)

bulk insert ReleaseDate
from 'E:\BulkInsert\dfReleaseDateDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table Distributor
(
	Num Varchar(Max)
	, Distributor Varchar(Max)
	, URL Varchar(Max)
)

bulk insert Distributor
from 'E:\BulkInsert\dfDistributorDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table Domestic
(
	Num Varchar(Max)
	, Domestic Varchar(Max)
	, URL Varchar(Max)
)

bulk insert Domestic
from 'E:\BulkInsert\dfDomesticDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table ForeignGrosses
(
	Num Varchar(Max)
	, ForeignGrosses Varchar(Max)
	, URL Varchar(Max)
)

bulk insert ForeignGrosses
from 'E:\BulkInsert\dfForeignDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table OpeningWeekendGross
(
	Num Varchar(Max)
	, OpeningWeekendGross Varchar(Max)
	, URL Varchar(Max)
)

bulk insert OpeningWeekendGross
from 'E:\BulkInsert\dfOpeningWeekendGrossDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table OpeningWeekendTheaters
(
	Num Varchar(Max)
	, OpeningWeekendTheaters Varchar(Max)
	, URL Varchar(Max)
)

bulk insert OpeningWeekendTheaters
from 'E:\BulkInsert\dfOpeningWeekendTheatersDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table Runtime
(
	Num Varchar(Max)
	, Runtime Varchar(Max)
	, URL Varchar(Max)
)

bulk insert Runtime
from 'E:\BulkInsert\dfRuntimeDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)

create table Worldwide
(
	Num Varchar(Max)
	, Worldwide Varchar(Max)
	, URL Varchar(Max)
)

bulk insert Worldwide
from 'E:\BulkInsert\dfWorldwideDataset.csv'
with
(
rowterminator='0x0a',
fieldterminator=',',
firstrow=2
)