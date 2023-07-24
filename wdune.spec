Summary:       A graphical X3D/VRML97 editor, simple 3D modeler and animation tool
Name:          wdune
Version:       1.958
Release:       12%{?dist}
License:       GPLv2+ and GPLv3+ and LGPLv3+ and BSD and Public Domain and ASL 2.0
URL:           http://wdune.ourproject.org/
Source:        ftp://ftp.ourproject.org/pub/wdune/wdune-%{version}.tar.bz2

BuildRequires: aqsis-core
BuildRequires: bash
BuildRequires: bison
BuildRequires: flex
BuildRequires: gawk
BuildRequires: gcc-c++
BuildRequires: grep
BuildRequires: ImageMagick
BuildRequires: make
BuildRequires: pkg-config
BuildRequires: xdg-utils

BuildRequires: bitstream-vera-sans-fonts
BuildRequires: CGAL-devel
BuildRequires: desktop-file-utils
BuildRequires: freeglut-devel
BuildRequires: freetype-devel 
BuildRequires: expat-devel
BuildRequires: gmp-devel
BuildRequires: motif-devel
BuildRequires: libcurl-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libXi-devel
BuildRequires: libusb-compat-0.1-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: opensubdiv-devel
BuildRequires: pkgconfig(eigen3)
#BuildRequires: pkgconfig(vcglib)

Requires:      aqsis-core
Requires:      bash
Requires:      bitstream-vera-sans-fonts
Requires:      gawk
Requires:      gedit
Requires:      git
Requires:      ImageMagick
Requires:      kdialog
Requires:      povray
Requires:      xorg-x11-fonts-misc

Recommends:    audacity
Recommends:    lxterminal
Recommends:    kolourpaint
Recommends:    vim

%description
The white_dune program is a graphical X3D/VRML97 editor, 
simple extrusion/NURBS/Superformula 3D modeler and animation tool.
With white_dune you can create/change 3D objects and animate them (in a easy 
way if you choose the -4kids GUI). The result can be shown in any WebGL enabled 
web browser or can be converted to the RIB format for movie creation. 
X3D and VRML97 are the ISO standard for displaying 3D data over the web. 
With Cobweb or X3DOM it can displayed in any WebGL enabled web browser. 

Under Linux, white_dune support some 3D input-devices like joysticks, game-pads
or all devices supported via the Xinput protocol.
White_dune support quad-buffer stereo visuals. Under Linux, this can be used
with Elsa Revelator, Crystal Eyes or Nvidia 3D Vision shutter-glasses and 
special drivers for expensive graphic-cards like Nvidia Quadro or ATI FireGL 4.

%package devel
License: BSD and MIT
Summary: Develop files for white_dune
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: freeglut%{?_isa}

%description devel
Develop files for white_dune

%package opengl-examples
License: BSD and MIT
Summary: Compiled OpenGL examples for white_dune
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: freeglut%{?_isa}

%description opengl-examples
Compiled OpenGL examples for white_dune

%package docs
License: GPLv2+ and BSD and MIT
Summary: Documentation for white_dune
Requires: %{name}%{?_isa} = %{version}-%{release}

%description docs
Documentation for white_dune

%prep
%setup -q -n "wdune-%{version}"

%build
./configure \
    --with-about="white_dune-%{version}" \
    --with-optimization \
    --without-devil \
    --without-ffmpeg \
    --with-helpurl="%{_docdir}/wdune-docs/docs/" \
    --with-protobaseurl="%{_docdir}/wdune-docs/docs" \
    --with-checkincommand="ci" \
    --with-x11-editor="gedit" \
    --with-imageeditor="kolourpaint" \
    --with-imageeditor4kids="kolourpaint" \
    --with-soundeditor=audacity \
    --with-cgalheaders \
    --with-allow-multiple-definition

CXXFLAGS=" -Wno-ignored-attributes -Wnonnull-compare -Wmaybe-uninitialized"
%make_build 
pushd docs/export_example_c++/opengl_example
%make_build render_with_picture_path
popd
pushd warbird
%make_build warbird_with_picture_path
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/white_dune
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/white_dune/opengl_example
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/white_dune/shaders

install -m 755 -p bin/dune $RPM_BUILD_ROOT/%{_bindir}/dune
install -m 755 -p bin/dune4kids $RPM_BUILD_ROOT/%{_bindir}/dune4kids
install -m 755 -p bin/gitview.sh $RPM_BUILD_ROOT/%{_bindir}/gitview.sh
install -m 644 -p tools/phong.slx $RPM_BUILD_ROOT/%{_datadir}/white_dune/shaders/phong.slx
install -m 755 -p tools/run_dune_and_aqsis.sh $RPM_BUILD_ROOT/usr/bin/run_dune_and_aqsis.sh
install -m 755 -p tools/run_dune_and_povray.sh $RPM_BUILD_ROOT/usr/bin/run_dune_and_povray.sh
install -m 755 -p bin/illegal2vrml $RPM_BUILD_ROOT/%{_bindir}/illegal2vrml
install -m 644 -p desktop/kde/dune.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/dune.desktop
install -m 644 -p desktop/kde/dune.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/dune.png
install -m 644 -p desktop/kde/dune4kids.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/dune4kids.desktop
install -m 644 -p desktop/kde/dune4kids.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/dune4kids.png
install -m 644 -p man/dune.1 $RPM_BUILD_ROOT/%{_mandir}/man1/dune.1
install -m 644 -p man/dune4kids.1 $RPM_BUILD_ROOT/%{_mandir}/man1/dune4kids.1
install -m 644 -p man/illegal2vrml.1 $RPM_BUILD_ROOT/%{_mandir}/man1/illegal2vrml.1
install -m 644 -p man/gitview.1 $RPM_BUILD_ROOT/%{_mandir}/man1/gitview.1
install -m 644 -p include/white_dune/libC++RWD.h $RPM_BUILD_ROOT/%{_includedir}/white_dune/libC++RWD.h
install -m 644 -p include/white_dune/libCRWD.h $RPM_BUILD_ROOT/%{_includedir}/white_dune/libCRWD.h
install -m 644 -p include/white_dune/libC++RWD_namespace.h $RPM_BUILD_ROOT/%{_includedir}/white_dune/libC++RWD_namespace.h
install -m 755 -p warbird/warbird_with_picture_path $RPM_BUILD_ROOT/%{_bindir}/warbird
install -m 644 -p warbird/warbird.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/warbird.desktop
install -m 644 -p warbird/warbird.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/warbird.png
install -m 755 -p docs/export_example_c++/opengl_example/render_with_picture_path $RPM_BUILD_ROOT/%{_bindir}/white_dune_opengl_example
install -m 644 -p warbird/cake.png $RPM_BUILD_ROOT/%{_datadir}/white_dune/opengl_example/cake.png
install -m 644 -p warbird/bill.jpg $RPM_BUILD_ROOT/%{_datadir}/white_dune/opengl_example/bill.jpg
# remove binary from noarch package
rm docs/export_example_c++/opengl_example/render_with_picture_path 
# remove big C++ file from opengl-examples package (can be restored using white_dune)
rm docs/export_example_c++/opengl_example/C++Export.cc
cp -r docs/export_example_c++/opengl_example/* $RPM_BUILD_ROOT/%{_datadir}/white_dune/opengl_example

# install desktop files
desktop-file-install                                    \
  --add-category="Graphics"                             \
  --delete-original                                     \
  --dir=$RPM_BUILD_ROOT/%{_datadir}/applications        \
  $RPM_BUILD_ROOT/%{_datadir}/applications/dune.desktop

desktop-file-install                                         \
  --add-category="Graphics"                                  \
  --delete-original                                          \
  --dir=$RPM_BUILD_ROOT/%{_datadir}/applications             \
  $RPM_BUILD_ROOT/%{_datadir}/applications/dune4kids.desktop

%files
%license COPYING
%{_bindir}/dune
%{_bindir}/dune4kids
%{_bindir}/gitview.sh
%{_bindir}/run_dune_and_aqsis.sh
%{_bindir}/run_dune_and_povray.sh
%{_bindir}/illegal2vrml
%{_datadir}/applications/dune.desktop
%{_datadir}/applications/dune4kids.desktop
%{_datadir}/pixmaps/dune.png
%{_datadir}/pixmaps/dune4kids.png
%{_datadir}/white_dune/shaders/phong.slx
%{_mandir}/man1/dune.1*
%{_mandir}/man1/dune4kids.1*
%{_mandir}/man1/illegal2vrml.1*
%{_mandir}/man1/gitview.1*

%files devel
%{_includedir}/white_dune/libC++RWD.h
%{_includedir}/white_dune/libCRWD.h
%{_includedir}/white_dune/libC++RWD_namespace.h

%files opengl-examples
%{_bindir}/warbird
%{_bindir}/white_dune_opengl_example
%{_datadir}/applications/warbird.desktop
%{_datadir}/pixmaps/warbird.png
%dir %{_datadir}/white_dune/
%dir %{_datadir}/white_dune/opengl_example/
%{_datadir}/white_dune/opengl_example/fin.png
%{_datadir}/white_dune/opengl_example/fire.png
%{_datadir}/white_dune/opengl_example/Makefile
%{_datadir}/white_dune/opengl_example/README.txt
%{_datadir}/white_dune/opengl_example/README_fedora.txt
%{_datadir}/white_dune/opengl_example/main.cpp
%{_datadir}/white_dune/opengl_example/robot.x3dv
%{_datadir}/white_dune/opengl_example/cake.png
%{_datadir}/white_dune/opengl_example/bill.jpg

%files docs
%license COPYING
%doc README.txt docs

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.958-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Sérgio Basto <sergio@serjux.com> - 1.958-11
- Fix FTI, package already requires opensubdiv-libs by auto requires
  libosdCPU.so.3.5.0()(64bit)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.958-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.958-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.958-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.958-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Andy Mender <andymenderunix@fedoraproject.org> - 1.958-6
- Add missing Requires on opensubdiv-libs

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.958-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 5 2020 Andy Mender <andymenderunix@fedoraproject.org> - 1.958-4
- Clean up SPEC file

* Thu Sep  3 16:45:22 CEST 2020 J. Scheurich <mufti11@web.de> - 1.958-3
- Initial RPM release


