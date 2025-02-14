Name: cozy
%global rtld_name com.github.geigi.cozy

Summary: Modern audiobook player
License: GPL-3.0-or-later

Version: 1.3.0
Release: 5%{?dist}

URL: https://cozy.geigi.de
Source0: https://github.com/geigi/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Source99: find-unpatched-imports.sh

# Unbundle python-inject
Patch0: 0000--unbundle-inject.patch

# The appdata XML file does not pass validation
Patch1: 0001-fix-appdata-file.patch

BuildArch: noarch

%global req_adwaita 1.4.0
%global req_py_inject 4.3.1
%global req_py_peewee 3.9.6

BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: libappstream-glib
BuildRequires: libadwaita-devel >= %{req_adwaita}
BuildRequires: meson >= 0.59.0
BuildRequires: python3-devel

%global with_tests 1

%if 0%{?with_tests}
BuildRequires: gstreamer1-plugins-base

BuildRequires: python3dist(distro)
BuildRequires: python3dist(inject) >= %{req_py_inject}
BuildRequires: python3dist(mutagen)
BuildRequires: python3dist(peewee) >= %{req_py_peewee}
BuildRequires: python3dist(pygobject)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytz)
BuildRequires: python3dist(requests)
%endif

Requires: file
Requires: glib2
Requires: libadwaita >= %{req_adwaita}
Requires: gstreamer1-plugins-bad-free
Requires: gstreamer1-plugins-good
Requires: gstreamer1-plugins-ugly-free
Requires: hicolor-icon-theme

# For whatever reason, the Python dependency generator doesn't seem to work
# for this RPM, so we'll just copy-paste the BuildRequires list
Requires: python3dist(distro)
Requires: python3dist(inject) >= %{req_py_inject}
Requires: python3dist(mutagen)
Requires: python3dist(peewee) >= %{req_py_peewee}
Requires: python3dist(pygobject)
Requires: python3dist(pytz)
Requires: python3dist(requests)

# Not available in official Fedora repos
# Requires: gstreamer1-libav


%description
Cozy is a modern audiobook player for Linux.

Here are some of the current features:
- Import your audiobooks into Cozy to browse them comfortably
- Sort your audio books by author, reader & name
- Remembers your playback position
- Sleep timer
- Playback speed control
- Search your library
- Offline Mode! This allows you to keep an audio book on your internal storage
  if you store your audiobooks on an external or network drive.
  Perfect for listening on the go!
- Add mulitple storage locations
- Drag & Drop to import new audio books
- Support for DRM free mp3, m4a (aac, ALAC, …), flac, ogg, opus, wav files
- Mpris integration (Media keys & playback info for desktop environment)


%prep
%setup -q

# Unbundle inject
%patch 0 -p1
rm -rf cozy/ext/inject

# Run the "find unpatched imports" script
"%{SOURCE99}" "$(pwd)"

# Apply other patches
%patch 1 -p1


%build
%meson
%meson_build
%meson_build com.github.geigi.cozy-update-po
%meson_build extra-update-po


%install
%meson_install
%find_lang %{rtld_name}

# Move "actions" icons out of /usr/share/icons/ to avoid conflicts with other packages
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2120689
#      https://github.com/geigi/cozy/issues/710
COZY_ICON_DIR="%{buildroot}%{_datadir}/%{rtld_name}/icons/hicolor/scalable"
install -m 755 -d "${COZY_ICON_DIR}"
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/actions "${COZY_ICON_DIR}/actions"

# Remove the "devel" icon
rm %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{rtld_name}.Devel.svg


%check
%if 0%{?with_tests}
%pytest
%endif

appstream-util validate --nonet %{buildroot}/%{_datadir}/metainfo/%{rtld_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop


%files -f %{rtld_name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{rtld_name}
%{_datadir}/%{rtld_name}/
%{_datadir}/applications/%{rtld_name}.desktop
%{_datadir}/glib-2.0/schemas/%{rtld_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{rtld_name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{rtld_name}-symbolic.svg
%{_metainfodir}/%{rtld_name}.appdata.xml
%{python3_sitelib}/%{name}/


%changelog
* Wed Feb 12 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.0-5
- Remove spurious BuildRequires on python-pytest-runner

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.13

* Sun Mar 03 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3.0-1
- Update to v1.3.0
- Drop Patch2 (fix crash at startup - merged upstream)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Python Maint <python-maint@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.12

* Sun May 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.1-4
- Modify Patch2 to fix yet another crash at startup

* Tue Mar 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.1-3
- Move "actions" icons out of /usr/share/icons to avoid conflicts with other packages
- Add a patch to fix crash at startup
- Convert License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 21 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.1-1
- Update to v1.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.0-1
- Update to v1.2.0

* Fri Dec 31 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1.3-1
- Update to v1.1.3

* Mon Oct 11 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.1.2-2
- Add missing dependencies to fix launching the app
  Resolves: #2013040, #2013041, #2013042

* Fri Aug 20 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1.2-1
- Update to v1.1.2

* Fri Aug 20 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1.1-1
- Update to v1.1.1
- Drop Patch1 (POTFILES references non-existent file - fixed upsteam)
- Don't modify the appdata file in %%prep - no longer needed to pass validation

* Mon Aug 09 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1.0-1
- Update to v1.1.0

* Thu Jul 29 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.4-1
- Update to v1.0.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.3-1
- Update to v1.0.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.10

* Sun May 30 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.1-1
- Update to v1.0.1

* Mon May 10 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.5-1
- Update to latest release

* Sun Apr 25 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.4-1
- Update to latest release

* Wed Apr 21 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.3-1
- Update to latest release

* Tue Apr 20 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.2-1
- Update to latest release

* Mon Apr 19 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.1-1
- Update to latest release

* Mon Feb 08 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8.1-1
- Update to latest release
- Fix license tag - cozy is GPLv3, the "and ASL 2.0" part
  came from a bundled library, which has been un-bundled

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.8-1
- Update to latest release

* Mon Nov 30 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.7-1
- Update to latest release

* Sun Nov 15 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.5-1
- Update to latest release

* Sat Nov 14 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.3-1
- Update to latest release

* Thu Oct 01 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.2-2
- Unbundle python3-inject

* Mon Sep 28 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.2-1
- Update to latest release
- Use python3dist() for specifying dependencies

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.1-1
- Update to latest release

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7-1
- Update to latest release
- Put tests behind an enable/disable macro

* Fri Sep 11 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.19-1
- Initial packaging

