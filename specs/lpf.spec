%global commit f9032ddd26ffb33fd140e0b9d5ee72c445608077
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20210927
#%%global rel .%%{gitdate}.%%{shortcommit}

Name:           lpf
Version:        0.3
Release:        14%{?rel}%{?dist}
Summary:        Local package factory - build non-redistributable rpms

# Icon from iconarchive.com
License:        MIT
URL:            https://github.com/sergiomb2/lpf
#Source0:        %%{url}/archive/%%{commit}/lpf-%%{version}%%{?rel}.tar.gz
Source0:        %{url}/archive/v%{version}/lpf-%{version}%{?rel}.tar.gz
Patch1:         https://github.com/sergiomb2/lpf/commit/4f414697e6977da5fdeff7632ec3ea86ffdfbdfb.patch
Patch3:         0003-Remove-option-allowerasing-of-dnf-install.patch
Patch4:         0004-Use-relative-symbol-links.patch

BuildArch:      noarch

BuildRequires:  appdata-tools
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
Requires:       hicolor-icon-theme
Requires:       inotify-tools
Requires:       polkit
Requires:       procps-ng
Requires:       rpmdevtools
Requires:       rpm-build
Requires:       sudo
Requires:       dnf
Requires:       zenity
#for lpf-gui
Requires:      python3-gobject-base


%description
lpf (Local Package Factory) is designed to handle two separate
problems:
 - Packages built from sources which does not allow redistribution.
 - Packages requiring user to accept EULA-like terms.

It works by downloading sources, possibly requiring a user to accept
license terms and then building and installing rpm package(s) locally.
Besides being interactive the operation is similar to akmod and dkms.


%prep
%autosetup -p1
#-n lpf-%%{commit}

# Create a sysusers.d config file
cat >lpf.sysusers.conf <<EOF
u pkg-build - 'lpf local package build user' /var/lib/lpf -
EOF


%build


%install
make DESTDIR=%{buildroot} install
desktop-file-validate %{buildroot}%{_datadir}/applications/lpf.desktop

install -m0644 -D lpf.sysusers.conf %{buildroot}%{_sysusersdir}/lpf.conf

%check
appstream-util validate-relax --nonet appdata/lpf-gui.appdata.xml




%files
%doc README.md LICENSE
%{_bindir}/lpf
%{_bindir}/lpf-gui
%{_rpmconfigdir}/macros.d/macros.lpf
%{_datadir}/lpf
%{_datadir}/applications/lpf.desktop
%{_datadir}/applications/lpf-gui.desktop
%{_datadir}/applications/lpf-notify.desktop
%{_datadir}/icons/hicolor/*/apps/lpf*.png
%{_datadir}/appdata/lpf-gui.appdata.xml
%{_datadir}/man/man1/lpf*
%{_libexecdir}/lpf-kill-pgroup
%attr(440, root, root) %config(noreplace) %{_sysconfdir}/sudoers.d/pkg-build
%attr(2775, pkg-build, pkg-build)/var/lib/lpf
%{_sysusersdir}/lpf.conf


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-13
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 03 2024 Sérgio Basto <sergio@serjux.com> - 0.3-11
- Only requires dnf to work with dnf5 Resolves: rhbz#2209396

* Thu Oct 24 2024 Sérgio Basto <sergio@serjux.com> - 0.3-10
- (#2319776) fixes dnf install for dnf5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Sérgio Basto <sergio@serjux.com> - 0.3-2
- Fix never end loop on lpf update (#2020711)

* Sat Oct 09 2021 Sérgio Basto <sergio@serjux.com> - 0.3-1
- Update to 0.3

* Fri Sep 03 2021 Sérgio Basto <sergio@serjux.com> - 0.2-18.20210903.414f14e
- Update to lpf-0.2.20210903.414f14e with more bug fixing

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-17.20210530.d1cb09f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Sérgio Basto <sergio@serjux.com> - 0.2-16.20210530.d1cb09f
- Update to lpf-0.2.20210530.d1cb09f

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Petr Viktorin <pviktori@redhat.com> - 0.2-14.f1f5dd9
- Switch BuildRequires to python3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Sérgio Basto <sergio@serjux.com> - 0.2-9.f1f5dd9
- Bux fix

* Tue Jul 24 2018 Sérgio Basto <sergio@serjux.com> - 0.2-8.f1f5dd9
- Remove dependency of yum-utils and add dependency of dnf-plugins-core
- Some cleanups
- Add patch 0001-add-gi.require_version-Gtk-3.0-before-import-Gtk.patch
- Add patch 0002-Fix-lpf-gui-behavior-and-a-strange-message.patch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2.f1f5dd9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Alec Leamas <leamas.alec@gmail.com> - 0.2-1.f1f5dd9
- Update to latest version, including yum -> dnf updates.
- Remove upstreamed patches.

* Sat Aug 30 2014 Alec Leamas <leamas.alec@gmail.com> - 0.1-8.36e5aa0
- Fix for umask problem (bz #1080149).
- Fix for missing -y tobuilddep (upstream #24).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7.36e5aa0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Alec Leamas <leamas.alec@gmail.com> - 0.1-6.36e5aa0
- Patch for bz #1057878 added.

* Thu Jan 23 2014 Alec Leamas <leamas.alec@gmail.com> - 0.1-5.36e5aa0
- Adding two patches, doc update + bugfix in lpf script.

* Fri Jan 17 2014 Alec Leamas <leamas.alec@gmail.com> - 0.1-4.36e5aa0
- rebuilt

* Wed Jan 08 2014 Alec Leamas <leamas.alec@gmail.com> - 0.1-3.36e5aa0
- Remove bad requirement, reinstall %%check, confirm fedkpg bug fixed.

* Wed Jan 08 2014 Alec Leamas <leamas.alec@gmail.com> - 0.1-2.36e5aa0
- Rebuilt, checking fo fedpkg bug.

* Wed Jan 08 2014 Alec Leamas <leamas.alec@gmail.com> - 0.1-1.36e5aa0
- First upstream release 0.1.

* Thu Dec 12 2013 Alec Leamas <leamas.alec@gmail.com> - 0-14.fc43f57
- upstream bugfix: Don't terminate running process in scripts.

* Wed Dec 04 2013 Alec Leamas <leamas.alec@gmail.com> - 0-13.ff55de0
- Fix for upstream bug #13: ignore errors in lpf-kill-pgroup

* Wed Nov 27 2013 Alec Leamas <leamas.alec@gmail.com> - 0-12.1478565
- Upstream bugfixes.

* Fri Nov 22 2013 Alec Leamas <leamas@nowhere.net> - 0-11.c885df3
- Upstream: Automate adding of pkg-build group to user.
- Upstream: Handle packages built only on i386.
- Fix left behind cruft after uninstalling lpf-* packages.

* Sat Nov 16 2013 Alec Leamas <leamas@nowhere.net> - 0-10.d18db6d
- Upstream bugfixes.
- Fix bug when installing pkg with eula.
- Fix bug in lpf install scriptlets.

* Sun Nov 10 2013 Alec Leamas <leamas@nowhere.net> - 0-9.b40e846
- Upstream bugfixes.

* Sun Nov 10 2013 Alec Leamas <leamas.alec@gmail.com> - 0-8.ff50a5b
- Adding missing Requires:

* Sat Oct 26 2013 Alec Leamas <leamas.alec@gmail.com> - 0-6.ff50a5b
- Yet another bugfix.

* Sat Oct 26 2013 Alec Leamas <leamas.alec@gmail.com> - 0-6.354c031
- Fixing silly version error.

* Sat Oct 26 2013 Alec Leamas <leamas.alec@gmail.com> - 0-5.6d285c5
- Allow spec file to be named .spec.in

* Fri Oct 25 2013 Alec Leamas <leamas.alec@gmail.com> - 0-4.3051236
- Updating examples

* Sun Jun 23 2013 Alec Leamas <leamas@nowhere.net> - 0-3.fe3defcf9
- Removed examples, added lpf spec tamplate.
- Add manpage

* Thu Jun 13 2013 Alec Leamas <leamas@nowhere.net> - 0-3.fe3defcf9
- Added BR: python2-devel
- Simplified Source0 (https://fedorahosted.org/fpc/ticket/284)
- Using 2775 instead of 775 perms (https://fedorahosted.org/fpc/ticket/286)

* Tue Jun 11 2013 Alec Leamas <leamas@nowhere.net> - 0-1.c4bc5a2
- Upstream Makefile added, clean up installation

* Mon Jun 10 2013 Alec Leamas <leamas@nowhere.net> - 0-1.d961366
- Initial release
