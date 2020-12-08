select tmp.Department, tmp.Employee, tmp.Salary
from (
    select
        d.Name Department,
        e.Name Employee,
        e.Salary,
        dense_rank() over (partition by d.Id order by e.Salary desc) rnk
    from Employee e
        inner join Department d on e.DepartmentId = d.Id
) tmp
where rnk in (1, 2, 3)
;