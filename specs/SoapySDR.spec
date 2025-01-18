Name:           SoapySDR
Version:        0.8.1
Release:        15%{?dist}
Summary:        A Vendor Neutral and Platform Independent SDR Support Library

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            https://github.com/pothosware/%{name}
Source0:        https://github.com/pothosware/%{name}/archive/refs/tags/soapy-sdr-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  swig
BuildRequires:  doxygen
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: (python3-setuptools if python3-devel >= 3.12)

%description
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n python3-%{name}
Summary:        Python3 Bindings for SoapySDR
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n %{name}-devel
Summary:        Development Files for SoapySDR
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n %{name}-doc
Summary:        Development Files for SoapySDR
BuildArch: noarch

%description -n %{name}-doc
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices. This package includes
library header file documentation.
    
    
%prep
%autosetup -n %{name}-soapy-sdr-%{version}

%build
export Python_ADDITIONAL_VERSIONS="%{python3_version}"
%cmake -DUSE_PYTHON_CONFIG=ON -DPYTHON3_EXECUTABLE=%{__python3} -DSOAPY_SDR_EXTVER=%{release}
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}/%{name}/modules0.8
# install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{__cmake_builddir}/docs/html/* %{buildroot}%{_pkgdocdir}

%check
ctest -V %{?_smp_mflags}

%ldconfig_scriptlets
%files
%license LICENSE_1_0.txt
%{_bindir}/SoapySDRUtil
%{_libdir}/libSoapySDR.so.0.8.1
%{_libdir}/libSoapySDR.so.0.8
%{_mandir}/man1/*
%doc README.md
# for hardware support modules
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules0.8

%files -n python3-%{name}
%license LICENSE_1_0.txt
%{python3_sitearch}/SoapySDR.py
%{python3_sitearch}/_SoapySDR.so
%{python3_sitearch}/__pycache__/SoapySDR.cpython-*.pyc


%files -n %{name}-devel
%{_includedir}/%{name}
%{_libdir}/libSoapySDR.so
%{_libdir}/pkgconfig/*
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/%{name}/*

%files -n %{name}-doc
%license LICENSE_1_0.txt
%{_pkgdocdir}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.1-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.8.1-12
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.1-9
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.1-7
- BZ 2154868 - Fix distutils dep for phyton 3.12

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Dave Olsthoorn <dave@bewaar.me> - 0.8.1-5
- use release as EXTVER

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.11

* Sun Jan 23 2022 Matt Domsch <matt@domsch.com> - 0.8.1-3
- Fix directory name of hardware support modules

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Matt Domsch <matt@domsch.com> - 0.8.1-1
- Upstream 0.8.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.2-12
- Rebuilt for Python 3.10

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.7.2-11
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Matt Domsch <matt@domsch.com> - 0.7.2-9
- Upstream 0.7.2, drop now-included patch
- fixes for F33 cmake

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Matt Domsch <matt@domsch.com> - 0.7.1-1
- upstream 0.7.1
- fix build for Python 3.8, with thanks to Miro Hrončok (BZ#1716544)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3.20180806gite694813
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2.20180806gite694813
- Subpackage python2-SoapySDR has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug  6 2018 Matt Domsch <matt@domsch.com> 0.6.1-1.20180806gite694813
- initial Fedora packaging
