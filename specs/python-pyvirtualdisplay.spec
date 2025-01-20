Name:           python-pyvirtualdisplay
Version:        3.0
Release:        2%{?dist}
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc

License:        BSD-2-Clause
URL:            https://github.com/ponty/PyVirtualDisplay
Source0:        %{url}/archive/%{version}/PyVirtualDisplay-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# For Tests
BuildRequires:  xmessage
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  xorg-x11-server-Xvfb

%global _description %{expand:
pyvirtualdisplay is a python wrapper for Xvfb, Xephyr and Xvnc}

%description %_description

%package -n     python3-pyvirtualdisplay
Summary:        %{summary}

Requires:       %{py3_dist py}
Requires:       xorg-x11-server-Xvfb
%description -n python3-pyvirtualdisplay %_description

%prep
%autosetup -n PyVirtualDisplay-%{version}
# TODO: package entrypoint2 and vncdotool and enable these tests
rm tests/test_race.py
rm tests/test_xvnc.py
sed -i -E -e '/^(types-pillow|entrypoint2|vncdotool=.*)$/d' requirements-test.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyvirtualdisplay

%check
%tox


%files -n python3-pyvirtualdisplay -f %{pyproject_files}
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Scott Talbert <swt@techie.net> - 3.0-1
- Update to new upstream release 3.0
- Update License tag to use SPDX identifiers
- Modernize Python packaging

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.2-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Scott Talbert <swt@techie.net> - 2.2-1
- Update to new upstream release 2.2 to fix FTBFS (#1987889)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1-2
- Rebuilt for Python 3.10

* Sat Feb 13 2021 Scott Talbert <swt@techie.net> - 2.1-1
- Initial package
