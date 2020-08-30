function fnOn() {
    $.ajax({
        type: "GET",
        url: "/on",
        success: function () {
            window.alert("成功！！");
        },
        error: function () {
            window.alert("失敗！！");
        }
    });
}

function fnOff() {
    $.ajax({
        type: "GET",
        url: "/off",
        success: function () {
            window.alert("成功！！");
        },
        error: function () {
            window.alert("失敗！！");
        }
    });
}
