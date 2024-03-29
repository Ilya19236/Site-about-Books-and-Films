USE BooksAndFilms
GO

Create procedure [dbo].[GetUsers] as
select * from [User]

GO

Create procedure [dbo].[UpdateUser]
@Id int,
@Name nvarchar(50),
@Surname nvarchar(50),
@Age int
as
update [User]
set Name = @Name, Surname = @Surname, Age = @Age
where Id = @Id

GO

Create procedure [dbo].[AddValuesInUser]
@Name nvarchar(50),
@Surname nvarchar(50),
@Age int
as 
insert into [User] (Name, Surname, Age)
Values (@Name, @Surname, @Age)

GO

Create procedure [dbo].[DeleteUser]
@Id int
as
delete from [User]
where Id = @Id

