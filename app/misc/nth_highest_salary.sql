CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select Salary
      from (
          select
            Salary,
            dense_rank() over (order by salary desc) rnk
          from Employee
      ) sal
      where rnk = N
      limit 1
  );
END
