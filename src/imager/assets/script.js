const picker = document.querySelector(".picker-button");
const scale = document.querySelector(".scale-range");
const image = document.querySelector(".image");

const output_code = document.querySelector(".output-code");
const generate_code = document.querySelector(".generate-code");

const update_image = () => {
    image.src = "/image?timestamp=" + Math.floor(Math.random() * 1000000);
}

picker.addEventListener("click", () => {
    let filepath = eel.update_file();

    console.log("Changed filepath to " + filepath);

    update_image();
});

scale.addEventListener("change", () => {
    let value = eel.update_scale(scale.value);

    console.log("Changed scale to " + value);

    update_image();
})


generate_code.addEventListener("click", () => {
    eel.generate_code()().then((value) => {
        output_code.innerHTML = value;
    });
});