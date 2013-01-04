/**
  * If the business rules specify that the email field should/can be
  * unique, then we should add a UNIQUE constraint to the email
  * field.  The following query would then suffice -
  */

select company.name,
       count(*) as email_address_count
from company
join contact
    on (company.id = contact.company_id)
group by company.name
order by email_address_count desc;

/**
  * However, if the unique constraint does not apply,
  * we should use this -
  */

with unique_email_addresses_by_company as (
    select distinct company.name as company_name,
                    contact.email as contact_email
    from company
    join contact
        on (company.id = contact.company_id)
)
select company_name,
       count(*) as email_address_count
from unique_email_addresses_by_company
group by company_name
order by email_address_count desc;

/**
  * Alternatively, for RDBMS that do not support common table
  * expressions you can use a subquery -
  */

select company_name,
       count(*) as email_address_count
from (
    select distinct company.name as company_name,
                    contact.email as contact_email
    from company
    join contact
        on (company.id = contact.company_id)
) as sq
group by company_name
order by email_address_count desc;
