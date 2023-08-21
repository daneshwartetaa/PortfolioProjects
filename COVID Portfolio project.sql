SELECT *
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
ORDER BY 3,4

--SELECT *
--FROM PortfolioProject..CovidVaccinations
--ORDER BY 3,4

SELECT location, date, total_cases, new_cases, total_deaths, population
FROM PortfolioProject..CovidDeaths
ORDER BY 1,2

--Total case vs Total death
--Shows likelihood of dying 

SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS DeathPercentage
FROM PortfolioProject..CovidDeaths
WHERE location like '%states%'
ORDER BY 1,2

--Total case vs Population
--What percentage of population got covid

SELECT location, date, population, total_cases, (total_cases/population)*100 AS DeathPercentage
FROM PortfolioProject..CovidDeaths
--WHERE location like '%states%'
ORDER BY 1,2


--Countries with highest infection rate vs population

SELECT location, population, MAX(total_cases) AS HighestInfectionCount, MAX(total_cases/population)*100 AS InfectedPercentage
FROM PortfolioProject..CovidDeaths
GROUP BY location, population
ORDER BY InfectedPercentage DESC

--Highest death count per population

SELECT location, MAX(cast(total_deaths as int)) AS HighestDeathCount
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY HighestDeathCount DESC



--Breaking down by Continent


SELECT continent, MAX(cast(total_deaths as int)) AS HighestDeathCount
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY HighestDeathCount DESC


--Continents with Highest Death Count per Population

  --Global Numbers

SELECT SUM(new_cases), SUM(CAST(new_deaths as int)), SUM(CAST(new_deaths AS int))/SUM(new_cases)*100 AS DeathPercentage
FROM PortfolioProject..CovidDeaths
--WHERE location like '%states%'
WHERE continent is not null
--GROUP BY date
ORDER BY 1,2

--Total Population vs vaccination

SELECT Dt.continent, Dt.location, Dt.date, Dt.population, Vt.new_vaccinations
, SUM(CONVERT(INT,Vt.new_vaccinations)) OVER (PARTITION BY Dt.location ORDER BY Dt.date, Dt.location) AS RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths Dt
JOIN PortfolioProject..CovidVaccination Vt
ON Dt.location = Vt.location
and Dt.date = Vt.date
WHERE Dt.continent IS NOT NULL
ORDER BY 2,3

--USING CTEs

WITH PopVsVac (continent, location, date, population, New_vaccinations, RollingPeopleVaccinated)
AS
(
SELECT Dt.continent, Dt.location, Dt.date, Dt.population, Vt.new_vaccinations
, SUM(CONVERT(INT,Vt.new_vaccinations)) OVER (PARTITION BY Dt.location ORDER BY Dt.location, Dt.date) AS RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths Dt
JOIN PortfolioProject..CovidVaccination Vt
ON Dt.location = Vt.location
and Dt.date = Vt.date
WHERE Dt.continent IS NOT NULL
--ORDER BY 2,3
)
SELECT *,(RollingPeopleVaccinated/population)*100
FROM PopVsVac

--Temp table

DROP TABLE IF EXISTS #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(continent nvarchar(255),
location nvarchar(255),
date Datetime,
population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

INSERT INTO #PercentPopulationVaccinated
SELECT Dt.continent, Dt.location, Dt.date, Dt.population, Vt.new_vaccinations
, SUM(CONVERT(INT,Vt.new_vaccinations)) OVER (PARTITION BY Dt.location ORDER BY Dt.location, Dt.date) AS RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths Dt
JOIN PortfolioProject..CovidVaccination Vt
ON Dt.location = Vt.location
and Dt.date = Vt.date
WHERE Dt.continent IS NOT NULL
--ORDER BY 2,3

SELECT *, (RollingPeopleVaccinated/population)*100
FROM #PercentPopulationVaccinated

--Creating View to store data for later visualizations

CREATE view PercentPopulationVaccinated AS
SELECT Dt.continent, Dt.location, Dt.date, Dt.population, Vt.new_vaccinations
, SUM(CONVERT(INT,Vt.new_vaccinations)) OVER (PARTITION BY Dt.location ORDER BY Dt.location, Dt.date) AS RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths Dt
JOIN PortfolioProject..CovidVaccination Vt
ON Dt.location = Vt.location
and Dt.date = Vt.date
WHERE Dt.continent IS NOT NULL
--ORDER BY 2,3