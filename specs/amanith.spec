Name:          amanith
Version:       0.3
Release:       57%{?dist}
Summary:       Crossplatform framework for 2d/3d vector graphics
# Automatically converted from old format: QPL - review is highly recommended.
License:       QPL-1.0
URL:           http://www.amanith.org
# Upstream no longer offers this code
# It originally came from: http://www.amanith.org/download/files/amanith_03.tar.gz
Source0:       amanith_03.tar.gz
BuildRequires:  gcc-c++
BuildRequires: qt3-devel, freetype-devel, libjpeg-devel, libpng-devel, zlib-devel
BuildRequires: libXmu-devel, glew-devel, mesa-libGLU-devel
BuildRequires: mesa-libGL-devel, pkgconfig
BuildRequires: make
Patch0:        amanith-0.3-nothirdpartystatic.patch
Patch1:        amanith-0.3-system-glew.patch
Patch3:        amanith-0.3-gcc-C++fix.patch
Patch4:        amanith-0.3-system-libjpeg.patch
Patch5:        amanith-0.3-system-libpng.patch
Patch6:        amanith-0.3-freetype-fix.patch
Patch7:        amanith-0.3-system-freetype.patch
Patch8:        amanith-0.3-gcc43.patch
Patch9:        amanith-0.3-gcc44.patch
Patch10:       amanith-0.3-fix-DSO.patch
Patch11:       amanith-0.3-gcc-constructor-fix.patch
Patch12:       amanith-0.3-libpng15-fix.patch

%description
Amanith is an OpenSource C++ CrossPlatform framework designed for 2d & 3d 
vector graphics.  All the framework is heavily based on a light plug-in 
system.

%package devel
Summary:       Development files for amanith
Requires:      glew-devel
Requires:      %{name} = %{version}-%{release}

%description devel
Development libraries and headers for developing programs that use amanith.

%prep
%setup -q -n %{name}
%patch -P0 -p1 -b .system
%patch -P1 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1 -b .DSO
%patch -P11 -p1 -b .constructor
%patch -P12 -p1 -b .pngfix
# Boo. Hiss. SGI Free B and GLX files.
rm -rf include/GL/
# Don't need the 3rdpart stuff either.
rm -rf 3rdpart/
chmod -x include/amanith/*.h include/amanith/1d/*.h \
         include/amanith/2d/*.h include/amanith/lang/*.h \
         include/amanith/numerics/*.h include/amanith/geometry/*.h \
         include/amanith/rendering/*.h include/amanith/support/*.h \
         FAQ CHANGELOG INSTALL README LICENSE.QPL doc/amanith.chm \
         src/1d/*.cpp src/2d/*.cpp src/support/*.cpp src/rendering/*.cpp \
         src/*.cpp src/geometry/*.cpp plugins/jpeg/*.cpp src/numerics/*.cpp \
         plugins/fonts/*.cpp plugins/png/*.cpp \
         plugins/jpeg/*.h plugins/png/*.h plugins/fonts/*.h
# convert to utf-8, fix end of line encoding
for i in FAQ CHANGELOG INSTALL README LICENSE.QPL; do
  sed -i -e 's|\r||g' $i
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,} 
  mv $i{.utf8,}
done

%build
export AMANITHDIR=$(pwd)
export LD_LIBRARY_PATH=$AMANITHDIR/lib:$LD_LIBRARY_PATH
source %{_sysconfdir}/profile.d/qt.sh
qmake amanith.pro
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}

# We're using cp instead of install because the symlinks are already
# created correctly.
cp -a lib/*.so* $RPM_BUILD_ROOT%{_libdir}
cp -a plugins/*.so* $RPM_BUILD_ROOT%{_libdir}
cp -a include/amanith $RPM_BUILD_ROOT%{_includedir}

%ldconfig_scriptlets

%files
%doc CHANGELOG FAQ LICENSE.QPL README doc/*
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/amanith/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3-56
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.3-49
- Rebuild for glew 2.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-45
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.3-40
- Rebuilt for glew 2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Tom Callaway <spot@fedoraproject.org> - 0.3-34
- rebuild for new GLEW

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.3-32
- Rebuild for glew 1.13

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3-30
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.3-27
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.3-24
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.3-23
- Rebuild for glew 1.9.0

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 0.3-22
- -Rebuild for new glew

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Tom Callaway <spot@fedoraproject.org> - 0.3-19
- fix code to use modern libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3-18
- Rebuild for new libpng

* Wed Jun 29 2011 Tom Callaway <spot@fedoraproject.org> - 0.3-17
- add missing default constructors

* Mon Jun 20 2011 ajax@redhat.com - 0.3-16
- Rebuild for new glew soname

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3-14
- fix implicit DSO linking

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3-13
- note that upstream is gone, drop URL from Source0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-10
- fix gcc44 compile

* Fri Apr  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-9
- fix FTBFS bz 440739, needed qt3-devel

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3-8
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-7
- fix for gcc4.3

* Tue Jan 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-6
- rebuild against new glew

* Thu Dec 20 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-5
- use macros when we source qt.sh

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-4
- source /etc/profile/qt.sh so qmake is in the path

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-3
- Add glew-devel as explicit Requires for amanith-devel
- change AMANITHDIR to use pwd rather than a macro combo
- drop INSTALL from %%doc

* Thu Nov 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-2
- fix freetype plugin to properly use system includes

* Sat May 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3-1
- initial Fedora package
