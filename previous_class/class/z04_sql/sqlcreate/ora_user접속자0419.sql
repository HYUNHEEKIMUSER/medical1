select * from employees;
--�޷��� ��ȭ�� ȯ��
select employee_id,emp_name,salary from employees;
select employee_id,emp_name,salary,salary*1381.79 from employees;

-- ���� *12 =����
select employee_id, emp_name, salary*12 from employees;
-- ������ ��ȭ�� ȯ��
select employee_id, emp_name,salary*12 ,(salary*12)*1381.79 from employees;

--Ŀ�̼��� �������� = ���� + ����*Ŀ�̼�
--commission_pct
select * from employees;
--nvl(�ķ�,0) Ŀ�̼��� 0�� ��쿡 ����
select employee_id, emp_name, nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;
select employ_id,emp_name,commission_pct,salary+(salary*commission_pct) from employees;

