%{?python_disable_dependency_generator}

%if 0%{?rhel} >= 7
%global with_python3 1
%global skip_tests 1
%else
# generally disable python2, maybe as legacy for older rhel <= 6
#%%global with_python2 1
%endif
%if 0%{?fedora}
%global with_python3 1
%endif

%global srcname pyvmomi

%global desc \
pyVmomi is the Python SDK for the vSphere API that allows you to manage\
ESX, ESXi, and vCenter.

Name:           python-%{srcname}
Version:        7.0.3
Release:        4%{?dist}
Summary:        vSphere Python SDK
License:        ASL 2.0
URL:            https://github.com/vmware/%{srcname}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%desc

%if %{with python3}
%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        vSphere SDK for Python%{python3_other_version}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-six

Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-six

# test dependencies
%if !0%{?skip_tests}
BuildRequires:  python%{python3_pkgversion}-testtools >= 0.9.34
BuildRequires:  python%{python3_pkgversion}-vcrpy
BuildRequires:  python%{python3_pkgversion}-yarl
BuildRequires:  python%{python3_pkgversion}-fixtures
BuildRequires:  python%{python3_pkgversion}-tox
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       python%{python3_pkgversion}-pyvim

%description -n python%{python3_pkgversion}-%{srcname}
%desc
This package is for Python3 version %{python3_version} only.

%if 0%{?python3_other_pkgversion}
%package -n     python%{python3_other_pkgversion}-%{srcname}
Summary:        vSphere SDK for Python%{python3_other_version}
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-requests
BuildRequires:  python%{python3_other_pkgversion}-six

Requires:       python%{python3_other_pkgversion}-requests
Requires:       python%{python3_other_pkgversion}-six

# test dependencies
%if !0%{?skip_tests}
BuildRequires:  python%{python3_other_pkgversion}-testtools >= 0.9.34
BuildRequires:  python%{python3_other_pkgversion}-vcrpy
BuildRequires:  python%{python3_other_pkgversion}-yarl
BuildRequires:  python%{python3_other_pkgversion}-fixtures
BuildRequires:  python%{python3_other_pkgversion}-tox
%endif

%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}
Provides:       python%{python3_other_pkgversion}-pyvim

%description -n python%{python3_other_pkgversion}-%{srcname}
%desc
This package is for Python3 version %{python3_other_version} only.
%endif
%endif

##### begin legacy python2
%if 0%{?with_python2}
%package -n     python2-%{srcname}
Summary:        vSphere Python SDK
BuildRequires:  python2-devel
# FIXME add proper version suffixes of python subpackages
BuildRequires:  python%{?!rhel:2}-testtools
BuildRequires:  python%{?!rhel:2}-vcrpy
BuildRequires:  python2-setuptools
BuildRequires:  python2-requests
BuildRequires:  python2-six
BuildRequires:  python%{?!rhel:2}-fixtures
BuildRequires:  python%{?!rhel:2}-tox
%{?python_provide:%python_provide python2-%{srcname}}
Provides:       python2-pyvim

%description -n python2-%{srcname}
%desc
This package is for Python version 2.
%endif
##### end legacy python2


%prep
%autosetup -n %{srcname}-%{version}
# FIXME python validator does not like any explicit version
# upstream issue#735, rhbz#1763484
# drop useless doublication of dependency generation
find -name \*requirements.txt -exec cp -v /dev/null '{}' \;


%build
%{?with_python3: %py3_build}
%{?python3_other_pkgversion: %py3_other_build}

##### begin legacy python2
%{?with_python2: %py2_build}
##### end legacy python2


%install
%{?with_python3: %py3_install}
%{?python3_other_pkgversion: %py3_other_install}

##### begin legacy python2
%{?with_python2: %py2_install}
##### end legacy python2

find %{buildroot} -name requires.txt -print -delete


%check
%if !0%{?skip_tests}
%{?with_python3: %{__python3} setup.py test}
%{?python3_other_pkgversion: %{__python3_other} setup.py test}
%endif

##### begin legacy python2
%{?with_python2: %{__python2} setup.py test}
##### end legacy python2


%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/pyVmomi
%{python3_sitelib}/pyVim
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%endif

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_other_sitelib}/pyVmomi
%{python3_other_sitelib}/pyVim
%{python3_other_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%endif

##### begin legacy python2
%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/pyVmomi
%{python2_sitelib}/pyVim
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%endif
##### end legacy python2


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 7.0.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Raphael Groner <raphgro@fedoraproject.org> - 7.0.3-1
- bump to v7.0.3 (7.0U3 APIs) 

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Raphael Groner <raphgro@fedoraproject.org> - 7.0.2-1
- bump to v7.0.2 (7.0U2 APIs)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Raphael Groner <raphgro@fedoraproject.org> - 7.0.1-1
- bump to v7.0.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.7.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Raphael Groner <projects.rg@smart.ms> - 6.7.3-3
- rebuilt for vcpry>=2 etc., rhbz#1763484
- avoid duplication of dependency generation
- [epel] try to enable tests for python3, still WIP

* Fri Sep 13 2019 Raphael Groner <projects.rg@smart.ms> - 6.7.3-2
- [epel7] disable support for python2 due to failing tests

* Fri Sep 06 2019 Raphael Groner <projects.rg@smart.ms> - 6.7.3-1
- new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.7.1-6
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 6.7.1-5
- drop brand

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 6.7.1-3
- [epel7] Rebuilt to change main python from 3.4 to 3.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Raphael Groner <projects.rg@smart.ms> - 6.7.1-2
- fix dependencies

* Wed Oct 31 2018 Raphael Groner <projects.rg@smart.ms> - 6.7.1-1
- new version
- introduce dependency generator
- use github for release tarball, due to pypi provides zip only
- drop duplicate README.rst, tests are obsolete
- add python3 subpackages for epel7, readd python2 but epel7 only

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.5-10
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.5-8
- Rebuilt for Python 3.7

* Wed Mar 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 6.5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 05 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 6.5-4
- Fix build adding yarl build deps 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 6.5-2
- Rebuild for Python 3.6

* Tue Dec 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 6.5-1
- Update to 6.5

* Thu Sep 08 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 6.0.0.2016.6-1
- Update to version 6.0.0.2016.6
- Simplify the SPEC file

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.2014.1.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0.2014.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.2014.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.2014.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Michael Rice <michael@michaelrice.org> - 5.5.0.2014.1.1-3
- Changed spec to work on EPEL

* Thu Sep 18 2014 Michael Rice <michael@michaelrice.org> - 5.5.0.2014.1.1-2
- Changes to spec from review suggestions

* Sun Aug 31 2014 Michael Rice <michael@michaelrice.org> - 5.5.0.2014.1.1-1
- Bugfix release from upstream.

* Fri Aug 22 2014 Michael Rice <michael@michaelrice.org> - 5.5.0.2014.1-2
- Changes to spec file based on bugzilla package review.

* Wed Aug 20 2014 Michael Rice <michael@michaelrice.org> - 5.5.0.2014.1-1
- Initial RPM build.

