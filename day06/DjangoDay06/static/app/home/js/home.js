$(function () {
    initTopSwiper();
})

function initTopSwiper() {
    var swiper = Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        autoplay: 5000,
    })
}
