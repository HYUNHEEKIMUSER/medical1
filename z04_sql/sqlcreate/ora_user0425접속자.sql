select sysdate-1, sysdate,sysdate+1 from dual;
--그 달의 제일 첫 번째 일 / 그 달의 마지막 일
select sysdate , trunc(sysdate,'month'), last_day(sysdate) from dual;
--두 날짜간 일 수/ 두 날짜간 달 수
select round(sysdate-hire_date,3) , trunc(months_between(sysdate,hire_date),2) from employees;
--trunc 일단위 버림/ group by 그룹함수
select trunc(kor,-1) as kor,count(trunc(kor,-1)) from stu_score_cdate group by trunc(kor,-1) order by kor;
--hire_date날짜에서 월만 출력하시오
select * from employees;
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') from employees;
select to_char(hire_date,'mm') as hire_date, count(to_char(hire_date,'mm')) from employees group by to_char(hire_date,'mm') order by hire_date;
--hire_date에서 2008년도를 출력하고 년도별 인원 수를 출력하시오
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'yyyy') as month_for_hire_date from employees group by to_char(hire_date,'yyyy') order by hire_date;
-- 형변환 number character date
--number 사칙연산 가능 쉼표표시안됨 원화표시안됨
--char 사칙연산 안됨 쉼표표시가능 원화표시가능 / to_char,to_date는 사칙연산됨
--date +- 가능 날짜출력형태는 변경불가

--시퀀스,날짜의 년도를 가지고 형태로 학번을 부여하시오
--stu_seq 시퀀스를 가지고 5개학번을 출력
--문자열 +가 안됨. ko+2024+0001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;
--문자형타입
--123,456,789 , 156,778 ,더하기값
--(123,456,789)+(100,000) = 123556789 출력


--salray
select to_char(salary,'999,999') from employees;

--숫자타입을 날짜타입으로 변경
select 20040425+3 from dual;
select to_char(20240425)+3 from dual;
select to_date(20240425) from dual;
--숫자타입을 날짜 타입으로 변경
select emp_name,hire_date from employees where hire_date > to_date(20070101) order by hire_date;
--08월에 입사하고 사원이름 2번째에 a가 들어가 있는 사람 출력 

select to_char(hire_date,'mm') from employees where to_char(hire_date,'mm')=08 order by hire_date;
select emp_name,hire_date from employees where emp_name like '_a%' order by hire_date;
select emp_name, hire_date from employees where emp_name like '_a%' and to_char(hire_date,'mm')=08 order by hire_date;
--or
--01,05,08월 입사
select hire_date from employees where to_char(hire_date,'mm')='01' or to_char(hire_date,'mm')='05' or to_char(hire_date,'mm')='08';
select hire_date from employees where to_char(hire_date,'mm') in(01,05,08);
--이름
select emp_name from employees where emp_name like '_a%';
--합치기
select emp_name, hire_date from employees where emp_name like '_a%' and to_char(hire_date,'mm') in(01,05,08) order by hire_date;
--20070101이후에 입사한 사원이름 2번째에 a가 들어가 있는 사람 출력 
select emp_name,hire_date from employees where hire_date > to_date(20070101) and emp_name like '%a%' order by hire_date;
-- +는 그냥 하고 -는 to_date로 붙여주기
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
select trunc(hire_date,'month') 기준일 ,hire_date from employees
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
--입력 시 날짜타입에 문자(형태-날짜형태)를 입력해도 저장됨
--날짜와 문자를 빼기는 불가능 그래서 문자를 날짜타입으로 변경해야 함.
insert into eventDate values(seq_mno.nextval,sysdate,'2024-04-01',sysdate-to_date('2024-04-01'));
select * from eventDate;

--문자타입을 숫자타입으로 변경
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

--null을 0으로 변경 nvl()
select salary, commission_pct, salary+(salary*nvl(commission_pct,0)) from employees;
--manager_id null ceo
select manager_id from employees order by manager_id desc;
--숫자타입을 문자타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees order by manager_id desc;
commit;
-- new 그룹함수 count ----------------------------------------------------------------------
select * from employees;
--결과값 : 107명
select count(emp_name) from employees;
--null값이 있으면 제외 결과값 : 106명
select count(manager_id) from employees;
--null값은 count가 안됨
select emp_name,manager_id from employees;
--sum 총합
select sum(salary) from employees;
--avg:평균 - 6461
select avg(salary) as avg_sal from employees;
--min: 최소값 max: 최대값
select min(salary),max(salary) from employees;
--avg 평균보다 높은 사람 6461보다 높은 사람
select emp_name, salary from employees where salary > 6461 order by salary; 
select emp_name, salary from employees where salary > (select avg(salary) as avg_sal from employees);
-- min(salary)는 그룹함수여서 emp_name이랑 같이 값을 낼 수 없음
select min(salary) from employees;

--그룹함수 sum, avg, count(), count(*), min, max 임 / emp_name 같이 쓰고 싶으면 group by 써야됨

--최소월급을 받는 사람의 사번, 이름을 출력
select employee_id, emp_name,salary from employees where salary = (select min(salary) from employees);

--최대 월급받는 사람 출력
select employee_id, emp_name, salary from employees where salary = (select max(salary) from employees);
--부서번호가 50번인 사원만 전체 월급
select department_id, salary from employees;
--그룹함수를 쓰고 where는 조건절로 쓸 수는 있다.
select sum(salary) from employees where department_id= 50;

select count(*) from stu_score_cdate;
--stu_score_cdate에서 kor점수가 80점 이상인 학생 출력
select * from stu_score_cdate;
select no,name,kor from stu_score_cdate where kor>=80;
--국어점수 평균 이상, 영어점수에서 영어점수 평균이상인 학생을 출력
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

--1000자리에다가 데이터평균값 넣음
insert into s_info values(
stu_seq.nextval,(select count(*) from stu_score_cdate 
where kor >= (select avg(kor) from stu_score_cdate) and eng >= (select avg(eng) from stu_score_cdate)));

select * from s_info;

--월급이 최대인 사람과 최소인 사람과 평균인 사람을 출력
select * from employees;

select emp_name,salary from employees 
where salary=(select max(salary) from employees) or salary = (select min(salary) from employees) or salary <= (select avg(salary) from employees) order by salary;

--촤대값
select emp_name, salary from employees where salary = (select max(salary) from employees);

--평균값보다 낮은 사원 중에 최대값을 출력하시오
--1.평균값보다 낮은 사원을 검색
select emp_name, salary from employees where salary <= (select avg(salary) from employees);
--2.1번에서 최대값을 검색
select emp_name, salary from employees where salary = 6400;
-- 평균값보다 낮은 사원 중에서 그나마 제일 높은 salary를 받는 사원
select emp_name,salary from employees where salary = (select max(salary) from employees where salary <= (select avg(salary) from employees));

-- 문자함수
--lpad / rpad 자릿수 만들 때
select emp_name,lpad(emp_name,15,'#') from employees;
select emp_name, rpad(emp_name,20,'@') from employees;
--엘 trim (do 잘라내기)
select emp_name,ltrim(emp_name,'Do') from employees;

--ko20240001
select 'ko20240001',ltrim('ko20240001','ko2024') from dual;
--substr(데이터, 순서, 갯수)3번째에서 4개를 자르는 것
select emp_name, substr(emp_name, 3,4) from employees;

-- job_id에 있는 SH와 사번번호를 결합해서 출력하세요
select *from employees;
select substr(job_id,0,2)||employee_id from employees;.
select employee_id||substr(job_id,0,2) from employees;

--length
select emp_name,length(emp_name) from employees
where length(emp_name)>15;

--날짜함수
--날짜와 숫자는 더하기 빼기 가능
select sysdate+1 from dual;
select sysdate-hire_date from employees;
--날짜끼리 빼는 건 가능한데 더하기는 안됨
select sysdate + hire_date from employees;
--반올림 올려서 일자가 올라감(4월25일)
select round(sysdate,'month')from dual;
--4월
select trunc(sysdate,'month')from dual;

select round(sysdate,'year') from dual;
--개월 수 더하기
select add_months(sysdate,3) from dual;
--개월 수 빼기
select add_months(sysdate,-3)from dual;
--ceil올림, floor 버림 mod 나머지 poswer 제곱
select ceil(-4.2) from dual;
select floor(-4.2) from dual;
select mod(8,3) from dual;
select power(2,10)from dual;

--사원 이름이랑 입사날짜 출력
select * from employees;
select emp_name||to_char(hire_date,' yyyy"년"mm"월"dd"일" day') from employees;
select concat(emp_name,hire_date) from employees;

-- 사원명,월급*1400 앞에 원화표시와 쉼표를 넣으시오 (빈 공백을 0으로 채우고 싶을 때는 0으로 입력)
select emp_name, to_char(salary*1400,'L999,999,999') from employees; 

--자신의 생일과 자신의 생일이 속한 달의 마지막 날짜
-- '2010-10-10'이 생일이라고 가정
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;
-- --------------------------------------------------------------------------------------------------
-- 컬럼추가, 수정, 삭제
select * from member;
--table 타입보기
desc member;
-- DDL(data definition language)- column 추가
-- commit rollback이 없음 바로 저장됨
alter table member add gender varchar2(6) default 'female' not null;

--컬럼수정 - 컬럼이름변경, 타입변경
alter table member rename column name to stu_name; 

--컬럼 타입변경
alter table member modify(stu_name varchar2(50));
-- -----------------------------------------------
update member set stu_name = '홍';
--기존의 데이터가 변경하려는 크기보다 작을 경우에 가능
alter table member modify(stu_name varchar2(6));

--컬럼의 타입을 변경하려면 컬럼데이터가 빈 공백이거나 null일 때 가능
update member set stu_name = '';
alter table member modify(stu_name number(4));
-- ------------------------------------------------------------

alter table member modify(stu_name number(100));

--컬럼삭제
alter table member drop column phone;

update member set gender = 'male';
commit;






