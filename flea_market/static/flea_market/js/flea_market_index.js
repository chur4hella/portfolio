var categories = document.querySelectorAll('.category');


function activationCategory(){
    if(this.classList.contains('category--active')){
      this.classList.remove('category--active');
    } else {
      categories.forEach(function (item, i, arr) {
        if(item.classList.contains('category--active')){
          item.classList.remove('category--active');
          return;
        }
      });
      this.classList.add('category--active')
    }
}

categories.forEach(function (item, i, arr) {
  item.addEventListener('click', activationCategory);
});
