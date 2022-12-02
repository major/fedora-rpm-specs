%global gettext_version 0.19.8
%global glib2_version 2.67.4
%global gtk3_version 3.19.12
%global libsoup_version 3.0
%global webkit2gtk_version 2.33.1

Name:		gnome-online-accounts
Version:	3.46.0
Release:	2%{?dist}
Summary:	Single sign-on framework for GNOME

License:	LGPLv2+
URL:		https://wiki.gnome.org/Projects/GnomeOnlineAccounts
Source0:	https://download.gnome.org/sources/gnome-online-accounts/3.46/%{name}-%{version}.tar.xz

# RHEL >=9 specific
# https://gitlab.gnome.org/GNOME/gnome-online-accounts/-/issues/63
# https://bugzilla.redhat.com/show_bug.cgi?id=1913641
Patch0:		0001-google-Remove-Photos-support.patch
Patch1:         112.patch


BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	gettext >= %{gettext_version}
BuildRequires:	gtk-doc
BuildRequires:	krb5-devel
BuildRequires:	meson
BuildRequires:	pkgconfig(webkit2gtk-4.1) >= %{webkit2gtk_version}
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libsoup-3.0) >= %{libsoup_version}
BuildRequires:	pkgconfig(rest-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	vala

Requires:	glib2%{?_isa} >= %{glib2_version}
Requires:	gtk3%{?_isa} >= %{gtk3_version}
Requires:	libsoup3%{?_isa} >= %{libsoup_version}
Requires:	webkit2gtk4.1%{?_isa} >= %{webkit2gtk_version}

%description
GNOME Online Accounts provides interfaces so that applications and libraries
in GNOME can access the user's online accounts. It has providers for Google,
Nextcloud, Flickr, Foursquare, Microsoft Account, Microsoft Exchange, Fedora,
IMAP/SMTP and Kerberos.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%if 0%{?rhel} >= 9
%patch0 -p1
%endif

%patch1 -p1

%build
%meson \
  -Dexchange=true \
  -Dfedora=true \
  -Dgoogle=true \
  -Dimap_smtp=true \
  -Dkerberos=true \
  -Dlastfm=false \
  -Dmedia_server=false \
  -Downcloud=true \
  -Dwindows_live=true \
  -Dman=true \
  %{nil}

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Goa-1.0.typelib
%{_libdir}/libgoa-1.0.so.0
%{_libdir}/libgoa-1.0.so.0.0.0
%{_libdir}/libgoa-backend-1.0.so.1
%{_libdir}/libgoa-backend-1.0.so.1.0.0
%dir %{_libdir}/goa-1.0
%dir %{_libdir}/goa-1.0/web-extensions
%{_libdir}/goa-1.0/web-extensions/libgoawebextension.so
%{_prefix}/libexec/goa-daemon
%{_prefix}/libexec/goa-identity-service
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/dbus-1/services/org.gnome.Identity.service
%{_datadir}/icons/hicolor/*/apps/goa-*.svg
%{_datadir}/man/man8/goa-daemon.8*
%{_datadir}/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml

%files devel
%{_includedir}/goa-1.0/
%{_libdir}/libgoa-1.0.so
%{_libdir}/libgoa-backend-1.0.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Goa-1.0.gir
%{_libdir}/pkgconfig/goa-1.0.pc
%{_libdir}/pkgconfig/goa-backend-1.0.pc
%{_libdir}/goa-1.0/include
%{_datadir}/vala/

%changelog
* Wed Nov 30 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.46.0-2
- Patch for multiple credential cache issues.

* Mon Sep 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.46.0-1
- 3.46.0

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 3.45.2-1
- Update to 3.45.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 3.45.1-1
- Update to 3.45.1
- Switch to meson build system
- Build against libsoup3

* Wed Mar 30 2022 Debarshi Ray <rishi@fedoraproject.org> - 3.44.0-1
- Update to 3.44.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.43.1-1
- Update to 3.43.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.40.0-3
- Disable the Foursquare provider on RHEL 8 too

* Sat Apr 24 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.40.0-2
- Disable the Flickr and Foursquare providers on RHEL >= 9
- Remove Photos support from the Google provider on RHEL >= 9

* Thu Apr 22 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.40.0-1
- Update to 3.40.0
- Disable the Facebook provider

* Tue Mar 16 2021 Debarshi Ray <rishi@fedoraproject.org> - 3.39.92-1
- Update to 3.39.92

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Aug 10 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.37.90-1
- Update to 3.37.90

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Feb 11 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 04 2020 Debarshi Ray <rishi@fedoraproject.org> - 3.35.3-1
- Update to 3.35.3

* Tue Oct 15 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.35.1-1
- Update to 3.35.1

* Wed Sep 11 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Wed Aug 21 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.33.91-1
- Update to 3.33.91

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Sat Feb 09 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.31.3-2
- Drop the documents integration (fedora-workstation/issue/83)

* Wed Dec 12 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.31.3-1
- Update to 3.31.3

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-3
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-2
- Fix gtk-doc directory ownership

* Mon Sep 03 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.30.0-1
- Update to 3.30.0
- Disable Pocket

* Thu Aug 16 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.29.91-1
- Update to 3.29.91

* Thu Aug  9 2018 Owen Taylor <otaylor@redhat.com> - 3.29.4-2
- Remove Requires: gettext-libs - it is extraneous
- Use a glob for man page, to handle variations in man page compression.

* Wed Jul 18 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.29.4-1
- Update to 3.29.4

* Mon Jul 16 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.29.1-1
- Update to 3.29.1
- Drop RHEL 7 compatibility because Telepathy is no longer supported

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.3-4
- Switch to %%ldconfig_scriptlets

* Fri Jan 12 2018 Tomas Popela <tpopela@redhat.com> - 3.27.3-3
- Adapt to the webkitgtk4 rename

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.3-2
- Remove obsolete scriptlets

* Fri Dec 15 2017 Kalev Lember <klember@redhat.com> - 3.27.3-1
- Update to 3.27.3

* Wed Oct 25 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.27.1-2
- Backport fix for adding multiple accounts of the same type (GNOME #781005)

* Thu Oct 19 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.27.1-1
- Update to 3.27.1

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Tue Sep 19 2017 Troy Dawson <tdawson@redhat.com> - 3.26.0-2
- Cleanup spec file conditionals

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Tue Sep 05 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.92-1
- Update to 3.25.92

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.4-1
- Update to 3.25.4

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 3.25.3-1
- Update to 3.25.3

* Tue May 30 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Mar 17 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Fri Mar 03 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.23.91-1
- Update to 3.23.91

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.23.4-1
- Update to 3.23.4

* Wed Dec 14 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.23.3-1
- Update to 3.23.3

* Wed Dec 14 2016 Kalev Lember <klember@redhat.com> - 3.22.3-1
- Update to 3.22.3

* Tue Nov 15 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-2
- BR vala instead of obsolete vala-tools subpackage

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92
- Co-own gir directories instead of depending on gobject-introspection

* Sat Sep 03 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Don't set group tags

* Tue Aug 30 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.21.90-3
- Set minimum libsoup & webkitgtk4 versions; use pkgconfig(...) for BRs

* Tue Aug 30 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.21.90-2
- Use make_build macro

* Fri Aug 19 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Set minimum glib2 and gtk3 versions

* Wed Jul 20 2016 Richard Hughes <rhughes@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1
- Package vala bindings

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Mar 16 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.19.92.1-1
- Update to 3.19.92.1

* Wed Mar 16 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Fri Feb 12 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.19.4-3
- Disable Telepathy

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Tue Dec 15 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Wed Nov 25 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Wed Oct 14 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Wed Sep 16 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.92.1-1
- Update to 3.17.92.1

* Tue Sep 15 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.92-1
- Update to 3.17.92

* Wed Sep 09 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.91-1
- Update to 3.17.91

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.2-1
- Update to 3.17.2

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Thu Apr 30 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.16.0-2
- Enable Foursquare

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Wed Mar 04 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91
- Use the %%license macro for the COPYING file

* Mon Feb 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.90-1
- Update to 3.15.90

* Mon Jan 19 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.15.4-1
- Update to 3.15.4

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Wed Nov 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Wed Nov 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1

* Wed Nov 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Thu Oct 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-3
- Rebuilt for gobject-introspection 1.41.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Tue Apr 01 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.12.0-2
- Popup is too small to display Facebook authorization (GNOME #726609)

* Tue Mar 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.11.92-1
- Update to 3.11.92

* Sat Mar 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Wed Dec 18 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.11.3-1
- Update to 3.11.3

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Tue Nov 12 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.2-1
- Update to 3.10.2

* Fri Oct 18 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.1-2
- Adapt to changes in the redirect URI used by Facebook (GNOME #710363)

* Wed Oct 16 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Tue Oct 08 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.0-3
- Add a Requires on realmd (Red Hat #949741)

* Fri Sep 27 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.0-2
- Fix GNOME #708462 and #708832

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 29 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-2
- Update to new webkitgtk-2.1.90 API

* Thu Aug 22 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.4-1
- Update to 3.9.4
- Update summary and description to match upstream DOAP file

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Mon Apr 15 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Tue Mar 05 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 26 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.90-2
- Enable IMAP / SMTP

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 06 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.5-1
- Update to 3.7.5

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.4-2
- Rebuilt for libgcr soname bump

* Mon Jan 14 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.4-1
- Update to 3.7.4

* Thu Jan 03 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3

* Sun Nov 18 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.7.2-1
- Update to 3.7.2

* Tue Oct 23 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1

* Mon Oct 15 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Mon Sep 17 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.4-1
- Update to 3.5.4

* Mon Jun 25 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.3-1
- Update to 3.5.3

* Tue Jun 05 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2

* Wed May 02 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1

* Tue Apr 17 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.3.92.1-1
- Update to 3.3.92.1

* Tue Mar 20 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.3.92-1
- Update to 3.3.92

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Brian Pepple <bpepple@fedoraproject.org> - 3.3.0-2
- Enable Windows Live provider.

* Mon Dec 19 2011 Brian Pepple <bpepple@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0.
- Update source url.

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 3.2.0.1-1
- Update to 3.2.0.1

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Tue Aug 30 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90-1
- Update to 3.1.90

* Fri Jul 01 2011 Bastien Nocera <bnocera@redhat.com> 3.1.1-1
- Update to 3.1.1

* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-3
- Add more necessary patches

* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-2
- Update with review comments from Peter Robinson

* Mon Jun 13 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-1
- First version

