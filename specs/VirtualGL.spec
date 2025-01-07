Name:           VirtualGL
Version:        3.1.2
Release:        1%{?dist}
Summary:        A toolkit for displaying OpenGL applications to thin clients

# Automatically converted from old format: wxWindows - review is highly recommended.
License:        LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            https://www.virtualgl.org
Source0:        https://github.com/VirtualGL/virtualgl/archive/%{version}/VirtualGL-%{version}.tar.gz
# fix for bz923961
Patch1:         %{name}-redhatpathsfix.patch
# fix for bz1088475
Patch2:         %{name}-redhatlibexecpathsfix.patch
# Do not rely on hostname package
Patch4:         %{name}-hostname.patch

%if 0%{?rhel} == 7
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  fltk-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig
# no need OpenCL-Headers, ocl-icd seems enough
#BuildRequires:  pkgconfig(OpenCL-Headers)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
%if 0%{?fedora:1} || 0%{?rhel} <= 7
BuildRequires:  fltk-fluid
%endif
Requires:       fltk
Provides:       bumblebee-bridge

%description
VirtualGL is a toolkit that allows most Unix/Linux OpenGL applications to be
remotely displayed with hardware 3D acceleration to thin clients, regardless
of whether the clients have 3D capabilities, and regardless of the size of the
3D data being rendered or the speed of the network.

Using the vglrun script, the VirtualGL "faker" is loaded into an OpenGL
application at run time.  The faker then intercepts a handful of GLX calls,
which it reroutes to the server's X display (the "3D X Server", which
presumably has a 3D accelerator attached.)  The GLX commands are also
dynamically modified such that all rendering is redirected into a Pbuffer
instead of a window.  As each frame is rendered by the application, the faker
reads back the pixels from the 3D accelerator and sends them to the
"2D X Server" for compositing into the appropriate X Window.

VirtualGL can be used to give hardware-accelerated 3D capabilities to VNC or
other X proxies that either lack OpenGL support or provide it through software
rendering.  In a LAN environment, VGL can also be used with its built-in
high-performance image transport, which sends the rendered 3D images to a
remote client (vglclient) for compositing on a remote X server.  VirtualGL
also supports image transport plugins, allowing the rendered 3D images to be
sent or captured using other mechanisms.

VirtualGL is based upon ideas presented in various academic papers on
this topic, including "A Generic Solution for Hardware-Accelerated Remote
Visualization" (Stegmaier, Magallon, Ertl 2002) and "A Framework for
Interactive Hardware Accelerated Remote 3D-Visualization" (Engel, Sommer,
Ertl 2000.)

%package devel
Summary:    Development headers and libraries for VirtualGL
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   turbojpeg-devel%{?_isa}
Requires:   mesa-libGLU-devel%{?_isa}
Requires:   libXv-devel%{?_isa}

%description devel
Development headers and libraries for VirtualGL.

%prep
%autosetup -p1

#sed -i -e 's,"glx.h",<GL/glx.h>,' server/*.[hc]*
# Remove bundled libraries
rm -r server/fltk

%build
%if 0%{?rhel} == 7
cmake3 \
%else
%cmake \
%endif
         -DVGL_SYSTEMFLTK=1 \
         -DVGL_FAKEXCB=1 \
         -DVGL_BUILDSTATIC=0 \
         -DVGL_FAKEOPENCL=1 \
         -DVGL_BUILDSERVER=1 \
         -DVGL_USEXV=1 \
         -DTJPEG_INCLUDE_DIR=%{_includedir} \
         -DTJPEG_LIBRARY=%{_libdir}/libturbojpeg.so \
         -DCMAKE_INSTALL_PREFIX=%{_prefix} \
         -DCMAKE_INSTALL_LIBDIR=%{_libdir}/VirtualGL \
         -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
         -DCMAKE_INSTALL_BINDIR=%{_bindir} \
         -DCMAKE_LIBRARY_PATH=%{_libdir}

%if 0%{?rhel} == 7
make %{?_smp_mflags}
%else
%cmake_build
%endif

%install
%if 0%{?rhel} == 7
make install DESTDIR=$RPM_BUILD_ROOT
%else
%cmake_install
%endif
# glxinfo conflicts with command from glx-utils so lets do what Arch does
# and rename the command
mv %{buildroot}/%{_bindir}/glxinfo %{buildroot}/%{_bindir}/vglxinfo
# eglinfo conflics with the command from egl-utils, rename eglinfo to veglinfo
mv %{buildroot}/%{_bindir}/eglinfo %{buildroot}/%{_bindir}/veglinfo

mkdir -p %{buildroot}%{_libdir}/fakelib/
ln -rsf %{_libdir}/VirtualGL/librrfaker.so %{buildroot}%{_libdir}/fakelib/libGL.so
# fix for bz1088475
mkdir %{buildroot}%{_libexecdir}
%if 0%{?__isa_bits} == 64
mv %{buildroot}%{_bindir}/.vglrun.vars64 %{buildroot}%{_libexecdir}/vglrun.vars64
%else
mv %{buildroot}%{_bindir}/.vglrun.vars32 %{buildroot}%{_libexecdir}/vglrun.vars32
%endif

%ldconfig_scriptlets

%files
%{_docdir}/%{name}/
%{_bindir}/tcbench
%{_bindir}/nettest
%{_bindir}/cpustat
%{_bindir}/veglinfo
%{_bindir}/eglxinfo
%{_bindir}/vglclient
%{_bindir}/vglconfig
%{_bindir}/vglconnect
%{_bindir}/vglgenkey
%{_bindir}/vgllogin
%{_bindir}/vglserver_config
%{_bindir}/vglrun
%{_bindir}/vglxinfo
%{_bindir}/glreadtest
%if 0%{?__isa_bits} == 64
%{_bindir}/eglxspheres64
%{_bindir}/glxspheres64
%{_libexecdir}/vglrun.vars64
%else
%{_bindir}/eglxspheres
%{_bindir}/glxspheres
%{_libexecdir}/vglrun.vars32
%endif
%{_libdir}/VirtualGL/
%{_libdir}/fakelib/

%files devel
%{_includedir}/rrtransport.h
%{_includedir}/rr.h


%changelog
* Mon Jan 06 2025 Packit <hello@packit.dev> - 3.1.2-1
- Update to version 3.1.2

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 22 2024 Sérgio Basto <sergio@serjux.com> - 3.1-3
- Prepare build for epel

* Wed Jun 12 2024 Sérgio Basto <sergio@serjux.com> - 3.1-2
- eglinfo conflics with the command from egl-utils, rename eglinfo to veglinfo

* Sun Jun 09 2024 Sérgio Basto <sergio@serjux.com> - 3.1-1
- Update VirtualGL to 3.1
- Do not rely on hostname package (#1860323)
  (Fri Jul 24 2020 Pavel Zhukov <pavel@pzhukov-pc.home.redhat.com>)

* Tue Feb 06 2024 František Zatloukal <fzatlouk@redhat.com> - 2.6.5-9
- Rebuilt for turbojpeg 3.0.2

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Gary Gatling <gsgatlin@ncsu.edu> - 2.6.5-1
- Update to 2.6.5

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Gary Gatling <gsgatlin@ncsu.edu> - 2.6.3-1
- Update to 2.6.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Gary Gatling <gsgatlin@ncsu.edu> - 2.5.2-1
- Fix (#1566666) Update to 2.5.2
- Fix (#1309831) adding hostname requires on rhel 7 and fedora
- Fix (#1574902) modify VirtualGL-redhatlibexecpathsfix.patch to use -f not -x 

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 08 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4-7
- Fix (#1307302) FTBFS with GCC 6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild


* Fri May 1 2015 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.4-4
- Fix (#1198149) Disable SSL support.
- Fix (#1198135) add -DVGL_FAKEXCB=1 to build options.

* Wed Apr 29 2015 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.4-3
- Fix problems with build on ppc rhel 6.

* Tue Apr 28 2015 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.4-2
- Fix problems in changelog.

* Tue Apr 28 2015 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.4-1
- Fix (#1198135) Update to 2.4.

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 2.3.3-6
- rebuild (fltk,gcc5)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.3-3
- Fix (#1088475) don't install hidden files into /usr/bin

* Thu Nov 7 2013 Dan Horák <dan[at]danny.cz> - 2.3.3-2
- fix build on non-x86 arches

* Sat Nov 2 2013 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.3-1
- Update to 2.3.3.

* Tue Aug 6 2013 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.2-7
- Fix (#993894) unversioned docdir change for f20.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 6 2013 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.2-5
- Fix (#923961) More path changes to vglrun to really fix issue.

* Sun Mar 24 2013 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.2-4
- Fix (#923961) Change /opt/VirtualGL/bin to /usr/bin in vglconnect.
- Add virtual provides for bumblebee-bridge package.

* Wed Feb 20 2013 Adam Tkac <atkac redhat com> - 2.3.2-3
- rebuild

* Thu Jan 17 2013 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.2-1
- rebuilding.

* Sun Jan 13 2013 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.2-2
- update to 2.3.2.

* Tue Oct 23 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-9
- Fix problems with multilib support. Fix created by Andy Kwong.

* Sun Jul 22 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-8
- removed BuildRequires:  mxml-devel. see BZ839060. (#839060)

* Sat Jul 14 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-7
- added BuildRequires:  mxml-devel for fedora builds only.

* Thu Jul 12 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-6
- removed BuildArch: noarch from "devel" subpackage

* Thu Jul 12 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-5
- change to cmake macros in the build section of specfile

* Tue Jul 10 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-4
- fix vglrun patch to use uname -i to determine platform.
- fix cmake macro problems on rhel 6.
- remove Vendor tag from specfile

* Tue Jul 10 2012 Orion Poplawski <orion@nwra.com> - 2.3.1-3
- Use system glx, fltk
- Don't ship glxinfo

* Fri Jul 6 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-2
- Added patch for library paths within the vglrun script.

* Thu Jul 5 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3.1-1
- Upgrade to 2.3.1 and made changes to better follow packaging guidelines for fedora project.

* Wed Jun 6 2012 Gary Gatling <gsgatlin@eos.ncsu.edu> - 2.3-2
- Very minor edit for building on RHEL 6 with the same specfile as newer fedora.

* Thu Feb 16 2012 Robin Lee <cheeselee@fedoraproject.org> - 2.3-1
- Specfile based on upstream and Mandriva specfiles
