/**
 * Created by 鏇捐崳 on 2016/9/25.
 */

var artElement = "<div class='col-lg-4 col-md-3 col-sm-4'>" +
                    "<a href=''><img src='images/1.png' title='' alt=''></a>" +
                    "<div class='art-info'>"+
                        "<h4><a href=''>OrgChart缁勭粐鏋舵瀯鍥炬帶浠�</a></h4>" +
                        "<small>jQuery OrgChart 鏄竴涓敤鏉ョ粯鍒剁粍缁囩粨鏋勫浘鐨� jQuery 鎻掍欢銆� 鍙互鑷繁瀹氬姞杞借嚜宸辨兂瑕佺殑缁勭粐鏋舵瀯锛岄€氳繃json鐨勫舰寮�</small>" +
                    "</div>" +
                    "<div class='art-fields'>" +
                        "<i class='fa fa-list-ul'></i>&nbsp;<span>jQuery鎻掍欢</span>" +
                    "</div>" +
                    "<div class='art-stars'>" +
                        "<i class='fa fa-eye'></i> <span class='eye'>&nbsp;105</span>" +
                        "<i class='fa fa-heart'></i> <span class='star'>&nbsp;105</span> " +
                        "<div class='art-author'>" +
                            "<a href='' data-toggle='tooltip' data-placement='top' data-original-title='绗ㄧ鐔婂枩娆㈠悆楗煎共' data-container='#article'><i class='fa fa-user-secret'></i> </a>" +
                        "</div>" +
                    "</div>" +
                 "</div>";



$('#view-more').click(function (){
    $(this).html('鍔犺浇涓�...');
    // $(this).attr('disabled', true);
    for(var i = 0; i < 2; i++){
        $('#art').append(artElement);
    }
});





