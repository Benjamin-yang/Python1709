$(function () {
    initTopSwiper();
    initSwiperMenu();


})

function initTopSwiper() {
    var swiper = Swiper('#topSwiper',{
        pagination:'.swiper-pagination',
        autoplay:5000,

    })
}

function initSwiperMenu() {
    var swiper = Swiper('#swiperMenu',{
        slidesPerView:3,


    })
}

