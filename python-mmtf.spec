%bcond_without check
%global pname mmtf-python

%global desc \
The Macromolecular Transmission Format (MMTF) is a new compact binary format to\
transmit and store biomolecular structures for fast 3D visualization and\
analysis.\
\
Bradley AR, Rose AS, Pavelka A, Valasatava Y, Duarte JM, Prlić A, Rose PW (2017)\
MMTF - an efficient file format for the transmission, visualization, and\
analysis of macromolecular structures. bioRxiv 122689. doi: 10.1101/122689\
\
Valasatava Y, Bradley AR, Rose AS, Duarte JM, Prlić A, Rose PW (2017) Towards an\
efficient compression of 3D coordinates of macromolecular structures. PLOS ONE\
12(3): e0174846. doi: 10.1371/journal.pone.01748464\
\
Rose AS, Bradley AR, Valasatava Y, Duarte JM, Prlić A, Rose PW (2016) Web-based\
molecular graphics for large complexes. In Proceedings of the 21st International\
Conference on Web3D Technology (Web3D '16). ACM, New York, NY, USA, 185-186.\
doi: 10.1145/2945292.2945324\


Name: python-mmtf
Version: 1.1.3
Release: 3%{?dist}
Summary: A decoding library for the macromolecular transmission format (MMTF) 
License: Apache-2.0
URL: https://github.com/rcsb/mmtf-python
Source0: https://files.pythonhosted.org/packages/source/m/%{pname}/%{pname}-%{version}.tar.gz
BuildArch: noarch

%description
%{desc}

%package -n python3-mmtf
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{with check}
BuildRequires: python3-msgpack
BuildRequires: python3-pytest
BuildRequires: python3-numpy
%endif
%{?python_provide:%python_provide python3-mmtf}
Requires: python3-msgpack

%description -n python3-mmtf
%{desc}

%prep
%setup -q -n %{pname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%pytest mmtf/tests/codec_tests.py
%endif

%files -n python3-mmtf
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{python3_sitelib}/mmtf_python-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/mmtf

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 Dominik Mierzejewski <dominik@greysector.net> 1.1.3-1
- update to 1.1.3
- use SPDX identifier in License field

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.2-20
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.2-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Charalampos Stratakis <cstratak@redhat.com> - 1.1.2-15
- Use pytest instead of the deprecated nose test runner

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.2-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.2-4
- Subpackage python2-mmtf has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.7

* Wed May 23 2018 Dominik Mierzejewski <dominik@greysector.net> 1.1.2-1
- update to 1.1.2 (#1581003)

* Fri Apr 06 2018 Dominik Mierzejewski <dominik@greysector.net> 1.1.0-1
- update to 1.1.0 (#1563660)

* Wed Mar 07 2018 Dominik Mierzejewski <dominik@greysector.net> 1.0.12-1
- update to 1.0.12 (#1549879)

* Wed Feb 21 2018 Dominik Mierzejewski <dominik@greysector.net> 1.0.10-1
- update to 1.0.10 (#1531012)
- use standard check wrapper

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Dominik Mierzejewski <dominik@greysector.net> 1.0.7-1
- update to 1.0.7 (#1466315)

* Mon Jun 05 2017 Dominik Mierzejewski <dominik@greysector.net> 1.0.6-2
- drop redundant macro definitions and use python version macros

* Sat Jun 03 2017 Dominik Mierzejewski <dominik@greysector.net> 1.0.6-1
- update to 1.0.6
- drop workarounds for issues fixed upstream

* Thu May 18 2017 Dominik Mierzejewski <dominik@greysector.net> 1.0.5-1
- initial build
- include upstream test data missing from tarball
- don't run tests requiring network access
