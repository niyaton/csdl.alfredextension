from csdl.open import get_conference_page_url
from csdl.open import get_conference_page_url_by_year
from csdl.open import open_url

def test_get_conference_page_url():
    url = get_conference_page_url('ase')
    assert url == 'http://www.computer.org/csdl/proceedings/ase/index.html'

def test_get_conference_page_by_url():
    url = get_conference_page_url_by_year('ase', 2000)
    assert url == 'http://www.computer.org/csdl/proceedings/ase/2000/0710/00/index.html'

def test_open_url():
    open_url('http://www.google.co.jp')
