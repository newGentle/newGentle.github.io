'use strict';

const coll = document.querySelectorAll('.collapsible');

coll.forEach((item) => {
    
    item.addEventListener('click', () => {
        const content = document.querySelector('.' + item.classList.item(0) + '-content');
        const allActives = document.querySelectorAll('.active')
        
        allActives.forEach((i) => {
            if (i.classList.item(0) != item.classList.item(0) + '-content') {
                i.classList.remove('active');
            }
        });

        content.classList.toggle('active');
    })
})
