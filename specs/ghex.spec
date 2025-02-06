%global tarball_version %%(echo %{version} | tr '~' '.')

%global __provides_exclude_from ^%{_libdir}/gtkhex-4.0/.*\\.so$

Name:           ghex
Version:        46.1
Release:        2%{?dist}
Summary:        Binary editor for GNOME

# Source code is under GPLv2+, help is under GFDL and icon is under CC-BY-SA.
License:        GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/GNOME/ghex
Source0:        https://download.gnome.org/sources/ghex/46/ghex-%{tarball_version}.tar.xz

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  /usr/bin/g-ir-scanner

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
GHex can load raw data from binary files and display them for editing in the
traditional hex editor view. The display is split in two columns, with
hexadecimal values in one column and the ASCII representation in the other.
A useful tool for working with raw data.


%package        libs
Summary:        GtkHex library

%description    libs
The %{name}-libs package contains the shared GtkHex library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GHex.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.GHex.appdata.xml


%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc NEWS README.md
%{_bindir}/ghex
%{_datadir}/applications/org.gnome.GHex.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.gnome.GHex.appdata.xml

%files libs
%license COPYING
%{_libdir}/libgtkhex-4.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Hex-4.typelib
%{_libdir}/gtkhex-4.0/

%files devel
%{_includedir}/gtkhex-4/
%{_libdir}/libgtkhex-4.so
%{_libdir}/pkgconfig/gtkhex-4.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Hex-4.gir


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Nieves Montero <nmontero@redhat.com> - 46.1-1
- Update to 46.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 22 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 David King <amigadave@amigadave.com> - 46~alpha-1
- Update to 46.alpha

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 Kalev Lember <klember@redhat.com> - 45.1-1
- Update to 45.1

* Sat Oct 21 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Wed Aug 23 2023 Kalev Lember <klember@redhat.com> - 45~beta-1
- Update to 45.beta

* Thu Aug 17 2023 Kalev Lember <klember@redhat.com> - 44.2-1
- Update to 44.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 28 2023 David King <amigadave@amigadave.com> - 44.1-1
- Update to 44.1

* Mon Mar 27 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Mon Feb 06 2023 David King <amigadave@amigadave.com> - 44.alpha-1
- Update to 44.alpha

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 07 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0
- Fix gir directory ownership

* Wed Sep 21 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 43~alpha-1
- Update to 43.alpha

* Tue Jun 14 2022 David King <amigadave@amigadave.com> - 42.3-1
- Update to 42.3

* Wed Apr 27 2022 David King <amigadave@amigadave.com> - 42.2-1
- Update to 42.2

* Sat Apr 16 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1

* Tue Apr 05 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4~beta.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 David King <amigadave@amigadave.com> - 4~beta.1-1
- Update to 4.beta.1

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 3.41.1-1
- Update to 3.41.1

* Sat Sep 25 2021 Kalev Lember <klember@redhat.com> - 3.41.0-1
- Update to 3.41.0

* Fri Sep 17 2021 Gustavo Costa <xfgusta@fedoraproject.com> - 3.41~rc-2
- Use _metainfodir macro
- Add appdata check

* Thu Sep 09 2021 Kalev Lember <klember@redhat.com> - 3.41~rc-1
- Update to 3.41.rc

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 3.41~beta-1
- Update to 3.41.beta

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Kalev Lember <klember@redhat.com> - 3.18.4-1
- Update to 3.18.4
- Switch to the meson build system

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.18.3-7
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.18.3-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.18.3-1
- Update to 3.18.3
- Don't set group tags
- Don't manually require ldconfig

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Wed May 11 2016 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 02 2016 Adel Gadllah <adel.gadllah@gmail.com> - 3.18.0-2
- Use %%global instead of %%define

* Wed Sep 23 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91
- Include new symbolic icons
- Use make_install macro
- Mark license files with the license macro
- Tighten -devel package deps with the _isa macro
- Split out the shared library to -libs subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.10.1-4
- Use better AppData screenshots

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Kalev Lember <kalevlember@gmail.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Tue Feb 05 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3
- Add icon cache scriptlets for HighContrast icons

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1
- Adjust buildrequires for the new documentation infrastructure

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Thu Aug 30 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Tue May 15 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-2
- Use %%find_lang for help files

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Mon Mar 26 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0
- Include HACKING in docs

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.91-1
- Update to 3.3.91
- Dropped manual gtk3-devel dependency from ghex-devel subpackage; it's
  automatically picked up by rpm pkgconfig depgen.

* Tue Feb 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.90-1
- Update to 3.3.90

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Sat Sep 10 2011 Kalev Lember <kalevlember@gmail.com> - 2.90.2-1
- Update to 2.90.2
- Switch to gsettings
- Updated description
- Don't require scrollkeeper
- Make sure files aren't listed twice in %%files
- Added icon cache scriplets

* Sat Aug 13 2011 Adel Gadllah <adel.gadllah@gmail.com> - 2.90.0-1
- Update to 2.90.0 - now uses GTK3
- Remove now obsolete patch

* Tue Feb 09 2010 Dodji Seketeli <dodji@redhat.com> - 2.24.0-5
- Add patch to fix building with --no-as-needed as linker option.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Dodji Seketeli <dodji@redhat.org> 2.24.0-2
- Use %%{?dist} in the Release number

* Fri Feb 20 2009 Dodji Seketeli <dodji@redhat.org> 2.24.0-1
- Update to 2.24.0
- Use system libtool
- Explicitely exclude static libraries
- Added BuildRequires intltools,libtool

* Fri Apr 11 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.22.0-1
- Update to 2.22.0 (no code changes, just a late release for Gnome 2.22 with
  updated translations)

* Sun Mar 02 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.21.92-1
- Update to 2.21.92

* Fri Feb 08 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.21.90-1
- Update to 2.21.90

* Sat Dec 29 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.21.4-1
- Update to 2.21.4
- Pass --disable-static to configure
- remove obsolete rm -rf RPM_BUILD_ROOT/var/scrollkeeper from install section

* Fri Dec 14 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.20.1-1
- Update to 2.20.1

* Fri Sep 21 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.20.0-1
- Update to 2.20.0

* Fri Aug 31 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.19.91-1
- Update to 2.19.91

* Fri Aug 17 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.19.90-1
- Update to 2.19.90

* Thu Aug 09 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.19.0-1
- Update to 2.19.0 and drop patches (stuff got fixed upstream)
- use make isntall instread of %%makeinstall

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Sun May 20 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.8.2-5
- Update project URL (#240646)

* Tue Aug 29 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.8.2-4
- Add BR perl-XML-Parser

* Tue Aug 29 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.8.2-3
- Rebuild for devel

* Wed Aug 09 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 2.8.2-2
- apply ghex-search-crash.patch from b.g.o #339055 -- fixes #175957 

* Sat Jul 15 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 2.8.2-1
- Update to 2.8.2
- Don't use the libtool worksaroung anymore
- Rename ghex-2.8.0-no-scrollkeeper.patch to
  ghex-no-scrollkeeper.patch and and update it

* Mon Feb 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info>
- Rebuild for Fedora Extras 5

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Jan 09 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.8.1-2
- Use make param LIBTOOL=/usr/bin/libtool instead autoreconf -- fixes x86_64
  build

* Mon Dec 27 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.8.1-1
- Update to 2.8.1
- recreate autoconf & co data during pre; fixes build issues on x86_64

* Tue Dec 21 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.8.0-3
- Ran into the incomplete-removal-of-epoch trap. Fixed that.

* Wed Nov 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.8.0-2
- Add patch to prevent scrollkeeper-updates during %%install.
- Drop Epoch.

* Sun Oct 17 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.8.0-0.fdr.1
- Updated to 2.8.0.

* Fri Jun  4 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.6.1-0.fdr.1
- Updated to 2.6.1.
- Reenabled parallel make (fixed upstream).

* Mon May 17 2004 Mark A. Fonnemann <m.fonneman.n@bc.edu> - 0:2.6.0-0.fdr.1
- Updated to 2.6.0.
- Divided Requires(post, postun) into Requires(post) and Requires(postun) (thanks, Michael Schwendt).
- Added gtk2-devel and gail-devel to build requirements (thanks, Michael).
- Changed {_datadir}/path to {_datadir}/path/* (thanks again, Michael).

* Thu Oct 23 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.4.0.1-0.fdr.4
- Reverted previous change.
- Disabled parallell make.
- Added build req scrollkeeper.

* Sat Oct 11 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.4.0.1-0.fdr.3
- Remove sr@Latn locale from desktop file if old desktop-file-install.

* Thu Oct  9 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.4.0.1-0.fdr.2
- Post req GConf2.
- Split out devel package.
- Added URL.

* Wed Sep 24 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.4.0.1-0.fdr.1
- Initial RPM release.
