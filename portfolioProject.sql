/*

cleaning data in sql queries

*/

 


-- Standardized Date format



SELECT SaleDateConverted, CONVERT(Date, SaleDate)
FROM PortfolioProject..NashvileHousing

ALTER TABLE NashvileHousing
ADD SaleDateConverted Date;

UPDATE NashvileHousing
SET SaleDateConverted = CONVERT(Date, SaleDate)

-- Populate property adress data

SELECT *
FROM PortfolioProject..NashvileHousing
-- WHERE PropertyAddress is null
ORDER BY ParcelID


SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM PortfolioProject..NashvileHousing a
JOIN PortfolioProject..NashvileHousing b
ON a.ParcelID = b.ParcelID
AND a.[UniqueID] <> b.[UniqueID]
WHERE a.PropertyAddress is null

UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM PortfolioProject..NashvileHousing a
JOIN PortfolioProject..NashvileHousing b
ON a.ParcelID = b.ParcelID
AND a.[UniqueID] <> b.[UniqueID]
WHERE a.PropertyAddress is null


-- Breaking out address into individual columns(address, city, state)


SELECT PropertyAddress
FROM PortfolioProject..NashvileHousing
--Where propertyAdress is null
--ORDER BY ParcelID


SELECT 
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 ) AS Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1 , LEN(PropertyAddress)) AS Address
FROM PortfolioProject..NashvileHousing




ALTER TABLE NashvileHousing
ADD PropertySplitAddress Nvarchar(255)

UPDATE NashvileHousing
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 )




ALTER TABLE NashvileHousing
ADD PropertySplitCity Nvarchar(255)

UPDATE NashvileHousing
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1 , LEN(PropertyAddress))


SELECT *
FROM PortfolioProject..NashvileHousing



SELECT OwnerAddress
FROM PortfolioProject..NashvileHousing


SELECT 
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
FROM PortfolioProject..NashvileHousing

ALTER TABLE NashvileHousing
ADD OwnerSplitAddress Nvarchar(255);


UPDATE NashvileHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)

ALTER TABLE NashvileHousing
ADD OwnerSplitCity Nvarchar(255);


UPDATE NashvileHousing
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)

ALTER TABLE NashvileHousing
ADD OwnerSplitState Nvarchar(255);


UPDATE NashvileHousing
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)



SELECT *
FROM PortfolioProject..NashvileHousing




-- Change Y and N to Yes and No in 'Sold as Vacant' field

SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant)
FROM PortfolioProject..NashvileHousing
GROUP BY SoldAsVacant
ORDER BY 2


SELECT SoldAsVacant, 
CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
WHEN SoldAsVacant = 'N' THEN 'No'
ELSE SoldAsVacant
END
FROM PortfolioProject..NashvileHousing

UPDATE NashvileHousing
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
WHEN SoldAsVacant = 'N' THEN 'No'
ELSE SoldAsVacant
END
FROM PortfolioProject..NashvileHousing


-- Remove Duplicates

WITH ROwNumCTE AS(
SELECT *,
ROW_NUMBER() OVER ( PARTITION BY ParcelID, SalePrice, SaleDate, LegalReference
ORDER BY UniqueID) 
row_num

FROM PortfolioProject..NashvileHousing
-- ORDER BY ParcelID 
)
SELECT *
FROM RowNumCTE
Where row_num > 1
ORDER BY PropertyAddress

-- DELETE Unused columns 

SELECT *
FROM PortfolioProject..NashvileHousing

ALTER TABLE PortfolioProject..NashvileHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress

ALTER TABLE PortfolioProject..NashvileHousing
DROP COLUMN SaleDate