select max(Salary) SecondHighestSalary
from Employee
where Id not in (
    select Id
    from Employee
    where Salary = (
        select max(Salary)
        from Employee
    )
)
;