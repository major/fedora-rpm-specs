%undefine __cmake_in_source_build

Name:		yubihsm-shell
Version:	2.6.0
Release:	3%{?dist}
Summary:	Tools to interact with YubiHSM 2

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0 
URL:		https://github.com/Yubico/%{name}/
Source0:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:	gpgkey-9588EA0F.gpg
# https://github.com/Yubico/yubihsm-shell/pull/430
Patch1: yubihsm-shell-2.6.0-incompatible-pointer.patch
# https://github.com/Yubico/yubihsm-shell/pull/411
Patch2:	yubihsm-shell-2.5.0-pcsc-lite.patch
# https://github.com/Yubico/yubihsm-shell/pull/450
Patch3:	yubihsm-shell-gcc15.patch

BuildRequires:	cmake
BuildRequires:	cppcheck
BuildRequires:	gcc
%if 0%{?fedora}
BuildRequires:	lcov
%endif
BuildRequires:	gengetopt
BuildRequires:	help2man
BuildRequires:	openssl-devel
BuildRequires:	libcurl-devel
BuildRequires:	libedit-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	clang
BuildRequires:	pkg-config
%if 0%{?fedora} > 36
BuildRequires: libusb-compat-0.1-devel
%else
BuildRequires:	libusb-devel
%endif
BuildRequires:	chrpath
BuildRequires:	gnupg2

%description
This package contains most of the components used to interact with
the YubiHSM 2 at both a user-facing and programmatic level.

%package devel
Summary: Development tools for interacting with YubiHSM 2
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for working with yubihsm 2.

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1


%build
%set_build_flags
# https://bugzilla.redhat.com/show_bug.cgi?id=1865658#c6
# The generated code fails to build on s390x in Fedora 33
# For now, disable this particular check when building this arch
%ifarch s390x
export CFLAGS="$CFLAGS -Wno-error=format-overflow"
%endif
# OpenSSL 3.0 deprecates a lot of functions still widely used here
export CFLAGS="$CFLAGS -Wno-error=deprecated-declarations"
%cmake -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build


%install
%cmake_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-shell
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-wrap
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/pkcs11/yubihsm_pkcs11.so


%files
%license LICENSE
%{_bindir}/yubihsm-auth
%{_bindir}/yubihsm-shell
%{_bindir}/yubihsm-wrap
%{_libdir}/libyubihsm.so.2
%{_libdir}/libyubihsm.so.2.*
%{_libdir}/libyubihsm_http.so.2
%{_libdir}/libyubihsm_http.so.2.*
%{_libdir}/libyubihsm_usb.so.2
%{_libdir}/libyubihsm_usb.so.2.*
%{_libdir}/libykhsmauth.so.2
%{_libdir}/libykhsmauth.so.2.*
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/yubihsm_pkcs11.so
%doc 
%{_mandir}/man1/yubihsm-auth.1.*
%{_mandir}/man1/yubihsm-shell.1.*
%{_mandir}/man1/yubihsm-wrap.1.*

%files devel
%{_libdir}/libyubihsm.so
%{_libdir}/libyubihsm_http.so
%{_libdir}/libyubihsm_usb.so
%{_libdir}/libykhsmauth.so
%{_includedir}/yubihsm.h
%{_includedir}/ykhsmauth.h
%dir %{_includedir}/pkcs11
%{_includedir}/pkcs11/pkcs11.h
%{_includedir}/pkcs11/pkcs11y.h
%{_includedir}/pkcs11/pkcs11f.h
%{_includedir}/pkcs11/pkcs11t.h
%{_datadir}/pkgconfig/yubihsm.pc
%{_datadir}/pkgconfig/ykhsmauth.pc



%changelog
* Wed Feb 05 2025 Jakub Jelen <jjelen@redhat.com> - 2.6.0-3
- Fix gcc15 warnings (#2341598)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 11 2024 Jakub Jelen <jjelen@redhat.com> - 2.6.0-1
- New upstream release (#2311424)

* Tue Jul 30 2024 Jakub Jelen <jjelen@redhat.com> - 2.5.0-4
- Fix build against pcsc-lite >= 2.2 (#2301379)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 02 2024 Jakub Jelen <jjelen@redhat.com> - 2.5.0-1
- New upstream release (#2272123)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 08 2023 Jakub Jelen <jjelen@redhat.com> - 2.4.2-1
- New upstream release (#2248609)

* Thu Aug 17 2023 Jakub Jelen <jjelen@redhat.com> - 2.4.1-1
- New upstream release (#2232340)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Jakub Jelen <jjelen@redhat.com> - 2.4.0-1
- New upstream release (#2165239)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Jakub Jelen <jjelen@redhat.com> - 2.3.2-1
- New upstream release (#2100542)

* Tue Feb 22 2022 Veronika Hanulikova <vhanulik@redhat.com> - 2.3.1-1
- New upstream release (#2050104)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Jakub Jelen <jjelen@redhat.com> - 2.3.0b-1
- New upstream release (#2035159)

* Mon Dec 13 2021 Jakub Jelen <jjelen@redhat.com> - 2.3.0-1
- New upstream release (#2030694)

* Thu Nov 18 2021 Jakub Jelen <jjelen@redhat.com> - 2.2.0-5
- Rebuild with deprecated OpenSSL 3.0 functions (#2021878)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.2.0-4
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 03 2021 Jakub Jelen <jjelen@redhat.com> - 2.2.0-3
- Disable rpath to allow build in Fedora 35 (#1988058)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Jakub Jelen <jjelen@redhat.com> - 2.2.0-1
- New upstream release (#1950207)

* Thu Mar 18 2021 Jakub Jelen <jjelen@redhat.com> - 2.1.0-1
- New upstream release (#1936041)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.3-1
- New upstream release (#1889941)

* Thu Aug 06 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-7
- Workaround FTBFS on s390x (#1865658)

* Thu Aug 06 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-6
- Rebuild after libz3 soname bump (#1865658)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 16 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-3
- Avoid warnings/errors with new gcc on s390x (#1800289)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-1
- New upstream release (#1772013)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Jakub Jelen <jjelen@redhat.com> - 2.0.1-1
- New upstream release (#1692935)

* Wed Feb 13 2019 Jakub Jelen <jjelen@redhat.com> - 2.0.0-4
- Workaround unreasonagle error from GCC9 (#1676257)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Jakub Jelen <jjelen@redhat.com> - 2.0.0-2
- Pull the latest signed tarballs
- Address review comments (#1654689)

* Thu Nov 29 2018 Jakub Jelen <jjelen@redhat.com> - 2.0.0-1
- Initial release


