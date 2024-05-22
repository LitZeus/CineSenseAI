new autoComplete({
    data: {                           
      src: films,
    },
    selector: "#autoComplete",           // Input field selector               
    threshold: 1,                        // Min. Chars length to start Engine  
    debounce: 100,                       // Post duration for engine to start  
    searchEngine: "strict",              // Search Engine type/mode            
    resultsList: {                            
        render: true,
        container: source => {
            source.setAttribute("id", "food_list");
        },
        destination: document.querySelector("#autoComplete"),
        position: "afterend",
        element: "ul"
    },
    maxResults: 7,                         
    highlight: true,                       // Highlight matching results       
    resultItem: {                          // Rendered result item             
        content: (data, source) => {
            source.innerHTML = data.match;
        },
        element: "li"
    },
    noResults: () => {                     // Action script on noResults       
        const result = document.createElement("li");
        result.setAttribute("class", "no_result");
        result.setAttribute("tabindex", "1");
        result.innerHTML = "No Results";
        document.querySelector("#autoComplete_list").appendChild(result);
    },
    onSelection: feedback => {             // Action script onSelection event  
        document.getElementById('autoComplete').value = feedback.selection.value;
    }
});