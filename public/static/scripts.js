if (document.title == "MaksDesign - Tworzenie Stron WWW i Grafik") {
    document.querySelectorAll('#kontakt').forEach(function(element) {
        element.addEventListener('click', (e)=> {
            e.preventDefault();
            let y = document.querySelector(".contact").getBoundingClientRect().top + window.scrollY - document.querySelector("header").offsetHeight;
            window.scrollTo({top: y, behavior: 'smooth'});
        });
    });
    document.querySelectorAll('#omnie').forEach(function(element) {
        element.addEventListener('click', (e)=> {
            e.preventDefault();
            let y = document.querySelector(".why-us").getBoundingClientRect().top + window.scrollY - document.querySelector("header").offsetHeight;
            window.scrollTo({top: y, behavior: 'smooth'});
        });
    });
    document.querySelectorAll('#projekty').forEach(function(element) {
        element.addEventListener('click', (e)=> {
            e.preventDefault();
            let y = document.querySelector(".projects").getBoundingClientRect().top + window.scrollY - document.querySelector("header").offsetHeight;
            window.scrollTo({top: y, behavior: 'smooth'});
        });
    });
}