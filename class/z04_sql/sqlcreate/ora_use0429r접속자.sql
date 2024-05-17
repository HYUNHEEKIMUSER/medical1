
--무결성 제약조건: 부적합한 자료가 입력되지 않도록 하기 위한 규칙
--not null, nuique, primary key, foreign key, check
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate
);

-- 데이터 입력,출력,수정,삭제 부문 잘 알아야됨
insert into member (memNo, id,pw,name,gender,mdate) values(
member_seq.nextval,'aaa','1111','홍길동','남자',sysdate
);

insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval, 'bbb','1111','유관순','여자'
);

select * from member;

insert into member values(
member_seq.nextval,'ccc','1111','이순신','남자',sysdate
);

--테이블 생성: 게시판 테이블 구조
create table board(
bno number(4) primary key,
id varchar2(30), --외래키 등록
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) --foreign key의 별칭(constraint) fk_id이다. 별칭을 따로 해놓으면 에러시 별칭을 알려줌
references member(id) --member 테이블의 primary key id 
);

-- primary key를 삭제하려면 foreign key 등록되어 있는 데이터를 우선 삭제를 모두 해야됨
-- primary key 삭제되면 모두 삭제하는 방법 - on delete cascade, 모두 존재하는 방법 - on update cascade
select * from board;

insert into board(bno, id,btitle,bcontent, bdate, bgroup, bstep, bindent, bhit, bfile) values(
board_seq.nextval, 'aaa', '제목입니다.','내용입니다.',sysdate, board_seq.currval,0,0,1,null
);

insert into board values(
board_seq.nextval, 'bbb', '제목입니다2.','내용입니다2.',sysdate, board_seq.currval,0,0,1,''
);

insert into board(bno, id,btitle,bcontent, bgroup) values(
board_seq.nextval, 'aaa', '제목입니다.3','내용입니다.3', board_seq.currval
);
--삭제
delete board where bno =3;

commit;

delete member where id = 'aaa';

-- DECODE 조건문
select emp_name,department_id,decode(department_id,10,'총무기획부', 20,'마케팅',30,'구매/생산부',40,'인사부') from employees order by department_id asc;

select department_id, department_name from departments;

select * from stu_score_cdate order by avg desc;
--90점-A 80점-B 70점-C

select name,avg,decode(avg,90,'A',80,'B',70,'C')as grade from stu_score_cdate order by avg desc;
select job_id, salary from employees;
--월급
--sh_clerk salary *15%, ad_asst *10% MK_rep *5%

select job_id, salary, decode(job_id, 'SH_CLERK', salary+(salary *0.15), 'AD_ASST', salary+(salary *0.10), 'MK_REP', salary+(salary *0.05)) as salary_up from employees order by salary desc;
--job_id, clerk이 들어가있는 job_id를 검색하시오
select job_id from employees where job_id like '%CLERK';

select name,avg from stu_score_cdate;
select name,avg, case when avg >=90 then 'A' when avg>=80 then 'a' when avg >=70 then 'c' else 'f' end as grade from stu_score_cdate;

select department_id, department_name from departments;
-- case구문을 가지고 department_id 이름을 출력하세요
select department_id from employees order by department_id asc;
select department_id, department_name, case when department_id >=100 then '자금부' end as depart_name from employees;

--job_id
--clerk포함 salary *15, ad_asst*10% rep포함 *5% man 포함 *2%
--case
select job_id,salary from employees;

select job_id, salary, case when job_id like '%CLERK' then salary+(salary*0.15) end as salary_up from employees order by job_id asc;


--월급 평균 이하인 사람은 0.15 평균 이상인 사람은 0.05로 인상해서 출력하세요
--두 테이블 조인해서 출력
select emp_name, salary, case when salary <= (select avg(salary) from employees) then salary+(salary*0.15) 
when salary > (select avg(salary) from employees) then salary+(salary*0.05) end as salary_up from employees;

select emp_name, salary, 
case when salary >= 6461 then 'down' else 'up' end as salary_updown from employees;

-- 위아래 문장 합침 맨 위 문장의 from employees 대신에 아래 문장 다 넣음
select emp_name, salary, salary_updown, case when salary <= (select avg(salary) from employees) then salary+(salary*0.15) 
when salary > (select avg(salary) from employees) then salary+(salary*0.05) end as salary_up from (select emp_name, salary,
case when salary >= 6461 then 'down' else 'up' end as salary_updown from employees);

-- or 케이스 두개 사용
select emp_name, salary, case when salary <= (select avg(salary) from employees) then up
when salary > (select avg(salary) from employees) then down end as money,
 case when salary <= (select avg(salary) from employees) then salary+(salary*0.15) 
when salary > (select avg(salary) from employees) then salary+(salary*0.05) end as salary_up
from employees;

select * from stu_score_cdate;


-- rank() 함수 
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


select department_id, case when department_id = 10 then '총무기획부' when department_id = 20  then '마케팅' end as depart_name  from employees order by department_id asc;
select department_id, salary from employees;
select emp_name, department_id from employees;

select emp_name, department_id, department_name from employees, departments;

-- employees.department_id
select emp_name,employees.department_id, department_name from employees, departments;

select emp_name, department_id from employees;
select department_id, department_name from departments; 
select emp_name, employees.department_id, department_name from employees, departments where employees.department_id = departments.department_id;


--그룹함수 sum, avg, count, max, min / stddev 표준편차, variance 분산

-- 월급 총합
select sum(salary) from employees;
--국어점수 총합 stu_score
select sum(kor) from stu_score_cdate;

select count(*) from employees;
select count(*) from employees where department_id = 50;

--커미션을 받는 사원의 수를 구하시오
select * from employees;
select count(*) from employees where commission_pct is not null;

--select * from employees a (a는 별칭 group by 뒤에는 별칭 못씀)
select e.employee_id from employees e;
select employees.employee_id from employees, departments;
--전체 사원수
select count(*) from employees 
--부서번호가 50번
select * from employees;
select count(*) from employees where department_id = 50;

select department_id,count(department_id) from employees group by department_id order by department_id;

-- avg grade 컬럼
--stu_score_cdate 90점이상 A 80점이상 B 70점이상 C 60점이상 D 60점미만 F
--A그룹 몇 몇인지 
select * from stu_score_cdate;
select name, avg, case when avg>=90 then 'A' when avg >=80 then 'B' when avg >=70 then 'C' else 'F' end as grade from stu_score_cdate;  

select  grade,count(grade) from stu_score_cdate 
where (select name, avg, case when avg>=90 then 'A' when avg >=80 then 'B' when avg >=70 then 'C' else 'F' end as grade from stu_score_cdate)group by grade order by grade asc;  

--kor점수를 91,92 -> 90 / 81..->80 출력
select trunc(kor,-1),count(*) from stu_score where trunc(kor,-1) = 90 group by trunc(kor,-1); 
select trunc(kor,-1), count((trunc(kor,-1)) from stu_score_cdate group by trunc(kor,-1);

select trunc(kor,-1) from stu_score_cdate;

select k_kor, count(k_kor) as k_count from (select trunc(kor,-1) as k_kor from stu_score_cdate) group by k_kor;

select department_id, count(*) from employees group by department_id order by department_id;
select emp_name, count(emp_name) from employees group by emp_name;

--부서별 평균 월급
select department_id, round(avg(salary),2) from employees group by department_id order by department_id;

-- clerk rep man별 월급평균

select job_id from employees where job_id like '%CLERK';
select job_id, count(job_id) from employees where job_id like '%CLERK' group by job_id;

select job_id, substr(job_id,4,5), length(substr(job_id,4,5)) from employees where job_id like '%CLERK';
select job_id, length(job_id) from employees;

--부서별 (group by department_id)최대 월급, 최소월급, 평균월급
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

--부서별 사원 수 , 커미션을 받는 사원 수를 출력하시오
select * from employees;
--부서별 사원수 
select department_id, count(department_id), count(commission_pct) from employees group by department_id                                                                                                                                                    ;
--부서별 커미션을 받는 사원 수 출력
select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

-- having group by 조건절 where 일반 컬럼의 조건절
select department_id, round(avg(salary),2) from employees group by department_id order by avg(salary);

select department_id, round(avg(salary),2) from employees group by department_id having avg(salary)>= 6000 order by avg(salary);

--emp_name a로 시작하지 않는 것만 
select emp_name from employees where emp_name not like '_a%';

select department_id, round(avg(salary),2) from employees where emp_name not like '_a%' group by department_id having avg(salary) >= (select avg(salary) from employees) order by avg(salary);

-- 부서별 최대 월급이 8000 이상인 것만 출력
select department_id,salary from employees where salary >=8000 order by salary;
select department_id, max(salary) from employees where emp_name not like '_a%' group by department_id having max(salary) >=8000 order by max(salary);

-- join
select emp_name, department_id, salary from employees;
select department_id, department_name from departments;
select count(*) from employees;
select count(*) from departments;
select count(*) from employees, departments;   --107*27

--equi join 동일 칼럼을 기준으로 조인 / 공통으로 존재하는 컬럼의 값이 일치되는 행을 연결하여 결과 생성 (where emp.deptno = dept.deptno)
--두 테이블간 같은 컬럼을 가지고 비교해서 해당되는 데이터를 출력 / null은 검색되지 않음
--1번
select employee_id, emp_name, department_id, salary from employees;
--2번
select department_id, department_name from departments;
--3번
select employee_id, emp_name, employees.department_id, department_name, salary from employees, departments
where employees.department_id = departments.department_id;
--4번 
select department_id, department_name from departments;

select * from member;
select * from board;
select  member.id,name,btitle,bcontent from board, member where member.id=board.id;
--id 대신에 이름 넣는 것
select bno,name,btitle,bcontent from board, member where member.id=board.id;

update member set name ='홍길자' where id = 'aaa';

-- non-equi join 동일 칼럼이 없이 다른 조건을 사용하여 조인
--outer join 조인 조건에 만족하지 않은 조인














