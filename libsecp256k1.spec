%global forgeurl https://github.com/Bitcoin-ABC/secp256k1

Name:    libsecp256k1
Version: 0.25.1
Release: 3%{?dist}
Summary: Optimized C library for EC operations on curve secp256k1

%forgemeta
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: gcc
BuildRequires: automake autoconf libtool
BuildRequires: gmp-devel
BuildRequires: openssl-devel
BuildRequires: make

%description
%{summary}.

Includes support for Schnorr signature.

Uses the implementation maintained by Bitcoin-ABC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgesetup

%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful, even on
# architectures were the ASM is not valid when compiling with LTO.
#
# -ffat-lto-objects is sufficient to address this issue.  It is the default
# for F33, but is expected to only be enabled for packages that need it in
# F34, so we use it here explicitly
%define _lto_cflags -flto=auto -ffat-lto-objects

./autogen.sh
%configure --disable-static \
           --enable-module-recovery \
           --enable-experimental \
           --enable-module-ecdh


%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%check
make check


%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.0*

%files devel
%license COPYING
%doc README.md
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Jonny Heggheim <hegjon@gmail.com> - 0.25.1-1
- Updated to version 0.25.1

* Thu Feb 24 2022 Jonny Heggheim <hegjon@gmail.com> - 0.25.0-1
- Updated to version 0.25.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Jeff Law <law@redhat.com> - 0.21.12-4
- Re-enable LTO

* Tue Aug 04 2020 Jonny Heggheim <hegjon@gmail.com> - 0.21.12-3
- Added BuildRequries on gmp-devel and openssl-devel

* Tue Aug 04 2020 Jonny Heggheim <hegjon@gmail.com> - 0.21.12-2
- Enable module-recovery and module-ecdh

* Tue Aug 04 2020 Jonny Heggheim <hegjon@gmail.com> - 0.21.12-1
- Updated to version 0.21.12

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jeff Law <law@redhat.com> - 0.20.9-3
- Disable LTO

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Jonny Heggheim <hegjon@gmail.com> - 0.20.9-1
- Using the implementation by Bitcoin-ABC, includes support for Schnorr

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190222git949e85b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20190221git949e85b
- Updated to 20190221git949e85b
- Added configure flags for schnorrsig

* Thu May 23 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20190210gita34bcaa
- Updated to 20190210gita34bcaa
- Included support for Schnorr module

* Fri Jan 11 2019 Jonny Heggheim <hegjon@gmail.com> - 0-0.20181126gite34ceb3
- Inital packaging
