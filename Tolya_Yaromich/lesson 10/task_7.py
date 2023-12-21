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
    

CREATE OR REPLACE FUNCTION increase_salary_in_department(department_name VARCHAR(50), percent_increase INT)
RETURNS VOID
AS $$
BEGIN
    -- Здесь напишите запрос для увеличения зарплаты всех сотрудников в указанном отделе
    UPDATE employees
    SET salary = salary + (salary * (percent_increase / 100))
    FROM departments
    WHERE employees.department = departments.department_id
    AND departments.department_name = increase_salary_in_department.department_name;
END;
$$ LANGUAGE plpgsql;


SELECT increase_salary_in_department('IT',20);