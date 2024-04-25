select sysdate-1, sysdate,sysdate+1 from dual;
--�� ���� ���� ù ��° �� / �� ���� ������ ��
select sysdate , trunc(sysdate,'month'), last_day(sysdate) from dual;
--�� ��¥�� �� ��/ �� ��¥�� �� ��
select round(sysdate-hire_date,3) , trunc(months_between(sysdate,hire_date),2) from employees;
--trunc �ϴ��� ����/ group by �׷��Լ�
select trunc(kor,-1) as kor,count(trunc(kor,-1)) from stu_score_cdate group by trunc(kor,-1) order by kor;
--hire_date��¥���� ���� ����Ͻÿ�
select * from employees;
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') from employees;
select to_char(hire_date,'mm') as hire_date, count(to_char(hire_date,'mm')) from employees group by to_char(hire_date,'mm') order by hire_date;
--hire_date���� 2008�⵵�� ����ϰ� �⵵�� �ο� ���� ����Ͻÿ�
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'yyyy') as month_for_hire_date from employees group by to_char(hire_date,'yyyy') order by hire_date;
-- ����ȯ number character date
--number ��Ģ���� ���� ��ǥǥ�þȵ� ��ȭǥ�þȵ�
--char ��Ģ���� �ȵ� ��ǥǥ�ð��� ��ȭǥ�ð��� / to_char,to_date�� ��Ģ�����
--date +- ���� ��¥������´� ����Ұ�

--������,��¥�� �⵵�� ������ ���·� �й��� �ο��Ͻÿ�
--stu_seq �������� ������ 5���й��� ���
--���ڿ� +�� �ȵ�. ko+2024+0001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;
--������Ÿ��
--123,456,789 , 156,778 ,���ϱⰪ
--(123,456,789)+(100,000) = 123556789 ���


--salray
select to_char(salary,'999,999') from employees;

--����Ÿ���� ��¥Ÿ������ ����
select 20040425+3 from dual;
select to_char(20240425)+3 from dual;
select to_date(20240425) from dual;
--����Ÿ���� ��¥ Ÿ������ ����
select emp_name,hire_date from employees where hire_date > to_date(20070101) order by hire_date;
--08���� �Ի��ϰ� ����̸� 2��°�� a�� �� �ִ� ��� ��� 

select to_char(hire_date,'mm') from employees where to_char(hire_date,'mm')=08 order by hire_date;
select emp_name,hire_date from employees where emp_name like '_a%' order by hire_date;
select emp_name, hire_date from employees where emp_name like '_a%' and to_char(hire_date,'mm')=08 order by hire_date;
--or
--01,05,08�� �Ի�
select hire_date from employees where to_char(hire_date,'mm')='01' or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08';
select hire_date from employees where to_char(hire_date,'mm') in(01,05,08);
--�̸�
select emp_name from employees where emp_name like '_a%';
--��ġ��
select emp_name, hire_date from employees where emp_name like '_a%' and to_char(hire_date,'mm') in(01,05,08) order by hire_date;
--20070101���Ŀ� �Ի��� ����̸� 2��°�� a�� �� �ִ� ��� ��� 
select emp_name,hire_date from employees where hire_date > to_date(20070101) and emp_name like '%a%' order by hire_date;
-- +�� �׳� �ϰ� -�� to_date�� �ٿ��ֱ�
select sysdate + '20240401' from dual;
select sysdate - to_date('20240401') from dual;
select sysdate, '2024-04-01', sysdate-to_date('2024-04-01') from dual;

-- create a new table --------------------------------------------------------------
create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;


create sequence seq_m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

date,timestamp
create table m_date (
m_no number(4),
m_yesterday date,m_today date,m_tomorrow date,m_year date
);

insert into m_date(m_no,m_yesterday,m_today,m_tomorrow,m_year) values (
seq_m_no.nextval, sysdate-1,sysdate,sysdate+1,sysdate+365 
);

select * from m_date;
select abs(hire_date-sysdate) from employees;
select hire_date,round(hire_date,'month') from employees;
select hire_date,trunc(hire_date,'month'),round(hire_date,'month') from employees;
select trunc(hire_date,'month') ������ ,hire_date from employees
order by hire_date;

select * from channels;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period='201111';
-- review ----------------------------------------------------
create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);
select * from eventDate;
--�Է� �� ��¥Ÿ�Կ� ����(����-��¥����)�� �Է��ص� �����
--��¥�� ���ڸ� ����� �Ұ��� �׷��� ���ڸ� ��¥Ÿ������ �����ؾ� ��.
insert into eventDate values(seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01'));
select * from eventDate;

--����Ÿ���� ����Ÿ������ ����
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

--null�� 0���� ���� nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;
--manager_id null ceo
select manager_id from employees order by manager_id desc;
--����Ÿ���� ����Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees order by manager_id desc;
commit;
-- new �׷��Լ� count ----------------------------------------------------------------------
select * from employees;
--����� : 107��
select count(emp_name) from employees;
--null���� ������ ���� ����� : 106��
select count(manager_id) from employees;
--null���� count�� �ȵ�
select emp_name,manager_id from employees;
--sum ����
select sum(salary) from employees;
--avg:��� - 6461
select avg(salary) as avg_sal from employees;
--min: �ּҰ� max: �ִ밪
select min(salary),max(salary) from employees;
--avg ��պ��� ���� ��� 6461���� ���� ���
select emp_name, salary from employees where salary > 6461 order by salary; 
select emp_name, salary from employees where salary > (select avg(salary) as avg_sal from employees);
-- min(salary)�� �׷��Լ����� emp_name�̶� ���� ���� �� �� ����
select min(salary) from employees;

--�׷��Լ� sum, avg, count(), count(*), min, max �� / emp_name ���� ���� ������ group by ��ߵ�

--�ּҿ����� �޴� ����� ���, �̸��� ���
select employee_id, emp_name,salary from employees where salary = (select min(salary) from employees);

--�ִ� ���޹޴� ��� ���
select employee_id, emp_name, salary from employees where salary = (select max(salary) from employees);
--�μ���ȣ�� 50���� ����� ��ü ����
select department_id, salary from employees;
--�׷��Լ��� ���� where�� �������� �� ���� �ִ�.
select sum(salary) from employees where department_id= 50;

select count(*) from stu_score_cdate;
--stu_score_cdate���� kor������ 80�� �̻��� �л� ���
select * from stu_score_cdate;
select no,name,kor from stu_score_cdate where kor>=80;
--�������� ��� �̻�, ������������ �������� ����̻��� �л��� ���
select no,name,kor,eng from stu_score_cdate 
where kor >= (select avg(kor) from stu_score_cdate) and eng >= (select avg(eng) from stu_score_cdate) order by no;

select count(*) from stu_score_cdate 
where kor >= (select avg(kor) from stu_score_cdate) and eng >= (select avg(eng) from stu_score_cdate);

--a new table
create table s_info(
sno number,
s_count number
);

insert into s_info values(
stu_seq.nextval,1000
);

--1000�ڸ����ٰ� ��������հ� ����
insert into s_info values(
stu_seq.nextval,(select count(*) from stu_score_cdate 
where kor >= (select avg(kor) from stu_score_cdate) and eng >= (select avg(eng) from stu_score_cdate)));

select * from s_info;

--������ �ִ��� ����� �ּ��� ����� ����� ����� ���
select * from employees;

select emp_name,salary from employees 
where salary=(select max(salary) from employees) or salary = (select min(salary) from employees) or salary <= (select avg(salary) from employees) order by salary;

--�Ҵ밪
select emp_name, salary from employees where salary = (select max(salary) from employees);

--��հ����� ���� ��� �߿� �ִ밪�� ����Ͻÿ�
--1.��հ����� ���� ����� �˻�
select emp_name, salary from employees where salary <= (select avg(salary) from employees);
--2.1������ �ִ밪�� �˻�
select emp_name, salary from employees where salary = 6400;
-- ��հ����� ���� ��� �߿��� �׳��� ���� ���� salary�� �޴� ���
select emp_name,salary from employees where salary = (select max(salary) from employees where salary <= (select avg(salary) from employees));

-- �����Լ�
--lpad / rpad �ڸ��� ���� ��
select emp_name,lpad(emp_name,15,'#') from employees;
select emp_name, rpad(emp_name,20,'@') from employees;
--�� trim (do �߶󳻱�)
select emp_name,ltrim(emp_name,'Do') from employees;

--ko20240001
select 'ko20240001',ltrim('ko20240001','ko2024') from dual;
--substr(������, ����, ����)3��°���� 4���� �ڸ��� ��
select emp_name, substr(emp_name, 3,4) from employees;

-- job_id�� �ִ� SH�� �����ȣ�� �����ؼ� ����ϼ���
select *from employees;
select substr(job_id,0,2)||employee_id from employees;.
select employee_id||substr(job_id,0,2) from employees;

--length
select emp_name,length(emp_name) from employees
where length(emp_name)>15;

--��¥�Լ�
--��¥�� ���ڴ� ���ϱ� ���� ����
select sysdate+1 from dual;
select sysdate-hire_date from employees;
--��¥���� ���� �� �����ѵ� ���ϱ�� �ȵ�
select sysdate + hire_date from employees;
--�ݿø� �÷��� ���ڰ� �ö�(4��25��)
select round(sysdate,'month')from dual;
--4��
select trunc(sysdate,'month')from dual;

select round(sysdate,'year') from dual;
--���� �� ���ϱ�
select add_months(sysdate,3) from dual;
--���� �� ����
select add_months(sysdate,-3)from dual;
--ceil�ø�, floor ���� mod ������ poswer ����
select ceil(-4.2) from dual;
select floor(-4.2) from dual;
select mod(8,3) from dual;
select power(2,10)from dual;

--��� �̸��̶� �Ի糯¥ ���
select * from employees;
select emp_name||to_char(hire_date,' yyyy"��"mm"��"dd"��" day') from employees;
select concat(emp_name,hire_date) from employees;

-- �����,����*1400 �տ� ��ȭǥ�ÿ� ��ǥ�� �����ÿ� (�� ������ 0���� ä��� ���� ���� 0���� �Է�)
select emp_name, to_char(salary*1400,'L999,999,999') from employees; 

--�ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ������ ��¥
-- '2010-10-10'�� �����̶�� ����
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;
-- --------------------------------------------------------------------------------------------------
-- �÷��߰�, ����, ����
select * from member;
--table Ÿ�Ժ���
desc member;
-- DDL(data definition language)- column �߰�
-- commit rollback�� ���� �ٷ� �����
alter table member add gender varchar2(6) default 'female' not null;

--�÷����� - �÷��̸�����, Ÿ�Ժ���
alter table member rename column name to stu_name; 

--�÷� Ÿ�Ժ���
alter table member modify(stu_name varchar2(50));
-- -----------------------------------------------
update member set stu_name = 'ȫ';
--������ �����Ͱ� �����Ϸ��� ũ�⺸�� ���� ��쿡 ����
alter table member modify(stu_name varchar2(6));

--�÷��� Ÿ���� �����Ϸ��� �÷������Ͱ� �� �����̰ų� null�� �� ����
update member set stu_name = '';
alter table member modify(stu_name number(4));
-- ------------------------------------------------------------

alter table member modify(stu_name number(100));

--�÷�����
alter table member drop column phone;

update member set gender = 'male';
commit;






