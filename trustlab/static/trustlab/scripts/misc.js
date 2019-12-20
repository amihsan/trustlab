/* jshint esversion: 6 */
/*
This file includes miscellaneous JS functions for the trustlab aTLAS.
 */
"use strict";

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function alertMessage(isErrorMsg = false, message = "") {
    const GENERAL_ERROR_MSG = "Something went wrong. Please try again.";
    const GENERAL_SUCCESS_MSG = "Success!"
    if (message === "")
    {
        message = isErrorMsg ? GENERAL_ERROR_MSG: GENERAL_SUCCESS_MSG;
    }
    $("#alert").removeClass()
        .addClass(isErrorMsg ? "alert alert-danger" : "alert alert-success")
        .text(message)
        .fadeIn().delay(2000).fadeOut();
}

function ajaxFunc(url, method, data, successHandler, dataType = "json", contentType = "application/json") {
        $.ajax({
            url: url,
            method: method,
            beforeSend: function (xhr, settings) {
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
                return true;
            },
            dataType: dataType,
            contentType: contentType,
            data: data,
            success: function (result) {
                successHandler(result);
            },
            error: function () {
                alertMessage(true);
            }
        });
    }


