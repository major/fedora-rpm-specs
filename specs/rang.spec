# We do build some executables, but we don't package them, so no debuginfo
%global debug_package %{nil}

Name: rang
License: Unlicense
Summary: Minimal, header-only, Modern C++ library for terminal goodies

Version: 3.2
Release: 7%{?dist}

URL: https://agauniyal.github.io/rang/
Source0: https://github.com/agauniyal/rang/archive/v%{version}/rang-v%{version}.tar.gz

# Fix tests failing to build
Patch0: 0000-rang-fix-tests.patch

%global with_tests 1

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%if 0%{?with_tests}
BuildRequires: cmake(doctest)
%endif

%global desc %{expand:rang is a minimal, single-header library for colors in your terminal.
rang only depends on C++ standard library, "unistd.h" system header on Unix
and "windows.h" & "io.h" system headers on Windows-based systems.
In other words, you don't need any 3rd party dependencies.
}

%description
%{desc}


%package devel
Summary: %{summary}

%description devel
This package contains development files for programs using the "rang" library.

%{desc}


%prep
%autosetup -p1


%build
%cmake

%if 0%{?with_tests}
pushd test
%cmake
%cmake_build
%endif


%install
%cmake_install


%if 0%{?with_tests}
%check
pushd test/%{__cmake_builddir}
./all_rang_tests
%endif


%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2-2
- Fix BuildRequires

* Thu May 04 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2-1
- Initial packaging
