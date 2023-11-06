const removeAfterRead = document.getElementById("TutorialDiv");

window.onload = () => 
{
    let reader = new FileReader(),
        selector = document.getElementById("SelectCSV"),
        table = document.getElementById("CSVTable");

    selector.onchange = () => reader.readAsText(selector.files[0]);

    reader.onload = () => 
    {
        removeAfterRead.remove();

        let csv = reader.result;
        table.innerHTML = "";

        let rows = csv.split("\r\n");

            for (let row of rows) 
            {
                let cols = row.match(/(?:\"([^\"]*(?:\"\"[^\"]*)*)\")|([^\",]+)/g);
                if (cols != null)
                {
                    let tablerow = table.insertRow();
                    for (let col of cols)
                    {
                        let td = tablerow.insertCell();
                        td.innerHTML = col.replace(/(^"|"$)/g, "");
                    }
                }
            }
    }
}