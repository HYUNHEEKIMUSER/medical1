select * from stu_score_cdate;
select * from member;
select * from board;

select a.*,name from board a, member b where a.id=b.id ;
select bno, a.id,name,btitle, bcontent, bdate,bgroup, bstep, bindent, bhit, bfile 
from board a, member b where a.id=b.id;

select no, name, total, avg, case when avg>=90 then 'A' 
when avg >=80 then 'B' when avg >=70 then 'C' else 'F' end as grade from stu_score_cdate; 

select*from employees;
select round(avg(salary),2) from employees;

select employee_id, emp_name, salary, nvl(salary+(salary*commission_pct),0), to_char(salary*1410,'L999,999,999')as korean from employees ;

select department_id, round(avg(salary),2), max(salary), min(salary) from employees where department_id is not null group by department_id order by department_id;

select * from stu_score;

select no, name from stu_score where name like '%홍%';

select name, round(avg,2) from stu_score_cdate;

select round(avg,1) from stu_score_cdate where avg >=60 order by no;
select round(avg,1) from stu_score_cdate where avg <60 order by no;

--사원번호 사원명 부서번호 부서명 을 출력하세요
select * from employees;
--join
select employee_id,emp_name,a.department_id, department_name from employees a, departments b where a.department_id=b.department_id;
-- 이름 두 번째 자리에 a가 들어가는 사원을 검색하시오
select emp_name from employees where emp_name like '_a%';

select employee_id,emp_name,a.department_id, department_name from employees a, departments b where a.department_id=b.department_id and emp_name like '_a%' and
salary >=(select avg(salary) from employees);

--월급이 평균 이상인 사람만 검색
select employee_id, emp_name, a.department_id, salary from employees a, departments b where salary>=(select avg(salary) from employees);

select * from employees;

select * from jobs;
--사원번호 사원명 부서번호 부서명 직급번호 직급명 출력
select employee_id, emp_name, a.department_id, department_name, d.job_id from employees a, departments b ,jobs d where a.department_id=b.department_id and a.job_id=d.job_id;
--선생님 답
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title from employees a, departments b, jobs c where a.department_id =b.department_id and a.job_id=c.job_id;

--사원번호, 사원명 ,월급 ,최소월급분, 직급, 직급타이블 출력 
select * from jobs;
select employee_id, emp_name, salary, min_salary, a.job_id, job_title from employees a, jobs b where a.job_id=b.job_id;

--최소월급의 인상에 몇 % 이상을 받고 있는 지 출력(최소월급 / 현재월급 *100)
select employee_id, emp_name, salary, min_salary,to_char(round(((salary-min_salary)/salary)*100,2))||'%',a.job_id,job_title from employees a, jobs b where a.job_id=b.job_id;
--job title manager 글자가 들어가 있는 사원의 사원번호, 사원명, 직급번호, 직급명, 월급, 최대 월급을 출력하시오
select a.job_id,emp_name,employee_id, job_title, salary, max_salary from employees a, jobs b where a.job_id=b.job_id and job_title like '%Manager%';

select a.user_id,user_name,user_phone,user_address1, user_address2, user_address3 from  Delivey_address a User b where a.user_id = b.user_id;

create table stu_grade (
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'F', 0,59
);
commit;

-- 둘 다 같은 컬럼이 없음
select * from stu_grade;
select * from stu_score;

--case when then  grade 컬럼을 만들어 90점 이상 A 80점 이상 B ... 학점출력
--non-equi join: 같은 컬럼이 없는데 join하는 것
select no, name, avg, grade from stu_score_cdate, stu_grade where avg between low_score and high_score order by no; 

update stu_grade set high_score = 62 where grade='F';
update stu_grade set low_score = 62, high_score=71 where grade='D';
commit;


-- 월별 매출액을 기준으로 고객등급

-- 지역별 대출 합계
select * from kor_loan_status;
select region, gubun , sum(loan_jan_amt) from kor_loan_status group by region, gubun order by region;
--부서별 월급 합계를 출력
select department_id, sum(salary) as a from employees group by department_id order by a; 

--연도별, 지역별, 대출 합계 금액
select substr(period,1,4), 
region, loan_jan_amt from kor_loan_status order by substr(period,1,4), region;

select substr(period,1,4), region, sum(loan_jan_amt) from kor_loan_status group by substr(period,1,4), region order by region;

-- 시간대별, 연령대별 판매량 총합을 출력하시오
select * from lotte_product;
select time_cd, age_cd, sum(purh_amt) as a from lotte_product group by time_cd, age_cd order by a desc;

select * from shop_product;
select * from shop_product where pdate >= '2024/03/01';
drop table shop_product;

--2024년 3월 이후 이름별 금액 합계 출력
select name,sum(amount) as a from shop_product where pdate>='2024/03/01' group by name;

--customer_rank 테이블 생성 
--rank 
--100만원 미만 bronze 200만원 미만 silver 300만원 미만 gold 300만원 이상 platinum
-- name, sum(amount) rank 출력하세요 non-equi join
drop table customer_rank;
create table customer_rank(
rank varchar2(38),
lower_amount number(38),
high_amount number(38)
);

insert into customer_rank values(
'platinum',3000000,9999999
);

select * from customer_rank;
select * from shop_product;
--customer_rank 테이블 생성 
--rank 
--100만원 미만 bronze 200만원 미만 silver 300만원 미만 gold 300만원 이상 platinum
-- name, sum(amount) rank 출력하세요 non-equi join
select name, s_amount, rank from (select name, sum(amount) as s_amount from shop_product  where pdate >= '2024/03/01'
group by name),customer_rank where s_amount between lower_amount and high_amount;

-- non-equi join
select no,name,avg,grade from stu_score,stu_grade
where avg between low_score and high_score
order by no
;
--순번을 새롭게 부여해서 출력해주는 함수
--rownum, row_number
select* from lotte_product order by std_ym ;
select rownum, std_ym, sex_cd, age_cd, time_cd, purh_amt from lotte_product;

select rownum, a.* from lotte_product a where rownum <=10;

select * from stu_score_cdate order by no;
select* from stu_score_cdate where no <=10 order by no;

select rnum, std_ym, sex_cd, age_cd, time_cd, purh_amt from(select rownum rnum,a.* from lotte_product a) b where rnum >=21 and rnum <=30;

select rownum, b.* from (select * from lotte_product order by std_ym ) b;
--kor 점수가 높은 순으로 21~30등까지 출력하시오
--순번 21,22....30번 부여
select * from stu_score_cdate order by no;
select rnum, no,name,kor,eng,math,total,avg,rank,c_date from (select rownum rnum, b.* from(select a.* from stu_score_cdate a order by kor desc ) b) 
where rnum >=21 and rnum>=30;











