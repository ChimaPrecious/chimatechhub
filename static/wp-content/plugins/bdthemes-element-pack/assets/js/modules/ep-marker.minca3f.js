!function(t,e){"use strict";var n=function(t,e){var n=t.find(".bdt-marker-wrapper");if(n.length){var o=n.find("> .bdt-tippy-tooltip"),r=t.data("id");o.each((function(t){tippy(this,{allowHTML:!0,theme:"bdt-tippy-"+r})}))}};jQuery(window).on("elementor/frontend/init",(function(){elementorFrontend.hooks.addAction("frontend/element_ready/bdt-marker.default",n)}))}(jQuery,window.elementorFrontend);