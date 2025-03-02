let users = ["Giorgi Janelidze", "nino Beridze", "Luka Maisuradze", "ana Kalandadze", "Davit Giorgadze"];

users = users.filter(user => user[0] === user[0].toUpperCase());

console.log(users);
