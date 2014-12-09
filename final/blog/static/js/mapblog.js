function getFriendList() {

}

function getFriendBlog() {

}

function publishBlog() {

}
function sendblog() {
	//alert("helloworld");
	content = document.getElementById("editor").value
	alert(content);
	$.ajax({
		type:"post",
		url:"127.0.0.1:8080/mapblog/newblog",
		async:true,
	});
}
