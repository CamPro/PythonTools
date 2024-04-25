import asyncio
import time
from pyppeteer import launcher
from pyppeteer import launch
launcher.AUTOMATION_ARGS.remove('--enable-automation')

launch_args = {
'headless': False,
#'executablePath': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
#'userDataDir': 'D:\000000000',
'args': [
'--start-maximized',
'--no-sandbox',
'--disable-infobars',
'--ignore-certificate-errors',
'--log-level=3',
'--enable-extensions',
#'--window-size=1366,768',
'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
],
}

async def main():
	browser = await launch(**launch_args)
	page = await browser.newPage()

	await page.goto('https://vn.mail.yahoo.com/mail/')
	await page.screenshot({'path': 'google.png'})
	height = await page.evaluate('() => document.body.scrollHeight')
	content = await page.evaluate('document.body.textContent', force_expr=True)
	title = await page.evaluate('(element) => element.textContent', element)
	await page.focus('#login-username')

	await page.waitFor('#login-username')
	time.sleep(1)
	element1 = await page.querySelector('#login-username')
	await element1.click()
	time.sleep(1)
	await page.keyboard.type('thanhgiau3325')
	time.sleep(1)

	await page.waitFor('#login-signin')
#element2 = await page.querySelector('#login-signin')
#await element2.click()
#time.sleep(5)

#await page.waitFor('#login-passwd')
#element3 = await page.querySelector('#login-passwd')
#await element3.click()
#time.sleep(1)
#await page.keyboard.type('thanh@2503')
#time.sleep(1)

#await page.waitFor('#login-signin')
#element4 = await page.querySelector('#login-signin')
#await element4.click()

const songs = await page.evaluate(() => {
	let items = document.querySelectorAll(".name_song");
	let links = [];
	items.forEach(item => {
		links.push({
			title: item.innerText,
			url: item.getAttribute("href")
			});
		});
	return links;
	});
console.log(songs);
for (let song of songs) {
await page.goto(song.url);
let lyric = await page.evaluate(() => {
	let lyric = document
	.getElementsByClassName("pd_lyric trans")[0]
	.innerHTML.replace(/\<br\>/g, "");
	return lyric;
	});
console.log(song.title);
console.log("..............................");
console.log(lyric);
}
for (let song of songs) {
await page.goto(song.url);
let lyric = await page.evaluate(() => {
	let lyric = document
	.getElementsByClassName("pd_lyric trans")[0]
	.innerHTML.replace(/\<br\>/g, "");
	return lyric;
	});
await fs.writeFile(`${song.title}.txt`, lyric, function(err) {
	if (err) throw err;
	console.log("Saved:" + song.title);
	});
}it('should show a list of results when searching actual word', async () => {
	await page.type('input[id=search_form_input_homepage]', 'puppeteer');
	await page.click('input[type="submit"]');
	await page.waitForSelector('h2 a');
	const links = await page.evaluate(() => {
		return Array.from(document.querySelectorAll('h2 a'));
		});
	expect(links.length).to.be.greaterThan(0);
	});

it('should show a warning when searching fake word', async () => {
	await page.type('input[id=search_form_input_homepage]', 'pupuppeppeteerteer');
	await page.click('input[type="submit"]');
	await page.waitForSelector('div[class=msg__wrap]');
	const text = await page.evaluate(() => {
		return document.querySelector('div[class=msg__wrap]').textContent;
		});
	expect(text).to.contain('Not many results contain');
	});


time.sleep(15)
await browser.close()

asyncio.get_event_loop().run_until_complete(main())


