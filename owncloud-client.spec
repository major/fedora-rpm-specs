Name:           owncloud-client
Version:        2.10.1
%global vertag  7389
Release:        1%{?dist}
Summary:        The ownCloud Client

# -libs are LGPLv2+, rest GPLv2
License:        LGPLv2+ and GPLv2
Url:            http://owncloud.org/sync-clients/
Source0:        https://download.owncloud.com/desktop/ownCloud/stable/%{version}.%{vertag}/source/ownCloud-%{version}.%{vertag}.tar.xz
Source1:        owncloud.appdata.xml
# https://github.com/owncloud/client/issues/410
Source2:	69-sync-inotify.conf
Source3:	ownCloud.conf

# The patch does 3 things:
#  - Depends on system lib for QtSingleApplication and QtLockedFile
#  - Remove the extraneous namespace when calling QtSingleApplication
#  - Fix a mismatch in the QtSingleApplication::messageReceived signal and the 
# Application::slotParseMessage slot
# These fix are needed because the system wide QtSingleApplication is slightly 
# different from the bundled one.
Patch0:         owncloud-client-2.9.0-syslibs.patch
# https://github.com/owncloud/client/commit/c1e3bb8457d77619a1c31217716789e76fd06500
Patch1:		owncloud-client-2.10.1.7389-gcc12.patch

BuildRequires:  check
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  libappstream-glib
BuildRequires:  neon-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-sphinx
BuildRequires:  qtlockedfile-qt5-devel
BuildRequires:  qtkeychain-qt5-devel >= 0.7.0
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-gui
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qttools qt5-qttools-devel
BuildRequires:  extra-cmake-modules

# Plasma 5 Dolphin integration
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-rpm-macros

BuildRequires:  sqlite-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Provides: mirall = %{version}-%{release}
Obsoletes: mirall < 1.8.0

%description
Owncloud-client enables you to connect to your private ownCloud Server.
With it you can create folders in your home directory, and keep the contents
of those folders synced with your ownCloud server. Simply copy a file into
the directory and the ownCloud Client does the rest.

%package libs
Summary: Common files for owncloud-client and owncloud-client
License: LGPLv2+
Provides: mirall-common = %{version}-%{release}
Obsoletes: mirall-common < 1.8.0

%description libs
Provides common files for owncloud-client and owncloud-client such as the
configuration file that determines the excluded files in a sync.

%package devel
Summary: Development files for owncloud-client
License: LGPLv2+
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
Provides: mirall-devel = %{version}-%{release}
Obsoletes: mirall-devel < 1.8.0

%description devel
Development headers for use of the owncloud-client library

%package nautilus
Summary: owncloud client nautilus extension
Requires: nautilus
Requires: python3-nautilus
Provides: mirall-nautilus = %{version}-%{release}
Obsoletes: mirall-nautilus < 1.8.0

%description nautilus
The owncloud desktop client nautilus extension.

%package nemo
Summary:        Nemo overlay icons
Requires:       nemo
Requires:       python3-nemo

%description nemo
This package provides overlay icons to visualize the sync state
in the nemo file manager.

%package caja
Summary:        Caja overlay icons
Requires:       caja
Requires:       python3-caja
Requires: %{name}%{?_isa} = %{version}-%{release}

%description caja
This package provides overlay icons to visualize the sync state
in the caja file manager.

%package dolphin
Summary:        Dolphin overlay icons
Requires:       dolphin

%description dolphin
The owncloud desktop client dolphin extension.

%prep
%autosetup -p1 -n ownCloud-%{version}.%{vertag}

rm -rf src/3rdparty/qtlockedfile src/3rdparty/qtsingleapplication


%build
%cmake_kf5 -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
%cmake_build


%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/appdata/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/owncloud.appdata.xml
install -m 644 -D %{SOURCE2} %{buildroot}/etc/sysctl.d/69-sync-inotify.conf
install -m 644 -D %{SOURCE3} %{buildroot}/etc/ownCloud/

# for distros that do not have KDE Plasma 5
rm -f %{buildroot}%{_libdir}/libnextclouddolphinpluginhelper.so
rm -f %{buildroot}%{_kf5_plugindir}/overlayicon/nextclouddolphinoverlayplugin.so
rm -f %{buildroot}%{_qt5_plugindir}/nextclouddolphinactionplugin.so
rm -f %{buildroot}%{_kf5_datadir}/kservices5/nextclouddolphinactionplugin.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/owncloud.appdata.xml


%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/ownCloud
%config(noreplace) %{_sysconfdir}/ownCloud/ownCloud.conf
%config(noreplace) %{_sysconfdir}/sysctl.d/69-sync-inotify.conf
%{_bindir}/owncloud
%{_bindir}/owncloudcmd
%{_datadir}/applications/owncloud.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/appdata/owncloud.appdata.xml
%{_datadir}/mime/packages/owncloud.xml

%files libs
%license COPYING
%{_libdir}/libowncloudsync.so.0
%{_libdir}/libowncloudsync.so.%{version}
%{_libdir}/libowncloud_csync.so.*
%config(noreplace) %{_sysconfdir}/ownCloud/sync-exclude.lst
%{_libdir}/qt5/plugins/owncloudsync_vfs_suffix.so

%files devel
%{_includedir}/owncloudsync/
%{_libdir}/libowncloudsync.so
%{_libdir}/libowncloud_csync.so

%files nautilus
%{_datadir}/nautilus-python/extensions/*

%files nemo
%{_datadir}/nemo-python/extensions/*

%files caja
%{_datadir}/caja-python/extensions/*

%files dolphin
%{_libdir}/libownclouddolphinpluginhelper.so
%{_kf5_plugindir}/overlayicon/ownclouddolphinoverlayplugin.so
%{_kf5_datadir}/kservices5/ownclouddolphinactionplugin.desktop
%{_qt5_plugindir}/ownclouddolphinactionplugin.so


%changelog
* Thu Aug 04 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1 (RHBZ #2106447)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 25 2021 Jos de Kloe <josdekloe@gmail.com> - 2.9.0-1
- Update to 2.9.0
- Fixes: rhbz#1913741

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.4-1
- Update to 2.7.4
- Fixes: rhbz#1792390

* Mon Dec 28 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.3-1
- Update to 2.6.3
- https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds
- Fixes: rhbz#1865188

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-1
- 2.6.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.5.4-1
- 2.5.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.4.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 14 2018 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.4.0-2
- Fix requires python2-nemo instead nemo-python

* Tue Feb 13 2018 Germano Massullo <germano.massullo@gmail.com> - 2.4.0-1
- 2.4.0 release
- Updated syslibs patch, thanks to Robert-André Mauchin
- added comment to syslibs patch, thanks to Robert-André Mauchin

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Nick Bebout <nb@fedoraproject.org> - 2.3.3-2
- Change to python2-sphinx instead of python-sphinx BR

* Mon Sep 11 2017 Nick Bebout <nb@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Germano Massullo <germano.massullo@gmail.com> - 2.3.2-3
- added macros to build Caja subpackage only in Fedora, not EPEL (Mate is Fedora only)
- added macro to build Dolphin (Plasma 5) subpackage only in Fedora >= 24 && EPEL > 7 (EPEL7 ships KDE 4)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed May 10 2017 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2
- Remove caja extension hack. Included in upstream
- Remove openssl patch. Included in upstream

* Wed Mar 08 2017 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.2.4-5
- Add caja extension

* Wed Jan 11 2017 Kalev Lember <klember@redhat.com> - 2.2.4-4
- Fix appdata file name to match with desktop file name

* Tue Nov 08 2016 Germano Massullo <germano.massullo@gmail.com> 2.2.4-4
- Added BuildRequires: python2-devel, python3-devel

* Wed Nov 02 2016 Germano Massullo <germano.massullo@gmail.com> 2.2.4-3
- Backport of https://github.com/owncloud/client/pull/5294

* Mon Oct 24 2016 Germano Massullo <germano.massullo@gmail.com> 2.2.4-2
- Disabled Dolphin integration for Enterprise Linux 7, because it works on Plasma 5 only

* Tue Oct 11 2016 Germano Massullo <germano.massullo@gmail.com> 2.2.4-1
- Update to 2.2.4

* Wed Jun 29 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Tue May 24 2016 Nikos Roussos <comzeradd@fedoraproject.org> 2.2.0-9
- Reapply dolphin changes

* Tue May 24 2016 Nikos Roussos <comzeradd@fedoraproject.org> 2.2.0-8
- Bump release

* Mon May 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-7
- Fix -dolphin subpkg

* Mon May 23 2016 Nikos Roussos <comzeradd@fedoraproject.org> 2.2.0-6
- Rebuild for qtkeychain new release

* Mon May 23 2016 Germano Massullo <germano.massullo@gmail.com> 2.2.0-5
- Added Dolphin integration subpackage

* Mon May 23 2016 Nikos Roussos <comzeradd@fedoraproject.org> 2.2.0-4
- Bump release

* Sun May 22 2016 Nikos Roussos <comzeradd@fedoraproject.org> 2.2.0-3
- Bump release

* Wed May 18 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 2.2.0-2
- Fix qtkeychain requirement

* Mon May 16 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 2.2.0-1
- Updated to 2.2.0
- Add hardened flag
- Update patches
- Remove merged patch

* Mon May 16 2016 Germano Massullo <germano.massullo@gmail.com> - 2.1.1-3
- Added BuildRequires:  openssl-devel to fix epel7 build problems. This buildrequires seems to be fine for other branches too.

* Thu Feb 11 2016 Germano Massullo <germano.massullo@gmail.com> - 2.1.1-2
- Added owncloud-client-nemo subpackage

* Wed Feb 10 2016 Germano Massullo <germano.massullo@gmail.com> - 2.1.1-1
- Minor update
- Added shebang patch (https://github.com/owncloud/client/issues/4436)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Germano Massullo <germano.massullo@gmail.com> - 2.1.0-1
- Updated to 2.1.0
- Removed httpbf stuff because no longer used in 2.1.0

* Wed Dec 02 2015 Germano Massullo <germano.massullo@gmail.com> - 2.0.2-2
- Enabled Qt5 support

* Wed Dec 02 2015  Nikos Roussos <comzeradd@fedoraproject.org> - 2.0.2-1
- Update patches

* Wed Nov 18 2015 Germano Massullo <germano.massullo@gmail.com> - 2.0.2-1
- Updated to 2.0.2
- Sorted BuildRequires entries
- Updated source URL

* Tue Sep 08 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 2.0.1-1
- Updated to 2.0.1

* Thu Sep 03 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.8.5-2
- remove extraneous client subpackage
- use macros for versions

* Mon Aug 31 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.8.4-2
- Rename -common to -libs
- Add Provides to all subpackages
- Validate appdata
- Fix multiple license issue

* Wed Jul 15 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.8.4-1
- Updated to 1.8.4
- Add appdata

* Wed Apr 22 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.8.0-5
- Remove 3rdparties dirs

* Mon Apr 20 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.8.0-4
- Fix provides statement
- All descriptions and summaries now start with capital letters
- Use %%license where appropriate instead of %%doc

* Wed Mar 18 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.8.0-3
- Obsolete all mirall subpackages

* Tue Mar 17 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.8.0-2
- Rename mirall to owncloud-client

* Mon Mar 16 2015 Dams <anvil[AT]livna.org> - 1.8.0-1
- Updated to 1.8.0
- Updated all patches

* Fri Mar  6 2015 Dams <anvil[AT]livna.org> - 1.7.1-2
- Added gcc5 compliance patch

* Fri Mar  6 2015 Dams <anvil[AT]livna.org> - 1.7.1-1
- Updated to 1.7.1

* Mon Nov 10 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 1.7.0-2
- Add missing dependency

* Mon Nov 10 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 1.7.0-1
- Updated to 1.7.0

* Sun Sep 14 2014 Dams <anvil[AT]livna.org> - 1.7.0-0.2.beta1
- Updated tarball URL

* Sun Sep 14 2014 Dams <anvil@livna.org> - 1.7.0-0.1.beta1
- Updated to 1.7.0-beta1
- Updated Patch0
- Added Patch1 to fix rpath in binaries
- Added nautilus subpackage

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5.4-2
- drop hard-coded Requires: neon, qtkeychain, let rpm autodeps handle it
- drop BR: gcc-c++
- -devel: tighten subpkg dep

* Mon May 05 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4
* Thu Mar 20 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.5.3-3
- Use system qtlockedfile and qtsingleapplication instead of bundled ones
* Wed Mar 19 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.3-2
- Updated Obsoletes for each subpackage
* Sun Mar 16 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.3-1
- Update to latest Upstream version
- Merge owncloud-csync and mirall as upstream has done

* Thu Jan 09 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.0-2
- Add requires owncloud-csync-libs
* Tue Jan 07 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.0-1
- Update to latest upstream release
* Sun Dec 29 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.4.2-4
- Build with $RPM_OPT_FLAGS.
- Move ldconfig scriptlets to -common.
* Thu Nov 14 2013 <jmarrero@fedoraproject.org> 1.4.2-3
- Add Requires neon as noted by Manuel Faux
- Add backported patch created by Klass Freitag backported by Manuel Faux
* Tue Nov 12 2013 <jmarrero@fedoraproject.org> 1.4.2-2
- Add BuildRequires neon-devel
* Sat Oct 26 2013 <jmarrero@fedoraproject.org> 1.4.2-1
- Update to version 1.4.2
* Fri Oct 04 2013 <jmarrero@fedoraproject.org> 1.4.1-1
- Update to version 1.4.1
* Wed Sep 04 2013 <jmarrero@fedoraproject.org> 1.4.0-2
- Add qtwebkit-devel dependency
* Wed Sep 04 2013 <jmarrero@fedoraproject.org> 1.4.0-1
- Update to version 1.4.0
- Update URL
* Sun Aug 18 2013 <jmarrero@fedoraproject.org> 1.4.0beta2-1
- Update to testing version 1.4.0beta2
* Wed Jun 26 2013 <jmarrero@fedoraproject.org> 1.3.0-1
- Update to version 1.3.0
* Thu May 23 2013 <jmarrero@fedoraproject.org> 1.3.0beta1-1
- Update to testing version 1.3.0beta1
* Tue Apr 23 2013 <jmarrero@fedoraproject.org> 1.2.5-1
- Update to upstream version 1.2.5
* Thu Apr 11 2013 <jmarrero@fedoraproject.org> 1.2.4-1
- Update to uptream version 1.2.4
* Wed Apr 03 2013 <jmarrero@fedoraproject.org> 1.2.3-1
- remove plasma client files as is not officially merged uptream
- Update to 1.2.3 uptream version
* Tue Mar 05 2013 <jmarrero@fedoraproject.org> 1.2.2-2
- plasma client files fix
* Tue Mar 05 2013 <jmarrero@fedoraproject.org> 1.2.2-1
- add new Plasma client package
* Sat Mar 02 2013 <jmarrero@fedoraproject.org> 1.2.1-2
- moved libowncloudsync.so* to common as it is now used by mirall and owncloud-client
- re-added mirall .desktop launcher
* Sat Mar 02 2013 <jmarrero@fedoraproject.org> 1.2.1-1
- Update to 1.2.1
* Sat Jan 26 2013 <jmarrero@fedoraproject.org> 1.2.0-1
- Update to 1.2.0
* Sat Jan 19 2013 <jmarrero@fedoraproject.org> 1.2.0beta2-1
- update to 1.2.0beta2
* Fri Dec 21 2012 <jmarrero@fedoraproject.org> 1.2.0beta1-1
- Update to 1.2.0beta1
* Thu Dec 20 2012 <jmarrero@fedoraproject.org> 1.1.4-1
- Update to 1.1.4
* Tue Dec 04 2012 <jmarrero@fedoraproject.org> 1.1.3-1
- Update to 1.1.3
* Fri Oct 19 2012 <jmarrero@fedoraproject.org> 1.1.1-1
- Update to 1.1.1
* Mon Oct 15 2012 <jmarrero@fedoraproject.org> 1.1.0-2
- fix mirall-common dependency problem
* Sun Oct 14 2012 <jmarrero@fedoraproject.org> 1.1.0-1
- Version Upgrade to 1.1.0
- Removed the need to look for occsync now mirall looks for ocsync the new name of owncloud-csync
* Mon Aug 20 2012 <jmarrero@fedoraproject.org> 1.0.5-4
- removed unesesary cmake flags
* Fri Aug 17 2012 <jmarrero@fedoraproject.org> 1.0.5-3
- added icon scriplets for owncloud-client icons
- moved %%doc to mirall-common
- Added cmake  dcSYNC_INCLUDE_PATH:PATH=_includedir}/occsync and dc SYNC_LIBRARY:PATH=_libdir}/liboccsync.so to have mirall look for occsync instead of csync
- Removed uneeded dep
- Changelog corrections and clean up
* Thu Aug 16 2012 <jmarrero@fedoraproject.org> 1.0.5-2
- Divided mirall into mirall-common, mirall and owncloud-client
- Added dcMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed
- moved exclude.lst back to /etc/, the apps look for it there
- fixed icons descriptions
- added refresh icon cache
- updated csync dep to owncloud-csync
* Sat Aug 11 2012 <jmarrero@fedoraproject.org> 1.0.5-1
- Update to 1.0.5
- drop defattr
- remove not-needed dependencies
- changelog cleanup
- moved exclude.lst to /etc/mirall/
- fixed source01 and source 02 (icons)
* Sat Aug 11 2012 <jmarrero@fedoraproject.org> 1.0.4-2
- added mirall icon and smp flags plus code cleanup
* Sat Aug 11 2012 <jmarrero@fedoraproject.org> 1.0.4-1
- Initial try
