%global git_commit fbee239a6fb36dd2fb564f6e6a0d393c4bc844db
%global git_date 20210210

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:          gr-iqbal
#URL:           http://cgit.osmocom.org/gr-iqbal/
URL:           https://github.com/osmocom/gr-iqbal
Version:       0.38.2
Release:       34.%{git_suffix}%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: fftw-devel
BuildRequires: libosmo-dsp-devel
BuildRequires: python3-devel
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: gmp-devel
BuildRequires: libunwind-devel
BuildRequires: pybind11-devel
Summary:       GNURadio block for suppressing IQ imbalance
#Source0:       https://github.com/osmocom/gr-iqbal/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:       https://github.com/osmocom/gr-iqbal/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

%description
This GNURadio block can suppress IQ imbalance in the RX path of
quadrature receivers.

%package devel
Summary:          Development files for gr-iqbal
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-iqbal.

%package doc
Summary:          Documentation files for gr-iqbal
Requires:         %{name} = %{version}-%{release}
# Doxygen bug
#BuildArch:        noarch

%description doc
Documentation files for gr-iqbal.

%prep
%setup -q -n %{name}-%{git_commit}

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

# Fix docs location
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/gr-iqbalance %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{python3_sitearch}/*
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/gnuradio/iqbalance
%{_libdir}/*.so
%{_libdir}/cmake/gnuradio/*.cmake

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-34.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 0.38.2-33.20210210gitfbee239a
- Rebuilt for spdlog 1.15.0

* Fri Jul 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-32.20210210gitfbee239a
- Rebuilt for new gnuradio

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.38.2-31.20210210gitfbee239a
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-30.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Python Maint <python-maint@redhat.com> - 0.38.2-29.20210210gitfbee239a
- Rebuilt for Python 3.13

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 0.38.2-28.20210210gitfbee239a
- Rebuilt for spdlog 1.14.1

* Thu Apr 25 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-27.20210210gitfbee239a
- Rebuilt for new gnuradio

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-26.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-25.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-24.20210210gitfbee239a
- Rebuilt for new gnuradio

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-23.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-22.20210210gitfbee239a
- Rebuilt for new python
  Resolves: rhbz#2220008

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.38.2-21.20210210gitfbee239a
- Rebuilt due to spdlog 1.12 update.

* Tue Jun 27 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-20.20210210gitfbee239a
- Rebuilt for new gnuradio

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-19.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.38.2-18.20210210gitfbee239a
- Rebuilt due to spdlog update.

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-17.20210210gitfbee239a
- Rebuilt for new gnuradio
  Resolves: rhbz#2129781

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-16.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-15.20210210gitfbee239a
- Rebuilt for new gnuradio

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 0.38.2-14.20210210gitfbee239a
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-13.20210210gitfbee239a
- Rebuilt for new gnuradio

* Tue Feb 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-12.20210210gitfbee239a
- Rebuilt for new gnuradio

* Mon Jan 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-11.20210210gitfbee239a
- Rebuilt for new gnuradio

* Thu Jan 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-10.20210210gitfbee239a
- Rebuilt for new gnuradio

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-9.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-8.20210210gitfbee239a
- Rebuilt for new gnuradio

* Mon Nov 01 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-7.20210210gitfbee239a
- Rebuilt for new gnuradio

* Thu Oct  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-6.20210210gitfbee239a
- Rebuilt for new gnuradio
  Resolves: rhbz#2011281

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-5.20210210gitfbee239a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-4.20210210gitfbee239a
- Rebuilt for new gnuradio
  Resolves: rhbz#1971253

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.38.2-3.20210210gitfbee239a
- Rebuilt for Python 3.10

* Thu Mar 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-2.20210210gitfbee239a
- Rebuilt for new gnuradio

* Wed Feb 10 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.2-1.20210210gitfbee239a
- New version
  Resolves: rhbz#1925572
  Resolves: rhbz#1923393

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.1-2
- Rebuilt for new gnuradio

* Fri Aug  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.38.1-1
- New version
- Fixed FTBFS
  Resolves: rhbz#1863821

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-41
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.37.2-39
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-38
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-36
- Switched to Python 3
  Resolves: rhbz#1738959

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-34
- Rebuilt for new gnuradio

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 0.37.2-33
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-32
- Rebuilt for new gnuradio

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-31
- Rebuilt for new gnuradio

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-29
- Rebuilt for new gnuradio
- Disabled parallel build

* Fri Feb  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-28
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.37.2-25
- Rebuilt for Boost 1.64

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-24
- Rebuilt for new gnuradio

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 0.37.2-23
- Rebuilt for Boost 1.63

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-22
- Rebuilt for new gnuradio

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37.2-21
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-20
- Rebuilt for new gnuradio

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-19
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0.37.2-17
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-16
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-15
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-14
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.37.2-13
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-12
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-11
- Rebuild for new boost

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-10
- Rebuilt for new gnuradio

* Thu Jul 23 2015 David Tardon <dtardon@redhat.com> - 0.37.2-9
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-7
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.37.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-5
- Rebuilt for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0.37.2-4
- Rebuild for boost 1.57.0

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-3
- Rebuilt for new gnuradio

* Thu Oct 16 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-2
- Added isa to devel package requirement

* Wed Oct  8 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.37.2-1
- Initial release
