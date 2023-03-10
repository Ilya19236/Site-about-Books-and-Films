USE BooksAndFilms

GO

Create procedure [dbo].[GetUnits] as
select Un.Name, Un.AgeRate, Un.Description, TOU.Name from Unit as Un
inner join TypeOfUnit as TOU on Un.TypeId = TOU.Id 

GO

Create procedure [dbo].[GetUnitsByUser]
@Id int,
@Type int
as
select Us.Name, Us.Surname as S, Us.Age as A, Un.Name, TOU.Name as Type from [User] as Us
inner join User_Unit as U_U on Us.Id = U_U.UserId and Us.Id = @Id
inner join Unit as Un on U_U.UnitId = Un.Id
inner join TypeOfUnit as TOU on TOU.Id = Un.TypeId and Un.TypeId = @Type
group by Us.Name, Us.Surname, Us.Age, Un.Name, TOU.Name

GO

Create procedure [dbo].[GetUnitsByUsers]
@Type int
as
select Us.Name, Us.Surname as S, Us.Age as A, Un.Name, TOU.Name as Type from [User] as Us
inner join User_Unit as U_U on Us.Id = U_U.UserId 
inner join Unit as Un on U_U.UnitId = Un.Id
inner join TypeOfUnit as TOU on TOU.Id = Un.TypeId and Un.TypeId = @Type
group by Us.Name, Us.Surname, Us.Age, Un.Name, TOU.Name
GO

Create procedure [dbo].[GetUnitsAndTitles] as
select Un.Name, Un.Description, T.Name, T.Surname, TOT.Name  from Unit as Un 
inner join Unit_Author as U_A on Un.Id = U_A.UnitId
inner join Title as T on T.Id = U_A.AuthorrId
inner join Title_TypeOfTitle as T_T on T_T.TitleId = T.Id
inner join TypeOfTitle as TOT on TOT.Id = T_T.TypeOfTitleId
group by Un.Name, Un.Description, T.Name, T.Surname, TOT.Name

GO

Create procedure [dbo].[GetPopularityOfUnit]
@Id int
as
select Un.Name, Count (Us.Name) as People from unit as Un
inner join User_Unit as U_U on Un.Id = U_U.UnitId and Un.Id = @Id
inner join [User] as Us on U_U.UserId = Us.Id
Group by Un.Name

GO

Create procedure [dbo].[GetPopularityOfUnits] as
select Un.Name, Count (Us.Name) as People from unit as Un
inner join User_Unit as U_U on Un.Id = U_U.UnitId 
inner join [User] as Us on U_U.UserId = Us.Id
Group by Un.Name 

GO

Create procedure [dbo].[FullInformationAboutUnits] as
select Un.Name, Un.Description, TOU.Name as Type, G.Name as Genre, T.Name, T.Surname, TOT.Name  from Unit as Un
inner join TypeOfUnit as TOU on TOU.Id = Un.TypeId
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId
inner join Genre as G on U_G.GenreId = G.Id
inner join Unit_Author as U_A on Un.Id = U_A.UnitId
inner join Title as T on T.Id = U_A.AuthorrId
inner join Title_TypeOfTitle as T_T on T_T.TitleId = T.Id
inner join TypeOfTitle as TOT on TOT.Id = T_T.TypeOfTitleId

GO

Create procedure [dbo].[FullInformationAboutUnit]
@Id int
as
select Un.Name, Un.Description, TOU.Name as Type, G.Name as Genre, T.Name, T.Surname, TOT.Name  from Unit as Un 
inner join TypeOfUnit as TOU on TOU.Id = Un.TypeId and Un.Id = @Id
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId
inner join Genre as G on U_G.GenreId = G.Id
inner join Unit_Author as U_A on Un.Id = U_A.UnitId
inner join Title as T on T.Id = U_A.AuthorrId
inner join Title_TypeOfTitle as T_T on T_T.TitleId = T.Id
inner join TypeOfTitle as TOT on TOT.Id = T_T.TypeOfTitleId

GO

Create procedure [dbo].[AddValuesInUnit]
@Name nvarchar(50),
@AgeRate int,
@Description nvarchar(500),
@TypeId int
as 
insert into Unit (Name, AgeRate, Description, TypeId)
Values (@Name, @AgeRate, @Description, @TypeId)

GO

create procedure UpdateUnit
@Id int, 
@Name nvarchar(50),
@AgeRate bit,
@Description nvarchar(500),
@TypeId int as
UPDATE [Unit]
set [Name] = @Name, [AgeRate] = @AgeRate, [Description] = @Description, [TypeId] = @TypeId
where [Id] = @Id

GO

Create procedure [dbo].[DeleteUnit]
@Id int
as
delete from Unit
where Id = @Id

GO

Create procedure [dbo].[DeleteTypeOfUnit]
@Id int
as
delete from TypeOfUnit
where Id = @Id

