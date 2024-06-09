document.addEventListener('DOMContentLoaded', function() {
           
    var selectElement = document.querySelector('.location-select');

   
    var languageValueItems = document.querySelectorAll('.language_value ul li');

    
    selectElement.addEventListener('change', function() {
       
        var selectedValue = selectElement.value;

       
        languageValueItems.forEach(function(item) {
            item.style.display = 'none';
        });

        
        var selectedLanguageItem = document.querySelector('.' + selectedValue);
        if (selectedLanguageItem) {
            selectedLanguageItem.style.display = 'block';
        }
    });
});