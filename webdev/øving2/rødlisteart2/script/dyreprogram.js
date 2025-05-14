const image = document.querySelector("#bird");

image.onclick = () => {
    const mySrc = image.getAttribute("src");
    if (mySrc === "bilder/ærfugl.jpg") { 
      image.setAttribute("src","bilder/E-unger.jpg");
    } else if (mySrc === "bilder/E-unger.jpg") {
        image.setAttribute("src", "bilder/E-kaill.jpg")
    } else {
      image.setAttribute("src","bilder/ærfugl.jpg");
    }
  }