--20,000/10,000 �������� ���� ������ �ؼ� 10,000 ����ϼ���
--number�� ����ȯ
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999') from dual;

select commission_pct from employees;
--�������� = ���� + (����*Ŀ�̼�) ������������ �ؼ� ����ϼ���
select*from employees;
select salary, salary + (salary*nvl(commission_pct,0)) from employees;
--commission_pct null ���� ���
select emp_name, commission_pct from employees where commission_pct is null;
--manager_id null�̸� 0�Է�
select nvl(manager_id,0) from employees order by manager_id desc;
--manager_id null�̸� ceo�Է�
select nvl(to_char(manager_id),'ceo') from employees order by manager_id desc;
