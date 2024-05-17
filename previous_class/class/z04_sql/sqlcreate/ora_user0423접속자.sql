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

--hire_date로 오름차순 컬럼은 사원번호, 사원명, job_id-직급,입사일,월급 컬럼을 출력하세요
select * from employees;
select employee_id, emp_name, job_id, hire_date, salary from employees order by hire_date desc;

--급여를 적게 받는 순으로 출력하고 월급이 같으면 사원명으로 역순 정렬
select salary,emp_name from employees order by salary,emp_name desc;

--숫자함수
-- abs (from 에 아무 것도 없을 때 dual로 가상테이블 만들어 줌)
select -10, abs(-10) from dual;
-- floor() as f / round() as r : 별칭 써줌
select 34.789, floor(34.789) as f,round(34.789) as r from dual;
--round(대상, 자릿수) ex) round(34.178,2) 2자리까지 표시
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from students;
--as 별칭 변수명 바꿀 수 있음
select round(avg,2) as avg from students;
select round(avg,2) from students;
-- -1을 넣어서 정수부분 반올림
select 34.5678 ,round(34.5678,-1) from dual;
--trunc 지정한 자릿수 이하 버림
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;
--무조건 올림 (-1안됨)
select ceil(34.123) from dual;

--국어점수 일단위 절사해서 출력하시오
select * from students;
select trunc(kor,-1) as revised_kor from students order by kor;

--국어, 영어, 수학 점수를 일단위 절사하여 국어, 영어, 수학 합계를 출력하세요
select * from students;
select trunc(kor,-1) as revised_kor,trunc(eng,-1)as revised_eng,trunc(math,-1) as revised_math, (trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) as revised_total from students;
--mod 나머지계산
select round(100/7,2) from dual;
select mod(10,7) from dual;
select 10/7 from dual;

--사원번호가 짝수인 것을 출력하시오
--파이썬 employee_id%2 = 0
select employee_id from employees;
select employee_id from employees where mod(employee_id,2)=0;
--파이썬 10//7
select floor(10/7) from dual;
--나머지
select mod(10,7) from dual;

-- 학번이 3의 배수인 것만 출력하시오
select * from students;
select no, name from students where mod(no,3) = 0;

--시퀀스
-- 1씩증가, 1부터 시작, 최소값 1, 최대값 9999, 순환하지 않음, 캐시사용하지 않음
create sequence seq_no  increment by 1 start with 1 minvalue 1 maxvalue 9999  nocycle  nocache;
--nextval 시퀀스번호 1씩 증가
select seq_no.nextval from dual;
--currval 시퀀스 번호 확인
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
insert into member values(seq_mno.nextval,'eee','1111','김구','010-5555-5555');
select * from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;
--currval 현재 값 확인
select 's0001'||to_char(seq_mno.currval) from dual; 
--'00000' 자릿수 / nextval 증가
select 's'||to_char(seq_mno.nextval,'00000') from dual; 

--한국대학교 ko202400001 시퀀스 seq_kono 1-99999
create sequence seq_kono increment by 1 start with 1 minvalue 1 maxvalue 99999 nocycle nocache;
--trim 공백제거
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;
select '한국대학교 ko2024'||to_char(seq_mno.nextval,'00000') as "seq_kono" from dual;
--게시판
create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

--시퀀스 시작 1001 증감 10 최소값 1 최대값 99999
--5번실행을 해보세요 / seq_deptno
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
emp_seq.nextval, '이순신', sysdate
);

select * from emp01;
commit;

-- emp 테이블 자료를 입사일을 오름차순으로 정렬 하여 최근 입사한 직원을 먼저 출력하고 사원번호, 사원명 직급 입사일 칼럼을 출력하는 쿼리문
select* from employees;

select employee_id, emp_name, job_id, hire_date from employees order by hire_date desc; 
--현재까지 입사한 일수를 출력하세요
select employee_id, emp_name, job_id, hire_date,ceil(sysdate-hire_date)||'일' from employees order by hire_date desc; 

select emp_name from employees;

--직급과 사번을 합쳐서 출력하세요
select * from employees;
select job_id||employee_id from employees;
select substr(job_id,0,2) from employees;
select emp_name,substr(emp_name,1,3) from employees;
--문자열 자르기 함수(2번째 자리에서 3개 가져오기), substr(대상,시작위치,갯수)
select substr('abcde',2,3) from dual;

--job_id에서 앞에 2개 문자와 사번 5자리 00101자리를 만들어 함께 출력하시오
select job_id, employee_id from employees;
--내답
select substr(job_id,1,2)||substr('00'||employee_id,0,5) from employees;
--선생님 답
select substr(job_id,0,2)||trim(to_char(employee_id,'00000')) from employees;

--날짜함수
select sysdate from dual;
select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
--두 날짜 사이의 개월 수 확인
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;
--개월 수를 추가
select sysdate,add_months(sysdate,2) from dual;
--입력한 기준으로 다음 번 요일을 알려줌
select next_day(sysdate,'월요일') from dual;
--입력한 기준으로 그 달의 마지막 일을 알려줌
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;

















