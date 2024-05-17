update students set id = 'fff', name ='김유신', gender = 'M' where id='Gawen' and pw='3447';
select * from students;
update students set id = 'ggg', name='홍길자', gender = 'F' where id='Mendie' and pw='2029';
update students set id = 'hhh', name ='홍길순', gender = 'F' where id = 'Alan' and pw='2225';
commit;
--순차적 번호 생성 rownum
select rownum, a.* from students a;
--1. 
select a.* from students a;
--2.
select rownum, a.* from students a order by grade;
--3. order by 구문 실행
select rownum, a.* from students a order by grade;
-- 1.select 2.order by 3.rownum
select * from students order by grade;
--괄호 안에 rownum를 붙여주는 격
select rownum,a.* from 
(select * from students order by grade)a;

--평균이 85점 이상 no >=500 출력
--위아래 같음
select * from stu_score_cdate where avg >=85 and no >=500;
select * from(select*from stu_score_cdate where avg >=85) where no>=500;

-- name,sum(amount),rank 출력하시오.
-- non-equi join으로 처리
select name,s_amount,rank from (select name,sum(amount) s_amount from shop_product where pdate>='2024/03/01'
group by name),customer_rank
where s_amount between lower_amount and high_amount;


--table 명이 shop_product
select name, amount,pdate from shop_product where pdate >= '2024-03-01';
--이름별(group by), 구매내역 합계를 구하시오
--sum(amount) -> 가상으로 만들어진 컬럼 별칭 형태
--가상으로 했을 때 에러가 나면 아래 문장처럼 하기 non-equi join(같은 컬럼이 없으면서 두 개의 테이블을 사용해서 검색하는 방법)
--equi join(같은 컬럼이 두 개의 테이블에 존재해서 2개의 컬럼을 이용해 검색하는 방법)
select name, s_amount,rank from (select name, sum(amount) as s_amount from shop_product
where pdate>='2024/03/01' group by name), customer_rank where
s_amount between lower_amount and high_amount;

-- 위 from shop_product 대신에 이 문장 넣음
select name, sum(amount) as s_amount from shop_product
where pdate>='2024/03/01' group by name;



--non-equi join
select name, avg from stu_score_cdate;
select * from stu_grade;
-- 두 문자 합체
select name, avg,grade from stu_score_cdate, stu_grade where avg between low_score and high_score;

select * from customer_rank;

-- -------------------------------------------------------------------------
select rownum, a.* from students a order by id;

-- 위의 문장처럼하면 id 순 배열이라서 rownum 정렬대로 안됨
-- 먼저 order by를 할 수 있게 괄호 문장을 만들어 줌
select rownum rnum, b.* from (select * from students order by id) b;

-- 2차 테이블을 또 지정해서 rnum 별칭이였는 실제적으로 또 사용될 수 있게 함(부등호 위해서). 
select * from(select rownum rnum, b.* from (select * from students order by id) b)where rnum >= 11 and rnum <=20;

-- ---------------------------------------------------------------------------
-- 괄호 안 select 먼저 실행되고 order by 두 번쨰 실행 밖의 select 세번째 실행 rownum 네 번째 실행
select rownum, a.* from(select * from students order by id)a;

-- rownum 인식 못함
select rownum, a.* from(select * from students order by id)a where rnum >=11;

--  rownum 인식 위해 또 한번 괄호 붙임
select * from (select rownum rnum, a.* from(select * from students order by id) a) where rnum >=11 and rnum <=20;
-- ----------------------------------------------------------------------------
-- order by 를 먼저 한 다음에 row number를 붙이는 것
--위 문장과 다르게 괄호 하나 덜 붙임
select * from (
select row_number() over(order by id) rnum, a.* from students a) where rnum >= 1 and rnum <=10;
-- ---------------------------------------------------------------------------
--부서명을 department_id 옆에 출력하기
select employee_id, emp_name, department_id, manager_id from employees order by department_id;
select * from departments;
select employee_id, emp_name, a.department_id,  department_name, a.manager_id from employees a, departments b where a.department_id = b.department_id order by a.department_id; 

--cross join 107*107
-- 테이블명이 다 똑같아서 컬럼에도 각각 별칭 붙여줌
--equi join 2개의 테이블에 같은 컬럼을 가지고 있는 것 (b에 있는 이름 찾기) - 아래 내용은 self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a,employees b where a.manager_id = b.employee_id order by a.employee_id;
-- 위에서 equi join 같이 해보기 (별칭이 테이블에 단독에 있으면 앞에 별칭 안붙여도 됨)
--self join과 equi join 같이 사용
select a.employee_id, a.emp_name,a.department_id,department_name, a.manager_id, b.emp_name from employees a,employees b ,departments c 
where a.manager_id = b.employee_id and a.department_id = c.department_id order by a.employee_id;

-- self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a, employees b where a.manager_id = b.employee_id;

select * from employees;
--Guy Himuro과 동일한 부서에 근무하는 사람을 출력
--Guy Himuro 부서 출력
--부서번호를 가지고 같은 사람을 출력 
--사원번호 사원명 부서번호, 같이 근무하는 사원명 출력
select a.employee_id, a.emp_name, a.department_id, b.emp_name from employees a, employees b
where a.manager_id = b.employee_id and a.emp_name = 'Guy Himuro';

select a.employee_id, a.emp_name, a.department_id from employees a 
where a.department_id = 30;
-- self join
select e1.emp_name, e1.department_id, e2.emp_name from employees e1, employees e2 where e1.department_id = e2.department_id
and e1.emp_name = 'Guy Himuro';

select * from member;
alter table member add memno number(10);
insert into member values(
member_seq.nextval, 'ggg', 1111, '홍길순', '여자', sysdate 
);
commit;
desc member;
rollback;
update member set name = '홍길동' where id = 'aaa';

--#  employees에 있는 이름으로 검색하는 부분을 로직을 구현하시오
select * from employees;
select emp_name from employees;


select a.emp_name,a.department_id, c.department_name, b.emp_name from employees a, employees b, departments c where a.department_id = b.department_id and 
a.emp_name = 'Pat Fay' and a.department_id = c.department_id;


select * from member order by id;
'hhh',1111,'홍길자','여자',sysdate
commit;

select * from member where id ='aaa';
select * from member;


create table mem(
id varchar2(30) primary key,
pw number,
name varchar2(30),
mdate date
);

select * from mem;
drop table mem;


create table yeogi (
yno number(4) primary key,
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(100),
price number
);

select * from yeogi;



