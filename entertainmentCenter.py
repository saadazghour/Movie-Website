import MovieWebsite
import fresh_tomatoes
import webbrowser


Toy_Story = MovieWebsite.Movie("Toy_Story","A Story of A Best Movie"
	,r"https://www.google	.com/imgres?imgurl=http%3A%2F%2Fyesofcorsa.com%2Fwp-content%2Fuploads%2F2017%2F02%2FToy-Story-Photo.jpg&imgrefurl=http%3A%2F%2Fyesofcorsa.com%2Ftoy-story%2F&docid=JgdrHqxr9kgWOM&tbnid=KZz5h8OlN_slRM%3A&vet=10ahUKEwiCy_mIhvnbAhVBpCwKHbgUD2cQMwgvKAAwAA..i&w=1024&h=768&bih=532&biw=1024&q=%22toy%20story%20image%20jpg%22&ved=0ahUKEwiCy_mIhvnbAhVBpCwKHbgUD2cQMwgvKAAwAA&iact=mrc&uact=8",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")


Avatar = MovieWebsite.Movie("Avatar","A Story of A Best Movie"
	,r"https://i.ytimg.com/vi/sTLzV79t4wY/maxresdefault.jpg",
	"https://www.youtube.com/watch?v=4TZiMvJ65Wc")

#print (toy_Story.storyline)

Detective = MovieWebsite.Movie("True-Detective","A Story of A Best Movie"
	,r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1gzFqfbjV0igS1-FCpwEKy9rTyMN25covRw67h1i8JTdhmCJ9",
		"https://www.youtube.com/watch?v=5PSNL1qE6VY")

Pablo = MovieWebsite.Movie("Pablo Iscobar","A Story of A Best Movie"
	,r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1gzFqfbjV0igS1-FCpwEKy9rTyMN25covRw67h1i8JTdhmCJ9",
		"https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Favorit_Trailer = MovieWebsite.Movie("https://www.youtube.com/watch?v=4-KfT0-Zdu8")
# Favorit_Trailer.Showing_My_Best_Trailer()

movies = [Toy_Story,Avatar,Detective,Pablo]
#fresh_tomatoes.open_movies_page(movies)

#print MovieWebsite.Movie.VALID_RADING
#print MovieWebsite.Movie.__doc__
# print MovieWebsite.Movie.__module__
# print MovieWebsite.Movie.__name__

#print(avatar.storyline)
#avatar.show_Trailer()
#print Show_Trailer

#print 7**3
#print 7*7*7
