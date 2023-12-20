CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL,
    department INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

INSERT INTO employees (first_name, last_name, salary, department) VALUES
    ('John', 'Doe', 50000, 1),
    ('Jane', 'Smith', 60000, 1),
    ('Bob', 'Johnson', 55000, 1),
    ('John', 'Doe', 50000, 2),
    ('Jane', 'Smith', 60000, 2),
    ('Bob', 'Johnson', 55000, 2),
    ('John', 'Doe', 50000, 3),
    ('Jane', 'Smith', 60000, 3),
    ('Bob', 'Johnson', 55000, 3);
    
    INSERT INTO departments (department_name) VALUES
    ('IT'),
    ('HR'),
    ('Finance');
    

CREATE OR REPLACE FUNCTION get_avg_salary_in_department(department_name VARCHAR(50))
RETURNS NUMERIC(10, 2)
AS $$
DECLARE
    avg_salary NUMERIC(10, 2);
BEGIN
    SELECT AVG(employees.salary) INTO avg_salary
    FROM employees 
    JOIN departments ON employees.department = departments.department_id
    WHERE departments.department_name = get_avg_salary_in_department.department_name;

    RETURN avg_salary;
END;
$$ LANGUAGE plpgsql;


SELECT get_avg_salary_in_department('IT');
