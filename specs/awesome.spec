Name:		awesome
Version:	4.3
Release:	20%{?dist}
Summary:	Highly configurable, framework window manager for X. Fast, light and extensible
# common/buffer.[ch]: BSD
# Automatically converted from old format: GPLv2+ and BSD - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:		https://awesomewm.org
Source0:	https://github.com/awesomeWM/awesome-releases/raw/master/%{name}-%{version}.tar.xz
Patch0:		awesome-4.0-use-vi-instead-of-nano.patch

BuildRequires:	cmake >= 3.0.0
BuildRequires:	lua-devel >= 5.1
BuildRequires:	gcc
BuildRequires:	make

BuildRequires:	ImageMagick
BuildRequires:	asciidoctor
BuildRequires:	xmlto
BuildRequires:	gzip

BuildRequires:	lua-ldoc

BuildRequires:	pkgconfig(xcb) >= 1.6
BuildRequires:	pkgconfig(glib-2.0) >= 2.40
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xcb-xtest)
BuildRequires:	pkgconfig(xcb-xinerama)
BuildRequires:	pkgconfig(xcb-shape)
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:	pkgconfig(xcb-icccm) >= 0.3.8
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(cairo-xcb)
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires:	pkgconfig(xproto) >= 7.0.15
BuildRequires:	pkgconfig(libxdg-basedir) >= 1.0.0
BuildRequires:	pkgconfig(xcb-xrm) >= 1.0
BuildRequires:	pkgconfig(dbus-1)

BuildRequires:	lua-lgi >= 0.8.0
Requires:	lua-lgi >= 0.8.0
# next two loaded via lgi
Requires:	pango%{?_isa} >= 1.19.3
Requires:	cairo-gobject%{?_isa}

BuildRequires:	desktop-file-utils
Requires:	startup-notification >= 0.10
# terminal used in the default configuration
Requires:	xterm
# optional but useful
Requires:	rlwrap
# default editor
Recommends:	vi


%description
Awesome is a highly configurable, next generation framework window
manager for X. It is very fast, light and extensible.

It is primary targeted at power users, developers and any people
dealing with every day computing tasks and want to have fine-grained
control on its graphical environment.


%package	doc
Summary:	API doc files
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	doc
API doc files for awesome generated by luadoc.

# short-term fix for FTBFS with GCC10
%define _legacy_common_support 1


%prep
%setup -q
%patch -P0 -p1 -b .use-vi-instead-of-nano

# fix shebang
sed -i -e '1 s,^#!.*,#!%{_bindir}/bash,' utils/awesome-client


%build
%cmake -DAWESOME_DOC_PATH=%{_pkgdocdir} \
       -DSYSCONFDIR=%{_sysconfdir}
%cmake_build


%install
%cmake_install

# verify desktop file
desktop-file-validate %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%files
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/*
%exclude %{_pkgdocdir}/LICENSE
%license LICENSE
%exclude %{_pkgdocdir}/doc
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/rc.lua
%{_bindir}/awesome
%{_bindir}/awesome-client
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_mandir}/*/man1/*
%{_mandir}/*/man5/*
%{_datadir}/xsessions/%{name}.desktop


%files doc
# -doc requires the main package, which provides the _pkdocdir
%doc %{_pkgdocdir}/doc


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb  6 2021 Xaver Hellauer <xaver.hellauer@gmail.com> – 4.3-9
- vi as weak dependency

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.3-7
- Update for https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb  6 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.3-4
- Workaround for FTBFS with GCC10.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb  7 2019 Thomas Moschny <thomas.moschny@gmx.de> - 4.3-1
- Update to 4.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Thomas Moschny <thomas.moschny@gmx.de> - 4.2-3
- Add BRs on make and gcc.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug  2 2017 Thomas Moschny <thomas.moschny@gmx.de> - 4.2-1
- Update to 4.2.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Thomas Moschny <thomas.moschny@gmx.de> - 4.1-1
- Update to 4.1.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Thomas Moschny <thomas.moschny@gmx.de> - 4.0-1
- Update to 4.0
- Update URLs.
- Update BR list.

* Mon Mar  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.9-1
- Update to 3.5.9.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.8-1
- Update to 3.5.8.

* Mon Jan 18 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.7-1
- Update to 3.5.7.
- Mark LICENSE with %%license.
- Remove unneeded definition of %%_pkgdocdir.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 3.5.6-2
- rebuild for lua 5.3
- trick cmake into finding lua 5.3

* Wed Jan 14 2015 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.6-1
- Update to 3.5.6.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.5-1
- Update to 3.5.5.

* Wed Apr  2 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.4-1
- Update to 3.5.4.

* Wed Apr  2 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.3-1
- Update to 3.5.3.
- Remove dependency on libev, and a related patch.
- Remove dependency on xcb-image.
- Add dependency on xcb-cursor.
- Simplify cmake invocation.

* Sun Aug 18 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.1-8
- Define (if undefined) and use _pkgdocdir macro (rhbz#993678).
- Fix bogus dates in the %%changelog.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.1-6
- Add vi as explicit requirement.
- Add requirement on cairo-gobject, should fix rhbz#959169.

* Sat May 25 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.1-5
- Remove obsolete BR on gperf.

* Mon May 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.1-4
- Set default editor to vi
- Resolves: rhbz#964945

* Mon May 13 2013 Tom Callaway <spot@fedoraproject.org> - 3.5.1-3
- rebuild for lua 5.2

* Thu Apr  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.1-2
- The Lua GObject introspection package is needed at runtime.

* Wed Apr  3 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.1-1
- Update to 3.5.1.
- Rework BR section:
  - Replace imlib2 with gdk-pixbuf-2.0.
  - Replace luadoc with lua-ldoc.
  - Add lua-lgi.

* Sat Mar 16 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.15-1
- Update to 3.4.15.
- Add patch from upstream to fix rhbz#901434.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.14-1
- Update to 3.4.14.
- Update buildrequires.

* Tue Aug 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.13-2
- Rebuilt for libxcb-util soname bump

* Wed Jul 18 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.13-1
- Update to 3.4.13.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.12-1
- Update to 3.4.12.
- Remove patches applied upstream.

* Wed May 30 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.11-5
- Update License tag.
- Fix permissions of generated HTML docs.
- Patch and validate the .desktop file.

* Thu May 24 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.11-4
- Specfile cleanups.

* Fri Apr  6 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.11-3
- Rebuilt.

* Wed Dec 14 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.11-2
- Add patch to build against glib2 2.31.0 and later.

* Mon Dec  5 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.11-1
- Update to 3.4.11, add patch for older Fedora releases.
- Add dependencies on xterm and rlwrap.
- Rework BR section.

* Tue Sep 27 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.10-3
- Remove dependency on xsri.

* Mon Sep 26 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.10-2
- Rebuilt for newer cairo rpm.

* Sun May 22 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.4.10-1
- Update to 3.4.10.
- Add dependencies to ease installation.

* Mon Jan 17 2011 Michal Nowak <mnowak@redhat.com> 3.4.9-1
- 3.4.9
- require cmake >= 2.8.0

* Mon Oct 18 2010 Michal Nowak <mnowak@redhat.com> 3.4.8-1
- 3.4.8

* Thu Aug 26 2010 Michal Nowak <mnowak@redhat.com> 3.4.7-1
- 3.4.7

* Fri Jul 23 2010 Michal Nowak <mnowak@redhat.com> 3.4.6-1
- 3.4.6

* Mon May 17 2010 Michal Nowak <mnowak@redhat.com> 3.4.5-1
- 3.4.5
- we ship non-English man pages with this release

* Thu Mar  4 2010 Michal Nowak <mnowak@redhat.com> 3.4.4-1
- 3.4.4

* Mon Jan  4 2010 Michal Nowak <mnowak@redhat.com> 3.4.3-1
- 3.4.3
- .in files are finally not installed anymore

* Wed Dec  2 2009 Michal Nowak <mnowak@redhat.com> 3.4.2-1
- 3.4.2
- use xz instead of bz2

* Sun Nov 22 2009 Michal Nowak <mnowak@redhat.com> 3.4.1-1
- 3.4.1

* Thu Oct 22 2009 Michal Nowak <mnowak@redhat.com> 3.4-1
- 3.4

* Mon Oct 12 2009 Michal Nowak <mnowak@redhat.com> 3.4-0.3.rc3
- 3.4~rc3

* Tue Oct  6 2009 Michal Nowak <mnowak@redhat.com> 3.4-0.2.rc2
- remove .in files in build root rather in source dir

* Mon Oct  5 2009 Michal Nowak <mnowak@redhat.com> 3.4-0.1.rc2
- 3.4-rc2

* Fri Sep 18 2009 Jens Petersen <petersen@redhat.com> - 3.3.4-3
- integrate rctag macro
- simplify removal of .in files and filelist

* Wed Sep 16 2009 Michal Nowak <mnowak@redhat.com> 3.3.4-2
- libxdg-basedir-devel as BR

* Wed Sep 16 2009 Michal Nowak <mnowak@redhat.com> 3.3.4-1
- 3.3.4
- BuildRequire: ImageMagick, libxdg-basedir

* Sat Aug 29 2009 Michal Nowak <mnowak@redhat.com> 3.3.3-1
- 3.3.3

* Sat Aug  1 2009 Michal Nowak <mnowak@redhat.com> 3.3.2-1
- 3.3.2

* Mon Jun 22 2009 Michal Nowak <mnowak@redhat.com> 3.3.1-1
- 3.3.1

* Fri Jun 12 2009 Michal Nowak <mnowak@redhat.com> 3.3-1
- 3.3

* Thu May 28 2009 Michal Nowak <mnowak@redhat.com> 3.3-0.4.rc4
- 3.3-rc4

* Tue May 19 2009 Michal Nowak <mnowak@redhat.com> 3.3-0.3.rc3
- 3.3-rc3

* Wed May 13 2009 Michal Nowak <mnowak@redhat.com> 3.3-0.2.rc2
- 3.3-rc2

* Thu May  7 2009 Michal Nowak <mnowak@redhat.com> 3.3-0.1.rc1
- 3.3-rc1

* Mon Mar 16 2009 Michal Nowak <mnowak@redhat.com> 3.2-1
- 3.2

* Mon Mar  2 2009 Michal Nowak <mnowak@redhat.com> 3.2-0.2.rc4
- 3.2-rc4

* Fri Feb 20 2009 Michal Nowak <mnowak@redhat.com> 3.2-0.1.rc3
- 3.2-rc3
- more docs files

* Tue Jan 13 2009 Michal Nowak <mnowak@redhat.com> 3.1.1-1
- 3.1.1

* Wed Dec 24 2008 Michal Nowak <mnowak@redhat.com> 3.1-2
- minor SPEC-file changes

* Sun Dec 14 2008 Michal Nowak <mnowak@redhat.com> 3.1-1
- 3.1

* Fri Sep 19 2008 Michal Nowak <mnowak@redhat.com> 3.0-1
- bump to 3.0

* Sat Sep 06 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.8.rc6
- bump to RC6
- /usr/share/awesome/themes/default is now, again, config file

* Fri Aug 29 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.7.rc5
- bump to RC5

* Sun Aug 24 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.6.rc4
- bump to RC4
- rejecting awesome-3.0-rc3-enhance-wallpaper-cmd.patch -- solved
  upstream via awsetbg script
- using imlib2 instead of GTK+ pixbuf

* Mon Aug 18 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.5.rc3
- buildepend on readline-devel, glib2-devel, gtk2-devel, luadoc
- install via "install -p"
- %%{_datadir}/%%{name}/themes/default is not a config file no more,
  having config file in /usr is kinda weird
- added sub-package awesome-doc to handle API doc files

* Sat Aug 16 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.4.rc3
- awesome-3.0-rc3-enhance-wallpaper-cmd.patch: enhance setting of wallpaper
- new dep: xsri
- %%{_datadir}/%%{name}/themes/default is now handled configfile

* Fri Aug 15 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.3.rc3
- bump to RC3
- xsession desktop file is now provided by upstream
- dumped patches
	awesome-3.0-rc1-fedora-doc-path.patch
	awesome-3.0-rc2-fedora-xsession-path.patch
  both are now in upstream
- cmake is now need >2.6 (present in rawhide)

* Mon Aug 11 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.2.rc2
- bump to RC2

* Mon Aug 04 2008 Michal Nowak <mnowak@redhat.com> 3.0-0.1.rc1
- bump to awesome v3-the new generation

* Mon Jul 28 2008 Michal Nowak <mnowak@redhat.com> 2.3.3-1
- version bump fixes two bugs
- give floating dialogs of maximized windows focus
- awesomerc: fix xterm -e in case of others terms

* Thu Jul 17 2008 Michal Nowak <mnowak@redhat.com> 2.3.2-7
- after some discussion I removed explicit dependency on libconfuse >= 2.6;
  the thing is that awesome runs fine with libconfuse-2.5 but does not
  build with < 2.6. Some build-time hack might be possible but I am obviously
  not going to be involved in this auto*magic. (thx Hans Ulrich Niedermann)

* Wed Jul 16 2008 Michal Nowak <mnowak@redhat.com> 2.3.2-6
- added libXinerama-devel, hopefully last BuildRequire

* Wed Jul 16 2008 Michal Nowak <mnowak@redhat.com> 2.3.2-5
- by mistake I removed BuildRequire on libconfuse-devel,
  now is back again (thanks Mamoru Tasaka)

* Tue Jul 15 2008 Michal Nowak <mnowak@redhat.com> 2.3.2-4
- small polishing in %%doc line

* Mon Jul 14 2008 Michal Nowak <mnowak@redhat.com> 2.3.2-3
- removed redundant libconfuse-devel in BuildRequires
- %%{__install} .desktop file instead of install via desktop-file-install
- changed the license to GPLv2+
- changes in .desktop file
- updated --docdir to include %%{version} too

* Thu Jul 10 2008 Michal Nowak <mnowak@redhat.com> 2.3.2-2
- bumped libconfuse BuildDependency to insist on version 2.6
- changed buildroot to not to have random one
- enhanced %%description

* Thu Jul 3 2008 Michal Nowak <mnowak@redhat.com> 2.3.2-1
- version bump
- add libconfuse-devel as a build dep.
- removed Fedora as a vendor from .desktop file

* Sun Jun 22 2008 Michal Nowak <mnowak@redhat.com> 2.3.1-1
- Initial package
