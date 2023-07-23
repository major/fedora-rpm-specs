%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%if 0%{?fedora} && 0%{?fedora} <= 31
%bcond_without python2
%else
%bcond_with python2
%endif

Name:           python-scales
Version:        1.0.9
Release:        16%{?dist}
Summary:        Stats for Python processes

License:        ASL 2.0
URL:            https://github.com/Cue/scales
Source0:        %{url}/archive/%{version}.tar.gz

# https://github.com/Cue/scales/pull/47
Patch0:         fix_py38_compatibility.patch

BuildArch:      noarch

%if %with python2
BuildRequires:  python2-devel
BuildRequires:  python2-six
BuildRequires:  python2-simplejson
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools
%endif
%if %with python3
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-simplejson
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools
%endif

%global _description\
Tracks server state and statistics, allowing you to see what your server is\
doing. It can also send metrics to Graphite for graphing or to a file for crash\
forensics.\


%description %_description

%if %with python2
%package -n python2-scales
Summary: %summary
Requires:       python2-six
Requires:       python2-simplejson
%{?python_provide:%python_provide python2-scales}

%description -n python2-scales %_description
%endif

%if %with python3
%package -n python3-scales
Summary:        Stats for Python 3 processes
Requires:       python3-six
Requires:       python3-simplejson

%description -n python3-scales %_description
%endif


%prep
%setup -q -n scales-%{version}
%patch0 -p1
# Python 3.11 compatibility
sed -i "s/self.assertEquals/self.assertEqual/g" \
    src/greplin/scales/scales_test.py \
    src/greplin/scales/aggregation_test.py \
    src/greplin/scales/formats_test.py

%if %with python3
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%if %with python2
%{__python2} setup.py build
%endif

%if %with python3
cd %{py3dir}
%{__python3} setup.py build
%endif



%install
%if %with python2
%{__python2} setup.py install --skip-build --root %{buildroot}
%endif

%if %with python3
cd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif


%check
%if %with python2
%{__python2} setup.py test
%endif

%if %with python3
cd %{py3dir}
%{__python3} setup.py test
%endif


%if %with python2
%files -n python2-scales
%{python2_sitelib}/greplin/
%{python2_sitelib}/scales*.egg-info/
%{python2_sitelib}/scales*.pth
%doc AUTHORS LICENSE README.md
%endif


%if %with python3
%files -n python3-scales
%{python3_sitelib}/greplin/
%{python3_sitelib}/scales*.egg-info
%{python3_sitelib}/scales*.pth
%doc AUTHORS LICENSE README.md
%endif


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.0.9-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.9-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 18 2021 Lumír Balhar <lbalhar@redhat.com> - 1.0.9-10
- Fix compatibility with Python 3.11

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.9-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Lumír Balhar <lbalhar@redhat.com> - 1.0.9-3
- Python 2 subpackage disabled for Fedora <32

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Lumír Balhar <lbalhar@redhat.com> - 1.0.9-1
- New upstream version 1.0.9
- Fixed compatibility with Python 3.8 (bz#1716527)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-15
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.5-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Troy Dawson <tdawson@redhat.com> - 1.0.5-12
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.5-11
- Python 2 binary package renamed to python2-scales
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 23 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.0.5-1
- Update to 1.0.5
- Add Python 3 support
- Run tests

* Thu Mar 27 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.0.3-1
- Initial packaging
