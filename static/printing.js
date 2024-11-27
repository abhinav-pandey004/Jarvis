let element = document.getElementById('output')
console.log("hello this is working fine ");
console.log(document.querySelector('#output'));
console.log(element);
element.addEventListener("input", () => {
    element.style.height = "auto";
    element.style.height = `${element.scrollHeight}px`;
});
const adjustHeight = () => {
    element.style.height = "auto";
    element.style.height = `${element.scrollHeight}px`; // Adjust height to content
};
element.addEventListener("input", adjustHeight);
adjustHeight();
element.classList.add("dynamicBox")


function animateTextById(elementId) {
    const element = document.getElementById(elementId);
    const fullText = element.textContent;
    const words = fullText.split(' '); 
    let currentWordIndex = 0;

    element.textContent = ''; 
    const interval = setInterval(() => {
      if (currentWordIndex < words.length) {
        element.textContent += (currentWordIndex === 0 ? '' : ' ') + words[currentWordIndex];
        currentWordIndex++;
      } else {
        clearInterval(interval);
      }
    }, 50);
  }
animateTextById("output")