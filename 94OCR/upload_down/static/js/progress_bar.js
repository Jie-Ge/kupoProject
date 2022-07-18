
function upload_progress_bar() {
    function set_progress_rate(n, total) {
        //设置进度
        var rate = (n / total * 100).toFixed(2);
        if (n === total){
            $(".upload-progress-bar").text("完成!");
            $(".upload-progress-bar").css('display','none');

        }
        else if (n > 0) {
            $(".upload-progress-bar").attr("aria-valuenow", n);
            $(".upload-progress-bar").attr("aria-valuemax", total);
            $(".upload-progress-bar").text(rate + "%");
            $(".upload-progress-bar").css("width", rate + "%");
        }
    }

    var interval = setInterval(function () {
        //每1秒请求一次进度
        $.ajax({
            url: "http://127.0.0.1:8080/upload_progress/",
            type: "GET",
            success: function (response) {
                response = JSON.parse(response)
                console.log(response);
                var n = response["file_order"];
                var total = response["total_files"];
                if (n===0 || n === null || total===0 || total===null){
                    clearInterval(interval)
                }else if (n < total){
                    set_progress_rate(n, total);
                }else if (n === total){
                     set_progress_rate(n, total);
                     clearInterval(interval);
                }
            }
        });
    }, 1000);
}

module.exports = {
    upload_progress_bar
};
