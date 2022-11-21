*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  simo  simonsalis123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  si  sipetin99
    Output Should Contain  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  sipetin  sipe99
    Output Should Contain  Password should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sipetin  sipettimensalis
    Output Should Contain  Password should contain at least one number

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command