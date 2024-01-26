# For testing
# Depends on downloading and being in a git repo
%bcond_with test

# Header only package
%global debug_package %{nil}

Summary:        Functional Programming Library for C++
Name:           fplus
License:        BSL-1.0
Version:        0.2.22
Release:        3%{?dist}

URL:            https://github.com/Dobiasd/FunctionalPlus
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/FunctionalPlus-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
FunctionalPlus is a small header-only library supporting you in
reducing code noise and in dealing with only one single level
of abstraction at a time. By increasing brevity and maintainability
of your code it can improve productivity (and fun!) in the long
run. It pursues these goals by providing pure and easy-to-use
functions that free you from implementing commonly used flows of
control over and over again.

%package devel

Summary:        Functional Programming Library for C++
Provides:       %{name}-static = %{version}-%{release}

%description devel
FunctionalPlus is a small header-only library supporting you in
reducing code noise and in dealing with only one single level
of abstraction at a time. By increasing brevity and maintainability
of your code it can improve productivity (and fun!) in the long
run. It pursues these goals by providing pure and easy-to-use
functions that free you from implementing commonly used flows of
control over and over again.

%prep
%autosetup -p1 -n FunctionalPlus-%{version}

# License check flags this as BSD 3-Clause
# api_search not distributed, remove to make license simpler
rm -rf api_search

%build
%cmake 
%cmake_build

%if %{with test}
%check
%ctest
%endif

%install
%cmake_install

%files devel
%dir %_includedir/%{name}
%dir %_includedir/%{name}/internal
%dir %_includedir/%{name}/internal/asserts
%license LICENSE
%doc README.md
%_includedir/%{name}/*_defines
%_includedir/%{name}/*.hpp
%_includedir/%{name}/internal/*.hpp
%_includedir/%{name}/internal/asserts/*.hpp
%_libdir/cmake/FunctionalPlus/

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Tom Rix <trix@redhat.com> - 0.2.22-1
- Update to 0.2.22
- Fix summary

* Fri Dec 15 2023 Tom Rix <trix@redhat.com> - 0.2.20-1
- Initial package
