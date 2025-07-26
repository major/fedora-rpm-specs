%global _description\
Nyx is a command-line monitor for Tor. With this you can get detailed\
real-time information about your relay such as bandwidth usage,\
connections, logs, and much more.

Name: nyx
Version: 2.1.0
Release: 26%{?dist}
Summary: Command-line monitor for Tor
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: https://nyx.torproject.org
Source0: %{pypi_source}
# https://github.com/torproject/nyx/issues/49
Patch0: nyx-2.1.0-replace-inspect.getargspec-usage.patch
BuildArch: noarch
BuildRequires: python3-devel
Suggests: %{name}-doc = %{version}-%{release}
Provides: tor-arm = %{version}-%{release}
Obsoletes: tor-arm <= 1.4.5.0-17
Obsoletes: tor-arm-gui <= 1.4.5.0-17
Obsoletes: tor-arm-devel <= 1.4.5.0-17

%description %_description

%package doc
Summary: %summary

%description doc %_description

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}
install -D -m 0644 nyx.1 %{buildroot}%{_mandir}/man1/nyx.1

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} run_tests.py

%files -f %{pyproject_files}
%{_bindir}/%{name}

%files doc
%doc web
%{_mandir}/man1/nyx.1*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
