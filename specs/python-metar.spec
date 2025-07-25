%global srcname metar
%global summary Coded METAR and SPECI weather reports parser for Python
%global packagezipfile python-metar-20250512git-d87ebdf.zip

Name: python-%{srcname}
Version: 1.11.0
Release: 20250513git%{?dist}
Summary: %{summary}

# This software uses the BSD-Source-Code license
# (but without the second condition on use of names of contributors)
License: BSD-Source-Code

URL: https://github.com/python-metar/python-metar

# note that development was moved to a new github account
# the old account was: http://github.com/tomp/python-metar
# see also this discussion on the 2 project names:
# https://github.com/python-metar/python-metar/issues/58

# releases are at pypi
# Source: https://files.pythonhosted.org/packages/source/m/%%{srcname}/%%{srcname}-%%{version}.tar.gz

# but the latest release does not contain a pyproject.toml file
# so cannot easily be build with the new pyproject macros.
# Therefore a snapshot from github is used in stead:
Source:  https://github.com/python-%{srcname}/python-%{srcname}/archive/d87ebdf3049cb542fb3a94f470dca37821378e91.zip#/%{packagezipfile}

BuildArch: noarch

BuildRequires: python3-devel python3-pytest

%global _description \
Python-metar is a python package for interpreting METAR and SPECI coded \
weather reports.  METAR (Meteorological Aerodrome Report) and SPECI (Specials) \
are reports containing airport weather information encoded in ASCII \
following standards set by WMO (World Meteorological Organization) \
and ICAO (International Civil Aviation Organization).

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python-%{srcname}}

%description -n python3-%{srcname} %_description

%prep

cd %{_builddir}
unzip %{_sourcedir}/%{packagezipfile}
mv python-metar-main python-%{srcname}-%{version}

%generate_buildrequires

cd %{_builddir}/python-%{srcname}-%{version}
%pyproject_buildrequires

%build

cd %{_builddir}/python-%{srcname}-%{version}
%pyproject_wheel

%install

cd %{_builddir}/python-%{srcname}-%{version}
%pyproject_install

# remove executable permissions from sample.py to
# prevent dependencies being pulled in from this file
chmod 644 sample.py

%check

cd %{_builddir}/python-%{srcname}-%{version}
%{__python3} -m pytest -v

%files -n python3-%{srcname}

%doc python-%{srcname}-%{version}/sample.py
%doc python-%{srcname}-%{version}/README.md
%doc python-%{srcname}-%{version}/CHANGELOG.md
%doc python-%{srcname}-%{version}/LICENSE

%{python3_sitelib}/%{srcname}
%{python3_sitelib}/python_%{srcname}*dist-info

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-20250513git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Jos de Kloe <josdekloe@gmail.com> 1.11.0-20250512git
- adapt spec file to use the new pyproject macros

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1.11.0-7
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.11.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Jos de Kloe <josdekloe@gmail.com> 1.11.0-1
- new upstream version 1.11.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.12

* Sat May 20 2023 Jos de Kloe <josdekloe@gmail.com> 1.10.0-1
- new upstream version 1.10.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Jos de Kloe <josdekloe@gmail.com> 1.9.0-3
- SPDX migration: change BSD to BSD-Source-Code

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jos de Kloe <josdekloe@gmail.com> 1.9.0-1
- new upstream version 1.9.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.8.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Jos de Kloe <josdekloe@gmail.com> 1.8.0-1
- new upstream version 1.8.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild


* Thu Mar 07 2019 Jos de Kloe <josdekloe@gmail.com> 1.7.0-1
- new upstream version and remove python2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Jos de Kloe <josdekloe@gmail.com> 1.6.0-1
- new upstream version and disable python2 sub-package for f30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Jos de Kloe <josdekloe@gmail.com> 1.5.0-3
- undo spec file name change since this seems not allowed

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Jos de Kloe <josdekloe@gmail.com> 1.5.0-1
- new upstream version and adapt to generate python2 and python3 versions

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Oct 08 2015 Jos de Kloe <josdekloe@gmail.com> 1.4.0-1
- Update to new upstream version and simplified spec file
- Add check section and run provided tests

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.0-4
- Rebuild for Python 2.6

* Thu Apr 24 2008 Matthias Saou <http://freshrpms.net/> 1.3.0-3
- Include everything under sitelib, to include egg files if present (F-9+).

* Tue Mar 27 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-2
- Include nobang patch.

* Fri Feb  9 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-1
- Initial RPM release.

