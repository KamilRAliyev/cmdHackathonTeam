const navbar = document.querySelector("#navbarSupportedContent");
const navbar_items = navbar.children[0];
for(let item of navbar_items.children){
    item.addEventListener('click',function(){
        for(let disableactiveitem of navbar_items.children){
            disableactiveitem.classList.remove("active");
        }
        this.classList.add('active');
    })
}