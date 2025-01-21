Name:             tntnet
Version:          3.0
Release:          12%{?dist}
Summary:          A web application server for web applications
Epoch:            1

# GPLv2+: framework/common/gcryptinit.c
# zlib:   framework/common/unzip.h
# Automatically converted from old format: LGPLv2+ and GPLv2+ and zlib - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND Zlib
URL:              http://www.tntnet.org/
Source0:          http://www.tntnet.org/download/%{name}-%{version}.tar.gz
# http://sourceforge.net/tracker/?func=detail&aid=3542704&group_id=119301&atid=684050
Source1:          %{name}.service
Patch0:           %{name}-%{version}-missing-call-to-setgroups-before-setuid.patch

BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    kernel-headers
BuildRequires:    openssl-devel
BuildRequires:    cxxtools-devel >= 3.0
BuildRequires:    perl-generators
BuildRequires:    zip
BuildRequires:    zlib-devel
BuildRequires:    systemd-units
Requires(pre):    shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

%description
%{summary}

%package          devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:         cxxtools-devel%{?_isa} >= 3.0

%description devel
Development files for %{name}

%prep
%autosetup -p0

%build
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%{buildroot} INSTALL="install -p"

# Systemd unit files
# copy tntnet.service to unitdir /lib/systemd/system
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/doc/
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service

# Find and remove all la files
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%check
test/tntnet-test

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || \
    useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin \
    -c "User" %{name}
exit 0

%post
/sbin/ldconfig
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog README
%license COPYING
%dir %{_sysconfdir}/tntnet
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.xml
%{_unitdir}/%{name}.service
%{_bindir}/ecppc
%{_bindir}/tntnet
%{_libdir}/libtntnet*.so.*
%{_libdir}/tntnet/
%{_datadir}/tntnet/
%exclude %{_datadir}/%{name}/template/
%{_mandir}/man1/ecppc.1.gz
%{_mandir}/man1/tntnet-defcomp.1.gz
%{_mandir}/man7/ecpp.7.gz
%{_mandir}/man7/tntnet.xml.7.gz
%{_mandir}/man8/tntnet.8.gz

%files devel
%{_bindir}/tntnet-project
%{_libdir}/libtntnet*.so
%{_includedir}/tnt/
%{_libdir}/pkgconfig/tntnet.pc
%{_libdir}/pkgconfig/tntnet_sdk.pc
%{_datadir}/%{name}/template/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:3.0-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:3.0-3
- Move template files to devel subpackage

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:3.0-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583

* Mon Mar 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:3.0-1
- Update to 3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
 
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-16
- Fix FTBFS due missing BR gcc-c++ (RHBZ#1606528)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-10
- Added missing-call-to-setgroups-before-setuid.patch
- Mark license files as %%license where available

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-8
- Added epoch for cxxtools-devel

* Thu Sep 24 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-7
- Rebuilt
- added epoch to allow upgrade to older release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.2.1-2
- Own the %%{_datadir}/tntnet dir.
- Run unit tests during build.

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-1
- New release

* Sun Sep 22 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2-8
- Add missing dependency on cxxtools-devel in tntnet-devel (#896003).
- Add missing /sbin/ldconfig calls in %%post and %%postun.
- Using %%defattr is not needed anymore.

* Thu Aug 08 2013 Petr Pisar <ppisar@redhat.com> - 2.2-7
- Perl 5.18 rebuild

* Wed Aug 07 2013 Petr Pisar <ppisar@redhat.com> - 2.2-6
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.2-4
- Perl 5.18 rebuild

* Fri May 10 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-3
- Corrected bogus date format in %%changelog
- Fixed typos in tntnet spec file
- Added minimal cxxtools version requirement

* Thu May 9 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-2
- Corrected requirements
- Rebuild

* Fri May 3 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-1
- New release
- Spec file cleanup

* Thu Aug 23 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-15
- Fixed typos in tntnet spec file

* Wed Aug 22 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-14
- Fix for "Introduce new systemd-rpm macros in tntnet spec file" (#850341)

* Thu Jul 26 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-13
- Added missing BuildRequires systemd-units 

* Thu Jul 26 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-12
- Spec file cleanup
- Changed changelog readability

* Wed Jul 18 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-11
- Added missing build requirement kernel-headers

* Fri Jul 13 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-10
- Added upstream link for gcc 4.7 patch
- Changed license type
- Make install preserve timestamps 

* Tue Jul 3 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-9
- Removed rm in install section
- Removed systemd readme file
- Added link to upstream systemd patch

* Sun Jun 24 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-8
- Removed group and user apache from tntnet.conf
- Added own group tntnet to tntnet.conf
- Added creation of users and groups in pre section

* Thu Jun 21 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-7
- Added systemd-fedora-readme

* Wed Jun 20 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-6
- Changed group and user for fedora to apache

* Sun Jun 17 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-5
- Fixed more missing slash in path
- Fixed missing system unit file

* Sun Jun 17 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-4
- Fixed missing slash in path

* Sat Jun 16 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-3
- Added gcc-4.7 patch
- Added systemd service file
- Removed sysv init stuff
- Cleanup spec file 

* Tue May 29 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-2
- Removed license comment
- Removed empty files
- Fixed Requires and Group tag

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-1
- New release

* Mon Sep 19 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-2
- Cleanup spec a bit

* Sun Sep 18 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-1
- Initial release
