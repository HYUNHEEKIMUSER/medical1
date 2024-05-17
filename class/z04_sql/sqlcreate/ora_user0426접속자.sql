create table emp01(
emp_id number (6),
emp_name varchar2 (80),
hire_date date
);

update emp01 where hire_date date(500);

--테이블 구조 복사
desc employees;
select * from emp01;

--employees에 있는 모든 정보를 emp02 테이블에 넣기
create table emp02 as select * from employees;
select * from emp02;

--테이블 구조만 복사하기
create table emp03 as select * from employees where 1=2;
select * from emp03;

-- 테이블이 존재하면서 데이터만 복사하기 (3개 -> 14개)
insert into emp01(emp_id, emp_name, hire_date) select employee_id, emp_name hire_date from employees;

--1개 데이터 추가
insert into emp01 values(
207,'홍길동','2024-04-26'
);

--테이블이 구조가 같으면서 데이터만 복사 (구조만 같은 경우)
insert into emp03 select * from employees;

select * from emp03;
select * from emp01 order by emp_id desc;
select * from employees;

drop table m_date;
delete emp01 where emp_id=207;

-- -------------------------------------------------------------------------------------------
desc member;
--타입변경
alter table member modify(stu_name varchar2(30));

--컬럼삭제
alter table member drop column pw;
--컬럼 추가
alter table member add (pw varchar2(30));

select * from member;

insert into member values(
seq_mno.nextval,'fff','김유신','male','1111'
);

--컬럼순서 변경 
--1.stu_name 숨기기
alter table member modify stu_name invisible; 
alter table member modify gender invisible;

--뒷 쪽으로 자리 이동 이런 식으로 순서 변경 가능
alter table member modify stu_name visible; 
alter table member modify gender visible;

--invisible이랑 같음
--일시적인 사용제한
alter table member set unused(id);
select * from member;
--컬럼 사용 제한 해제
alter table member drop unused columns;

drop table emp03;

--테이블 이름 변경
rename emp01 to employees01;

desc employees;

--[무결성 제약조건]
--foreign key 다른 테이블에서 데이터 입력 시 선언되어 있는 기존 테이블에 입력하려는 데이터가 있는 지 확인 


create table member(
id varchar2 (30) primary key,
pw varchar2 (30) not null,
name varchar2(30), 
gender varchar2(6)
);

--이름에 제약 조건을 걸지 않아서 이름은 동일해도 들어감 id랑 pw만 제약 조건을 걸음
insert into member(id,pw,name) values(
'a','1111','홍길동'
);

select * from member;

--null 값만 제외
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
'5555','강감찬','공무원','05'
);

select * from emp02;

update emp02 set job = '수녀' where deptno = 2;

--unique: 중복만 제거
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp03 values(
1,'김구','3',3
);

select  * from emp03;

--1번 홍길동 검색하세요
select empno from emp03 where empno=1;
select * from emp03 where empno =1;

--null, 홍길동 검색
select * from emp03 where empno is null and ename = '홍길동'; 

-- null인 모든 사람 검색
select * from emp03 where empno is null;

--primary key로 컬럼 하나로 찾을 수 있는데 unique면 하나 더 검색을 해야될 수도 있다(primary key는 null도 안됨)
create table emp01(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);
--5개 null, 1,2,3,1
insert into emp01 values(
4, '김구', '교수', 04
);
select * from emp01;




-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- foreign key (외래키): 반드시 primary key가 있어야 됨
drop table emp01;

--emp01 테이블 생성
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

alter table emp01 modify(deptno number(6));
insert into emp01 values(
1,'홍길동','0001', 10
);

insert into emp01 values(
3,'유관순','0002',30
);

--foreign key 삭제
alter table emp01 drop constraint fk_deptno;

--foreign key 삭제 후 deptno에 없는 데이터를 추가로 입력할 수 있음.
insert into emp01 values(
5,'강감찬','0004',280
);


commit;
--emp01 foreign key 추가(fk_daptno 별칭)
--add constraint+별칭 / foreign key+현재컬럼/ references+다른테이블(컬럼이름)
alter table emp01 add constraint fk_deptno foreign key(deptno)
references dept01(deptno);

select * from emp01;





--dept01 테이블 생성
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
8, 'bbb', '게시글8','내용8'
);

commit;

select * from board;

alter table board add constraint fk_id foreign key(id) references member(id);

--comment 테이블 댓글테이블 
create table comments(
cno number(4) primary key, 
bno number(4), 
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno) 
references board(bno)
);
--댓글달기
insert into comments values(
5,2,'1111','댓글내용4'
);
--fk를 등록할 때 설정
--jk를 등록할 때 설정 부모의 foreign key로 등록되어 있는 모든 데이터를 삭제시키는 것
--kf키로 등록되어 있는 모든 데이터는 모두 존재 시키는 것.
delete board where bno = 5;

commit;
select * from board;
select * from comments;

--외래키 삭제
alter table board drop constraints fk_id;
alter table comments drop constraint fk_bno;

select * from board;
select * from comments;

delete comments where cno=2;
delete board where bno=1;

alter table board add constraints fk_id foreign key(id) references member(id);

--fk_cno가 삭제가 되도록 함. (update cascade: 부모키가 삭제되어도 살아있게 하는 거) (on delete cascade: 부모가 삭제되었으면 같이 삭제되는 것)
alter table comments add constraints fk_bno foreign key(bno) references comments(cno) on delete cascade;

--foreign key를 설정하면 삭제도 컨트롤 하고 새로운 내용을 입력을 못하게 제약을 걸 수 있음
--unique는 중복은 안되고 null은 가능
--check는 정해진 것만 들어가게 한 것

-- check 제약 조건 특정값의 범위, 특정값만 입력되도록 함. 
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', --컬럼에 데이터를 넣지 않으면 자동으로 0001이 저장됨
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in ('남자','여자'))
);
--에러 나는 예시
insert into emp(empno, ename, job, sal, gender) values(
3,'이순신','0004',5000,'남'
);
insert into emp(empno, ename, job, sal, gender) values(
5,'김구','0006',1000,'남자'
);

--job default - job 입력이 없으면 자동으로 0001로 설정됨
insert into emp(empno, ename, sal, gender) values(
6,'김유신',10000,'남자'
);

select * from emp;










