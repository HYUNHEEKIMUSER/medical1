
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
1,'ȫ�浿',100,100,100,300,100,1
);
insert into stu_score values (
5,'�豸',100,100,100,300,100,1
);
commit;
select * from stu_score;

--��������� numberŸ���� ���
select * from stu_score;

insert into stu_score values(
6,'������', 100,95,96,(100+95+96),(100+95+96)/3,1
);

select * from stu_score;

insert into stu_score values(
7,'ȫ����',100,100,99,(100+100+99),(100+100+99)/3,1
);

select * from stu_score;
--��ȣ, �̸�, ��������, ���������� -20��, ���, ��������-20���� �� �������
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score; 







