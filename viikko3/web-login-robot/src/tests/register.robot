*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  timodeus
    Set Password  timooo123
    Set Password Confirmation  timooo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ti
    Set Password  timooo123
    Set Password Confirmation  timooo123
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  timoodenkku
    Set Password  tipe
    Set Password Confirmation  tipe
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  timoopekka
    Set Password  timbeksoni178
    Set Password Confirmation  timbekzone178
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  timbeossi
    Set Password  timbethesuperman99
    Set Password Confirmation  timbethesuperman99
    Submit Credentials
    Go To Login Page
    Set Username  timbeossi
    Set Password  timbethesuperman99
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  timoooo
    Set Password  moi
    Set Password Confirmation  moi
    Submit Credentials
    Go To Login Page
    Set Username  timoooo
    Set Password  moi
    Submit Login Credentials
    Login Should Fail

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
