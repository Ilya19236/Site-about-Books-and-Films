USE BooksAndFilms
GO

Create procedure [dbo].[GetGenreByUser]
@Id int,
@Genre int
as
select Us.Name, Us.Surname as S, Us.Age as A, G.Name from [User] as Us
inner join User_Unit as U_U on Us.Id = U_U.UserId and Us.Id = @Id
inner join Unit as Un on U_U.UnitId = Un.Id
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId
inner join Genre as G on G.Id = U_G.GenreId and G.Id = @Genre
group by Us.Name, Us.Surname, Us.Age, G.Name

GO

Create procedure [dbo].[GetGenres] as
select * from Genre

GO

Create procedure [dbo].[GetGenreByUsers]
@Genre int
as
select Us.Name, Us.Surname as S, Us.Age as A, G.Name from [User] as Us
inner join User_Unit as U_U on Us.Id = U_U.UserId 
inner join Unit as Un on U_U.UnitId = Un.Id
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId
inner join Genre as G on G.Id = U_G.GenreId and G.Id = @Genre
group by Us.Name, Us.Surname, Us.Age, G.Name

GO

Create procedure [dbo].[GetUsersAndGenre]
as
select Us.Name, Us.Surname as S, Us.Age as A, G.Name from [User] as Us
inner join User_Unit as U_U on Us.Id = U_U.UserId 
inner join Unit as Un on U_U.UnitId = Un.Id
inner join Unit_Genre as U_G on Un.Id = U_G.UnitId
inner join Genre as G on G.Id = U_G.GenreId
group by Us.Name, Us.Surname, Us.Age, G.Name

GO

create procedure UpdateGenre
@Id int, 
@Name nvarchar(50) as
UPDATE [Genre]
set [Name] = @Name
where [Id] = @Id


GO

Create procedure [dbo].[DeleteGenre]
@Id int
as
delete from Genre
where Id = @Id

GO

Create procedure [dbo].[AddValuesInGenre] 
@Name nvarchar(50)
as 
insert into Genre (Name)
Values (@Name)

GO