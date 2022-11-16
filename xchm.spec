Summary:        A GUI front-end to CHMlib
Name:           xchm
Version:        1.23
Release:        23%{?dist}
License:        GPLv2+
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         wxwidgets-3.0.patch
URL:            http://xchm.sourceforge.net/
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  chmlib-devel
BuildRequires:  wxGTK-devel
BuildRequires:  desktop-file-utils

%description
xCHM is a wxWidgets-based .chm viewer. xCHM can show the contents tree if 
one is available, print the displayed page, change fonts faces and size, 
work with bookmarks, do the usual history stunts (forward, back, home), 
provide a searchable index and seach for text in the whole book. The 
search is a fast B-tree search, based on the internal $FIftiMain file 
found inside indexed .chm archives, and it can be customized to search in 
content or just the topics' titles.

%prep
%setup -q
%patch0 -p1

%build
#export CFLAGS="-g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m64 -mtune=generic"
%configure --disable-dependency-tracking
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications/
desktop-file-install  \
        %if 0%{?fedora} < 19
          --vendor fedora \
        %endif
          --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE1}
for resolution in 16 32 48 128; do
  dir=${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/${resolution}x${resolution}/
  mkdir -p $dir/apps $dir/mimetypes
  install -p -m644 art/xchm-${resolution}.xpm $dir/apps/xchm.xpm
  install -p -m644 art/xchmdoc-${resolution}.xpm $dir/mimetypes/application-x-chm.xpm
  ln -s application-x-chm.xpm $dir/mimetypes/gnome-mime-application-x-chm.xpm
done
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/xchm
%{_datadir}/icons/hicolor/
%{_datadir}/applications/*

%changelog
* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 1.23-23
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Scott Talbert <swt@techie.net> - 1.23-14
- Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.23-11
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.23-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 26 2014 manuel "lonely wolf" wolfshant <wolfy@fedoraproject.org> - 1.23-2
- Adjust version required for wxGTK and fixed "bogus date in %%changelog"

* Mon Sep 02 2013 manuel "lonely wolf" wolfshant <wolfy@fedoraproject.org> - 1.23-1
- New upstream version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 manuel "lonely wolf" wolfshant <wolfy@fedoraproject.org> - 1.22-1
- New upstream version
- Use newer autoconf in order to support ARM64

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.21-2
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Mon Nov 26 2012 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.21-1
- New upstream version

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 6 2011 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.20-1
- New upstream version, fixes #701827

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.17-3
- rebuilt against wxGTK-2.8.11-2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 8 2009 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.17-1
- Version update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Mar  1 2008 Patrice Dumas <pertusus@free.fr> 1.14-1
- update to 1.14. Remove upstreamed gcc 4.3 patch

* Sat Jan  5 2008 Patrice Dumas <pertusus@free.fr> 1.13-2
- fixes for gcc 4.3

* Wed Aug  8 2007 Patrice Dumas <pertusus@free.fr> 1.13-1
- update to 1.13

* Sun Dec 17 2006 Patrice Dumas <pertusus@free.fr> 1.10-2
- rebuild for wxGTK-2.8.0

* Wed Nov 22 2006 Patrice Dumas <pertusus@free.fr> 1.10-1
- update to 1.10

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.9-6
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Patrice Dumas <pertusus@free.fr> 1.9-5
- install the icon for the chm file type

* Sun Sep 24 2006 Patrice Dumas <pertusus@free.fr> 1.9-4
- add a MimeType entry in desktop file. Fix #207833

* Sat Sep 23 2006 Patrice Dumas <pertusus@free.fr> 1.9-3
- install icons in %%{_datadir}/icons/ instead of %%{_datadir}/pixmaps/
  fix #207759

* Tue Sep 12 2006 Patrice Dumas <pertusus@free.fr> 1.9-2
- rebuild for FC6

* Fri Jun  2 2006 Patrice Dumas <pertusus@free.fr> 1.9-1
- update to 1.9

* Fri Jun  2 2006 Patrice Dumas <pertusus@free.fr> 1.8-1
- update to 1.8

* Thu Mar  9 2006 Patrice Dumas <pertusus@free.fr> 1.4-3
- update to 1.4

* Mon Dec 05 2005 Peter Lemenkov <lemenkov@newmail.ru> 1.2-1
- Version 1.2

* Mon Mar 21 2005 Nick Soracco <nick@deepgroove.org>
- Initial RPM release.  Complementing the faderbox.org package.
