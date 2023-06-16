%{?python_enable_dependency_generator}
%global module_name drat

Name:           python-%{module_name}
Version:        1.0.3
Release:        16%{?dist}
Summary:        A reading text analysis tool

License:        GPL-3.0-or-later
URL:            https://github.com/riverrun/drat
Source0:        %{pypi_source %{module_name}}

BuildArch:      noarch

%global _description\
Drat is a tool that analyzes reading texts and produces a brief report which\
gives a readability score (according to the Dale-Chall readability formula)\
and the number of uncommon words (based on the General Service List) in the\
text. It also lists all of these uncommon words (if you choose the verbose\
option).

%description %_description

%package -n python3-%{module_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{module_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(click)

%description -n python3-%{module_name} %_description

%package -n %{module_name}-tools
Summary:        %{summary}
Requires:       python3-%{module_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{module_name}-tools
drat tool.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n %{module_name}-tools
%doc README.rst
%{_bindir}/drat

%files -n python3-%{module_name}
%doc README.rst
%{python3_sitelib}/%{module_name}/
%{python3_sitelib}/%{module_name}-*.egg-info/

%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.0.3-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Parag Nemade <pnemade AT redhat DOT com> - 1.0.3-14
- Update license tag to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.3-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 13 2019 Parag Nemade <pnemade AT redhat DOT com> - 1.0.3-1
- Update to 1.0.3 version (#1697399)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-16
- Cleanups and improvements in spec

* Wed Sep 12 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-15
- Resolves:rh#1627403: Remove python2-drat subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-13
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.2-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.2-10
- Python 2 binary package renamed to python2-drat
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-2
- Fix drat execution
- require python3-drat

* Sun Oct 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-1
- Update to 0.4.2 release

* Sun Sep 28 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.1-1
- Update to 0.4.1 release

* Mon Sep 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.0-1
- Initial packaging

