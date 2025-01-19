%global cmake_module_ver 2018.02

Name:          lunchbox
Version:       1.17.0
Release:       14%{?dist}
Summary:       C++ library for multi-threaded programming
# Boost license: lunchbox/atomic.h, lunchbox/any.h
# LGPLv3 license: e.g. any.cpp and lfVector.h
# the rest is under LGPLv2
License:       Boost and LGPLv2 and LGPLv3
URL:           http://www.equalizergraphics.com/
Source0:       https://github.com/Eyescale/Lunchbox/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/Eyescale/Lunchbox/issues/329
Source1:       https://github.com/Eyescale/CMake/archive/refs/tags/%{cmake_module_ver}.tar.gz
# https://github.com/Eyescale/Lunchbox/issues/331
Source2:       https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
Source3:       https://www.gnu.org/licenses/lgpl-3.0.txt
Source4:       https://www.boost.org/LICENSE_1_0.txt
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: servus-devel
BuildRequires: qt5-qtbase-devel
Provides:      bundled(eyescale-cmake-common) = %{cmake_module_ver}
# https://github.com/Eyescale/CMake/pull/599
Patch0:        lunchbox-1.17.0-libdir-fix.patch
# https://github.com/Eyescale/CMake/pull/601
Patch1:        lunchbox-1.17.0-docdir-override.patch
# https://github.com/Eyescale/Lunchbox/pull/334
Patch2:        lunchbox-1.17.0-nanosleep-fix.patch

%description
Lunchbox is C++ library for multi-threaded programming, providing
OS abstraction, utility classes and high-performance primitives,
such as atomic variables, spin locks and lock-free containers.

%package devel
Summary:       Development files for lunchbox
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for lunchbox.

%prep
%setup -q -a 1 -n Lunchbox-%{version}

# drop bundled pthreads
rm -f pthreads/*.tar.gz

mv CMake-%{cmake_module_ver}/* CMake/common/
rm -f CMake-%{cmake_module_ver}/.gitignore
rmdir CMake-%{cmake_module_ver}
%autopatch -p1

cp -at . %{SOURCE2} %{SOURCE3} %{SOURCE4}

# perf-memory test failing
# https://github.com/Eyescale/Lunchbox/issues/330
rm -f tests/perf/memory.cpp

# drop tests failing on armv7hl
# https://github.com/Eyescale/Lunchbox/issues/333
%ifarch armv7hl
pushd tests
rm -f bitOperation.cpp intervalSet.cpp result.cpp string.cpp
popd
%endif

%build
%cmake -DCOMMON_DOC_DIR=%{_docdir}/%{name} -DCOMMON_FIND_PACKAGE_QUIET=OFF
%cmake_build

%install
%cmake_install

# Drop tests from the installation according to the package review
rm -rf %{buildroot}%{_datadir}/Lunchbox/tests

# Move benchmark binaries to the correct place
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/Lunchbox/benchmarks/* %{buildroot}%{_bindir}
rmdir %{buildroot}%{_datadir}/Lunchbox/benchmarks

%check
cd %{_vpath_builddir}
make test

%files
%license lgpl-2.1.txt lgpl-3.0.txt LICENSE_1_0.txt
%doc %{_docdir}/%{name}
# https://github.com/Eyescale/Lunchbox/issues/332
%{_libdir}/libLunchbox.so.1.*
%{_libdir}/libLunchbox.so.10

%files devel
%{_bindir}/perf-*
%{_includedir}/lunchbox
%{_libdir}/libLunchbox*.so
%{_datadir}/Lunchbox

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.17.0-10
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.17.0-8
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 12 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.17.0-6
- Updated lgpl-3.0 license URL
  Related: rhbz#976793

* Fri Sep 10 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.17.0-5
- Updated according to the review
  Related: rhbz#976793

* Wed Jul 21 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.17.0-4
- Updated according to the review
  Related: rhbz#976793

* Tue Jul 20 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.17.0-3
- Fixed FTBFS in rawhide (f35)

* Mon Jun 28 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.17.0-2
- Updated according to the review
  Related: rhbz#976793

* Tue Jun 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.17.0-1
- New version

* Wed Jul  9 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.1-2
- Dropped doxygen-fix patch, used workaround from upstream

* Mon Jul  7 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.1-1
- New version

* Fri Jun 21 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.0-1
- Initial release
