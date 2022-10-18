import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Flask!'
    
    def test_get_shows(self, api):
        res = api.get('/shows')
        assert res.status == '200 OK'
        assert len(res.json) == 5

    def test_get_show(self, api):
        res = api.get('/shows/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'House Of The Dragon'

    def test_get_shows_error(self, api):
        res = api.get('/shows/57')
        assert res.status == '400 BAD REQUEST'
        assert "show with id 57" in res.json['message']

    def test_post_shows(self, api):
        mock_data = json.dumps({'name': 'Molly'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/shows', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 6

    def test_patch_show(self, api):
        mock_data = json.dumps({'name': 'Molly'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.patch('/shows/2', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2
        assert res.json['name'] == 'Molly'

    def test_delete_show(self, api):
        res = api.delete('/shows/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'oops' in res.json['message']
