var body = document.querySelector('body'),
  regionBox = body.querySelector('.regions'),
  regionSelect = regionBox.querySelector('.regions-title__select'),
  regionSelectText = regionBox.querySelector('.regions-title__selected'),
  popupRegion = regionBox.querySelector('.regions-popup'),
  popupRegionItems = popupRegion.querySelectorAll('.regions-list__item');


function activationRegionPopup(e){
  e.stopPropagation();
  popupRegion.classList.toggle('regions-popup_active');
}

regionSelect.addEventListener('click', activationRegionPopup);

function closeRegionPopup(){
  popupRegion.classList.remove('regions-popup_active');
}

body.addEventListener('click', closeRegionPopup);

function setRegion(){
  if (!this.classList.contains('regions-list__item_active')){
    popupRegion.querySelector('.regions-list__item_active').classList.remove('regions-list__item_active');
    this.classList.add('regions-list__item_active');
    regionSelectText.innerHTML = this.querySelector('.regions-list__region').innerHTML;
    popupRegion.classList.remove('regions-popup_active');
  }
}

popupRegionItems.forEach(function (item, i, arr) {
  item.addEventListener('click', setRegion);
});

