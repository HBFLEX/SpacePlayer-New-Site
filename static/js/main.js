const timeRemaining = document.querySelector('.time-remaining')
const platform = document.querySelector('.platform')
const downloadBtn = document.querySelector('.downloadBtn')
const downloadStatus = document.querySelector('.status')

let counter = 9

timeRemaining.innerHTML = counter

const updateSiteAnalytics = () => {
    fetch('https://spaceplayer-bt5e.onrender.com/download/started', {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({
            isDownloadStarted:"yes"
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((err) => console.log('There was an error sending the request to the server', err))
}

if(window.location.pathname === '/download'){

    const showTimeRemainingToDownloadFile = () => {
        if(counter === 0) counter = 0
        else counter--
        timeRemaining.innerHTML = counter
    }

    setInterval(showTimeRemainingToDownloadFile, 1000);
    clearInterval(showTimeRemainingToDownloadFile)

    const downloadApp = () => {
        const a = document.createElement('a')
        let fileToDownload

        if(platform.innerHTML.trim() === 'windows'){
            fileToDownload = 'splaceplayer(Win32-x64).zip'
            a.href = 'https://drive.google.com/uc?export=download&id=16zF5N8UPt06lPw9hu57ndyGYp_49Jb0W'
        }else{
            fileToDownload = 'splaceplayer(Linux-x64).zip'
            a.href = 'https://drive.google.com/uc?export=download&id=1ImV7ad_4a3GKza8JsyDuwH9dfKwp1Qw5'
        }

        a.download = fileToDownload
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
        clearTimeout(downloadApp)
        downloadStatus.innerHTML = `<p class="status lead">Status: <span class="bg-success p-1 rounded">🫡👍</span></p>`
        updateSiteAnalytics()
    }

    setTimeout(downloadApp, 9000)
}

downloadBtn.addEventListener('click', (event) => {
    downloadStatus.innerHTML = `<p class="status lead">Status: <span class="bg-success p-1 rounded">🫡👍</span></p>`
    updateSiteAnalytics()
})