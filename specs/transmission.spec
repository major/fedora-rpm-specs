Name:           transmission
Version:        4.0.6
Release:        4%{?dist}
Summary:        A lightweight GTK+ BitTorrent client
# See COPYING. This licensing situation is... special.
License:        MIT and GPL-2.0-only
URL:            http://www.transmissionbt.com

Source0:        https://github.com/transmission/transmission/releases/download/%{version}/transmission-%{version}.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=1221292
Source1:        https://raw.githubusercontent.com/gnome-design-team/gnome-icons/master/apps-symbolic/Adwaita/scalable/apps/transmission-symbolic.svg
# Fix the DBus name to match the app name for flatpak builds
# https://github.com/transmission/transmission/pull/847
Patch0:         0001-gtk-use-com.transmissionbt.Transmission.-D-Bus-names.patch
Patch1:         %{name}-miniupnp228.patch


BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  gtk4-devel
BuildRequires:  gtkmm4.0-devel
BuildRequires:  libcurl-devel >= 7.16.3
BuildRequires:  libevent-devel >= 2.0.10
BuildRequires:  desktop-file-utils
BuildRequires:  gettext intltool
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  systemd-devel
BuildRequires:  libnatpmp-devel >= 20150609-1
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(libpsl)
# unbundled dependencies
BuildRequires:  fast_float-static
#BuildRequires:  fmt-static
BuildRequires:  libb64-static
BuildRequires:  utf8cpp-static
# Default
Requires: transmission-gtk%{?_isa}


%description
Transmission is a free, lightweight BitTorrent client. It features a
simple, intuitive interface on top on an efficient, cross-platform
back-end.

%package common
Summary:       Transmission common files
Provides:      bundled(dht) = 0.27
# remove, unbundle, and BR: fmt-static once ported to fmt-10
Provides:      bundled(fmt) = 9.0.0
Provides:      bundled(libutp) = 3.4
Provides:      bundled(wide-integer)
Provides:      bundled(wildmat)
%description common
Common files for Transmission BitTorrent client sub-packages. It includes
the web user interface, icons and transmission-remote, transmission-create,
transmission-edit, transmission-show utilities.

%package cli
Summary:       Transmission command line implementation
Requires:      transmission-common%{?_isa}
%description cli
Command line version of Transmission BitTorrent client.

%package daemon
Summary:       Transmission daemon
Requires:      transmission-common%{?_isa}
Requires(pre): shadow-utils
BuildRequires: systemd
%description daemon
Transmission BitTorrent client daemon.

%package gtk
Summary:       Transmission GTK interface
Requires:      transmission-common%{?_isa}
# for canberra-gtk-play
Recommends:    libcanberra-gtk3%{?_isa}

%description gtk
GTK graphical interface of Transmission BitTorrent client.

%package qt
Summary:       Transmission Qt interface
Requires:      transmission-common%{?_isa}
# for canberra-gtk-play
Recommends:    libcanberra-gtk3%{?_isa}

%description qt
Qt graphical interface of Transmission BitTorrent client.

%pre daemon
getent group transmission >/dev/null || groupadd -r transmission
getent passwd transmission >/dev/null || \
useradd -r -g transmission -d %{_sharedstatedir}/transmission -s /sbin/nologin \
        -c "transmission daemon account" transmission
exit 0

%prep
%autosetup -p1

# unbundle
pushd third-party
find fast_float/ libb64/ libdeflate/ libevent/ libnatpmp/ libpsl/ \
     miniupnpc/ utfcpp/ -type f -delete
popd

# fix icon location for Transmission Qt
sed -i 's|Icon=%{name}-qt|Icon=%{name}|g' qt/%{name}-qt.desktop

# convert to UTF encoding
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new
mv AUTHORS.new AUTHORS

%build

CXXFLAGS="%{optflags} -fPIC"
CFLAGS="%{optflags} -fPIC"

%cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_CLI=ON -DENABLE_QT=ON -DUSE_QT_VERSION=6 -DENABLE_GTK=ON -DUSE_GTK_VERSION=4
%cmake_build

# Re-enable if DhtTest.usesBootstrapFile passes
#%%check
#%%ctest

%install
mkdir -p %{buildroot}%{_unitdir}
install -m0644 daemon/transmission-daemon.service  %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sharedstatedir}/transmission
%cmake_install

mv -f %{buildroot}%{_docdir}/transmission %{buildroot}%{_docdir}/transmission-common

# Install the symbolic icon
mkdir -p  %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps
cp %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/transmission-symbolic.svg

%find_lang %{name} --with-qt
%find_lang %{name}-gtk

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop
desktop-file-install \
                --dir=%{buildroot}%{_datadir}/applications/  \
                  qt/%{name}-qt.desktop

%post daemon
%systemd_post transmission-daemon.service

%preun daemon
%systemd_preun transmission-daemon.service

%postun daemon
%systemd_postun_with_restart transmission-daemon.service

%files

%files common
%license COPYING
%doc COPYING AUTHORS README.md news/ rpc-spec.md send-email-when-torrent-done.sh
%{_bindir}/transmission-remote
%{_bindir}/transmission-create
%{_bindir}/transmission-edit
%{_bindir}/transmission-show
%{_datadir}/transmission/public_html/
%{_datadir}/icons/hicolor/*/apps/transmission.*
%{_datadir}/icons/hicolor/symbolic/apps/transmission-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/transmission-devel.svg
%doc %{_mandir}/man1/transmission-remote*
%doc %{_mandir}/man1/transmission-create*
%doc %{_mandir}/man1/transmission-edit*
%doc %{_mandir}/man1/transmission-show*

%files cli
%{_bindir}/transmission-cli
%doc %{_mandir}/man1/transmission-cli*

%files daemon
%{_bindir}/transmission-daemon
%{_unitdir}/transmission-daemon.service
%attr(-,transmission, transmission)%{_sharedstatedir}/transmission/
%doc %{_mandir}/man1/transmission-daemon*

%files gtk -f %{name}-gtk.lang
%{_bindir}/transmission-gtk
%{_datadir}/metainfo/transmission-gtk.metainfo.xml
%{_datadir}/applications/transmission-gtk.desktop
%doc %{_mandir}/man1/transmission-gtk.*

%files qt -f %{name}.lang
%{_bindir}/transmission-qt
%{_datadir}/applications/transmission-qt.desktop
%doc %{_mandir}/man1/transmission-qt.*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 4.0.6-3
- Rebuild for updated miniupnpc.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.0.6-1
- 4.0.6

* Tue Apr 02 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 4.0.5-4
- Update and unbundle dependencies

* Tue Mar 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.0.5-3
- Fix translation ownership.
- Move gtk client to gtk4, qt to qt6.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.5-1
- 4.0.5

* Mon Aug 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.4-1
- 4.0.4

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Kalev Lember <klember@redhat.com> - 4.0.3-3
- Remove unnecessary post/preun/postun requires on systemd

* Thu Jun 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.3-2
- Set build type

* Mon Apr 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.3-1
- 4.0.3

* Thu Mar 16 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.2-1
- 4.0.2

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.1-2
- migrated to SPDX license

* Thu Feb 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.1-1
- 4.0.1

* Wed Feb 15 2023 Kalev Lember <klember@redhat.com> - 4.0.0-3
- Avoid hardcoding /usr prefix
- Restore flatpak DBus name patch

* Tue Feb 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.0-2
- Patches for crash.

* Wed Feb 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.0.0-1
- 4.0.0, moved to qt6.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.00-14
- Patch from Debian to use OpenSSL 3.x

* Mon Aug 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.00-13
- Move to OpenSSL 1.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.00-10
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.00-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 Jeff Law <law@redhat.com> - 3.00-6
- Force -fPIC into CFLAGS for QT

* Tue Sep 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.00-5
- libevent re-rebuild

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.00-4
- libevent rebuild

* Sun Sep 13 2020 Kalev Lember <klember@redhat.com> - 3.00-3
- Use upstream appdata file

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.00-1
- 3.00

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.94-9
- Backported patch for CVE-2018-10756

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.94-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.94-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Kalev Lember <klember@redhat.com> - 2.94-6
- Add a patch to fix the DBus name to match the app name for flatpak builds

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.94-5
- Add appindicator support, BZ 1679345.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.94-1

* Thu Feb 15 2018 Björn Esser <besser82@fedoraproject.org> - 2.93-2
- Rebuilt for libevent-2.1.so.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.92-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.92-12
- Patch for openssl 1.1.x
- Corrected CVE-2018-5702 patch.

* Tue Jan 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.92-11
- Upstream fix for CVE-2018-5702 (Mitigate dns rebinding attacks against daemon)

* Wed Jan 10 2018 Heiko Reese <fedora@heiko-reese.de> - 2.92-10
- Removed hardcoded fdlimit of 1024

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.92-9
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.92-6
- Restore systemd usage.

* Thu Apr 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.92-5
- Correct unit file service type, BZ 1442085.

* Tue Apr 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.92-4
- Fix FTBFS.

* Mon Feb 13 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.92-3
- Make requires arch specific
- Make transmission require -gtk, which will be default

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 07 2016 Jon Ciesla <limburgher@gmail.com> - 2.92-1
- Latest upstream, dbus fix and OSX malware removal.

* Sun Feb 28 2016 Jon Ciesla <limburgher@gmail.com> - 2.90-1
- 2.90, BZ 1312701
- Overshoot patch upstreamed.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Jon Ciesla <limburgher@gmail.com> - 2.84-10
- Patch for gtk bug, BZ 1288861.

* Fri Sep 18 2015 Jon Ciesla <limburgher@gmail.com> - 2.84-9
- Use system libnatpmp, BZ 1264292.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.84-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Kalev Lember <kalevlember@gmail.com> - 2.84-7
- Try harder to install the correct symbolic icon

* Wed May 13 2015 Kalev Lember <kalevlember@gmail.com> - 2.84-6
- Install a symbolic app icon (#1221292)
- Use license macro for the COPYING file

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.84-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.84-4
- Add an AppData file for the software center

* Thu Mar 12 2015 Helio Chissini de Castro <helio@kde.org> - 2.83-3
- Compile with Qt5 now

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 2.84-1
- update to 2.84
- resolves rhbz#1118291 - peer communication vulnerability

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.83-1
- Updated to 2.83
- https://trac.transmissionbt.com/wiki/Changes
- Remove patch: https://trac.transmissionbt.com/ticket/5465

* Sat May 17 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 2.82-3
- fix Transmission Qt icon location (rhbz#1096423)

* Thu Aug 29 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.82-2
- Remove obseleted Obsoletes tag
- Forgot a spec bump

* Thu Aug 15 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.82-1
- Update to latest upstream release
- Changes listed at: https://trac.transmissionbt.com/wiki/Changes#version-2.82
- Add patch to revert qt5 changes since it doesn't build with it.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.81-2
- Typo: sharedstate not sharestate

* Mon Jul 22 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.81-1
- Update to new upstream release: 2.81
- https://trac.transmissionbt.com/wiki/Changes#version-2.81
- Replace /var/lib by sharestatedir macro
- Replace $RPM_OPT_FLAGS with optflags for consistency

* Sun Jul 14 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.80-2
- systemd-units -> systemd. rhbz:981647
- Add systemd-devel as BR. rhbz:984220

* Thu Jun 27 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.80-1
- upstream release 2.80
- use upstream systemd service file

* Fri May 10 2013 Adam Williamson <awilliam@redhat.com>
- update scriptlets to match current guidelines

* Mon Apr 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.77-3
- use hardened build macro and enable fPIC for Qt build. resolves rhbz#955268

* Tue Apr 02 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.77-2
- fix use of systemd macros to apply to daemon subpackage only

* Tue Feb 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.77-1
- upstream release 2.77
- https://trac.transmissionbt.com/wiki/Changes#version-2.77

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.76-1
- upstream release 2.76
- https://trac.transmissionbt.com/wiki/Changes#version-2.76
- use rpm ld_flags for qt build. resolves rhbz#868502
- use upstream transmission-qt.desktop file. resolves rhbz#799673
- remove -T parameter from the systemd file. resolves rhz#823220

* Sat Dec 15 2012 Rahul Sundaram <sundaram@fedoraproject.org> - 2.75-1
- upstream release 2.75
- https://trac.transmissionbt.com/wiki/Changes#version-2.75

* Sat Oct 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.72-1
- Update to 2.72

* Thu Sep 27 2012 Kalev Lember <kalevlember@gmail.com> - 2.71-1
- Update to 2.71
- Drop upstreamed desktop file patch

* Sat Jul 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.61-1
- Update to 2.61
- Build with gtk3
- Add a patch to make desktop-file-validate happy

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 02 2012 Rahul Sundaram <sundaram@fedoraproject.org> - 2.52-1
- upstream release 2.52
- https://trac.transmissionbt.com/wiki/Changes#version-2.52

* Sat Jun 02 2012 Rahul Sundaram <sundaram@fedoraproject.org> - 2.50-3
- apply upstream bug fix patch from https://trac.transmissionbt.com/changeset/13300?format=diff&new=13300
- fixes https://trac.transmissionbt.com/ticket/4894

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.50-2
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012 Rahul Sundaram <sundaram@fedoraproject.org> - 2.50-1
- upstream release 2.50
- https://trac.transmissionbt.com/wiki/Changes#version-2.50

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-2
- Rebuilt for glibc bug#747377

* Sun Oct 23 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 2.42-1
- upstream release 2.42
- https://trac.transmissionbt.com/wiki/Changes#version-2.42

* Sat Sep 10 2011 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.33-2
- add systemd unit (#659919)
- drop sysconfig file

* Sun Aug 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 2.33-1.1
- Rebuilt for rpm (#728707)

* Thu Jul 21 2011 Raghu Udiyar <raghusiddarth@gmail.com> - 2.33-1
- https://trac.transmissionbt.com/wiki/Changes#version-2.33
- Remove deprecated gconf2 dependency

* Tue Jul 05 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 2.32-1
- Upstream 2.32 release
- https://trac.transmissionbt.com/wiki/Changes#version-2.32
- Drop defattr throughout the spec since recent RPM makes it redundant

* Sun Apr 24 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 2.31-1
- Upstream 2.31 release
- https://trac.transmissionbt.com/wiki/Changes#version-2.31
- Fix source url

* Sun Apr 24 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 2.30-0.b3
- Upstream 2.30 Beta 3 release
- https://trac.transmissionbt.com/wiki/Changes#version-2.30b3

* Mon Apr 04 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 2.30-0.b1
- Upstream 2.30 Beta 1 release
- Enable configure options explicitly
- Drop source and patch for icons since it is now upstream
- https://trac.transmissionbt.com/wiki/Changes#version-2.30b1
  * Major changes include the following:
  * µTP, UDP tracker, Multiscrape support
  * Download scarcest pieces first 
  * The "lazy bitfield" feature has been superseded by the "Fast Extension" BEP6 
  * GTK: Register as a magnet link handler in the .desktop file 
  * Web: Peer and Network preferences 

* Thu Mar 10 2011 Bastien Nocera <bnocera@redhat.com> 2.22-2
- Add new icons

* Thu Mar 10 2011 Bastien Nocera <bnocera@redhat.com> 2.22-1
- Update to 2.22

* Wed Mar  2 2011 Ville Skyttä <ville.skytta@iki.fi> - 2.21-2
- Own %%{_datadir}/transmission dir.

* Wed Feb 09 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 2.21-1
- Update to latest upstream release
- Drop no longer needed libnotify patch
- https://trac.transmissionbt.com/wiki/Changes

* Tue Dec 28 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.13-1
- updated to latest upstream release: https://trac.transmissionbt.com/wiki/Changes
- fixes #654793
- update libnotify patch

* Sun Nov 07 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.11-3
- fix build errors
- update patch to fix another libnotify breakage

* Sun Nov 07 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.11-2
- added patch to fix breakage for libnotify API changes

* Thu Oct 21 2010 Pavol Šimo <palos AT fedoraproject DOT org> - 2.11-1
- updated to latest release version
- added new files, updated fix-optflag.patch

* Wed Sep 29 2010 jkeating - 2.04-3
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.04-2
- Added patch to fix https://trac.transmissionbt.com/ticket/3539

* Mon Aug 09 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.04-1
- Updated to latest release
- bug 622239

* Wed Jul 21 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.03-1
- updated to latest release version
- bug 616745

* Sun Jun 27 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.01-2
- corrected build failure

* Sun Jun 27 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.01-1
- https://trac.transmissionbt.com/wiki/Changes 

* Thu Jun 17 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 2.00-1
- https://trac.transmissionbt.com/wiki/Changes?version=57
- Drop the clean section as it is redundant now

* Fri Mar 12 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.92-1
- Some bug fixes
- http://trac.transmissionbt.com/query?groupdesc=1&group=component&milestone=1.92&order=severity

* Sun Mar 07 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.91-3
- Don't lose user configuration with updates 
- Fixes rhbz#571044

* Wed Feb 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.91-2
- -common: move icon scriptlets here (where the icons are), update/optimize 
- -qt : add mime scriptlet

* Mon Feb 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.91-1
- http://trac.transmissionbt.com/wiki/Changes#version-1.91

* Sun Feb 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.90-2
- BR: qt4-devel
- -qt: Requires: qt4 >= %%_qt4_version

* Wed Feb 17 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.90-1
- http://trac.transmissionbt.com/browser/trunk/NEWS#L1
- Fix initscript to use the config file properly

* Wed Feb 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.83-3
- rhbz #563090 - fixed config for daemon initscript

* Wed Feb 3 2010 Ankur Sinha <ankursinha@fedoraproject.org> - 1.83-2
- Bugfix - #560180 - changed init script

* Sun Jan 31 2010 Ankur Sinha <ankursinha@fedoraproject.org> - 1.83-1
- New Release
- Fix 1.80 announce error that caused uploads and downloads to periodically freeze
- Fix 1.80 announce timeout error that caused "no response from tracker" message
- Fix 1.80 "file not found" error message that stopped some torrents
- Fix 1.82 crash when adding new torrents via their ftp URL
- Fix 1.80 crash when receiving invalid request messages from peers
- Fix 1.82 error when updating the blocklist
- http://trac.transmissionbt.com/wiki/Changes#version-1.83

* Mon Jan 25 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.82-2
- Fix icon cache 

* Sun Jan 24 2010 Ankur Sinha <ankursinha@fedoraproject.org> - 1.82-1
- Bugfix
- http://trac.transmissionbt.com/wiki/Changes#version-1.82

* Thu Jan 21 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.80-1
- Many major new features including magnet link support, trackerless torrents
- http://trac.transmissionbt.com/wiki/Changes#version-1.80

* Wed Jan 20 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.80-0.6.b5
- Add a initscript for transmission daemon. Fixes rhbz#556228
- Description changes, add group for sub-packages and fix make

* Thu Jan 14 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.80-0.5.b5
- Bug fixes
- http://trac.transmissionbt.com/wiki/Changes#version-1.80b5

* Sat Jan 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.80-0.4.b4
- Build the qt interface as a sub package
- Build daemon as a separate sub package
- Translations are for only the gtk sub package
- Fix obsoletes and add conflicts

* Thu Jan 07 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.80-0.3.b4
- Split package to sub packages

* Tue Jan 05 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.80-0.2.b4
- Add BR GConf2-devel

* Tue Jan 05 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.80-0.1.b4
- 1.80 Beta 4
- http://trac.transmissionbt.com/wiki/Changes#version-1.80b4

* Thu Dec 17 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.80-0.1.b3
- 1.80 Beta 3
- Enable sounds via libcanberra
- http://trac.transmissionbt.com/wiki/Changes#version-1.80b3

* Sun Oct 25 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.76-1
- http://trac.transmissionbt.com/wiki/Changes#version-1.76

* Tue Sep 15 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.75-1
- new upstream release
- Fixes seg fault, rhbz#522783

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 1.74-3
- rebuilt with new openssl

* Tue Aug 25 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.74-2
- Add source

* Tue Aug 25 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.74-1
- Bug fix release
- http://trac.transmissionbt.com/wiki/Changes
- disable static linking explicitly

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 24 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.73-1
- new upstream
- switch to using LZMA source

* Sun Jun 21 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.72-1
- Update to new upstream version
- Drop compiler options patch since upstream has fixed this issue

* Fri Jun 12 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 1.71-1
- Update to upstream version 1.71
- Update compiler options patch to match new upstream release
- Drop patch for not using bundled libevent. Upstream now has been fixed to use the system copy whenever possible
- Don't use vendor tag for desktop file. It is not recommended anymore
- Follow https://fedoraproject.org/wiki/Packaging/Guidelines#All_patches_should_have_an_upstream_bug_link_or_comment

* Thu May 28 2009 Denis Leroy <denis@poolshark.org> - 1.61-1
- Update to upstream version 1.61
- fallocate patch upstreamed
- Patches updated for 1.61

* Fri May 22 2009 Denis Leroy <denis@poolshark.org> - 1.53-1
- Update to upstream 1.53
- XDG Download patch upstreamed
- Security fix CVE-2009-1757 (#500278)

* Sat Mar 28 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.51-2
- Use XDG Download directory (#490950)

* Sat Feb 28 2009 Denis Leroy <denis@poolshark.org> - 1.51-1
- Update to upstream 1.51
- Added icon cache scriplets (#487824)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Denis Leroy <denis@poolshark.org> - 1.50-1
- Update to upstream 1.50
- Ported patches to 1.50, enforce compile flags

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 1.42-2
- rebuild with new openssl

* Wed Dec 31 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.42-1
- Update to 1.42.
- Update event patch to 1.42.

* Fri Nov 21 2008 Denis Leroy <denis@poolshark.org> - 1.40-1
- Update to upstream 1.40
- Ported patches to 1.40

* Sun Sep 28 2008 Denis Leroy <denis@poolshark.org> - 1.34-1
- Update to upstream 1.34
- Added patch to link with distributed libevent library

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.33-2
- fix license tag

* Sun Aug 24 2008 Denis Leroy <denis@poolshark.org> - 1.33-1
- Update to upstream 1.33
- Now dual-licensed
- Gnusource and download dir patches upstreamed

* Wed Jun 18 2008 Denis Leroy <denis@poolshark.org> - 1.22-1
- Update to upstream 1.22

* Sat May 31 2008 Denis Leroy <denis@poolshark.org> - 1.21-1
- Update to upstream 1.21

* Tue May 13 2008 Denis Leroy <denis@poolshark.org> - 1.20-1
- Update to upstream 1.20
- Browser opening patch upstreamed
- New dependencies (dbus, curl)

* Tue May  6 2008 Denis Leroy <denis@poolshark.org> - 1.11-2
- Patch to fix opening issue from browser (#431769)
- Patch to fix hardcoded optimize compile flags

* Fri May  2 2008 Denis Leroy <denis@poolshark.org> - 1.11-1
- Update to upstream 1.11, many bug fixes

* Fri Mar 14 2008 Denis Leroy <denis@poolshark.org> - 1.06-1
- Update to upstream 1.06, bug fixes, memory leak fix

* Sun Feb 10 2008 Denis Leroy <denis@poolshark.org> - 1.05-1
- Update to upstream 1.05, with a bunch of bug fixes

* Thu Jan 31 2008 Denis Leroy <denis@poolshark.org> - 1.03-1
- Update to upstream 1.03

* Wed Jan 23 2008 Denis Leroy <denis@poolshark.org> - 1.02-1
- Update to upstream 1.02, bugfix release

* Sat Jan  5 2008 Denis Leroy <denis@poolshark.org> - 1.00-1
- Update to upstream 1.00. New project URL

* Wed Dec  5 2007 Denis Leroy <denis@poolshark.org> - 0.95-1
- Update to upstream 0.95
- Rebuild with new openssl

* Thu Nov 29 2007 Denis Leroy <denis@poolshark.org> - 0.94-1
- Update to upstream 0.94

* Tue Nov  6 2007 Denis Leroy <denis@poolshark.org> - 0.92-1
- Update to upstream 0.92, important bug fixes

* Sat Nov  3 2007 Denis Leroy <denis@poolshark.org> - 0.91-1
- Update to upstream 0.91
- Removal of -gtk suffix
- Obsoleting manpath patch

* Wed Sep 12 2007 Denis Leroy <denis@poolshark.org> - 0.82-1
- Update to upstream 0.82, many bug fixes
- Added patch to support default user download directory (Bastien Nocera)

* Sat Aug 25 2007 - Bastien Nocera <bnocera@redhat.com> - 0.81-1
- Update to upstream 0.81
- Add work-around for busted tarball without a sub-directory

* Thu Aug 16 2007 Denis Leroy <denis@poolshark.org> - 0.80-1
- Update to upstream 0.80

* Wed May  2 2007 Denis Leroy <denis@poolshark.org> - 0.72-1
- Update to 0.72
- Added libevent BR

* Wed Apr 25 2007 Denis Leroy <denis@poolshark.org> - 0.71-1
- Update to 0.71
- Removed custom desktop file
- Added patch to fix manpath

* Thu Sep 28 2006 Denis Leroy <denis@poolshark.org> - 0.6.1-3
- Added project icon
- Honor cc variable

* Mon Sep 25 2006 Denis Leroy <denis@poolshark.org> - 0.6.1-2
- Removed ldconfig Requires

* Wed Sep 13 2006 Denis Leroy <denis@poolshark.org> - 0.6.1-1
- First version
`
