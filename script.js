function createChart() {

    let form = new FormData(document.getElementById("chartForm"));

    fetch("/custom_chart", {
        method: "POST",
        body: form
    })
    .then(response => response.json())
    .then(data => {

        if (data.error) {
            alert(data.error);
            return;
        }

        // 🔥 force refresh image
        document.getElementById("customChart").src =
            "/" + data.path + "?t=" + new Date().getTime();
    })
    .catch(err => {
        alert("Error generating chart");
        console.log(err);
    });
}
function sendMessage(){
 let q=document.getElementById("chatInput").value;

 fetch("/chat",{
  method:"POST",
  headers:{"Content-Type":"application/x-www-form-urlencoded"},
  body:"question="+q
 })
 .then(r=>r.text())
 .then(d=>{
  document.getElementById("chatBox").innerHTML+=
  "<p><b>Bot:</b> "+d+"</p>";
 });
}