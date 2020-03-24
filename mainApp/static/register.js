document.addEventListener('DOMContentLoaded', () => {
    console.log("Hi there")
    const t1 = document.querySelector('#team1')
    const t2 = document.querySelector('#team2')

    t1.style.display = "none"
    t2.style.display = "none"

    document.addEventListener('click',event => {

        if (event.target.id === "teamSize"){
            loadTemplate()
        }
    }
    document.addEventListener('click'. event => {
        if (event.target.id === "submit"){
            destruction()
        }
    })
    );


    function loadTemplate(){

        const size = document.querySelector('#teamSize').value

        if (size === 1){
            t1.style.display = "none"
            t2.style.display = "none"
        }
        else if(size === 2){
            t1.style.display = "block"
            t2.style.display = "none"
        }
        else if(size === 3){
            t1.style.display = "block"
            t2.style.display = "block"
        }
    }
    function destruction(){
        t1.parentNode.removeChild(t1)
        t2.parentNode.removeChild(t2)
    }
});

