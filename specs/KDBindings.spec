# Bindings only
%global debug_package %{nil}

Name:           KDBindings
Version:        1.1.0
Release:        1%{?dist}
Summary:        Reactive programming & data binding in C++

License:        BSD-3-Clause AND MIT
URL:            https://github.com/KDAB/KDBindings
Source0:        https://github.com/KDAB/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description    devel
Reactive programming & data binding in C++.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# Removing "built" licenses, already included from source
rm -rf %{buildroot}%{_datadir}/doc/KDBindings

%check
%ctest

%files devel
%license LICENSES/*
%doc README.md ChangeLog
%{_includedir}/kdbindings/
%{_libdir}/cmake/KDBindings/

%changelog
* Sat Nov 29 2025 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- Initial Release
