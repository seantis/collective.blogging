/* FANCYBOX */

jq(document).ready(function () {
    jq(".blogNewsImageContainer a, .blogImageContainer a")
        .prepOverlay({
            subtype:'image',
            urlmatch:'/image_view_fullscreen$',
            urlreplace:'_large'
    });
});

/* GALLERY */

jq(document).ready(function () {
    jq("div.scrollable").scrollable();
    
    jq("div.galleryItems img").click(function() { 

        // calclulate large image's URL based on the thumbnail URL (flickr specific)
        imgel = jq(this)
        var url = imgel.attr("src").replace("_thumb", "_preview");
        var url_full = imgel.attr("src").replace("_thumb", "_view_fullscreen");
        var title = imgel.attr("alt");
        var desc = imgel.attr("title");

        // get handle to element that wraps the image and make it semitransparent 
        var wrap = jq("#image_wrap").fadeTo("medium", 0.5); 

        // the large image from flickr 
        var img = new Image(); 

        // call this function after it's loaded 
        img.onload = function() {

            // make wrapper fully visible 
            wrap.fadeTo("fast", 1); 

            // change the image 
            wrap.find("img").attr("src", url); 

        }; 

        img.src = url;
        var img_link = jq("div.imageTitle a");
        img_link.html(title);
        img_link.attr("href", url_full);
        img_link.attr("title", desc);

    // when page loads simulate a "click" on the first image 
    }).filter(":first").click();
    
});

/* BLOG VIEW */

/* filter toolbar */
var bloggingEmptyHash = (new Date()).getTime()
var bloggingLastHash = '';

function bloggingMonitorHash() {
    var param = window.location.hash;
    if(bloggingLastHash!=param) {
        var url = window.location.href;
        if(url.indexOf('#')>-1) {
            url = url.substring(0, url.indexOf('#'));
        }
        jq('#content').load(url + '?' + param.substring(1) + ' #content>div', bloggingFilterToolbar);
        bloggingLastHash = param;
    }
}

function bloggingFilterToolbar() {
    jq("#filter-blog-form input[name=collective.blog.filter]").click(function(event) {
        // stop default click of button
        event.preventDefault();
        event.stopPropagation();
        // feedback for user
        jq('body').css('cursor', 'wait');
        // get button, form and data
        var button = jQuery(event.target);
        var form = button.closest('form');
        var url = form.attr('action');
        var param = form.serialize();
        // update url with proper hash
        window.location.hash = param;
    });
    
    jq('#collective-blog-clearfilter').click(function(event) {
        // stop default click of button
        event.preventDefault();
        event.stopPropagation();
        // feedback for user
        jq('body').css('cursor', 'wait');
        // get link and url
        var link = jQuery(event.target);
        var url = link.attr('href');
        // update url with no hash
        window.location.hash = bloggingEmptyHash;
    });
    // reset feedback for user
    jq('body').css('cursor', 'auto');
}

function bloggingPreloadFilter() {
    var form = jq('#filter-blog-form');
    var hash = window.location.hash;
    
    if (hash!='') {
        hash = hash.substring(1);
    }
    var params = hash.split('&');
    jQuery.each(params, function(idx, pair) {
        var field_name = pair.split('=')[0];
        var field_value = pair.split('=')[1];
        form.find('[name=' + field_name + ']').val(field_value);
    });
}
jq(document).ready(function () {
    bloggingFilterToolbar();
    bloggingPreloadFilter();
    setInterval(bloggingMonitorHash, 100);
});


