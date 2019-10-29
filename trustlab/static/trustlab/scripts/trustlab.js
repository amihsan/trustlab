"use strict";

function openSpecifyScenarioCard() {
    $("#c-start").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function openSpecifyScenarioCard2() {
    $("#c-results").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function openLabRuntimeCard() {
    $("#c-scenario").addClass("not-displayed");
    $("#c-runtime").removeClass("not-displayed");
    setTimeout(function(){
        $("#c-runtime").addClass("not-displayed");
        $("#c-results").removeClass("not-displayed");
    }, 2000);
}

function showScenarioDescription() {
    var val = $(this).children("option:selected").val();
    $(".scenario-ul:not(.not-displayed)").addClass("not-displayed")
    $(".scenario-ul[data-scenario='"+val+"']").removeClass("not-displayed");
}


//OnClick Events
$("#btn-specify-scenario").click(openSpecifyScenarioCard);
$("#btn-run-scenario").click(openLabRuntimeCard);
$("#btn-specify-scenario2").click(openSpecifyScenarioCard2);
$("#selector-scenario").change(showScenarioDescription);


