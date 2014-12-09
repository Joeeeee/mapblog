function hideFriendList() {
	$("#friend_list").fadeOut("slow");
	$("#new_blog").fadeOut("slow");
}

function showFriendList() {
	$("#friend_list").fadeIn("slow");
	showCloseButton();
}

function showCloseButton() {
	$("#closeButton").slideDown("50000");
}

function newBlog() {
	$("#new_blog").fadeIn("slow");
}