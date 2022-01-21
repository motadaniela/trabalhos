var i = 0
const carrinho =[]

create_button()

function create_button() {
    for (let i = 0; i < document.getElementById("main").children[1].childElementCount; i++) {
        let article = document.getElementById("main").children[1].children[i];
        let btn = document.createElement("button");
        btn.id = "carrinho" + 0;
        btn.innerHTML = "Add Carrinho"
        btn.addEventListener("click", function () {
            let carrinho = document.getElementById("dropdown-content");
            let link = document.createElement("a");
            let img = document.createElement("img");
            let p = document.createElement("p");
            p.innerHTML = article.children[1].innerHTML;
            img.src = article.children[0].firstChild.src;
            //link = article.children[];
            link.append(img);
            link.append(p);
            carrinho.append(link);
        });
        article.append(btn);
    }
}

function adicionarItem(Item){
    for (let i = 0; i < carrinho.length; i+= 1){
        if (carrinho[i].item === item){
            cart[i].qty += 1
        
        }
    }
}

function removeItem(item){
    for(let i = 0; i < carrinho.length; i+=1){
        bttn.id = "Remover" + 0
        bttn.innerHTML = "Remover"
        if(carrinho[i].item === item){
            carrinho.splice(i, 1)
        return
        }
    }
}