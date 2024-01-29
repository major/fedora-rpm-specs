Name:           xmlcopyeditor
Version:        1.2.1.3
Release:        23%{?dist}
Summary:        A fast, free, validating XML editor

License:        GPLv2
URL:            http://xml-copy-editor.sourceforge.net/
Source0:        http://downloads.sourceforge.net/xml-copy-editor/%name-%version.tar.gz
Patch0:         xmlcopyeditor-wx3.2.patch

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  wxGTK-devel pcre-devel aspell-devel boost-devel intltool
BuildRequires:  xerces-c-devel libxslt-devel expat-devel desktop-file-utils libappstream-glib

%description
XML Copy Editor is a fast, free, validating XML editor.

%prep
%autosetup -p1
find src -type f -print0 | xargs -0 chmod a-x
tr -d '\r' < src/copying/gpl.txt > COPYING
chmod a-x AUTHORS COPYING NEWS

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
desktop-file-install --remove-category Application \
  --delete-original \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
#rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/po

%find_lang %{name}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/%{name}*

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 1.2.1.3-20
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Scott Talbert <swt@techie.net> - 1.2.1.3-11
- Rebuild with wxWidgets 3.0 and fix FTBFS (#1606742)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2.1.3-5
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2.1.3-3
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.1.3-2
- Rebuilt for Boost 1.59

* Thu Jul 30 2015 Adam Williamson <awilliam@redhat.com> - 1.2.1.3-1
- update to newest upstream
- drop both patches and the inline sed fixes (all fixed upstream)

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.0.4-14
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.2.0.4-12
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.2.0.4-9
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.2.0.4-7
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.2.0.4-6
- Add fix in spec file only for failed compilation

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.2.0.4-5
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.2.0.4-3
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 20 2011 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.2.0.4-1
- Upstream update

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.2.0.2-5
- Rebuilt with xerces-c 3.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.2.0.2-3
- rebuilt against wxGTK-2.8.11-2

* Sat Sep 12 2009 Caolán McNamara <caolanm@redhat.com> 1.2.0.2-2
- Resolves: rhbz#508867 rhbz#511552 FTBFS

* Thu Feb 05 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.2.0.2-1
- Upstream update (http://sourceforge.net/news/?group_id=141776)

* Wed Feb 13 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.0.6-4
- Fixed build under GCC 4.3

* Tue Jan 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.0.6-3
- Removed locale files for now
- Removed spurious license files
- Fixed debuginfo permissions
- Fixed desktop file handling

* Mon Jan 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.0.6-2
- Changed search list of default browsers

* Sun Jan 27 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.0.6-1
- Initial RPM release
