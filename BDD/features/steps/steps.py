from behave import given, when, then
from steps import calcular_media

@given('que eu tenho dois números')
def step_impl(context):
    context.numero1 = 10
    context.numero2 = 20

@when('eu calculo a média desses números')
def step_impl(context):
    context.media = calcular_media(context.numero1, context.numero2)

@then('eu devo obter a média correta')
def step_impl(context):
    assert context.media == 15