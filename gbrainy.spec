# http://fedoraproject.org/wiki/Packaging/Debuginfo#Useless_or_incomplete_debuginfo_packages_due_to_other_reasons
%global debug_package %{nil}

Name:       gbrainy
Version:    2.4.6
Epoch:      1
Release:    3%{?dist}
Summary:    A brain teaser game and trainer to keep your brain trained

License:    GPLv2
URL:        https://wiki.gnome.org/Apps/gbrainy
Source0:    https://gent.softcatala.org/jmas/%{name}/%{name}-%{version}.tar.gz
# To fix 460353 :
Patch0:     %{name}-fix-location.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk-sharp3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  librsvg2-devel
BuildRequires:  mono-devel
BuildRequires:  yelp-tools
BuildRequires:  make

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
gbrainy is a brain teaser game and trainer to have
fun and to keep your brain trained.

It provides the following types of games:

* Logic puzzles. Games designed to challenge your
    reasoning and thinking skills.
* Mental calculation. Games based on arithmetical
    operations designed to prove your mental calculation skills.
* Memory trainers. Games designed to challenge your short term memory.

%package devel
Summary:      Files needed for developing with gbrainy
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package provides the necessary development libraries and headers
for writing gbrainy applications.

%prep
%autosetup -p0

# use mcs instead of gmcs to compile, as recommended in below link
# http://www.mono-project.com/docs/about-mono/languages/csharp/
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac
autoconf

%build

%configure
%make_build

%install
%make_install
desktop-file-install                                \
    --delete-original                               \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# To fix a rpmlint issue
chmod a-x $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}.exe.config

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS NEWS README MAINTAINERS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/pixmaps/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.4.6-1
- Update to 2.4.6 fixes rhbz#2157249

* Wed Sep 07 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.4.5-1
- Update to 2.4.5 remove upstreamed patch

* Fri Aug 26 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.4.4-3
- Fix FTBFS Fedora 37+

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.4.4-1
- Update to 2.4.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.4.3-1
- Update to 2.4.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 11 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.4.2-1
- Update to 2.4.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.4.1-1
- update to new upstream version 2.4.1

* Wed Mar 20 2019 Benoît Marcelin <sereinity@online.fr> 1:2.4.0-1
- update to new upstream version 2.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.3.5-1
- update to new upstream version 2.3.5

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.3.3-4
- added gcc as BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.3.3-2
- Remove obsolete scriptlets

* Sun Nov 12 2017 Sereinity <sereinit@fedoraproject.org> - 1:2.3.3-1
- new version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.3.2-1
- Rebuilt for new upstream version 2.3.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.3.1-1
- Rebuilt for new upstream version 2.3.1
- Migrating docs from gnome-doc-utils to yelp-tools
- Added itstool as BR
- Fix URLs and use https, fixes rhbz #1380996 - thanks to terrycloth

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.3.0-2
- mono rebuild for aarch64 support

* Wed Sep 14 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.3.0-1
- Rebuilt for new upstream version 2.3.0

* Wed May 18 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.2.7-1
- Rebuilt for new upstream version 2.2.7

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.2.5-1
- Rebuilt for new upstream version 2.2.5, fixes rhbz #1232684, #1239519, #1222424

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1:2.2.3-2
- Rebuild (mono4)

* Wed Aug 27 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.2.3-1
- Rebuilt for new upstream version 2.2.3, fixes rhbz #1008213

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1:2.2.2-2
- Rebuilt for new upstream version 2.2.2, spec cleanup, fixes rhbz #925388

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 08 2013 Jon Ciesla <limburgher@gmail.com> - 1:2.1.3-5
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Benoît Marcelin <sereinity@online.fr> 1:2.1.3-2
- Add Epoch in dependencies

* Wed Jun 27 2012 Benoît Marcelin <sereinity@online.fr> 1:2.1.3-1
- Update to 2.1.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Benoît Marcelin <sereinity@online.fr> 2.06-1
- Update to 2.06
- Remove Ubuntu cleaner patch (now clean from upstream)

* Mon Jul 25 2011 Benoît Marcelin <sereinity@online.fr> 2.00-1
- Update to 2.00

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.52-3.1
- Add BR libtool

* Thu Oct 28 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.52-3
- Change gnome-common to gnome-doc-utils

* Thu Oct 28 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.52-2
- Add BR gnome-common

* Wed Oct 27 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.52-1
- Bump to 1.52
- Add devel subpackage
- Rebuild against mono-2.8

* Mon Jun 07 2010 Christian Krause <chkr@fedoraproject.org> - 1.1-7
- Rebuilt against new mono-addins

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 1.1-6
- Exclude sparc64

* Thu Aug 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1-5
- Build with ppc64 again due to obsolecense of previous update.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Xavier Lamien <laxathom@fedoraproject.org> - 1.1-4
- Build arch ppc64.

* Tue Apr 14 2009 Benoît Marcelin <sereinity@online.fr> 1.1-3
- Re-enable ppc

* Thu Apr 09 2009 Benoît Marcelin <sereinity@online.fr> 1.1-2
- Fix buildrequires

* Wed Apr 08 2009 Benoît Marcelin <sereinity@online.fr> 1.1-1
- Update to 1.1
- Update ExclusiveArch according to mono

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Benoît Marcelin <sereinity@online.fr> 1.00-3
- Fix Summary

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.00-2
- rebuild for new gnome-sharp

* Thu Sep 25 2008 Benoît Marcelin <sereinity@online.fr> 1.00-1
- Clean Build Requires
- Fix bug 460353
- Upate to 1.00
- 1 new logic puzzle, 1 new memory puzzle
- Better look and feel (new background)
- Switch font drawing to Pango
- Better I18N support
- Bug fixes 

* Tue Jun 03 2008 Benoît Marcelin <sereinity@online.fr> 0.70-1
- Update to 0.70
- 8 new puzzles
- License included in the about box
- The drawing area is now square and the application resizes better
- Better score feedback
- Player's history
- Preferences persistence
- Better game selection
- Bug fixes

* Mon Mar 24 2008 Benoît Marcelin <sereinity@online.fr> 0.61-5
- Do if on more than one line (in %%post and %%postun)
- Change ExcludeArch to AxclusiveArch
- Change licence to GPLv2+
- add directory owner %%{_libdir}/%%{name}

* Mon Mar 24 2008 Benoît Marcelin <sereinity@online.fr> 0.61-4
- Update %%post ans %%postun section

* Mon Mar 24 2008 Benoît Marcelin <sereinity@online.fr> 0.61-3
- Add BuildRequires : desktop-file-utils

* Mon Mar 24 2008 Benoît Marcelin <sereinity@online.fr> 0.61-2
- Exclude arch ppc64
- Remove --add-category X-Fedora from the desktop file
- Don't generate empty debuginfo
- Add docfile MAINTAINERS

* Mon Mar 24 2008 Benoît Marcelin <sereinity@online.fr> 0.61-1
- Update to 0.61
- add gtk-update-icon-cache into post and unpost section

* Sun Mar 09 2008 Benoît Marcelin <sereinity@online.fr> 0.60-1
- Initial Fedora build
