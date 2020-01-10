/* jshint esversion: 6 */
/*
This file includes the business logic and workflow for a user-agent surfing aTLAS.
 */
"use strict";

function openSpecifyScenarioCard() {
    $("#c-start").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function openSpecifyScenarioCardFromResults() {
    $("#c-results").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function openLabRuntimeCard() {
    let scenarioName = $("#selector-scenario").children("option:selected").val();
    if (scenarioName !== "")
    {
        console.log(scenarioName);
    }
    else
    {
        errorInSelector($("#selector-scenario"));
        snackMessage(true);
    }
    $("#c-scenario").addClass("not-displayed");
    $("#c-runtime").removeClass("not-displayed");
    setTimeout(function(){
        $("#c-runtime").addClass("not-displayed");
        $("#c-results").removeClass("not-displayed");
    }, 2000);
}

function showScenarioDescription() {
    let value = $(this).children("option:selected").val();
    $(".scenario-ul:not(.not-displayed)").addClass("not-displayed")
    $(".scenario-ul[data-scenario='"+value+"']").removeClass("not-displayed");
}


//OnClick Events
$("#btn-specify-scenario").click(openSpecifyScenarioCard);
$("#btn-run-scenario").click(openLabRuntimeCard);
$("#btn-specify-scenario2").click(openSpecifyScenarioCardFromResults);
$("#selector-scenario").change(showScenarioDescription);


