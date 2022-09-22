Summary:        Library to build graphical widgets for the unicap library
Name:           libunicapgtk
Version:        0.9.8
Release:        28%{?dist}
License:        GPLv2+
URL:            https://www.unicap-imaging.org/
Source0:        https://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0:         libunicapgtk-bz532289.patch
# fix ivalid use of local variable in update_lock_destroy_cb()
Patch1:         libunicapgtk-0.9.8-destroycb.patch
Patch2:         libunicapgtk-0.9.8-datadirname.patch
BuildRequires:  gcc, make, autoconf, automake, gettext-devel, libtool
BuildRequires:  intltool, %{_bindir}/perl, perl(XML::Parser), gettext, gtk-doc >= 1.4
BuildRequires:  libucil-devel, gtk2-devel, libXv-devel, libXext-devel, libX11-devel
BuildRequires:  libICE-devel
Obsoletes:      unicap <= 0.9.7-1

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
Building applications with a graphical user interface is made especially
easy with the unicapGTK widget set.

%package devel
Summary:        Development files for the unicapgtk library
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig, libucil-devel
Obsoletes:      unicap-devel <= 0.9.7-1

%description devel
The libunicapgtk-devel package includes header files and libraries necessary
for for developing programs which use the unicapgtk library. It contains the
API documentation of the library, too.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# fixes for gtk-doc 1.26
sed -e '/^DOC_SOURCE_DIR/s/--sourcedir=//g' -i doc/libunicapgtk/Makefile.am
mkdir -p m4
gtkdocize --copy
autoreconf -fiv

%build
%configure --disable-rpath --enable-gtk-doc
%make_build

%install
%make_install

# Don't install any static .a and libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.{a,la}

%find_lang unicapgtk

%ldconfig_scriptlets

%files -f unicapgtk.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/unicap/*.h
%{_datadir}/gtk-doc/html/%{name}

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Robert Scheck <robert@fedoraproject.org> 0.9.8-21
- Avoid /usr/@DATADIRNAME@/locale/ directory (#1657538)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 07 2010 Kamil Dudka <kdudka@redhat.com> 0.9.8-5
- fix ivalid use of local variable in update_lock_destroy_cb()

* Wed Sep 29 2010 jkeating - 0.9.8-4
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Kamil Dudka <kdudka@redhat.com> 0.9.8-3
- add missing lock/unlock in unicapgtk_video_display_set_pause() (#532289)

* Fri Mar 12 2010 Kamil Dudka <kdudka@redhat.com> 0.9.8-2
- build the package in %%build

* Sun Feb 21 2010 Robert Scheck <robert@fedoraproject.org> 0.9.8-1
- Upgrade to 0.9.8 (#530702, #567109, #567110, #567111)
- Splitting of unicap into libunicap, libucil and libunicapgtk

* Sat Oct 24 2009 Robert Scheck <robert@fedoraproject.org> 0.9.7-1
- Upgrade to 0.9.7 (#530702)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Dan Horak <dan[at]danny.cz> 0.9.5-2
- don't require libraw1394 on s390/s390x

* Sun May 03 2009 Robert Scheck <robert@fedoraproject.org> 0.9.5-1
- Upgrade to 0.9.5

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.9.3-2
- Rebuild against gcc 4.4 and rpm 4.6

* Mon Oct 13 2008 Robert Scheck <robert@fedoraproject.org> 0.9.3-1
- Upgrade to 0.9.3 (#466825, thanks to Hans de Goede)
- Enabled libv4l support for the new gspca kernel driver

* Sat Aug 09 2008 Robert Scheck <robert@fedoraproject.org> 0.2.23-4
- Rebuild to get missing dependencies back (#443015, #458527)

* Tue Aug 05 2008 Robert Scheck <robert@fedoraproject.org> 0.2.23-3
- Filter the unicap plugins which overlap with libv4l libraries

* Tue Jul 22 2008 Robert Scheck <robert@fedoraproject.org> 0.2.23-2
- Rebuild for libraw1394 2.0.0

* Mon May 19 2008 Robert Scheck <robert@fedoraproject.org> 0.2.23-1
- Upgrade to 0.2.23
- Corrected packaging of cpi/*.so files (thanks to Arne Caspari)

* Sat May 17 2008 Robert Scheck <robert@fedoraproject.org> 0.2.22-1
- Upgrade to 0.2.22 (#446021)

* Sat Feb 16 2008 Robert Scheck <robert@fedoraproject.org> 0.2.19-3
- Added patch to correct libdir paths (thanks to Ralf Corsepius)

* Mon Feb 04 2008 Robert Scheck <robert@fedoraproject.org> 0.2.19-2
- Changes to match with Fedora Packaging Guidelines (#431381)

* Mon Feb 04 2008 Robert Scheck <robert@fedoraproject.org> 0.2.19-1
- Upgrade to 0.2.19
- Initial spec file for Fedora and Red Hat Enterprise Linux
