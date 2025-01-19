%global irrxml_version 1.8.5
%global irrlicht_version 1.8.5

Name:		irrlicht
Summary: 	A high performance realtime 3D engine
Version:	%{irrlicht_version}
Release:	9%{?dist}
License:	zlib
Source0:	http://downloads.sourceforge.net/irrlicht/%{name}-%{irrlicht_version}.zip
# Various fixes, optflags, system libraries/headers
# http://irrlicht.sourceforge.net/phpBB2/viewtopic.php?t=24076&highlight=
Patch0:		irrlicht-1.8-optflags.patch
# Get the code compiling
Patch1:		irrlicht-1.8-glext.patch
# Use system libaesgm
Patch2:		irrlicht18-libaesgm.patch
# Use improved fastatof from assimp
# Upstream applied a modified version of most of this.
# Patch3:	irrlicht18-fastatof-improvements-typefixes.patch
# Make libIrrXML.so
Patch4:		irrlicht-1.8-irrXML-shared-library.patch
# Fix issue with definition of LOCALE_DECIMAL_POINTS
Patch5:		irrlicht-1.8-fix-locale-decimal-points.patch
# Fix build with Mesa 10
Patch6:		irrlicht-1.8.1-mesa10.patch
# Use RPM_LD_FLAGS
Patch7:		irrlicht-1.8.4-ldflags.patch

URL:		http://irrlicht.sourceforge.net/
BuildRequires:  gcc-c++
BuildRequires:	libXxf86vm-devel, mesa-libGL-devel, mesa-libGLU-devel
BuildRequires:	libjpeg-devel, zlib-devel, libaesgm-devel
BuildRequires:	libpng-devel, bzip2-devel
BuildRequires: make
Provides:	irrlicht18 = %{version}-%{release}
Obsoletes:	irrlicht18 <= 1.8-0.4.svn3629%{?dist}

%description
The Irrlicht Engine is an open source high performance realtime 3D engine 
written and usable in C++ and also available for .NET languages. It is 
completely cross-platform, using D3D, OpenGL and its own software renderer, 
and has all of the state-of-the-art features which can be found in 
commercial 3d engines.

%package devel
Summary:	Development headers and libraries for irrlicht
Requires:	%{name}%{?_isa} = %{irrlicht_version}-%{release}
Requires:	mesa-libGL-devel, mesa-libGLU-devel, libXxf86vm-devel
Requires:	libjpeg-devel, zlib-devel, libpng-devel
Requires:	irrXML-devel%{?_isa} = %{irrxml_version}
Provides:	irrlicht18-devel = %{version}-%{release}
Obsoletes:	irrlicht18-devel <= 1.8-0.4.svn3629%{?dist}

%description devel
Development headers and libraries for irrlicht.

%package -n irrXML
Summary:	Simple and fast XML parser for C++
Version:	%{irrxml_version}
Provides:	irrXML18 = %{irrxml_version}-%{release}
Obsoletes:	irrXML18 <= 1.8-0.4.svn3629%{?dist}

%description -n irrXML
irrXML is a simple and fast open source xml parser for C++.

%package -n irrXML-devel
Summary:	Development headers and libraries for irrXML
Version:	%{irrxml_version}
Requires:	irrXML%{?_isa} = %{irrxml_version}-%{release}
Provides:	irrXML18-devel = %{irrxml_version}-%{release}
Obsoletes:	irrXML18-devel <= 1.8-0.4.svn3629%{?dist}

%description -n irrXML-devel
Development headers and libraries for irrXML.

%prep
%setup -q
%patch -P0 -p1 -b .optflags
%patch -P1 -p1 -b .glext
%patch -P2 -p1 -b .libaesgm
# %patch3 -p1 -b .fastatof
%patch -P4 -p1 -b .irrXML
%patch -P5 -p1 -b .fix-locale-decimal-points
%patch -P6 -p1 -b .mesa10
%patch -P7 -p1 -b .ldflags

# Upstream forgot to increment VERSION_RELEASE to 1 in 1.8.1
sed -i 's|VERSION_RELEASE = 0|VERSION_RELEASE = 1|g' source/Irrlicht/Makefile

sed -i 's/\r//' readme.txt
iconv -o readme.txt.iso88591 -f iso88591 -t utf8 readme.txt
mv readme.txt.iso88591 readme.txt
# We don't use any of this. Deleting it so the debuginfo doesn't pick it up.
rm -rf source/Irrlicht/jpeglib source/Irrlicht/zlib source/Irrlicht/libpng source/Irrlicht/aesGladman

for i in include/*.h doc/upgrade-guide.txt source/Irrlicht/*.cpp source/Irrlicht/*.h; do
  	sed -i 's/\r//' $i
	chmod -x $i
	touch -r changes.txt $i
done

# https://bugzilla.redhat.com/show_bug.cgi?id=1035757
sed -i -e '/_IRR_MATERIAL_MAX_TEXTURES_/s/4/8/' include/IrrCompileConfig.h

%build
cd source/Irrlicht
%make_build sharedlib

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
make -C source/Irrlicht INSTALL_DIR=%{buildroot}%{_libdir} install 
cp -a include/*.h %{buildroot}%{_includedir}/%{name}/
pushd %{buildroot}%{_libdir}
ln -s libIrrlicht.so.%{irrlicht_version} libIrrlicht.so.1
ln -s libIrrXML.so.%{irrlicht_version} libIrrXML.so.1
popd

%ldconfig_scriptlets

%ldconfig_scriptlets -n irrXML

%files
%doc readme.txt
%{_libdir}/libIrrlicht.so.*

%files devel
%doc doc/upgrade-guide.txt
%{_includedir}/%{name}/
%exclude %{_includedir}/%{name}/fast_atof.h
%exclude %{_includedir}/%{name}/heapsort.h
%exclude %{_includedir}/%{name}/irrArray.h
%exclude %{_includedir}/%{name}/irrString.h
%exclude %{_includedir}/%{name}/irrTypes.h
%exclude %{_includedir}/%{name}/irrXML.h
%{_libdir}/libIrrlicht.so

%files -n irrXML
%doc readme.txt
%{_libdir}/libIrrXML.so.*

%files -n irrXML-devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/fast_atof.h
%{_includedir}/%{name}/heapsort.h
%{_includedir}/%{name}/irrArray.h
%{_includedir}/%{name}/irrString.h
%{_includedir}/%{name}/irrTypes.h
%{_includedir}/%{name}/irrXML.h
%{_libdir}/libIrrXML.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov  3 2021 Tom Callaway <spot@fedoraproject.org> - 1.8.5-1
- update to 1.8.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug  6 2020 Tom Callaway <spot@fedoraproject.org> - 1.8.4-15
- fix compile against rawhide glibc

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1.8.4-12
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar  5 2018 Tom Callaway <spot@fedoraproject.org> - 1.8.4-7
- actual fix for LDFLAGS from redhat-rpm-config

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 1.8.4-1.6
- Revert LDFLAGS change

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 1.8.4-1.5
- Use LDFLAGS from redhat-rpm-config

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 26 2016 Tom Callaway <spot@fedoraproject.org> - 1.8.4-1
- update to 1.8.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Tom Callaway <spot@fedoraproject.org> - 1.8.3-1
- update to 1.8.3

* Tue Sep  1 2015 Tom Callaway <spot@fedoraproject.org> - 1.8.2-1
- update to 1.8.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.1-3.3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 1.8.1-3
- fix VERSION_RELEASE to be correct in Makefile, resolving bz 1096792

* Thu Nov 28 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.8.1-2
- Change _IRR_MATERIAL_MAX_TEXTURES_ to 8 (RHBZ #1035757)

* Mon Nov 25 2013 Tom Callaway <spot@fedoraproject.org> - 1.8.1-1
- update to 1.8.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.8-2.1
- rebuild due to "jpeg8-ABI" feature drop

* Wed Dec 19 2012 Tom Callaway <spot@fedoraproject.org> - 1.8-2
- fix issue with LOCALE_DECIMAL_POINTS

* Tue Nov 13 2012 Tom Callaway <spot@fedoraproject.org> - 1.8-1
- update to 1.8 final

* Thu Aug 23 2012 Tom Callaway <spot@fedoraproject.org> - 1.7.3-4
- add missing %%{dist} tags.

* Thu Aug 23 2012 Tom Callaway <spot@fedoraproject.org> - 1.7.3-3
- add Irrlicht18 subpackages for supertuxkart (they'll be killed off when 1.8 is final/stable)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Tom Callaway <spot@fedoraproject.org> - 1.7.3-1
- update to 1.7.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.2-10
- fix irrlicht to use libpng-config for cflags/libs
- patches for support for libpng15

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7.2-9
- Rebuild for new libpng

* Wed Aug  3 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.2-8
- cleanup spec
- use correct version when performing symlink

* Tue Mar 22 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.2-7
- fix soname version in link (bz699767)

* Tue Mar 22 2011 Tom Callaway <spot@fedoraproject.org> - 1.7.2-6
- rework shared library patch to ignore crufty ld flags
- rework fast_atof patch to use new naming, more portable typing
- do not package unnecessary patch history files

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7.2-4
- add post/postun scripts for irrXML

* Wed Dec 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7.2-3
- fix versioning on irrXML-devel

* Wed Dec 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7.2-2
- make subpackages for irrXML
- use assimp patch for performance improvement in IrrXML

* Wed Nov 17 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7.2-1
- update to 1.7.2

* Mon May 24 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7.1-2
- rebuild against fixed libaesgm

* Thu Feb 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7.1-1
- update to 1.7.1

* Thu Jan 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.1-1
- update to 1.6.1

* Wed Sep 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6-1
- update to 1.6

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.1-1
- update to 1.5.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-2
- fix libpng calls so we can use system libpng (thanks to tom lane)
- fix license tag

* Thu Jan 8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-1
- build against system libpng
- update to 1.5 final

* Thu Dec 4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-0.2.beta
- fix optflags patch so that ldconfig isn't called during make install

* Wed Dec 3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-0.1.beta
- Initial package for Fedora
