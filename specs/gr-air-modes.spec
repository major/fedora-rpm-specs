# git ls-remote git://github.com/bistromath/gr-air-modes.git
%global git_commit 9e2515a56609658f168f0c833a14ca4d2332713e
%global git_date 20200807

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             gr-air-modes
URL:              http://github.com/bistromath/gr-air-modes
Version:          0
Release:          0.117.%{git_suffix}%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later
BuildRequires:    cmake
BuildRequires:    gcc-c++
BuildRequires:    python3-devel
BuildRequires:    python3-numpy
BuildRequires:    python3-scipy
BuildRequires:    gnuradio-devel
BuildRequires:    sqlite-devel
BuildRequires:    uhd-devel
BuildRequires:    boost-devel
BuildRequires:    graphviz
BuildRequires:    python3-zmq
BuildRequires:    gmp-devel
BuildRequires:    python3-pyqtgraph
BuildRequires:    libunwind-devel
BuildRequires:    pybind11-devel
BuildRequires:    python3-PyQt4-devel
# gnuradio dependency
BuildRequires:    spdlog-devel
# TODO: check whether qwt is needed
BuildRequires:    qwt5-qt4-devel
Requires:         python3-numpy
Requires:         python3-scipy
Requires:         python3-zmq
Requires:         qwt5-qt4
Summary:          SDR receiver for Mode S transponder signals (ADS-B)
Source0:          https://github.com/bistromath/gr-air-modes/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
# https://github.com/bistromath/gr-air-modes/issues/111
Patch0:           gr-air-modes-0-gnuradio-3.9.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Software defined radio receiver for Mode S transponder signals, including
ADS-B reports.

%package devel
Summary:          Development files for gr-air-modes
Requires:         %{name} = %{version}-%{release}

%description devel
Development files for gr-air-modes.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
%cmake
%cmake_build

%install
%cmake_install

# remove hashbangs
pushd %{buildroot}%{python3_sitearch}/air_modes
for f in *.py
do
  sed -i '/^[ \t]*#!\/usr\/bin\/\(env\|python\)/ d' $f
done
popd

%ldconfig_scriptlets

%files
%doc COPYING README
%{_bindir}/uhd_modes.py
%{_bindir}/modes_gui
%{_bindir}/modes_rx
%{_libdir}/*.so.*
%{python3_sitearch}/*

%files devel
%{_includedir}/gr_air_modes
%{_libdir}/*.so
%{_libdir}/cmake/{air_modes,gr-air_modes}/*.cmake

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.117.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 21 2024 Orion Poplawski <orion@nwra.com> - 0-0.116.20200807git9e2515a5
- Rebuild with numpy 2.2 (rhbz#2333031)

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 0-0.115.20200807git9e2515a5
- Rebuilt for spdlog 1.15.0

* Fri Jul 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.114.20200807git9e2515a5
- Rebuilt for new gnuradio

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.113.20200807git9e2515a5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.112.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Python Maint <python-maint@redhat.com> - 0-0.111.20200807git9e2515a5
- Rebuilt for Python 3.13

* Tue Jun 18 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.110.20200807git9e2515a5
- Rebuilt for python 3.13
  Resolves: rhbz#2291534

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 0-0.109.20200807git9e2515a5
- Rebuilt for spdlog 1.14.1

* Thu Apr 25 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.108.20200807git9e2515a5
- Rebuilt for new gnuradio

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.107.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.106.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.105.20200807git9e2515a5
- Rebuilt for new gnuradio

* Tue Jul 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0-0.104.20200807git9e2515a5
- Drop x86 support (leaf package)
- Drop commented-out BuildRequires on mpir-devel, which is retired

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.103.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.102.20200807git9e2515a5
- Rebuilt for new python
  Resolves: rhbz#2220005

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0-0.101.20200807git9e2515a5
- Rebuilt due to spdlog 1.12 update.

* Tue Jun 27 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.100.20200807git9e2515a5
- Rebuilt for new gnuradio

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.99.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0-0.98.20200807git9e2515a5
- Rebuilt due to spdlog update.

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.97.20200807git9e2515a5
- Rebuilt for new gnuradio
  Resolves: rhbz#2129778

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.96.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.95.20200807git9e2515a5
- Rebuilt for new gnuradio

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 0-0.94.20200807git9e2515a5
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.93.20200807git9e2515a5
- Rebuilt for new gnuradio

* Tue Feb 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.92.20200807git9e2515a5
- Rebuilt for new gnuradio

* Mon Jan 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.91.20200807git9e2515a5
- Rebuilt for new gnuradio

* Thu Jan 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.90.20200807git9e2515a5
- Rebuilt for new gnuradio

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.89.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.88.20200807git9e2515a5
- Rebuilt for new gnuradio

* Mon Nov 01 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.87.20200807git9e2515a5
- Rebuilt for new gnuradio

* Thu Oct  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.86.20200807git9e2515a5
- Rebuilt for new gnuradio
  Resolves: rhbz#2011278

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0-0.85.20200807git9e2515a5
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.84.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.83.20200807git9e2515a5
- Rebuilt for new gnuradio
  Resolves: rhbz#1971250

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0-0.82.20200807git9e2515a5
- Rebuilt for Python 3.10

* Thu Mar 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.81.20200807git9e2515a5
- Rebuilt for new gnuradio

* Tue Feb 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.80.20200807git9e2515a5
- Switched to upstream patch to support gnuradio-3.9

* Wed Feb 10 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.79.20200807git9e2515a5
- Minor spec improvements

* Mon Feb  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.78.20200807git9e2515a5
- Fixed FTBFS
  Resolves: rhbz#1923390
  Resolves: rhbz#1925569

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.77.20200807git9e2515a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.76.20200807git9e2515a5
- Rebuilt for new gnuradio

* Thu Aug  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.75.20200807git9e2515a5
- New version
- Fixed FTBFS
  Resolves: rhbz#1863817

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.74.20191111gita2f2627c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.73.20191111gita2f2627c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.72.20191111gita2f2627c
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.71.20191111gita2f2627c
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.70.20191111gita2f2627c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.69.20191111gita2f2627c
- New version
- Switched to Python 3
  Resolves: rhbz#1738963

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.68.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.67.20160831git3bad1f5d
- Changed unversioned python requirements to explicit python2

* Mon May  6 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.66.20160831git3bad1f5d
- Dropped PyQwt in f31+

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.65.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 0-0.64.20160831git3bad1f5d
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.63.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.62.20160831git3bad1f5d
- Added requirement for C++

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.61.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0-0.60.20160831git3bad1f5d
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.59.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.58.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Tue Feb  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.57.20160831git3bad1f5d
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.56.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.55.20160831git3bad1f5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0-0.54.20160831git3bad1f5d
- Rebuilt for Boost 1.64

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.53.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 0-0.52.20160831git3bad1f5d
- Rebuilt for Boost 1.63

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.51.20160831git3bad1f5d
- Rebuilt for new gnuradio

* Thu Sep  1 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.50.20160831git3bad1f5d
- Fixed traceback in modes_gui
  Related: rhbz#1369923

* Wed Aug 31 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.49.20160831git3bad1f5d
- New version
  Related: rhbz#1369923
- Simplified snapshots updates

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.48.20160106git514414f6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.47.20160106git514414f6
- Rebuilt for new gnuradio

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.46.20160106git514414f6
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.45.20160106git514414f6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0-0.44.20160106git514414f6
- Rebuilt for Boost 1.60

* Wed Jan  6 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.43.20160106git514414f6
- New version
  Resolves: rhbz#1295996

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.42.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.41.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.40.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0-0.39.20140312gitcc0fa180
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.38.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.37.20140312gitcc0fa180
- Rebuilt for new boost

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.36.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.35.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0-0.34.20140312gitcc0fa180
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.33.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.32.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.31.20140312gitcc0fa180
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.30.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0-0.29.20140312gitcc0fa180
- Rebuild for boost 1.57.0

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.28.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Tue Sep  2 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.27.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.26.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.25.20140312gitcc0fa180
- Rebuilt for new gnuradio

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.24.20140312gitcc0fa180
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 0-0.23.20140312gitcc0fa180
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0-0.22.20140312gitcc0fa180
- rebuild for boost 1.55.0

* Wed Mar 12 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.21.20140312gitcc0fa180
- New version
- Dropped build-fix patch (not needed)

* Tue Mar 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.20.20130730git797bef13
- Rebuilt for new gnuradio

* Mon Dec  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.19.20130730git797bef13
- Rebuilt for new gnuradio

* Mon Nov 18 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.18.20130730git797bef13
- Rebuilt for new gnuradio

* Mon Sep  2 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.17.20130730git797bef13
- Rebuilt for new gnuradio

* Tue Aug  6 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.16.20130730git797bef13
- Used unversioned doc directory
  Resolves: rhbz#993801

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0-0.15.20130730git797bef13
- Rebuild for boost 1.54.0

* Tue Jul 30 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.14.20130730git797bef13
- New version

* Tue May 28 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.13.20130409gitf25d21f5
- Rebuilt for new gnuradio

* Tue Apr  9 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.12.20130409gitf25d21f5
- Fixed modes_gui build (missed requirements)

* Tue Apr  9 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.11.20130409gitf25d21f5
- New git snapshot
- Dropped add-soname patch (upstreamed)

* Thu Mar 21 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.10.20120905git6c7a7370
- Rebuilt for new gnuradio

* Thu Feb 28 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.9.20120905git6c7a7370
- Rebuilt for new gnuradio

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20120905git6c7a7370
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.7.20120905git6c7a7370
- Rebuilt for new gnuradio

* Mon Nov 12 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.6.20120905git6c7a7370
- Added swig build requires

* Fri Oct 26 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.5.20120905git6c7a7370
- Rebuilt for new gnuradio

* Tue Sep 25 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.4.20120905git6c7a7370
- Hardcoded path for sbindir to silent depcheck errors

* Mon Sep 24 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.3.20120905git6c7a7370
- Packaged doxygen generated documentation as doc subpackage

* Wed Sep 19 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20120905git6c7a7370
- Used macro for sbindir

* Wed Sep  5 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20120905git6c7a7370
- Initial version
