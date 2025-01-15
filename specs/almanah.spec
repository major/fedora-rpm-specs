Name:		almanah
Version:	0.12.4
Release:	1%{?dist}
Summary:	Application for keeping an encrypted diary

License:	GPL-3.0-or-later
URL:		https://wiki.gnome.org/Apps/Almanah_Diary
Source0:	https://download.gnome.org/sources/almanah/0.12/almanah-%{version}.tar.xz

BuildRequires:	appstream
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	gpgme-devel
BuildRequires:	desktop-file-utils
BuildRequires:	meson
BuildRequires:	pkgconfig(cryptui-0.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gcr-4)
BuildRequires:	pkgconfig(gtkspell3-3.0)
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(libecal-2.0) >= 3.45.1
BuildRequires:	pkgconfig(libedataserver-1.2) >= 3.45.1
BuildRequires:	pkgconfig(sqlite3)

%description
Almanah Diary is a small application to ease the management of an encrypted
personal diary. It's got good editing abilities, including text formatting
and printing. Evolution tasks and appointments will be listed to ease the
creation of diary entries related to them. At the same time, you can create
diary entries using multiple events.

%prep
%autosetup -p1 -S gendiff

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/org.gnome.Almanah.png
%{_datadir}/icons/hicolor/scalable/actions/org.gnome.Almanah-tags-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Almanah-symbolic.svg
%{_datadir}/applications/org.gnome.Almanah.desktop
%{_datadir}/metainfo/org.gnome.Almanah.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml

%changelog
* Mon Jan 13 2025 Milan Crha <mcrha@redhat.com> - 0.12.4-1
- Update to 0.12.4

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Milan Crha <mcrha@redhat.com> - 0.12.3-9
- Rebuilt for evolution-data-server soname bump

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Kalev Lember <klember@redhat.com> - 0.12.3-7
- Rebuilt for gcr soname bump

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 0.12.3-4
- Rebuilt for evolution-data-server soname bump
- Add patch to build with gcr4
- Add patch to build with meson 0.61

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 08 2021 Milan Crha <mcrha@redhat.com> - 0.12.3-1
- Update to 0.12.3

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 0.12.0-7
- Rebuilt for evolution-data-server soname bump

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 0.12.0-3
- Rebuilt for evolution-data-server soname bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 0.12.0-1
- Update to 0.12.0
- Switch to the meson build system
- Remove obsolete GConf schemas scriptlet
- Update source URLs
- Use license macro for COPYING

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 0.11.1-25
- Add patch to build against newer evolution-data-server (libecal-2.0)

* Fri May 03 2019 Milan Crha <mcrha@redhat.com> - 0.11.1-24
- Add patch for RH bug #1705678 (Remove Evolution runtime dependency)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Milan Crha <mcrha@redhat.com> - 0.11.1-22
- Rebuilt for evolution-data-server soname bump

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 0.11.1-20
- Rebuilt for evolution-data-server soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.1-18
- Remove obsolete scriptlets

* Wed Nov 08 2017 Milan Crha <mcrha@redhat.com> - 0.11.1-17
- Rebuild for newer libical

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.11.1-13
- Rebuild for gpgme 1.18

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 0.11.1-12
- Rebuild for newer evolution-data-server

* Wed Jun 22 2016 Milan Crha <mcrha@redhat.com> - 0.11.1-11
- Do not require evolution, when using evolution-data-server libraries

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 0.11.1-10
- Rebuild for newer evolution-data-server

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.11.1-9
- rebuild for ICU 57.1

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 0.11.1-8
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 0.11.1-6
- rebuild for libical 2.0.0

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 0.11.1-5
- Rebuild for newer evolution-data-server

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 0.11.1-3
- Rebuild for newer evolution-data-server

* Mon Feb 23 2015 Milan Crha <mcrha@redhat.com> - 0.11.1-2
- Rebuild against newer evolution-data-server

* Thu Jan 29 2015 Jaromir Capik <jcapik@redhat.com> - 0.11.1-1
- Update to 0.11.1 (#1180423)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Milan Crha <mcrha@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Bruno Wolff III <bruno@wolff.to> - 0.10.0-4
- Rebuild for a couple of soname bumps

* Tue Nov 20 2012 Milan Crha <mcrha@redhat.com> - 0.10.0-3
- Rebuild against newer evolution-data-server

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 0.10.0-2
- Rebuild against newer evolution-data-server

* Tue Oct 16 2012 Milan Crha <mcrha@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Milan Crha <mcrha@redhat.com> - 0.8.0-7
- Rebuild against newer evolution-data-server

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Milan Crha <mcrha@redhat.com> - 0.8.0-5
- Rebuild against newer evolution-data-server

* Sun Oct 30 2011 Bruno Wolff III <bruno@wolff.to> - 0.8.0-4
- Rebuild against newer evolution-data-server

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 0.8.0-3
- Rebuild against newer evolution-data-server

* Tue Aug 16 2011 Milan Crha <mcrha@redhat.com> - 0.8.0-2
- Rebuild against newer evolution-data-server

* Fri Aug  5 2011 Tom Callaway <spot@fedoraproject.org> - 0.8.0-1
- update to 0.8.0

* Thu Jun 16 2011 Milan Crha <mcrha@redhat.com> - 0.7.3-12
- Rebuild against newer evolution-data-server

* Fri May 20 2011 Kalev Lember <kalev@smartlink.ee> - 0.7.3-11
- Rebuilt for libcamel soname bump

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 0.7.3-10
- Rebuild against newer gtk

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Tom Callaway <spot@fedoraproject.org> - 0.7.3-8
- port to gtk3, disable spellchecking because gtkspell is still GTK2
 
* Fri Feb  4 2011 Tom Callaway <spot@fedoraproject.org> - 0.7.3-7
- rebuild again to fix broken deps, support new libedataserverui

* Wed Jan 12 2011 Milan Crha <mcrha@redhat.com> - 0.7.3-6
- Rebuild against newer evolution-data-server

* Tue Oct 12 2010 Milan Crha <mcrha@redhat.com> - 0.7.3-5
- Rebuild against newer evolution-data-server

* Mon Oct  4 2010 Bill Nottingham <notting@redhat.com> - 0.7.3-4
- Release bump and build to fix libedataserver broken dep

* Sat Jun 26 2010 Caolán McNamara <caolanm@redhat.com> - 0.7.3-3
- Release bump and build to fix libedataserver broken dep

* Fri Jun 11 2010 Mike McGrath <mmcgrath@redhat.com> - 0.7.3-2
- Release bump and build to fix libedataserver broken dep

* Sat May 22 2010 Andreas Osowski <th0br0@mkdir.name> - 0.7.3-1
- Update to 0.7.3
- Improved the UI appearance a little by adding some padding
- Updated translations

* Sun Feb  7 2010 Andreas Osowski <th0br0@mkdir.name> - 0.7.2-1
- Update to 0.7.2

* Tue Dec  8 2009 Andreas Osowski <th0br0@mkdir.name> - 0.6.1-3
- Added patch required for F-11 (link against dbus-glib)

* Tue Dec  8 2009 Andreas Osowski <th0br0@mkdir.name> - 0.6.1-2
- Cosmetic changes

* Fri Nov 27 2009 Andreas Osowski <th0br0@mkdir.name> - 0.6.1-1
- Update to new release
- Fixed BuildRequires for new release

* Wed Dec  3 2008 Jean-François Martin <lokthare@gmail.com> - 0.5.0-1
- Update to the new release

* Mon Jul 14 2008 Jean-François Martin <lokthare@gmail.com> - 0.4.0-2
- Fix rpmlint warnings
- Include ChangeLog
- Fix icon name in desktop file
 
* Sat Jul 12 2008 Jean-François Martin <lokthare@gmail.com> - 0.4.0-1 
- Change to the new name
- Remove GConf scriplets

* Mon Jun 23 2008 Jean-François Martin <lokthare@gmail.com> 0.3.1-1
- Update to the new release
- Drop the patch (fixed upstream)

* Fri Jun 20 2008 Jean-François Martin <lokthare@gmail.com> 0.3-1
- Update to the new release

* Wed May 21 2008 Jean-François Martin <lokthare@gmail.com> 0.2-1
- First RPM release.

