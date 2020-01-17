/* jshint esversion: 6 */
/*
This file includes the business logic and workflow for a user-agent surfing aTLAS.
 */

function openSpecifyScenarioCard() {
    $("#c-start").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function openSpecifyScenarioCardFromResults() {
    $("#c-results").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function startLabRuntime() {
    let scenarioSelector = $("#selector-scenario");
    let scenarioName = scenarioSelector.children("option:selected").val();
    if (scenarioName !== "")
    {
        let scenario = scenarios.filter(scenario => scenario.name === scenarioName)[0];
        ajaxFunc(INDEX_URL,"PUT", JSON.stringify(scenario), openLabRuntimeCard, "html");
    }
    else
    {
        errorInTextfield(scenarioSelector);
        snackMessage(true);
    }
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
    let value = $("#selector-scenario").children("option:selected").val();
    $(".scenario-ul:not(.not-displayed)").addClass("not-displayed");
    $(".scenario-ul[data-scenario='"+value+"']").removeClass("not-displayed");
}


//OnClick Events
$("#btn-specify-scenario").click(openSpecifyScenarioCard);
$("#btn-run-scenario").click(startLabRuntime);
$("#btn-specify-scenario2").click(openSpecifyScenarioCardFromResults);
$("#selector-scenario").change(showScenarioDescription);


