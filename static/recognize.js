var input = document.getElementById('file');
var infoArea = document.getElementById('file-filename');
input.addEventListener('change', showFileName);
function showFileName(event) {
 var input = event.srcElement;
 var fileName = input.files[0].name;
 infoArea.textContent = 'File name: ' + fileName;
}
