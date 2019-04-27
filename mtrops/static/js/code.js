////////////////////////////项目管理/////////////////////////////////

//添加项目
$("#sub-project").click(function(){
    var project_name = $("#project-name").val();
    var project_msg = $("#project-msg").val();

    $.post('/code/addproject/',{'project_name':project_name,'project_msg':project_msg},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        alert(data);

        if (data == "添加成功"){
            location.reload();
        }
        }
    })
});



//编辑项目信息填充内容
$('td a[name="edit-project"]').click(function(){
    var project_id = $(this).attr("project_id");
    $.post("/code/editproject/",{'project_id':project_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        var info = eval('(' + data + ')');
        $("#edit-project-name").val(info.project_name);
        $("#edit-project-msg").val(info.project_msg);
        $("#sub-edit-project").attr('project_id',info.project_id);
        $("#edit-projectModal").modal('show');
        }
    })
});



//修改项目
$("#sub-edit-project").click(function(){
    var project_name = $("#edit-project-name").val();
    var project_msg = $("#edit-project-msg").val();
    var project_id = $(this).attr("project_id");
    $.post("/code/editproject/",{'action':'edit','project_name':project_name, 'project_msg':project_msg,'project_id':project_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        alert(data);
        if (data == "修改成功"){
            location.reload();
        }
    }
    })

});


//删除项目
$("td a[name='del-project']").click(function(){
   var project_id = $(this).attr('project_id');
   var statu = confirm("是否确认删除！");
   if (statu==true)
    {
    $.post("/code/delproject/",{'project_id':project_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        if (data == "已删除"){
            location.reload();
        }
    }
    })

    }
});


////////////////////////////站点管理////////////////////////////////


//添加站点
$("#sub-site").click(function(){
    var site_name = $("#site-name").val();
    var site_msg = $("#site-msg").val();
    var site_project = $("#site-project").val();
    var site_url = $("#site-url").val();
    var site_depend = $("#site-depend").val();
    var depend = JSON.stringify(site_depend);
    $.post('/code/addsite/',{'site_name':site_name,'site_msg':site_msg,'site_project':site_project,'site_url':site_url,'site_depend':depend},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        alert(data);

        if (data == "添加成功"){
            location.reload();
        }
        }
    });
});


//编辑站点信息填充内容
$('td a[name="edit-site"]').click(function(){
    var site_id = $(this).attr("site_id");
    $.post("/code/editsite/",{'site_id':site_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        var info = eval('(' + data + ')');
        $("#edit-site-name").val(info.site_name);
        $("#edit-site-msg").val(info.site_msg);
        $("#edit-site-project").val(info.site_project);
        $("#edit-site-url").val(info.site_url);

        var arr = info.site_depend.split('/');

        var sel = document.getElementById("edit-site-depend");
        var len = sel.options.length;

        $("#edit-site-depend option").attr("selected", false);

        for (var i = 0; i < arr.length; i++) {
            $("#edit-site-depend option[value='" + arr[i] + "'] ").attr("selected", true);
        }

        $('#edit-site-depend').multiselect('rebuild');
        $('#edit-site-depend').multiselect('refresh');

        $("#sub-edit-site").attr('site_id',info.site_id);
        $("#edit-siteModal").modal('show');
        }
    })
});



//修改站点
$("#sub-edit-site").click(function(){
    var site_id = $(this).attr('site_id');
    var site_name = $("#edit-site-name").val();
    var site_msg = $("#edit-site-msg").val();
    var site_project = $("#edit-site-project").val();
    var site_url = $("#edit-site-url").val();
    var site_depend = $("#edit-site-depend").val();
    var depend = JSON.stringify(site_depend);
    $.post('/code/editsite/',{'action':'edit','site_name':site_name,'site_id':site_id,'site_msg':site_msg,'site_project':site_project,'site_url':site_url,'site_depend':depend},function(data){
     if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        alert(data);

        if (data == "修改成功"){
            location.reload();
        }
        }
    });
});




//删除站点
$("td a[name='del-site']").click(function(){
   var site_id = $(this).attr('site_id');
   var statu = confirm("是否确认删除！");
   if (statu==true)
    {
    $.post("/code/delsite/",{'site_id':site_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        if (data == "已删除"){
            location.reload();
        }
    }
    })

    }
});

////////////////环境部署//////////////////

//添加发布环境
$("#sub-depend").click(function(){
    var depend_name = $("#depend-name").val();
    var depend_version = $("#depend-version").val();


    var install_script = $("#install-script").val();
    $.post('/code/addepend/',{'depend_name':depend_name,'depend_version':depend_version,'install_script':install_script},function(data){
     if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        alert(data);
        if (data == "添加成功"){
            location.reload();
        }
        }
    });
});





//编辑依赖环境填充内容
$('td a[name="edit-depend"]').click(function(){
    var depend_id = $(this).attr("depend_id");
    $.post("/code/editdepend/",{'depend_id':depend_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        var info = eval('(' + data + ')');
        $("#edit-depend-name").val(info.depend_name);
        $("#edit-depend-version").val(info.depend_version);

        $("#edit-install-script").val(info.install_script);
        $("#sub-edit-depend").attr('depend_id',info.depend_id);
        $("#edit-dependModal").modal('show');
        }
    })
});



//修改依赖环境
$("#sub-edit-depend").click(function(){
    var depend_id = $(this).attr('depend_id');
    var depend_name = $("#edit-depend-name").val();
    var depend_version =$("#edit-depend-version").val();


    var install_script = $("#edit-install-script").val();
    $.post('/code/editdepend/',{'action':'edit','depend_name':depend_name,'depend_id':depend_id,'depend_version':depend_version,'install_script':install_script},function(data){
     if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        alert(data);
        if (data == "修改成功"){
            location.reload();
        }
        }
    });
});




//删除依赖环境
$("td a[name='del-depend']").click(function(){
   var depend_id = $(this).attr('depend_id');
   var statu = confirm("是否确认删除！");
   if (statu==true)
    {
    $.post("/code/deldepend/",{'depend_id':depend_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        if (data == "已删除"){
            location.reload();
        }
    }
    })

    }
});




//////////////////代码发布//////////////////////

//新建发布
$("#sub-post").click(function(){
    var site_name = $("#site-name").val();
    var ips = $("#post-ip").val();
    var post_ip = JSON.stringify(ips);
    var site_dir = $("#site-path").val();
    var postsite_msg = $("#postsite-msg").val();
    $.post('/code/addpost/',{'site_name':site_name,'post_ip':post_ip,'site_dir':site_dir,'postsite_msg':postsite_msg},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        alert(data);
        if (data == "发布成功"){
            location.reload();
        }
        }
    });
});



//删除已发布站点
$("td a[name='delcode']").click(function(){
   var post_id = $(this).attr('post_id');

   var statu = confirm("是否确认删除！");

   if (statu==true)
    {
    $.post("/code/delpost/",{'post_id':post_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        if (data == "已删除"){

            location.reload();
        }
    }
    })

    }
});



//更新代码
$("a[name='upcode']").click(function(){

    var post_id = $(this).attr("post_id");
    $.post('/code/upcode/',{'post_id':post_id},function(data){
    if (data == "权限不足"){
        alert("权限不足，请联系管理员！");
    }else{

        alert(data);
        //location.reload();
        }
    });
});



 //版本回滚
$("a[name='record_rollback']").click(function(){
    console.log(23213);
    var record_id = $(this).attr("record_id");

    $.post('/code/rollback/',{'record_id':record_id},function(data){
        if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

            alert(data);
            //location.reload();
        }
    });
});


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});

////////////////////站点查询//////////////////////////

//通过站点名称查询
$("#select-site").change(function(){
    var site_id = $("#select-site").val();
    $("#select-project").val(0);
    $("#select-ip").val(0);
    $.post('/code/filtersite/',{'site_id':site_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        $("#site-info").empty();
        $("#site-info").append(data);
        }
    })
});



//通过项目查询
$("#select-project").change(function(){

    var project_id= $("#select-project").val();

    $("#select-site").val(0);
    $("#select-ip").val(0);
    $.post('/code/filtersite/',{'project_id':project_id},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        $("#site-info").empty();
        $("#site-info").append(data);
        }
    })
});


//通过设备类型查询
$("#select-ip").change(function(){
    var ip = $("#select-ip").val();
    $("#select-project").val(0);
    $("#select-site").val(0);

    $.post('/code/filtersite/',{'ip':ip},function(data){
    if (data == "权限不足"){
            alert("权限不足，请联系管理员！");
        }else{

        $("#site-info").empty();
        $("#site-info").append(data);
        }
    })
});

