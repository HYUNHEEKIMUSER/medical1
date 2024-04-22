select * from employees;

-- k_sal은 별칭임
select salary, salary *1400 as k_sal from employees;
select department_id from employees;

select nvl(department_id,0) from employees;

--변수가 너무 길어서 as 별칭을 넣으면 열에 제목이 생김 / ""로 넣어주면 소문자 지켜서 나옴/한글사용 가능 / ""는 있는 그대로 나옴
select salary, salary + (salary * nvl( commission_pct,0)) as "real_sal" from employees;

select * from departments;
select department_id, department_name from departments;

--여러 개의 데이터를 1개 합쳐서 넘겨야 할 경우 concat
-- concat(합치기)홍길동,유관순,이순신,김구,강감찬 / split(분리) -> split(",")

select * from stu_score;
--concat ||
select kor||','||eng||','||math as stu from stu_score;

select kor+eng+math as total,(kor+eng+math)/3 from stu_score;
--distinct: 중복이 제거 되어서 넘어옴 / where 별칭 is not null: null 제거함
select distinct department_id from employees where department_id is not null;

select manager_id from employees;
select distinct manager_id from employees;
select distinct manager_id from employees where manager_id is not null;

select * from employees;

select employee_id,salary from employees where employee_id = 200;
select employee_id, salary from employees where employee_id  = 200 or employee_id = 201 or employee_id =202;

select *from employees where employee_id >=200 and employee_id <=203;
select * from employees where employee_id >=150 or employee_id <=200;

--department_id 10,30,50에 해당되는 사원을 출력하시오
select employee_id, department_id from employees where department_id = 10 or department_id = 30 or department_id = 50;

-- 1)월급 6000-9000이하인 사원을 출력하세요
--order by 컬럼 asc(순차정렬), desc(역순) (order by salary asc / order by salary desc)
select * from employees;
select salary from employees where salary >= 6000 and salary <=9000 order by salary;
-- 2)월급이 6000,7000,8000인 사원
select salary from employees where salary =6000 or salary = 7000 or salary =8000;
-- 3)부서번호가 50번이면서 월급이 8000이상인 사원을 출력하세요
select * from employees;
select department_id, salary from employees where department_id = 50 and salary >=8000;
--stu_score에서 이름이 홍길동인 사람을 출력하세요
select * from stu_score where name ='홍길동';
--그 name 딱 하나만 나옴
select name from stu_score where name ='홍길동'; 

--역순 정렬
select hire_date from employees order by hire_date desc;

select emp_name,hire_date from employees where hire_date >='02/01/01' order by hire_date asc;

select hire_date,hire_date+100 from employees;
--round 반올림 현재 날짜에서 hire_date 빼기
select round( sysdate-hire_date,2) from employees;

select * from employees;
--concat 문자 합치기 
select emp_name||email from employees;

--입사일이 05년 이상 06년 이하이면서 월급이 6000달러 이상인 사원을 입사일 역순으로 출력하시오.
select * from employees;
select emp_name, hire_date, salary from employees where salary >=6000 and hire_date>='05/01/01' and hire_date<='06/12/31' order by hire_date desc;
--10번이 아닌 것만 출력 / not -> !=,<>,not
select department_id from employees where department_id !=10 and not department_id =50 order by department_id;

--5000이상 9000이하
select emp_name, salary from employees where salary >=5000 and salary <=9000 order by salary;

--평균이 99점 이상인 학생을 검색하세요
select * from stu_score;
select name, avg from stu_score where avg >=99 order by avg;

select * from students;
update students set name='이순신' where no=3;
commit;

--students
--국어 70점 이상 평균이 75점 이상인 학생을 출력하시오.
select name,kor,avg from students where kor >=70 and avg >=75 order by avg;

--국어점수 80점, 국어 70점 국어 90점인 학생을 출력하시오
select name, kor from students where kor =70 or kor = 80 or kor =90 order by kor;
--total과 avg 같이 바꾸기
update students set kor =100 where no=1;
rollback;
--업데이트 및 수정
update students set kor = 100, total =100+eng+math, avg = (100+eng+math)/3 where no=1;
select * from students where no=1;

-- 국어점수 80~90점 이상인 학생을 출력하세요
select name,kor from students where kor >= 80 and kor <=90 order by kor;
select kor from students where kor between 70 and 90;
--80에서 90점 빼고 a보다 크거나 b보다 작은 것
select kor from students where kor not between 70 and 90;
--날짜
select hire_date from employees order by hire_date;
--99년보다 크거나 같고 , 01보다 작거나 같은 사원 검색하기
select emp_name,hire_date from employees where hire_date between '99/01/01' and '01/12/31' order by hire_date;
select emp_name,hire_date from employees where hire_date >'99/01/01' and hire_date < '01/12/31';

--in 연산 동일한 필드를 여러 개 값으로.. kor = 80 kor = 70 kor  =90과 같은 말 
select name, kor from students where kor in(80,70,90);
select name, kor from students where kor not in(80,70,90);

--이름검색 (% : 무한대) 홍만 기억나고 잘 모를 때 '%홍%'이라는 것이 다 출력됨 ('%홍': 끝글자가 홍으로 끝나는 거 찾는 것)('홍%': 시작 글자가 홍으로 끝나는 거 찾는 것)
--%길%: 길이 포함되어 있는 단어 검색 
select * from students where name like '%홍%';
--순으로 끝난 이름을 검색하는 것
select * from students where name like '%순';

--  _: 한 칸의 공간을 사용 _:길 앞에 어떠한 단어가 있고 길은 중간에 그 다음 뒷 글자 모를 때
select * from students where name like '_길%';
--이름 세번 째 t가 들어가 있는 것
select name from students where name like '__t%';
--이름이 4자리인 3번째 r이 들어가 있는 이름
select name from students where name like '__r_';

select name from students where length(name) = 4;

select * from students where name like '__r%' and length(name)=4;

--이름이 A로 시작되는 것을 검색
select name from students where name like 'A%';

--이름에 a가 들어가 있는 학생 검색
select name from students where name like '%a%';
select name from students where name like '%A%';

--대소문자 구분없이 a가 들어가 있는 학생 검색
--소문자 취환(lower),대문자 취환(upper), 첫 글자만 대문자로 취환(initcap)
select no,name from students where lower(name) like '%a%'; 
--a가 포함 안된 이름
select no, name from students where lower(name) not like '%a%';

select * from employees;
select employee_id, emp_name, manager_id from employees where manager_id=100;
-- null은 등가비교가 안됨
select employee_id, emp_name, manager_id from employees where manager_id = null;
select employee_id,emp_name,manager_id from employees where manager_id is null;
select employee_id,emp_name,manager_id from employees where manager_id is not null;
--한글이름 역순도 가능
select * from stu_score order by name desc;
--1차 국어 점수로 역순 정렬을 한 다음에 같은 점수인 경우에는 영어점수로 순차정렬
select * from students;
select * from students order by kor desc, eng asc;

--total로 역순 정렬
select total from stu_score order by total desc;

--컬럼추가
alter table students add rank number(3);
desc students;
select * from students;
update students set rank =0;
commit;

--등수
select no,name, total,rank() over(order by total desc) as rank from students;

--수정
update students set rank = 13 where no =1;
update students s1 set s1.rank =13 where no=1; 

-- 수정2 (첫 번째 구문: update students s1) (두 번째 구문: select no no2, rank() over(order by total desc ) as ranks from students) -> 이중 쿼리
update students s1 set rank = (select ranks from (select no no2, rank() over(order by total desc ) as ranks from students) s2 where s1.no = s2.no2 );
select * from students;

-- 오후에 설명한 것
update students s1 set rank = 13 where no = 1;
update students set rank = 0;
--전체 중에서 국어 70점 이상을 찾는 것
select * from studenets where kor >=70;
-- avg 60점~100점에서 70점 이상을 찾는 것
select *from(select * from students where avg >=60) where kor >=70 ;

























