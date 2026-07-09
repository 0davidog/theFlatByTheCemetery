# Flat by the Cemetery

_Author: David O'Gara_

Flat by the Cemetery is an interactive Front-End web application using HTML and CSS to present a portfolio website that showcases the visual work of an artist/illustrator.

Users of the site will be able to find information on the artist, see examples of their work, and get in touch via a contact form or social media links. The target audience of the website are people, like-minded to the author and potential clients or collaborators that may wish to learn more about the work or follow any future developments.
The project goal for the site owner is to drive engagement and interest with the artist's work by providing a visual demonstration/overview of the work. An additional goal is to build and demonstrate skill regarding HTML and CSS based web design for the site author.

![am-i-responsive-image](https://github.com/0davidog/flatbythecemetery/assets/135815736/4541a755-539d-4e64-8409-3ba444810770)

## Contents

- [Deployed Website](#deployed-website)
- [Repository](#repository)
- [Wireframes](#wireframes)
- [Features](#features)
  - [Main Image](#main-image)
  - [About the title and colour scheme](#about-the-title-and-colour-scheme)
  - [About the font choice](#about-the-font-choice)
  - [Navigation Bar](#navigation-bar)
  - [Footer](#footer)
  - [Gallery Section](#gallery-section)
  - [About section](#about-section)
  - [Contact Form](#contact-form)
  - [404 Error Page](#404-error-page)
- [Future Features](#future-features)
- [Testing](#testing)
  - [Link Tests](#link-tests)
  - [Contact Form Test](#contact-form-test)
  - [Initial Screen Size Tests](#initial-screen-size-tests)
  - [Bugs](#bugs)
  - [Browser and OS testing](#browser-and-os-testing)
  - [Market Research](#market-research)
  - [Validator Testing](#validator-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)

## Deployed Website

[Flat by the Cemetery](https://0davidog.github.io/CI_PP1_FlatByTheCemetery/) via Github Pages.

## Repository

[Github](https://github.com/0davidog/CI_PP!_flatbythecemetery/) Repository.

## Wireframes

Here is a PDF of the wireframes put together at the sites inception. Adobe photoshop was used to visually plan the sites look and layout using an iPhone Xs (375x812) and a Dell laptop (1920x1080) as reference for viewport size/ratio.

[Wireframes.pdf](https://github.com/0davidog/flatbythecemetery/files/12063710/Wireframes.pdf)

## Features

### Main Image

- The first thing a user will take notice of is the large background image that dominates the index page. This will immediately give the user an idea what the site is about and sets the tone stylistically for the content within.
- A short line of description 'Art and illustration by David C. O’Gara. Based in Derbyshire, UK" is in front of the image in varying positions dependent of screen size. This will let the user know the subject of the site if they weren't already aware. The container has a black background at half transparency to aid in readability and contrast against the page's background image.

As this is the only content that is featured exclusively on the landing/index page the user should have their attention drawn to the header, displaying the sites title and its navigation menu.

![Screenshot 2023-07-16 at 13-05-46 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/e821cd20-ff04-4568-bcff-dbdd9cd7e599)

### About the title and colour scheme

- The title for the site, 'Flat by the Cemetery' was chosen simply due to the fact the the sites author has lived for some years in an apartment building across from and old cemetery and had been using it already as an [Instagram](https://www.instagram.com/flatbythecemetery/) handle where much the artwork is already shared.
- The colour scheme follows on from this theme in direct homage to a poster of the Luci Fulci film 'House by the Cemetery' that was displayed in the apartment after moving in. This color scheme is black (#000000) for the background, white (#ffffff) for the text and red (#ff0000) for highlights such as headings and active links. A grey colour (#888888) was chosen for emphasis of subtitles and the gallery's additional navigation menu.
- Originally the red highlight used was a darker shade (#990000) out of personal preference but this was changed to aid in contrast and readability.

![Color scheme image screenshot using https://coolors.co/](https://github.com/0davidog/flatbythecemetery/assets/135815736/ed7fa0c8-1451-46e0-b801-c2ef93a2a093)

![House by the Cemetery poster in the author's flat](https://github.com/0davidog/flatbythecemetery/assets/135815736/6295bfc6-9c19-4bd7-b0e5-24173f7daa2f)

### About the font choice

The font choice for the site is the serif font Palatino as this resembles the text of a paperback novel and fits within the sites themes of horror-fiction.

### Navigation Bar

- The navigation bar sits below the sites h1 title in the header and displays in text the links for 'Home, Gallery, About and Contact'. Active and highlighted (hovered over) links will be displayed in red with the hovered-over links underlined while standard links are the sites default white with no extra adornment.
- The order of the links reflect the visual nature of the site, users are encouraged to explore further after their encounter with the 'Home' page and presumably intend to check out more of the work directly at the 'Gallery'. Then if interested in the work the 'About' page offers a place they can visit next to learn a little more about the artist. Finally in the interest of further interaction the user can submit a message to the artist directly using the 'Contact' page.
- The h1 title at the top of the page also acts as a link to the home page as I feel from a user perspective I expect website titles and headers to act in this way, always providing a clear return to the beginning if sense of navigation is lost.

![Screenshot 2023-07-16 at 11-52-54 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/fb7ec8ff-41f2-41e3-9f5b-0102f624211c)

### Footer

- The footer sits at the bottom of every page in a fixed position and provides social media links for ease of access as this is often a user preferred mode of following work and communicating with individual creatives or small businesses and from a site-owner perspective this should drive engagement with social media accounts.
- The social links chosen were Instagram and YouTube and were illustrated using icons from font-awesome. These social links are aligned center. At the wireframe stage the social icons were intended to be fixed to the right but this proved to be visually less appealing.
- Underneath the social links is displayed a copyright reminder as users will be viewing images of an artists work. This is simply to discourage unorthorised use of the images. This is aligned center also for the same reasons as the social links.

![Screenshot 2023-07-16 at 12-35-39 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/d6595b23-b71a-473f-bc5a-8bd7679b91e0)

### Gallery Section

- Gallery section consists of a main menu page in which users can select from an option of 4 gallery collections, each on their own page.
- For extra ease of navigation users are given a second navigation bar under the initial nav-bar that provides text links to the main gallery page and the four collection pages [(This was later removed for smaller device screens)](#bugs).
- The links are illustrated using specially made thumbnail images that give a glimse of the artwork that will be inside each collection. Plain text giving the links a title such as 'Collection 01' sits on top of the thumbnails.
- This combination of both thumbnail images with text overlaid is to remove any ambiguity from a user perspective on where links will lead.

![Screenshot 2023-07-16 at 12-59-06 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/25c3ed43-f50c-4743-ac54-376699a61bb5)

- Each collection page follows the same format as the main gallery page with links to four different image pages being illustrated by specially made thumbnails images hinting at the works content and plain text giving the links a description of 'image 01' etc.

![Screenshot 2023-07-16 at 13-00-04 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/ca2439b4-fcf3-4c9f-9ee2-4213b4c14b3c)

- The final piece of the gallery section is the pages for each individual image, 16 in total.
- I chose to do this as individual pages to give the user an opportunity to look closely at the work and in a decent size depending on the screen used.
- The pages consist of the image/artwork, followed by the works title and a short line of description on the origin, idea or intended use of the artwork/design.
- Two of the pieces were later changed to videos to display another aspect of the author's work. The videos play on a loop automatically and allow a user to interact with the choice of turning the audio on/off due to videos playing with audio automically being considered bad practice.

![Screenshot 2023-07-16 at 13-23-14 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/ae1565c9-321b-4131-bd77-a94d1eede2a6)

### About section

- About section contains a paragraph which gives an overview of the artist and their work as well as links to Instagram, Youtube and Linkedin.
- The section is also decorated with the same image use as the index background, used here as an aside to the text.
- This page is intended to give the audience an introduction to the author and suggest ways in which they can interect or connect in addition to the on-site contact form.

![Screenshot 2023-07-16 at 16-39-44 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/6fe96578-26cb-49f0-8e03-c114306bbb8d)

### Contact Form

- The 'Contact' page contains a form in which the user can get in touch with the artist.
- Form elements include text inputs for name, email and subject and a text field for message content.
- A submit button, styled in red follows.
- All fields except Subject will be required for submission.

![Screenshot 2023-07-16 at 12-35-54 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/98afaa42-9388-4310-94da-76e09bcdabc1)

- Upon completing the form and hitting submit, the form (for the time being) will make use of CodeInstitutes form dump link given in the lessons leading up to the first project. This will open a link in a new window confirming the form was successful.
- In the future the form should send the data given to the site's author via email message (this, however is currently out of the scope of this project and course learning stage).

![Screenshot 2023-07-16 at 14-03-46 Returned form data](https://github.com/0davidog/flatbythecemetery/assets/135815736/a2c16409-d6f7-4ce8-b3a4-a4aaa845b4b1)

### 404 Error Page

- A custom 404 error page was created in the style of the rest of the site with the header and footers from the other pages.
- This provides the user with the navigation options to return to the start or another page without the error seeming too jarring or frustrating.

![Screenshot 2023-07-30 at 16-32-12 Flat by the Cemetery](https://github.com/0davidog/flatbythecemetery/assets/135815736/dd79f5a9-c9c5-4228-89f0-834ec9a3b0f5)

## Future Features

- A fix of the contact form to allow for fully functional email capabilities.
- A blog page/section would be a great fit for a site that follows the work of an artist/creative allowing for periodic updates of activity in greater detail than offered in social media posts.
- A shop for selling prints of artwork or related goods would also be ideal.

## Testing

### Link Tests

I tested all the navigation links on the deployed site to check they perform as expected.

- [x] All links lead to expected location
- [x] All external links open in new window (this includes form result)
- [x] All links accessible by tab key

### Contact Form Test

- Attempted to submit form without any input:

![contact-screen-01](https://github.com/0davidog/flatbythecemetery/assets/135815736/544b57e7-f4da-401c-85b1-7646bfbaadea)

- Attempted to submit form without valid email input:

![contact-screen-02](https://github.com/0davidog/flatbythecemetery/assets/135815736/68a1dc60-8303-42f4-a1ff-56ad6fac4fc8)

- Attempted to submit form without message text field input:

![contact-screen-03](https://github.com/0davidog/flatbythecemetery/assets/135815736/e1cd9792-2b34-4ff5-9d07-8ed67e7c0fe2)

- Submitted form with all valid inputs:

![contact-screen-04](https://github.com/0davidog/flatbythecemetery/assets/135815736/48fd5d6a-a253-433e-b04b-c7d8c2d1c57b)

- Result returned:

![contact-screen-05](https://github.com/0davidog/flatbythecemetery/assets/135815736/97f25982-eaed-4b4f-8b11-9797bfc1a36d)

### Initial Screen Size Tests

For the sake of responsivity the site was frequently tested against various screen sizes for appearance and to guide media query values. The sizes used at this stage are the default device sizes offered as part of Google Chrome's Dev Tools as well as the browser size provided by the Windows Laptop I use. This provided great variety for responsive testing, so I ensured the site looked acceptable on each of these dimensions.

| Device                   | Dimensions |
| ------------------------ | ---------- |
| iPhone SE                | 375x667    |
| iPhone XR                | 414x896    |
| iPhone 12 Pro            | 390x844    |
| Pixel 5                  | 393x851    |
| Samsung Galaxy S8+       | 360x740    |
| Samsung Galaxy S20 Ultra | 412x915    |
| iPad Air                 | 820x1180   |
| iPad Mini                | 768x1024   |
| Surface Pro 7            | 912x1368   |
| Surface Duo              | 540x720    |
| Galaxy Fold              | 280x653    |
| Samsung Galaxy A51/71    | 412x914    |
| Nest Hub                 | 1024x600   |
| Nest Hub Max             | 1280x800   |
| Windows laptop           | 1920x1080  |

### Bugs

In testing the site over time there were many challenges that presented themselves, especially when testing across devices and viewport sizes. These provided opportunities to tweak various aspects of the code to ensure the site looks appropriate across platforms.

This included;

- The second navigation bar introduced in the gallery pages, while allowing for an even clearer version of the links otherwise presented as images, proved to take up valuable viewport space needed on small devices such as the Galaxy Fold, Galaxy S8+ or Huawei P30. The decision was made to remove the secondary nav-bar from display on screens of this size (below 375px width) and free up that space for page content.
- The two videos displayed in the gallery had been encoded with an anamorphic setting. This didn't appear to be an issue as the videos displayed in the intended aspect ratio on all the emulated viewports in Chrome's Dev Tools. However, upon testing with the Mac os via browserstack the videos appeared squashed into a square aspect ratio. The solution taken was simply to republish the videos with a fixed 16.9 aspect.
- I found the images unresponsive to screen size changes at one time and found that my css was targeting the pictue element. Changing the target to the img element fixed the issue.

```
.picture-frame picture{
	width: 100%;
}
```

to

```
.picture-frame img{
	width: 100%;
}
```

### Browser and OS testing

To make sure that the site looked good and responded properly across multiple different devices, browsers and operating systems I used the site [Browserstack](https://www.browserstack.com/) to live test multiple devices I wouldn't otherwise have access to. Here's a list of combinations that I confirmed the site looked and function properly on. Included is my own personal devices used to create the project.

| Device      | OS            | Viewport  | Browser                       | Browserstack Screenshot                                                                                             |
| ----------- | ------------- | --------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Dell Laptop | Windows 10    | 1920x1080 | Firefox, Chrome, Edge         | N/A                                                                                                                 |
| iPhone Xs   | ios16.5.1     | 375x812   | Firefox, Safari, Chrome, Edge | N/A                                                                                                                 |
| iPhone 14   | ios16.5       | 390x664   | Safari                        | [bs-screen-01](https://github.com/0davidog/flatbythecemetery/assets/135815736/b78e03c1-8efe-4510-b181-147710d919d3) |
| Galaxy S23  | An13.0        | 393x786   | Chrome                        | [bs-screen-02](https://github.com/0davidog/flatbythecemetery/assets/135815736/d1dcea02-38fd-4c9b-acea-b6a749bdc18d) |
| Redmi Note  | And12.0       | 390x873   | Chrome                        | [bs-screen-03](https://github.com/0davidog/flatbythecemetery/assets/135815736/e88924d7-40e1-4806-bfef-56021609e017) |
| Pixel 6 Pro | An13.0        | 412x778   | Edge                          | [bs-screen-04](https://github.com/0davidog/flatbythecemetery/assets/135815736/9c1ebb1a-c434-4004-9824-d0e91206f7a4) |
| iPad 10th   | ios16.0       | 393x786   | Safari                        | [bs-screen-05](https://github.com/0davidog/flatbythecemetery/assets/135815736/2bbba2d4-4009-492e-95c1-141d1da9115a) |
| Moto g71    | An11.0        | 412x797   | Chrome                        | [bs-screen-06](https://github.com/0davidog/flatbythecemetery/assets/135815736/79938274-1a15-43c7-ac08-44d6bce458da) |
| P30         | An9.0         | 360x657   | Chrome                        | [bs-screen-07](https://github.com/0davidog/flatbythecemetery/assets/135815736/6e91ec64-e505-4397-b900-a696213efd1b) |
| Mac         | macOS Ventura | 1920x927  | Safari16.3                    | [bs-screen-08](https://github.com/0davidog/flatbythecemetery/assets/135815736/afb98a44-9c5b-49a0-8ed9-469d12953a6e) |

### Market Research

In choosing which combinations of device, operating system and browser to test with I used information from [Statcounter](https://gs.statcounter.com/) to assess which browsers devices and operating systems were most popular. This suggested I make sure to include Chrome as a browser, Samsung Android phones and Apple ios devices.

- Market share stats for Device Vendor

  ![StatCounter-vendor-ww-monthly-202206-202306-bar](https://github.com/0davidog/flatbythecemetery/assets/135815736/494dd527-2855-4399-afe6-171816573f4b)

- Market Share stats for Browser

  ![StatCounter-browser-ww-monthly-202206-202306-bar](https://github.com/0davidog/flatbythecemetery/assets/135815736/4f5c6a28-03dc-47f0-821a-85b31bc96ee4)

### Validator Testing

- Deployed website passed through official W3C Validator service for HTML [link](https://validator.w3.org/)
- [Attatched PDF displays screenshots for each page's test](https://github.com/0davidog/flatbythecemetery/files/12094965/html-validation.pdf)
- Deployed website passed through official W3C Validator service for CSS [link](https://jigsaw.w3.org/css-validator/)

![Screenshot 2023-07-22 at 13-25-42 W3C CSS Validator results for https __0davidog github io_flatbythecemetery_index html (CSS level 3 SVG)](https://github.com/0davidog/flatbythecemetery/assets/135815736/b4b24d1b-f42a-489c-bb9c-296b0c9d7bae)

- [CSS full screenshot here](https://github.com/0davidog/flatbythecemetery/assets/135815736/964b4b95-8608-44f7-968a-7c767e10758f)

### Lighthouse Testing

Used Google Chromes 'Lighthouse' dev tool to assess the deployed site for Performance, Accessibility, Best Practices and Search Engine Optimisation. During development, I periodically checked the lighthouse assessment and made the occasional change as directed.

This included:

- Changing the red highlight colour to a brighter red to improve contrast with the background.
- Switching to newer web formats (webp/webm) for images and video to improve performance.
- Adding meta data of 'userscalable=yes' and 'maxscale=10' so users have more control over page zoom.
- Making sure all images have an 'alt' attribute.

The lighthouse results for the deployed site are as follows:

| Page             | Performance | Accessibility | Best Practice | SEO | Screenshot                                                                                                                  |
| ---------------- | ----------- | ------------- | ------------- | --- | --------------------------------------------------------------------------------------------------------------------------- |
| index            | 99          | 100           | 100           | 100 | [lighthouse-screen-01](https://github.com/0davidog/flatbythecemetery/assets/135815736/4e4313b2-a4eb-4669-ba84-1d5c4ecd6d1a) |
| gallery          | 100         | 100           | 100           | 100 | [lighthouse-screen-02](https://github.com/0davidog/flatbythecemetery/assets/135815736/e2f63ff3-aca3-45a0-90e0-890c50f0de25) |
| collection01     | 99          | 100           | 100           | 100 | [lighthouse-screen-03](https://github.com/0davidog/flatbythecemetery/assets/135815736/3efa4fbc-decf-4491-b0d8-9985c65b498d) |
| collection02     | 100         | 100           | 100           | 100 | [lighthouse-screen-04](https://github.com/0davidog/flatbythecemetery/assets/135815736/a92ece92-b89e-44da-a105-4a3d7f1c93e8) |
| collection03     | 100         | 100           | 100           | 100 | [lighthouse-screen-05](https://github.com/0davidog/flatbythecemetery/assets/135815736/3751fc21-382c-449f-898a-48f0ed206de3) |
| collection04     | 100         | 100           | 100           | 100 | [lighthouse-screen-06](https://github.com/0davidog/flatbythecemetery/assets/135815736/1e7d6b34-be10-4643-a611-cd42b27fa5ed) |
| about            | 99          | 100           | 100           | 100 | [lighthouse-screen-07](https://github.com/0davidog/flatbythecemetery/assets/135815736/3d277b88-be3e-419b-bb0f-780788124ad6) |
| contact          | 100         | 100           | 100           | 100 | [lighthouse-screen-08](https://github.com/0davidog/flatbythecemetery/assets/135815736/5c995b26-ea38-46b9-97a7-a3bed88a3c47) |
| gallery-image-01 | 92          | 100           | 100           | 100 | [lighthouse-screen-09](https://github.com/0davidog/flatbythecemetery/assets/135815736/922de014-8c6b-4755-9c15-10aee4266491) |
| gallery-image-02 | 100         | 100           | 100           | 100 | [lighthouse-screen-10](https://github.com/0davidog/flatbythecemetery/assets/135815736/e0f8d2c5-2c4a-4398-b65d-6b100439d7c9) |
| gallery-image-03 | 92          | 100           | 100           | 100 | [lighthouse-screen-11](https://github.com/0davidog/flatbythecemetery/assets/135815736/cec6a6c9-9a26-4ee8-9f22-ae307e8152c1) |
| gallery-image-04 | 92          | 100           | 100           | 100 | [lighthouse-screen-12](https://github.com/0davidog/flatbythecemetery/assets/135815736/b9a0a9fe-2642-4083-aac6-91127f0be204) |
| gallery-image-05 | 100         | 100           | 100           | 100 | [lighthouse-screen-13](https://github.com/0davidog/flatbythecemetery/assets/135815736/fb8cba0c-6bf3-4217-bc78-a364722948a1) |
| gallery-image-06 | 100         | 100           | 100           | 100 | [lighthouse-screen-14](https://github.com/0davidog/flatbythecemetery/assets/135815736/1ff0d243-ebc0-4e4a-91bf-f15e8af1281f) |
| gallery-image-07 | 100         | 100           | 100           | 100 | [lighthouse-screen-15](https://github.com/0davidog/flatbythecemetery/assets/135815736/77f23b9d-10c8-470e-8fc8-8a29f5468264) |
| gallery-image-08 | 98          | 100           | 100           | 100 | [lighthouse-screen-16](https://github.com/0davidog/flatbythecemetery/assets/135815736/5a87c9b5-3ab5-4a6c-be1f-a347a876a276) |
| gallery-image-09 | 100         | 100           | 100           | 100 | [lighthouse-screen-17](https://github.com/0davidog/flatbythecemetery/assets/135815736/55c328ea-eb4c-4ebd-a414-38b29bf837b2) |
| gallery-image-10 | 100         | 100           | 100           | 100 | [lighthouse-screen-18](https://github.com/0davidog/flatbythecemetery/assets/135815736/f3656aa8-3067-4e3e-a296-87f08a8a7683) |
| gallery-image-11 | 100         | 100           | 100           | 100 | [lighthouse-screen-19](https://github.com/0davidog/flatbythecemetery/assets/135815736/2e0ab728-8173-4492-9d1e-fd9557a53f3d) |
| gallery-image-12 | 99          | 100           | 100           | 100 | [lighthouse-screen-20](https://github.com/0davidog/flatbythecemetery/assets/135815736/985874e5-9f72-48f5-adb2-6ab1a1c32fa9) |
| gallery-image-13 | 94          | 100           | 100           | 100 | [lighthouse-screen-21](https://github.com/0davidog/flatbythecemetery/assets/135815736/b25e31bd-2fa1-4f7f-9a90-2f32c5daea70) |
| gallery-image-14 | 91          | 100           | 100           | 100 | [lighthouse-screen-22](https://github.com/0davidog/flatbythecemetery/assets/135815736/45ddab7c-2639-445f-9bf7-edff6819161e) |
| gallery-image-15 | 100         | 100           | 100           | 100 | [lighthouse-screen-23](https://github.com/0davidog/flatbythecemetery/assets/135815736/a75ab231-73e0-4490-9f1a-f3442d0919fe) |
| gallery-image-16 | 100         | 100           | 100           | 90  | [lighthouse-screen-24](https://github.com/0davidog/flatbythecemetery/assets/135815736/6836de7c-6c6f-4fb4-a517-8e095413ccd7) |

## Unfixed Bugs

No known bugs remain unfixed.

## Deployment

The website is deployed on [Github](https://github.com/) using GithubPages.
The instructions for this are as follows:

- Navigate to the settings tab in the Github repository.

![Screenshot 2023-07-30 at 16-40-46 0davidog_flatbythecemetery Artist Portfolio  Project 01](https://github.com/0davidog/flatbythecemetery/assets/135815736/6a60e5e1-cbd1-4678-b57f-ae54fd67c312)

- In the left hand menu, navigate to 'Pages', under 'Code and Automation'.

![github-pages-menu](https://github.com/0davidog/flatbythecemetery/assets/135815736/a560845a-8b95-4b39-97f0-812cce082eb1)

- Select 'main' as the branch in the dropdown menu under 'Build and Deployment' and hit 'Save'.

![github-pages-menu-branch](https://github.com/0davidog/flatbythecemetery/assets/135815736/5e2d0e0b-370d-4bbf-ac9c-0d400e186c11)

- Once ready the url for the deployed site will be available at the top of the page.

![Screenshot 2023-07-30 at 17-00-43 0davidog_flatbythecemetery Artist Portfolio  Project 01](https://github.com/0davidog/flatbythecemetery/assets/135815736/2beb814e-867f-4db6-864b-10cff9adb7dd)

- [LINK](https://0davidog.github.io/flatbythecemetery/index.html)

## Credits

### Languages Used

- HTML
- CSS

### Tools Used

- Adobe Dreamweaver
- Adobe Photoshop (for images and wire-frames)
- Adobe Premiere Pro (for videos in gallery)
- [Git](https://git-scm.com/)
- [Github](https://github.com/)

### Content

#### Font Awesome Icons

- The Icons for Instagram and Youtube were sourced from the [Font Awesome website](https://fontawesome.com/).
  - [Instagram Icon](https://fontawesome.com/icons/instagram?f=brands&s=solid)
  - [Youtube Icon](https://fontawesome.com/icons/youtube?f=brands&s=solid)
  - [Linkedin Icon](https://fontawesome.com/icons/linkedin?f=brands&s=solid)

- [Multi Device Image in README generated with 'Am I Responsive?'](https://ui.dev/amiresponsive)
- [Table of contents in README generated with markdown-toc](http://ecotrust-canada.github.io/markdown-toc/')
- [Colour palate image in README generated with coolors.co](https://coolors.co/)
- [Favicon icons and code courtesy of favicon.io](https://favicon.io/favicon-converter/)

#### Flex Grid Tutorial

- Used a tutorial to create a flex-grid that allows content to be arranged in a grid in a responsive manner.
- [link to tutorial](https://www.taniarascia.com/easiest-flex-grid-ever/)
- My css code:

```
  /* setting a flex grid for about section */
/* learning from https://www.taniarascia.com/easiest-flex-grid-ever/ */
#about-section {
	margin-top: 100px;
	margin-bottom: 100px;
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
}
#portrait {
	text-align: center;
	flex-basis: 100%;
	padding-top: 50px;
	color: #888888;
}
#portrait img {
	width: 80%;
	padding-bottom: 10px;
}
#about-text {
	line-height: 200%;
	padding: 50px;
	flex-basis: 100%;
}
```

```
/*media query for flex grid */
/* learning from https://www.taniarascia.com/easiest-flex-grid-ever/ */
@media screen and (min-width: 1500px) {
	#portrait {
   flex: 3.5;
 }
	#about-text {
   flex: 6.5;
 }
}
```

#### Media

All images and video used are the author's own work.

#### Acknowledgements

- Much of the learning and code framwork is inspired by the html and css essentials and Love-Running modules in the Code Institute Software Development Course.

#### Mentor

Malia Havlicek

#### Author

David C. O'Gara 2023
