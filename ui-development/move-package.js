const fs = require('fs')
const fsExtra = require("fs-extra");
const path = require('path')
const delete_directory = '../server/public'
const move_dir = "./public/"

//Remove the  old public folder
fs.readdir(delete_directory, (err, files) =>{
    if(err) throw err;
    for(const file of files){
        if(file.includes(".")){
            fs.unlinkSync(path.join(delete_directory, file));
        }
    }

    //ONce directory is remove lets move the new files...
    moveFiles()
});

function moveFiles(){

   fsExtra.copy(move_dir, delete_directory, (err)=> {
       if(err) throw err;
   });
}