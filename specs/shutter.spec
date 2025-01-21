# For git snapshots, set to 0 to use release instead:
%global usesnapshot 1
%if 0%{?usesnapshot}
%global commit0 66c21b2b4750b2bb354887454a9977296d2d844e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif

Name:       shutter
%if 0%{?usesnapshot}
Version:    0.99.6
Release:    0.3%{?snapshottag}%{?dist}
%else
Version:    0.99.5
Release:    3%{?dist}
%endif

Summary:    GTK+3-based screenshot application written in Perl
# share/shutter/resources/icons/draw.svg packaged is CC-BY-SA
# share/shutter/resources/system/plugins/perl/spwatermark/spwatermark.svg is Public Domain
# share/shutter/resources/po/shutter/zh_TW.po is MIT (same as gscrot <https://github.com/gscrot/gscrot/blob/master/LICENSE.md>)
# share/shutter/resources/icons/drawing_tool/objects/tux.svg is GPLv2
# share/shutter/resources/icons/drawing_tool/cursor files are GPLv2+
# share/appdata/shutter.appdata.xml is CC0
# Automatically converted from old format: GPLv3+ and GPLv2+ and GPLv2 and CC-BY-SA and MIT and CC0 and Public Domain - review is highly recommended.
License:    GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT AND CC0-1.0 AND LicenseRef-Callaway-Public-Domain
URL:        https://shutter-project.org/
%if 0%{?usesnapshot}
Source0:    https://github.com/shutter-project/shutter/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
%else
Source0:    https://github.com/shutter-project/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

# https://bugs.launchpad.net/shutter/+bug/1469840
BuildArch:  noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  coreutils
BuildRequires:  sed
%if 0%{?fedora}
BuildRequires:  perl-interpreter
%endif
BuildRequires:  perl-generators
BuildRequires:  gettext

Requires:       ImageMagick
Requires:       tango-icon-theme
Requires:       perl(X11::Protocol::Ext::XFIXES)
Requires:       hicolor-icon-theme
Requires:       libwnck3
Requires:       perl(Image::ExifTool)
Requires:       perl(Goo::Canvas)
%if 0%{?fedora} >= 41
Requires:       gdk-pixbuf2-modules-extra
%endif


# Filter all provides  
%global __provides_exclude_from %{_datadir}/%{name}/resources/system/upload_plugins
# Do not provide perl(Gtk3::IconSize)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Gtk3::IconSize\\)

%description
Shutter is a feature-rich screenshot program for Linux based operating systems
such as Ubuntu. You can take a screenshot of a specific area, window, your whole
screen, or even of a website – apply different effects to it, draw on it to
highlight points, and then upload to an image hosting site, all within one
window. Shutter is free, open-source, and licensed under GPL v3.

%prep
%if 0%{?usesnapshot}
  %autosetup -n %{name}-%{commit0}
%else
  %autosetup -p0 -n %{name}-%{version}
%endif
# Remove the bundled perl(X11::Protocol::Ext::XFIXES)
rm -vr share/%{name}/resources/modules/X11

%build
./po2mo.sh

%install
# executable and data
install -d -m 0755 -p %{buildroot}%{_bindir}
install -d -m 0755 -p %{buildroot}%{_datadir}
install -d -m 0755 -p %{buildroot}%{perl_vendorlib}
cp -pfr bin/* %{buildroot}%{_bindir}/
cp -pfr share/* %{buildroot}%{_datadir}/
mv %{buildroot}%{_datadir}/%{name}/resources/modules/* \
   %{buildroot}%{perl_vendorlib}
rmdir %{buildroot}%{_datadir}/%{name}/resources/modules/

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# fixes E: script-without-shebang
chmod 0644 %{buildroot}%{_datadir}/%{name}/resources/system/upload_plugins/upload/*.pm

%find_lang %{name} --all-name

# Symlink duplicated files
rm %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/shutter-panel.svg
ln -s %{_datadir}/icons/HighContrast/scalable/apps/shutter.svg %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/shutter-panel.svg
rm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/shutter-panel.png
ln -s %{_datadir}/icons/hicolor/16x16/apps/shutter.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/shutter-panel.png
rm %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/shutter-panel.png
ln -s %{_datadir}/icons/hicolor/22x22/apps/shutter.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/shutter-panel.png
rm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/shutter.png
ln -s %{_datadir}/icons/hicolor/32x32/apps/shutter.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/shutter-panel.png
rm %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/shutter-panel.svg 
ln -s %{_datadir}/icons/hicolor/scalable/apps/shutter.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/shutter-panel.svg
rm %{buildroot}%{_datadir}/shutter/resources/icons/Image.svg
ln -s %{_datadir}/shutter/resources/icons/drawing_tool/draw-image.svg %{buildroot}%{_datadir}/shutter/resources/icons/Image.svg
rm %{buildroot}%{_datadir}/shutter/resources/icons/Normal.cur
ln -s %{_datadir}/shutter/resources/icons/drawing_tool/objects/Cursors/Normal.cur %{buildroot}%{_datadir}/shutter/resources/icons/Normal.cur
rm %{buildroot}%{_datadir}/shutter/resources/icons/drawing_tool/cursor/backtext
ln -s %{_datadir}/shutter/resources/icons/drawing_tool/cursor/text %{buildroot}%{_datadir}/shutter/resources/icons/drawing_tool/cursor/backtext

# linking tango-icon theme
ln -s %{_datadir}/icons/Tango/scalable %{buildroot}/%{_datadir}/shutter/resources/icons/drawing_tool/objects/Tango

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%doc CHANGES README
%license COPYING
%license %{_datadir}/%{name}/resources/license/*
%{_bindir}/%{name}
%{perl_vendorlib}/Shutter/
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/icons/HighContrast/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.6-0.3.git66c21b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 06 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.99.6-0.2.git66c21b2
- Add RR gdk-pixbuf2-modules-extra fix bug (#2323682)

* Thu Oct 31 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.99.6-0.1.git66c21b2
- Update to 0.99.6-0.1.git66c21b2

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.99.5-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 27 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.99.5-1
- Update to 0.99.5-1

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 25 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.99.4-1
- Update to 0.99.4-1

* Mon Mar 06 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.99.3-1
- Update to 0.99.3-1

* Fri Mar 03 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.99.3-0.1.gitb089b93
- Update to 0.99.3-0.1.gitb089b93

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.99.2-4
- Add %%{name}-appdata.patch to fix invalid tag in xml file (BZ#2109819)

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.2-3
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.99.2-1
- Update to 0.99.2-1

* Mon Oct 18 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.99.1-1
- Update to 0.99.1-1

* Sun Sep 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.99-2
- Cleanup spec file

* Sat Sep 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.99-1
- Update to 0.99-1

* Tue Aug 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.98-6
- Add RR libwnck3 needed by X11

* Thu Aug 19 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.98-5
- Use plain "perl" instead of %%{__perl} macro
- Do not provide perl(Gtk3::IconSize)

* Thu Aug 19 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.98-4
- Move %%global __provides_exclude_from above the description section
- Add share/shutter/resources/icons/drawing_tool/cursor files are GPLv2+
- List the licenses of all the packaged files into the License section
- Creating symbolic links (ln -s) instead of hard links in the %%install section
- Do not explicitly run-require perl(GooCanvas2::CairoTypes) and perl(Gtk3::ImageView)
  they are found automatically.
- Do not run-require perl-Pango. It is found as perl(Pango) automatically

* Sun Aug 08 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.98-3
- Unbundle tango-icon-theme
- Add RR tango-icon-theme

* Thu Aug 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.98-2
- Update URL 
- Use a description from About
- Declare license files
- Add Provides bundled(tango-icon-theme)
- Do not use %%filter_provides_in use %%__provides_exclude_from
- Add BR libappstream-glib
- Add BR coreutils
- Add BR sed
- Move icons into the correct directory
- Symlink duplicated files
- Filter all provides

* Wed Aug 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.98-1
- Update to 0.98-1

* Tue Jun 22 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.97-0.1.git01d8563
- Update to 0.97-0.1.git01d8563
- Add RR perl(Gtk3::ImageView)
- Add RR perl(Goo::Canvas)
- Add RR perl(GooCanvas2::CairoTypes)
- Add RR perl-Pango

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.94.3-4
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.94.3-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Till Maas <opensource@till.name> - 0.94.3-1
- Update to latest release with critical bug fix
- Remove outdated conditional
- Remove broken patch

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.93.1-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.93.1-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.93.1-8
- use %%license, simplify %%find_lang
- ImageMagick missing from dependencies (#1435789)
- Shutter requires retired orphaned gnome-web-photo (#1436632)
- fix perl-interpretter/gnome-web-photo deps for epel

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.93.1-6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.93.1-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.93.1-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.93.1-1
- Update to 0.93.1 (BZ#1178438, BZ#1247730)
- Requires perl(Gtk2::AppIndicator) (BZ#1228973)
- Fix xdg-email usage (BZ#1209360)
- Specfile untabified

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-3
- Perl 5.22 rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.93-2
- Add an AppData file for the software center

* Sun Oct 19 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.93-1
- Update to 0.93

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-2
- Perl 5.20 rebuild

* Tue Jun 17 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.91-1
- Update to 0.91

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.90.1-1
- Update to 0.90.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.90-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.90-1
- Update to 0.90

* Mon Aug 20 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.89.1-2
- Remove the bundled perl(X11::Protocol::Ext::XFIXES)

* Thu Aug 16 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.89.1-1
- Update to 0.89.1
- Remove the patch for desktop entry file
- Filtered fake provides
- Add Perl MODULE_COMPAT requires
- Requires perl(X11::Protocol::Ext::XFIXES)
- Don't remove the executable bit of the upload plugins

* Fri Aug 10 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.89-1
- Update to 0.89 (#722700, #753423, #659378, #759686, #754880)
- License changed to GPLv3+
- Patch updated
- Perl modules moved to %%{perl_vendorlib}
- Scriptlet updated
- Other cleanup

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 11 2011 Liang Suilong <liangsuilong@gmail.com> - 0.87.3-1
- Upgrade to shutter-0.87.3

* Sat Jun 4 2011 Liang Suilong <liangsuilong@gmail.com> - 0.87.2-1
- Upgrade to shutter-0.87.2
- Add BR: perl(Gtk2::Unique)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.86.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 13 2010 Liang Suilong <liangsuilong@gmail.com> - 0.86.4-1
- Upgrade to shutter-0.86.2
- Add icons for new version

* Thu May 06 2010 Liang Suilong <liangsuilong@gmail.com> - 0.86.2-1
- Upgrade to shutter-0.86.2
- Add BR: hicolor-icon-theme

* Mon Apr 19 2010 Liang Suilong <liangsuilong@gmail.com> - 0.86.1-1
- Upgrade to shutter-0.86.1

* Tue Mar 2 2010 Liang Suilong <liangsuilong@gmail.com> - 0.85.1-2
- Remove BR:gtklp
- fix the bug of directory ownership

* Mon Dec 7 2009 Liang Suilong <liangsuilong@gmail.com> - 0.85.1-1
- Upgrade to shutter-0.85.1

* Sat Nov 21 2009 Liang Suilong <liangsuilong@gmail.com> - 0.85-1
- Upgrade to shutter-0.85

* Mon Aug 3 2009 Liang Suilong <liangsuilong@gmail.com> - 0.80.1-1
- Updrade to shutter-0.80.1

* Mon Aug 3 2009 Liang Suilong <liangsuilong@gmail.com> - 0.80-5
- Update %%install script

* Wed Jul 29 2009 Liang Suilong <liangsuilong@gmail.com> - 0.80-4
- Update %%install script

* Mon Jul 20 2009 Liang Suilong <liangsuilong@gmail.com> - 0.80-3
- Add perl(X11::Protocol) as require

* Thu Jun 25 2009 Liang Suilong <liangsuilong@gmail.com> - 0.80-2
- Upstream to shutter-0.80 Final GA

* Thu Jun 25 2009 Liang Suilong <liangsuilong@gmail.com> - 0.80-1.ppa6
- Upstream to shutter-0.80~ppa6
- Update the SPEC file

* Thu Jun 25 2009 Liang Suilong <liangsuilong@gmail.com> - 0.70.2-3.ppa4
- Remove share/shutter/resources/pofiles/
- Remove share/shutter/resources/modules/File
- Remove share/shutter/resources/pofiles/Proc

* Wed Apr 15 2009 Liang Suilong <liangsuilong@gmail.com> - 0.70.2-2.ppa4
- Add a desktop-file-utils as BuildRequires

* Wed Apr 15 2009 Liang Suilong <liangsuilong@gmail.com> - 0.70.2-2.ppa3
- Add a desktop-file-utils as BuildRequires

* Sun Jan 18 2009 Liang Suilong <liangsuilong@gmail.com> - 0.70.2-1
- Upstream to 0.70.2

* Sun Jan 18 2009 Liang Suilong <liangsuilong@gmail.com> - 0.70.1-1
- Upstream to 0.70.1

* Sun Jan 18 2009 Liang Suilong <liangsuilong@gmail.com> - 0.70-1
- Upstream to 0.70

* Sun Jan 18 2009 Liang Suilong <liangsuilong@gmail.com> - 0.64-2
- Add several Requires so that advanced functions can run.
- Fix the authoritie of install path.

* Fri Jan 02 2009 bbbush <bbbush.yuan@gmail.com> - 0.64-1
- update to 0.64, clean up spec

* Mon Dec 29 2008 Liang Suilong <liangsuilong@gmail.com> - 0.63-3
- Initial package for Fedora
