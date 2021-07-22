$(document).ready(function() {
    $('#demo1').owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        margin: 10,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,

            },
            600: {
                items: 3,

            },
            1000: {
                items: 3,
            }
        }
    })
});
$(document).ready(function() {
    $('#demo').owlCarousel({
        loop: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,

            },
            600: {
                items: 3,

            },
            1000: {
                items: 3,
            }
        }
    })
});
$(document).ready(function() {
    $('#demo2').owlCarousel({
        loop: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,

            },
            600: {
                items: 3,

            },
            1000: {
                items: 5,
            }
        }
    })
});



// ========Filter Hospital======================================================================

window.onload = function() {
    var stateSelect = document.getElementById('stateSelect')
    var citySelect = document.getElementById('citySelect')
    var facilitySelect = document.getElementById('facilitySelect')
    var form = document.getElementById('filterForm')

    var formSubmit = function() {
        form.submit()
    }
    stateSelect.onchange = formSubmit
    citySelect.onchange = formSubmit
    facilitySelect.onchange = formSubmit
}