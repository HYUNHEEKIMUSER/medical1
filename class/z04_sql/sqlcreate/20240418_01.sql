--���̺� ����
create table stu_score(
    no number(4) primary key,
    name varchar2(30),
    kor number(3),
    eng number(3),
    math number(3),
    total number(3),
    avg number(6)
);

--1�� ������ �Է�: insert
insert into stu_score (no,name,kor,eng,math,total,avg) values(
 1,'ȫ�浿',58,99,95,(58+99+95),(58+99+95)/3
);

--������ �˻�: select
select * from stu_score;

-- ������ ����(�����Ϸ��� commit�� �ϰ� ������ �ؾߵ�)
commit;

-- 1�� ������ ����: update
update stu_score set name='ȫ����' where no=1;

--���� �� �ٽ� Ȯ��
select * from stu_score;

--�� ó�� ���� �ٽ� �ǵ�����
rollback;

--���̺� ��������
desc stu_score;

--����: delete (no=1�� ������ ��)(drop�� ��ü������ ����)
delete stu_score where no=1;

--���� �� ������ Ȯ��
select * from stu_score;

--���� �� ������ ������� ����
commit;

--�����ȵ�
drop table stu_score;



