%global commit 1f13bf5c5e86cbc99a6f0492fcdcd38cf0da2105
%global gittag v1.8.6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		rdesktop
Version:	1.9.0
Release:	17%{?dist}
Summary:	X client for remote desktop into Windows Terminal Server

License:	GPL-3.0-or-later
URL:		http://www.rdesktop.org/
#Source0:	https://github.com/%%{name}/%%{name}/archive/%%{commit}/%%{name}-%%{shortcommit}.tar.gz
Source0:	https://github.com/%{name}/%{name}/releases/download/v%{version}/rdesktop-%{version}.tar.gz
# Fix segfault in utils_cert_handle_exception
# https://bugzilla.redhat.com/show_bug.cgi?id=2008044
# https://github.com/rdesktop/rdesktop/pull/394
Patch0:         https://patch-diff.githubusercontent.com/raw/rdesktop/rdesktop/pull/394.patch
# Use system cypto policy
Patch1:         rdesktop-crypto.patch
Patch2: rdesktop-configure-c99.patch
# Upstream fix: use correct modulus and exponent in rdssl_rkey_get_exp_mod
Patch3:         https://github.com/rdesktop/rdesktop/commit/53ba87dc174175e98332e22355ad8662c02880d6.patch
BuildRequires: make
BuildRequires:	gnutls-devel
BuildRequires:	krb5-devel
BuildRequires:	libtasn1-devel
BuildRequires:	libX11-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXrandr-devel
BuildRequires:	nettle-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	autoconf automake libtool

%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 & 2003 Terminal Services, capable of natively speaking 
Remote Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
#setup -q -n %%{name}-%%{commit}
%autosetup -p1

%build
autoreconf -vif
%configure --with-ipv6 --with-sound=pulse
%make_build

%install
%make_install STRIP=/bin/true

%files
%doc COPYING README* doc/{AUTHORS,ChangeLog,HACKING,TODO,*.txt}
%{_bindir}/rdesktop
%{_datadir}/rdesktop/
%{_mandir}/man1/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Orion Poplawski <orion@nwra.com> - 1.9.0-15
- Add upstream patch to use correct modulus and exponent in
  rdssl_rkey_get_exp_mod
- Use SPDX license

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Florian Weimer <fweimer@redhat.com> - 1.9.0-11
- Port configure script to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Orion Poplawski <orion@nwra.com> - 1.9.0-8
- Use system crypto policy

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Orion Poplawski <orion@nwra.com> - 1.9.0-6
- Add patch to fix segfault in utils_cert_handle_exception (bz#2008044)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Charles R. Anderson <cra@wpi.edu> - 1.8.6-1
- Update to 1.9.0
- Use new PulseAudio support rather than libao
- Reenable CredSSP support now that libgssglue is no longer required

* Fri Aug 16 2019 Charles R. Anderson <cra@wpi.edu> - 1.8.6-1
- Update to 1.8.6 release which fixes a bug in 1.8.5.
- 1.8.5 is a security  release to address various buffer overflow 
  and overrun issues in the rdesktop protocol handling.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Charles R. Anderson <cra@wpi.edu> - 1.8.4-2
- Escape macros in comments
- 1.8.4 release security fixes rhbz#1670427:
  CVE-2018-8794 CVE-2018-8795 CVE-2018-8797 CVE-2018-20175 CVE-2018-20176
  CVE-2018-8791 CVE-2018-8792 CVE-2018-8793 CVE-2018-8796 CVE-2018-8798
  CVE-2018-8799 CVE-2018-8800 CVE-2018-20174 CVE-2018-20177 CVE-2018-20178
  CVE-2018-20179 CVE-2018-20180 CVE-2018-20181 CVE-2018-20182

* Sat Jan 26 2019 Charles R. Anderson <cra@wpi.edu> - 1.8.4-1
- Update to 1.8.4 release

* Fri Nov 30 2018 Charles R. Anderson <cra@wpi.edu> - 1.8.4-0.1
- Update to git master

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 02 2014 Dominik Mierzejewski <rpm@greysector.net> - 1.8.3-1
- update to 1.8.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Dominik Mierzejewski <rpm@greysector.net> - 1.8.2-1
- update to 1.8.2

* Mon Jan 06 2014 Jon Disnard <jdisnard@gmail.com> - 1.8.1-2
- Aarch64 autoreconf (bz #926432)

* Mon Dec 23 2013 Dominik Mierzejewski <rpm@greysector.net> - 1.8.1-1
- update to 1.8.1

* Fri Sep 06 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.0-2
- --disable-credssp (f20+, where libgssglue was retired)

* Mon Aug 12 2013 Dominik Mierzejewski <rpm@greysector.net> - 1.8.0-1
- update to 1.8.0
- add missing BuildRequires (also bug #949316)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Kalev Lember <kalevlember@gmail.com> - 1.7.1-1
- Update to 1.7.1
- Dropped the pcsc patch, fixed upstream

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 30 2011 Kalev Lember <kalev@smartlink.ee> - 1.7.0-1
- Update to 1.7.0

* Mon May 30 2011 Kalev Lember <kalev@smartlink.ee> - 1.6.0-12
- Prevent remote file access (CVE-2011-1595)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Dominik Mierzejewski <rpm@greysector.net> - 1.6.0-10
- patch libao output driver to fix segfault (bugs #657172, #657813,
  #658018, #658799, #659072)

* Sat Nov 20 2010 Dominik Mierzejewski <rpm@greysector.net> - 1.6.0-9
- add libao support (supports ALSA and PulseAudio, should fix bugs
  #503431 and #577878)

* Fri Aug 20 2010 Dominik Mierzejewski <rpm@greysector.net> - 1.6.0-8
- drop hard dependency on pcsc-lite (bug #527712)
- fix build against current pcsc-lite
- add a proper source URL

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.0-7
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 1 2009 Soren Sandmann <ssp@redhat.com> - 1.6.0-5
- Enable SmartCard support

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.0-3
- rebuild with new openssl

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0-2
- fix license tag

* Tue May 13 2008 Soren Sandmann <sandmann@redhat.com> - 1.6.0-1
Update to 1.6.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-5
- Autorebuild for GCC 4.3

* Tue Dec  4 2007 Matthias Clasen <mclasen@redhat.com> - 1.5.0-4
- Rebuild against openssl

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.5.0-4
- Rebuild for selinux ppc32 issue.

* Sat Jul 28 2007 Matthias Clasen <mclasen@redhat.com> - 1.5.0-3
- Produce useful debuginfo (#249962)

* Thu Apr 26 2007 David Zeuthen <davidz@redhat.com> - 1.5.0-2
- Fix segfault triggered by X11 update (#238032)

* Sun Nov 19 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Thu Aug 31 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.4.1-4
- configure --with-ipv6 (bug 198405)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.4.1-3.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.4.1-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.4.1-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> - 1.4.1-3
- rebuilt against new openssl

* Tue Nov  1 2005 Carl Worth <cworth@redhat.com> - 1.4.1-2
- Require modular libX11-devel instead of monolithic xorg-x11-devel

* Thu Jun 30 2005 Warren Togami <wtogami@redhat.com> - 1.4.1-1
- 1.4.1

* Sat Mar 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.0-2
- Use the %%configure macro (rdesktop now has a real configure file).
- Patch rdesktop-optflags.patch no longer needed.
- Add several missing doc files.

* Mon Mar 21 2005 David Zeuthen <davidz@redhat.com> 1.4.0-1
- New upstream version; drop some patches that is now upstream
- Require xorg-x11-devel instead of XFree86-devel for building

* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 1.3.1-7
- Rebuild with gcc4

* Thu Nov 18 2004 Than Ngo <than@redhat.com> 1.3.1-6
- add cvs patch to make krdc working again

* Thu Jul 08 2004 Warren Togami <wtogami@redhat.com>
- #127207 Finnish "fi" keymap fix
	  "fi" ISO_Level3_Shift warning fix

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 23 2004 Ville Skyttä <ville.skytta at iki.fi> - 1.3.1-3
- Honor $RPM_OPT_FLAGS.
- Include ChangeLog and TODO in docs.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 11 2004 Warren Togami <wtogami@redhat.com> 1.3.1-1
- upgrade to 1.3.1

* Thu Jan 15 2004 Warren Togami <wtogami@redhat.com> 1.3.0-3
- upgrade to 1.3.0
- improve summary
- BuildPrereq -> BuildRequires, the former is deprecated
- Remove doc files that no longer exist
- Add missing XFree86-devel
- There was no -1 or -2.  Nothing to see here.	Move along.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 10 2003 Alexander Larsson <alexl@redhat.com> 1.2.0-1
- 1.2.0, new stable release
- Removed now-upstream ssl patch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 1.1.0-5
- work around now-private definition of BN_CTX

* Wed Dec 11 2002 Elliot Lee <sopwith@redhat.com> 1.1.0-4
- Fix multilib builds by passing LDLIBS on make command line
- Use _smp_mflags

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- rebuild in current tree

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 12 2002 Alexander Larsson <alexl@redhat.com>
- Initial build.

