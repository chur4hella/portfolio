var body = document.querySelector('body'),
  contentFilter = body.querySelector('.main-content-filter'),
  btnCloseFilter = contentFilter.querySelector('.filter__btn-close'),
  btnFilterActivation = body.querySelector('.filter-activation-btn');


function filterActivation() {
  contentFilter.classList.add('main-content-filter--active');
  body.classList.add('body--fixed');
}

btnFilterActivation.addEventListener('click', filterActivation);

function closeFilter() {
  contentFilter.classList.remove('main-content-filter--active');
  body.classList.remove('body--fixed');
}

btnCloseFilter.addEventListener('click', closeFilter);
