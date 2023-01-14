%global sum Python Task Warrior library

%global forgeurl https://github.com/GothenburgBitFactory/tasklib


Name:           python-tasklib
Version:        2.5.1
Release:        %autorelease
Summary:        %{sum}

License:        MIT

URL:            %{forgeurl}
%global tag  %{version}
%forgemeta
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3-pytest
BuildRequires:  task >= 2.4


%description
tasklib is a Python library for interacting with taskwarrior databases, using a
queryset API similar to that of Django's ORM.

Supports Python 3.5+, taskwarrior 2.4+.
Older versions of taskwarrior are untested and may not work.

%package -n python3-tasklib
Summary:        %{sum}
Requires:       task >= 2.4

%description -n python3-tasklib
tasklib is a Python library for interacting with taskwarrior databases, using a
queryset API similar to that of Django's ORM.

Supports Python 3.5+, taskwarrior 2.4+.
Older versions of taskwarrior are untested and may not work.


%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tasklib

%check
%pytest tasklib/tests.py
%pyproject_check_import

%files -n python3-tasklib -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
