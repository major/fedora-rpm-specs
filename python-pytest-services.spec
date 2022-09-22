%global srcname pytest-services
%global forgeurl https://github.com/pytest-dev/%{srcname}

Name:           python-%{srcname}
Version:        2.2.1
Release:        %autorelease
Summary:        Services plugin for pytest
License:        MIT
URL:            %{forgeurl}
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  memcached

%global common_description %{expand:
This plugin provides a set of fixtures and utility functions to start service
processes for your tests with pytest.}

%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# we don't care about upstream's PEP8 lint checks
# (and need to port it to flake8 if we do)
sed -i '/^pytest-pep8$/d' requirements-testing.txt

%generate_buildrequires
# not using -t as tox.ini has extra cruft
%pyproject_buildrequires -r requirements-testing.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_services


%check
k="$(awk 'NR>1 {pre=" and " } { printf "%snot %s", pre, $0 }' <<EOF
test_mysql
test_xvfb
EOF
)"
%pytest -k "${k}"


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc AUTHORS.rst CHANGES.rst README.rst


%changelog
%autochangelog
