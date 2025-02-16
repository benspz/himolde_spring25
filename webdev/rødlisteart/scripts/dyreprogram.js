const image = document.querySelector("#bird");

image.onclick = () => {
    const mySrc = image.getAttribute('src');
    if (mySrc === 'images/ærfugl.jpg') { 
      image.setAttribute('src','images/E-unger.jpg');
    } else {
      image.setAttribute('src','images/ærfugl.jpg');
    }
  }