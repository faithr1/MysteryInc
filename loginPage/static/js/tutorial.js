/* clicking on the help button should make the hidden popup box appear
*  currently isn't working. */
function need_help() {
    document.getElementById('help').addEventListener('click', function () {
        document.querySelector('.bg-modal').style.display = 'flex';
    });

}