Name:          gr-hpsdr
URL:           https://github.com/Tom-McDermott/gr-hpsdr
Version:       3.0
Release:       33%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: pybind11-devel
BuildRequires: boost-filesystem
BuildRequires: boost-system
BuildRequires: python3-devel
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: gmp-devel
BuildRequires: libunwind-devel
Summary:       GNU Radio modules for OpenHPSDR Hermes / Metis and Red Pitaya
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/Tom-McDermott/gr-hpsdr/issues/18
Patch0:        gr-hpsdr-3.0-soname-fix.patch

%description
GNU Radio modules for OpenHPSDR Hermes / Metis and Red Pitaya using the
OpenHpsdr protocol.

%package devel
Summary:          Development files for gr-hpsdr
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-hpsdr.

%package doc
Summary:          Documentation files for gr-hpsdr
Requires:         %{name} = %{version}-%{release}
# Workaround for doxygen bug?
#BuildArch:        noarch

%description doc
Documentation files for gr-hpsdr.

%prep
%autosetup -p1

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%license license.txt
%doc README.md

%{_libdir}/*.so.*
%{python3_sitearch}/hpsdr
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/hpsdr
%{_libdir}/*.so
%{_libdir}/cmake/hpsdr

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 3.0-32
- Rebuilt for spdlog 1.15.0

* Fri Jul 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-31
- Rebuilt for new gnuradio

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0-30
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Python Maint <python-maint@redhat.com> - 3.0-28
- Rebuilt for Python 3.13

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 3.0-27
- Rebuilt for spdlog 1.14.1

* Thu Apr 25 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-26
- Rebuilt for new gnuradio

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-23
- Rebuilt for new gnuradio

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-21
- Rebuilt for new python
  Resolves: rhbz#2220007

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0-20
- Rebuilt due to spdlog 1.12 update.

* Tue Jun 27 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-19
- Rebuilt for new gnuradio

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0-17
- Rebuilt due to spdlog update.

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-16
- Rebuilt for new gnuradio
  Resolves: rhbz#2129780

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-14
- Rebuilt for new gnuradio

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 3.0-13
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-12
- Rebuilt for new gnuradio

* Tue Feb 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-11
- Rebuilt for new gnuradio

* Mon Jan 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-10
- Rebuilt for new gnuradio

* Thu Jan 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-9
- Rebuilt for new gnuradio

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-7
- Rebuilt for new gnuradio

* Mon Nov 01 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-6
- Rebuilt for new gnuradio

* Thu Oct  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-5
- Rebuilt for new gnuradio
  Resolves: rhbz#2011280

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0-4
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-2
- Fixed soname

* Mon Jun 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0-1
- New version
  Resolves: rhbz#1971252

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-22
- Rebuilt for Python 3.10

* Thu Mar 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-21
- Rebuilt for new gnuradio

* Tue Feb 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-20
- Added support for gnuradio 3.9
  Resolves: rhbz#1923392
  Resolves: rhbz#1925571

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-18
- Rebuilt for new gnuradio

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-17
- Fixed FTBFS
  Resolves: rhbz#1863819

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-14
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-13
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-11
- Switched to Python 3
  Resolves: rhbz#1738960

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-9
- Rebuilt for new gnuradio

* Fri Mar 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-8
- Fixed FTBFS
  Resolves: rhbz#1675055

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.2-6
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-5
- Rebuilt for new gnuradio

* Thu Jul 19 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-4
- More fixes according to review

* Wed Jul  4 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-3
- More fixes according to review

* Wed Jul  4 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-2
- Various fixes according to review

* Tue Jul  3 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-1
- Initial version
