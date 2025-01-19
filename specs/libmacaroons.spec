Name:		libmacaroons
Version:	0.3.0
Release:	21%{?dist}
Summary:	C library supporting generation and use of macaroons

License:	BSD-3-Clause AND ISC
URL:		https://github.com/rescrv/libmacaroons
Source0:	%url/archive/releases/%{version}/%{name}-%{version}.tar.gz
# Fix for the inspect() method triggering an assert on newer versions of libsodium.
# See the upstream PR: https://github.com/rescrv/libmacaroons/pull/52
Patch0:		libmacaroons-hex-encoding.patch

# Fix for the memory leak when the deserialize routine succeeds.
# See the upstream PR: https://github.com/rescrv/libmacaroons/pull/56
Patch1:		libmacaroons-deserialize-memleak.patch

BuildRequires:	libsodium-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python3
BuildRequires:	make

%description
%{summary}

%package devel
Summary:	Development libraries linking against libmacaroons
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -q -n %{name}-releases-%{version}
%patch -P0 -p 1
%patch -P1 -p 1

%build
autoreconf -i
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la

%files
%license LICENSE
%doc README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/macaroons.h

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 02 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.0-20
- Update License tag

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 0.3.0-15
- rebuild for new libsodium

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Brian Bockelman <brian.bockelman@cern.ch> - 0.3.0-2
- Fix memory leak when deserializing a macaroon.

* Mon Mar 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Subpackage python2-macaroons has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Brian Bockelman <bbockelm@cse.unl.edu> - 0.3.0-1
- Initial packaging of libmacaroons.


