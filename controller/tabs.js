document.addEventListener('DOMContentLoaded', function() {
    const tabLinks = document.querySelectorAll('.tabs ul li');
    const tabContents = document.querySelectorAll('.tab-content');
  
    tabLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        const target = this.getAttribute('data-tab');
  
        tabLinks.forEach(function(link) {
          link.classList.remove('active');
        });
  
        tabContents.forEach(function(content) {
          content.style.display = 'none';
        });
  
        this.classList.add('active');
        document.getElementById(target).style.display = 'block';
      });
    });
  });
  