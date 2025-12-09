



  const searchForm = document.getElementById('searchForm');
  // if search bar not empty
  if (searchForm) {                   
    searchForm.addEventListener('submit', () => {
      const grouped = document.getElementById('groupedView');
      if (grouped) grouped.style.display = 'none';
    });
  }