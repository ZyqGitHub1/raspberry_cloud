jQuery.fn.shake = function(intShakes, intDistance, intDuration) {
    this.each(function() {
        $(this).css({
            position: 'relative',
        });
        for (var i = 1; i <= intShakes; i++) {
            $(this).animate({
                left: (intDistance * -1)
            }, (((intDuration / intShakes) / 4))).animate({
                left: intDistance
            }, ((intDuration / intShakes) / 2)).animate({
                left: 0
            }, (((intDuration / intShakes) / 4)));
        }
    });
    return this;
};
