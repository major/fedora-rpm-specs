Name:           python-pytest-xvfb
Version:        3.0.0
Release:        2%{?dist}
Summary:        A pytest plugin to run Xvfb for tests

License:        MIT
URL:            https://github.com/The-Compiler/pytest-xvfb
Source0:        %{url}/archive/v%{version}/pytest-xvfb-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-tkinter
BuildRequires:  tigervnc-server-minimal
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  xorg-x11-xauth

%global _description %{expand:
With Xvfb and the plugin installed, your testsuite automatically runs with
Xvfb. This allows tests to be run without windows popping up during GUI tests
or on systems without a display (like a CI).

If Xvfb is not installed, the plugin does not run and your tests will still
work as normal. However, a warning message will print to standard output
letting you know that Xvfb is not installed.

If you're currently using xvfb-run in something like .travis.yml, simply remove
it and install this plugin instead - then you'll also have the benefits of Xvfb
locally.}

%description %_description

%package -n     python3-pytest-xvfb
Summary:        %{summary}

%description -n python3-pytest-xvfb %_description

%prep
%autosetup -n pytest-xvfb-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_xvfb

%check
%pytest


%files -n python3-pytest-xvfb -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Scott Talbert <swt@techie.net> - 3.0.0-1
- Update to new upstream release 3.0.0
- Update License tag to use SPDX identifiers
- Modernize Python packaging

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.0.0-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.10

* Sat Feb 13 2021 Scott Talbert <swt@techie.net> - 2.0.0-1
- Initial package
