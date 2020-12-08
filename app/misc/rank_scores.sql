select
    Score score,
    dense_rank() over (order by Score desc) `Rank`
from Scores
order by `Rank`
;