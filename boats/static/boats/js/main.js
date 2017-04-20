(function($) {
  $('img').load(function() {
    $("#status").fadeOut("slow"); 
    $("#preloader").delay(50).fadeOut("slow").remove();      

  }) 

  if($("html").hasClass('ie8')) {
  	$("#hero").backstretch("images/hero-bg.jpg");  	
  	$("#page-title").backstretch("images/hero-bg.jpg");	
  } 

  setTimeout(function() {
    $('#page-title h1').fitText(1, { minFontSize: '38px', maxFontSize: '54px' });
  }, 100);

  $(window).on('scroll', function() {
	var h = $('header').height();
	var y = $(window).scrollTop();
    var header = $('#main-header');

	if ((y > h + 30 ) && ($(window).outerWidth() > 768 ) ) {
	  header.addClass('opaque');
	}
    else {
      if (y < h + 30) {
        header.removeClass('opaque');
      }
      else {
        header.addClass('opaque');
      }
    }

  });

  $('.alert-box').on('click', '.close', function() {
    $(this).parent().fadeOut(500);
  });	

  var menu_icon = $("<span class='menu-icon'></span>");
  var toggle_button = $("<a>", {                         
                        id: "toggle-btn", 
                        html : "<span class='menu-text'>Menu</span>",
                        title: "Menu",
                        href : "#" } 
                        );
  var nav_wrap = $('nav#nav-wrap')
  var nav = $("ul#nav");  
   
  nav_wrap.find('a.mobile-btn').remove(); 
  toggle_button.append(menu_icon); 
  nav_wrap.prepend(toggle_button); 

  toggle_button.on("click", function(e) {
    e.preventDefault();
    nav.slideToggle("fast");     
  });

  if (toggle_button.is(':visible')) nav.addClass('mobile');

  $(window).resize(function() {
    if (toggle_button.is(':visible')) nav.addClass('mobile');
  	else nav.removeClass('mobile');
  });

  $('ul#nav li a').on("click", function() {      
    if (nav.hasClass('mobile')) nav.fadeOut('fast');      
  });

  $('.smoothscroll').on('click', function (e) {
    e.preventDefault();

   	var target = this.hash,
    $target = $(target);

    $('html, body').stop().animate({
      'scrollTop': $target.offset().top
    }, 800, 'swing', 
      function () {
        window.location.hash = target;
    });

  });

  var sections = $("section"),
  navigation_links = $("#nav-wrap a");

  if($("body").hasClass('homepage')) {

    sections.waypoint( {

	  handler: function(event, direction) {

	    var active_section;

		active_section = $(this);
		if (direction === "up") active_section = active_section.prev();

		var active_link = $('#nav-wrap a[href="#' + active_section.attr("id") + '"]');

	    navigation_links.parent().removeClass("current");
		active_link.parent().addClass("current");

	  },
	  offset: '25%'
	});
  }

   /*----------------------------------------------------*/
  	/* Flexslider
  	/*----------------------------------------------------*/
  $('img').load(function() {  		

    $('#hero-slider').flexslider({
	  namespace: "flex-",
	  controlsContainer: ".flex-container",
	  animation: 'fade',
	  controlNav: true,
	  directionNav: false,
	  smoothHeight: true,
	  slideshowSpeed: 7000,
	  animationSpeed: 600,
	  randomize: false
	});	   

  });

 
	/*----------------------------------------------------*/
	/*	contact form
	------------------------------------------------------*/

    $('form#contactForm button.submit').on('click', function() {
      $('#image-loader').fadeIn();
      $.ajax({
	    type: "POST",
	    url: "/",
        data: $('form#contactForm').serialize(),
	    success: function(msg) {
          // Message was sent
          if (msg == 'OK') {
            $('#image-loader').fadeOut();
            $('#message-warning').hide();
            $('#contactForm').fadeOut();
            $('#message-success').fadeIn();   
            ga('send', 'event', 'contact', 'submit');
          }
            // There was an error
          else {
            $('#image-loader').fadeOut();
            $('#message-warning').html(msg);
	        $('#message-warning').fadeIn();
          }
	    }
      });
      return false;
   });


  /*-----------------------------------------------------*/
  /* Back to top
  ------------------------------------------------------ */ 
  var pxShow = 300; // height on which the button will show
  var fadeInTime = 400; // how slow/fast you want the button to show
  var fadeOutTime = 400; // how slow/fast you want the button to hide
  var scrollSpeed = 300; // how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'

   // Show or hide the sticky footer button
  jQuery(window).scroll(function() {

	if (jQuery(window).scrollTop() >= pxShow) {
	  jQuery("#go-top").fadeIn(fadeInTime);
	} else {
	  jQuery("#go-top").fadeOut(fadeOutTime);
	}

  }); 


})(jQuery);
