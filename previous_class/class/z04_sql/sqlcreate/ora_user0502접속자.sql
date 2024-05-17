-- 2개 테이블 : department_id로 연결
select * from employees;
select * from departments;

select employee_id, emp_name, a.department_id, department_name from employees a, departments b where a.department_id = b.department_id;

select * from stu_score_cdat
e;
select * from students;
update stu_score_cdate set name ='김구' where no = 168;
commit;
--홍길동에 있는 학생성적의 모든 내용과 전화번호 , 이메일, 과,학년
select * from stu_score_cdate where name = '홍길동';
select id, a.name, phone, email, major, grade, kor, eng, math, total, avg, rank, c_date 
from  stu_score_cdate a, students b where a.name = '홍길동' and a.name= b.name;

select count(*) from stu_score_cdate;

--컬럼추가
alter table students add no number(38);

insert into students(no) select no from stu_score_cdate;
update students b set no = a.num() from (select rownum rnum, id from students) a where b.id = a.id;
--rownum 만들어진 번호를 no에 넣기
update students b set no = (select rnum from(select rownum rnum, id from students)a) 
where a.id=b.id ;
--equi join
--2개의 테이블을 join할 때 한 개의 동일한 컬럼이 있어야 함. 
--1개의 동일한 컬럼은 중복이 없어야 함. 2개 중에 한 테이블에서는 primary key가 사용 되어야 함.
select a.id, a.name, phone, total,avg from students a, stu_score b where a.id=b.id order by name;

--self join 동일한 테이블 2개를 가지고 서로 join
select a.employee_id,a.emp_name, a.department_id, a.job_id, a.manager_id,b.emp_name  from employees a, employees b 
where a.manager_id = b.employee_id order by a.department_id;

select * from students;

select * from stu_score;
-- 컬럼 자리가 비었을 때 테이블 다른 컬럼 덮어 씌우기
--2.b의 rank가 0이어서 숫자 넣을 것
update stu_score a set rank = (select  ranks from(select no, id, rank() over(order by total desc)as ranks,rank,total from stu_score)b 
where a.no = b.no); 
--1.rank
select  ranks from(select no, id, rank() over(order by total desc)as ranks,rank,total from stu_score) b;
select no, id, rank() over(order by total desc)as ranks,rank,total from stu_score;

select * from students;
select * from member;
alter table member add no number;
select rownum,id from member;
-- ----------------------------------------------------------------------------------------------
--no가 null이어서 숫자 넣는 것
--1.
update member a set no=()b where a.id=b.id;
--2.
select rownum rnum, id from member;
select rnum from(select rownum rnum, id from member);
--3.
update member a set no = (select rnum from(select rownum rnum,id from member) b where a.id=b.id);
-- -------------------------------------------------------------------------------------------------
update stu_score set rank = 0;
commit;
select total,rank from stu_score order by total desc;
-- rank 붙이기
select total, rank() over(order by total desc) ranks from stu_score;
--rownum 임의로 순서
select row_number() over(order by total desc) rnum, total from stu_score;

-- stu_score에 rank 순위를 모두 업데이트
select * from stu_score;
select total, rank()over(order by total desc) ranks from stu_score where no=no;
update stu_score a set rank = (select ranks from (select no, rank()over(order by total desc) ranks from stu_score)b where a.no=b.no);
-- row_number()over()
select * from stu_score;



-- 1~10번
select rownum rnum, a.* from (select * from stu_score order by total desc)a where rownum >=1 and rownum <=10;
--11번~20번 위의 방법으로 안됨. 아래의 방법으로
select * from (select rownum rnum, a.* from (select * from stu_score order by total desc)a) where rnum >=11 and rnum <=20;
--repeat 다시 한번 위의 문장과 동일
select * from
(select rownum rnum,a.* from( select * from stu_score order by total desc ) a)where rnum>=11 and rnum<=20;
--혹은
select * from (select row_number() over(order by total desc) rnum,a.* from stu_score a)where rnum>=11 and rnum<=20;


select employee_id, emp_name, manager_id from employees order by employee_id;

--self join manager_id, 이름 출력 null 값 제외가 됨
select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a, employees b where a.manager_id = b.employee_id;
--null값포함 outer join / null 값이 있는 반대편 항목에 (+)추가(b.emp_name)
select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a, employees b where a.manager_id = b.employee_id(+);

select manager_id , emp_name from employees where emp_name = 'Diana Lorentz';

-- equi join ,outer join , employees 테이블 부서번호 10~110 (null값도 같이 출력하고 싶을 때)
select emp_name, b.department_id, department_name from employees a, departments b where a.department_id(+) = b.department_id order by department_id;
--10~270번까지
select department_id from departments;

--ansi join (employees * departments 값)
select * from employees cross join departments;
select * from employees, departments;
--equi join
select a.department_id, department_name from employees a, departments b where a.department_id = b.department_id;
--ansi join(위의 equi join과 같음)
select a.department_id, department_name from employees a inner join departments b on a.department_id = b.department_id; 
--위의 문장과 다른 버전(ansi inner join (using 사용법))
select department_id, department_name from employees join departments using (department_id);


select a.*, b.* from employees a, departments b where a.department_id = b.department_id;

desc employees;

--ansi outer join -> left outer join, right outer join, full outer join
select a.emp_name, a.manager_id, b.emp_name from employees a left outer join employees b on a.manager_id = b.employee_id;
-- 위 아래 문장 같음 ->그러나 full outer join 불가능/ 기본sql 가능
select a.emp_name, a.manager_id, b.emp_name from employees a, employees b where a.manager_id = b.employee_id;
