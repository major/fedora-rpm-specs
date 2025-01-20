Name:           python3-saml
Version:        1.16.0
Release:        7%{?dist}
Summary:        Add SAML support to your Python software using this library

License:        MIT
URL:            https://pypi.python.org/pypi/%{name}
Source0:        https://github.com/SAML-Toolkits/python3-saml/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0001:      0001-keep-settings.patch

# Fix build-system in pyproject.toml: use poetry-core
Patch:          https://github.com/SAML-Toolkits/python3-saml/pull/341.patch

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
%generate_buildrequires
%pyproject_buildrequires

%description
This toolkit lets you turn your Python application into a SP
(Service Provider) that can be connected to an IdP (Identity Provider).


%prep
%autosetup -p1


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files onelogin

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Python Maint <python-maint@redhat.com> - 1.16.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Miro Hrončok <mhroncok@redhat.com> - 1.16.0-4
- Drop unneeded build dependencies on poetry, setuptools and wheel

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 04 2023 Kefu Chai <tchaikov@gmail.com> - 1.16.0-1
- Update to 1.16.0.

* Sat Aug 19 2023 Kefu Chai <tchaikov@gmail.com> - 1.15.0-1
- Update to 1.15.0.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 1.14.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Kefu Chai <tchaikov@gmail.com> - 1.14.0-1
- Update to 1.14.0.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.11.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 08 2021 Dan Callaghan <djc@djc.id.au> - 1.11.0-1
- new upstream release 1.11.0 (RHBZ#1916534):
  https://github.com/onelogin/python3-saml/blob/v1.11.0/changelog.md

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-2
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Ken Dreyer <kdreyer@redhat.com> - 1.9.0-1
- Update to 1.9.0 (rhbz#1726650)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0.
- Relax defusedxml requirement. Fixes bug #1723432

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.0-1
- Initial package.
