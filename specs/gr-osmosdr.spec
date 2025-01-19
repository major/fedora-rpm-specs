#%%global git_commit 2fedabec385a91af71468b179f0050f74e17f51e
#%%global git_date 20231108

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

%{?filter_setup:
%filter_provides_in %{python3_sitearch}/osmosdr/.*\.so$
%filter_setup
}

Name:          gr-osmosdr
URL:           http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version:       0.2.5
Release:       14%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: gnuradio-devel
BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: pybind11-devel
BuildRequires: libunwind-devel
BuildRequires: rtl-sdr-devel
BuildRequires: uhd-devel
BuildRequires: hackrf-devel
BuildRequires: gr-funcube-devel
BuildRequires: gmp-devel
BuildRequires: gr-iqbal-devel
BuildRequires: airspyone_host-devel
BuildRequires: SoapySDR-devel
BuildRequires: python3-mako
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: fftw-devel
BuildRequires: libosmo-dsp-devel
BuildRequires: libsndfile-devel
BuildRequires: python3-six
Summary:       Common software API for various radio hardware
#Source0:       https://github.com/osmocom/gr-osmosdr/archive/%%{git_commit}/%%{name}-%%{git_commit}.tar.gz
#Source0:       https://github.com/osmocom/gr-osmosdr/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:        https://gitea.osmocom.org/sdr/gr-osmosdr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://osmocom.org/issues/5144
Patch0:        gr-osmosdr-0.2.3-airspy-multi-dev.patch

%description
Primarily gr-osmosdr supports the OsmoSDR hardware, but it also
offers a wrapper functionality for FunCube Dongle,  Ettus UHD
and rtl-sdr radios. By using gr-osmosdr source you can take
advantage of a common software api in your application(s)
independent of the underlying radio hardware.

%package devel
Summary:       Development files for gr-osmosdr
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-osmosdr.

# Made doc arch due to bug in doxygen
%package doc
Summary:       Documentation files for gr-osmosdr
Requires:      %{name} = %{version}-%{release}

%description doc
Documentation files for gr-osmosdr.

%prep
#%%autosetup -p1 -n %%{name}-%%{git_commit}
#%%autosetup -p1
%autosetup -p1 -n %{name}

# TODO fix the lib location nicer way
sed -i 's|/lib/|/%{_lib}/|g' CMakeLists.txt

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc AUTHORS COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{python3_sitearch}/osmosdr
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/osmosdr
%{_libdir}/*.so
%{_libdir}/cmake/osmosdr/*.cmake

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 0.2.5-13
- Rebuilt for spdlog 1.15.0

* Fri Jul 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.5-12
- Rebuilt for new gnuradio

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.5-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.5-9
- Rebuilt for new uhd

* Wed Jun 26 2024 Python Maint <python-maint@redhat.com> - 0.2.5-8
- Rebuilt for Python 3.13

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 0.2.5-7
- Rebuilt for spdlog 1.14.1

* Thu Apr 25 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.5-6
- Rebuilt for new gnuradio

* Tue Apr  9 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.5-5
- Rebuilt for new rtl-sdr

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.2.5-2
- Rebuilt for Boost 1.83

* Tue Jan 16 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.5-1
- New version
  Resolves: rhbz#2258628

* Tue Jan 02 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4^20231108git2fedabec-3
- Rebuilt for new gnuradio

* Wed Nov 22 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4^20231108git2fedabec-2
- Rebuilt for new uhd

* Wed Nov  8 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4^20231108git2fedabec-1
- New snapshot

* Mon Sep 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4-9
- Rebuilt for new uhd

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4-7
- Rebuilt for new python
  Resolves: rhbz#2220009

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.4-6
- Rebuilt due to spdlog 1.12 update.

* Tue Jun 27 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4-5
- Rebuilt for new gnuradio

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.2.4-4
- Rebuilt for Boost 1.81

* Wed Feb  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4-3
- Rebuilt for new uhd

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.4-1
- New version
  Resolves: rhbz#2157047

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.3-32.20210217gita100eb02
- Rebuilt due to spdlog update.

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-31.20210217gita100eb02
- Rebuilt for new gnuradio
  Resolves: rhbz#2129782

* Sat Jul 30 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-30.20210217gita100eb02
- Rebuilt for new uhd

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-29.20210217gita100eb02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-28.20210217gita100eb02
- Rebuilt for new airspyone_host

* Thu Jun 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-27.20210217gita100eb02
- Rebuilt for new gnuradio

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 0.2.3-26.20210217gita100eb02
- Rebuilt for Python 3.11

* Tue May 17 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-25.20210217gita100eb02
- Fixed gain initialization

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.2.3-24.20210217gita100eb02
- Rebuilt for Boost 1.78

* Tue Apr 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-23.20210217gita100eb02
- Rebuilt for new uhd
  Resolves: rhbz#2077802

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-22.20210217gita100eb02
- Rebuilt for new gnuradio

* Tue Feb 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-21.20210217gita100eb02
- Rebuilt for new gnuradio

* Thu Feb 17 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-20.20210217gita100eb02
- Updated ppm patch for better precision in set_center_freq()

* Tue Feb 15 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-19.20210217gita100eb02
- Use double for ppm with fcd/pp

* Mon Jan 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-18.20210217gita100eb02
- Rebuilt for new gnuradio

* Thu Jan 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-17.20210217gita100eb02
- Rebuilt for new gnuradio

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-16.20210217gita100eb02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-15.20210217gita100eb02
- Rebuilt for new gnuradio

* Thu Nov  4 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-14.20210217gita100eb02
- Rebuilt for new gnuradio
  Resolves: rhbz#2020177

* Tue Oct 12 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-13.20210217gita100eb02
- Added support for multiple Airspy devices (Daniel Rusek pointed to the patch)
  Resolves: rhbz#1958557

* Thu Oct  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-12.20210217gita100eb02
- Rebuilt for new gnuradio
  Resolves: rhbz#2011282

* Tue Aug 24 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-11.20210217gita100eb02
- Rebuilt for new soapy
  Resolves: rhbz#1996421

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-10.20210217gita100eb02
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9.20210217gita100eb02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul  2 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-8.20210217gita100eb02
- Rebuilt for new uhd

* Thu Jun 17 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-7.20210217gita100eb02
- Correctly enabled funcube support

* Mon Jun 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-6.20210217gita100eb02
- Rebuilt for new gnuradio
  Resolves: rhbz#1971254

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.3-5.20210217gita100eb02
- Rebuilt for Python 3.10

* Fri Mar 26 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-4.20210217gita100eb02
- Added python3-six build requirement
  Resolves: rhbz#1851045

* Fri Mar 26 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-3.20210217gita100eb02
- Switched to gr-funcube

* Fri Mar  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-2.20210217gita100eb02
- Fixed FTBFS
  Resolves: rhbz#1935598

* Wed Feb 17 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.3-1.20210217gita100eb02
- New version
  Resolves: rhbz#1923394
  Resolves: rhbz#1921505

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-30.20191112gitf3905d35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-29.20191112gitf3905d35
- Rebuilt for new gnuradio

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-28.20191112gitf3905d35
- Rebuilt for new gr-iqbal
  Resolves: rhbz#1777874

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-27.20191112gitf3905d35
- Fixed FTBFS
  Resolves: rhbz#1863822
- Made doc arch due to bug in doxygen

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-26.20191112gitf3905d35
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-25.20191112gitf3905d35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 0.1.4-24.20191112gitf3905d35
- Rebuilt and patched for Boost 1.73.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-23.20191112gitf3905d35
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-22.20191112gitf3905d35
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-21.20191112gitf3905d35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-20.20191112gitf3905d35
- Re-enabled gr-iqbal support

* Mon Nov 11 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-19.20191112gitf3905d35
- New version
- Switched to Python 3
  Resolves: rhbz#1738958

* Mon Aug 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-18.20170221git2a2236cc
- Rebuilt for new uhd

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-17.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-16.20170221git2a2236cc
- Rebuilt for new gnuradio

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-14.20170221git2a2236cc
- Rebuilt for new gnuradio and UHD
  Resolves: rhbz#1625012

* Mon Dec 10 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-13.20170221git2a2236cc
- Rebuilt for new gnuradio

* Fri Aug 31 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-12.20170221git2a2236cc
- Added support for SoapySDR
  Resolves: rhbz#1624000

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-11.20170221git2a2236cc
- Disabled parallel build
  Resolves: rhbz#1604317

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-10.20170221git2a2236cc
- Rebuilt for new gnuradio
- Fixed python macros
- Added requirement for C++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-8.20170221git2a2236cc
- Added support for Airspy
- Rebuilt for new gnuradio

* Tue Feb  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-7.20170221git2a2236cc
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5.20170221git2a2236cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 0.1.4-4.20170221git2a2236cc
- Rebuilt for Boost 1.64

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.4-3.20170221git2a2236cc
- Rebuild due to bug in RPM (RHBZ #1468476)

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-2.20170221git2a2236cc
- Rebuilt for new gnuradio

* Tue Feb 21 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-1.20170221git2a2236cc
- New version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-24.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-23.20141023git42c66fdd
- Rebuilt for new uhd

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-22.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-21.20141023git42c66fdd
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-20.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue May 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-19.20141023git42c66fdd
- Rebuilt for new uhd

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-18.20141023git42c66fdd
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-17.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1.3-16.20141023git42c66fdd
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-15.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-14.20141023git42c66fdd
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-13.20141023git42c66fdd
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.1.3-12.20141023git42c66fdd
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-11.20141023git42c66fdd
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-10.20141023git42c66fdd
- Rebuilt for new boost

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-9.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-8.20141023git42c66fdd
- Rebuilt for new gnuradio

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.1.3-7.20141023git42c66fdd
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-6.20141023git42c66fdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-5.20141023git42c66fdd
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.3-4.20141023git42c66fdd
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-3.20141023git42c66fdd
- Rebuilt for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0.1.3-2.20141023git42c66fdd
- Rebuild for boost 1.57.0

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-1.20141023git42c66fdd
- New version
- Added gr-fcdproplus (FUNcube Dongle Pro+) support
- Added gr-iqbal support

* Wed Sep 24 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-17.20130729git9dfe3a63
- Added hackrf support

* Tue Sep  2 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-16.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-15.20130729git9dfe3a63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-14.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-13.20130729git9dfe3a63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 0.1.1-12.20130729git9dfe3a63
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.1.1-11.20130729git9dfe3a63
- rebuild for boost 1.55.0

* Mon May  5 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-10.20130729git9dfe3a63
- Enabled UHD support
  Resolves: rhbz#1093954

* Tue Mar 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-9.20130729git9dfe3a63
- Fixed pkgconfig version string

* Tue Mar 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-8.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Mon Jan  6 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-7.20130729git9dfe3a63
- Dummy release bump due to http://fedorahosted.org/rel-eng/ticket/5823

* Mon Dec  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-6.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Mon Nov 18 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-5.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Mon Sep  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-4.20130729git9dfe3a63
- Rebuilt for new gnuradio

* Tue Aug  6 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-3.20130729git9dfe3a63
- Used unversioned doc directory
  Resolves: rhbz#993807

* Mon Jul 29 2013 Petr Machata <pmachata@redhat.com> - 0.1.1-2.20130729git9dfe3a63
- Rebuild for boost 1.54.0

* Mon Jul 29 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-1.20130729git9dfe3a63
- New version
- Dropped doxygen-fix and docdir-override patches (upstreamed)

* Tue May 28 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.1-3.20130403gite85c68d9
- Rebuilt for new gnuradio

* Tue Apr  9 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.1-2.20130403gite85c68d9
- Packaged doxygen docs and examples
- Various improvements according to comments in the merge review

* Wed Apr  3 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.1-1.20130403gite85c68d9
- Initial version
