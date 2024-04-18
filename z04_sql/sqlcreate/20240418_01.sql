--테이블 생성
create table stu_score(
    no number(4) primary key,
    name varchar2(30),
    kor number(3),
    eng number(3),
    math number(3),
    total number(3),
    avg number(6)
);

--1개 데이터 입력: insert
insert into stu_score (no,name,kor,eng,math,total,avg) values(
 1,'홍길동',58,99,95,(58+99+95),(58+99+95)/3
);

--데이터 검색: select
select * from stu_score;

-- 완전한 저장(수정하려면 commit을 하고 수정을 해야됨)
commit;

-- 1개 데이터 수정: update
update stu_score set name='홍길자' where no=1;

--수정 후 다시 확인
select * from stu_score;

--맨 처음 꺼로 다시 되돌리기
rollback;

--테이블 구조보기
desc stu_score;

--삭제: delete (no=1만 삭제할 때)(drop은 전체적으로 삭제)
delete stu_score where no=1;

--삭제 후 데이터 확인
select * from stu_score;

--삭제 후 완전히 사라지게 저장
commit;

--복구안됨
drop table stu_score;



