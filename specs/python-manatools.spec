%global module manatools

Name:           python-%{module}
Version:        0.99.0
Release:        1%{?dist}

Summary:        A Python framework to build ManaTools applications
License:        LGPL-2.1-or-later
URL:            https://github.com/manatools/python-manatools
Source0:        https://github.com/manatools/python-manatools/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Python ManaTools aim is to help in writing tools to be collected
under the ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%package -n python3-%{module}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{module}}
Recommends:     (python3dist(python-%{name}[qt]) if qt6-qtbase-gui)
Recommends:     (python3dist(python-%{name}[gtk]) if gtk4)

%description -n python3-%{module}
Python ManaTools aim is to help in writing tools to be collected
under the ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%pyproject_extras_subpkg -n python3-%{module} qt
%pyproject_extras_subpkg -n python3-%{module} gtk

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{module}
%doc README.md NEWS
%license LICENSE
%{python3_sitelib}/%{module}/
%{python3_sitelib}/python_manatools-%{version}.dist-info/

%changelog
* Fri Apr 24 2026 Neal Gompa <ngompa@fedoraproject.org> - 0.99.0-1
- Rebase to 0.99.0

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.0.4-16
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.0.4-15
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.0.4-13
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.4-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.0.4-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.4-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.4-2
- Rebuilt for Python 3.11

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.0.4-1
- Version 0.0.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.3-1
- Initial package

