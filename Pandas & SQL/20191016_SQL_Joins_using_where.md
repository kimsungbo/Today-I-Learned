# SQL Joins Using WHERE or ON

## Write a query that shows a company's name, "status" (found in the Companies table), and the number of unique investors in that company. Order by the number of investors from most to fewest. Limit to only companies in the state of New York.


``` sql
SELECT com.name
        , com.status
        , count(DISTINCT inv.investor_name) AS num_investors
FROM tutorial.crunchbase_companies AS com
LEFT JOIN tutorial.crunchbase_investments AS inv 
ON com.permalink = inv.company_permalink
WHERE com.state_code = 'NY'
GROUP BY com.name, com.status
ORDER BY num_investors DESC;
```

## Write a query that lists investors based on the number of companies in which they are invested. Include a row for companies with no investor, and order from most companies to least.


```sql
SELECT CASE WHEN investments.investor_name IS NULL THEN 'No Investors'
            ELSE investments.investor_name END AS investor,
       COUNT(DISTINCT companies.permalink) AS companies_invested_in
  FROM tutorial.crunchbase_companies companies
  LEFT JOIN tutorial.crunchbase_investments investments
    ON companies.permalink = investments.company_permalink
 GROUP BY investor
 ORDER BY companies_invested_in DESC;
```