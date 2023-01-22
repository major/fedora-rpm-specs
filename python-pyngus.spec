%global srcname pyngus
%global proton_minimum_version 0.28.0

# Don't duplicate the same documentation
%global _docdir_fmt %{name}

Name:          python-%{srcname}
Version:       2.3.0
Release:       14%{?dist}
Summary:       Callback API implemented over Proton

License:       ASL 2.0
URL:           https://github.com/kgiusti/%{srcname}
Source0:       %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:     noarch

%global _description \
A connection oriented messaging framework using QPID Proton.\
It provides a callback-based API for message passing.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qpid-proton >= %{proton_minimum_version}
Requires:       python3-qpid-proton >= %{proton_minimum_version}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
#  PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} test-runner || :
#popd

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Irina Boverman <iboverma@redhat.com> - 2.3.0-1
- Rebased to 2.3.0

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-4
- Subpackage python2-pyngus has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Irina Boverman <iboverma@redhat.com> - 2.2.4-2
- Added python2-pyngus

* Tue Jul 24 2018 Irina Boverman <iboverma@redhat.com> - 2.2.4-1
- Rebased to 2.2.4
- Removed python2-pyngus

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-2
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Irina Boverman <iboverma@redhat.com> - 2.2.2-1
- Rebased to 2.2.2

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Irina Boverman <iboverma@redhat.com> - 2.2.1-3
- Rebuilt against qpid-proton 0.18.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Irina Boverman <iboverma@redhat.com> - 2.2.1-1
- Rebased to 2.2.1

* Mon Feb 20 2017 Irina Boverman <iboverma@redhat.com> - 2.1.4-1
- Rebased to 2.1.4
- Rebuilt against qpid-proton 0.17.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuild for Python 3.6

* Thu Sep  8 2016 Irina Boverman <iboverma@redhat.com> - 2.1.2-2
- Rebuilt against qpid-proton 0.14.0

* Thu Sep 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Thu Sep 01 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Aug  9 2016 Irina Boverman <iboverma@redhat.com> - 2.0.4-1
- Rebased to 2.0.4
- Rebuilt against proton 0.13.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 24 2016 Irina Boverman <iboverma@redhat.com> - 2.0.3-5
- Rebuilt against qpid-proton 0.13.0

* Mon May 16 2016 Philip Worrall <philip.worrall@googlemail.com> - 2.0.3-4
- Add python3 subpackage (http://fedora.portingdb.xyz/pkg/python-pyngus/)
- Edit spec to use the python2/3 specific installation macros
- Add global macros for package name and summary
- Add calls to run the testsuite
- Point the source url at the upstream github repository (for license files)

* Wed Mar 23 2016 Irina Boverman <iboverma@redhat.com> - 2.0.3-3
- Rebuilt against qpid-proton 0.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Irina Boverman <iboverma@redhat.com> - 2.0.3-1
- Rebased to 2.0.3

* Thu Sep  3 2015 Irina Boverman <iboverma@redhat.com> - 2.0.1-1
- Rebased to 2.0.1
- Rebuilt against proton 0.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.2.0-1
- Rebased on Pyngus 1.2.0.

* Wed Oct  1 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-1
- First official build.

* Mon Sep 29 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-0.1
- Replaced the python-qpid-proton requirement.
- Added egg info to the list of docs for this package.

* Thu Sep 25 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-0
- Initial build.
