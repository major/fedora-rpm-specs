%define _legacy_common_support 1

Name:		novacom-server
Version:	1.1.0
Release:	0.33.rc1%{?dist}
Summary:	Service for utility that connects to WebOS devices
License:	ASL 2.0
URL:		https://github.com/openwebos/novacomd
Source0:	https://github.com/openwebos/novacomd/tarball/versions/1.1.0-rc1/openwebos-novacomd-submissions-119.1-0-ge77d336.tar.gz
Source1:	novacomd.service
Source2:	config-novacomd
# This patch allows novacomd to work against Fedora's libusb
Patch0:		0001-Use-usb_bulk_-read-write-instead-of-homemade-handler.patch
# This patch forces the makefile to use our CFLAGS
Patch1:		novacomd_add_cflags.patch
# This patch muffles the logging of every packet to the device
Patch2:		novacomd-quiet-logging.patch
# This patch removes unused adler32 library from the makefile
Patch3:		novacomd-makefile-remove-adler32.patch
%{?systemd_requires}
Provides:	novacomd = %{version}-%{release}
BuildRequires: make
BuildRequires:	gcc
BuildRequires:	libusb-devel
BuildRequires:	systemd

%description
This service allows the novacom client to connect to WebOS devices that are
connected over USB.

It should be started using 'systemctl start novacomd.service' as root.

%prep
%setup -q -n openwebos-novacomd-e77d336
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Remove unused and unneeded zlib headers and adler32 library
rm -f src/lib/cksum/adler32.c
rm -f src/lib/cksum/zlib.h

%build
make host LDFLAGS="%{__global_ldflags}" CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -pm 755 build-novacomd-host/novacomd $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/default
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/default/novacomd

%post
%systemd_post novacomd.service

%preun
%systemd_preun novacomd.service

%postun
%systemd_postun_with_restart novacomd.service

%files
%doc README.md
%{_bindir}/novacomd
%{_unitdir}/novacomd.service
%config(noreplace) %{_sysconfdir}/default/novacomd

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.33.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.32.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.31.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-0.30.rc1
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.29.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.28.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Jonathan Dieter <jdieter@gmail.com> - 1.1.0-0.27.rc1
- Work around build failure with GCC 10
- Remove unneeded hardened_build flag (since all builds are hardened now)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.26.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.25.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.24.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.23.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Jonathan Dieter <jdieter@gmail.com> - 1.1.0-0.22.rc1
- Add BuildRequires: gcc

* Wed Feb 14 2018 Jonathan Dieter <jdieter@gmail.com> - 1.1.0-0.21.rc1
- Remove %%{isa} from BR (Fixes bug #1545200)

* Thu Feb 08 2018 Jonathan Dieter <jdieter@gmail.com> - 1.1.0-0.20.rc1
- Remove obsolete Group and Buildroot tags, and stop removing buildroot on install

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.19.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Jonathan Dieter <jdieter@gmail.com> - 1.1.0-0.18.rc1
- Fix systemd Requires and BuildRequires

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.17.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.16.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.15.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.14.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.13.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.12.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.11.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.10.rc1
- Use new systemd macros (way overdue) (#850230)
- Enable PIE flags for daemon (also way overdue (#955314)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.7.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.6.rc1
- Preserve timestamps during install
- Remove unused zlib header and adler32 code
- Remove unnecessary filler that's not needed for Fedora

* Sun May  6 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.5.rc1
- Let's try this one again.  This time really muffle logging of every packet
  sent to device

* Wed May  2 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.4.rc1
- Muffle logging of every packet sent to device

* Thu Apr 26 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.3.rc1
- Use consistent RPM_OPT_FLAGS and RPM_BUILD_ROOT variables
- Change define macro to global
- Remove unnecessary BR: glibc-devel
- Turn on hardened build
- Fix provides for novacomd

* Thu Apr 12 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.2.rc1
- Rename to novacom-server and add provides for novacomd
- Add systemd service

* Mon Apr  2 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.1.rc1
- Add patch that allows novacomd to work against Fedora's libusb

* Sat Mar 31 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.9-0.1.git.e77d33616f
- Initial release
