%global commit0 fce5a14b8f0a4ba8ac4d6d684516b3695fc8b9cd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global commit1 4dda149b9e4f1753ebc8b011ece2fe794be1281a
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

%global snapdate 20241211

%global __python %{__python3}

Name:          trellis
Version:       1.2.1
Release:       30.%{snapdate}git%{shortcommit0}%{?dist}
Summary:       Lattice ECP5 FPGA bitstream creation/analysis/programming tools
License:       ISC
URL:           https://github.com/YosysHQ/prj%{name}
Source0:       https://github.com/YosysHQ/prj%{name}/archive/%{commit0}/prj%{name}-%{shortcommit0}.tar.gz
Source1:       https://github.com/YosysHQ/prj%{name}-db/archive/%{commit1}/prj%{name}-db-%{shortcommit1}.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: boost-python3-devel
#BuildRequires: pybind11-devel
# for building docs:
BuildRequires: python3-sphinx-latex
BuildRequires: python3-recommonmark
BuildRequires: latexmk
# for building manpages:
BuildRequires: help2man

Requires:      %{name}-data = %{version}-%{release}

%description
Project Trellis enables a fully open-source flow for ECP5 FPGAs using
Yosys for Verilog synthesis and nextpnr for place and route. Project
Trellis provides the device database and tools for bitstream creation.

%package devel
Summary:       Development files for Project Trellis
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-data = %{version}-%{release}

%description devel
Development files to build packages using Project Trellis

%package data
Summary:       Project Trellis - Lattice ECP5 Bitstream Database
BuildArch:     noarch

%description data
This package contains the bitstream documentation database for
Lattice ECP5 FPGA devices.

%prep
%setup -q -n prj%{name}-%{commit0} -a 1
rm -rf database
mv prj%{name}-db-%{commit1} database
# add "-fPIC -g1" to CMAKE_CXX_FLAGS:
# (NOTE: "-g1" reduces debuginfo verbosity over "-g", which helps on armv7hl)
sed -i '/CMAKE_CXX_FLAGS/s/-O3/-O3 -fPIC -g1/' libtrellis/CMakeLists.txt
# prevent "lib64" false positive (e.g., on i386):
sed -i 's/"lib64"/"lib${LIB_SUFFIX}"/' libtrellis/CMakeLists.txt
# fix shebang lines in Python scripts:
find . -name \*.py -exec sed -i 's|/usr/bin/env python3|/usr/bin/python3|' {} \;
# remove .gitignore files in examples:
find . -name \.gitignore -delete

%build
# building manpages requires in-source build:
%define __cmake_in_source_build 1
# disable LTO to allow building for f33 rawhide (BZ 1865586):
%define _lto_cflags %{nil}
%cmake libtrellis \
	-DCURRENT_GIT_VERSION=%{version}-%{release}
#	-DPYBIND11_INCLUDE_DIR="/usr/include/pybind11/" \
%cmake_build
%make_build -C docs latexpdf
# build manpages:
mkdir man1
for f in ecp*
do
  [ -x $f ] || continue
  LD_PRELOAD=./libtrellis.so \
    help2man --no-discard-stderr --version-string %{version} -N \
             -o man1/$f.1 ./$f
  sed -i '/required but missing/d' man1/$f.1
done

%install
%cmake_install
install -Dpm644 -t %{buildroot}%{_mandir}/man1 man1/*

%check
# nothing to do for now.

%files
%license COPYING
%doc README.md
%doc docs/_build/latex/ProjectTrellis.pdf
%doc examples
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libtrellis.so
%{_datadir}/%{name}/misc
%{_mandir}/man1/ecp*.1*

%files devel
%doc libtrellis/examples
%{_libdir}/%{name}/pytrellis.so
%{_datadir}/%{name}/timing
%{_datadir}/%{name}/util

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/database

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-30.20241211gitfce5a14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-29.20241211gitfce5a14
- Update to newer snapshot

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28.20240524git2dab009
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.2.1-27.20240524git2dab009
- Rebuilt for Python 3.13

* Fri May 24 2024 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-26.20240524git2dab009
- Update to newer snapshot

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25.20231006git36c615d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-24.20231006git36c615d
- Rebuilt for Boost 1.83

* Fri Oct 06 2023 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-23.20231006git36c615d
- update to newer snapshot (incl. database)

* Tue Sep 12 2023 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-22.20230912gitbe909ba
- update to newer snapshot (incl. database)

* Sat Jul 29 2023 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-21.20230729gite830a28
- Update to newer snapshot

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20.20230511gitf1e5710
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.2.1-19.20230511gitf1e5710
- Rebuilt for Python 3.12

* Thu May 11 2023 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-18.20230511gitf1e5710
- update to newer snapshot (incl. database)

* Sun Apr 23 2023 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-17.20230423gitb9120de
- update to newer snapshot (incl. updated database)

* Sun Feb 26 2023 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-16.20230226gitf767e56
- Update to newer snapshot
- Temp. use bundled pybind11 (https://github.com/pybind/pybind11/issues/4529)

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-15.20230215git0c522ce
- Rebuilt for Boost 1.81

* Wed Feb 15 2023 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-14.20230215git0c522ce
- Update to newer snapshot

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-13.20221109git35f5aff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-12.20221109git35f5aff
- Update to newer snapshot

* Thu Oct 06 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-11.20221006git5e51529
- Update to newer snapshot

* Sun Aug 21 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-10.20220821git98e0ea3
- Update to newer snapshot

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9.20220705git7a2e9ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-8.20220705git7a2e9ed
- Update to newer snapshot (incl. fix for Python 3.11, BZ 2103635).

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-7.20220509git64b38df
- Rebuilt for Python 3.11

* Wed May 11 2022 Thomas Rodgers <trodgers@redhat.com> - 1.2.1-6.20220509git64b38df
- Rebuilt for Boost 1.78

* Mon May 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-5.20220509git64b38df
- Update to newer snapshot.

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.2.1-4.20220407git46f50f7
- Rebuilt for Boost 1.78

* Thu Apr 07 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-3.20220407git46f50f7
- Update to newer snapshot.

* Wed Apr 06 2022 Karolina Surma <ksurma@redhat.com> - 1.2.1-2.20220127git3ae21cf
- Use versioned BR on python3-sphinx-latex

* Mon Feb 21 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.2.1-1.20220222git3ae21cf
- Switch upstream to YosysHQ
- Update to version 1.21

* Thu Jan 27 2022 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.23.20220127git2f06397
- Update to newer snapshot.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.20210904git03e0070
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 04 2021 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.21.20210904git03e0070
- Update to newer snapshot.

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.0-0.20.20210523gitfe1c39c
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.19.20210523gitfe1c39c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0-0.18.20210523gitfe1c39c
- Rebuilt for Python 3.10

* Sun May 23 2021 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.17.20210523gitfe1c39c
- Update to newer snapshot.
- Remove patch for pdf doc build (revert applied upstream).

* Sun Mar 07 2021 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.16.20210307git210a0a7
- Update to newer snapshot.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.20201124git52d2915
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.0-0.14.              20201124git52d2915
- Rebuilt for Boost 1.75

* Tue Nov 24 2020 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.13.20201124git52d2915
- Update to newer snapshot.
- Fix Python 3.10 build (BZ #1898928).

* Thu Aug 06 2020 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.12.20200806gitf93243b
- Update to newer snapshot.
- Disable LTO for f33 rebuild (BZ 1865586)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.20200127git30ee6f2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.20200127git30ee6f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 1.0-0.9.20200127git30ee6f2
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.8.20200127git30ee6f2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.7.20200127git30ee6f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.6.20200127git30ee6f2
- Update to newer snapshot.
- Fix Python 3.9 build (BZ #1793496).
- Fix pdf doc build (upstream requires obscure python/sphinx dependency).

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.5.20190806git7e97b5b
- Rebuilt for Python 3.8

* Tue Aug 06 2019 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.4.20190806git7e97b5b
- Update to newer snapshot.
- Fix python 3.8 build (BZ #1737016).

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.3.20190327gitf1b1b35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.2.20190327gitf1b1b35
- Update to newer snapshot.
- Fix library suffix mis-detection on i686.

* Wed Mar 20 2019 Gabriel Somlo <gsomlo@gmail.com> - 1.0-0.1.20190320git26d6667
- Initial version.
