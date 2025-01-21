%define _legacy_common_support 1

%ifarch %{ix86} x86_64
%define with_spice 1
%endif

Name:           vinagre
Version:        3.22.0
Release:        33%{?dist}
Summary:        VNC client for GNOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Vinagre
#VCS: git:git://git.gnome.org/vinagre
Source0:        https://download.gnome.org/sources/%{name}/3.22/%{name}-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/vinagre/merge_requests/3
Patch0:         fix-build-with-recent-freerdp-versions.patch

# Let the user cancel the rdp auth dialog instead of looping forever
# https://bugzilla.gnome.org/show_bug.cgi?id=780713
Patch1:         %{name}-rdp-let-cancel-auth-dialog.patch

# https://gitlab.gnome.org/GNOME/vinagre/merge_requests/7
Patch2:         fix-appstream-data.patch
Patch3: vinagre-c99.patch

%if 0%{?with_spice}
BuildRequires:  pkgconfig(spice-client-gtk-3.0)
%endif
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(avahi-ui-gtk3)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-vnc-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  vala-devel
# For Patch0 gnome-autogen.sh
BuildRequires:  gnome-common
BuildRequires:  libappstream-glib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

# for /usr/share/dbus-1/services
Requires: dbus
Requires: telepathy-filesystem

# for file triggers
Requires: glib2 >= 2.45.4-2
Requires: desktop-file-utils >= 0.22-6
Requires: shared-mime-info >= 1.4-7

%description
Vinagre is a VNC client for the GNOME desktop.

With Vinagre you can have several connections open simultaneously, bookmark
your servers thanks to the Favorites support, store the passwords in the
GNOME keyring, and browse the network to look for VNC servers.

Apart from the VNC protocol, vinagre supports Spice and RDP.


%prep
%autosetup -p1

%build
# copied from autogen.sh, needed for Patch0; drop when that is merged
ACLOCAL_FLAGS="$ACLOCAL_FLAGS" USE_GNOME2_MACROS=1 . gnome-autogen.sh
export CFLAGS="%{optflags} -Wno-deprecated-declarations -Wno-format-nonliteral"
%configure \
%if 0%{?with_spice}
           --enable-spice \
%endif
           --enable-rdp \
           --enable-ssh \
           --with-avahi
make V=1 %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%find_lang vinagre --with-gnome


%check
make check

%files -f vinagre.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/vinagre
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/vinagre-mime.xml
%{_datadir}/vinagre/
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vinagre.service
%{_datadir}/telepathy/clients/Vinagre.client
%{_datadir}/glib-2.0/schemas/org.gnome.Vinagre.gschema.xml
%dir %{_datadir}/GConf/
%dir %{_datadir}/GConf/gsettings/
%{_datadir}/GConf/gsettings/org.gnome.Vinagre.convert
%{_mandir}/man1/vinagre.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.22.0-32
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Florian Weimer <fweimer@redhat.com> - 3.22.0-28
- Port to C99 (#2179869)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Simone Caronni <negativo17@gmail.com> - 3.22.0-26
- Rebuild for updated FreeRDP.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 3.22.0-22
- Rebuild for updated FreeRDP.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Simone Caronni <negativo17@gmail.com> - 3.22.0-19
- Rebuild for updated FreeRDP.

* Fri Feb 07 2020 Simone Caronni <negativo17@gmail.com> - 3.22.0-18
- Rebuild for updated FreeRDP.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Felipe Borges <feborges@redhat.com> - 3.22.0-16
- Update appstream data to pass validation

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 3.22.0-14
- Rebuild for FreeRDP update.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Ondrej Holy <oholy@redhat.com> - 3.22.0-12
- Fix build with recent FreeRDP versions

* Mon Oct 15 2018 Simone Caronni <negativo17@gmail.com> - 3.22.0-11
- Rebuild for updated FreeRDP.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.22.0-9
- Simplify spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Karsten Hopp <karsten@redhat.com> - 3.22.0-8
- build with freerdp2

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.22.0-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Simone Caronni <negativo17@gmail.com> - 3.22.0-4
- Build requirement compat-freerdp12 has been renamed to freerdp1.2.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 3.22.0-3
- Tune compile options and use compatibility FreeRDP 1.2 package to fix FTBFS
  in rawhide.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 David King <amigadave@amigadave.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 David King <amigadave@amigadave.com> - 3.21.92-1
- Update to 3.21.92

* Wed Jun 22 2016 Marc-André Lureau <mlureau@redhat.com> - 3.21.3-2
- Rebuild to pick spice-gtk 0.32 ABI break

* Tue Jun 21 2016 David King <amigadave@amigadave.com> - 3.21.3-1
- Update to 3.21.3

* Mon May 09 2016 David King <amigadave@amigadave.com> - 3.20.2-2
- Update to 3.20.2

* Fri Apr 22 2016 Adam Williamson <awilliam@redhat.com> - 3.20.1-2
- rebuild for changed freerdp sonames
- backport patch to handle freerdp pkgconfig module rename

* Mon Apr 11 2016 David King <amigadave@amigadave.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 David King <amigadave@amigadave.com> - 3.20.0-1
- Update to 3.20.0

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.2-2
- Fix AppData (#1308230)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 David King <amigadave@amigadave.com> - 3.19.2-1
- Update to 3.19.2

* Mon Nov 16 2015 David King <amigadave@amigadave.com> - 3.18.2-2
- Rebuild for new freerdp

* Thu Nov 12 2015 David King <amigadave@amigadave.com> - 3.18.2-1
- Update to 3.18.2

* Tue Oct 13 2015 David King <amigadave@amigadave.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 David King <amigadave@amigadave.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 01 2015 David King <amigadave@amigadave.com> - 3.17.91-1
- Update to 3.17.91

* Fri Aug 14 2015 Matthias Clasen <mclasen@redhat.com> - 3.17.2-3
- Rely on file triggers

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2

* Mon May 11 2015 David King <amigadave@amigadave.com> - 3.16.1-1
- Update to 3.16.1

* Sat Apr 18 2015 David King <amigadave@amigadave.com> - 3.16.0-2
- Increase SPICE password limit

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sun Mar 22 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-2
- Rebuilt for freerdp version downgrade

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 David King <amigadave@amigadave.com> - 3.15.91-1
- Update to 3.15.91
- Use license macro for COPYING

* Thu Jan 08 2015 David King <amigadave@amigadave.com> - 3.15.3-3
- Update mimeinfo scriptlet snippet
- Update man page glob in files section

* Sat Dec 20 2014 David King <amigadave@amigadave.com> - 3.15.3-2
- Rebuild for FreeRDP bump

* Mon Dec 15 2014 David King <amigadave@amigadave.com> - 3.15.3-1
- Update to 3.15.3

* Mon Nov 24 2014 David King <amigadave@amigadave.com> - 3.15.2-1
- Update to 3.15.2
- Depend on appstream-util at build time for AppData check

* Mon Nov 10 2014 David King <amigadave@amigadave.com> - 3.14.2-1
- Update to 3.14.2
- Use pkgconfig for BuildRequires
- Call "make check" in check
- Update homepage
- Preserve timestamps during install

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90
- Run update-mime-database scriptlets once per transaction

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1
- Use desktop-file-validate

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Mon Nov 18 2013 Richard Hughes <rhughes@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Thu Sep  5 2013 Matthias Clasen <mclasen@redhat.com> - 3.9.90-2
- Depend on freerdp, thats what is used now

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Tue Apr 23 2013 Mat Booth <fedora@matbooth.co.uk> - 3.8.1-2
- Add explicit dep on rdesktop for RDP functionality (#903225)

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Fri Mar  8 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Wed Sep 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Thu Sep  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.90-2
- Rebuild against new spice

* Wed Aug 22 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Thu Aug 09 2012 Christophe Fergeau <cfergeau@redhat.com> - 3.5.2-3
- Rebuilt against new spice-gtk

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Sun May 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence rpm scriptlet output

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1
- Dropped upstreamed translation patch

* Wed Mar 28 2012 Richard Hughes <rhughes@redhat.com> - 3.4.0-2
- Fix the build by fixing the Russian help translation.

* Tue Mar 27 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Fri Mar  9 2012 Ville Skyttä <ville.skytta@iki.fi> - 3.3.4-3
- Own %%{_datadir}/telepathy and %%{_datadir}/GConf dirs (#681636).

* Mon Feb 13 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-2
- Update the description to mention RDP and Spice

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Thu Nov 24 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.3.2-2
- Fix the spice plugin

* Tue Nov 22 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Wed Aug 31 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90-1
- Update to 3.1.90
- Make the dbus dep archful

* Thu Aug 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.5-1
- Update to 3.1.5

* Wed Aug 03 2011 Adam Williamson <awilliam@redhat.com> - 3.1.4-2
- rebuild against updated spice

* Mon Jul 25 2011 Matthew Barnes <mbarnes@redhat.com> 3.1.4-1
- Update to 3.1.4

* Tue Jul 05 2011 Bastien Nocera <bnocera@redhat.com> 3.1.3-1
- Update to 3.1.3

* Mon Jun 20 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-3
- Fix vala sources compilation

* Wed Jun 15 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-2
- Fix the main notebook widget expansion

* Tue Jun 14 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-1
- Update to 3.1.2
- Removed -devel package

* Wed May 11 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 3.0.1-3
- Update scriptlets

* Thu Apr 28 2011 Dan Horák <dan[at]danny.cz> - 3.0.1-2
- spice available only on x86

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Tue Apr  5 2011 Christopher Aillon <caillon@redhat.com> - 3.0.0-2
- Kill off the remnants of GConf, this uses GSettings now.
- Bring back ssh support (by building against vte3 instead of vte)

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Fri Mar 25 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.93-1
- Update to 2.91.93

* Mon Mar 21 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91-2
- Fix build

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Tue Mar  1 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.8-2
- Update to 2.91.8
- Build the spice plugin

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.7-1
- Update to 2.91.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> 2.31.4-2
- Disable the applet
- Build against gtk3

* Wed Jun 30 2010 Matthias Clasen <mclasen@redhat.com> 2.31.4-1
- Update to 2.31.4

* Sat Jun 19 2010 Matthias Clasen <mclasen@redhat.com> 2.30.1-2
- Reduce overlinking

* Thu May 27 2010 Matthias Clasen <mclasen@redhat.com> 2.30.1-1
- Update to 2.30.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> 2.30.0-1
- Update to 2.30.0
- Modernize the icon cache handling

* Tue Mar  9 2010 Tomas Bzatek <tbzatek@redhat.com> 2.29.92-1
- Update to 2.29.92

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> 2.29.91-1
- Update to 2.29.91

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Tue Jan 26 2010 Matthias Clasen <mclasen@redhat.com> 2.29.6-1
- Update to 2.29.6

* Mon Jan  4 2010 Matthias Clasen <mclasen@redhat.com> 2.29.1-2
- Don't crash when the history file is empty (#552076)

* Fri Dec  4 2009 Matthias Clasen <mclasen@redhat.com> 2.29.1-1
- 2.29.1

* Mon Oct 19 2009 Matthias Clasen <mclasen@redhat.com> 2.28.1-1
- Update to 2.28.1

* Wed Sep 23 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0.1-1
- Update to 2.28.0.1

* Fri Sep 18 2009 Bastien Nocera <bnocera@redhat.com> 2.27.92-3
- Update mDNS patch

* Fri Sep 18 2009 Bastien Nocera <bnocera@redhat.com> 2.27.92-2
- Fix mDNS bookmarks activation

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Sat Sep  5 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-3
- Fix warnings at startup (#521382)

* Thu Sep  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-2
- Make ids unique

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Tue Aug 11 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- 2.27.90

* Tue Aug 04 2009 Bastien Nocera <bnocera@redhat.com> 2.27.5-2
- Fix pkg-config requires

* Tue Jul 28 2009 Matthisa Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5
- Split off a -devel package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/vinagre/2.26/vinagre-2.26.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Fri Jan 23 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Tue Jan  6 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.4-1
- Update to 2.25.4

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.3-1
- Update to 2.25.3

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-2
- Better URL
- Tweak %%description

* Mon Oct 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Thu Oct  9 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-2
- Save some space

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Wed Jun 25 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.4-2
- Rebuild

* Tue Jun 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.4-1
- Update to 2.23.4
- Fix URL (#451746)

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.3.1-1
- Update to 2.23.3.1

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 0.5.1-1
- Update to 0.5.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.92-1
- Update to 0.4.92

* Mon Feb 18 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.91-2
- Spec file fixes

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.91-1
- Update to 0.4.91

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.90-1
- Update to 0.4.90

* Thu Dec 13 2007 - Bastien Nocera <bnocera@redhat.com> - 0.4-1
- Update to 0.4 and drop obsolete patches

* Fri Nov 23 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3-3
- Fix crasher when passing broken options on the command-line (#394671)

* Thu Oct 25 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3-2
- Fix crasher when setting a favourite with no password (#352371)

* Mon Sep 24 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3-1
- Update to 0.3

* Wed Aug 22 2007 - Bastien Nocera <bnocera@redhat.com> - 0.2-1
- First version
- Fix plenty of comments from Ray Strode as per review
- Have work-around for BZ #253734

