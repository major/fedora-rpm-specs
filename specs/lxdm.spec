# Review at https://bugzilla.redhat.com/show_bug.cgi?id=540034

%{!?_unitdir: %global _unitdir %{_prefix}/lib/systemd/system/}

%global git_snapshot 1

%if 0%{?git_snapshot}
%global git_rev  2d4ba970e9bf97ec7d9c2730c940cabc58c54d27
%global git_date 20220831
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version %{git_date}git%{git_short}
%endif

%global main_version 0.5.3

Name:           lxdm
Version:        %{main_version}%{?git_version:^%{?git_version}}
Release:        8%{?dist}
Summary:        Lightweight X11 Display Manager

# src/*.c	GPL-3.0-or-later
# src/gdm/		GPL-2.0-or-later AND LGPL-2.1-or-later
# src/greeter.c	GPL-2.0-or-later
# SPDX confirmed
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://lxde.org

%if 0%{?git_snapshot}
Source0:        %{name}-%{main_version}-D%{?git_version}.tar.bz2
%else
Source0:        http://downloads.sourceforge.net/sourceforge/lxdm/%{name}-%{version}.tar.xz
%endif

# systemd service file and preset
Source1:        lxdm.service
Source2:        lxdm.preset

# The default contents of /var/lib/lxdm/lxdm.conf (c.f. lxdm.c:lxdm_save_login)
Source5:        lxdm_conf_login

# Fedora pam setting
# F-39: remove pam_console.so (bug 1822227, bug 2166692)
Source10:		pam.lxdm
Source11:		pam.lxdm.f38

# Shell script to create tarball from git scm
Source100:      create-tarball-from-git.sh

## Patches needing discussion with the upstream

## Distro specific patches ##

# Distro artwork, start on vt1
Patch50:        lxdm-0.4.1-config.patch
Patch60:        lxdm-0.5.1-ssh-agent-on-start.patch
# Remove /bin, /sbin from PATH with usrmove
Patch61:        lxdm-0.5.3-path-usrmove.patch


BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pam-devel
BuildRequires:  intltool >= 0.40.0
%if 0%{?git_snapshot}
BuildRequires:  automake
BuildRequires:  libtool
%endif
Requires:       pam
Requires:       /sbin/shutdown
Requires:       desktop-backgrounds-compat
Requires:		%{_bindir}/ssh-agent
# Loading jpegxl format img requires the below
%if 0%{?fedora} >= 42
Requires:       jxl-pixbuf-loader%{?_isa}
%endif
# needed for anaconda to boot into runlevel 5 after install
Provides:       service(graphical-login) = lxdm

BuildRequires:  systemd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd


%description
LXDM is the future display manager of LXDE, the Lightweight X11 Desktop 
environment. It is designed as a lightweight alternative to replace GDM or 
KDM in LXDE distros. It's still in very early stage of development.


%prep
%setup -q %{?git_version:-n %{name}-%{main_version}-D%{?git_version}}

%patch -P50 -p1 -b .config
%patch -P60 -p1 -b .ssh_agent
%patch -P61 -p1 -b .usemove

# Reset X after logout (bug 1269917)
sed -i.reset data/lxdm.conf.in \
	-e '\@reset@s|^.*$|reset=1|' 
# Fedora 42 changed default background file format
%if 0%{?fedora} >= 42
sed -i.f42 data/lxdm.conf.in \
	-e '\@bg=@s|default.png|default.jxl|'
%endif

install -cpm 644 \
%if 0%{?fedora} >= 39
	%{SOURCE10} \
%else
	%{SOURCE11} \
%endif
	pam/lxdm

cat << EOF > tempfiles.lxdm.conf
d /run/%{name} 0755 root root
EOF

%build
%{?git_version:sh autogen.sh}
%configure \
	--enable-gtk3 \
	--disable-silent-rules \
	--disable-consolekit \
	%{nil}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
%find_lang %{name}

# these files are not in the package, but should be owned by lxdm 
touch %{buildroot}%{_sysconfdir}/%{name}/xinitrc
mkdir -p %{buildroot}/run/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
install -m644 -p %{SOURCE5} %{buildroot}%{_localstatedir}/lib/%{name}/%{name}.conf

install -Dpm 644 tempfiles.lxdm.conf %{buildroot}%{_prefix}/lib/tmpfiles.d/lxdm.conf

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -m644 -p -D %{SOURCE2} %{buildroot}%{_unitdir}-preset/83-fedora-lxdm.preset


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service


%files -f %{name}.lang
# FIXME add ChangeLog and NEWS if not empty
%doc AUTHORS
%license COPYING
%doc README TODO
%license gpl-2.0.txt
%license lgpl-2.1.txt

%dir %{_sysconfdir}/%{name}
%ghost %config(noreplace,missingok) %{_sysconfdir}/%{name}/xinitrc
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/Xsession
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/LoginReady
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PostLogin
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PostLogout
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PreLogin
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PreReboot
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PreShutdown
%config %attr(640,root,root) %{_sysconfdir}/%{name}/lxdm.conf
%config(noreplace) %{_sysconfdir}/pam.d/%{name}

%{_bindir}/%{name}-config
%{_sbindir}/%{name}
%{_sbindir}/lxdm-binary
%{_libexecdir}/lxdm-greeter-gtk
%{_libexecdir}/lxdm-greeter-gdk
%{_libexecdir}/lxdm-numlock
%{_libexecdir}/lxdm-session

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/config.ui
%{_datadir}/%{name}/lxdm.glade
%{_datadir}/%{name}/themes/

%{_tmpfilesdir}/lxdm.conf
%dir /run/%{name}

%{_unitdir}/lxdm.service
%{_unitdir}-preset/83-fedora-lxdm.preset

%dir %{_localstatedir}/lib/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_localstatedir}/lib/%{name}/%{name}.conf


%changelog
* Fri Feb 14 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3^20220831git2d4ba970-8
- F42 switches default background from png to jxl
- Require jpegxl gdk-pixbuf loader

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3^20220831git2d4ba970-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3^20220831git2d4ba970-5
- Remove deprecated PATH with usrmove (bug 2276996)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3^20220831git2d4ba970-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3^20220831git2d4ba970-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3^20220831git2d4ba970-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3^20220831git2d4ba970-1
- LXDM migration
- Change EVR scheme to use hat

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-27.D20220831git2d4ba970
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar  2 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-26.D20220831git2d4ba970
- F-39 (and above): remove pam_console.so (bug 1822227, bug 2166692)

* Wed Feb 15 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-25.D20220831git2d4ba970
- F-38 is using default.png, not .webp, reflect this

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-24.D20220831git2d4ba970
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 29 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-23.D20220831git2d4ba970
- Update for tmpfiles.d guideline - config file is not %%config
- Fix up %%{_localstatedir}/lib/%%{name}/%%{name}.conf entry
  and mark as %%config, not %%ghost, install default file
- More verbose entry under %%{_datadir}/%%{name}/
- F-37: update default background image
- F-37: loading webp img requires webp-pixbuf-loader

* Sun Sep 11 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-22.D20220831git2d4ba970
- Update to the latest git (20220831)
- Switch to GTK3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-21.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-20.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-17.D20161111gita548c73e
- Use /run instead of %%_localstatedir/run (bug 1775734)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-14.D20161111gita548c73e
- Fix systemd scriptlet error on F-31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-13.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.5.3-9.D20161111gita548c73e
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6.D20161111gita548c73e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-5.D20161111gita548c73e
- Update to the latest git

* Fri May 20 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-4.D20160321git72812894
- Update to the latest git

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3.D20160103gitc6836939
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan  3 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-2.D20160103gitc6836939
- Make xauthority fallback file being created under user
  specific directory (sfbug #789) (patch accepted by
  the upstream)

* Tue Nov 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-1
- 0.5.3

* Tue Nov 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-0.1.D20151123gitc731487c
- Update to the latest git
- Login issue with system with "lxdm" user
- Respawn X when relogin (bug 1269917)

* Sat Nov 21 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-2.D20151121gitd5b7ae6b
- Update to the latest git
- Login issue with user with NFS mounted home directory (bug 1283581)

* Wed Oct 14 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-1
- 0.5.2

* Thu Oct  8 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-7.D20151007gite8f38708
- Update to the latest git (X server auth issue: bug 1268900)

* Sat Aug 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-6.D20150806git17ac3772
- More fix wrt relogin from the upstream

* Sun Aug  2 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-5.D20150802git50b704be.
- Update to the lates git (for some more issue with login)

* Wed Jul 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-3.D20150726git4dfe7924
- Update to the latest git (fix logout issue with recent systemd)

* Fri Jun 26 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-2
- ssh-agent patch

* Mon Jun 22 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.5.1-1
- Update to 0.5.1
- drop all upstream patches

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.4.1-8
- Fix FTBFS with -Werror=format-security (#1037184, #1106142)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 07 2012 Adam Williamson <awilliam@redhat.com> - 0.4.1-4
- ship a systemd preset for lxdm (#855470)
- add After: livesys-late.service to the service file, testing of other
  DMs indicated this is needed for lives

* Tue Aug 07 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-3
- Move tmpfiles configuration to new location (#840186)
- Ship systemd service file for Fedora >= 18 (#846148)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1 (#758480), fixes #596360, #635897, #652697, #683728, #758480
  and #758484
- Fix softlock bug causing 100% CPU (#767861, #794478)
- Fix SELinux problem with xauth (#635897)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.0-5
- Rebuild for new libpng

* Wed Feb 16 2011 Adam Williamson <awilliam@redhat.com> - 0.3.0-4
- add background.patch from upstream: change X parameter -nr to
  -background (fixes #661600)
- rediff config.patch to account for background.patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-2
- Mark files in /var/run as %%ghost (#656618)

* Thu Sep 30 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Wed Sep 29 2010 jkeating - 0.3.0-0.2.20100921gitcf9b2cbb
- Rebuilt for gcc bug 634757

* Mon Sep 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-0.1.20100921gitcf9b2cbb
- Update to GIT snapshot of 20100921 (fixes #635396)

* Tue May 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-4
- Fix env XAUTHORITY bug

* Sun May 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-3
- Fix permissions of /var/run/lxdm
- Add patches to fix some env settings
- Add --debug option

* Sun May 09 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-2
- Patch for SELinux problems (#564320)

* Wed May 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sat Apr 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-0.3.20100405gitd65ce94
- Adjustments for recent Goddard artwork changes

* Tue Apr 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-0.2.20100405gitd65ce94
- Fix ownership of scripts in /etc/lxdm

* Mon Apr 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-0.1.20100405gitd65ce94
- Update to git release cb858f7
- New BuildRequires pam-devel
- Bump version to 0.2.0

* Wed Mar 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-0.2.20100303gite4f7b39
- Make sure lxdm.conf gets updated to avoid login problems

* Wed Mar 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-0.1.20100303gite4f7b39
- Update to git release e4f7b39 (fixes #564995)
- Fix SELinux problems (#564320)

* Wed Feb 24 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-0.1.20100223gitdf819fd
- Update to latest git
- BR iso-codes-devel
- Don't hardcode tty1 in the source, use lxdm.conf instead

* Fri Jan 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Update to 0.1.0
- Change license to GPLv2+ and LGPLv2+
- Use tty1 by default
- PAM fixes for SELinux (#552885)

* Mon Nov 16 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.3-0.2.20091116svn2145
- Review fixes

* Mon Nov 16 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.3-0.1.20091116svn2145
- Update to SVN release 2145

* Thu Nov 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.3-0.1.20091105svn2132
- Update to SVN release 2132

* Sat Oct 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.3-0.1.20091031svn2100
- Update to SVN release 2100

* Tue Oct 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.3-0.1.20091020svn2082
- Update to SVN release 2082

* Fri Sep 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.2-1
- Initial Fedora package
