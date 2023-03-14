USE [DATABASE]
GO 
 
Create procedure [dbo].[GetUnitsAndTitles] as 
select Un.Name, Un.Description, T.Name, T.Surname, TOT.Name  from Unit as Un  
inner join Unit_Author as U_A on Un.Id = U_A.UnitId 
inner join Title as T on T.Id = U_A.AuthorrId 
inner join Title_TypeOfTitle as T_T on T_T.TitleIdd = T.Id 
inner join TypeOfTitle as TOT on TOT.Id = T_T.TypeOfTitleId 
group by Un.Name, Un.Description, T.Name, T.Surname, TOT.Name 
 
GO  
 
create procedure GetTitle as 
select * from Title 
 
Go 
 
Create procedure [dbo].[GetUsersAndTitles] 
as 
select Us.Name, Us.Surname as S, Us.Age as A, T.Name, T.Surname, TOT.Name from [User] as Us 
inner join User_Unit as U_U on Us.Id = U_U.UserId 
inner join Unit as Un on U_U.UnitId = Un.Id 
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId 
inner join Unit_Author as U_A on Un.Id = U_A.UnitId 
inner join Title as T on U_A.AuthorrId = T.Id 
inner join Title_TypeOfTitle as T_T on T.Id = T_T.TitleIdd 
inner join TypeOfTitle as TOT on T_T.TypeOfTitleId = TOT.Id 
group by Us.Name, Us.Surname, Us.Age, Un.Name, Un.Description, T.Name, T.Surname, TOT.Name 
 
GO 
 
Create procedure [dbo].[GetTitlesByUsers] 
@TypeOfTitle int  
as 
select Us.Name, Us.Surname as S, Us.Age as A, T.Name, T.Surname, TOT.Name from [User] as Us 
inner join User_Unit as U_U on Us.Id = U_U.UserId  
inner join Unit as Un on U_U.UnitId = Un.Id 
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId 
inner join Unit_Author as U_A on Un.Id = U_A.UnitId 
inner join Title as T on U_A.AuthorrId = T.Id 
inner join Title_TypeOfTitle as T_T on T.Id = T_T.TitleIdd 
inner join TypeOfTitle as TOT on T_T.TypeOfTitleId = TOT.Id and TOT.Id = @TypeOfTitle 
group by Us.Name, Us.Surname, Us.Age, Un.Name, Un.Description, T.Name, T.Surname, TOT.Name 
 
GO 
 
Create procedure [dbo].[GetTitlesByUser] 
@Id int, 
@TypeOfTitle int 
as 
select Us.Name, Us.Surname as S, Us.Age as A, T.Name, T.Surname, TOT.Name from [User] as Us 
inner join User_Unit as U_U on Us.Id = U_U.UserId and Us.Id = @Id 
inner join Unit as Un on U_U.UnitId = Un.Id 
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId 
inner join Unit_Author as U_A on Un.Id = U_A.UnitId 
inner join Title as T on U_A.AuthorrId = T.Id 
inner join Title_TypeOfTitle as T_T on T.Id = T_T.TitleIdd 
inner join TypeOfTitle as TOT on T_T.TypeOfTitleId = TOT.Id and TOT.Id = @TypeOfTitle 
group by Us.Name, Us.Surname, Us.Age, Un.Name, Un.Description, T.Name, T.Surname, TOT.Name 
 
GO 
 
Create procedure [dbo].[GetTitlesByUnits] 
@Type int 
as 
select Un.Name, Un.Description, T.Name, T.Surname, TOT.Name  from Unit as Un  
inner join Unit_Author as U_A on Un.Id = U_A.UnitId 
inner join Title as T on T.Id = U_A.AuthorrId 
inner join Title_TypeOfTitle as T_T on T_T.TitleIdd = T.Id 
inner join TypeOfTitle as TOT on TOT.Id = T_T.TypeOfTitleId and TOT.Id = @Type 
group by Un.Name, Un.Description, T.Name, T.Surname, TOT.Name 
 
 
GO 
 
Create procedure [dbo].[GetTitlesByUnit] 
@Id int, 
@Type int 
as 
select Un.Name, Un.Description, T.Name, T.Surname, TOT.Name  from Unit as Un  
inner join Unit_Author as U_A on Un.Id = U_A.UnitId and Un.Id = @Id 
inner join Title as T on T.Id = U_A.AuthorrId 
inner join Title_TypeOfTitle as T_T on T_T.TitleIdd = T.Id 
inner join TypeOfTitle as TOT on TOT.Id = T_T.TypeOfTitleId and TOT.Id = @Type 
group by Un.Name, Un.Description, T.Name, T.Surname, TOT.Name 
 
GO 
 
Create procedure [dbo].[AddValuesInTitle] 
@Name nvarchar(50), 
@Surname nvarchar(50) 
as  
insert into Title(Name, Surname) 
Values (@Name, @Surname) 

GO

create procedure UpdateTitle
@Id int, 
@Name nvarchar(50),
@Surname nvarchar(50),
@Type int as
UPDATE [Title]
set [Name] = @Name, [Surname] = @Surname, [Type] = @Type
where [Id] = @Id

GO 
 
Create procedure [dbo].[DeleteTitle] 
@Id int 
as 
delete from Title 
where Id = @Id 
 
GO 
 
Create procedure [dbo].[DeleteTypeOfTitle] 
@Id int 
as 
delete from TypeOfTitle 
where Id = @Id 
 