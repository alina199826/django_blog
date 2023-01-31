    async function buttonClick(event) {
       myButton();

        let target = event.target;
        let url = target.dataset['indexLink'];
        let response = await fetch(url);


        if(response.ok) {

            console.log('200 ok');
        } else if (response.status === 400){
            console.log('400');
        }

        let index_text = await response.json();

        console.log(index_text);
    }

    async function onLoad(){
        let button = document.getElementById('button');
             if (button){
            button.onclick = buttonClick();


             }

        }


    window.addEventListener('load', onLoad )




function myButton(){

   document.querySelectorAll('.button').forEach(button => {
  button.addEventListener('click', e => {
    button.classList.toggle('liked');
    if (button.classList.contains('liked')) {
      gsap.fromTo(button, {
        '--hand-rotate': 8
      }, {
        ease: 'none',
        keyframes: [{
          '--hand-rotate': -45,
          duration: .16,
          ease: 'none'
        }, {
          '--hand-rotate': 15,
          duration: .12,
          ease: 'none'
        }, {
          '--hand-rotate': 0,
          duration: .2,
          ease: 'none',
          clearProps: true
        }]
      });
    }
  })
});}






