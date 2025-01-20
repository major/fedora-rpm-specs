%global srcname pyvmomi

%global desc %{expand:
pyVmomi is the Python SDK for the vSphere API that allows you to manage\
ESX, ESXi, and vCenter.}

Name:           python-%{srcname}
Version:        8.0.3.0.1
Release:        2%{?dist}
Summary:        vSphere Python SDK
License:        Apache-2.0
URL:            https://github.com/vmware/%{srcname}
Source0:        %{pypi_source}

# FIXME python validator does not like any explicit version
# upstream issue#735, rhbz#1763484
# drop useless doublication of dependency generation
Patch0:         00-test-requirements.patch
BuildArch:      noarch

%description %desc


%package -n     python3-%{srcname}
Summary:        vSphere SDK for Python3
BuildRequires:  python3-devel
BuildRequires:  dos2unix

%description -n python3-%{srcname} %desc


%prep
%autosetup -n %{srcname}-%{version} -p1

# fix line endings
find . -name '*' -exec dos2unix -o {} \;

# shebang fix
find . -name '*.py' -exec sed -i 's@/usr/bin/env python@@' {} \;

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyVmomi pyVim vsanapiutils vsanmgmtObjects


%check
# Temporarily reverting unit tests due to pyvcr version...
# %%tox
%pyproject_check_import -t


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 14 2024 Robby Callicotte <rcallicotte@fedoraproject.org> - 8.0.3.0.1-1
- Rebased to version 8.0.3.0.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 7.0.3-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Raphael Groner <raphgro@fedoraproject.org> - 7.0.3-9
- support deprecation of ssl.wrap_socket 

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 7.0.3-7
- Rebuilt for Python 3.12

* Tue Jun 20 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 7.0.3-6
- Updated spec to new packaging standards
- Updated license field to use SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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

