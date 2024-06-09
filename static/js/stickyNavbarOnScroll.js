var lastScrollTop = 0;
        window.addEventListener('scroll', function() {
            var navbar = document.getElementById('sticky-navbar');
            var navbarHeight = navbar.offsetHeight;

            
            var churchNavBlock = document.querySelector('.church_navigation_block');
            var churchNavBlockPosition = churchNavBlock.getBoundingClientRect().top + window.scrollY;

            var scrollTop = window.scrollY || window.pageYOffset;

            if (scrollTop > lastScrollTop) {
                
                if (scrollTop >= churchNavBlockPosition) {
                    navbar.classList.add('fixed');
                    churchNavBlock.classList.add('placeholder');
                }
            } else {
                
                if (scrollTop <= churchNavBlockPosition) {
                    navbar.classList.remove('fixed');
                    churchNavBlock.classList.remove('placeholder');
                }
            }
            lastScrollTop = scrollTop;
        });