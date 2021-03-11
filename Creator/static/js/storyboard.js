// This function will take the user back to their homepage without saving
// their progress on the current story thus all progress will be lost
// will gain functionality once other pages are added into the same project
// and function properly
function return_to_home() {

    if(confirm("Are you sure you wish to return to the home screen? You will lose " +
               "all unsaved progress on current story.")) {

    }

}
////////////////////////////////////////////////////////////////////////////////

// This function will create a new story by clearing all attributes on the
// storyboard such as its title,synopsis, and clues (Currently clues cannot be
// added thus they removal shall be added later once added remove this comment
// section)
function start_new_story() {

    // Confirms if the user means to start a new story before clearing the storyboard
    if(confirm("Are you sure you wish to start a new story? You will lose " +
               "all unsaved progress on current story.")) {

        document.getElementById("title").value = "";
        document.getElementById("synopsis").value = "";

        // Will need to add more to this to accommodate for clues in the storyboard
        // but right now this clears all existing information on the storyboard(title, synopsis)
        // since clues cannot be created and added to the storyboard yet

    }

}
////////////////////////////////////////////////////////////////////////////////

// Shall take all the information stored within the storyboard and save it
// either to a text file on the users PC or to the database linked to the
// users account
function save_story() {

    alert("You're attempting to save, sorry but that's not implemented yet " +
          "so have fun memorizing all your progress!!");

}
////////////////////////////////////////////////////////////////////////////////

// Shall read in information from a selected story and propagate the storyboard
// with its information not sure if it will try to read from the database thus
// providing a list of stories or asking for the stories name or load in from a
// text file that is stored on the users PC
function load_story() {

    alert("You're attempting to load in a previously created story, sorry but " +
          "that's not implemented yet so have fun typing it all out again!!");

}
////////////////////////////////////////////////////////////////////////////////

// Shall add a clue to the storyboard without clearing any of the information that
// already exists within the storyboard will be implemented after clue objects have
// been properly created
function add_clue() {

    alert("You're attempting to add a clue to the storyboard, sorry but that's " +
          "not implemented yet so have fun with the synopsis!!");

}
////////////////////////////////////////////////////////////////////////////////