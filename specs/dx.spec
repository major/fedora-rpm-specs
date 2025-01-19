Name: dx
Version: 4.4.4
Release: 70%{?dist}
Summary: Open source version of IBM's Visualization Data Explorer
License: IPL-1.0
URL: http://www.opendx.org/

Source0: http://opendx.informatics.jax.org/source/dx-%{version}.tar.gz
Source1: %{name}.desktop
Patch1: 0001-dx-rpm.patch
Patch2: 0002-dx-open.patch
Patch3: 0003-dx-gcc43.patch
# fixes http://www.opendx.org/bugs/view.php?id=236
Patch4: 0004-dx-errno.patch
# fix NULL pointer dereference when running dxexec over ssh
# without X forwarding
Patch5: 0005-dx-null.patch
# remove calls to non-public ImageMagick function to fix linking
Patch6: 0006-dx-magick.patch
# fix -Werror=format-security errors
Patch7: 0007-dx-format-security.patch
# fix gcc-6.0 -Warrowing errors
Patch8: 0008-dx-narrowing.patch
# fix gcc-7.0 incompatibilites
Patch9: 0009-gcc7.0-compatibility.patch
Patch10: dx-c99.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: hdf-static, hdf-devel
BuildRequires: ImageMagick-devel
#FIXME doesn't build currently
#BuildRequires: java-devel
BuildRequires: motif-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libtool
BuildRequires: libXinerama-devel
BuildRequires: libXpm-devel
BuildRequires: netcdf-devel
BuildRequires: openssh-clients
BuildRequires: make
Requires: openssh-clients

%description
OpenDX is a uniquely powerful, full-featured software package for the
visualization of scientific, engineering and analytical data: Its open
system design is built on familiar standard interface environments. And its
sophisticated data model provides users with great flexibility in creating
visualizations.

%package libs
Summary: OpenDX shared libraries

%description libs
This package contains the shared libraries from OpenDX.

%package devel
Summary: OpenDX module development headers and libraries
Requires: %{name}-libs = %{version}-%{release}

%description devel
If you want to write a module to use in the Data Explorer Visual Program
Editor, or in the scripting language, you will need this package.

%prep
%setup -q
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1

# fix debuginfo rpmlint warnings
chmod a-x src/exec/{dxmods,dpexec,hwrender}/*.{c,h}

%build
autoreconf --force --install

# The sources aren't ready for modern c++
# As a work-around, use c++11 and c11
%configure \
	--disable-static \
	--enable-shared \
	--with-jni-path=%{java_home}/include \
	--without-javadx \
	--disable-dependency-tracking \
	--enable-smp-linux \
	--enable-new-keylayout \
	--with-rsh=%{_bindir}/ssh \
	CXXFLAGS="-std=c++11 $RPM_OPT_FLAGS" \
	CFLAGS="-std=c11 $RPM_OPT_FLAGS"

%{make_build}

%install
%{make_install}

ln -s ../../%{_lib}/dx/bin_linux $RPM_BUILD_ROOT%{_datadir}/dx/

mv $RPM_BUILD_ROOT%{_libdir}/arch.mak $RPM_BUILD_ROOT%{_includedir}/dx/

install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
sed -e 's/"R. c #b4b4b4",/"R. c none",/' src/uipp/ui/icon50.xpm > $RPM_BUILD_ROOT%{_datadir}/pixmaps/dx.xpm
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

# cleanup buildroot
rm -rf $RPM_BUILD_ROOT%{_datadir}/dx/doc
rm     $RPM_BUILD_ROOT%{_datadir}/dx/lib/outboard.c
rm     $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets libs

%files
%doc AUTHORS ChangeLog NEWS doc/README*
%license LICENSE
%{_bindir}/*
%{_libdir}/dx
%{_datadir}/dx
%{_mandir}/*/*
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/%{name}.desktop

%files libs
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/dx
%{_includedir}/*.h
%{_libdir}/lib*.so

%changelog
* Fri Jan 17 2025 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.4-70
- Switch to using c11 and c++11 (Work-around F42FTBS).

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.4-67
- Use %%patch -P <N> instead of %%patch<N>.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Florian Weimer <fweimer@redhat.com> - 4.4.4-64
- Fix more C compatibility issues (#2154342)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Florian Weimer <fweimer@redhat.com> - 4.4.4-61
- Port to C99 (#2154342)

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.4-60
- Spec file cosmetics.
- Convert license to SPDX.
- Update sources to sha512.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 4.4.4-57
- Rebuild for netcdf 4.8.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 4.4.4-56
- Rebuild for netcdf 4.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 4.4.4-53
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 4.4.4-49
- Rebuild for netcdf 4.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 4.4.4-47
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 4.4.4-45
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-41
- Add 0009-gcc7.0-compatibility.patch (Fix F26FTBFS).
- Rebase patches.
- Modernize spec.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 17 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.4.4-39
- Add dx-narrowing.patch (F24FTBFS, RHBZ#1307436).
- Modernize spec.
- Add license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.4-37
- Rebuild for netcdf 4.4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.4.4-35
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-32
- drop ancient Obsoletes (bug #1002099)
- rebuild to fix bug #925284
- fix -Werror=format-security errors (bug #1037047)

* Mon Aug 12 2013 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-31
- Rebuild against OpenMotif instead of LessTif (should finally fix bug #216160)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Kevin Fenzi <kevin@scrye.com> - 4.4.4-29
- Rebuild for broken deps in rawhide

* Sun Feb 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 4.4.4-28
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 4.4.4-26
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 4.4.4-25
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Tom Callaway <spot@fedoraproject.org> - 4.4.4-23
- rebuild for new ImageMagick

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-22
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 6 2011 Orion Poplawski <orion@cora.nwra.com> - 4.4.4-20
- Rebuild for netcdf 4.1.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 4.4.4-18
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.4-17
- rebuild against new ImageMagick

* Sun Mar 07 2010 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-16
- rebuild against latest ImageMagick

* Sat Feb 27 2010 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-15
- fix netcdf detection (headers are back in /usr/include),
  drop unnecessary patch hunk (rhbz #569066)

* Fri Feb 26 2010 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-14
- fix FTBFS due to calls to non-public function from ImageMagick

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 4.4.4-13
- Explicitly BR hdf-static in accordance with the Packaging
  Guidelines (hdf-devel is still static-only).

* Sun Nov 08 2009 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-12
- bump release to clear up cvs tag mixup

* Thu Nov 05 2009 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-11
- updated source URL
- fix build afainst new netcdf headers location
- fix build against new ImageMagick
- fix NULL pointer dereference when running dxexec over ssh
  without X forwarding

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-8
- fix leftover dxexec process consuming 100% CPU after quitting (bug #469664)
- fix building with current libtool/autoconf

* Wed Sep 24 2008 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-7
- rediff patch to fix build with new rpm

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.4.4-6
- Autorebuild for GCC 4.3

* Mon Jan 07 2008 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-5
- fix build with gcc-4.3
- drop X-Fedora from desktop file (per current packaging guidelines)
- move shared libraries to a subpackage to avoid multilib conflicts
  (bug #341041)

* Fri Aug 17 2007 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-4
- fix open() invocation with O_CREAT and no mode
- update License: in accordance with latest guidelines

* Wed Jul 04 2007 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-3
- rebuild against new netcdf shared libs
- fix menu icon transparency (#207841)
- drop redundant BRs
- fix some rpmlint warnings

* Wed Sep 27 2006 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-2
- rebuild against lesstif

* Fri Sep 22 2006 Dominik Mierzejewski <rpm@greysector.net> 4.4.4-1
- updated to 4.4.4

* Sun Sep 17 2006 Dominik Mierzejewski <rpm@greysector.net> 4.4.0-5
- fix make -jN build

* Sun Sep 03 2006 Dominik Mierzejewski <rpm@greysector.net> 4.4.0-4
- moved arch.mak to _includedir/dx
- fixed program startup from the main ui

* Sat Sep 02 2006 Dominik Mierzejewski <rpm@greysector.net> 4.4.0-3
- removed -samples, will package separately
- disable java parts completely for now
- fixed build on fc6
- moved non-binary stuff to _datadir

* Tue Aug 29 2006 Dominik Mierzejewski <rpm@greysector.net> 4.4.0-2
- simplified autotools invocation
- added dist tag

* Tue Aug 22 2006 Dominik Mierzejewski <rpm@greysector.net> 4.4.0-1
- renamed to dx
- package samples
- install desktop file and icon
- use ssh instead of rsh
- run ldconfig for libs

* Sat Aug 19 2006 Dominik Mierzejewski <rpm@greysector.net>
- fixed remaining paths
- split off -devel package
- added missing BRs
- smp_mflags work again
- TODO: java parts

* Fri Aug 18 2006 Dominik Mierzejewski <rpm@greysector.net>
- initial build
- fix lib paths
