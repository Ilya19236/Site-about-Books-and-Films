create procedure IsChangeUserData
@Id int, 
@Name nvarchar(50),
@Surname nvarchar(50) as
UPDATE [User]
set [Name] = @Name, [Surname] = @Surname
where [Id] = @Id

GO

create procedure IsChangeUnitData
@Id int, 
@Name nvarchar(50),
@AgeRate bit,
@Description nvarchar(500),
@TypeId int as
UPDATE [Unit]
set [Name] = @Name, [AgeRate] = @AgeRate, [Description] = @Description, [TypeId] = @TypeId
where [Id] = @Id

GO

create procedure IsChangeTitleData
@Id int, 
@Name nvarchar(50),
@Surname nvarchar(50),
@Type int as
UPDATE [Title]
set [Name] = @Name, [Surname] = @Surname, [Type] = @Type
where [Id] = @Id

GO

create procedure IsChangeGenreData
@Id int, 
@Name nvarchar(50) as
UPDATE [Genre]
set [Name] = @Name
where [Id] = @Id

GO

