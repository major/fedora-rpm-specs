%global debug_package %{nil}

Name:		stats-collect
Version:	1.0.6
Release:	%autorelease
Summary:	A tool for collecting and visualising system statistics and telemetry

License:	BSD-3-Clause
Url:		https://github.com/intel/stats-collect
Source0:	%url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	web-assets-devel
Provides:	bundled(lit) = 2.2.8
Requires:	web-assets-filesystem
Requires:	wult%{?_isa} >= 1.11.21

%description
The Statistics Collection Tool project provides the 'stats-collect'
command-line tool. This tool collects system statistics and telemetry,
and visualizes them. It’s for debugging and tracing purposes only.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files statscollectlibs statscollecttools
install -pDm644 docs/man1/stats-collect.1 %{buildroot}/%{_mandir}/man1/stats-collect.1

%check
STATS_COLLECT_WEB_ASSETS_PATH=%{buildroot}%{_jsdir}/%{name} STATS_COLLECT_DATA_PATH=%{buildroot}%{_datadir}/%{name} %pytest -v

%files -n %{name} -f %{pyproject_files}
%license js/dist/main.js.LICENSE.txt
%doc CHANGELOG.md README.md security.md
%{_bindir}/ipmi-helper
%{_bindir}/stats-collect
%{_bindir}/stc-agent
%{_datadir}/%{name}
%{_jsdir}/%{name}
%{_mandir}/man1/stats-collect.1*

%changelog
%autochangelog
