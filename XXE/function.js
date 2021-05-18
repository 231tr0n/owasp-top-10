function zeltron(file) {
     let file_variable = file.files[0];
     let file_reader = new FileReader();

     file_reader.readAsText(file_variable);

     file_reader.onload = function() {
          let file_data = file_reader.result;
          let name = [];
          let nickname = [];
          let age = [];
          let level = [];
          let rank = [];

          let xml_parser = new DOMParser();

          //The patch to prevent xml external entity attacks is to disable all external entities and DTD processing
          /*// Do not expand entity references
          xml_parser.setAttribute(DOMParser.EXPAND_ENTITYREF, false);

          // dtdObj is an instance of oracle.xml.parser.v2.DTD
          xml_parser.setAttribute(DOMParser.DTD_OBJECT, dtdObj);

          // Do not allow more than 11 levels of entity expansion
          xml_parser.setAttribute(DOMParser.ENTITY_EXPANSION_DEPTH, 12);*/

          let xml_data = xml_parser.parseFromString(file_data,"text/xml");
          console.log(xml_data);
          var x = xml_data.getElementsByTagName("name");

          for (let i = 0; i < x.length; i ++) {
               name[i] = xml_data.getElementsByTagName("name")[i].childNodes[0].nodeValue;
          }

          for (let j = 0; j < x.length; j ++) {
               nickname[j] = xml_data.getElementsByTagName("nickname")[j].childNodes[0].nodeValue;
          }

          for (let d = 0; d < x.length; d ++) {
               age[d] = xml_data.getElementsByTagName("age")[d].childNodes[0].nodeValue;
          }

          for (let a = 0; a < x.length; a ++) {
               level[a] = xml_data.getElementsByTagName("level")[a].childNodes[0].nodeValue;
          }

          for (let b = 0; b < x.length; b ++) {
               rank[b] = xml_data.getElementsByTagName("rank")[b].childNodes[0].nodeValue;
          }
          let inner_html = "";
          for (let u = 0; u < x.length; u ++) {
               inner_html = inner_html + '<tr>' + '<td align = "center" class = "input">' + name[u] + '</td>' + '<td align = "center" class = "input">' + nickname[u] + '</td>' + '<td align = "center" class = "input">' + age[u] + '</td>' + '<td align = "center" class = "input">' + level[u] + '</td>' + '<td align = "center" class = "input">' + rank[u] + '</td>' + '</tr>';
          }

          document.getElementById("zeltron").innerHTML = inner_html;
          document.getElementById("zeltron55").innerHTML = file_data;
   };

   file_reader.onerror = function() {
       console.log(file_reader.error);
   };
}
