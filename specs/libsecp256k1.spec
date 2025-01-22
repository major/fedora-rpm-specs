%global forgeurl https://github.com/bitcoin-core/secp256k1

Name:    libsecp256k1
Epoch:   1
Version: 0.6.0
Release: 2%{?dist}
Summary: Optimized C library for EC operations on curve secp256k1

%forgemeta
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: automake autoconf libtool
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: make
BuildRequires: openssl-devel

%description
%{summary}.

Includes support for Schnorr signature.

Uses the implementation maintained by Bitcoin Core.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgesetup

%build
./autogen.sh
%configure \
    --disable-static \
    --disable-benchmark \
    --disable-coverage \
    --enable-module-ecdh \
    --enable-module-recovery \
    --enable-module-extrakeys \
    --enable-module-schnorrsig \
    --enable-tests \
    --enable-exhaustive-tests \
    --with-gnu-ld

%make_build

%install
%make_install

%check
make check


%files
%license COPYING
%doc README.md
%doc CHANGELOG.md
%doc SECURITY.md
%{_libdir}/%{name}.so.5
%{_libdir}/%{name}.so.5.0.0

%files devel
%license COPYING
%doc README.md
%doc examples
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov  4 2024 Peter Lemenkov <lemenkov@gmail.com> - 1:0.6.0-1
- Updated to version 0.6.0

* Fri Aug 16 2024 Peter Lemenkov <lemenkov@gmail.com> - 1:0.5.1-1
- Updated to version 0.5.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Jonny Heggheim <hegjon@gmail.com> - 0.4.1-1
- Using the implementation by Bitcoin Core
- Set epoch to 1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
