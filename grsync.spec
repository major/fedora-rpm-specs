%define _legacy_common_support 1

Name:           grsync
Version:        1.3.0
Release:        6%{?dist}
Summary:        A Gtk+ GUI for rsync

License:        GPLv2
URL:            http://www.opbyte.it/grsync/
Source0:        http://www.opbyte.it/release/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gtk3-devel desktop-file-utils gettext perl(XML::Parser)
BuildRequires:  intltool
BuildRequires: make
Requires:       polkit

%description
Grsync is a GUI (Graphical User Interface) for rsync, the commandline 
directory synchronization tool. It makes use of the GTK libraries and 
is released under the GPL license, so it is opensource. It is in beta 
stage and doesn't support all of rsync features, but can be effectively 
used to synchronize local directories. For example some people use 
grsync to synchronize their music collection with removable devices or 
to backup personal files to a networked drive. 


%prep
%autosetup

# some minor corrections for rpmlint
sed -i 's/\r//' README AUTHORS NEWS
sed -i 's|@prefix@/bin/@PACKAGE@|@PACKAGE@|' grsync.desktop.in


%build
%configure --disable-unity
%make_build
sed -i 's|Icon=%{name}.png|Icon=%{name}|g' %{name}.desktop


%install
%make_install
desktop-file-install \
    --remove-category=Application \
    --add-category=FileTransfer \
    --add-category=GTK \
    --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/grsync*
%{_mandir}/man1/grsync*.1.*
%{_datadir}/pixmaps/grsync*.png
%{_datadir}/applications/grsync.desktop
%{_datadir}/grsync/
%{_datadir}/icons/hicolor/*/mimetypes/application-x-grsync-session.png
%{_datadir}/mime/packages/grsync.xml


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.0-1
- Update to 1.3.0 fixes rhbz#1900707

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.8-1
- Update to 1.2.8 fixes rhbz#1830922

* Fri Apr 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.6-6
- Fix FTBFS with gcc10 fixes rhbz#1799495

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.6-1
- update to latest upstream release 1.2.6 fixes rhbz #1397648
- spec cleanup, modernization and silent rpmlint

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.5-8
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.5-2
- update mime scriptlet

* Thu Aug 21 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4
- Remove dsofix patch, fixed upstream
- Minor spec file clean-up

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Mon Oct 22 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- Configure with --disable-unity to make sure the package builds

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.0-2
- Rebuild for new libpng

* Sat Jul 30 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Require polkit for 'Run as superuser' option through pkexec

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Wed Mar 31 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Add scriptlets to update icon cache and install mime type

* Tue Feb 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- Add patch to fix DSO linking (#565142)

* Thu Feb 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Tue Dec 22 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.9.3-1
- new upstream release

* Mon Oct 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.2-1
- new upstream release (fixes #524169)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.9.1-1
- new upstream release

* Sun Jun 14 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.9.0-1
- new upstream release

* Fri Apr 10 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.3-2
- BR: intltool

* Fri Apr 10 2009 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.3-1
- new upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.2-1
- new upstream release
- drop grsync-0.6.1-fix-crash-when-adding-new-sessions.patch

* Fri Feb 08 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.1-2
- workaround crash when adding new sessions (#385051)

* Wed Nov 28 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.6.1-1
- New upstream version: 0.6.1

* Tue Sep 18 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.6-1
- New upstream version: 0.6
- Change license to GPLv2

* Tue May 15 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.2-2
- BR: perl(XML::Parser)

* Tue Jan 23 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.5.2-1
- New upstream version: 0.5.2

* Fri Dec 01 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-2
- BR: gettext

* Sat Nov 11 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.5-1
- New upstream version: 0.5

* Fri May 05 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.4.1-1
- Initial Spec Release
