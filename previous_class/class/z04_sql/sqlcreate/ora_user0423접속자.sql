select * from students;

alter table students add rank number(3);

update students set rank = 0;
commit;

select no, rank()over(order by total desc) as ranks from students;
update students s1 set rank=(select ranks from(select no,rank() over(order by total desc)
as ranks from students) s2 where s1.no=s2.no);

select manager_id from employees order by manager_id desc;
select max(hire_date)-min(hire_date) from employees order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math) from students;

--hire_date�� �������� �÷��� �����ȣ, �����, job_id-����,�Ի���,���� �÷��� ����ϼ���
select * from employees;
select employee_id, emp_name, job_id, hire_date, salary from employees order by hire_date desc;

--�޿��� ���� �޴� ������ ����ϰ� ������ ������ ��������� ���� ����
select salary,emp_name from employees order by salary,emp_name desc;

--�����Լ�
-- abs (from �� �ƹ� �͵� ���� �� dual�� �������̺� ����� ��)
select -10, abs(-10) from dual;
-- floor() as f / round() as r : ��Ī ����
select 34.789, floor(34.789) as f,round(34.789) as r from dual;
--round(���, �ڸ���) ex) round(34.178,2) 2�ڸ����� ǥ��
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from students;
--as ��Ī ������ �ٲ� �� ����
select round(avg,2) as avg from students;
select round(avg,2) from students;
-- -1�� �־ �����κ� �ݿø�
select 34.5678 ,round(34.5678,-1) from dual;
--trunc ������ �ڸ��� ���� ����
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;
--������ �ø� (-1�ȵ�)
select ceil(34.123) from dual;

--�������� �ϴ��� �����ؼ� ����Ͻÿ�
select * from students;
select trunc(kor,-1) as revised_kor from students order by kor;

--����, ����, ���� ������ �ϴ��� �����Ͽ� ����, ����, ���� �հ踦 ����ϼ���
select * from students;
select trunc(kor,-1) as revised_kor,trunc(eng,-1)as revised_eng,trunc(math,-1) as revised_math, (trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) as revised_total from students;
--mod ���������
select round(100/7,2) from dual;
select mod(10,7) from dual;
select 10/7 from dual;

--�����ȣ�� ¦���� ���� ����Ͻÿ�
--���̽� employee_id%2 = 0
select employee_id from employees;
select employee_id from employees where mod(employee_id,2)=0;
--���̽� 10//7
select floor(10/7) from dual;
--������
select mod(10,7) from dual;

-- �й��� 3�� ����� �͸� ����Ͻÿ�
select * from students;
select no, name from students where mod(no,3) = 0;

--������
-- 1������, 1���� ����, �ּҰ� 1, �ִ밪 9999, ��ȯ���� ����, ĳ�û������ ����
create sequence seq_no  increment by 1 start with 1 minvalue 1 maxvalue 9999  nocycle  nocache;
--nextval ��������ȣ 1�� ����
select seq_no.nextval from dual;
--currval ������ ��ȣ Ȯ��
select seq_no.currval from dual;

--drop table member;
create table member (
mno number(4),
id varchar2(30),
pw varchar(20),
name varchar2(30),
phone varchar2(15)
);

select seq_mno.nextval from dual;

create sequence seq_mno increment by 1 start with 1 minvalue 1 maxvalue 9999 nocycle nocache;
insert into member values(seq_mno.nextval,'eee','1111','�豸','010-5555-5555');
select * from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;
--currval ���� �� Ȯ��
select 's0001'||to_char(seq_mno.currval) from dual; 
--'00000' �ڸ��� / nextval ����
select 's'||to_char(seq_mno.nextval,'00000') from dual; 

--�ѱ����б� ko202400001 ������ seq_kono 1-99999
create sequence seq_kono increment by 1 start with 1 minvalue 1 maxvalue 99999 nocycle nocache;
--trim ��������
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;
select '�ѱ����б� ko2024'||to_char(seq_mno.nextval,'00000') as "seq_kono" from dual;
--�Խ���
create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

--������ ���� 1001 ���� 10 �ּҰ� 1 �ִ밪 99999
--5�������� �غ����� / seq_deptno
create sequence seq_deptno increment by 10 start with 1001 minvalue 1 maxvalue 99999 cycle nocache;
select to_char(seq_deptno.nextval,'00000') as seq_deptno from dual;

create table emp01(
empno number(4) primary key,
ename varchar(20),
hire_date date
);

create sequence emp_seq 
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle 
nocache;

alter sequence emp_seq increment by 1001;

insert into emp01 values(
emp_seq.nextval, '�̼���', sysdate
);

select * from emp01;
commit;

-- emp ���̺� �ڷḦ �Ի����� ������������ ���� �Ͽ� �ֱ� �Ի��� ������ ���� ����ϰ� �����ȣ, ����� ���� �Ի��� Į���� ����ϴ� ������
select* from employees;

select employee_id, emp_name, job_id, hire_date from employees order by hire_date desc; 
--������� �Ի��� �ϼ��� ����ϼ���
select employee_id, emp_name, job_id, hire_date,ceil(sysdate-hire_date)||'��' from employees order by hire_date desc; 

select emp_name from employees;

--���ް� ����� ���ļ� ����ϼ���
select * from employees;
select job_id||employee_id from employees;
select substr(job_id,0,2) from employees;
select emp_name,substr(emp_name,1,3) from employees;
--���ڿ� �ڸ��� �Լ�(2��° �ڸ����� 3�� ��������), substr(���,������ġ,����)
select substr('abcde',2,3) from dual;

--job_id���� �տ� 2�� ���ڿ� ��� 5�ڸ� 00101�ڸ��� ����� �Բ� ����Ͻÿ�
select job_id, employee_id from employees;
--����
select substr(job_id,1,2)||substr('00'||employee_id,0,5) from employees;
--������ ��
select substr(job_id,0,2)||trim(to_char(employee_id,'00000')) from employees;

--��¥�Լ�
select sysdate from dual;
select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
--�� ��¥ ������ ���� �� Ȯ��
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;
--���� ���� �߰�
select sysdate,add_months(sysdate,2) from dual;
--�Է��� �������� ���� �� ������ �˷���
select next_day(sysdate,'������') from dual;
--�Է��� �������� �� ���� ������ ���� �˷���
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;

















