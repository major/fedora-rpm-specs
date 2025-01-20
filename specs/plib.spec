Name:           plib
Version:        1.8.5
Release:        39%{?dist}
Summary:        Set of portable libraries especially useful for games
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://plib.sourceforge.net/
Source:         http://plib.sourceforge.net/dist/plib-%{version}.tar.gz
Patch1:         plib-1.8.4-fullscreen.patch
Patch3:         plib-1.8.4-autorepeat.patch
Patch4:         plib-1.8.5-CVE-2011-4620.patch
Patch5:         plib-1.8.5-CVE-2012-4552.patch
Patch6:         plib-freeglut.patch
Patch7:         plib-1.8.5-spelling_errors.patch
Patch8:         plib-1.8.5-dont_break_joystick_system_calibration.patch
Patch9:         plib-1.8.5-CVE-2021-38714.patch
BuildRequires:  gcc gcc-c++ make
BuildRequires:  freeglut-devel libpng-devel libXext-devel libXi-devel
Buildrequires:  libXmu-devel libSM-devel libXxf86vm-devel

%description
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%
portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.


%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libGL-devel

%description devel
This package contains the header files and libraries needed to write
or compile programs that use plib.


%prep
%autosetup -p1
# for some reason this file has its x permission sets, which makes rpmlint cry
chmod -x src/sg/sgdIsect.cxx


%build
%configure CXXFLAGS="$RPM_OPT_FLAGS -fPIC -DXF86VIDMODE"
make %{?_smp_mflags} 
# and below is a somewhat dirty hack inspired by debian to build shared libs
# instead of static. Notice that the adding of -fPIC to CXXFLAGS above is part
# of the hack.
dirnames=(util sg ssg fnt js net psl pui puAux pw sl sl ssgAux)
libnames=(ul sg ssg fnt js net psl pu puaux pw sl sm ssgaux)
libdeps=("" \
  "-L../util -lplibul" \
  "-L../util -lplibul -L../sg -lplibsg -lGL" \
  "-L../util -lplibul -L../sg -lplibsg -lGL" \
  "-L../util -lplibul" \
  "-L../util -lplibul" \
  "-L../util -lplibul" \
  "-L../util -lplibul -L../sg -lplibsg -L../fnt -lplibfnt -lGL" \
  "-L../util -lplibul -L../sg -lplibsg -L../fnt -lplibfnt -L../pui -lplibpu -lGL" \
  "-L../util -lplibul -lX11 -lGL -lXxf86vm" \
  "-L../util -lplibul" \
  "-L../util -lplibul" \
  "-L../util -lplibul -L../sg -lplibsg -L../ssg -lplibssg -lGL")

for (( i = 0; i < 13; i++ )) ; do
  pushd src/${dirnames[$i]}
  g++ -shared -Wl,-soname,libplib${libnames[$i]}.so.%{version} \
    -o libplib${libnames[$i]}.so.%{version} `ar t libplib${libnames[$i]}.a` \
    ${libdeps[$i]} -Wl,-z,relro -Wl,-z,now
  ln -s libplib${libnames[$i]}.so.%{version} libplib${libnames[$i]}.so
  popd
done


%install
make install DESTDIR=$RPM_BUILD_ROOT
# we don't want the static libs
rm $RPM_BUILD_ROOT%{_libdir}/*.a
# instead do a DIY install of the shared libs we created
cp -a `find . -name "libplib*.so*"` $RPM_BUILD_ROOT%{_libdir}


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog NOTICE README
%license COPYING
%{_libdir}/libplib*.so.%{version}

%files devel
%{_includedir}/*
%{_libdir}/libplib*.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.5-38
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 13 2022 Hans de Goede <hdegoede@redhat.com> - 1.8.5-30
- Add 3 patches from Debian
- Fixes CVE-2021-38714 (rhbz#1997815)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.8.5-24
- Update for new freeglut.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug  9 2018 Hans de Goede <hdegoede@redhat.com> 1.8.5-21
- Fix FTBFS (rhbz#1605477)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Adam Jackson <ajax@redhat.com> 1.8.5-14
- Use g++ to link, and fix linker flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
