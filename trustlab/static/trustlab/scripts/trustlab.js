/* jshint esversion: 6 */
/*
This file includes the business logic and workflow for a user-agent surfing aTLAS.
 */

let scenarioSelector = $("#selector-scenario");
let labSocket;

function openLabSocket() {
    labSocket = new WebSocket('ws://' + window.location.host + LAB_URL);
    labSocket.onmessage = onLabSocketMessage;
    labSocket.onclose = onLabSocketClose;
}

function onLabSocketClose(closingEvent){
    console.error('Lab socket closed unexpectedly!');
}

function onLabSocketMessage(messageEvent){
    let data = JSON.parse(messageEvent.data);
    if (data.type === "scenario_results") {
        $("#trust_log").text(data.trust_log);
        let agents_log = JSON.parse(data.agents_log);
        let agents_log_end = $("#agents_log_end");
        let currentRunId = data.scenario_run_id;
        for (const [key, value] of Object.entries(agents_log)) {
            agents_log_end.before(`<p class="agent_log">Agent '${key}' trust log:</p>`);
            agents_log_end.before(`<pre id="agent_log_${key}" class="agent_log">${value}</pre>`);
        }
        if (inRuntimeState()) {
            history.pushState(null, null, '#' + currentRunId);
            $("#c-runtime").addClass("not-displayed");
            $("#c-results").removeClass("not-displayed");
        } else if (inGetResultsState()) {
            $("#c-loadingResults").addClass("not-displayed");
            $("#c-results").removeClass("not-displayed");
        }
    } else if (data.type === "scenario_run_id") {
        let baseURL = window.location.href.split('#')[0];
        let currentRunId = data.scenario_run_id;
        let currentRunUrl = baseURL + '#' + currentRunId;
        let idCopyField = $("#scenario_run_id_copyField");
        let urlCopyField = $("#scenario_run_url_copyField");
        idCopyField.val(currentRunId);
        idCopyField.parent().addClass("is-dirty");
        urlCopyField.val(currentRunUrl);
        urlCopyField.parent().addClass("is-dirty");
    } else if (data.type === "scenario_result_not_found") {
        cancelScenarioResults();
        snackMessage(true, "Scenario Result not found");
    } else if (data.type === "error") {
        snackMessage(true, data.message);
    }
}

function startLabRuntime() {
    let scenarioName = scenarioSelector.children("option:selected").val();
    if (scenarioName !== "")
    {
        let scenario = scenarios.filter(scenario => scenario.name === scenarioName)[0];
        let scenarioMessage = {'type': 'run_scenario', 'scenario': scenario};
        waitForSocketConnection(labSocket, function(){
            labSocket.send(JSON.stringify(scenarioMessage));
            openLabRuntimeCard();
        }, function(){
            snackMessage(true, "No socket connection ready");
            openLabSocket();
        });
    }
    else
    {
        errorInTextfield(scenarioSelector);
        snackMessage(true);
    }
}

function sendScenarioRunIdForResults(scenarioRunId) {
    waitForSocketConnection(labSocket, function(){
        let scenarioResultMessage = {'type': 'get_scenario_results', 'scenario_run_id': scenarioRunId};
        labSocket.send(JSON.stringify(scenarioResultMessage));
    }, function(){
        snackMessage(true, "No socket connection ready, automatic retry");
        openLabSocket();
        if (inGetResultsState()) {
            sendScenarioRunIdForResults(scenarioRunId);
        }
    });
}

function openSpecifyScenarioCard() {
    $("#c-start").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function openSpecifyScenarioCardFromResults() {
    $(".agent_log").remove();
    $("#c-results").addClass("not-displayed");
    $("#c-scenario").removeClass("not-displayed");
}

function openLabRuntimeCard() {
    $("#c-scenario").addClass("not-displayed");
    $("#c-runtime").removeClass("not-displayed");
}

function showScenarioDescription() {
    let value = scenarioSelector.children("option:selected").val();
    $(".scenario-ul:not(.not-displayed)").addClass("not-displayed");
    $(".scenario-ul[data-scenario='"+value+"']").removeClass("not-displayed");
}

function cancelScenarioResults() {
    $("#c-loadingResults").addClass("not-displayed");
    $("#c-start").removeClass("not-displayed");
    if(window.location.hash) {
        history.pushState(null, null, '#');
    }
}

function inGetResultsState() {
    return !$("#c-loadingResults").hasClass("not-displayed");
}

function inRuntimeState() {
    return !$("#c-runtime").hasClass("not-displayed");
}


//OnClick Events
$("#btn-specify-scenario").click(openSpecifyScenarioCard);
$("#btn-run-scenario").click(startLabRuntime);
$("#btn-specify-scenario2").click(openSpecifyScenarioCardFromResults);
$("#btn-cancel-scenario-results").click(cancelScenarioResults);
scenarioSelector.change(showScenarioDescription);

$( document ).ready(function() {
    openLabSocket();
    if(window.location.hash) {
        let hash = window.location.hash.substring(1);
        if (hash.startsWith("scenarioRun_")) {
            $("#c-start").addClass("not-displayed");
            $("#c-loadingResults").removeClass("not-displayed");
            sendScenarioRunIdForResults(hash);
        }
        // TODO: add functionality to catch unknown url fragments or rather scenarioRunIds
    }
});



