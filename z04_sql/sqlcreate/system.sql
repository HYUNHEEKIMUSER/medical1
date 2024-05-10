
create table stu_score (
 no number,
 name varchar2(30),
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(5,2),
 rank number
);
insert into stu_score values (
1,'홍길동',100,100,100,300,100,1
);
insert into stu_score values (
5,'김구',100,100,100,300,100,1
);
commit;
select * from stu_score;

--산술연산자 number타입인 경우
select * from stu_score;

insert into stu_score values(
6,'김유신', 100,95,96,(100+95+96),(100+95+96)/3,1
);

select * from stu_score;

insert into stu_score values(
7,'홍길자',100,100,99,(100+100+99),(100+100+99)/3,1
);

select * from stu_score;
--번호, 이름, 국어점수, 국어점수의 -20점, 평균, 국어점수-20점을 한 평균점수
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score; 







