define(["require","framework/controllers/PageController","framework/globalEventManager","framework/Util","jquery","app/libs/CustomSelectBox","app/view-controllers/SearchViewController"],function(e){var t=e("framework/controllers/PageController"),n=e("framework/globalEventManager"),r=e("framework/Util"),i=e("jquery"),s=e("app/libs/CustomSelectBox"),o=e("app/view-controllers/SearchViewController"),u=t.extend({constructor:function(e,t){this.base(e,t);var n=r.Cookie.get("language__name"),o=i(".js-custom-select");if(o.length){var u=new s(o);u.on("optionChanged",this._onOptionChanged.bind(this)),u.setOption(n)}return this},_initReferences:function(e){this.base(e);var t=this._references;t.$userImage=i(".js-user-image"),t.$userDropDown=i(".js-user-dropdown"),t.$userDropDownArrow=i(".js-user-dropdown-arrow");var n=i(".js-search-wrapper");t.searchViewController=new o(n),t.$feedbackModal=i(".js-modal"),t.$smileyClick=i(".js-smiley-click"),t.$submitForm=i(".js-submit-form")},_initEvents:function(){this.base();var e=this._references,t=this._boundFunctions;t.onUserImageClick=this._onUserImageClick.bind(this),e.$userImage.on("click",t.onUserImageClick),t.onSmileyClick=this._onSmileyClick.bind(this),e.$smileyClick.on("click",t.onSmileyClick),t.onSubmitClick=this._onSubmitClick.bind(this),e.$submitForm.on("click",t.onSubmitClick)},_onOptionChanged:function(e){r.Cookie.set("language__name",e),n.trigger("languageChanged",e)},_onUserImageClick:function(e){e.preventDefault(),this._references.$userDropDown.toggle(),this._references.$userDropDownArrow.toggle(),$("html, body").animate({scrollTop:0},"slow")},_onSmileyClick:function(e){e.preventDefault(),$(".selected").removeClass("selected");var t=$(e.currentTarget);t.addClass("selected"),this._references.$feedbackModal.removeClass("comment-survey")},_onSubmitClick:function(){var e=$("#comments").val(),t=$("#email").val(),n=$("#csrftoken").val(),r=$(".selected"),i=r.attr("data");return $.ajax({url:"/feedbacksubmit_json",type:"POST",dataType:"json",data:{comments:e,email:t,rating:i},success:function(e){$("#result").append("ServerResponse:"+e.server_response),location.href="#close"},error:function(e,t,n){alert(e.status+": "+e.responseText),location.href="#close"}}),!1},destroy:function(){this.base()}});return u});