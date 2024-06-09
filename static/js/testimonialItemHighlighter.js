document.addEventListener("DOMContentLoaded", function() {
    const testimonialItems = document.querySelectorAll('.ch_testimonial_item');

    testimonialItems.forEach(item => {
        item.addEventListener('click', function() {
            
            testimonialItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active'); 
            const saintId = this.querySelector('.saint-image').dataset.id;
            console.log('Clicked on saint with ID:', saintId);
            
        });
    });
});