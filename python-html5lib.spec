Name:           python-html5lib
Summary:        A python based HTML parser/tokenizer
Version:        1.1
Release:        %autorelease
Epoch:          1
License:        MIT
URL:            https://github.com/html5lib/html5lib-python
Source:         %{pypi_source html5lib}

# Fix compatibility with pytest 6
Patch:          %{url}/pull/506.patch
# Fix compatibility with pytest 7.4.0
Patch:          %{url}/pull/573.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Test deps
# Upstream uses requirements-test.txt but it has tox, coverage, mock, flake8 in it
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-expect)

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.


%package -n python3-html5lib
Summary:        %{summary}

%description -n python3-html5lib
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.

%pyproject_extras_subpkg -n python3-html5lib lxml genshi chardet all


%prep
%autosetup -p1 -n html5lib-%{version}

# Use standard library unittest.mock instead of 3rd party mock
# From https://github.com/html5lib/html5lib-python/pull/536
sed -i 's/from mock import/from unittest.mock import/' html5lib/tests/test_meta.py


%generate_buildrequires
%pyproject_buildrequires -x all

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files html5lib


%check
%pytest


%files -n python3-html5lib -f %{pyproject_files}
%doc CHANGES.rst README.rst


%changelog
%autochangelog
