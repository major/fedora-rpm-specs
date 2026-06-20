%global srcname nagiosplugin

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
License:        ZPL-2.1
Summary:        Library for writing Nagios (Icinga) plugins

URL:            https://nagiosplugin.readthedocs.io
Source:         https://github.com/mpounsett/nagiosplugin/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:	python3-devel
BuildRequires:	python3-pytest

BuildArch:      noarch

%global _description %{expand:
nagiosplugin is a Python class library which helps writing Nagios (or Icinga)
compatible plugins easily in Python. It cares for much of the boilerplate
code and default logic commonly found in Nagios checks, including:

- Nagios 3 Plugin API compliant parameters and output formatting
- Full Nagios range syntax support
- Automatic threshold checking
- Multiple independend measures
- Custom status line to communicate the main point quickly
- Long output and performance data
- Timeout handling
- Persistent “cookies” to retain state information between check runs
- Resume log file processing at the point where the last run left}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nagiosplugin

%check
%pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.txt

%changelog
%autochangelog
