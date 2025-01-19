# Tests fail to build with
# LLVM ERROR: Cannot select: intrinsic %%llvm.objc.clang.arc.use
# https://bugs.llvm.org/show_bug.cgi?id=49717
%bcond_with tests

%global toolchain clang

Name:           libobjc2
Version:        2.1
Release:        12%{?dist}
Summary:        GNUstep Objective-C runtime library
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/gnustep/libobjc2
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Don't use CXXFLAGS when compiling eh_trampoline.cc
Patch0:         %{url}/commit/365e53632e8be41e49f21ee47a63e41be424a237.patch

BuildRequires:  sed
BuildRequires:  cmake
BuildRequires:  clang >= 7.0.1
BuildRequires:  libdispatch-devel >= 1.3
BuildRequires:  robin-map-devel

# libdispatch is not available on these architectures
ExcludeArch:    armv7hl i686 ppc64le s390x

%description
The GNUstep Objective-C runtime is designed as a drop-in replacement for the
GCC runtime. It supports both a legacy and a modern ABI, allowing code compiled
with old versions of GCC to be supported without requiring recompilation.
The modern ABI adds the following features:

* Non-fragile instance variables.
* Protocol uniquing.
* Object planes support.
* Declared property introspection.

Both ABIs support the following feature above and beyond the GCC runtime:

* The modern Objective-C runtime APIs, introduced with OS X 10.5.
* Blocks (closures).
* Low memory profile for platforms where memory usage is more important than
  speed.
* Synthesised property accessors.
* Efficient support for @synchronized()
* Type-dependent dispatch, eliminating stack corruption from mismatched
  selectors.
* Support for the associated reference APIs introduced with Mac OS X 10.6.
* Support for the automatic reference counting APIs introduced with Mac OS X
  10.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1
# replace bundled robin-map with the system one
mkdir -p third_party/robin-map/include
ln -s %{_includedir}/tsl third_party/robin-map/include/

# drop flag conflicting with FORTIFY_SOURCE
sed -e 's/-O0//g' -i CMakeLists.txt Test/CMakeLists.txt

%build
%cmake \
%if %{with tests}
%else
  -DTESTS=OFF \
%endif
  -DCMAKE_INSTALL_LIBDIR=%{_lib}

%cmake_build

%install
%cmake_install

# Workaround for https://github.com/gnustep/libobjc2/issues/199
mv %{buildroot}%{_includedir}/Block.h %{buildroot}%{_includedir}/Block-libobjc.h

%if %{with tests}
%check
%ctest
%endif

%files
%license COPYING
%doc README.md ANNOUNCE.%{version}
%{_libdir}/libobjc.so.*

%files devel
%{_includedir}/*.h
%{_includedir}/objc
%{_libdir}/libobjc.so
%{_libdir}/pkgconfig/libobjc.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul  3 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.1-2
- Update source URL

* Fri Jul  2 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.1-1
- Initial Fedora packaging
- Convert tabs to spaces and wrap description to 80 cols
- Drop el7 logic and update BuildRequires
- Switch to using the cmake macros
- Replace bundled robin-map with the system one
- Backport upstream build fix
- Misc specfile fixes to comply with the Fedora policy

* Thu Aug 27 2020 Sergii Stoian <stoyan255@gmail.com> - 2.1-0
- Switch to new ObjC library realease - 2.1

* Wed Apr 29 2020 Sergii Stoian <stoyan255@gmail.com> - 2.0-4
- Use clang from RedHat SCL repo on CentOS 7.
- Source file should be downloaded with `spectool -g` command into
  SOURCES directory manually.
- SPEC file adopted for Fedora 31.

* Thu May  2 2019 Sergii Stoian <stoyan255@gmail.com> - 2.0-3
- build with released 2.0 verion of libobjc2

* Fri Mar 29 2019 Sergii Stoian <stoyan255@gmail.com> - 2.0-2
- now library can be build without GNUstep Make installed
- switch to libobjc2 installation routines

* Wed Mar 27 2019 Sergii Stoian <stoyan255@gmail.com> - 2.0-1
- Fix an issue with incorrect offsets for the first ivar.
- Rework some of the ivar offset calculations.

* Fri Mar 22 2019 Sergii Stoian <stoyan255@gmail.com> 2.0
- New 2.0 version that aimed to build by clang 7.0.

* Wed Oct 12 2016 Sergii Stoian <stoyan255@gmail.com> 1.8.2-1
- Initial spec.
