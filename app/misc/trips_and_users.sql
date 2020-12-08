select
  all_trips.Request_at Day,
  coalesce(round(cancelled_trips.amount / all_trips.amount, 2), 0) 'Cancellation Rate'
from (
    select t.Request_at, count(0) amount
    from Trips t
        inner join Users c on t.Client_Id = c.Users_id
        inner join Users d on t.Driver_Id = d.Users_id
    where c.Banned = 'No'
      and d.Banned = 'No'
      and Request_at between '2013-10-01' and '2013-10-03'
    group by t.Request_at
) all_trips
left outer join (
    select t.Request_at, count(0) amount
    from Trips t
        inner join Users c on t.Client_Id = c.Users_id
        inner join Users d on t.Driver_Id = d.Users_id
    where c.Banned = 'No'
      and d.Banned = 'No'
      and t.Request_at between '2013-10-01' and '2013-10-03'
      and t.Status <> 'completed'
    group by t.Request_at
) cancelled_trips
on cancelled_trips.Request_at = all_trips.Request_at
;