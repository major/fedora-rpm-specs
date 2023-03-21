Name:           raw-thumbnailer
Version:        3.0.0
Release:        25%{?dist}
Summary:        Nautilus file manager thumbnailer for RAW images

License:        GPLv2+
URL:            https://libopenraw.freedesktop.org/raw-thumbnailer/
Source0:        https://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-libopenraw.patch
Patch1:         %{name}-%{version}-larger-thumbnails.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libopenraw-gnome-0.1)
BuildRequires:  perl(XML::Parser)

%description
RawThumbnailer is a thumbnailer for RAW files that works with Nautilus.

%prep
%autosetup -p 1


%build
%configure
%make_build


%install
%make_install

%files
%{_bindir}/raw-thumbnailer
%{_datadir}/mime/packages/*.xml
%{_datadir}/thumbnailers/raw.thumbnailer
%doc AUTHORS COPYING NEWS


%changelog
* Sun Mar 19 2023 Julian Sikorski <belegdol+github@gmail.com> - 3.0.0-25
- Fix maximum thumbnail size limin (RH #2165576)
- Switch to https URLs for URL and Source0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 3.0.0-9
- Rebuilt and patched for libopenraw-0.1.0
- Modernised the .spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-6
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 30 2012 Julian Sikorski <belegdol@fedoraproject.org> - 3.0.0-1
- Updated to 3.0.0
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- GConf2 is no more
- Switched to .bz2 sources
- Added intltool to BuildRequires, removed libgsf-devel and gnome-vfs2-devel

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Caolán McNamara <caolanm@redhat.com> - 0.99.1-9
- Rebuild for new libgsf

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.99.1-7
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 22 2010 Victor Bogado <victor@bogado.net> - 0.99.1-5
- License tag
- gconf schemas don't recieve the "config" macro.

* Mon Feb 08 2010 Victor Bogado <victor@bogado.net> - 0.99.1-4
- More adjustments, fine tunnings, sugjested by ELMORABITY Mohamed in (https://bugzilla.redhat.com/show_bug.cgi?id=533887#c6).

* Wed Dec 30 2009 Victor Bogado <victor@bogado.net> - 0.99.1-3
- Fixed problems pointed out by ELMORABITY Mohamed in (https://bugzilla.redhat.com/show_bug.cgi?id=533887#c2).

* Mon Nov 09 2009 Victor Bogado <victor@bogado.net> - 0.99.1-2
- Compleated some missing some build requires.

* Mon Nov 09 2009 Victor Bogado <victor@bogado.net> - 0.99.1-1
- Initial spec file
