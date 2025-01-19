Name:           monocypher
Version:        3.1.2
Release:        11%{?dist}
Summary:        Boring crypto that simply works

# Automatically converted from old format: BSD or CC0 - review is highly recommended.
License:        LicenseRef-Callaway-BSD OR CC0-1.0
URL:            https://monocypher.org/
Source0:        https://monocypher.org/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Monocypher is an easy to use cryptographic library. It provides functions for
authenticated encryption, hashing, password hashing and key derivation, key
exchange, and public key signatures. It is:

- Small. Monocypher contains under 2000 lines of code, small enough to allow
audits. The binaries can be under 50KB, small enough for many embedded targets.
- Easy to deploy. Just add monocypher.c and monocypher.h to your project. They
compile as C99 or C++ and are dedicated to the public domain (CC0-1.0,
alternatively 2-clause BSD).
- Portable. There are no dependencies, not even on libc.
- Honest. The API is small, consistent, and cannot fail on correct input.
- Direct. The abstractions are minimal. A developer with experience in applied
cryptography can be productive in minutes.
- Fast. The primitives are fast to begin with, and performance wasn't
needlessly sacrificed. Monocypher holds up pretty well against Libsodium,
despite being closer in size to TweetNaCl.

%package devel
Summary:        Development files for monocypher
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains the development files for monocypher.

%prep
%autosetup

%build
export CFLAGS="${RPM_OPT_FLAGS}"
%make_build CFLAGS="${RPM_OPT_FLAGS}"

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -v %{buildroot}%{_libdir}/*.a

%check
make check CFLAGS="${RPM_OPT_FLAGS}"

%files
%doc AUTHORS.md README.md CHANGELOG.md
%license LICENCE.md
%{_libdir}/libmonocypher.so.3

%files devel
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 2 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.2-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Patrik Polakovič <patrik@alphamail.org> - 3.1.2-1
- Initial package.

