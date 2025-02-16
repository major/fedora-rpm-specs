%global forgeurl https://github.com/ngine-io/cs
Version:        3.3.1
%forgemeta

Name:           python-cs
Release:        %autorelease
Summary:        A simple, yet powerful CloudStack API client for python and the command-line

License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

# Remove pytest-runner
# https://github.com/ngine-io/cs/pull/141
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:          %{forgeurl}/pull/141.patch

BuildArch:      noarch

%global _description %{expand:
A simple, yet powerful CloudStack API client for python and the command-line.

* Async support.
* All present and future CloudStack API calls and parameters are supported.
* Syntax highlight in the command-line client if Pygments is installed.}

%description %_description

%package -n python3-cs
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
# clearsilver also wants to install the cs executable, the upstream is dead,
# Fedora package is probably used by someone, python3-cs is modern, and conflicts are unlikely.
Conflicts: clearsilver

%description -n python3-cs %_description

%pyproject_extras_subpkg -n python3-cs async highlight

%prep
%forgeautosetup


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files cs


%check
%pytest -c /dev/null tests.py


%files -n python3-cs -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/cs


%changelog
%autochangelog
