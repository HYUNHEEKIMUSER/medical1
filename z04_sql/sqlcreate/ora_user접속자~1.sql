--가지고 있는 모든 테이블 검색
select * from tab;

--f5는 전체실행(실행키 f9은 한 행만 실행됨, 테이블형태로 보임)
select * from employees;

--테이블 구조 확인
desc employees;

--테이블 생성 (5,2) 총 숫자는 5자리이고 2는 소수점
create table stu_score (
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2)
);

insert into stu_score(no,kor,eng,avg) values(
1,100,99,(100+99)/2
);

insert into stu_score values(
1,99,98,(95+98)/2
);

insert into stu_score values(
    1,80,70.223,(80+70.223)/2
);

select * from stu_score;

commit;

create table num (
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);
-- commit 후 실행 다시 하려면??

-- 날짜 확인(/) 기본형태
-- dual은 가상테이블
select sysdate from dual;

-- 날짜 확인(-) to_char는 형변환 -> 포맷변경 -> 포맷을 지정
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
-- 시간만 나오게 하는 것
select to_char(sysdate, 'hh:mi:ss') from dual;

-- 날짜 계산도 해줌 (+100일)
select sysdate+100 from dual;
select sysdate+1000 from dual;

-- 1월1일부터 얼마나 날짜가 지났는 지
select sysdate - to_date('24/01/01') from dual;





