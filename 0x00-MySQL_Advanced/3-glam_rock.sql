-- lists all bands with Glam rock as their main style, ranked by their longevity

WITH BandLifespan AS (
    SELECT 
        band_name,
        COALESCE(split, 2020) - COALESCE(formed, 0) AS lifespan
    FROM 
        metal_bands
    WHERE 
        style LIKE '%Glam rock%'
)
SELECT 
    band_name,
    lifespan
FROM 
    BandLifespan
ORDER BY 
    lifespan DESC;
