def test_get_account_balance(api_client):
    response = api_client.get_account_balance()
    assert 'accountType' in response and 'balances' in response
    assert len(response['balances']) > 0, 'Account Balance not found'
    assert response["canWithdraw"] == True, 'Account can not withdraw'
    assert response["canTrade"] == True, 'Account can not trade'