# bytecompile with Python 3
%global __python %{__python3}
%global provider org.gnome.Lollypop

Name:           lollypop
Version:        1.4.40
Release:        4%{?dist}
Summary:        Music player for GNOME
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/lollypop
Source0:        https://adishatz.org/lollypop/%{name}-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.29.1
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.5
Requires:       gdk-pixbuf2
Requires:       gstreamer1-plugins-base
Requires:       gobject-introspection
Requires:       gtk3
Recommends:     kid3-common
Requires:       libnotify >= 0.7.6
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-pillow
Requires:       python3-beautifulsoup4
Requires:       python3-gstreamer1
Requires:       pango
Requires:       totem-pl-parser
Requires:       gstreamer1-plugins-good
Requires:       libhandy1 >= 1.5
Requires:       yt-dlp
# last.fm support
BuildArch:      noarch
Obsoletes:      lollypop-cli < 1.0.6

%description
Lollypop is a new GNOME music playing application.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i -e 's|libsoup-2.4|libsoup-3.0|' meson.build

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome
chmod +x %{buildroot}%{_bindir}/*%{name}*

%check
#meson_test failed on koji build server with
#url-not-found : <screenshot> failed to connect: Cannot resolve hostname
desktop-file-validate %{buildroot}%{_datadir}/applications/%{provider}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS README.md
%license LICENSE 
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.gresource
%{_libexecdir}/%{name}-sp
%{_datadir}/metainfo/%{provider}.*.xml
%{_datadir}/applications/%{provider}.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/%{provider}.png
%{_datadir}/icons/hicolor/*/apps/%{provider}*.svg
%{_datadir}/icons/hicolor/*/actions/%{provider}-*.svg
%{_datadir}/dbus-1/services/%{provider}.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/%{provider}.SearchProvider.ini
%{python3_sitelib}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.40-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.4.40-1
- Update to 1.4.40

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.39-2
- Rebuilt for Python 3.13

* Mon Apr 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.4.39-1
- Update to 1.4.39

* Wed Apr 03 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.4.38-1
- Update to 1.4.38

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.4.37-4
- Rebuilt for Python 3.12

* Thu Feb 09 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.37-3
- Fix flatpak build

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.37-1
- Update to 1.4.37
- Add RR yt-dlp

* Wed Nov 16 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.36-2
- replaced BR libsoup-2.4 by libsoup-3.0

* Mon Nov 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.36-1
- Update to 1.4.36

* Wed Aug 17 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.35-1
- Update to 1.4.35

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.34-2
- Rebuilt for Python 3.11

* Mon May 02 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.34-1
- Update to 1.4.34

* Fri Apr 15 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.33-1
- Update to 1.4.33

* Thu Apr 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.32-1
- Update to 1.4.32

* Tue Apr 12 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.31-1
- Update to 1.4.31

* Sat Mar 19 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.30-1
- Update to 1.4.30
- Needs now libhandy1 >= 1.5

* Wed Jan 26 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.29-1
- Update to 1.4.29

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.28-1
- Update to 1.4.28

* Wed Jan 12 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.27-1
- Update to 1.4.27

* Tue Dec 21 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.26-1
- Update to 1.4.26

* Mon Dec 13 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.25-1
- Update to 1.4.25

* Fri Nov 19 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.24-1
- Update to 1.4.24

* Tue Aug 24 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.23-1
- Update to 1.4.23

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.22-1
- Update to 1.4.22

* Mon Jul 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.21-1
- Update to 1.4.21

* Wed Jun 23 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.20-1
- Update to 1.4.20

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.19-2
- Rebuilt for Python 3.10

* Tue Apr 06 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.19-1
- Update to 1.4.19

* Tue Mar 23 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.18-1
- Update to 1.4.18

* Fri Mar 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.17-1
- Update to 1.4.17

* Fri Feb 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.16-1
- Update to 1.4.16

* Sun Jan 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.15-1
- Update to 1.4.15

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.14-1
- Update to 1.4.14

* Mon Jan 18 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.13-1
- Update to 1.4.13

* Sat Jan 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.11-1
- Update to 1.4.11

* Sat Jan 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.10-1
- Update to 1.4.10

* Mon Jan 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.9-1
- Update to 1.4.9

* Thu Jan 07 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.4.8-1
- Update to 1.4.8

* Sat Dec 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.7-1
- Update to 1.4.7

* Sat Dec 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.6-1
- Update to 1.4.6

* Sun Oct 25 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5

* Sat Oct 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4

* Thu Oct 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Sat Oct 10 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sun Oct 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Sep 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.0-3
- Add RR libhandy1

* Thu Sep 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.0-2
- Add BR pkgconfig(libhandy-1)

* Thu Sep 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Sat Aug 29 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.6-1
- Update to 1.3.6

* Sat Aug 15 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.5-1
- Update to 1.3.5

* Fri Aug 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.4-2
- Add RR python3-gstreamer1, Python bindings for GStreamer

* Mon Aug 10 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Thu Jul 30 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Fri Jun 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Thu May 28 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.9

* Wed May 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- Remove RR python3-pylast

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.35-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.35-1
- Update to 1.2.35

* Tue Apr 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.34-1
- Update to 1.2.34

* Sat Apr 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.33-1
- Update to 1.2.33

* Sat Mar 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.32-1
- Update to 1.2.32

* Fri Mar 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.31-1
- Update to 1.2.31

* Fri Mar 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.30-1
- Update to 1.2.30

* Sun Mar 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.29-1
- Update to 1.2.29

* Fri Mar 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.26-1
- Update to 1.2.26

* Thu Mar 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.25-1
- Update to 1.2.25

* Wed Mar 11 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.24-1
- Update to 1.2.24

* Sat Feb 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.23-1
- Update to 1.2.23

* Thu Feb 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.22-1
- Update to 1.2.22

* Tue Feb 11 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.21-1
- Update to 1.2.21

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.20-1
- Update to 1.2.20

* Sun Dec 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.19-1
- Update to 1.2.19

* Fri Dec 27 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.18-1
- Update to 1.2.18

* Sun Dec 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-2
- Add RR python3-beautifulsoup4 needed for lyrics

* Tue Nov 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-1
- Update to 1.2.16

* Sun Nov 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15

* Sun Nov 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.14-1
- Update to 1.2.14

* Sun Nov 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.13-1
- Update to 1.2.13

* Tue Nov 12 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Mon Nov 11 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.11-1
- Update to 1.2.11

* Thu Nov 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Tue Nov 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6

* Sun Nov 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Fri Nov 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Thu Oct 31 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Sat Oct 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Wed Oct 23 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Mon Oct 21 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Add pkgconfig(pygobject-3.0)
- Add pkgconfig(libsoup-2.4)

* Fri Sep 27 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.97.3-1
- Update to 1.1.97.3

* Fri Sep 27 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.97.1-1
- Update to 1.1.97.1

* Thu Sep 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.97-1
- Update to 1.1.97

* Thu Sep 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.16-2
- Create EPEL8 package (RHBZ#1755787)

* Sat Aug 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.16-1
- Update to 1.1.4.16
- Fix (RHBZ#1737737), (RHBZ#1748217)

* Sat Aug 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.15-1
- Update to 1.1.4.15

* Thu Aug 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.14-1
- Update to 1.1.4.14

* Wed Aug 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.11-1
- Update to 1.1.4.11

* Mon Jul 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.7-1
- Update to 1.1.4.7
- Drop RR python3-wikipedia

* Thu Jul 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.5-1
- Update to 1.1.4.5

* Thu Jul 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.4-1
- Update to 1.1.4.4

* Mon Jul 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.3-1
- Update to 1.1.4.3

* Mon Jul 08 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.2-1
- Update to 1.1.4.2

* Sun Jul 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4.1-1
- Update to 1.1.4.1

* Sat Jun 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3.1-1
- Update to 1.1.3.1

* Fri Jun 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Sun Jun 23 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Thu Jun 20 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue May 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12

* Wed May 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.11-2
- Add RR gstreamer1-plugins-good
- Add RR python3-pillow

* Mon May 20 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11

* Sun May 12 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10

* Tue May 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Sat May 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Mon Apr 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7

* Wed Apr 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-3
- Obsoletes lollypop-cli

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.0.6-2
- Rebuild with Meson fix for #1699099

* Tue Apr 16 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6
- Drop lollypop-cli

* Wed Apr 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Tue Apr 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Fri Mar 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Fri Mar 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Tue Mar 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0-1
- Update to 1.0

* Mon Mar 11 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.925-1
- Update to 0.9.925

* Fri Mar 08 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.924-3
- Fix do_render:TypeError: Argument 0 does not allow None as a value (RHBZ#1686716)

* Wed Mar 06 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.924-2
- Fix Opening a file from the command line doesn't work (RHBZ#1677701)

* Mon Mar 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.924-1
- Update to 0.9.924

* Thu Feb 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.923-1
- Update to 0.9.923

* Tue Feb 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.922-1
- Update to 0.9.922

* Sun Feb 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.921-1
- Update to 0.9.921

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.916-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.916-1
- Update to 0.9.916

* Mon Jan 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.915-1
- Update to 0.9.915

* Thu Jan 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.914-1
- Update to 0.9.914

* Wed Jan 23 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.913-1
- Update to 0.9.913

* Fri Jan 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.912-1
- Update to 0.9.912

* Thu Jan 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.911-1
- Update to 0.9.911

* Sat Jan 12 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.910-2
- Add %%{name}-fix-radio-restore-state.patch

* Wed Jan 09 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.910-1
- Update to 0.9.910

* Thu Jan 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.909-1
- Update to 0.9.909

* Thu Dec 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.908-1
- Update to 0.9.908

* Wed Dec 26 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.907-1
- Update to 0.9.907

* Thu Dec 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.906-1
- Update to 0.9.906

* Wed Dec 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.905-1
- Update to 0.9.905

* Tue Dec 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.904-1
- Update to 0.9.904

* Sat Dec 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.903-1
- Update to 0.9.903

* Sat Dec 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.902-1
- Update to 0.9.902

* Fri Dec 14 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.900-1
- Update to 0.9.900

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.612-2
- Drop a Python 2 dependency from Python 3 package

* Thu Nov 08 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.612-1
- Update to 0.9.612

* Mon Oct 29 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.610-1
- Update to 0.9.610

* Thu Oct 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.609-1
- Update to 0.9.609

* Thu Oct 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.608-1
- Update to 0.9.608

* Mon Oct 22 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.607-1
- Update to 0.9.607

* Fri Oct 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.605-1
- Update to 0.9.605

* Mon Oct 08 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.604-1
- Update to 0.9.604

* Sun Oct 07 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.602-1
- Update to 0.9.602

* Mon Sep 24 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.601-1
- Update to 0.9.601

* Sun Sep 23 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.600-2
- Add view_lyrics.patch

* Fri Sep 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.600-1
- Update to 0.9.600
- Remove lollypop-portal

* Tue Sep 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.522-2
- Add Patch crash_fix.diff
- Add Patch skip_album_fix.diff (BZ1625407)

* Fri Aug 24 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.522-1
- Update to 0.9.522
- Dropped %%{name}-%%{version}-toolbar_end.patch

* Wed Aug 22 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.521-2
- Add %%{name}-%%{version}-toolbar_end.patch fixes (BZ#1619867)

* Sat Aug 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.521-1
- Update to 0.9.521

* Mon Jul 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.520-1
- Update to 0.9.520

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.519-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.519-1
- Update to 0.9.519

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.518-2
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.518-1
- Update to 0.9.518

* Sat Jun 30 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.517-1
- Update to 0.9.517

* Mon Jun 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.516-1
- Update to 0.9.516

* Thu Jun 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.515-1
- Update to 0.9.515

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.514-2
- Rebuilt for Python 3.7

* Fri May 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.514-1
- Update to 0.9.514

* Wed May 23 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.513-1
- Update to 0.9.513

* Wed May 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.512-1
- Update to 0.9.512

* Wed May 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.511-1
- Update to 0.9.511

* Tue May 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.510-1
- Update to 0.9.510

* Wed May 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.508-1
- Update to 0.9.508

* Thu Apr 26 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.507-1
- Update to 0.9.507

* Thu Apr 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.506-1
- Update to 0.9.506

* Sat Apr 14 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.504-1
- Update to 0.9.504

* Fri Apr 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.502-1
- Update to 0.9.502

* Thu Apr 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.501-1
- Update to 0.9.501

* Thu Apr 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.500-1
- Update to 0.9.500

* Tue Apr 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.403-3
- Changed RR from pyplast to python2-pylast

* Thu Apr 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.403-2
- Add art_album.py.diff (BZ #1562595)
- Add bytecompile with Python 3 %%global __python %%{__python3}

* Thu Mar 29 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.403-1
- Update to 0.9.403

* Wed Mar 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.402-2
- Update lollypop-portal to 0.9.7

* Tue Mar 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.402-1
- Update to 0.9.402

* Wed Mar 14 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.401-1
- Update to 0.9.401
- Cleanup spec file

* Wed Mar 07 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.400-1
- Update to 0.9.400

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.306-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.306-2
- Remove obsolete scriptlets

* Sun Dec 31 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.306-1
- Update to 0.9.306
- Switch to gitlab

* Tue Oct 17 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.304-1
- Update to 0.9.304

* Sat Oct 07 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.303-1
- Update to 0.9.303

* Thu Jul 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.244-1
- Remove rhythmbox2lollypop since it moved to lollypop-cli
- Update lollypop-portal to 3a3a8b1
- Update to 0.9.244

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.243-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.243-2
- Set executable flag for %%{buildroot}%%{_libexecdir}/%%{name}-portal

* Fri Jul 07 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.243-1
- Update to 0.9.243
- Switched to meson build system
- Add BR meson

* Wed Jul 05 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.242-1
- Update to 0.9.242

* Fri Jun 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.240-1
- Update to 0.9.240

* Sat Jun 03 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.239-1
- Update to 0.9.239

* Fri May 26 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.238-1
- Update to 0.9.238

* Sun Apr 16 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.231-1
- Update to 0.9.231
- Dropped %%{name}_fix_handle_locked_DB.patch

* Sat Mar 25 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.230-3
- Add RR totem-pl-parser - (bz#1435866)

* Sat Mar 25 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.230-2
- Add %%{name}_fix_handle_locked_DB.patch - (bz#1431320)

* Tue Feb 28 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.230-1
- Update to 0.9.230

* Tue Jan 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.229-1
- Update to 0.9.229

* Sat Jan 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.226-1
- Update to 0.9.226

* Wed Dec 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.223-5
- remove %%exclude %%{_datadir}/locale/*/LC_MESSAGES/%%{name}.mo
  due missing "*.mo" files (rhbz#1408854)

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.223-4
- Rebuild for Python 3.6

* Sun Dec 11 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.223-3
- Add some documentation fixes

* Sat Dec 10 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.223-2
- Add Requires to base package
- Remove Requires on the subpkg lollypop-portal
- Add NOCONFIGURE=1 ./autogen.sh to subpkg lollypop-portal

* Fri Dec 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.223-1
- Update to 0.9.223
- Add subpkg lollypop-cli

* Thu Dec 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.222-1
- Update to 0.9.222
- Set correct file permission
- Add subpkg lollypop-portal

* Fri Nov 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.220-1
- Update to 0.9.220

* Wed Nov 23 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.219-1
- Update to 0.9.219
- Add %%attr to correct file permisson

* Mon Nov 14 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.216-1
- Update to 0.9.216

* Mon Oct 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.213-1
- Update to 0.9.213

* Sat Oct 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.210-1
- Update to 0.9.210

* Thu Oct 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.209-1
- Update to 0.9.209

* Sun Oct 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.206-1
- Update to 0.9.206
- Added Requires: kid3-common
- Added Requires: python3-pylast
- Added Requires: python3-wikipedia

* Mon Sep 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.205-1
- Update to 0.9.205

* Wed Sep 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.204-1
- Update to 0.9.204
- Use full path for scriptlets
- Corrected ownership of %%{_datadir/%%{name}/ in file section
- Dropped Requires: gstreamer1

* Sun Sep 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.202-1
- Update to 0.9.202
- Added pylast Requirement

- Mon Aug 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.112-2
- Added pylast Requirement

* Mon Jul 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.112-1
- Initial package
