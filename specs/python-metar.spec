%global srcname metar
%global summary Coded METAR and SPECI weather reports parser for Python

Name: python-%{srcname}
Version: 2.0.1
Release: 1%{?dist}
Summary: %{summary}

# This software uses the BSD-Source-Code license
# (but without the second condition on use of names of contributors)
License: BSD-1-Clause

URL: https://github.com/python-metar/python-metar

# note that development was moved to a new github account
# the old account was: http://github.com/tomp/python-metar
# see also this discussion on the 2 project names:
# https://github.com/python-metar/python-metar/issues/58

# releases are at pypi (https://pypi.org/project/metar/)
Source: https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel python3-pytest

%global _description \
  Python-metar is a python package for interpreting METAR and SPECI coded \
  weather reports. \
  \
  METAR and SPECI are coded aviation weather reports. The official coding \
  schemes are specified in the World Meteorological Organization (WMO) Manual \
  on Codes, vol I.1, Part A (WMO-306 I.i.A). US conventions for METAR/SPECI \
  reports vary in a number of ways from the international standard, and are \
  described in chapter 12 of the Federal Meteorological Handbook No.1. \
  (FMH-1 1995), issued by the National Oceanic and Atmospheric Administration \
  (NOAA). General information about the use and history of the METAR standard \
  can be found here. \
  \
  This module extracts the data recorded in the main-body groups of reports \
  that follow the WMO spec or the US conventions, except for the runway state \
  and trend groups, which are parsed but ignored. The most useful remark \
  groups defined in the US spec are parsed, as well, such as the cumulative \
  precipitation, min/max temperature, peak wind and sea-level pressure groups. \
  No other regional conventions are formally supported, but a large number of \
  variant formats found in international reports are accepted.

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# remove executable permissions from sample.py
chmod 644 sample.py

%check

# check importing the python-metar module
%py3_check_import metar

# run the test suite
%{__python3} -m pytest -v

%files -n python-%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}*dist-info
%doc sample.py
%doc README.md
%doc CHANGELOG.md
%doc LICENSE


%changelog
* Sun Apr 26 2026 Jos de Kloe <josdekloe@gmail.com> 2.0.1-1
- update to new upstream version 2.0.1

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-20250516git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.11.0-20250515git
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.11.0-20250514git
- Rebuilt for Python 3.14.0rc2 bytecode

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

