Name: eiciel
Version: 0.10.1
%global tar_version %{version}

Release: 3%{?dist}
Summary: Graphical editor for ACLs and xattr
License: GPL-2.0-or-later
URL: http://rofi.roger-ferrer.org/eiciel
Source0: http://rofi.roger-ferrer.org/eiciel/files/eiciel-%{tar_version}.tar.xz

Patch0: eiciel-0.10.1-rawhide-gcc.patch

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: pkgconfig(gtkmm-4.0)
BuildRequires: pkgconfig(libnautilus-extension-4)
BuildRequires: libacl-devel
BuildRequires: itstool
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme

%global ext_dir %(eval "pkg-config --variable=extensiondir libnautilus-extension-4")

# don't "provide" a private shlib
%global __provides_exclude_from ^%{ext_dir}/.*\\.so$


%description
Graphical editor for access control lists (ACLs) and extended attributes
(xattr), either as an extension within Nautilus, or as a standalone
utility.


%prep
%autosetup -p1 -n %{name}-%{tar_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/help/C/%{name}/
%{_datadir}/applications/*.desktop
%{ext_dir}/lib%{name}*.so
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*%{name}.*
%{_mandir}/man1/%{name}.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 30 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 0.10.1-2
- Failed to built for Rawhide.

* Mon Aug 26 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1.

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.10.0-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Michael Schwendt <mschwendt@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0 final (no code changes but added manual page).

* Sat Sep 17 2022 Michael Schwendt <mschwendt@fedoraproject.org> - 0.10.0-0.2.rc2
- Update to 0.10.0-rc2.

* Fri Sep  9 2022 Michael Schwendt <mschwendt@fedoraproject.org> - 0.10.0-0.1.rc1
- Upgrade to 0.10.0-rc1 for Nautilus 4.
- Major spec overhaul for Meson usage and updated BuildRequires.

* Fri Aug 26 2022 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.13.1-4
- Disable Nautilus extension for rawhide/f37   #rhbz2113186

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep  1 2021 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.13.1-1
- Update to 0.9.13.1 (makes patch unnecessary + autotools updates).

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 29 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.13-1
- Update to 0.9.13 (adds recursive changing of permissions).

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 0.9.12.1-10
- No longer force C++11 mode

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 26 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.12.1-8
- Avoid C++ name mangling for Nautilus extension symbols. (#1807260)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.12.1-4
- <xattr/attr.h> is deprecated, use <sys/attr.h> instead

* Tue Jul 17 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.12.1-3
- add BuildRequires libattr-devel
- add BuildRequires gcc-c++
- use %%license macro

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.12.1-1
- Update to 0.9.12.1 to get a desktop file that validates.

* Tue Jan 16 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12 for better integration with AppStream.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.11-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.11-2
- Prefer %%global over %%define. No build just for that, though.

* Fri Dec 18 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.11-1
- Update to 0.9.11 (new translations for 13 languages).
- Compile with -std=c++11 as needed for glibmm24 and libsigc++20.
- BR gcc-c++

* Mon Aug 31 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10 (fix for GTK+ >= 3.14).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.9-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Aug 20 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Richard Hughes <richard@hughsie.com> - 0.9.8.3-1
- Update to 0.9.8.3.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 29 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.8.2-1
- Update to 0.9.8.2.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.8.1-9
- Add patch for newer config.guess/config.sub files for aarch64 (#925300).
- Drop the LDFLAGS patch again.
- Fix ChangeLog guard.

* Mon Feb 25 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.8.1-8
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- drop obsolete user groups patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 11 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.8.1-5
- Patch open_file() file not found crash (#811460).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.8.1-3
- General cleanup of spec file and remove obsolete items.
- Insert %%prep guard to check whether ChangeLog file gets replaced.
- Fix desktop file issues.

* Sat Nov  5 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.8.1-2
- Move LDFLAGS before libs and link with --as-needed.

* Sun Jul 31 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.8.1-1
- Update to 0.9.8.1 to fix GTK2 vs. GTK3 crash (#726950)
  and Nautilus freeze (#703924).
- BR gtkmm30-devel instead of gtkmm24-devel.
- Apply user/group bounds patch only for Fedora <= 15, because Fedora 16
  will start at 1000.

* Wed Apr 27 2011 Chris Weyl <cweyl@alumni.drew.edu> 0.9.8-1
- update to 0.9.8
- filter out our private plugin shlib from rpm metadata provides

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 0.9.6.1-5
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 24 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.9.6.1-1
- update to 0.9.6.1
- patch system user/group bounds; primitive but works :)  Should resolve
  RH#445667.
- oh, and the nautlius extensions dir seems to have changed.  Let's use what
  libnautilus-extensions.pc says is the right directory, instead of
  hardcoding it.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.5-2
- Autorebuild for GCC 4.3

* Thu Oct 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.9.5-1
- update to 0.9.5

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.9.4-2
- bump

* Sun Nov 12 2006 Chris Weyl <cweyl@alumni.drew.edu>
- update to 0.9.4
- src/eiciel.desktop and doc/C/eiciel.xml no longer in source tarball 

* Sun Nov 12 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.9.3-1
- update to 0.9.3
- nuke src/eiciel.desktop during prep, drop the patch and just let configure
  do its thing

* Sat Nov 11 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.9.2-8
- bump

* Sat Nov 11 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.9.2-7
- rm doc/C/eiciel.xml during prep; otherwise it isn't rebuilt properly

* Wed Nov 08 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.9.2-6
- minor tweaks, resubmitted

* Sun Jul 09 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9.2-5
- Drop excludes for .debug files
- Tidy up summary and description
- Make includes more precise
- Use .desktop file now accepted upstream (but with patch)
- Use existing .png file as icon instead of copy

* Mon Jul 03 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9.2-4
- Change .debug excludes to work on x86_64 too

* Mon Jul 03 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9.2-3
- Exclude *.debug files
- Remove macros from changelog section to shut up rpmlint
- Reduced file permissions on .spec and .desktop files

* Mon Jul 03 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9.2-2
- Claim files under libdir more precisely
- Add nautilus to buildreqs

* Mon Jul 03 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9.2-1
- Update source to 0.9.2
- Drop gcc4.1 patch accepted upstream

* Sat Feb 04 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-8
- Use __mkdir and __install macros

* Fri Feb 03 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-7
- Make version key in .desktop refer to fd.o spec ver, not eicel ver
- Actually install the .destop file
- Provide icon for .desktop file in /usr/share/pixmaps
- Replace all RPM_BUILD_ROOT macros with buildroot

* Fri Feb 03 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-6
- All docs are in doc
- All Requires were detected automatically
- Omit .la as well as .a
- Reset file permissions on source files
- Use find_lang for locale files
- Added .desktop file
- Change instances of eiciel to name macro

* Fri Feb 03 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-5
- Exclude .a library which is unlikely to be used
- Use more fine-grained file specs, particularly for man/doc files

* Thu Feb 02 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-4
- Attempt to fix rpmlint ownership warnings about man1 files/dirs

* Thu Feb 02 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-3
- Changed BuildRequires/Requires

* Thu Feb 02 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-2
- Added patch for gcc4.1

* Thu Feb 02 2006 Andy Burns <fedora@adslpipe.co.uk> 0.9-1
- Initial RPM build

