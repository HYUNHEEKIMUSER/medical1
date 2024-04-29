
--���Ἲ ��������: �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
--not null, nuique, primary key, foreign key, check
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate
);

-- ������ �Է�,���,����,���� �ι� �� �˾ƾߵ�
insert into member (memNo, id,pw,name,gender,mdate) values(
member_seq.nextval,'aaa','1111','ȫ�浿','����',sysdate
);

insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval, 'bbb','1111','������','����'
);

select * from member;

insert into member values(
member_seq.nextval,'ccc','1111','�̼���','����',sysdate
);

--���̺� ����: �Խ��� ���̺� ����
create table board(
bno number(4) primary key,
id varchar2(30), --�ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) --foreign key�� ��Ī(constraint) fk_id�̴�. ��Ī�� ���� �س����� ������ ��Ī�� �˷���
references member(id) --member ���̺��� primary key id 
);

-- primary key�� �����Ϸ��� foreign key ��ϵǾ� �ִ� �����͸� �켱 ������ ��� �ؾߵ�
-- primary key �����Ǹ� ��� �����ϴ� ��� - on delete cascade, ��� �����ϴ� ��� - on update cascade
select * from board;

insert into board(bno, id,btitle,bcontent, bdate, bgroup, bstep, bindent, bhit, bfile) values(
board_seq.nextval, 'aaa', '�����Դϴ�.','�����Դϴ�.',sysdate, board_seq.currval,0,0,1,null
);

insert into board values(
board_seq.nextval, 'bbb', '�����Դϴ�2.','�����Դϴ�2.',sysdate, board_seq.currval,0,0,1,''
);

insert into board(bno, id,btitle,bcontent, bgroup) values(
board_seq.nextval, 'aaa', '�����Դϴ�.3','�����Դϴ�.3', board_seq.currval
);
--����
delete board where bno =3;

commit;

delete member where id = 'aaa';

-- DECODE ���ǹ�
select emp_name,department_id,decode(department_id,10,'�ѹ���ȹ��', 20,'������',30,'����/�����',40,'�λ��') from employees order by department_id asc;

select department_id, department_name from departments;

select * from stu_score_cdate order by avg desc;
--90��-A 80��-B 70��-C

select name,avg,decode(avg,90,'A',80,'B',70,'C')as grade from stu_score_cdate order by avg desc;
select job_id, salary from employees;
--����
--sh_clerk salary *15%, ad_asst *10% MK_rep *5%

select job_id, salary, decode(job_id, 'SH_CLERK', salary+(salary *0.15), 'AD_ASST', salary+(salary *0.10), 'MK_REP', salary+(salary *0.05)) as salary_up from employees order by salary desc;
--job_id, clerk�� ���ִ� job_id�� �˻��Ͻÿ�
select job_id from employees where job_id like '%CLERK';

select name,avg from stu_score_cdate;
select name,avg, case when avg >=90 then 'A' when avg>=80 then 'a' when avg >=70 then 'c' else 'f' end as grade from stu_score_cdate;

select department_id, department_name from departments;
-- case������ ������ department_id �̸��� ����ϼ���
select department_id from employees order by department_id asc;
select department_id, department_name, case when department_id >=100 then '�ڱݺ�' end as depart_name from employees;

--job_id
--clerk���� salary *15, ad_asst*10% rep���� *5% man ���� *2%
--case
select job_id,salary from employees;

select job_id, salary, case when job_id like '%CLERK' then salary+(salary*0.15) end as salary_up from employees order by job_id asc;


--���� ��� ������ ����� 0.15 ��� �̻��� ����� 0.05�� �λ��ؼ� ����ϼ���
--�� ���̺� �����ؼ� ���
select emp_name, salary, case when salary <= (select avg(salary) from employees) then salary+(salary*0.15) 
when salary > (select avg(salary) from employees) then salary+(salary*0.05) end as salary_up from employees;

select emp_name, salary, 
case when salary >= 6461 then 'down' else 'up' end as salary_updown from employees;

-- ���Ʒ� ���� ��ħ �� �� ������ from employees ��ſ� �Ʒ� ���� �� ����
select emp_name, salary, salary_updown, case when salary <= (select avg(salary) from employees) then salary+(salary*0.15) 
when salary > (select avg(salary) from employees) then salary+(salary*0.05) end as salary_up from (select emp_name, salary,
case when salary >= 6461 then 'down' else 'up' end as salary_updown from employees);

-- or ���̽� �ΰ� ���
select emp_name, salary, case when salary <= (select avg(salary) from employees) then up
when salary > (select avg(salary) from employees) then down end as money,
 case when salary <= (select avg(salary) from employees) then salary+(salary*0.15) 
when salary > (select avg(salary) from employees) then salary+(salary*0.05) end as salary_up
from employees;

select * from stu_score_cdate;


-- rank() �Լ� 
select total,rank, rank()over (order by total desc) as ranks from stu_score_cdate;
select rank()over(order by total desc) as ranks from stu_score_cdate;

select total,rank from stu_score_cdate order by total desc;
update stu_score_cdate set rank = 1 where total =291;

-- ----------------------------------------------------------------------------------------
select total, rank from stu_score_cdate order by total desc;
update stu_score_cdate a set rank= (

select ranks from(
select no, rank()over(order by total desc) as ranks from stu_score_cdate) b where a.no=b.no
);

commit;
select * from stu_score_cdate;
-- -----------------------------------------------------------------------------------------


select department_id, case when department_id = 10 then '�ѹ���ȹ��' when department_id = 20  then '������' end as depart_name  from employees order by department_id asc;
select department_id, salary from employees;
select emp_name, department_id from employees;

select emp_name, department_id, department_name from employees, departments;

-- employees.department_id
select emp_name,employees.department_id, department_name from employees, departments;

select emp_name, department_id from employees;
select department_id, department_name from departments; 
select emp_name, employees.department_id, department_name from employees, departments where employees.department_id = departments.department_id;


--�׷��Լ� sum, avg, count, max, min / stddev ǥ������, variance �л�

-- ���� ����
select sum(salary) from employees;
--�������� ���� stu_score
select sum(kor) from stu_score_cdate;

select count(*) from employees;
select count(*) from employees where department_id = 50;

--Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�
select * from employees;
select count(*) from employees where commission_pct is not null;

--select * from employees a (a�� ��Ī group by �ڿ��� ��Ī ����)
select e.employee_id from employees e;
select employees.employee_id from employees, departments;
--��ü �����
select count(*) from employees 
--�μ���ȣ�� 50��
select * from employees;
select count(*) from employees where department_id = 50;

select department_id,count(department_id) from employees group by department_id order by department_id;

-- avg grade �÷�
--stu_score_cdate 90���̻� A 80���̻� B 70���̻� C 60���̻� D 60���̸� F
--A�׷� �� ������ 
select * from stu_score_cdate;
select name, avg, case when avg>=90 then 'A' when avg >=80 then 'B' when avg >=70 then 'C' else 'F' end as grade from stu_score_cdate;  

select  grade,count(grade) from stu_score_cdate 
where (select name, avg, case when avg>=90 then 'A' when avg >=80 then 'B' when avg >=70 then 'C' else 'F' end as grade from stu_score_cdate)group by grade order by grade asc;  

--kor������ 91,92 -> 90 / 81..->80 ���
select trunc(kor,-1),count(*) from stu_score where trunc(kor,-1) = 90 group by trunc(kor,-1); 
select trunc(kor,-1), count((trunc(kor,-1)) from stu_score_cdate group by trunc(kor,-1);

select trunc(kor,-1) from stu_score_cdate;

select k_kor, count(k_kor) as k_count from (select trunc(kor,-1) as k_kor from stu_score_cdate) group by k_kor;

select department_id, count(*) from employees group by department_id order by department_id;
select emp_name, count(emp_name) from employees group by emp_name;

--�μ��� ��� ����
select department_id, round(avg(salary),2) from employees group by department_id order by department_id;

-- clerk rep man�� �������

select job_id from employees where job_id like '%CLERK';
select job_id, count(job_id) from employees where job_id like '%CLERK' group by job_id;

select job_id, substr(job_id,4,5), length(substr(job_id,4,5)) from employees where job_id like '%CLERK';
select job_id, length(job_id) from employees;

--�μ��� (group by department_id)�ִ� ����, �ּҿ���, ��տ���
select department_id,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees
group by department_id
order by department_id
;

select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

--�μ��� ��� �� , Ŀ�̼��� �޴� ��� ���� ����Ͻÿ�
select * from employees;
--�μ��� ����� 
select department_id, count(department_id), count(commission_pct) from employees group by department_id                                                                                                                                                    ;
--�μ��� Ŀ�̼��� �޴� ��� �� ���
select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

-- having group by ������ where �Ϲ� �÷��� ������
select department_id, round(avg(salary),2) from employees group by department_id order by avg(salary);

select department_id, round(avg(salary),2) from employees group by department_id having avg(salary)>= 6000 order by avg(salary);

--emp_name a�� �������� �ʴ� �͸� 
select emp_name from employees where emp_name not like '_a%';

select department_id, round(avg(salary),2) from employees where emp_name not like '_a%' group by department_id having avg(salary) >= (select avg(salary) from employees) order by avg(salary);

-- �μ��� �ִ� ������ 8000 �̻��� �͸� ���
select department_id,salary from employees where salary >=8000 order by salary;
select department_id, max(salary) from employees where emp_name not like '_a%' group by department_id having max(salary) >=8000 order by max(salary);

-- join
select emp_name, department_id, salary from employees;
select department_id, department_name from departments;
select count(*) from employees;
select count(*) from departments;
select count(*) from employees, departments;   --107*27

--equi join ���� Į���� �������� ���� / �������� �����ϴ� �÷��� ���� ��ġ�Ǵ� ���� �����Ͽ� ��� ���� (where emp.deptno = dept.deptno)
--�� ���̺� ���� �÷��� ������ ���ؼ� �ش�Ǵ� �����͸� ��� / null�� �˻����� ����
--1��
select employee_id, emp_name, department_id, salary from employees;
--2��
select department_id, department_name from departments;
--3��
select employee_id, emp_name, employees.department_id, department_name, salary from employees, departments
where employees.department_id = departments.department_id;
--4�� 
select department_id, department_name from departments;

select * from member;
select * from board;
select  member.id,name,btitle,bcontent from board, member where member.id=board.id;
--id ��ſ� �̸� �ִ� ��
select bno,name,btitle,bcontent from board, member where member.id=board.id;

update member set name ='ȫ����' where id = 'aaa';

-- non-equi join ���� Į���� ���� �ٸ� ������ ����Ͽ� ����
--outer join ���� ���ǿ� �������� ���� ����














