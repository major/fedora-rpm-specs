%global appid org.gajim.Gajim

Name:     gajim
Version:  1.7.3
Release:  9%{?dist}
Summary:  Jabber client written in PyGTK
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
URL:      https://gajim.org/
Source0:  https://gajim.org/downloads/1.7/gajim-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

## Hard requirements
Requires:    python3-gobject >= 3.42
Requires:    cairo >= 1.16
Requires:    python3-pillow
Requires:    gtk3 >= 3.24.30
Requires:    glib2 >= 2.60
Requires:    gtksourceview4
Requires:    pango >= 1.50
Requires:    sqlite-libs >= 3.33
Requires:    hicolor-icon-theme
## Optional, but not too big and not worth exploding the test matrix for
# For gajim-remote, desktop notifications, logind, NetworkManager, ...
Requires:    python3-dbus
## Optional, roughly in the order listed in upstream README.md
# OpenPGP message encryption - Encrypting chat messages with OpenPGP keys
Recommends:  python3-gnupg
# Spell checker - Spellchecking of composed messages
Recommends:  gspell
# Password storage
Recommends:  libsecret
# UPnP-IGD - Ability to request your router to forward port for file transfer
Recommends:  gupnp-igd
# Sharing location
Recommends:  geoclue2-libs
# Sound
Recommends:  gsound
# Audio/Video - Ability to start audio and video chat
Recommends:  farstream02
Recommends:  gstreamer1
Recommends:  gstreamer1-plugins-base
Recommends:  gstreamer1-plugins-good-gtk
## Plugins
# OMEMO
Recommends:  python3-axolotl
Recommends:  python3-protobuf
Recommends:  python3-qrcode

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's developers is
to provide a full featured and easy to use xmpp client for the GTK+ users.
Gajim does not require GNOME to run, even though it exists with it nicely.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
./pep517build/build_metadata.py --output-dir dist/metadata

%install
%pyproject_install
./pep517build/install_metadata.py dist/metadata --prefix %{buildroot}/%{_prefix}
%pyproject_save_files gajim

# RHEL <= 9 doesn't support .desktop files with version 1.5,
# see: https://bugzilla.redhat.com/show_bug.cgi?id=2107278
%if 0%{?rhel} && 0%{?rhel} <= 9
sed -e 's/^SingleMainWindow=/X-GNOME-SingleWindow=/' \
    -i %{buildroot}/%{_datadir}/applications/%{appid}.desktop
%endif

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{appid}.appdata.xml

%find_lang %{name}

%files -f %{pyproject_files} -f %{name}.lang
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-remote.1*
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid}-symbolic.svg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.3-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 1.7.3-3
- Rebuilt for Python 3.12

* Tue Apr 04 2023 Michael Kuhn <suraia@fedoraproject.org> - 1.7.3-2
- Recommend python3-qrcode for OMEMO (#2181758)

* Tue Apr 04 2023 Michael Kuhn <suraia@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3

* Sat Mar 11 2023 Michael Kuhn <suraia@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Thu Feb 09 2023 Michael Kuhn <suraia@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Michael Kuhn <suraia@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Sat Jan 07 2023 Michael Kuhn <suraia@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sat Dec 03 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Mon Oct 31 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Sun Oct 09 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Mon Sep 19 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Mon Sep 19 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0
- CVE-2022-39835

* Sun Jul 24 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.7-1
- Update to 1.4.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.6-1
- Update to 1.4.6

* Mon Jun 27 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5

* Sat Jun 18 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4

* Sun Jun 12 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.3-2
- Add (weak) dependencies for OMEMO plugin

* Thu Jun 02 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3
- Update to newer Python packaging guidelines

* Wed May 25 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sat May 21 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Sat May 14 2022 Michael Kuhn <suraia@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 10 2021 Michael Kuhn <suraia@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.2-2
- Rebuilt for Python 3.10

* Sat Apr 24 2021 Michael Kuhn <suraia@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2 (#1953220)

* Mon Mar 01 2021 Michael Kuhn <suraia@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1
- Include plugin_installer (#1884903)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Michal Schmidt <mschmidt@redhat.com> - 1.2.0-1
- Upstream release 1.2.0.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Michal Schmidt <mschmidt@redhat.com> - 1.1.3-1
- Upstream release 1.1.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Michal Schmidt <mschmidt@redhat.com> - 1.1.2-3
- Drop python3-crypto dependency.
- Enable python dependency generator.

* Mon Jan 28 2019 Michal Schmidt <mschmidt@redhat.com> - 1.1.2-2
- Require python-precis_i18n now that it's available.

* Thu Jan 24 2019 Michal Schmidt <mschmidt@redhat.com> - 1.1.2-1
- Upstream release 1.1.2.

* Fri Jan 04 2019 Michal Schmidt <mschmidt@redhat.com> - 1.1.1-1
- Upstream release 1.1.1.
- Make precis-i18n dep optional until it's available in Fedora.

* Wed Nov 14 2018 Michal Schmidt <mschmidt@redhat.com> - 1.1.0-2
- Update runtime requirements according to upstream README.

* Wed Nov 14 2018 Michal Schmidt <mschmidt@redhat.com> - 1.1.0-1
- Upstream release 1.1.0.

* Thu Jul 26 2018 Michal Schmidt <mschmidt@redhat.com> - 1.0.3-3
- Apply upstream patch for getting idle time from Mutter (no X11 needed).

* Thu Jul 26 2018 Michal Schmidt <mschmidt@redhat.com> - 1.0.3-2
- Prefer x11 backend for working status icon and idle detection.

* Mon Jul 23 2018 Michal Schmidt <mschmidt@redhat.com> - 1.0.3-1
- Upstream release 1.0.3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.7

* Tue Apr 03 2018 Michal Schmidt <mschmidt@redhat.com> - 1.0.1-1
- Upstream release 1.0.1.
- Add patch from upstream to fix py3_install.

* Mon Mar 19 2018 Michal Schmidt <mschmidt@redhat.com> - 1.0.0-1
- Upstream release 1.0.0
- now using Python3, GTK3.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.9-3
- Remove obsolete scriptlets

* Mon Dec 04 2017 Michal Schmidt <mschmidt@redhat.com> - 0.16.9-2
- Bump minimum required version of python2-nbxmpp.

* Mon Dec 04 2017 Michal Schmidt <mschmidt@redhat.com> - 0.16.9-1
- Upstream release 0.16.9.
- Refer to python dependencies using their current package names.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Michal Schmidt <mschmidt@redhat.com> - 0.16.8-1
- Upstream release 0.16.8. (#1458616)
- Makes XEP-0146 Commands opt-in (CVE-2016-10376, #1456364)

* Mon Feb 06 2017 Michal Schmidt <mschmidt@redhat.com> - 0.16.7-1
- Upstream release 0.16.7. (#1418487)

* Mon Oct 03 2016 Michal Schmidt <mschmidt@redhat.com> - 0.16.6-1
- Upstream release 0.16.6. (#1381093)
- Fixes crash with broken plugins. (#1381214)
- Minor spec file tweaks.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Michal Schmidt <mschmidt@redhat.com> - 0.16.5-2
- Use weak dependencies for most of the optional features. (#1293082)
- Additional Recommends for A/V calls. (#1231496, #1279047)

* Tue Jan 05 2016 Michal Schmidt <mschmidt@redhat.com> - 0.16.5-1
- Upstream release 0.16.5. (#1294552)
- CVE-2015-8688 (#1295475, #1295476)

* Thu Nov 05 2015 Michal Schmidt <mschmidt@redhat.com> - 0.16.4-3
- Apply patches from upstream gajim_0.16 branch.
- Drop demandimport disabling patch.

* Thu Oct 15 2015 Michal Schmidt <mschmidt@redhat.com> - 0.16.4-2
- Disable demandimport to fix gst detection.

* Wed Oct 14 2015 Michal Schmidt <mschmidt@redhat.com> - 0.16.4-1
- Upstream release 0.16.4. (#1246802)
- Require python-avahi instead of avahi-ui-tools. (#1264166)

* Fri Jul 31 2015 Matej Cepl <mcepl@redhat.com> - 0.16.3-1
- Upstream release 0.16.3.

* Mon Jul 27 2015 Matej Cepl <mcepl@redhat.com> - 0.16.2-2
- Bump the Requires version of python-nbxmpp to 0.5.3 as required
  by the upstream.

* Mon Jul 27 2015 Matej Cepl <mcepl@redhat.com> - 0.16.2-1
- Upstream release 0.16.2.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Michal Schmidt <mschmidt@redhat.com> - 0.16.1-3
- Bump required version of python-nbxmpp.

* Mon Mar 02 2015 Michal Schmidt <mschmidt@redhat.com> - 0.16.1-2
- Force Python 2. Gajim is not quite ready for Python 3.

* Mon Mar 02 2015 Michal Schmidt <mschmidt@redhat.com> - 0.16.1-1
- Upstream release 0.16.1.

* Thu Oct 16 2014 Michal Schmidt <mschmidt@redhat.com> - 0.16-1
- Upstream release 0.16.

* Mon Aug 11 2014 Michal Schmidt <mschmidt@redhat.com> - 0.16-0.3.rc2
- Upstream release 0.16 rc2.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Michal Schmidt <mschmidt@redhat.com> - 0.16-0.1.rc1
- Update to 0.16 rc1
- Update Requires.

* Fri Dec  6 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.15.3-5
- Fix path to docs where doc dir is unversioned (#993765).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Michal Schmidt <mschmidt@redhat.com> - 0.15.3-3
- Fix connecting to non-SSL servers (#953243).
- Remove unused patch files.

* Mon Apr 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.15.3-2
- Drop desktop vendor tag.

* Wed Mar 20 2013 Michal Schmidt <mschmidt@redhat.com> - 0.15.3-1
- Upstream bugfix release (#923692, #875820, #875809).
- Require python-pyasn1 (#826737).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 31 2012 Michal Schmidt <mschmidt@redhat.com> - 0.15.2-1
- Upstream bugfix release.
- Dropped all patches, already included.

* Mon Aug 06 2012 Michal Schmidt <mschmidt@redhat.com> - 0.15-5
- Apply upstream patch to use farstream for audio/video (#845825)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Michal Schmidt <mschmidt@redhat.com> - 0.15-3
- Require gupnp-igd-python (#825035)

* Tue Apr 17 2012 Michal Schmidt <mschmidt@redhat.com> - 0.15-2
- CVE-2012-2093 gajim (LaTeX module): Insecure creation of temporary file

* Mon Mar 19 2012 Michal Schmidt <mschmidt@redhat.com> - 0.15-1
- Upstream release 0.15.

* Mon Mar 12 2012 Michal Schmidt <mschmidt@redhat.com> - 0.15-0.5.beta4
- Drop the requirement on farsight2-python. It's available no more in F17.
  Upstream needs to be ported to farstream.

* Thu Jan 26 2012 Michal Schmidt <mschmidt@redhat.com> - 0.15-0.4.beta4
- Upstream release 0.15 beta4.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.3.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Michal Schmidt <mschmidt@redhat.com> 0.15-0.2.beta3
- Upstream release 0.15 beta3.
- Drop gajim-0.13.90-pygtk-crash-python2.7-workaround.patch
  Cannot reproduce the crash anymore.

* Tue Oct 11 2011 Michal Schmidt <mschmidt@redhat.com> 0.15-0.1.beta2
- Upstream release 0.15 beta2.

* Mon Jun 20 2011 Michal Schmidt <mschmidt@redhat.com> 0.14.3-1
- Upstream bugfix release.
- gajim-0.14-handle-read-before-close.patch already applied.

* Thu Jun 09 2011 Michal Schmidt <mschmidt@redhat.com> 0.14.2-1
- Upstream bugfix release.
- Dropped a merged patch.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Michal Schmidt <mschmidt@redhat.com> 0.14.1-3
- Fix a regression noted by Peter Lemenkov in Bodhi.
  (Could not connect to gmail.com)

* Fri Nov 05 2010 Michal Schmidt <mschmidt@redhat.com> 0.14.1-2
- Fix high CPU usage when the server announces a strange streamhost
  (RHBZ#649986)

* Tue Oct 26 2010 Michal Schmidt <mschmidt@redhat.com> 0.14.1-1
- Upstream bugfix release.
- Dropped merged patches.

* Tue Sep 21 2010 Michal Schmidt <mschmidt@redhat.com> 0.14-4
- Replace our gnome-keyring patch with one picked from upstream hg.
- Prevent traceback when receiving strange reply to iq:last.

* Mon Sep 20 2010 Michal Schmidt <mschmidt@redhat.com> 0.14-3
- Require gstreamer-python too. (RHBZ#632927)

* Tue Sep 14 2010 Michal Schmidt <mschmidt@redhat.com> 0.14-2
- Require farsight2-python for audio/video. (RHBZ#632927)

* Mon Sep 06 2010 Michal Schmidt <mschmidt@redhat.com> 0.14-1
- Update to 0.14 release.

* Thu Aug 19 2010 Michal Schmidt <mschmidt@redhat.com> 0.13.90-1
- Update to 0.13.90 (a.k.a. 0.14 beta1)
- Icon cache handling.
- Cleanups and fixes of Requires.
- Refresh pygtk crash patch.
- Update gnome-keyring patch.
- Remove now unnecessary declaration and cleaning of BuildRoot.

* Tue Aug 10 2010 Michal Schmidt <mschmidt@redhat.com> 0.13.4-2
- Workaround pygtk crash with Python 2.7 (RHBZ#621887).

* Sat Apr 03 2010 Michal Schmidt <mschmidt@redhat.com> 0.13.4-1
- Update to upstream bugfix release 0.13.4.

* Sun Mar 28 2010 Michal Schmidt <mschmidt@redhat.com> 0.13.4-0.1.20100328hg
- Update to current gajim_0.13 branch to fix contact syncing (RHBZ#577534).

* Mon Mar 15 2010 Michal Schmidt <mschmidt@redhat.com> 0.13.3-3
- What the trayicon really needs is gnome-python2-libegg (RHBZ#573358).

* Mon Mar 15 2010 Michal Schmidt <mschmidt@redhat.com> 0.13.3-2
- Require gnome-python2-extras for trayicon (RHBZ#573358).

* Mon Mar 08 2010 Michal Schmidt <mschmidt@redhat.com> 0.13.3-1
- Update to 0.13.3.
- Add gajim-0.13.3-gnome-keyring-CancelledError.patch (RHBZ#556374).

* Fri Feb 05 2010 Michal Schmidt <mschmidt@redhat.com> - 0.13.2-1
- Version bump to 0.13.2. (RHBZ#541470)
- 0.13.1 and 0.13.2 are bugfix releases.
- New in 0.13:
  * BOSH connection support
  * Roster versioning support
  * Interface to send XHTML messages
  * Changelog: http://hg.gajim.org/gajim/file/cb35a23ac836/ChangeLog
  * Bugs fixed: http://trac.gajim.org/query?status=closed&milestone=0.13
- 'idle' and 'gtkspell' modules are now implemented in Python using ctype.
- Internal 'trayicon' module is not necessary with gnome-python2-desktop.
- With no more binary modules included the package is now noarch.
- Require python-libasyncns for src/common/resolver.py.
- --enable-remote is no longer recognized by ./configure.
- Hardlink identical scripts.
- Remove fc8, fc9 support.

* Sat Sep 19 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.12.5-1
- Version bump to 0.12.5. (Red Hat Bugzilla #516191)
  * Fixed history manager.
  * Improved file transfer.
  * http://trac.gajim.org/query?status=closed&milestone=0.12.4
  * http://trac.gajim.org/browser/ChangeLog?rev=5f8edb79072f

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.12.3-3
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 0.12.3-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.12.3-1
- Version bump to 0.12.3. (Red Hat Bugzilla #510803)
  * Better keepalive / ping behaviour.
  * Fixed custom port handling.
  * Fixed PEP discovery.
  * Fixed PLAIN authentication (in particular with Google Talk).
  * Fixed SSL with some servers.
  * Handle XFCE notification-daemon.
  * Improve Kerberos support.
  * NetworkManager 0.7 support.
  * Restore old behaviour of click on systray: left click to open events.
  * Totem support for played music.
  * http://trac.gajim.org/query?status=closed&milestone=0.12.2

* Tue Jul 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.12.1-2
- Replaced 'License: GPLv2' with 'License: GPLv3'.
- Added 'Requires: gnupg python-crypto python-GnuPGInterface'. (Red Hat
  Bugzilla #510804)

* Sat May 02 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.12.1-3
- Added 'Requires: gnome-python2-bonobo'. (Red Hat Bugzilla #470181)

* Tue Feb 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 0.12.1-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.12.1-1
- Version bump to 0.12.1.
  * Fixed click on notifications when text string is empty.
  * Fixed file transfer.
  * Improve systray popup menu.
  * Translation updates: de.
- /usr/share/gajim/src/gajim-{remote}.py need not contain shebangs nor have the
  executable bits.

* Thu Dec 18 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.12-1
- Version bump to 0.12.
  * Better auto-away support.
  * Better sessions support.
  * Fixed Banshee support.
  * Fixed end to end encryption autonegation.
  * Fixed GSSAPI authentication.
  * Fixed text rendering in notifications.
  * Quodlibet support.
  * http://trac.gajim.org/query?status=closed&milestone=0.12
  * http://trac.gajim.org/browser/tags/gajim-0.12/ChangeLog
- Added 'Requires: notify-python python-kerberos'.

* Sun Nov 30 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.12-0.1.beta1
- Version bump to 0.12 beta1. (Red Hat Bugzilla #471295)
- Added 'Requires: pyOpenSSL'. (Red Hat Bugzilla #467523)
- Added 'Requires: python-sexy'.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.11.4-7
- Rebuilding with python-2.6 in Rawhide.

* Sun Nov 09 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.11.4-6
- Added 'Requires: gnome-python2-gnome' on all distributions starting from
  Fedora 10. (Red Hat Bugzilla #470181)

* Tue Oct 28 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.11.4-5
- Added 'Requires: avahi-tools'.

* Mon Jul 14 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.11.4-4
- Rebuilding to overcome Koji outage.

* Mon Jul 14 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.11.4-3
- Updated BuildRoot according to Fedora packaging guidelines.
- Added 'Requires: gnome-python2-canvas'. (Red Hat Bugzilla #454622)
- Removed 'BuildRequires: pkgconfig' and dropped version from
  'BuildRequires: pygtk2-devel'.
- Fixed docdir and removed empty README.

* Tue Feb 19 2008 Release Engineering <rel-eng@fedoraproject.org> - 0.11.4-2
- Autorebuild for gcc-4.3.

* Wed Dec 26 2007 Matěj Cepl <mcepl@redhat.com> 0.11.4-1
- New upstream release.

* Sun Nov 25 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 0.11.3-2
- Fix problem with python(abi)
- Add Requires: python-docutils

* Sun Nov 18 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 0.11.3-1
- Update to 0.11.3 (#315931)
- Fix Licence tag

* Fri Feb 23 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 0.11.1-1
- Update to 0.11.1
- Remove python-sqlite2 dependency (it's now provided by python-2.5)

* Tue Jan 23 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 0.11.1-0.1.pre1
- Update to 0.11.1-pre1

* Sun Jan 14 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 0.11-1
- Update to 0.11

* Thu Dec 21 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.10.1-4
- Rebuild for new Python.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.10.1-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.10.1-2
- Rebuild for FE6
- Fix mixed-use-of-spaces-and-tabs rpmlint warning

* Mon Jun  5 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.10.1-1
- Update to 0.10.1
- Change e-mail address in ChangeLog

* Tue May  2 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.10-1
- Update to 0.10

* Wed Apr 19 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.10-0.1.pre2
- Update to 0.10-pre2

* Thu Apr 13 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.10-0.1.pre1
- Update to 0.10-pre1
- Drop patches

* Thu Mar 30 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.9.1-3
- Remove Gnome dependencies
- Fix crash with notify-daemon (#187274, Stefan Plewako)
  http://trac.gajim.org/ticket/1347

* Tue Feb 14 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.9.1-2
- Rebuild for Fedora Extras 5

* Sun Jan 15 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 0.9.1-1
- update to 0.9.1 (Eric Tanguy, #176614)
- drop aplay.patch
- fix compilation with modular X.Org X11R7

* Tue Sep  6 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.8.2-1
- new version 0.8.2
- remove patches .cflags, .po, .x86_64, .remote (pushed upstream)

* Sat Sep  3 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.8.1-1
- Version 0.8.1
- drop gajim-remote.py file (included in tarball)

* Wed Aug 24 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.8-5
- Don't build internal modules

* Wed Aug 24 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.8-4
- Add missing BuildRequires:  desktop-file-utils

* Wed Aug 24 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.8-3
- add .x86_64.patch (fix broken lib dir)

* Wed Aug 24 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.8-2
- fix gajim-remote.py script

* Sat Aug 20 2005 Dawid Gajownik <gajownik[AT]gmail.com> - 0.8-1
- Initial RPM release.
