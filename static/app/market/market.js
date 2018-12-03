$(function () {
    $('#alltype').click(function () {
        console.log('alltype');
        //child class hidden and pick out
        $('#alltypecontainer').toggle();
        $('#adown').addClass('glyphicon-chevron-up').toggleClass('glyphicon-chevron-down')
        $('#sortcontainer').hide();
        $('#sdown').addClass('glyphicon-chevron-down')
    });

    $('#alltypecontainer').click(function () {
        $('#alltypecontainer').hide()
        $('#adown').addClass('glyphicon-chevron-down')

    });

    $('#allsort').click(function () {
        console.log('allsort');
        //child class hidden and pick out
        $('#sortcontainer').toggle();
        $('#sdown').addClass('glyphicon-chevron-up').toggleClass('glyphicon-chevron-down');
        $('#alltypecontainer').hide();
        $('#adown').addClass('glyphicon-chevron-down')
    });

    $('#sortcontainer').click(function () {
        $('#sortcontainer').hide()
        $('#sdown').addClass('glyphicon-chevron-down')
    })
});