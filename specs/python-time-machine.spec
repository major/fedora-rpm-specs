Name:           python-time-machine
Version:        2.16.0
Release:        %autorelease
Summary:        Travel through time in your Python tests
License:        MIT
URL:            https://github.com/adamchainz/time-machine
Source:         %{url}/archive/%{version}/time-machine-%{version}.tar.gz

# Fix date.today() for Python 3.15+
# https://github.com/adamchainz/time-machine/pull/618
Patch:          python315-date-today.patch

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
A Python library that allows to travel in time and freeze it as well.
Includes a test-function decorator that sets time to an arbitrary value.}

%description %_description

%package -n     python3-time-machine
Summary:        %{summary}

%description -n python3-time-machine %_description


%prep
%autosetup -p1 -n time-machine-%{version}
sed -i '/coverage/d' tests/requirements/requirements.in


%generate_buildrequires
# tox uses a pinned version of requirements/requirements.in and also uses coverage
# so we bypass it.
# This also saves us one dependency cycle as tox uses time-machine for tests.
%pyproject_buildrequires tests/requirements/requirements.in


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files time_machine _time_machine


%check
%pytest -v


%files -n python3-time-machine -f %{pyproject_files}
%doc README.rst HISTORY.rst


%changelog
%autochangelog
