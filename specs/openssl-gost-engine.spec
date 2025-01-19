Name: openssl-gost-engine
Version: 3.0.3
Release: 5%{?dist}

URL: https://github.com/gost-engine/engine
License: OpenSSL
Summary: A reference implementation of the Russian GOST crypto algorithms for OpenSSL

Source: https://github.com/gost-engine/engine/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1: 01-engine-nowerror.patch

BuildRequires: make
BuildRequires: cmake-rpm-macros gcc perl-Test-Simple
BuildRequires: cmake openssl-devel pkgconf-pkg-config

%{?!_without_check:%{?!_disable_check:BuildRequires: perl-devel openssl}}

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%package -n gostsum
Summary: GOST file digesting utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n gostsum
GOST file digesting utilities.

%global _enginesdir %(pkg-config --variable=enginesdir libcrypto)
%global _providersdir %(pkg-config --variable=modulesdir libcrypto)
%prep
%autosetup -n engine-%version

%build
%cmake -B "%{_vpath_builddir}"

%make_build -C "%{_vpath_builddir}"

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
mkdir -p %buildroot%_enginesdir
mkdir -p %buildroot%_providersdir
cp "%{_vpath_builddir}"/bin/gost.so README.gost %buildroot%_enginesdir/
cp "%{_vpath_builddir}"/bin/gostprov.so %buildroot%_providersdir/
cp "%{_vpath_builddir}"/bin/gost*sum %buildroot%_bindir/
cp gost*sum.1 %buildroot%_mandir/man1/

%check
echo "ALL" > "$PWD/openssl-crypto-policy.override"
OPENSSL_ENGINES="$PWD/%{_vpath_builddir}/bin" \
	OPENSSL_SYSTEM_CIPHERS_OVERRIDE="$PWD/openssl-crypto-policy.override" \
	LD_LIBRARY_PATH="$PWD/%{_vpath_builddir}/bin" \
	CTEST_OUTPUT_ON_FAILURE=1 \
	make -C "%{_vpath_builddir}" test ARGS="--verbose"

%files
%_enginesdir/gost.so
%_providersdir/gostprov.so
%doc %_enginesdir/README.gost

%files -n gostsum
%_bindir/gost*sum*
%_mandir/man1/gost*sum*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Dmitry Belyavskiy <dbelyavs@redhat.com> - 3.0.3-1
- Update to version 3.0.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Dmitry Belyavskiy <dbelyavs@redhat.com> - 3.0.1-1
- Update to version 3.0.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Alexander Bokovoy <abokovoy@redhat.com> - 3.0.0-1
- Final release for OpenSSL 3.0.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.1.1.0-0.4
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Alexander Bokovoy <abokovoy@redhat.com> - 1.1.1.0-0.1
- Initial build for upcoming gost-engine release 1.1.1.0
- Fixes: rhbz#1865169

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Dmitry Belyavskiy <beldmit@gmail.com> - 1.1.0.3-3
- Update after review by Tomas Mraz

* Sun Oct 07 2018 Dmitry Belyavskiy <beldmit@gmail.com> - 1.1.0.3-2
- Update after rpmlint

* Thu Oct 04 2018 Alexander Bokovoy <abokovoy@redhat.com> 1.1.0.3-1
- Initial build using git master commit 3383ad1
