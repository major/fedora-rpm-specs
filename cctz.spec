Name:           cctz
Version:        2.3
%global sover   2
Release:        10%{?dist}
License:        ASL 2.0
Summary:        Translating between absolute and civil times using time zone rules
Url:            https://github.com/google/cctz
Source0:        https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://sources.debian.org/patches/cctz/2.2+dfsg1-1/0001-Compile-shared-lib-and-install-it.patch/
Patch0001:      0001-Compile-library-as-shared.patch

BuildRequires:  tzdata
BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gtest-devel >= 1.8.0
BuildRequires:  gmock-devel >= 1.8.0
BuildRequires:  google-benchmark-devel

Requires:       tzdata

%description
CCTZ contains two libraries that cooperate with <chrono> to give C++
programmers all the necessary tools for computing with dates, times, and time
zones in a simple and correct manner. The libraries in CCTZ are:
  * The Civil-Time Library - This is a header-only library that supports
    computing with human-scale time, such as dates (which are represented by
    the cctz::civil_day class).
  * The Time-Zone Library - This library uses the IANA time zone database that
    is installed on the system to convert between absolute time and civil time.


%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Development files for %{name} library.


%prep
%autosetup -p1


%build
# Version and shared library version match Debian's.
%cmake -DVERSION=%{version} -DSOVERSION=%{sover}
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%doc README.md
%license LICENSE.txt
%{_bindir}/time_tool
%{_libdir}/libcctz.so.%{sover}
%{_libdir}/libcctz.so.%{version}

%files devel
%doc examples
%{_includedir}/cctz
%{_libdir}/libcctz.so
%{_libdir}/cmake/cctz


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-4
- Enable google-benchmark in build as it's now available

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-2
- Remove example build artifacts from documentation

* Tue Mar 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-1
- Initial package release
