%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		geary
Version:	46.0
Release:	5%{?dist}
Summary:	A lightweight email program designed around conversations
# Geary is under LGPL-2.1-or-later.
# SQLite3-unicodesn code is in the Public Domain.
# libstemmer.vapi is covered by the BSD license.
# libunwind.vapi is covered by the MIT (aka Expat) license.
# Icons are under CC-BY-3.0, CC-BY-SA-3.0 or in the Public Domain (see
# COPYING.icons).
# As libstemmer.vapi and libunwind.vapi are built into the same binary with
# LGPLv2+ code, we end up with the more restrictive LGPLv2+ license covering
# the whole binary, so we don't need to specify BSD and MIT separately.
# Automatically converted from old format: Public Domain - review is highly recommended.
License:	LGPL-2.1-or-later AND CC-BY-3.0 AND CC-BY-SA-3.0 AND LicenseRef-Callaway-Public-Domain
URL:		https://wiki.gnome.org/Apps/Geary
Source0:	https://download.gnome.org/sources/geary/46/%{name}-%{tarball_version}.tar.xz

BuildRequires:	meson >= 0.49
BuildRequires:	vala >= 0.26.0
BuildRequires:	valadoc
# primary deps
BuildRequires:	pkgconfig(glib-2.0) >= 2.68
BuildRequires:	pkgconfig(gmime-3.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.24.24
BuildRequires:	pkgconfig(sqlite3) >= 3.12
BuildRequires:	pkgconfig(webkit2gtk-4.1)
# secondary deps
BuildRequires:	libstemmer-devel
BuildRequires:	pkgconfig(appstream-glib) >= 0.7.10
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(enchant-2) >= 2.1
BuildRequires:	pkgconfig(folks) >= 0.11
BuildRequires:	pkgconfig(gck-1)
BuildRequires:	pkgconfig(gcr-3) >= 3.10.1
BuildRequires:	pkgconfig(gdk-3.0) >= 3.24.24
BuildRequires:	pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:	pkgconfig(gio-2.0) >= 2.54
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	pkgconfig(gthread-2.0) >= 2.54
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(javascriptcoregtk-4.1)
BuildRequires:	pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:	pkgconfig(libhandy-1) >= 1.2.1
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libsecret-1) >= 0.11
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libunwind) >= 1.1
BuildRequires:	pkgconfig(libunwind-generic) >= 1.1
BuildRequires:	pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:	pkgconfig(libytnef) >= 1.9.3
BuildRequires:	pkgconfig(webkit2gtk-web-extension-4.1)

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	python3
BuildRequires:	symlinks fakechroot
Requires:	hicolor-icon-theme
Recommends:	gnome-keyring

%description
Geary is a new email reader for GNOME designed to let you read your
email quickly and effortlessly. Its interface is based on
conversations, so you can easily read an entire discussion without
having to click from message to message. Geary is still in early
development and has limited features today, but we're planning to add
drag-and-drop attachments, lightning-fast searching, multiple account
support and much more. Eventually we'd like Geary to have an
extensible plugin architecture so that developers will be able to add
all kinds of nifty features in a modular way.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson -Dprofile=release
%meson_build

%install
%meson_install

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.gnome.Geary.desktop \
  %{buildroot}%{_datadir}/applications/geary-autostart.desktop

pushd %{buildroot}
fakechroot -- symlinks -C -cvr %{_datadir}/help
popd

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING COPYING.icons
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/geary
%{_libdir}/geary
%{_datadir}/geary
%{_datadir}/applications/org.gnome.Geary.desktop
%{_datadir}/applications/geary-autostart.desktop
%{_metainfodir}/org.gnome.Geary.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Geary.service
%{_datadir}/glib-2.0/schemas/org.gnome.Geary.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Geary*
%{_datadir}/icons/hicolor/*/actions/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 46.0-4
- Rebuild for ICU 76

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 46.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 30 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0 (#2281627)

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 44.1-4
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 17 2023 Kalev Lember <klember@redhat.com> - 44.1-1
- Update to 44.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 44.0-2
- Rebuilt for ICU 73.2

* Thu Jul 06 2023 Kalev Lember <klember@redhat.com> - 44.0-1
- Update to 44.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 43.0-2
- Rebuild for ICU 72

* Fri Sep 30 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Thu Aug 18 2022 Kalev Lember <klember@redhat.com> - 40.0-9
- Build against libsoup 3 (rhbz#2119119)

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 40.0-8
- Rebuilt for ICU 71.1

* Mon Jul 25 2022 Thomas Moschny <thomas.moschny@gmx.de> - 40.0-7
- Fix FTBFS on F37.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Thomas Moschny <thomas.moschny@gmx.de> - 40.0-5
- Fix FTBFS on F36.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 40.0-2
- Rebuild for ICU 69

* Fri Apr 23 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Wed Apr 14 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Wed Mar 17 2021 Kalev Lember <klember@redhat.com> - 40~alpha-3
- Backport another upstream crash fix

* Thu Mar 11 2021 Kalev Lember <klember@redhat.com> - 40~alpha-2
- Backport an upstream fix for latest WebKit compatibility

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha-1
- Update to 40.alpha
- Update licensing information in the spec file

* Tue Feb 16 2021 Kalev Lember <klember@redhat.com> - 3.38.2-2
- Rebuilt for folks soname bump

* Sun Feb 07 2021 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct  4 2020 Thomas Moschny <thomas.moschny@gmx.de> - 3.38.1-1
- Update to 3.38.1.

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 3.38.0.1-1
- Update to 3.38.0.1

* Sun Sep 13 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 06 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Thu Aug 27 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Wed Aug 19 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Mon May 04 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Mon Apr 06 2020 Kalev Lember <klember@redhat.com> - 3.36.1-2
- Move gnome-keyring recommends here instead of libsecret (#1781864, #1813547)

* Sun Mar 29 2020 Thomas Moschny <thomas.moschny@gmx.de> - 3.36.1-1
- Update to 3.36.1.
- Fix absolute symlinks.

* Fri Mar 13 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-2
- Rebuild for GNOME 3.34.1 megaupdate

* Mon Oct  7 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.34.1-1
- Update to 3.34.1.
- Update BRs.

* Sun Sep 22 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Wed Sep 11 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Sat Aug 31 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.33.90-1
- Update to 3.33.90.
- Update BRs.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Kalev Lember <klember@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Sun Apr 28 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.32.1-1
- Update to 3.32.1.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.0-2
- Rebuild with Meson fix for #1699099

* Sun Mar 17 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.32-1
- Update to 3.32.

* Mon Mar 11 2019 Thomas Moschny <thomas.moschny@gmx.de> - 0.13.3-1
- Update to 0.13.3.

* Thu Mar  7 2019 Thomas Moschny <thomas.moschny@gmx.de> - 0.13.2-1
- Update to 0.13.2.

* Thu Feb 21 2019 Kalev Lember <klember@redhat.com> - 0.13.1-1
- Update to 0.13.1
- Use upstream screenshots for appdata

* Mon Feb 18 2019 Thomas Moschny <thomas.moschny@gmx.de> - 0.13.0-2
- Add patch to make dependency on libunwind optional.

* Sun Feb 17 2019 Thomas Moschny <thomas.moschny@gmx.de> - 0.13.0-1
- Update to 0.13.0.
- Geary uses the Meson build system now.
- Update dependencies.

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.12.4-3
- Update BRs for vala packaging changes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.4-1
- Update to 0.12.4.
- Update BRs.

* Sat Jul 14 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.3-1
- Update to 0.12.3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.2-1
- Update to 0.12.2.

* Tue Feb 13 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.1-1
- Update to 0.12.1.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-2
- Remove obsolete scriptlets

* Wed Oct  4 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.0-1
- Update to 0.12.0.
- Rebase patch.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-0.3.20170322.02e3d30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-0.2.20170322.02e3d30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.0-0.1.20170322.02e3d30
- Update to 0.12 snapshot version (move to webkitgtk4).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.11.3-1
- Update to 0.11.3.

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 0.11.2-1
- Update to 0.11.2

* Wed Jun 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.11.1-2
- Rebuild on F24.

* Mon Jun 27 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.11.1-1
- Update to 0.11.1.

* Tue May 17 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.11.0-2
- Restore doc files.

* Sun May 15 2016 Kalev Lember <klember@redhat.com> - 0.11.0-1
- Update to 0.11.0
- Use out of tree build

* Sun Mar 27 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.10.0-5
- Include upstream patches for crashes using WebKitGTK+ 2.4.10.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Thomas Moschny <thomas.moschny@gmx.de> - 0.10.0-2
- Update dependencies.
- Remove conditionals for Fedora < 20.
- New appstream-util features available only in Fedora >= 22.

* Thu Apr 16 2015 Kalev Lember <kalevlember@gmail.com> - 0.10.0-1
- Update to 0.10.0
- Use license macro for COPYING files

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 0.9.1-2
- Use better AppData screenshots

* Wed Feb  4 2015 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.1-1
- Update to 0.9.1.

* Mon Jan 26 2015 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.0-1
- Update to 0.9.0.

* Sat Dec 20 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.8.3-1
- Update to 0.8.3.

* Sun Nov 23 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.8.2-1
- Update to 0.8.2.
- Update License tag.

* Sat Oct 11 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.8.1-1
- Update to 0.8.1.
- Remove patch applied upstream.

* Mon Sep 29 2014 Debarshi Ray <rishi@fedoraproject.org> - 0.8.0-2
- Fix toolbar icon size (GNOME 732065)

* Fri Sep 19 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.8.0-1
- Update to 0.8.0.

* Wed Sep  3 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2 (fixes CVE-2014-5444)
- Drop upstreamed patch for vala 0.25.x support

* Wed Aug 27 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.7.1-1
- Update to 0.7.1.
- Update patches.
- Drop obsolete dependency on libunique.

* Fri Aug 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.2-1
- Update to 0.6.2.
- Drop patch applied upstream.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.1-2
- Add patch to fix timezone in date header (rhbz#1121306).
- Add patch to build with vala 0.25.1.

* Fri Jul  4 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.1-1
- Update to 0.6.1.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.6.0-1
- Update to 0.6.0.

* Tue Feb 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.3-1
- Update to 0.4.3.
- Cherry-pick patch to compile with WebKitGTK 2.3.x.
- Update source URL.

* Sat Nov 23 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-1
- Update to 0.4.2.
- Drop patch applied upstream.

* Sat Nov 16 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.1-1
- Update to 0.4.1.

* Wed Oct  9 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-1
- Update to 0.4.0.
- Drop patch applied upstream.
- Update build requirements.
- Include appdata file.

* Sat Aug 17 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.1-3
- Fix FTBFS with WebKitGTK+ 2.1 (rhbz#992326).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.1-1
- Update to 0.3.1.

* Wed Mar 20 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.0-1
- Update to 0.3.0.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.2.2-1
- Update to 0.2.2.

* Wed Oct 10 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.2.1-1
- Update to 0.2.1.
- Add missing BR on intltool.

* Thu Oct  4 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.2.0-1
- Update to 0.2.0.

* Sun Sep 16 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.1.90-1.git9867509
- Update to current head.
- Fix icon items in %%files.

* Sat Sep  1 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.1.0-3.gitb6c50c2
- Update to current head.

* Wed Aug 22 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.1.0-2.git5665a4f
- Update to current head.
- Remove wildcards from %%files section.
- Do not pack other binaries than 'geary'.

* Sun Aug 19 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.1.0-1.git4ff24e0
- New package.
