person = 'CREATE TABLE person(user_id int not null , first_name varchar(50), last_name varchar(50),PRIMARY KEY(user_id))'

books_1 = 'create table book (book_id int not null primary key, title varchar(100), book_author varchar(100),author_id int,genre varchar(100))'

authors = 'create table author (author_id int not null primary key,name varchar(50),book_id int,FOREIGN KEY(book_id) REFERENCES book(book_id))'

genre = 'create table genre (genre_id int not null primary key, genre_type varchar(100)) '

user_book = 'create table user_book (usrbook_id int not null primary key,user_id int,book_id int, foreign key(user_id) references person(user_id),foreign key(book_id) references book(book_id))'

book_genre = 'create table book_genre (book_gen_id int not null primary key ,book_id int, genre_id int,foreign key(book_id) references book(book_id),foreign key (genre_id) references genre(genre_id))'

insert_user = [[707, 'tokyo', 'lisbon'],
               [708, 'luffy', 'monkey'],
               [709, 'eren', 'yeager'],
               [710, 'nami', 'berholdt'],
               [722, 'Kate', 'waver']]

insert_books_1 = [[332, 'Capitol murder', 'judith erwin', 661, 'mystery'],
                  [333, 'Think and grow rich', 'Napoleon HIll', 664, 'self-help'],
                  [334, 'the Dragon Blood', 'lindsay', 666, 'fiction'],
                  [335, 'A game of thrones', 'george martin', 667, 'thriller'],
                  [554, 'SAPIENS', 'Yualnoal harari', 669, 'Non-fiction'],
                  [434, 'IKigai', 'Hector garcia', 778, 'self-help'],
                  [437, 'A thousand splendid suns', 'Khaled Hosseini', 887, 'novel'],
                  [455, 'Jaya', ' Devdutt Pattanaik', 889, 'mythology']]

insert_authors = [[661, 'judith erwin', 332],
                  [664, 'Napoleon HIll', 333],
                  [666, 'lindsay', 334],
                  [667, 'george martin', 335],
                  [669, 'Yualnoal harari', 554],
                  [778, 'Hector garcia', 434],
                  [887, 'Khaled hosseni', 437],
                  [889, 'Devdutt Pattanaik', 455]]

insert_genre = [[40, 'mystery'],
                [43, 'self-help'],
                [44, 'fiction'],
                [45, 'thriller'],
                [46, 'non-fiction'],
                [47, 'novel'],
                [48, 'mythology']]

insert_usrbook = [[50, 707, 332],
                  [51, 708, 333],
                  [54, 709, 334],
                  [58, 707, 335]]

insert_book_genre = [[22, 332, 40],
                     [23, 333, 43],
                     [24, 334, 44],
                     [25, 335, 45],
                     [26, 554, 46],
                     [27, 434, 43],
                     [28, 437, 47],
                     [29, 455, 48]]
