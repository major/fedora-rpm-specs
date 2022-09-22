Name:           arora
Version:        0.11.0
Release:        27%{?dist}
Summary:        A cross platform web browser

License:        GPLv2+
URL:            http://code.google.com/p/arora/
Source0:        http://arora.googlecode.com/files/%{name}-%{version}.tar.gz
Patch1:         arora-0.10.0-fedorabookmarks.patch
Patch2:         arora-0.10.2-fedorahome.patch
Patch3:         arora-0.11.0-fake-certificate-issuer.patch

BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel >= 4.5.0
BuildRequires:  qt4-webkit-devel
BuildRequires: make

# Gnome does not support preferred applications anymore
Obsoletes:      %{name}-gnome < 0.11.0-2

%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
Arora is a simple, cross platform web browser based on the QtWebKit engine.
Currently, Arora is still under development, but it already has support for
browsing and other common features such as web history and bookmarks.


%prep
%setup -q

%patch1 -p1 -b .fedorabookmarks
%patch2 -p1 -b .fedorahome
%patch3 -p1 -b .fake-certificate-issuer

%build
%{qmake_qt4} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT install

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications\
      $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS README ChangeLog
%doc LICENSE.GPL2 LICENSE.GPL3
%{_bindir}/arora
%{_bindir}/arora-placesimport
%{_bindir}/htmlToXBel
%{_bindir}/arora-cacheinfo
%{_datadir}/applications/%{name}.desktop    
%{_datadir}/icons/hicolor/128x128/apps/arora.png
%{_datadir}/icons/hicolor/16x16/apps/arora.png
%{_datadir}/icons/hicolor/32x32/apps/arora.png
%{_datadir}/icons/hicolor/scalable/apps/arora.svg
%{_datadir}/arora/
%{_datadir}/pixmaps/arora.xpm
%{_mandir}/man1/*


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-17
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.11.0-12
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.11.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.11.0-6
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Jaroslav Reznik <jreznik@redhat.com> - 0.11.0-3
- CVE-2011-3367 - input validation flaw (rhbz#746875)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
- Remove Gnome support as it's not possible to set preferred apps in Gnome 3

* Wed Oct 06 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.11.0-1
- Update to 0.11.0
- Remove Git version patch

* Mon May 17 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.10.2-4
- QWebElement metatype redeclaration in QtWebKit 2.0

* Thu May 13 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.10.2-3
- qt4-webkit-devel BuildRequires preparation

* Thu Dec 10 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.10.2-2
- Conditionaly check for qt4 version

* Thu Dec 10 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.10.2-1
- Update to 0.10.2
- QtWebKit patch removed

* Wed Nov 18 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.10.1-4
- Build over latest qtwebkit trunk from qt 4.6-rc1

* Wed Nov 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10.1-3
- respin against newer qt

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10.1-2
- add dep on qt4 version built against

* Tue Oct 06 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Fri Oct 02 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.10.0-2
- Fedorahome patch rebased

* Fri Oct 02 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Sun Sep 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-2
- add icon/mime scriptlets
- don't own %%{_mandir}/man1
- BR: qt4-devel

* Mon Jul 31 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.8.0-1
- Update to 0.8.0
- Removed custom arora.xml

* Thu Jul 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.7.1-3
- Arora-gnome subpackage now requires Arora package

* Tue Jun 09 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.7.1-2
- Adds arora-gnome subpackage to support preferred app selection
  in Gnome

* Mon Jun 01 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.7.1-1
- Update to 0.7.1
- Parallel build reenabled, fixed in 0.7.1

* Mon May 25 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.7.0-1
- Update to 0.7.0
- Googlesuggest removed

* Sat May 09 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.6.1-2
- Correct Changelog date

* Sat Apr 09 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Mon Mar 30 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.6-2
- Add arora-cacheinfo to package

* Mon Mar 30 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.6-1
- Update to 0.6

* Tue Feb 24 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.5-1
- Update to 0.5
- SPEC file cleanup

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 02 2008 Jaroslav Reznik <jreznik@redhat.com> - 0.4-3
- owns arora and locale directories (bz#473621)

* Mon Oct 06 2008 Jaroslav Reznik <jreznik@redhat.com> - 0.4-2
- Fedora Project & Red Hat bookmarks
- Fedora Project homepage
- GIT version patch

* Wed Oct 01 2008 Jaroslav Reznik <jreznik@redhat.com> - 0.4-1
- Updated to version 0.4

* Thu Sep 25 2008 Jaroslav Reznik <jreznik@redhat.com> - 0.3-2
- Location bar's double click selects all

* Wed Aug 13 2008 Jaroslav Reznik <jreznik@redhat.com> - 0.3-1  
- Initial spec file 
