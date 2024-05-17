select * from employees;

-- k_sal�� ��Ī��
select salary, salary *1400 as k_sal from employees;
select department_id from employees;

select nvl(department_id,0) from employees;

--������ �ʹ� �� as ��Ī�� ������ ���� ������ ���� / ""�� �־��ָ� �ҹ��� ���Ѽ� ����/�ѱۻ�� ���� / ""�� �ִ� �״�� ����
select salary, salary + (salary * nvl( commission_pct,0)) as "real_sal" from employees;

select * from departments;
select department_id, department_name from departments;

--���� ���� �����͸� 1�� ���ļ� �Ѱܾ� �� ��� concat
-- concat(��ġ��)ȫ�浿,������,�̼���,�豸,������ / split(�и�) -> split(",")

select * from stu_score;
--concat ||
select kor||','||eng||','||math as stu from stu_score;

select kor+eng+math as total,(kor+eng+math)/3 from stu_score;
--distinct: �ߺ��� ���� �Ǿ �Ѿ�� / where ��Ī is not null: null ������
select distinct department_id from employees where department_id is not null;

select manager_id from employees;
select distinct manager_id from employees;
select distinct manager_id from employees where manager_id is not null;

select * from employees;

select employee_id,salary from employees where employee_id = 200;
select employee_id, salary from employees where employee_id  = 200 or employee_id = 201 or employee_id =202;

select *from employees where employee_id >=200 and employee_id <=203;
select * from employees where employee_id >=150 or employee_id <=200;

--department_id 10,30,50�� �ش�Ǵ� ����� ����Ͻÿ�
select employee_id, department_id from employees where department_id = 10 or department_id = 30 or department_id = 50;

-- 1)���� 6000-9000������ ����� ����ϼ���
--order by �÷� asc(��������), desc(����) (order by salary asc / order by salary desc)
select * from employees;
select salary from employees where salary >= 6000 and salary <=9000 order by salary;
-- 2)������ 6000,7000,8000�� ���
select salary from employees where salary =6000 or salary = 7000 or salary =8000;
-- 3)�μ���ȣ�� 50���̸鼭 ������ 8000�̻��� ����� ����ϼ���
select * from employees;
select department_id, salary from employees where department_id = 50 and salary >=8000;
--stu_score���� �̸��� ȫ�浿�� ����� ����ϼ���
select * from stu_score where name ='ȫ�浿';
--�� name �� �ϳ��� ����
select name from stu_score where name ='ȫ�浿'; 

--���� ����
select hire_date from employees order by hire_date desc;

select emp_name,hire_date from employees where hire_date >='02/01/01' order by hire_date asc;

select hire_date,hire_date+100 from employees;
--round �ݿø� ���� ��¥���� hire_date ����
select round( sysdate-hire_date,2) from employees;

select * from employees;
--concat ���� ��ġ�� 
select emp_name||email from employees;

--�Ի����� 05�� �̻� 06�� �����̸鼭 ������ 6000�޷� �̻��� ����� �Ի��� �������� ����Ͻÿ�.
select * from employees;
select emp_name, hire_date, salary from employees where salary >=6000 and hire_date>='05/01/01' and hire_date<='06/12/31' order by hire_date desc;
--10���� �ƴ� �͸� ��� / not -> !=,<>,not
select department_id from employees where department_id !=10 and not department_id =50 order by department_id;

--5000�̻� 9000����
select emp_name, salary from employees where salary >=5000 and salary <=9000 order by salary;

--����� 99�� �̻��� �л��� �˻��ϼ���
select * from stu_score;
select name, avg from stu_score where avg >=99 order by avg;

select * from students;
update students set name='�̼���' where no=3;
commit;

--students
--���� 70�� �̻� ����� 75�� �̻��� �л��� ����Ͻÿ�.
select name,kor,avg from students where kor >=70 and avg >=75 order by avg;

--�������� 80��, ���� 70�� ���� 90���� �л��� ����Ͻÿ�
select name, kor from students where kor =70 or kor = 80 or kor =90 order by kor;
--total�� avg ���� �ٲٱ�
update students set kor =100 where no=1;
rollback;
--������Ʈ �� ����
update students set kor = 100, total =100+eng+math, avg = (100+eng+math)/3 where no=1;
select * from students where no=1;

-- �������� 80~90�� �̻��� �л��� ����ϼ���
select name,kor from students where kor >= 80 and kor <=90 order by kor;
select kor from students where kor between 70 and 90;
--80���� 90�� ���� a���� ũ�ų� b���� ���� ��
select kor from students where kor not between 70 and 90;
--��¥
select hire_date from employees order by hire_date;
--99�⺸�� ũ�ų� ���� , 01���� �۰ų� ���� ��� �˻��ϱ�
select emp_name,hire_date from employees where hire_date between '99/01/01' and '01/12/31' order by hire_date;
select emp_name,hire_date from employees where hire_date >'99/01/01' and hire_date < '01/12/31';

--in ���� ������ �ʵ带 ���� �� ������.. kor = 80 kor = 70 kor  =90�� ���� �� 
select name, kor from students where kor in(80,70,90);
select name, kor from students where kor not in(80,70,90);

--�̸��˻� (% : ���Ѵ�) ȫ�� ��ﳪ�� �� �� �� '%ȫ%'�̶�� ���� �� ��µ� ('%ȫ': �����ڰ� ȫ���� ������ �� ã�� ��)('ȫ%': ���� ���ڰ� ȫ���� ������ �� ã�� ��)
--%��%: ���� ���ԵǾ� �ִ� �ܾ� �˻� 
select * from students where name like '%ȫ%';
--������ ���� �̸��� �˻��ϴ� ��
select * from students where name like '%��';

--  _: �� ĭ�� ������ ��� _:�� �տ� ��� �ܾ �ְ� ���� �߰��� �� ���� �� ���� �� ��
select * from students where name like '_��%';
--�̸� ���� ° t�� �� �ִ� ��
select name from students where name like '__t%';
--�̸��� 4�ڸ��� 3��° r�� �� �ִ� �̸�
select name from students where name like '__r_';

select name from students where length(name) = 4;

select * from students where name like '__r%' and length(name)=4;

--�̸��� A�� ���۵Ǵ� ���� �˻�
select name from students where name like 'A%';

--�̸��� a�� �� �ִ� �л� �˻�
select name from students where name like '%a%';
select name from students where name like '%A%';

--��ҹ��� ���о��� a�� �� �ִ� �л� �˻�
--�ҹ��� ��ȯ(lower),�빮�� ��ȯ(upper), ù ���ڸ� �빮�ڷ� ��ȯ(initcap)
select no,name from students where lower(name) like '%a%'; 
--a�� ���� �ȵ� �̸�
select no, name from students where lower(name) not like '%a%';

select * from employees;
select employee_id, emp_name, manager_id from employees where manager_id=100;
-- null�� ��񱳰� �ȵ�
select employee_id, emp_name, manager_id from employees where manager_id = null;
select employee_id,emp_name,manager_id from employees where manager_id is null;
select employee_id,emp_name,manager_id from employees where manager_id is not null;
--�ѱ��̸� ������ ����
select * from stu_score order by name desc;
--1�� ���� ������ ���� ������ �� ������ ���� ������ ��쿡�� ���������� ��������
select * from students;
select * from students order by kor desc, eng asc;

--total�� ���� ����
select total from stu_score order by total desc;

--�÷��߰�
alter table students add rank number(3);
desc students;
select * from students;
update students set rank =0;
commit;

--���
select no,name, total,rank() over(order by total desc) as rank from students;

--����
update students set rank = 13 where no =1;
update students s1 set s1.rank =13 where no=1; 

-- ����2 (ù ��° ����: update students s1) (�� ��° ����: select no no2, rank() over(order by total desc ) as ranks from students) -> ���� ����
update students s1 set rank = (select ranks from (select no no2, rank() over(order by total desc ) as ranks from students) s2 where s1.no = s2.no2 );
select * from students;

-- ���Ŀ� ������ ��
update students s1 set rank = 13 where no = 1;
update students set rank = 0;
--��ü �߿��� ���� 70�� �̻��� ã�� ��
select * from studenets where kor >=70;
-- avg 60��~100������ 70�� �̻��� ã�� ��
select *from(select * from students where avg >=60) where kor >=70 ;

























