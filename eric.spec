
# avoid empty debuginfo package
%define debug_package %{nil}

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    eric
Summary: Python IDE
Version: 20.1
Release: 12%{?dist}

License: GPLv3+
URL:     http://eric-ide.python-projects.org
Source0: http://downloads.sourceforge.net/sourceforge/eric-ide/%{name}6-%{version}.tar.gz
Source2: http://downloads.sourceforge.net/sourceforge/eric-ide/%{name}6-i18n-de-%{version}.tar.gz
Source4: http://downloads.sourceforge.net/sourceforge/eric-ide/%{name}6-i18n-en-%{version}.tar.gz
Source6: http://downloads.sourceforge.net/sourceforge/eric-ide/%{name}6-i18n-es-%{version}.tar.gz
Source8: http://downloads.sourceforge.net/sourceforge/eric-ide/%{name}6-i18n-ru-%{version}.tar.gz
BuildArch: noarch
# webengine not available on all archs
ExclusiveArch: %{qt5_qtwebengine_arches} noarch

Source30: eric-32.png
Source31: eric-48.png
Source32: eric-64.png

## downstream patches
# sane defaults: disable version check, qt4/qt5 configuration
Patch100: eric6-20.1-defaults.patch

BuildRequires: desktop-file-utils
BuildRequires: python3-devel python3
BuildRequires: python3-qt5
BuildRequires: python3-qt5-webengine
BuildRequires: python3-pyqtchart
BuildRequires: python3-qscintilla-qt5
%if 0%{?fedora}
BuildRequires: libappstream-glib
%endif

Provides: eric6 = %{version}-%{release}

Requires: python3-qt5
Requires: python3-qt5-webengine
Requires: python3-pyqtchart
Requires: python3-qscintilla-qt5
# for python2 DebugClient mostly
#Requires: python2

%description
eric6 is a full featured Python IDE.


%prep
%setup -q -a 2 -a 4 -a 6 -a 8 -n eric6-%{version}

%patch100 -p1 -b .defaults

# copy language files
cp -a  eric6-%{version}/* .


%build
# Empty build


%install
%{__python3} install.py \
  -i %{buildroot}/ \
  -b %{_bindir} \
  -d %{python3_sitelib} \
  -z

# icons
install -m644 -p -D %{SOURCE30} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/eric.png
install -m644 -p -D %{SOURCE31} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/eric.png
install -m644 -p -D %{SOURCE32} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/eric.png

%find_lang %{name} --with-qt --all-name

## toplevel __pycache__ creation is ... inconsistent
## rawhide makes one, f23 local builds do not, so let's *make* it consistent
mkdir -p %{buildroot}%{python3_sitelib}/__pycache__/exclude_rpm_hack

## unpackaged files
# deprecated icons
rm -rfv %{buildroot}%{_datadir}/pixmaps/eric*
rm -fv  %{buildroot}%{python3_sitelib}/eric6/LICENSE.GPL3


%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/eric6.appdata.xml
%endif
test "$(grep '^Exec' %{buildroot}%{_datadir}/applications/eric6.desktop)" = "Exec=%{_bindir}/eric6"
desktop-file-validate %{buildroot}%{_datadir}/applications/eric6.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/eric6_browser.desktop


%files -f %{name}.lang
%doc eric/docs/README.rst
%doc eric/docs/THANKS
%license eric/docs/LICENSE.GPL3
%{_bindir}/eric6*
%{python3_sitelib}/eric6config.py*
%{python3_sitelib}/__pycache__/*
%exclude %{python3_sitelib}/__pycache__/exclude_rpm_hack
%dir %{python3_sitelib}/eric6/
%{python3_sitelib}/eric6/*.py*
%{python3_sitelib}/eric6/__pycache__/
%{python3_sitelib}/eric6/icons/
%{python3_sitelib}/eric6/pixmaps/
%{python3_sitelib}/eric6/[A-Z]*/
%{python3_sitelib}/eric6/*.e4k
%dir %{python3_sitelib}/eric6/i18n/
%{python3_sitelib}/eric6plugins/
%{_datadir}/metainfo/eric6.appdata.xml
%{_datadir}/applications/eric6.desktop
%{_datadir}/applications/eric6_browser.desktop
%{_datadir}/icons/hicolor/*/apps/eric.*
%{_datadir}/qt5/qsci/api/python/
%{_datadir}/qt5/qsci/api/qss/
%{_datadir}/qt5/qsci/api/ruby/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 20.1-10
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20.1-7
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.1-4
- Rebuilt for Python 3.9

* Mon Feb 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.1-3
- ExclusiveArch: %%qt5_qtwebengine_arches noarch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.1-1
- 20.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 18.12-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 18.12-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12-1
- 18.12

* Tue Aug 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08-1
- 18.08

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 18.06-2
- Rebuilt for Python 3.7

* Sat Jun 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.06-1
- 18.06

* Wed May 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.05-2
- fix-bindir.patch (credit to obs frispete:PyQt5/eric6 repo)

* Tue May 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.05-1
- 18.05

* Wed Apr 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04-1
- 18.04

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.03-1
- 18.03

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.02-1
- 18.02

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12-2
- Remove obsolete scriptlets

* Mon Dec 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12-1
- 17.12

* Fri Nov 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11-1
- 17.11

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.05-1
- 17.05

* Thu Apr 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-2
- improve -defaults.patch (include default doc paths mostly)

* Sun Apr 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Fri Apr 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04-1
- eric6-17.04

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 6.1.10-2
- Rebuild for Python 3.6

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 6.1.10-1
- 6.1.10

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 6.1.6-1
- 6.1.6

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 6.1.5-1
- 6.1.5

* Sat Apr 09 2016 Rex Dieter <rdieter@fedoraproject.org> 6.1.4-1
- 6.1.4

* Mon Mar 07 2016 Rex Dieter <rdieter@fedoraproject.org> 6.1.3-1
- 6.1.3, BuildRequires: python3-qt5

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 6.1.2-3
- Requires: python3-qt5-webkit

* Thu Feb 18 2016 Rex Dieter <rdieter@fedoraproject.org> 6.1.2-2
- move python2 DebugClient code under %%python2_sitelib (#1309112)

* Tue Feb 16 2016 Rex Dieter <rdieter@fedoraproject.org> 6.1.2-1
- 6.1.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 04 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.11-1
- 6.0.11

* Wed Oct 21 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.10-1
- 6.0.10

* Tue Sep 08 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.9-1
- 6.0.9

* Tue Jul 07 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.7-1
- 6.0.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.6-1
- 6.0.6, %%lang'ify translations

* Fri Apr 24 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.4-1
- 6.0.4

* Mon Mar 30 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.3-2
- fix app icons (name eric.png instead of eric6.png)

* Wed Mar 04 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0.3-1
- 6.0.3

* Sun Jan 25 2015 Rex Dieter <rdieter@fedoraproject.org>  6.0.1-1
- first try at eric6

* Mon Dec 29 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.5.25-2
- disable update check (by default)
- fix/improve icons

* Mon Dec 29 2014 Rex Dieter <rdieter@fedoraproject.org> 4.5.25-1
- eric4-4.5.25

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Rex Dieter <rdieter@fedoraproject.org> 4.5.19-1
- eric4-4.5.19

* Sun Sep 29 2013 Rex Dieter <rdieter@fedoraproject.org> 4.5.15-1
- eric4-4.5.15

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.5.10-1
- eric4-4.5.10
- fix License
- cleanup .spec

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 4.4.19-4
- Disable requirement for PyXML.  This should allow us to build and run eric
  but it won't be able to validate that project files and other config files
  are correct.  We need to do this because PyXML is going away in Fedora.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Rex Dieter <rdieter@fedoraproject.org> 4.4.19-1
- 4.4.19
- Requires: PyQt4 PyQt4-webkit

* Sat Jun 18 2011 Rex Dieter <rdieter@fedoraproject.org> 4.4.15-1
- 4.4.15

* Mon May 09 2011 Rex Dieter <rdieter@fedoraproject.org> 4.4.14-1
- 4.4.14

* Fri May 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.4.13-1
- 4.4.13
- .desktop category entry needs improvement (#614716)
- update icon scriptlets

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 24 2010 Johan Cwiklinski <johan AT x-td DOT be> 4.4.8-1
- 4.4.8

* Tue Aug 02 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.4.7-1
- 4.4.7

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 04 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.4.6-1
- 4.4.6

* Sun Jun 13 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.4.5-1
- 4.4.5

* Sat May 08 2010 Johan Cwiklinski <johan AT x-tnd DOt be> 4.4.4-1
- 4.4.4

* Tue May 06 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.4.3-1
- 4.4.3

* Sat Mar 06 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.4.2-1
- 4.4.2

* Sat Feb 06 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.4.1-1
- 4.4.1

* Sat Jan 09 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.4.0-1
- 4.4.0
- Add italian translation

* Fri Jan 01 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.10-1
- 4.3.10

* Mon Nov 09 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.9-1
- 4.3.9

* Wed Oct 28 2009 Rex Dieter <rdieter@fedoraproject.org> 4.3.8-2
- eric:desktop : drop deprecated Application category (#487800)

* Fri Oct 16 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.8-1
- 4.3.8

* Fri Sep 18 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.7.1-2
- add default suffix for qt4 apps

* Sun Sep 13 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.7.1-1
- 4.3.7.1
- add BR on qscintilla-python since qscintilla-python-devel no longer
  requires it

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 5 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.5-1
- 4.3.5

* Sun May 31 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.4-1
- 4.3.4

* Tue May 19 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.3-1
- 4.3.3

* Mon Apr 6 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.2-1
- 4.3.2

* Sun Mar 8 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.1-1
- 4.3.1

* Thu Mar 5 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 4.3.0-3
- Fixed bad 'full_python_ver'

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 9 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.3.0-1
- 4.3.0
- Added new translation files (zh_CN)

* Thu Jan 8 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 4.2.5-1
- 4.2.5

* Wed Dec 9 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.2.4a-1
- 4.2.4a

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.2.3-2
- Rebuild for Python 2.6

* Wed Nov 19 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.2.3-1
- 4.2.3

* Wed Oct 8 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.2.2a-1
- 4.2.2a

* Sun Sep 7 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.2.1-1
- 4.2.1
- no longer noarch package (see bz #456761)
- .ts files from translations should not be included

* Sat Jul 05 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.6-1
- 4.1.6

* Sat Jun 07 2008  Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.5-1
- 4.1.5

* Wed May 21 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.4-1
- 4.1.4

* Sat May 17 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.3-1
- 4.1.3

* Sat Apr 05 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.2-2
- using qt4-designer and qt4-doc

* Sat Apr 05 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.2-1
- 4.1.2

* Mon Mar 24 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.1-2
- Qt4 package was renamed from qt4 to qt

* Sat Mar 01 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.1-1
- 4.1.1

* Thu Feb 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-2
- BR: qscintilla-python-devel
- update Source URLS
- omit superfluous (Build)Requires 

* Mon Feb 04 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.1.0-1
- 4.1.0
- Requires PyQt4, not PyQt

* Tue Jan 29 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.0.4-4
- define qt_ver and pyqt_ver
- use environment variables to set documentation path
- init preferences to have relevant qt commands suffix
- add PyQt4 as Requires

* Tue Jan 29 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 4.0.4-3
- requires qt4-designer not qt-designer
- BR : qt-devel already required by PyQt-devel
- seems no longer necessary to define qt_ver
- language files were sourced, not installed
- error on language files path

* Wed Jan 28 2008 Dennis Gilmore <dennis@ausil.us> 4.0.4-2
- fix incorrect BuildRequires/Requires  qscintilla-python 

* Wed Jan 28 2008 Dennis Gilmore <dennis@ausil.us> 4.0.4-1
- update to eric4

* Thu Jan 17 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 3.9.5-2
- Add environment variable to set python, qt4 and qt docs path (bug #200856)
- Requires python-doc, qt-designer, qt4-devel and qt4-doc
- BR: PyQt-devel is already needeed by PyQt-qscintilla-devel

* Fri Jan 11 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 3.9.5-1
- Rebuild for last version
- Include the translation files

* Mon Aug 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.9.2-3
- License: GPL+
- don't set PYTHONOPTIMIZE, let brp-python-bytecompile do it's job,
  addresses selinux issues (#243163, #254421)

* Wed Nov 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.2-2
- Provides: eric3 (get ready for PyQt4-based eric4)
- fix biffed %%version's in %%changelog
- simplify %%description

* Mon Nov 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.2-1
- 3.9.2 

* Mon Nov 06 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.1-4
- BR: PyQt-qscintilla-devel
- (unversioned) Requires: PyQt-qscintilla

* Thu Sep 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.1-3
- include .py[c,o] files again (with no %%ghost'ing)

* Thu Jul 27 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.1-2
- (re)enable PYTHONOPTIMIZE

* Thu Jul 27 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.1-1
- 3.9.1
- gen_sip_api_20060711.tar.gz

* Thu Jul 27 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.0-6
- (re)comment PYTHONOPTIMIZE

* Wed Jul 26 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.0-5
- make fastparser.py eXecutable
- s/$RPM_BUILD_ROOT/%%buildroot/

* Wed Jul 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.0-4
- fix fedora > 4 %%ghost'ing case.

* Wed Jul 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.0-3
- %%ghost .pyo files

* Thu May 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.0-2
- merge -fonts,-api patches into -prefs patch, make it work on
  fc5/python24 too

* Mon May 1 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.9.0-1
- 3.9.0
- create/own %%{_datadir}/eric, for .api files
- generate .api files for python, PyQt
- %%triggerin PyQt4/PyKDE to (auto)generate .api files

* Wed Apr 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.8.2-3
- --vendor=""

* Mon Apr 10 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.8.2-2
- cleanup/drop unused bits 
- note PyQt-qscintilla submission (#188496)

* Mon Mar 27 2006 Rex Dieter <rexdieter[AT]users.sf.net> 3.8.2-1
- 3.8.2

* Mon Dec 19 2005 Rex Dieter <rexdieter[AT]users.sf.net> 3.8.1-1
- 3.8.1
- include gen_python_api, gen_sip_api

* Sun Sep 18 2005 Rex Dieter 3.7.2-0.1.kde
- 3.7.2

* Wed Sep 14 2005 Rex Dieter 3.7.1-0.1.kde
- 3.7.1

* Mon Jun 13 2005 Rex Dieter 0:3.6.1-0.1.kde
- cleanup

* Sat Jan 29 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0:3.6.1-0.fdr.1
- 3.6.1
- TODO: package .api files as (one or more) separate .noarch.rpms

* Mon Nov 29 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0:3.5.1-0.fdr.2
- get icons right

* Mon Nov 29 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0:3.5.1-0.fdr.1
- 3.5.1

* Fri Oct 08 2004 Rex Dieter <rexdieter at sf.net> 0:3.5.0-0.fdr.1
- 3.5.0

* Thu Sep 16 2004 Rex Dieter <rexdieter at sf.net> 0:3.4.2-0.fdr.2
- remove Provides: eric3, (redundant) Provides: eric
- allow build going back as far as rh73.

* Sun May 30 2004 Aurelien Bompard <gauret[AT]free.fr> 0:3.4.2-0.fdr.1
- Initial RPM package

