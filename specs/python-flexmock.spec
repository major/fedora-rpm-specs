Name:           python-flexmock
Version:        0.12.2
Release:        %autorelease
Summary:        Testing library that makes it easy to create mocks, stubs and fakes

License:        BSD-2-Clause-Views

URL:            https://flexmock.readthedocs.org
Source0:        https://github.com/flexmock/flexmock/archive/v%{version}/flexmock-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# Test-only dep
# https://github.com/flexmock/flexmock/blob/54401b5a138e9216bb7eb258cb80cdb1f78e8519/tox.ini#L37
BuildRequires:  /usr/bin/subunit2pyunit

%global _description\
Flexmock is a testing library for Python that makes it easy to create mocks,\
stubs and fakes. The API is inspired by a Ruby library of the same name, but\
Python flexmock is not a clone of the Ruby version. It omits a number of\
redundancies in the Ruby flexmock API, alters some defaults, and introduces\
a number of Python-only features.\

%description %_description


%package -n python3-flexmock
Summary:        %{summary}

%{?python_provide:%python_provide python3-flexmock}

%description -n python3-flexmock %_description


%prep
%autosetup -p1 -n flexmock-%{version}
# teamcity-messages package not yet available in Fedora
sed -i "/teamcity-messages$/d" tox.ini
sed -i "/test_teamcity.py$/d" tox.ini
# Upstream manipulates PYTHONPATH which breaks testing
sed -i "/setenv = PYTHONPATH/d" tox.ini


%generate_buildrequires
%pyproject_buildrequires -r -e %{toxenv}-pytest-latest


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flexmock


%check
PYTHONPATH=.:%{buildroot}/%{python3_sitelib} %tox

# Remove misplaced files
rm -rf %{buildroot}/%{python3_sitelib}/{LICENSE,docs,*.md,tests}


%files -n python3-flexmock -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md docs/

%changelog
%autochangelog
