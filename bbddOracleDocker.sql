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



select count(*) as empleados
, dept.dnombre, emp.oficio
from dept
inner join emp
on dept.dept_no=emp.dept_no
group by dept.dnombre;

select count(emp.dept_no)
, dept.dnombre , emp.oficio
from dept
right join emp
on dept.dept_no=emp.dept_no
;


group by dept.dept_no ;



-- --

select count(hospital.nombre)
from hospital

select count(plantilla.nombre)
from plantilla

select count(sala.nombre)
from sala

-- apellido, fincion , nombre hospital y nombre de sala

select  sala.nombre, hospital.nombre , plantilla.funcion, plantilla.apellido 
from plantilla
inner join hospital
on plantilla.hospital_cod=hospital.hospital_cod
left join sala
on plantilla.hospital_cod=sala.hospital_cod
order by sala.nombre;


select sala_cod from plantilla



select  sala.nombre, hospital.nombre , plantilla.funcion, plantilla.apellido 
from plantilla
inner join hospital
on plantilla.hospital_cod=hospital.hospital_cod 
left join sala
on hospital.hospital_cod=sala.hospital_cod
and sala.sala_cod=plantilla.sala_cod
order by sala.nombre;



select max(emp.salario) as salarioMaximo
from emp 

select emp.apellido , emp.salarioMaximo
from emp
when salario = resultadosalarioMaximo




select * from EMP where salario=(select MAX(salario) from EMP); 

select * from EMP where OFICIO=(select OFICIO from emp where APELLIDO='sala');


select * from EMP where OFICIO=(select OFICIO from emp where APELLIDO='sala') and SALARIO > (select SALARIO from emp where APELLIDO='ford');


select * from EMP where OFICIO=(select OFICIO from emp where APELLIDO='sala') or (select OFICIO from emp where APELLIDO='jimenez'); -- falla por que le devuelven 2 valores

select * from EMP where OFICIO=(select OFICIO from emp where APELLIDO='sala' or APELLIDO='jimenez'); -- falla por que le devuelven 2 valores




select * from EMP where OFICIO in (select OFICIO from emp where APELLIDO='sala' or APELLIDO='jimenez');
select * from EMP where OFICIO  where APELLIDO='sala'


(select OFICIO from EMP where APELLIDO='sala')  union  (select OFICIO from emp where APELLIDO='jimenez')


select APELLIDO, SALARIO , OFICIO from emp;


select APELLIDO, SALARIO , ESPECIALIDAD from doctor;

select APELLIDO,OFICIO  ,SALARIO  from emp 
where SALARIO > 25000
union 
select APELLIDO,ESPECIALIDAD ,SALARIO  from DOCTOR 
where SALARIO > 25000
union 
select APELLIDO , FUNCION, SALARIO from  PLANTILLA
where SALARIO > 25000
order by APELLIDO
;

select APELLIDO,OFICIO  ,SALARIO  from emp 
union all
select APELLIDO,OFICIO  ,SALARIO  from emp 
order by APELLIDO;






select APELLIDO,OFICIO  ,SALARIO  from emp 
union 
select APELLIDO,ESPECIALIDAD ,SALARIO  from DOCTOR 
union 
select APELLIDO , FUNCION, SALARIO  from  PLANTILLA
where SALARIO > 25000
order by APELLIDO
;

select * from DOCTOR
--consulta sobre un cursor --

select * from (select APELLIDO,OFICIO  ,(SALARIO + COMISION) as SUELDO  from emp 
union 
select APELLIDO,ESPECIALIDAD ,SALARIO  from DOCTOR 
union 
select APELLIDO , FUNCION, SALARIO  from  PLANTILLA
order by APELLIDO
) ALIASC 
where  ALIASC.SUELDO >=  35000 and ALIASC.SUELDO >= 250000
order by OFICIO;

-- los campos calculados tienen que tener siempre un alias

select APELLIDO
,case TURNO
    when 'T' then 'Tarde' 
    when 'M' then 'Mañana'
    else 'Noche'
end as TEE
, (APELLIDO || ' trabaja como :' || FUNCION || ' turno :' || TURNO || '   :'  )
from plantilla


select * from emp


select  emp.oficio, emp.salario , dept.DNOMBRE, emp.APELLIDO
from  emp
inner join dept
on emp.DEPT_NO=dept.DEPT_NO;

select hospital.NOMBRE , sala.NOMBRE 
from hospital
inner join sala
on hospital.HOSPITAL_COD=sala.HOSPITAL_COD;



select hospital.NOMBRE , sala.NOMBRE 
from hospital
inner join sala
on hospital.HOSPITAL_COD=sala.HOSPITAL_COD;




select emp.APELLIDO, emp.EMP_NO -- , hospital.HOSPITAL_COD, hospital.NOMBRE
from emp
union
select hospital.NOMBRE, hospital.HOSPITAL_COD
from hospital
union
select 


select count(sala.SALA_COD) as numeroSalas, count(hospital.hospital_cod) as numeroHospitales
from sala
inner join hospital
on sala.hospital_cod=hospital.hospital_cod


select fecha_alt, emp.APELLIDO
from emp
where emp.fecha_alt >= '01/01/95' and emp.fecha_alt <= '01/01/99' 


select * from dept

insert into dept values(50, 'python', 'Getafe');
insert into dept (dept_no, dnombre) values (60, 'i+D')


select  max(EMPLEADO_NO) + 1 from plantilla; 

insert into plantilla(EMPLEADO_NO,APELLIDO,FUNCION,TURNO,HOSPITAL_COD)
values( (select MAX(EMPLEADO_NO) + 1 from plantilla), 'Super Lopez', 'ENFERMERA', 'T', 22);
select * from plantilla;

rollback;

commit;

-- borrar el ultimo introcucido 

delete from plantilla where EMPLEADO_NO=(select max(EMPLEADO_NO) from plantilla )


update  plantilla set SALA_COD=4, SALARIO=35000 where APELLIDO='Super Lopez';


update plantilla
set salario=salario+1
where FUNCION='INTERINO';

update plantilla set SALARIO=(
select SALARIO from plantilla where APELLIDO='karplus w.') where SALA_COD=4 

select * from plantilla

insert into plantilla(EMPLEADO_NO, APELLIDO, FUNCION, TURNO, HOSPITAL_COD ) 
values(
(select MAX(EMPLEADO_NO) + 1 from plantilla )
,'Cabrales'
,'ENFERMERA'
,'M'
,(select HOSPITAL_COD from HOSPITAL where NOMBRE='la paz2')
);


insert into plantilla(EMPLEADO_NO, APELLIDO, FUNCION, TURNO, HOSPITAL_COD ) 
values(
(select MAX(EMPLEADO_NO) + 1 from plantilla )
,'Barroso David'
,'ENFERMERO'
,'M'
,(select HOSPITAL_COD from HOSPITAL where NOMBRE='la paz2') || '54'
);

--elimina si no tiene hospital asignado o es nulo
DELETE FROM PLANTILLA where HOSPITAL_COD not in (select HOSPITAL_COD from HOSPITAL) or HOSPITAL_COD is null;


select * from plantilla;

INSERT INTO OCUPACION VALUES(59676,22,8,4);

select ESPECIALIDAD, HOSPITAL_COD
from doctor 
where ESPECIALIDAD = 'Cardiologia'

select HOSPITAL.NOMBRE, hospital.hospital_cod from HOSPITAL where HOSPITAL_COD in(select  DOCTOR.HOSPITAL_COD from DOCTOR)

select DOCTOR.APELLIDO ,DOCTOR.ESPECIALIDAD, DOCTOR.hospital_cod from DOCTOR where HOSPITAL_COD in(select  HOSPITAL.HOSPITAL_COD from HOSPITAL) 













-- José Escriche Barrera como programador perteneciente al departamento de producción.  Tendrá un salario base de 70000 pts/mes y no cobrará comisión. 



insert into emp(EMP_NO, APELLIDO, OFICIO, FECHA_ALT, SALARIO, COMISION, DEPT_NO ) 
values(
(select MAX(EMP_NO) + 1 from emp )
,'José Escriche Barrera'
,'PROGRAMADOR'
,'20-02-2025'
,70000
,0
,(select HOSPITAL_COD from HOSPITAL where NOMBRE='PROCUCCION') 
);


select * from dept



insert into DEPT(DEPT.DNOMBRE, DEPT.DEPT_NO, DEPT.LOC) 
values(
'DEPPRODUCCION'
,(select MAX(DEPT.DEPT_NO) + 1 from dept )
,'Fuenlabrada'
);


rollback

update DEPT
set loc='Barcelona'
where DNOMBRE='VENTAS';


select * from EMP

-- (ventas), se dan de alta dos empleados: Julián Romeral y Luis Alonso.  Su salario base es el menor que cobre un empleado, y cobrarán una comisión del 15% de dicho salario.
insert into EMP(EMP.APELLIDO, EMP.SALARIO, EMP.COMISION, EMP.EMP_NO) 
values(
'Julian Romeral'
,(select MIN(EMP.SALARIO)from EMP)
,(select MIN(EMP.SALARIO)from EMP) * 15 / 100
,(select MAX(EMP.EMP_NO) + 1 from EMP )
)
;

select * from emp

update EMP 
set SALARIO=(SALARIO + (SALARIO * 15 / 100))

rollback

--Incrementar un 5% el salario de los interinos de la plantilla que trabajen en el turno de noche.
update plantilla 
set SALARIO= (SALARIO + (select plantilla.SALARIO from plantilla where plantilla.FUNCION = 'INTERINO' AND plantilla.TURNO = 'N') * 5 / 100 )

--Incrementar en 5000 Pts. el salario de los empleados del departamento de ventas y del presidente, tomando en cuenta los que se dieron de alta antes que el presidente de la empresa.

update EMP 
set SALARIO=(SALARIO + 5000) 
where EMP.FECHA_ALT < (select EMP.FECHA_ALT  from EMP where EMP.OFICIO='PRESIDENTE');

--El empleado Sanchez ha pasado por la derecha a un compañero.  Debe cobrar de comisión 12.000 ptas más que el empleado Arroyo y su sueldo se ha incrementado un 10% respecto a su compañero.


update EMP 
set COMISION=(select EMP.COMISION from EMP where EMP.APELLIDO = 'arroyo') + 12000
,SALARIO=EMP.SALARIO + ((select EMP.SALARIO from EMP where EMP.APELLIDO = 'arroyo') * 10 / 100)
where EMP.APELLIDO='sanchez'