Name:           libsfdo
Version:        0.1.3
Release:        1%{?dist}
Summary:        A collection of libraries implementing freedesktop.org specifications

License:        BSD-2-Clause
URL:            https://gitlab.freedesktop.org/vyivel/libsfdo
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libsfdo-*.so.0

%files devel
%{_includedir}/sfdo-*.h
%{_libdir}/libsfdo-*.so
%{_libdir}/pkgconfig/libsfdo-*.pc

%changelog
* Sat Oct 26 2024 Steve Cossette <farchord@gmail.com> - 0.1.3-1
- 0.1.3
