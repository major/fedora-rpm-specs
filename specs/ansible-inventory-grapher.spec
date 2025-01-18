%global archive_name ansible-inventory-grapher
%global lib_name ansibleinventorygrapher

Name:           %{archive_name}
Version:        2.6.0
Release:        2%{?dist}
Summary:        Creates graphs representing ansible inventory

License:        GPL-3.0-or-later
URL:            https://github.com/willthames/ansible-inventory-grapher
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
ansible-inventory-grapher creates a dot file suitable for use by graphviz.\

%description %_description

%package -n python3-%{archive_name}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  (ansible-core or ansible)
Requires:       (ansible-core or ansible)

%description  -n python3-%{archive_name} %_description

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{lib_name}
ln -sr %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3

%check
%pytest -vv

%files -n python3-%{archive_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-3

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 Parag Nemade <pnemade AT redhat DOT com> - 2.6.0-1
- Update to 2.6.0 version (#2307515)
- Use pyproject macros
- Drop python2 subpackage as its not compatible with new python packaging

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.5.0-19
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.5.0-15
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Parag Nemade <pnemade AT redhat DOT com> - 2.5.0-13
- Update package to use SPDX expression license

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.5.0-11
- Rebuilt for Python 3.11

* Thu Feb 03 2022 Maxwell G <gotmax@e.email> - 2.5.0-10
- Allow users to choose between ansible and ansible-core.
- Make compliant with SourceURL Guidelines.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Parag Nemade <pnemade AT redhat DOT com> - 2.5.0-8
- Resolves:rhbz#2040942 - Change package requirement from ansible-python3 to ansible

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.5.0-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Parag Nemade <pnemade AT redhat DOT com> - 2.5.0-1
- Update to 2.5.0 version (#1747773)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.5-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.4.5-4
- Drop python2 subpackage in F29+

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.5-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.4.5-1
- Update to 2.4.5 version (#1535260)

* Tue Dec 12 2017 Jan Beran <jberan@redhat.com> - 2.4.4-2
- Python 2 binary package renamed to python2-ansible-inventory-grapher
- Python 3 subpackage

* Tue Nov 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.4-1
- Update to 2.4.4 version (#1514766)

* Wed Nov 08 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.2-1
- Update to 2.4.2 version (#1510677)

* Mon Nov 06 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.1-1
- Update to 2.4.1 version (#1509732)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Parag Nemade <pnemade AT redhat DOT com> - 2.4.0-1
- Update to 2.4.0 version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.2-1
- Update to 2.3.2

* Thu Jul 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.1-1
- Update to 2.3.1

* Mon Jul 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.0-1
- Update to 2.3.0

* Sun Jul 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-1
- Update to 2.2.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-2
- Use github source that provided license and test files

* Mon May 09 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-1
- Update to 2.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-2
- Rename to ansible-inventory-grapher

* Sat Oct 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- Update to 1.0.1

* Thu Sep 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging

