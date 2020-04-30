[![Build Status](https://travis-ci.org/jonnytdavies/waste-recycle-MS4.svg?branch=master)](https://travis-ci.org/jonnytdavies/waste-recycle-MS4)

# Junk To Your Trunk - Code Institute Milestone Project 4

You can view the running project on Heroku [here](https://junk-to-your-trunk.herokuapp.com/)
## Junk To Your Trunk Full-Stack E-commerce Website
This project is based on a newfound passion of my Father’s to reduce waste. He is focusing on corporate sustainability and finding ways to reduce commercial waste, particularly waste materials that are usually sent to landfill. The purpose of this website is to create a platform where people who have waste materials, such as brick and wood can post to the community to find out if anyone else has a use for such materials before they pay for them to be sent to landfill.

This also has a benefit to anyone who uses such materials to make new things, so anyone can search their local area to see if there are building sites or factories that are throwing away materials that would benefit their own projects.

Off the back of this, profits would become donations that would be given to charities that promote sustainability. This way we might be able to create a cycle and reduce overall landfill to protect our planet.

### UX
Wireframes can be found [here](https://github.com/jonnytdavies/waste-recycle-MS4/tree/master/wireframes). 

Since beginning development on the site and understanding how elements worked together in practical terms, some elements of my original designs have changed, however the frames are very much the same

This website is built predominantly for manual labourers who have waste materials to dispose of, and for people who are looking to repurpose the same materials that these labourers are discarding.

- I am a builder with lots of old bricks that I don’t need.
    1. I want to be able to get rid of them, but I am concerned about them going into landfill
    2.  I need a way to publicly list the materials I have to find out if there is anyone who can repurpose them.


-   I am a hobbyist who likes to build furniture out of offcuts and old pieces of wood
    1. I don’t have a big budget to source new materials, and like to repurpose materials instead of using new ones.
    2. I need a place where I can find such materials locally to me.


###  User Story
- I am a builder looking to post online the unused bricks from my most recent project
    1. Upon loading the website, I need to see an obvious place to make a listing.
    2. I see there are some instructions for sellers, and I am told I need to register to the site before posting.
    3. I register, login, and then see that in the menu a new item has popped up that says ‘Create Listing’
    4. I click on it and am taken to a page where I can add the details of the bricks I have and no longer need.
    5. I want to add a photo so the potential buyer can have an idea of what they’re going to be receiving.
    6. I add a photo, submit the form and am redirected to the listings page, where I can see my listing has been successfully posted.

-   I am someone who wants to build a fire pit in my garden for the summer and want to make it out of bricks.
    1. Since it will become charred, I am not concerned about using new bricks.
    2. I want to be able to find someone local to me who has old bricks that I can use.
    3. I load the Junk To Your Trunk website and immediately see on a carousel a listing for bricks near where I live.
    4. I create an account, add the listing to my cart and checkout.
### Junk To Your Trunk - UX Brief
#### Strategy:

I am aiming to produce a simple and well structured e-commerce site that is intuitive to the user.
It will be responsive to all devices and browsers
It will successfully take payments


#### Scope:

It will be able to:
-   Showcase what listings are on the website
-   Take payments from a user
-   Display search results based on location

Users will be able to:
1.  Create a user and edit their profile information
2.  Reset forgotten passwords
3.  List items for sale
4.  Purchase items
#### Structure / Skeleton:


The website will include multiple pages:

-   Home
    1. Showcase some of the listings on the website
    2. Give the user information about the purpose of the website and how to use it

-   Register
    1. Allow the user to register a user

-   Login
    1.  Allow the user to login to their account that they registered
    2. Reset their password if they forgot it

-   Profile
    1.  Allow the user to view their profile information and edit it

-   Create a Listing
    1.  This page will allow a logged in user to list something for sale

-   All Listings
    1.  This page will give users the opportunity to see all the listings on the website.

-   Cart
    1.  This will allow users to view items they have added to their carts and proceed to the checkout

-   Checkout
    1. This will allow users to pay for their chosen listings.

The website will have the same header and footer on every page

-   Header will include:
    1. Search bar
    2. Login link (if not logged in)
    3. Register link (if not logged in)
    4. Profile (if logged in)
    5. Logout link (if logged in)
    6. Create listing link (if logged in)
    7. All Listings link (if logged in)
    8. Cart link (if logged in)

-   Footer will include:
    1.  Short menu:
        -   Home, Profile, Terms and Conditions
    2.  Social Media Icons (Will be unlinked as no pages set up, but have the potential to be)
    3. Support details


#### Surface:
-   Colour Scheme: The colour scheme has been inspired by the colour of cement and will be #FFDEB6. It will be complimented by black, and the two will be interchanged consistently throughout the site. I think it is important not to use too many colours and allow a user to associate this colour combination with this site.

-   Font Family
'Anton’ (Google Fonts) - Heavily weighted and easy to read font that gives the site a bit of character

-   Images:
The images will be ones found online, and will demonstrate what is being sold in the listing
#### Features
#### Existing Features
-   The Header - allows the users to navigate the website by having clear links to the other pages within the website. It is dynamic in that it changes depending on a user’s level of authorisation (logged in or not).

-   The Footer - gives the user some simple navigation and information.

-   Authentication - User can register, login and change their password and other profile information

-   Create listing - users can create a listing for other users to purchase

-   All listings - users can view all listings in specific locations

-   Cart - users can view which items they added to their carts

-   Checkout - users can checkout and pay for their chosen items

#### Features Left to Implement
If I had more time I would create an order history page. Since I had less than a week to build this project I didn’t have time before deadline to organise such a feature.

Storing user cart sessions. This has frustrated me and I tried many things, but I was unsuccessful in allowing a user to store their cart sessions, so if they log out then the items in their cart are removed. A positive is that if a user doesn’t log out but leaves the site, then the items are still there when they come back.

With more time I would add functionality so that a buyer can communicate with the seller to arrange picking up what they have purchased.

#### Technologies Used

**HTML5**

I used HTML5, as it is the base of every website.

**CSS**

I used CSS to style my HTML code, to create a global design scheme, and make the website visually appealing for users.

**[Django](https://www.djangoproject.com/)**

I used Django as the framework to build my site.

**[Bootstrap](https://getbootstrap.com/)**

I used Bootstrap’s grid layout to divide my page into sections, which helped keep content in order and evenly spaced around the site. I also made use of some of its predefined styles, mainly for the buttons, form layouts and carousel.

**[Font Awesome](https://fontawesome.com/icons?d=gallery)**

I used Font-Awesome for icons

### Testing
-   Registration:
I went to ‘Register’ page
Entered my details to sign up
When valid data was entered, a user was created and I received a success message
When invalid data was entered I received correct error messages.

-   Login:
    1. After registering I went to the login page and entered the details for the user I just created
    2. With the correct details, I successfully logged in and was redirected to the homepage
    3. With incorrect details entered I was given the correct error message to say I entered invalid details

-   Profile:
    1. I went to the Profile page and could see my user details.
    2. I clicked on ‘Edit Profile’
    3. I was taken to a new page where I could enter a new email address and username. I changed them and successfully saved my new details.
    4. There was an option to reset the password, so I followed that link and successfully changed my password.
    5. I then logged out and tried to log back in with my new details, which was successful.

- Logout:
    1. When logged in, I clicked the button to logout, and I was successfully logged out. I also saw a message to notify me that logging out had been successful.
    2. The Navigation changed which links it had correctly to show ‘Login’ and ‘Register’

-   Create listing
    1. I went to the create listing page via the link that only appears in the navigation when logged in.
    2. I entered details as if I were a user with a genuine listing, I uploaded a photo and pressed ‘Post Listing’. I was successfully redirected to a page which showed all listings on the site, which included mine that I had just made.

- Add to cart

    1. From an individual listing page I clicked the button ‘Add to cart’, which successfully redirected me to the cart page, which showed the item I added was in there.

- Checkout
    1. From the cart, I clicked ‘Checkout’ when I had added an item to it, and I was taken to the checkout page.
    2. I saw the total amount to pay had been correctly calculated and entered my address details. I then added the test stripe cards to pay, and clicked ‘Make Payment’
    3. I was redirected to the homepage, where I saw a success message telling me that my purchase was successful

Overall when filling in forms the site correctly notified me if I hadn’t filled in a required form, and wouldn’t let me submit any forms if required data was missing.

A bug I have found is that Stripe do not allow any payments below the value of £0.30. This caused an issue for me, because I had hoped people would be able to list things for free on the site. A way around this in the future would be to let sellers and buyers communicate before any purchase has been made, so if no payment is required they don’t need to go through Stripe’s payment system.

I have used Travis to test my code, and as of final deployment, everything is running without any issues.
### Responsiveness
Using the chrome inspector tool, I tested different screen sizes, to see how the menu would respond. Because I have built the site using Bootstrap’s grid system it successfully responds at every breakpoint to resize content, and there are never any clashes of content.

I set a fixed size for images in the listing preview cards so that they all remain a uniform size. I also truncated the descriptions to be no longer than 15 words on these cards for the same reason.

I am happy with the way my navbar responds to smaller screen sizes and becomes a burger menu. This is powered by a Bootstrap Navbar combined with jQuery. Initially I had wanted the searchbar to be outside the burger menu when on mobile, but attempts to move it outside presented multiple complications that I haven’t yet had time to fix.


**All tests were done individually on Firefox, Chrome, Safari on Mac and iOS, and returned the same results. I have been unable to test Edge and Internet Explorer, or any browsers on PC.**
### Deployment
This website has been deployed using Heroku, and can be found running [here](https://junk-to-your-trunk.herokuapp.com/)

For more details on how to deploy a site to Heroku see this [video](https://www.youtube.com/watch?time_continue=4&v=XQcdS9mx97E&feature=emb_title)

#### Credits
The structure to a lot of this website came from what I learnt in the Code Institute lessons. Particular note must go to them for the accounts app, checkout and cart.

##### Content
The pictures that are in listings I have made came from [Unsplash](https://unsplash.com/)


##### Acknowledgements
I’d like to give credit to my Father for helping me come up with the concept for this website.
Thanks goes to the tutors who were able to point me in the right direction to solutions for the bugs I was having in my code.
