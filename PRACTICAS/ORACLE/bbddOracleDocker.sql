-- comentarios: con doble guion

/*
comentario varias lineas
las que sean
*/

select * from DEPT;
select APELLIDO,oficio from emp ;
select * from DEPT;
select APELLIDO,oficio from emp order by "APELLIDO" asc;
select * from emp order by "APELLIDO" desc ;

select * from emp where 'APELLIDO' <> 'tovar' ;

select * from emp where 'APELLIDO' = 'negro' ;
select * from EMP where DEPT_NO = 10;
select * from EMP ;
select * from EMP where oficio = 'ANALISTA' or oficio = 'DIRECTOR';

select * from EMP where DEPT_NO=10 or DEPT_NO=20 and OFICIO = 'DIRECTOR' order by DEPT_NO;
select * from EMP where OFICIO <> 'VENDEDOR' ;
select * from EMP where not OFICIO = 'VENDEDOR' ;--not prohibido -- 

select * from EMP where OFICIO <> 'VENDEDOR' and SALARIO BETWEEN 31800 and 39000 ;
select * from EMP where SALARIO >= 31800 and SALARIO <= 39000;

select * from EMP where DEPT_NO=10 or DEPT_NO=20 or DEPT_NO=30 or DEPT_NO=50 or DEPT_NO=88;
select * from EMP where DEPT_NO in (10,20,30,50,88);
select * from EMP where DEPT_NO not in (10,20,30);

select * from EMP where OFICIO like '%IRE%' or OFICIO like '%VENDE%';
select * from EMP where APELLIDO like 's%' ;
select * from EMP where APELLIDO like 's%a' ;
select * from EMP where APELLIDO like 's%_a' ;

select * from EMP where APELLIDO like '%a';
select DISTINCT OFICIO  from EMP  ;
select APELLIDO,(SALARIO + COMISION) as TOTALES from EMP;


--- select APELLIDO,(SALARIO + COMISION) as TOTALES from EMP order by TOTALES  where (SALARIO + COMISION) > 210000; ---

--- order by ordena respecto al cursor y where a partir de un campo de la tabla ---

select APELLIDO, OFICIO, SALARIO, COMISION ,(SALARIO + COMISION) as TOTALES from EMP where (SALARIO + COMISION)  > 100000;
select * from EMP order by DEPT_NO , OFICIO;

select * from EMP where FECHA_ALT > '1/1/70' order by emp_no ;


select * from plantilla where TURNO like 'N'; 

select * from DOCTOR ; --- where FUNCION =  ; ---

select APELLIDO,(SALARIO + COMISION) as TOTALES from EMP  where (SALARIO + COMISION) > 210000 order by TOTALES ;
select OFICIO,APELLIDO,(SALARIO + COMISION) as TOTALES from EMP  where (SALARIO + COMISION) > 210000 order by TOTALES ;
select OFICIO, APELLIDO,(SALARIO + COMISION) as TOTALES from EMP  where (SALARIO + COMISION) > 210000 order by TOTALES desc;

select  OFICIO, APELLIDO,(SALARIO + COMISION) as TOTALES from EMP  where (SALARIO + COMISION) > 210000 order by TOTALES desc;


SELECT COUNT(DOCTOR_NO) AS "NUMERO", ESPECIALIDAD FROM DOCTOR GROUP BY ESPECIALIDAD;
select count(*) as REGISTROS from EMP;
SELECT COUNT(DOCTOR_NO) AS "NUMERO", ESPECIALIDAD FROM DOCTOR WHERE ESPECIALIDAD='Pediatria' GROUP BY ESPECIALIDAD; --- columna que no esta en el select va en group by---

select count(*) as REGISTROS, oficio, dept_no, sum(SALARIO) from EMP group by oficio,dept_no;

select count(*) as REGISTROS, oficio, dept_no, sum(SALARIO) from EMP where OFICIO='DIRECTOR' group by oficio,dept_no;

select count(*) as REGISTROS, oficio, dept_no, sum(SALARIO) from EMP where OFICIO='DIRECTOR' group by oficio,dept_no HAVING dept_no>10;
select count(*) as REGISTROS, oficio, dept_no, sum(SALARIO) from EMP where OFICIO in ('DIRECTOR', 'ANALISTA') group by oficio,dept_no HAVING dept_no>10;


select count(*) as REGISTROS, oficio, dept_no, sum(SALARIO) from EMP where OFICIO in ('DIRECTOR', 'ANALISTA') group by oficio,dept_no HAVING count(*) > 1 ;


select * from emp where oficio in 'ANALISTA';
select count(*) as personas  from EMP where oficio = 'ANALISTA';

select avg(salario),oficio   from EMP where oficio = 'ANALISTA' group by oficio ;


select avg(salario),count(*) as contador from EMP where oficio = 'ANALISTA' group by oficio ;
select oficio,avg(salario),count(*) as contador from EMP  group by oficio HAVING oficio = 'ANALISTA' ;

select * from plantilla;
select count(*) as contador,funcion   from plantilla group by funcion;



select * from sala;
select   hospital_cod, avg(num_cama) as camas from sala group by hospital_cod;



select count(*) as contador,funcion   from plantilla group by funcion order by funcion asc ;

select * from emp;
select max(fecha_alt) AS FECHAMAXIMA, Oficio from emp group by oficio order by 1;

select * from enfermo;
select max(fecha_nac) AS FECHANACIMIENTO, sexo from enfermo group by sexo order by 1;

select * from plantilla;
select avg(salario) as media, count(*) as contador from emp ;
select max(fecha_nac) AS FECHANACIMIENTO, sexo from enfermo group by sexo order by 1;
select sum(salario) AS sumasalario, funcion  from plantilla group by funcion order by 1;
select * from emp;
select * from dept;
---combinacion--
select sum(salario) AS sumasalario, funcion  
from plantilla inner join avg(salario) as media, count(*) as contador from emp ;


select emp.apellido, emp.oficio
,dept.DNOMBRE
,dept.LOC
from emp
inner join dept
on emp.dept_no=dept.dept_no ;




select emp.apellido, emp.oficio
,dept.DNOMBRE
,dept.LOC
from emp
inner join dept
on emp.dept_no=dept.dept_no ;

select * from emp;


select emp.apellido, emp.oficio
,dept.DNOMBRE
,dept.LOC
from emp
inner join dept
on emp.dept_no=dept.dept_no ;



select count(*) as contadorPersonas ,dept.dnombre
from emp 
inner join dept
on emp.dept_no=dept.dept_no
group by dept.dnombre


select * from emp
select * from dept
select * from plantilla

select emp.oficio,emp.apellido,dept.dnombre
from emp  
inner join dept
on emp.dept_no=dept.dept_no
;
select * from hospital;
select * from plantilla;

select hospital.nombre,plantilla.hospital_cod
from hospital  
inner join plantilla
on plantilla.hospital_cod=hospital.hospital_cod
order by hospital.hospital_cod;



select * from dept;
select * from emp;
select distinct dept_no from emp;



select hospital.nombre,plantilla.hospital_cod
from hospital  
inner join plantilla
on plantilla.hospital_cod=hospital.hospital_cod
order by hospital.hospital_cod;


select hospital.nombre,plantilla.hospital_cod
from hospital  
left join plantilla
on plantilla.hospital_cod=hospital.hospital_cod
order by hospital.hospital_cod;


select hospital.nombre,plantilla.hospital_cod
from hospital  
right join plantilla
on plantilla.hospital_cod=hospital.hospital_cod
order by hospital.hospital_cod;


select hospital.nombre,plantilla.hospital_cod
from hospital  
cross join plantilla
on plantilla.hospital_cod=hospital.hospital_cod
order by hospital.hospital_cod;

--- insertamos a david sin departamento ---


select emp.oficio,emp.apellido,dept.dnombre
from emp  
inner join dept
on emp.dept_no=dept.dept_no


--muestra los empleados , aunque esten sin departamento 
select emp.oficio,emp.apellido,dept.dnombre,dept.loc
from emp  
left join dept
on emp.dept_no=dept.dept_no;


select emp.oficio,emp.apellido,dept.dnombre, dept.loc
from emp  
right join dept
on emp.dept_no=dept.dept_no


---muestra los dos ---
select emp.oficio,emp.apellido,dept.dnombre, dept.loc
from emp  
full join dept
on emp.dept_no=dept.dept_no

---cartesiano---
select emp.oficio,emp.apellido,dept.dnombre,dept.loc
from emp  
cross join dept
---on emp.dept_no=dept.dept_no---
select * from hospital

select hospital.hospital_cod, hospital.direccion, doctor.apellido, doctor.salario, doctor.especialidad
from doctor
inner join hospital
on doctor.hospital_cod=hospital.hospital_cod
where hospital.nombre = 'la paz';


select hospital.hospital_cod, hospital.direccion, doctor.apellido, doctor.salario, doctor.especialidad
from doctor
inner join hospital
on doctor.hospital_cod=hospital.hospital_cod
where hospital.nombre <> 'la paz';



select count(*) as numeroTrabajadores, dept.dnombre, emp.oficio
from dept
inner join emp
on dept.dept_no=emp.dept_no;
group by dept.dnombre;