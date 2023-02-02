Name:           bloaty
Version:        1.1
Release:        19%{?dist}
Summary:        A size profiler for binaries


License:        ASL 2.0
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
%patch2 -p1


%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBLOATY_ENABLE_CMAKETARGETS=OFF \
  -DBUILD_TESTING=ON
%cmake_build


%install
%cmake_install

%check
%ctest --verbose || exit 0

%files
%license LICENSE
%doc README.md how-bloaty-works.md 
%{_bindir}/bloaty


%changelog
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
