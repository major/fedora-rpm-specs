Name:           slim
Version:        1.4.0
Release:        10%{?dist}
Summary:        Simple Login Manager
License:        GPL-2.0-or-later
#changed from GPLv2+ per BZ: 2173236, comment 11 and https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_2

URL:            https://sourceforge.net/projects/slim-fork/
Source0:        https://versaweb.dl.sourceforge.net/project/%{name}-fork/%{name}-%{version}.tar.gz
# stolen from xdm
Source1:        %{name}.pam
# adapted from debian to use freedesktop
Source2:        slim-update_slim_wmlist
Source3:        slim-dynwm
Source4:        slim-fedora.txt
# logrotate entry (see bz#573743)
Source5:        slim.logrotate.d
Source6:        slim-tmpfiles.conf
Source7:        slim.service
patch0:	        slim-1.4.0-fedora.patch  
patch1:         slim-1.4.0-selinux.patch

## Keyring copied on 2023-02-26 from: xfontsel.gpg

# Fedora-specific patches
#%patch  0
#%patch 1 
#slim-1.4.0-fedora.patch
#%patch 2         
#slim-1.4.0-selinux.patch
#Patch3:         slim-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXmu-devel libXft-devel libXrender-devel
BuildRequires:  libpng-devel libjpeg-devel freetype-devel fontconfig-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig gettext libselinux-devel pam-devel cmake
BuildRequires:  scrot xterm freeglut-devel libXrandr-devel
BuildRequires:  cmake

Requires:       scrot xterm /sbin/shutdown
Requires:       %{_sysconfdir}/pam.d
# we use 'include' in the pam file, so
Requires:       pam >= 0.80
# reuse the images
Requires:       f%{?fedora}-backgrounds-base

# for anaconda dnf
Provides:       service(graphical-login)

BuildRequires:    systemd
BuildRequires:    systemd-rpm-macros

%description
SLiM (Simple Login Manager) is a graphical login manager for X11.
It aims to be simple, fast and independent from the various
desktop environments.
SLiM is based on latest stable release of Login.app by Per LidÃ©n.

In the distribution, slim may be called through a wrapper, slim-dynwm,
which determines the available window managers using the freedesktop
information and modifies the slim configuration file accordingly,
before launching slim.

%prep
%setup -q

%patch 0 -p0 -b .fedora
%patch 1 -p1 -b .selinux
cp -p %{SOURCE4} README.Fedora
#%patch3 -p1 -b .gcc11 # no longer needed

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS -lXft"
%cmake -DUSE_PAM=yes -DUSE_CONSOLEKIT=no -DBUILD_SHARED_LIBS=no -DBUILD_SLIMLOCK=yes
%cmake_build

%install
%cmake_install
install -p -m755 %{SOURCE2} %{buildroot}%{_bindir}/update_slim_wmlist
install -p -m755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-dynwm
chmod 0644 %{buildroot}%{_sysconfdir}/%{name}.conf
install -d -m755 %{buildroot}%{_sysconfdir}/pam.d
install -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/%{name}
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
rm -f %{buildroot}%{_datadir}/%{name}/themes/default/background.jpg
ln -s ../../../backgrounds/f%{?fedora}/default/f%{?fedora}-01-day.png %{buildroot}%{_datadir}/%{name}/themes/default/background.png
# install logrotate entry
install -m0644 -D %{SOURCE5} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

install -p -D %{SOURCE6} %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE7} %{buildroot}%{_unitdir}/%{name}.service

# Fix lib dir according to bits of system
mkdir -p %{buildroot}/%{_libdir}/
#mv %{buildroot}/usr/lib/lib%{name}.so* %{buildroot}/%{_libdir}/ | :
# rm garbage from instaler
#rm %{buildroot}/lib/systemd/system/%{name}.service
# devel .so
# rm %{buildroot}/%{_libdir}/lib%{name}.so

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%doc ChangeLog README* THEMES TODO
%license COPYING
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/logrotate.d/%{name}
%ghost %dir %{_localstatedir}/run/%{name}
%{_bindir}/%{name}*
%{_bindir}/update_slim_wmlist
%{_mandir}/man1/%{name}*.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes/
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 14 2023 Ranjan Maitra <aarem@Fedoraproject.org> - 1.4.0-6
- Bumped up version, really does nothing new

* Sun May 14 2023 Ranjan Maitra <aarem@Fedoraproject.org> - 1.4.0-5
- Changed invocation of patch, since patchN is deprecated.

* Fri Mar 03 2023 Ranjan Maitra <aarem@Fedoraproject.org> - 1.4.0-4
- Changed  %cmake -DUSE_PAM=yes  to %cmake -DUSE_PAM=yes -DUSE_CONSOLEKIT=no -DBUILD_SHARED_LIBS=no -DBUILD_SLIMLOCK=yes (per RH BZ #2173236, comment #18)
- Also removed rm %{buildroot}/%{_libdir}/lib%{name}.so as a consequence	- Removed %{_libdir}/lib%{name}.so.%{version} from before the config files
-Changed daemon default to no in slim.conf

* Mon Feb 27 2023 Ranjan Maitra <aarem@Fedoraproject.org> - 1.4.0-3
- changed #GPLv2+ to be a comment in new line, per RH BZ #2173236, comment #11

* Sun Feb 26 2023 Ranjan Maitra <aarem@Fedoraproject.org> - 1.4.0-2
- Changed default theme to the current Fedora theme
- dropped desktop-backgrounds-basic and included f%{fedora}-backgrounds-base

* Sat Feb 25 2023 Ranjan Maitra <aarem@Fedoraproject.org> - 1.4.0-1
- Rebuilt 1.4.0 from slim-fork
- Updated Fedora and selinux patches to correspond to 1.4.0
- Note no need to remove files from slim.service and libslim.so.
- selinux patch now removes xserver_arguments   -nolisten tcp -deferglyphs 16
- TOD0: changes to the default wallpaoer for Fedora, perhaps through a patch

* Sat Feb 25 2023 Ranjan Maitra <aarem@Fedoraproject.org> - 1.3.6-23
- Rebuilt for Fedora unretired package
- Follows comments by lichaoran and Artur Frenszek-Iwicki, see RH BZ #2173236
- Note that the Source0 file actually has a v instead of slim in the address at the very end. However, the file that is downloaded is slim-version.tar.gz.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 1.3.6-19
- Fix check of return value from XCreateGC

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com>
- Force C++14 as this code is not C++17 ready

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 BjÃ¶rn Esser <besser82@fedoraproject.org> - 1.3.6-13
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 BjÃ¶rn Esser <besser82@fedoraproject.org> - 1.3.6-10
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 16 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.6-1
- Update to 1.3.6 (bz#1030423)
- Add libslim.so.%%{version}
- Add BR libXrandr-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.3.5-4
- Perl 5.18 rebuild

* Fri Apr 26 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.5-3
- Harden build - bz#954324

* Thu Feb 7 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.5-2
- Update to 1.3.5.
- Fix typo in changelog
- Replace $RPM_BUILD_ROOT by %%{buildroot}
- rm garbage from installer /usr/usr/lib/systemd/system/slim.service
- Remove libpng patch.

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.3.4-2
- rebuild due to "jpeg8-ABI" feature drop

* Fri Nov 9 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.4-1
- Update to 1.3.4 version by Globe Trotter request (bz#868594).
- Add Patch0 to fix libpng1.5 incompatability..

* Sun Aug 12 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.3-5
- Display Manager Rework - https://fedoraproject.org/wiki/Features/DisplayManagerRework (bz#846152).
    Thanks to Lennart Poettering <lpoetter@redhat.com>

* Sun Aug 12 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.3-4
- Add BR freeglut-devel to fix FBFS on Fedora 18.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 6 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.3-2
- Update to 1.3.3 version by request bz#800254
- Step to cmake build system.
- Drop libpng and make patches.
- Rebase to new version Fedora patch.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-11
- Rebuilt for c++ ABI breakage

* Thu Jan 26 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.3.2-10
- Add Patch slim-1.3.2-libpng-version.patch to fix FBFS in rawhide.
- Fix bz#717774

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.2-8
- Rebuild for new libpng

* Sun Jul 24 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 1.3.2-7
- Rebuild for Rawhide

* Wed Jun 01 2011 Jan Kaluza <jkaluza@redhat.com> - 1.3.2-6
- fix #708693 - added tmfiles.d config to create /var/run/slim directory

* Tue Mar 01 2011 Petr Sabata <psabata@redhat.com> - 1.3.2-5
- General spec cleanup
- Moved slim-dynwm to a separate source file
- Patches renamed
- Buildroot removed

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Petr Sabata <psabata@redhat.com> - 1.3.2-3
- /var/run/slim is now ghost'd, rhbz#656689

* Tue Aug 31 2010 Petr Sabata <psabata@redhat.com> - 1.3.2-2
- slim-update_wm_list script modification, rhbz#581518

* Sun Aug 22 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.2-1
- New upstream version 1.3.2
- Drop slim-1.3.1-usexwd.patch (folded into 02-slim-1.3.2-fedora.patch)
- Drop slim-1.3.1-curdir.patch (folded into 02-slim-1.3.2-fedora.patch)
- Drop slim-1.3.1-strtol.patch (merged upstream)
- Drop slim-1.3.1-remove.patch (merged upstream)
- Drop slim-1.3.1-gcc44.patch (merged upstream)
- Drop slim-1.3.1-CVE-2009-1756.patch (merged upstream)
- Drop slim-1.3.1-fix-insecure-mcookie-generation.patch (merged upstream)

* Tue Mar 30 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-13
- Missing /var/run/slim (Fix bz#573284)

* Mon Mar 29 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-12
- Add logrotate.d file to work-around bz#573743

* Fri Feb 19 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-11
- Refresh slim-1.3.1-selinux.patch to include fix for bz#561095

* Tue Dec 22 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-9
- Fix CVE-2009-1756 (bugzilla: 544024)
- Fix MIT insecure cookie generation (patch from Debian)
- Fix build with GCC 4.4

* Sat Oct 10 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-8
- Fix BZ #518068

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-6
- exclude current directory from default_path in slim.conf (#505359)

* Sat Feb 28 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-5
- provide service(graphical-login) for anaconda yuminstall (#485789)

* Sun Feb 22 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-4
- Add header for remove(3)

* Wed Feb 04 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-3
- use small "default_blue" background, instead of large compat "default"

* Wed Oct 15 2008 Marco Pesenti Gritti <mpg@redhat.com>  1.3.1-2
- Enable pam_selinux

* Thu Oct 09 2008 Marco Pesenti Gritti <mpg@redhat.com>  1.3.1-1
- Update to 1.3.1

* Sun Oct 05 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-7
- add compat req (#465631)

* Wed Sep 24 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-6
- fix patch fuzz

* Fri May 16 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-5
- all the images are now in desktop-backgrounds-basic

* Fri Feb 22 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-4
- add header for strtol(3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.0-3
- Autorebuild for GCC 4.3

* Sat Jan 19 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-2
- rebuild

* Mon Aug  6 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-1
- version upgrade

* Mon Aug  6 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-6
- require system-logos instead of fedora-logos (#250365)

* Tue May 22 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-5
- make sure to own datadir slim parent too

* Mon May 21 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-4
- use desktop background, instead of slim
- leave (unused) pam files in the package

* Mon May 14 2007 Anders F Bjorklund <afb@users.sourceforge.net>
- clean up spec file
- correct README user

* Sun May 13 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-3
- use slim background instead of default
- added more build dependencies / -devel
- add "README.Fedora"
- patch issue display

* Wed May 09 2007 Anders F Bjorklund <afb@users.sourceforge.net>
- clean up spec file
- noreplace slim.conf

* Tue May 08 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-2
- fixed source URL
- added libXft-devel
- removed xrdb dependency (left from wdm)
- added xwd dependency (for screenshots)

* Sun May 06 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-1
- initial package
- adopted wdm spec
