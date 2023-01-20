Name:           alacarte
Version:        3.44.2
Release:        3%{?dist}
Summary:        Menu editor for the GNOME desktop

License:        LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/alacarte
Source0:        https://download.gnome.org/sources/alacarte/3.44/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gnome-menus-devel >= 3.5.3
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pygobject3-devel
BuildRequires:  python3
BuildRequires:  python3-devel

Requires:       gnome-menus >= 3.5.3
Requires:       gtk3
Requires:       python3-gobject


%description
Alacarte is a graphical menu editor that lets you edit, add, and delete
menu entries. It follows the freedesktop.org menu specification and
should work with any desktop environment that uses this specification.


%prep
%autosetup -p1
autoreconf -i -f


%build
%configure
%make_build


%install
%make_install

# desktop-file-install can't manipulate NotShowIn
sed -i -e 's/NotShowIn=KDE;/OnlyShowIn=GNOME;/' \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS
%{python3_sitelib}/Alacarte
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_mandir}/man1/*.1*


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.44.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.44.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Yaakov Selkowitz <yselkowi@redhat.com> - 3.44.2-1
- chore(update): 3.44.2

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.44.1-2
- Rebuilt for Python 3.11

* Mon Mar 21 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 3.44.1-1
- chore(update): 3.44.1

* Sun Mar 20 2022 Yaakov Selkowitz <yselkowi@redhat.com> - 3.44.0-1
- chore(update): 3.44.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.42.0-1
- chore(update): 3.42.0

* Sun Nov 21 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 3.36.0-7
- Fix compatibility with Python 3.10 (#2010664)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.36.0-5
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.36.0-2
- Rebuilt for Python 3.9

* Mon May 25 2020 Yaakov Selkowitz <yselkowi@redhat.com> - 3.36.0-1
- Unretire and update to 3.36.0 (#1839877)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.91-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.11.91-13
- Update requires for pygobject3 -> python2-gobject rename

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.91-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.91-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.91-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.11.91-9
- Remove obsolete scriptlets

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.11.91-8
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.91-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.91-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Jasper St. Pierre <jstpierre@mecheye.net> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.3-1
- Update to 3.7.3

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Wed Sep 19 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.5-1
- Update to 3.5.5

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Matthias Clasen <mclasen@redhat.com> - 0.13.4-6
- Fix requires

* Tue Jun 26 2012 Matthias Clasen <mclasen@redhat.com> - 0.13.4-5
- Spec file cleanups
- Drop gnome-panel dep

* Fri Jun 01 2012 Jasper St. Pierre <jstpierre@mecheye.net> - 0.13.4-5
- Update to 0.13.4. Resolves: #734442

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 14 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.13.2-3
- Require gnome-panel (#684927)
- Compile with %%{?_smp_mflags}
- Update icon-cache scriptlets

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.13.2-1
- Update to 0.13.2

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.13.1-3
- patch configure.ac to support python 2.7; regenerate configure script

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.13.1-1
- Update to 0.13.1

* Sun Mar 14 2010 Matthias Clasen <mclasen@redhat.com> - 0.12.4-2
- Use startup notification

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.4-1
- Update to 0.12.4

* Sat Sep 12 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.3-2
- Bump the gnome-menus requires

* Tue Sep  8 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.3-1
- Update to 0.12.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 16 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.10-1
- Update to 0.11.10

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.9-2
- Only show in GNOME (#486887)

* Tue Feb 17 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.9-1
- Update to 0.11.9

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.8-1
- Update to 0.11.8

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 0.11.7-1
- Update to 0.11.7

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.11.6-6
- Rebuild for Python 2.6

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.6-5
- Tweak %%summary and %%description

* Fri Oct 17 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.6-4
- Make undoing of deletion work

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.6-3
- Update to 0.11.6

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.5-1
- Update to 0.11.5

* Thu Feb 21 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.4-1
- Update to 0.11.4

* Sun Dec 02 2007 Todd Zullinger <tmz@pobox.com> - 0.11.3-5
- put the python scripts in sitelib, not sitearch
- remove autoconf, automake, and intltool BRs
- don't run autoconf/automake in %%build
- BR perl(XML::Parser)
- remove smeg Obsoletes and Provides
- minor rpmlint cleanups

* Sat Aug 11 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.3-4
- Fix the build with intltool 0.36
- Update the license field

* Fri Mar 23 2007 Ray Strode <rstrode@redhat.com> - 0.11.3-3
- change url to gnome.org (bug 233237)

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.3-2
- Update to 0.11.3

* Mon Feb 12 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.2-1.svn20070212
- Bring back editing of the System menu

* Fri Jan 26 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.1.1-2
- Fix the Provides: line

* Thu Jan 11 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.1.1-1
- Update to 0.11.1.1

* Wed Dec 20 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.2-2
- Update to 0.10.2

* Sat Dec  9 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.1-4
- try again 

* Wed Dec  6 2006 Jeremy Katz <katzj@redhat.com> - 0.10.1-2
- build against python 2.5 

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.1-1
- Update to 0.10.1
* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.0-1.fc6
- Update to 0.10.0

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.90-7.fc6
- Fix more build requires

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.90-3.fc6
- Add BR for pkgconfig

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.90-1.fc6
- Update to 0.9.90

* Thu Aug 17 2006 Ray Strode <rstrode@redhat.com> - 0.8-8
- initial build for Fedora Core

* Wed Feb 15 2006 John Mahowald <jpmahowald@gmail.com> - 0.8-7
- Rebuild for Fedora Extras 5

* Fri Feb 3 2006  John Mahowald <jpmahowald@gmail.com> - 0.8-3
- Fix stray reference to smeg
- Use python sitearch macro from template

* Sat Oct 29 2005  John Mahowald <jpmahowald@gmail.com> - 0.8-2
- Rebuild

* Thu Oct 27 2005  John Mahowald <jpmahowald@gmail.com> - 0.8-1
- rename to alacarte
- Update to 0.8

* Thu Oct 20 2005  John Mahowald <jpmahowald@gmail.com> - 0.7.5-4
- remove requires gnome-menus

* Tue Aug 30 2005 John Mahowald <jpmahowald@gmail.com> - 0.7.5-3
- Move to /usr/share

* Tue Jun 28 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.5-2
- Desktop-file-utils for kde desktop entry as well as default one.

* Wed Jun 08 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.5-1
- Rebuilt for 0.7.5

* Mon Jun 06 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.4-1
- Rebuilt for 0.7.4

* Wed Jun 01 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7.1-1
- Rebuilt for 0.7.1
- Smeg now use the stock gnome menu icon, removed pixmaps from %%files

* Wed Jun 01 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7-2
- Added missing dependency gnome-python2-gconf

* Tue May 31 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.7-1
- Rebuilt for 0.7

* Mon May 30 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.6.2-2
- Added desktop-file-utils to Buildrequires
- Addded desktop-file-utils %%post and %%postun

* Sun May 29 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.6.2-1
- Rebuilt for 0.6.2

* Mon May 23 2005 Sindre Pedersen Bjordal <foolish[AT]fedoraforum.org> - 0.5-1
- Initial build
