Name:           bloaty
Version:        1.1
Release:        24%{?dist}
Summary:        A size profiler for binaries

# The entire source is Apache-2.0, except:
#
# BSD-2-Clause:
#   third_party/freebsd_elf/
# APSL-2.0:
#   third_party/darwin_xnu_macho/ except as below:
# APSL-2.0 AND BSD-4-Clause-UC:
#   third_party/darwin_xnu_macho/mach-o/nlist.h
# APSL-2.0 AND BSD-3-Clause
#   third_party/darwin_xnu_macho/mach-o/reloc.h
#
# Note that the contents of third_party/freebsd_elf/ and
# third_party/darwin_xnu_macho/ *are* used in the Linux build (to support
# examining binaries built for other platforms).
License:        Apache-2.0 AND BSD-2-Clause AND BSD-4-Clause-UC AND BSD-3-Clause
URL:            https://github.com/google/bloaty
Source0:        https://github.com/google/bloaty/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch to use system versions of abseil, google-test and google-mock
Patch0:         bloaty-1.1-absl.patch
# Patch to fix size detection function to use 64 bit types on 32bit architectures
Patch1:         bloaty-1.1-longlong.patch
# Add missing #include needed on GCC13
# https://github.com/google/bloaty/pull/332
Patch2:         %{url}/pull/332.patch

BuildRequires:  abseil-cpp-devel
BuildRequires:  capstone-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
BuildRequires:  re2-devel

BuildRequires:  help2man

%description
Ever wondered what's making your binary big? Bloaty McBloatface will show
you a size profile of the binary so you can understand what's taking up
space inside.

Bloaty works on binaries, shared objects, object files, and static
libraries. Bloaty supports the ELF and Mach-O formats, and has experimental
support for WebAssembly.

%prep
%autosetup -S gendiff -N
%autopatch -p0 -M 1
%autopatch -p1 -m 2


%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBLOATY_ENABLE_CMAKETARGETS=OFF \
  -DBUILD_TESTING=ON
%cmake_build
help2man --no-info --output=bloaty.1 %{_vpath_builddir}/bloaty


%install
%cmake_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 bloaty.1

%check
%ctest --verbose || exit 0

%files
%license LICENSE
%doc README.md how-bloaty-works.md 
%{_bindir}/bloaty
%{_mandir}/man1/bloaty.1*


%changelog
* Tue Nov 14 2023 Rich Mattes <richmattes@gmail.com> - 1.1-24
- Rebuild for capstone-5.0.1

* Fri Sep 01 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1-23
- Update License to SPDX
- Stop using deprecated %%patchN macros
- Add an automatically-generated man page

* Wed Aug 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1-22
- Rebuilt for abseil-cpp 20230802.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Rich Mattes <richmattes@gmail.com> - 1.1-20
- Rebuild for abseil-cpp-20230125.1

* Thu Jan 26 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1-19
- Patch for GCC 13

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Rich Mattes <richmattes@gmail.com> - 1.1-17
- Rebuilt for abseil-cpp 20220623.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 09 2022 Rich Mattes <richmattes@gmail.com> - 1.1-15
- Rebuild for abseil-cpp 20211102.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.1-13
- Rebuilt for libre2.so.9

* Sun Nov 07 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1-12
- rebuild for new protobuf

* Sun Oct 24 2021 Adrian Reber <adrian@lisas.de> - 1.1-11
- Rebuilt for protobuf 3.18.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rich Mattes <richmattes@gmail.com> - 1.1-9
- Rebuild for abseil-cpp-20210324.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 08:55:29 CET 2021 Adrian Reber <adrian@lisas.de> - 1.1-7
- Rebuilt for protobuf 3.14

* Sat Dec 19 11:31:29 EST 2020 Rich Mattes <richmattes@gmail.com> - 1.1-6
- Rebuild for abseil-cpp 20200923.2

* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 1.1-5
- Rebuilt for protobuf 3.13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Rich Mattes <richmattes@gmail.com> - 1.1-2
- Don't remove buildroot in install
- Patch to use system gtest and gmock, enable tests

* Sat May 23 2020 Rich Mattes <richmattes@gmail.com> - 1.1-1
- Inital Package 
