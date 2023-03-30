'use strict';

const coll = document.querySelectorAll('.collapsible');

coll.forEach((item) => {
    
    item.addEventListener('click', () => {
        const content = document.querySelector('.' + item.classList.item(0) + '-content');
        const allActives = document.querySelectorAll('.active')
        
        allActives.forEach((i) => {
            if (i.classList.item(0) != item.classList.item(0) + '-content') {
                i.classList.remove('active');
                coll.forEach(el => {
                    if (el.classList.item(0) != item.classList.item(0)) {
                        el.classList.remove('opened')
                    }});
            }
        });


        item.classList.toggle('opened');
        content.classList.toggle('active');
    })
})
