let links = document.querySelectorAll("[onclick^=addToList]");
links.forEach(element => {
    element.click();
});
window.open("https://usdb.animux.de/index.php?link=ziparchiv"); 