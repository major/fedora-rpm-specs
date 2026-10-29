# these features are disabled by default
%bcond opengl 0
# not all arches support quadmath
%ifarch x86_64 ppc64le
%bcond quadmath 0
%endif

Name:           xaos
Version:        4.3.8
Release:        %autorelease
Summary:        A fast, portable real-time interactive fractal zoomer
License:        GPL-2.0-or-later
URL:            https://xaos-project.github.io/
VCS:            https://github.com/xaos-project/XaoS
Source:         %{vcs}/archive/release-%{version}/XaoS-release-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
%if %{with opengl}
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(glut)
%endif
%if %{with quadmath}
BuildRequires:  libquadmath-devel
%endif


%description
XaoS is a fast, portable real-time interactive fractal zoomer. It
displays the Mandelbrot set (among other escape time fractals) and
allows you zoom smoothly into the fractal. Various coloring modes are
provided for both the points inside and outside the selected set. XaoS
supports switching between Julia and Mandelbrot fractal types and
on-the-fly plane switching.


%prep
%autosetup -p1 -n XaoS-release-%{version}
# fix DATAPATH for variable prefix (e.g. flatpaks)
sed -i -e 's|/usr/share|%{_datadir}|' src/include/config.h


%build
%cmake \
  -DDEEPZOOM=%{?with_quadmath:ON}%{!?with_quadmath:OFF} \
  -DOPENGL=%{?with_opengl:ON}%{!?with_opengl:OFF} \
  -DMOBILE_UI=OFF
%cmake_build


%install
%cmake_install

# Data; Datapath forced to XaoS (not configurable)
mkdir -p %{buildroot}%{_datadir}/XaoS
mv %{buildroot}%{_prefix}/{catalogs,examples,tutorial} %{buildroot}%{_datadir}/XaoS/

# Icon, .desktop, AppData
install -D --mode 0644 --target-directory %{buildroot}%{_metainfodir} xdg/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
  --set-key=Exec --set-value=XaoS \
  xdg/io.github.xaos_project.XaoS.desktop
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/icons/hicolor/256x256/apps xdg/%{name}.png

# Man
install -D --mode 0644 --target-directory %{buildroot}%{_mandir}/man6 doc/%{name}.6


%files
%doc CREDITS.md NEWS doc/README
%license COPYING
%{_bindir}/XaoS
%{_datadir}/XaoS/
%{_datadir}/applications/io.github.xaos_project.XaoS.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_mandir}/man6/xaos.6.gz
%{_metainfodir}/%{name}.appdata.xml


%changelog
%autochangelog
