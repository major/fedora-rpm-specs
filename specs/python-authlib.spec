%bcond tests 1
%bcond tests_clients %{undefined rhel}
%bcond tests_flask %{undefined rhel}
%bcond tests_django %{undefined rhel}
%bcond tests_jose %{undefined rhel}

Name:           python-authlib
Version:        1.4.0
Release:        %autorelease
Summary:        Build OAuth and OpenID Connect servers in Python

License:        BSD-3-Clause
URL:            https://github.com/lepture/authlib
Source0:        %{url}/archive/v%{version}/authlib-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python library for building OAuth and OpenID Connect servers. JWS, JWK, JWA,
JWT are included.}

%description %_description

%package -n     python3-authlib
Summary:        %{summary}

%description -n python3-authlib %_description


%prep
%autosetup -p1 -n authlib-%{version}

# Remove OAuth 1 tests, because they require support for SHA1.
sed -i '/tests\.django\.test_oauth1/d' tests/django/settings.py
rm -rf \
  tests/django/test_oauth1 \
  tests/flask/test_oauth1 \
  tests/clients/test_requests/test_oauth1_session.py \
  tests/clients/test_httpx/test_oauth1_client.py

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i '/coverage/d' tests/requirements-base.txt
sed -i 's/coverage run --source=authlib -p -m pytest/python3 -m pytest/' tox.ini


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-e %{toxenv}%{?with_tests_clients:,%{toxenv}-clients}%{?with_tests_flask:,%{toxenv}-flask}%{?with_tests_django:,%{toxenv}-django}%{?with_tests_jose:,%{toxenv}-jose}}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files authlib


%check
%if %{with tests}
%tox
%endif
# for import check, we exclude modules with optional dependencies:
%pyproject_check_import -e '*django*' -e '*flask*' -e '*httpx*' -e '*requests*' -e '*sqla*' -e '*starlette*'


%files -n python3-authlib -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
