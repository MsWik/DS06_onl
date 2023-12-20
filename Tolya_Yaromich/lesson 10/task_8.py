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


CREATE OR REPLACE FUNCTION delete_employee(employee_id_param INT)
RETURNS VOID
AS $$
BEGIN
  DELETE FROM employees
    WHERE employees.employee_id = delete_employee.employee_id_param;
END;
$$ LANGUAGE plpgsql;



SELECT delete_employee(1);

SELECT * FROM employees;