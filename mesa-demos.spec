%global gitdate 20210504
%global gitcommit 0f9e7d995a14f15666600fc8598f941b619d82fe
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global xdriinfo xdriinfo-1.0.4
%global demodir %{_libdir}/mesa

Summary: Mesa demos
Name: mesa-demos
Version: 8.4.0
Release: 14.%{gitdate}git%{shortcommit}%{?dist}
License: MIT
URL: http://www.mesa3d.org
#Source0: https://mesa.freedesktop.org/archive/demos/%{version}/%{name}-%{version}.tar.bz2
Source0: mesa-demos-%{gitdate}.tar.bz2
Source1: http://www.x.org/pub/individual/app/%{xdriinfo}.tar.bz2
Source2: mesad-git-snapshot.sh
# Patch pointblast/spriteblast out of the Makefile for legal reasons
Patch0: mesa-demos-8.0.1-legal.patch
Patch1: mesa-demos-as-needed.patch
# Fix xdriinfo not working with libglvnd
Patch2: xdriinfo-1.0.4-glvnd.patch
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig autoconf automake libtool
BuildRequires: freeglut-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGLES-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: libGLU-devel
BuildRequires: libXext-devel
BuildRequires: wayland-devel
BuildRequires: freetype-devel

%description
This package provides some demo applications for testing Mesa.

%package -n glx-utils
Summary: GLX utilities
Provides: glxinfo glxinfo%{?__isa_bits}

%description -n glx-utils
The glx-utils package provides the glxinfo and glxgears utilities.

%package -n egl-utils
Summary: EGL utilities
Provides: eglinfo es2_info

%description -n egl-utils
The egl-utils package provides the eglinfo and es2_info utilities.

%prep
%setup -q -n %{name}-%{gitdate} -b1
%patch0 -p1 -b .legal
%patch1 -p1 -b .asneeded
pushd ../%{xdriinfo}
%patch2 -p1
popd

# These two files are distributable, but non-free (lack of permission to modify).
rm -rf src/demos/pointblast.c
rm -rf src/demos/spriteblast.c

%build
autoreconf -vfi
%configure \
    --bindir=%{demodir} \
    --with-system-data-files \
    --enable-x11 \
    --enable-wayland \
    --enable-gbm \
    --enable-egl \
    --enable-gles2 \
    --enable-libdrm \
    --enable-freetype2
%make_build

pushd ../%{xdriinfo}
%configure
%make_build
popd

%install
%make_install

pushd ../%{xdriinfo}
%make_install %{?_smp_mflags}
popd

install -m 0755 src/xdemos/glxgears %{buildroot}%{_bindir}
install -m 0755 src/xdemos/glxinfo %{buildroot}%{_bindir}
%if 0%{?__isa_bits} != 0
install -m 0755 src/xdemos/glxinfo %{buildroot}%{_bindir}/glxinfo%{?__isa_bits}
%endif

install -m 0755 src/egl/opengl/eglinfo %{buildroot}%{_bindir}
install -m 0755 src/egl/opengles2/es2_info %{buildroot}%{_bindir}

%check

%files
%{demodir}
%{_datadir}/%{name}/

%files -n glx-utils
%{_bindir}/glxinfo*
%{_bindir}/glxgears
%{_bindir}/xdriinfo
%{_datadir}/man/man1/xdriinfo.1*

%files -n egl-utils
%{_bindir}/eglinfo
%{_bindir}/es2_info

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-14.20210504git0f9e7d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-13.20210504git0f9e7d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-12.20210504git0f9e7d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Adam Jackson <ajax@redhat.com> - 8.4.0-11.20210504git0f9e7d995a14f15
- Sync with upstream to drop the glew dependency

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-9.20181118git1830dcb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Tom Stellard <tstellar@redhat.com> - 8.4.0-8.20181118git1830dcb
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-7.20181118git1830dcb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-6.20181118git1830dcb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Gwyn Ciesla <gwync@protonmail.com> - 8.4.0-5.20181118git1830dcb
- Rebuilt for new freeglut.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-4.20181118git1830dcb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-3.20181118git1830dcb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Lyude Paul <lyude@redhat.com> - 8.4.0-2.20181118git1830dcb
- Start using proper git version strings for rawhide
- Enabling building of wayland and freetype demos

* Sun Nov 18 2018 Lyude Paul <lyude@redhat.com> - 8.4.0-1
- New git snapshot

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 8.3.0-12
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Adam Jackson <ajax@redhat.com> - 8.3.0-9
- New git snapshot

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Hans de Goede <hdegoede@redhat.com> - 8.3.0-6
- Fix xdriinfo not working with libglvnd (rhbz#1429894)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 8.3.0-4
- Rebuild for glew 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 8.3.0-2
- Rebuild for glew 1.13

* Fri Dec 18 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 8.3.0-1
- 8.3.0

* Thu Dec 03 2015 Adam Jackson <ajax@redhat.com> 8.2.0-5
- New git snap
- Add EGL/GLES buildreqs and egl-utils subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 8.2.0-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 05 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 8.2.0-1
- 8.2.0 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 17 2013 Dave Airlie <airlied@redhat.com> - 8.1.0-5
- rebuilt for glew 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Adam Jackson <ajax@redhat.com> 8.1.0-3
- Build with --as-needed so glxinfo doesn't needlessly drag in GLEW

* Wed Feb 27 2013 Adam Jackson <ajax@redhat.com> 8.1.0-2
- Copy glxinfo to glxinfo%%{__isa_bits}, to allow people to check that their
  compatibility drivers are working.

* Sun Feb 24 2013 Dave Airlie <airlied@redhat.com> 8.1.0-1
- package upstream demos release 8.1.0 (mainly for new glxinfo)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.1-2.20121218git6eef979
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Tom Callaway <spot@fedoraproject.org> - 8.0.1-1.20121218git6eef979
- update to 8.0.1 (git checkout from 20121218)
- update xdriinfo to 1.0.4
- remove non-free files (bz892925)

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 7.10-9.20101028
- Rebuild for glew 1.9.0

* Fri Jul 27 2012 Kalev Lember <kalevlember@gmail.com> - 7.10-8.20101028
- Rebuilt for GLEW soname bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.10-7.20101028
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.10-6.20101028
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 ajax@redhat.com - 7.10-5.20101028
- Rebuild for new glew soname

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.10-4.20101028
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Adam Jackson <ajax@redhat.com> 7.10-3.20101028
- Install rgba images too (#640688)

* Sat Oct 30 2010 Dave Airlie <airlied@redhat.com> 7.10-2.20101028
- fix install of gears/info (#647947)

* Thu Oct 28 2010 Adam Jackson <ajax@redhat.com> 7.10-1.20101028
- Today's git snapshot
- Arbitrary EVR bump to be newer than when the mesa source package dropped
  the demos subpackage.

* Tue Jun 15 2010 Jerome Glisse <jglisse@redhat.com> 7.7
- Initial build.
