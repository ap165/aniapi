////////////////////////////////////
/*  

fetch('url')
  .then(response => {
    return response.json();
  }).then(data => {
    console.log(data);
  }).catch(error => {
    console.error(error)
  });

*/
///////////////////////////////////////




// navbar openClose
let closeBtn = document.querySelector(".close_menu button");
let openBtn = document.querySelector(".nav_title .sidebar");
let sidebar_menu = document.querySelector(".sidebar_menu");
let opened = false;
function openCloseNav() {
  if (opened) {
    opened = false;
    sidebar_menu.style.width = "0";
  }
  else if (!opened) {
    opened = true;
    sidebar_menu.style.width = "300px";
  }
}
openBtn.addEventListener("click", openCloseNav);
closeBtn.addEventListener("click", openCloseNav);

/// slider
let slider = document.querySelector('.slideShow .slider');
console.log(slider.offsetWidth)
slider.style.height = `${1.42 * (slider.offsetWidth)}px`;
let counter = 0;
// image Slide show //
fetch('https://aniapi-eight.vercel.app/api/topAnimes?page=1')
  .then(response => {
    return response.json();
  }).then(data => {
    // console.log(data);
    let SlidesList = data['items'];
    for (let i = 0; i < 11; i++) {
      slider.innerHTML += `<div class='a' style='left: ${i * 100}%'>
  <div class='btn'>
  <span class='bg2'><img src='${SlidesList[i]['imgs']['large']}'></span>
  <span class='bg1'></span>
  <div class="card-content fx">
      <div class="info">
        <h5 style="color: lightgreen; font-weight: bold">#${i + 1} Spotlight</h5>
        <h1> ${SlidesList[i]['title']} </h1> <br>\n
        <h5 style="color: #999; font-weight: bolder; flex-wrap: wrap; justify-content: left" class="fx fx-center">
          <span style="color: #FFF" class="material-symbols-rounded">smart_display</span> &nbsp;${SlidesList[i]["otherInfo"].split("\n")[0].split("(")[0]} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span style="color: #FFF" class="material-symbols-rounded">calendar_month</span>&nbsp;${SlidesList[i]["otherInfo"].split("\n")[1].replace("-", ",")} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <svg style="fill: lightgreen" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M300-440h80v50q0 13 8.5 21.5T410-360q13 0 21.5-8.5T440-390v-180q0-13-8.5-21.5T410-600q-13 0-21.5 8.5T380-570v70h-80v-70q0-13-8.5-21.5T270-600q-13 0-21.5 8.5T240-570v180q0 13 8.5 21.5T270-360q13 0 21.5-8.5T300-390v-50Zm240 80h140q17 0 28.5-11.5T720-400v-160q0-17-11.5-28.5T680-600H540q-8 0-14 6t-6 14v200q0 8 6 14t14 6Zm40-60v-120h80v120h-80ZM160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Z"/></svg>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ep-no"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#333"><path d="M18 4l1.82 3.64c.08.16-.04.36-.22.36h-1.98c-.38 0-.73-.21-.89-.55L15 4h-2l1.82 3.64c.08.16-.04.36-.22.36h-1.98c-.38 0-.73-.21-.89-.55L10 4H8l1.82 3.64c.08.16-.04.36-.22.36H7.62c-.38 0-.73-.21-.9-.55L5 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V5c0-.55-.45-1-1-1h-3z"/></svg>&nbsp;${SlidesList[i]["otherInfo"].split("\n")[0].split("(")[1].replace(" eps)", "")}</span>
        </h5> <h5 style="justify-content: left; margin-top 5px;fill: #FFD700" class="fx fx-center"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M480-308 332-195q-11 9-24 8.5t-23-7.5q-10-7-15.5-19t-.5-26l57-185-145-103q-12-8-15-21t1-24q4-11 14-19.5t24-8.5h179l58-192q5-14 15.5-21.5T480-821q12 0 22.5 7.5T518-792l58 192h179q14 0 24 8.5t14 19.5q4 11 1 24t-15 21L634-424l57 185q5 14-.5 26T675-194q-10 7-23 7.5t-24-8.5L480-308Z"/></svg> &nbsp;${SlidesList[i]['score']}</h5> <br><br>
        <a href="#" style="display: block; margin: auto;"><button class="slideShow-button fx fx-center">
        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="m426-330 195-125q14-9 14-25t-14-25L426-630q-15-10-30.5-1.5T380-605v250q0 18 15.5 26.5T426-330Zm54 250q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z"/></svg> &nbsp;&nbsp;Watch Now</button></a>
      </div>
      <div class='slideshowImg'><img src='${SlidesList[i]['imgs']['large']}'></div>
  </div>
  </div></div>`;
    }
  }).catch(error => {
    console.error(error)
  });

let slidesNo = 11;
let x = 10;
function slide() {
  let slides = slider.querySelectorAll('.a');
  if (Math.abs(counter) > (slidesNo - 1)) {
    counter = 0;
  }
  for (let i = 0; i < slidesNo; i++) {
    slides[i].style.transform = `translateX(-${(Math.abs(counter)) * 100}%)`;
  }
}
let prev = () => {
  if (counter > 0) {
    counter -= 1;
    slide()
  }
  else if (counter == 0) {
    counter = x - 1;
    slide()
  }
}
let next = () => {
  if (counter == 9) {
    counter = -1
  }
  counter += 1;
  slide()
}
setInterval(next, 8000);
/////////////////////////////////


/// tranding anime ///
let cards = document.querySelector(".trending .cards");
fetch('https://aniapi-eight.vercel.app/api/topAnimes?type=favorite&page=1')
  .then(response => {
    return response.json();
  }).then(data => {
    console.log(data);
    let SlidesList = data['items'];
    for (let i = 0; i < 10; i++) {
      cards.innerHTML += `
      <div class="card fx" style="transform: translateX(${i}px)">
  <div class="rank">#${i+1}</div>
    <div class="image">
      <div class="card_bg2"></div>
      <div class="card_bg" style="background-image: url('${SlidesList[i]['imgs']['large']}');"></div>
      <img src="${SlidesList[i]['imgs']['large']}" alt="${SlidesList[i]['title']}">
    </div>
  <div class="card-title">${SlidesList[i]['title']}</div>
</div>`;
    }
  }).catch(error => {
    console.error(error)
  });

  

let trandingScrollCount = 0
function nextTrending(){
    let x = 9 - Math.floor(document.body.offsetWidth / 195)
    if(trandingScrollCount > x){
      trandingScrollCount = x
  }
  
  trandingScrollCount += 1;
  cards.style.transform = `translateX(-${196*trandingScrollCount}px)`;
}

function prevTrending(){
  if(trandingScrollCount < 1){
    trandingScrollCount = 1
  }
  trandingScrollCount -= 1;
  cards.style.transform = `translateX(-${196*trandingScrollCount}px)`;
}

/// tranding anime ///
let popularCards = document.querySelector(".popular .cards");
fetch('https://aniapi-eight.vercel.app/api/topAnimes?type=bypopularity&page=1')
  .then(response => {
    return response.json();
  }).then(data => {
    console.log(data);
    let SlidesList = data['items'];
    for (let i = 0; i < 10; i++) {
      popularCards.innerHTML += `
      <div class="card fx" style="transform: translateX(${i}px)">
  <div class="rank">#${i+1}</div>
    <div class="image">
      <div class="card_bg2"></div>
      <div class="card_bg" style="background-image: url('${SlidesList[i]['imgs']['large']}');"></div>
      <img src="${SlidesList[i]['imgs']['large']}" alt="${SlidesList[i]['title']}">
    </div>
  <div class="card-title">${SlidesList[i]['title']}</div>
</div>`;
    }
  }).catch(error => {
    console.error(error)
  });

  

let popularScrollCount = 0
function nextPopular(){
    let x = 9 - Math.floor(document.body.offsetWidth / 195)
    if(popularScrollCount > x){
      popularScrollCount = x
  }
  
  popularScrollCount += 1;
  popularCards.style.transform = `translateX(-${196*popularScrollCount}px)`;
}

function prevPopular(){
  if(popularScrollCount < 1){
    popularScrollCount = 1
  }
  popularScrollCount -= 1;
  popularCards.style.transform = `translateX(-${196*popularScrollCount}px)`;
}