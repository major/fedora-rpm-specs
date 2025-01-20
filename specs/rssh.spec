Name:           rssh
Version:        2.3.4
Release:        31%{?dist}
Summary:        Restricted shell for use with OpenSSH, allowing only scp and/or sftp
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD 
URL:            http://www.pizzashack.org/rssh/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz.sig
Patch0:         rssh-2.3.4-makefile.patch
Patch2:         rssh-2.3.4-command-line-error.patch
# https://sourceforge.net/p/rssh/mailman/message/36536555/
# CVE-2019-3463 CVE-2019-3464 007
Patch3:         rssh-2.3.4-Verify-rsync-command-options.patch
# https://sourceforge.net/p/rssh/mailman/message/36530715/
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=919623
# CVE-2019-1000018 009
Patch4:         rssh-2.3.4-Verify-scp-command-options.patch
# 010
Patch5:         rssh-2.3.4-Check-command-line-after-chroot.patch
Patch6:         rssh-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openssh-server
BuildRequires:  openssh-clients
BuildRequires:  cvs
BuildRequires:  rsync
BuildRequires:  rdist
Requires:       openssh-server
Requires(pre):  shadow-utils


%description
rssh is a restricted shell for use with OpenSSH, allowing only scp
and/or sftp. For example, if you have a server which you only want
to allow users to copy files off of via scp, without providing shell
access, you can use rssh to do that. It is a alternative to scponly.


%prep
%setup -q
%patch -P0 -p1 -b .makefile
%patch -P2 -p1 -b .cmdline-error
%patch -P3 -p1 -b .rsync_opts
%patch -P4 -p1 -b .scp_opts
%patch -P5 -p1 -b .chroot_cmd
%patch -P6 -p1 -b .c99

chmod 644 conf_convert.sh
chmod 644 mkchroot.sh


%build
%configure
%make_build


%install
%make_install
# since rssh 2.3.4, default config is installed as rssh.conf.default,
# rename it for packaging in rpm
mv %{buildroot}/%{_sysconfdir}/rssh.conf{.default,}


%pre
getent group rsshusers >/dev/null || groupadd -r rsshusers
exit 0


%files
%license COPYING
%doc AUTHORS ChangeLog CHROOT NEWS README SECURITY TODO
%doc conf_convert.sh mkchroot.sh
%{_mandir}/man1/rssh.1*
%{_mandir}/man5/rssh.conf.5*
%config(noreplace) %{_sysconfdir}/rssh.conf
%attr(750, root, rsshusers) %{_bindir}/rssh
%attr(4750, root, rsshusers) %{_libexecdir}/rssh_chroot_helper


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.4-30
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 2.3.4-24
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Frederick Lefebvre <fredlef@amazon.com> - 2.3.4-16
- Fix regression in patch for CVE-2019-1000018.

* Wed Oct 30 2019 Xavier Bachelot <xavier@bachelot.org> - 2.3.4-15
- Clean up specfile.
- Add patches for CVE-2019-3463, CVE-2019-3464 and CVE-2019-1000018.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Tomas Hoger <thoger@fedoraproject.org> - 2.3.4-1
- Update to upstream version 2.3.4, which fixes CVE-2012-3478 and CVE-2012-2252
- Updated rsync-protocol.patch to fix CVE-2012-2251, and to apply on top of the
  CVE-2012-3478 and CVE-2012-2252 fixes.
- Updated makefile.patch to preserve RPM CFLAGS.
- Added command-line-error.patch (from Debian), correcting error message
  generated when insecure command line option is used (CVE-2012-3478 fix
  regression).

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb  6 2012 Daniel Drake <dsd@laptop.org> - 2.3.3-3
- Add patch for rsync3 compat (#485946)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 19 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 2.3.3-1
- Upstream security fix release.  Resolves rhbz#705904

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 30 2008 Ian Weller <ianweller@gmail.com> - 2.3.2-5
- Remove pre and post scripts
  - https://bugzilla.redhat.com/show_bug.cgi?id=456182#c17

* Mon Aug 11 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 2.3.2-4
- Fix review issues and apply patch

* Thu Aug 07 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 2.3.2-3
- Fix postun to remove rssh shell

* Wed Jul 30 2008 Rahul Sundaram <sundaram@fedoraproject.org>  - 2.3.2-2
- Fix BR and defattr. Added a group and shell

* Tue Jul 22 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 2.3.2-1
- initial spec

