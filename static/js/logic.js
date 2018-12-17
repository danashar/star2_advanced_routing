 $.ajax({
    type: "GET",
    url: "http://localhost:7000/get_all",
    }).done(function (data) {

    var title = document.createElement("h2");
    title.innerHTML = ("jpost articles");
    document.body.appendChild(title);

    var article_list = document.createElement("ul")
    document.body.appendChild(article_list);

    var articles = JSON.parse(data);
    console.log(JSON.parse(data))
    articles.forEach(function(element) {
        var article_item = document.createElement("li")
        var article = document.createElement("a");
        article.href = element['link'];
        article.innerHTML = element['title'];


        $('ul').append($("<li/>").html(article));
     });
});
