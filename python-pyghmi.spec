%global sname pyghmi
%global common_summary Python General Hardware Management Initiative (IPMI and others)

%global common_desc This is a pure Python implementation of IPMI protocol. \
\
The included pyghmicons and pyghmiutil scripts demonstrate how one may \
incorporate the pyghmi library into a Python application.

%global common_desc_tests Tests for the pyghmi library

# Enable python3 build in fedora and rhel>7 and python2 only for rhel=7
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%global with_python2 0
%else
%global with_python3 0
%global with_python2 1
%endif

Summary: %{common_summary}
Name: python-%{sname}
Version: %{?version:%{version}}%{!?version:1.5.29}
Release: 4%{?dist}
Source0: https://tarballs.opendev.org/x/%{sname}/%{sname}-%{version}.tar.gz
License: ASL 2.0
Prefix: %{_prefix}
BuildArch: noarch
Url: https://opendev.org/x/pyghmi

%description
%{common_desc}

%if 0%{?with_python2}
%package -n python2-%{sname}
Summary: %{common_summary}
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires: python2-devel
BuildRequires: python2-pbr
BuildRequires: python2-setuptools

Requires: python2-cryptography >= 2.1
Requires: python2-six >= 1.10.0
Requires: python2-dateutil >= 2.6.1

%description -n python2-%{sname}
%{common_desc}

%package -n python2-%{sname}-tests
Summary: %{common_desc_tests}
Requires: python2-%{sname} = %{version}-%{release}

%description -n python2-%{sname}-tests
%{common_desc_tests}

%endif # with_python2

%if 0%{?with_python3}

%package -n python3-%{sname}
Summary: %{common_summary}
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools

Requires: python3-cryptography >= 2.1
Requires: python3-six >= 1.10.0
Requires: python3-dateutil >= 2.6.1

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: %{common_desc_tests}
Requires: python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
%{common_desc_tests}

%endif # with_python3

%package -n python-%{sname}-doc
Summary: The pyghmi library documentation

%if 0%{?with_python2}
BuildRequires: python2-sphinx
BuildRequires: python2-openstackdocstheme
%else
BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme
%endif

%description -n python-%{sname}-doc
Documentation for the pyghmi library

%prep
%setup -qn %{sname}-%{version}
# NOTE(dtantsur): pyghmi is actual fine with older dateutil, 2.8.1 is missing
# from both Fedora and CentOS currently. See
# https://bugzilla.redhat.com/show_bug.cgi?id=1835084
sed -i 's/python-dateutil.*/python-dateutil>=2.6.1/' requirements.txt

%build
%if 0%{?with_python3}
%py3_build
%{__python3} setup.py build_sphinx -b html
%endif # with_python3

%if 0%{?with_python2}
%py2_build
%{__python2} setup.py build_sphinx -b html
%endif

# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install

# rename python3 binary
pushd %{buildroot}/%{_bindir}
mv pyghmicons pyghmicons-%{python3_version}
ln -s pyghmicons-%{python3_version} pyghmicons-3
ln -s pyghmicons-3 pyghmicons
mv pyghmiutil pyghmiutil-%{python3_version}
ln -s pyghmiutil-%{python3_version} pyghmiutil-3
ln -s pyghmiutil-3 pyghmiutil
mv virshbmc virshbmc-%{python3_version}
ln -s virshbmc-%{python3_version} virshbmc-3
ln -s virshbmc-3 virshbmc
popd

%endif # with_python3

%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%{_bindir}/pyghmicons*
%{_bindir}/pyghmiutil*
%{_bindir}/virshbmc*
%{_bindir}/fakebmc
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests
%endif # with_python3

%if 0%{?with_python2}
%files -n python2-%{sname}
%license LICENSE
%{_bindir}/pyghmicons
%{_bindir}/pyghmiutil
%{_bindir}/virshbmc
%{_bindir}/fakebmc
%{python2_sitelib}/%{sname}
%{python2_sitelib}/%{sname}-*.egg-info
%exclude %{python2_sitelib}/%{sname}/tests

%files -n python2-%{sname}-tests
%license LICENSE
%{python2_sitelib}/%{sname}/tests
%endif

%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.md

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.5.29-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Joel Capitao <jcapitao@redhat.com> - 1.5.29-1
- Update to 1.5.29.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.19-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Joel Capitao <jcapitao@redhat.com> - 1.5.19-1
- Updated to 1.5.19.

* Sun Aug 30 2020 Dmitry Tantsur <divius.inside@gmail.com> - 1.5.16-1
- Updated to 1.5.16.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Dmitry Tantsur <divius.inside@gmail.com> - 1.5.14-4
- Relax dateutil requirement in requirement.txt as well (#1835084)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.14-3
- Rebuilt for Python 3.9

* Wed May 13 2020 Yatin Karel <ykarel@redhat.com> - 1.5.14-2
- Fix typo in requirements

* Mon May 11 2020 Yatin Karel <ykarel@redhat.com> - 1.5.14-1
- Updated to 1.5.14.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.16-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.16-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.2.16-1
- Updated to 1.2.16.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Aug 14 2018 Ilya Etingof <etingof@gmail.com> - 1.2.4-3
- Added Python 3 build

* Mon Aug 13 2018 Ilya Etingof <etingof@gmail.com> - 1.2.4-1
- Upstream 1.2.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.22-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.22-1
- Upstream 1.0.22

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.12-4
- Python 2 binary package renamed to python2-pyghmi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Lucas Alvares Gomes <lucasagomes@gmail.com> - 1.0.12-1
- Rebased to 1.0.12

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Lucas Alvares Gomes <lucasagomes@gmail.com> - 0.8.0-1
- Rebased to 0.8.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Lucas Alvares Gomes <lucasagomes@gmail.com> - 0.5.9-1
- Initial package.
