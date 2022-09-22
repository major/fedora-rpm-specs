# workaround the Deprecated types
%global optflags %(echo %{optflags} -Wno-deprecated-declarations)

Name:           nautilus-search-tool
Version:        0.3.0
Release:        37%{?dist}
Summary:        A Nautilus extension that makes searching for files easier

License:        GPLv2+
URL:            http://saettaz.altervista.org/software/nautilus_search_tool.html
Source0:        http://dl.sourceforge.net/nautsearchtool/%{name}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml
Patch0:         nautilus-search-tool-0.3.0-headers-typos.patch
Patch1:         nautilus-search-tool-no-eels.patch
Patch2:         nautilus-search-tool-0.3.0-noninit.patch
Patch3:         nautilus-search-tool-0.3.0-startdir.patch
Patch4:         nautilus-search-tool-0.3.0-gtk3.patch
Patch5:         nautilus-search-tool-0.3.0-gnome-desktop.patch
Patch6:         nautilus-search-tool-0.3.0-gnome3.patch
Patch7:         nautilus-search-tool-0.3.0-neheader.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	libtool gettext intltool
BuildRequires:	nautilus-devel
BuildRequires:	GConf2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:  /usr/bin/gnome-search-tool
BuildRequires:  autoconf

Requires:       /usr/bin/gnome-search-tool


%description
This package adds an option to the context menu of folders in Nautilus to
search for files.

%prep
%setup -q
%patch0 -p1 -b .headers-typos
%patch1 -p1 -b .no-eels
%patch2 -p1 -b .noninit
%patch3 -p1 -b .startdir
%patch4 -p1 -b .gtk3
%patch5 -p1 -b .gnome-desktop
%patch6 -p1 -b .gnome3
%patch7 -p1 -b .neheader

%build
autoconf
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
install -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/appdata/%{SOURCE1}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING
%defattr(-,root,root,-)
%{_libdir}/nautilus/extensions-3.0/*.so
%{_datadir}/appdata/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Than Ngo <than@redhat.com> - 0.3.0-32
- Fix FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Paul W. Frields <stickster@gmail.com> - 0.3.0-28
- Fix header call
- Clean up specfile

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Paul W. Frields <stickster@gmail.com> - 0.3.0-21
- Include add-on appdata

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Paul W. Frields <stickster@gmail.com> - 0.3.0-16
- Fix missing Requires (#902003)
- Fix inability to start with selected folder

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.0-12
- Rebuild for new libpng

* Thu Mar 24 2011 Christopher Aillon <caillon@redhat.com> - 0.3.0-11
- Drop unused gnome-desktop dependency

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 0.3.0-10
- Rebuild against newer gtk

* Wed Feb  9 2011 Paul W. Frields <stickster@gmail.com> - 0.3.0-9
- Fix missing BR (#660990)
- Fix building under GTK3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 26 2010 Paul W. Frields <stickster@gmail.com> - 0.3.0-7
- Fix reversed conditional for --path (#568692, James Ettle)

* Mon Jan 18 2010 Paul W. Frields <stickster@gmail.com> - 0.3.0-6
- Rebuild for libgnome-desktop soname bump

* Mon Nov  2 2009 Paul W. Frields <stickster@gmail.com> - 0.3.0-5
- Drop patch in favor of gnome-utils-2.28.1-3

* Mon Nov 02 2009 Paul W. Frields <stickster@gmail.com> - 0.3.0-4
- Cope with missing --version in gnome-search-tool (#516491)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Paul W. Frields <stickster@gmail.com> - 0.3.0-2
- Fix missing BuildRequires

* Sat Jul 18 2009 Paul W. Frields <stickster@gmail.com> - 0.3.0-1
- Update to upstream 0.3.0
- Fixes bug #477810

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Matthias Clasen  <mclasen@redhat.com> - 0.2.2-8
- Try harder not to link against eel

* Tue Dec 16 2008 Matthias Clasen  <mclasen@redhat.com> - 0.2.2-7
- Rebuild to drop eel dependency

* Fri Nov 28 2008 Caolán McNamara <caolanm@redhat.com> - 0.2.2-6
- rebuild for dependancies

* Sat Nov 22 2008 Paul W. Frields <stickster@gmail.com> - 0.2.2-5
- Fix summary

* Thu Jun 06 2008 Caolán McNamara <caolanm@redhat.com> - 0.2.2-4
- rebuild for dependancies

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.2-3
- Autorebuild for GCC 4.3

* Thu Dec 27 2007 Paul W. Frields <stickster@gmail.com> - 0.2.2-2
- Put extension in the proper directory (#426831)

* Fri Aug 17 2007 Paul W. Frields <stickster@gmail.com> - 0.2.2-1
- Update License tag
- Updated to 0.2.2

* Wed Aug 30 2006 Paul W. Frields <stickster@gmail.com> - 0.2-2
- Fix BuildRequires (#200420)

* Sat Feb 18 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.2-1
- Upstream update

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1-2
- Rebuild for Fedora Extras 5

* Tue Sep  3 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1-1
- Initial RPM release
