Name:           ftgl
Version:        2.1.3
Release:        0.30.rc5%{?dist}
Summary:        OpenGL frontend to Freetype 2

License:        LGPLv2
URL:            http://ftgl.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ftgl/ftgl-%{version}-rc5.tar.bz2
Patch0:         ftgl-2.1.3-rc5-ttf_font.patch
Patch1:         ftgl-2.1.3-rc5-ldflags.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen

BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  cppunit-devel
BuildRequires: make

Obsoletes: ftgl-utils < %{version}


%description
FTGL is a free open source library to enable developers to use arbitrary
fonts in their OpenGL (www.opengl.org)  applications.
Unlike other OpenGL font libraries FTGL uses standard font file formats
so doesn't need a preprocessing step to convert the high quality font data
into a lesser quality, proprietary format.
FTGL uses the Freetype (www.freetype.org) font library to open and 'decode'
the fonts. It then takes that output and stores it in a format most 
efficient for OpenGL rendering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       freetype-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package docs
Summary:        Documentation for %{name}

%description docs
This package contains documentation files for %{name}.


%prep
%setup -q -n ftgl-%{version}~rc5
%patch0 -p1 -b .destdir
%patch1 -p1 -b .ldflags



%build
%configure \
  --enable-shared \
  --disable-static \
  --with-gl-inc=%{_includedir} \
  --with-gl-lib=%{_libdir} \
  --with-glut-inc=%{_includedir} \
  --with-glut-lib=%{_libdir} \
  --with-x

# Remove the ~rc5 from the pc file, as this causes rpm to add a
# Requires: rpmlib(TildeInVersions) <= 4.10.0-1 
# Which breaks installing ftgl-devel into a koji buildroot (rhbz#843460)
sed -i 's/2\.1\.3~rc5/2.1.3/' ftgl.pc

make all %{?_smp_mflags}


%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Doc fixes
mkdir -p __doc/html
install -pm 0644 $RPM_BUILD_ROOT%{_datadir}/doc/ftgl/html/* __doc/html
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc


%ldconfig_scriptlets


%files
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/FTGL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files docs
%doc __doc/*


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.30.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.29.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.28.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.27.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.26.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.25.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.24.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.23.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.22.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.21.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.20.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.19.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.18.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.17.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.16.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.15.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-0.14.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.13.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.3-0.12.rc5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.11.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.10.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.9.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.8.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 26 2012 Hans de Goede <hdegoede@redhat.com> - 2.1.3-0.7.rc5
- Don't put ~rc5 in the pkg-config version string - rhbz#843460

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.6.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.5.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.4.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 2.1.3-0.3.rc5
- Fix Missing ldflags - rhbz#565150

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.2.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 kwizart < kwizart at gmail.com > - 2.1.3-0.1.rc5
- Update to 2.1.3-rc5
- Obsoletes -utils sub-package

* Fri Feb 27 2009 kwizart < kwizart at gmail.com > - 2.1.2-10
- Switch from freefont to dejavu-sans-fonts - #480455

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  9 2008 kwizart < kwizart at gmail.com > - 2.1.2-8
- Rebuild for gcc43

* Sat Dec 15 2007 kwizart < kwizart at gmail.com > - 2.1.2-7
- Add -docs to fix multiarch conflicts  #341191
- Fix libGL requirement.
- Project Moved to sourceforge

* Sun Aug 26 2007 kwizart < kwizart at gmail.com > - 2.1.2-6
- rebuild for ppc32
- Update the license field

* Sat Jul 14 2007 kwizart < kwizart at gmail.com > - 2.1.2-5
- Fix version field the whole package

* Fri Jul 13 2007 kwizart < kwizart at gmail.com > - 2.1.2-4
- Modified ftgl-2.1.2-pc_req.patch
- Add Requires freefont to -utils

* Fri Jul 13 2007 kwizart < kwizart at gmail.com > - 2.1.2-3
- Add Requirements for -devel
- Preserve timestramp for install step
- Add ftgl-utils to prevent conflict with multilibs
  Add patch to prevent rpath

* Mon May 28 2007 kwizart < kwizart at gmail.com > - 2.1.2-2
- Add ftgl.pc patch
- Add BR freeglut-devel
- Remove unneeded LDFLAGS
- Cleaned spec file

* Mon May 14 2007 kwizart < kwizart at gmail.com > - 2.1.2-1
- Initial package for Fedora
