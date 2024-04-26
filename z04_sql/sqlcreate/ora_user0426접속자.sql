create table emp01(
emp_id number (6),
emp_name varchar2 (80),
hire_date date
);

update emp01 where hire_date date(500);

--���̺� ���� ����
desc employees;
select * from emp01;

--employees�� �ִ� ��� ������ emp02 ���̺� �ֱ�
create table emp02 as select * from employees;
select * from emp02;

--���̺� ������ �����ϱ�
create table emp03 as select * from employees where 1=2;
select * from emp03;

-- ���̺��� �����ϸ鼭 �����͸� �����ϱ� (3�� -> 14��)
insert into emp01(emp_id, emp_name, hire_date) select employee_id, emp_name hire_date from employees;

--1�� ������ �߰�
insert into emp01 values(
207,'ȫ�浿','2024-04-26'
);

--���̺��� ������ �����鼭 �����͸� ���� (������ ���� ���)
insert into emp03 select * from employees;

select * from emp03;
select * from emp01 order by emp_id desc;
select * from employees;

drop table m_date;
delete emp01 where emp_id=207;

-- -------------------------------------------------------------------------------------------
desc member;
--Ÿ�Ժ���
alter table member modify(stu_name varchar2(30));

--�÷�����
alter table member drop column pw;
--�÷� �߰�
alter table member add (pw varchar2(30));

select * from member;

insert into member values(
seq_mno.nextval,'fff','������','male','1111'
);

--�÷����� ���� 
--1.stu_name �����
alter table member modify stu_name invisible; 
alter table member modify gender invisible;

--�� ������ �ڸ� �̵� �̷� ������ ���� ���� ����
alter table member modify stu_name visible; 
alter table member modify gender visible;

--invisible�̶� ����
--�Ͻ����� �������
alter table member set unused(id);
select * from member;
--�÷� ��� ���� ����
alter table member drop unused columns;

drop table emp03;

--���̺� �̸� ����
rename emp01 to employees01;

desc employees;

--[���Ἲ ��������]
--foreign key �ٸ� ���̺��� ������ �Է� �� ����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ� �� Ȯ�� 


create table member(
id varchar2 (30) primary key,
pw varchar2 (30) not null,
name varchar2(30), 
gender varchar2(6)
);

--�̸��� ���� ������ ���� �ʾƼ� �̸��� �����ص� �� id�� pw�� ���� ������ ����
insert into member(id,pw,name) values(
'a','1111','ȫ�浿'
);

select * from member;

--null ���� ����
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
'5555','������','������','05'
);

select * from emp02;

update emp02 set job = '����' where deptno = 2;

--unique: �ߺ��� ����
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp03 values(
1,'�豸','3',3
);

select  * from emp03;

--1�� ȫ�浿 �˻��ϼ���
select empno from emp03 where empno=1;
select * from emp03 where empno =1;

--null, ȫ�浿 �˻�
select * from emp03 where empno is null and ename = 'ȫ�浿'; 

-- null�� ��� ��� �˻�
select * from emp03 where empno is null;

--primary key�� �÷� �ϳ��� ã�� �� �ִµ� unique�� �ϳ� �� �˻��� �ؾߵ� ���� �ִ�(primary key�� null�� �ȵ�)
create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);
--5�� null, 1,2,3,1
insert into emp01 values(
4, '�豸', '����', 04
);
select * from emp01;




-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- foreign key (�ܷ�Ű): �ݵ�� primary key�� �־�� ��
drop table emp01;

--emp01 ���̺� ����
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

alter table emp01 modify(deptno number(6));
insert into emp01 values(
1,'ȫ�浿','0001', 10
);

insert into emp01 values(
3,'������','0002',30
);

--foreign key ����
alter table emp01 drop constraint fk_deptno;

--foreign key ���� �� deptno�� ���� �����͸� �߰��� �Է��� �� ����.
insert into emp01 values(
5,'������','0004',280
);


commit;
--emp01 foreign key �߰�(fk_daptno ��Ī)
--add constraint+��Ī / foreign key+�����÷�/ references+�ٸ����̺�(�÷��̸�)
alter table emp01 add constraint fk_deptno foreign key(deptno)
references dept01(deptno);

select * from emp01;





--dept01 ���̺� ����
create table dept01(
deptno number(2) primary key,
dept_name varchar2(20)
);

alter table dept01 modify(deptno number(6));
alter table dept01 modify(dept_name varchar2(80));

desc departments;
insert into dept01(deptno,dept_name) select department_id, department_name from departments;

select * from departments;

desc member;
-- ---------------------------------------------------------------
create table board(
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(
8, 'bbb', '�Խñ�8','����8'
);

commit;

select * from board;

alter table board add constraint fk_id foreign key(id) references member(id);

--comment ���̺� ������̺� 
create table comments(
cno number(4) primary key, 
bno number(4), 
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno) 
references board(bno)
);
--��۴ޱ�
insert into comments values(
5,2,'1111','��۳���4'
);
--fk�� ����� �� ����
--jk�� ����� �� ���� �θ��� foreign key�� ��ϵǾ� �ִ� ��� �����͸� ������Ű�� ��
--kfŰ�� ��ϵǾ� �ִ� ��� �����ʹ� ��� ���� ��Ű�� ��.
delete board where bno = 5;

commit;
select * from board;
select * from comments;

--�ܷ�Ű ����
alter table board drop constraints fk_id;
alter table comments drop constraint fk_bno;

select * from board;
select * from comments;

delete comments where cno=2;
delete board where bno=1;

alter table board add constraints fk_id foreign key(id) references member(id);

--fk_cno�� ������ �ǵ��� ��. (update cascade: �θ�Ű�� �����Ǿ ����ְ� �ϴ� ��) (on delete cascade: �θ� �����Ǿ����� ���� �����Ǵ� ��)
alter table comments add constraints fk_bno foreign key(bno) references comments(cno) on delete cascade;

--foreign key�� �����ϸ� ������ ��Ʈ�� �ϰ� ���ο� ������ �Է��� ���ϰ� ������ �� �� ����
--unique�� �ߺ��� �ȵǰ� null�� ����
--check�� ������ �͸� ���� �� ��

-- check ���� ���� Ư������ ����, Ư������ �Էµǵ��� ��. 
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', --�÷��� �����͸� ���� ������ �ڵ����� 0001�� �����
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in ('����','����'))
);
--���� ���� ����
insert into emp(empno, ename, job, sal, gender) values(
3,'�̼���','0004',5000,'��'
);
insert into emp(empno, ename, job, sal, gender) values(
5,'�豸','0006',1000,'����'
);

--job default - job �Է��� ������ �ڵ����� 0001�� ������
insert into emp(empno, ename, sal, gender) values(
6,'������',10000,'����'
);

select * from emp;










