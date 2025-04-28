Name:           raylib
Version:        5.5
Release:        %autorelease
Summary:        A simple and easy-to-use library to enjoy videogames programming

License:        Zlib AND MIT
URL:            https://github.com/raysan5/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: mesa-libGL-devel
BuildRequires: wayland-devel
BuildRequires: libxkbcommon-devel
BuildRequires: wayland-protocols-devel
# raylib ships an in-tree glfw that is a copy of *a* git revision of upstream glfw
# containing features they need. They are unhappy that it takes such
# a long time for 3.4 to be released. So ship it.
#BuildRequires: glfw-devel >= 3.4


%description
raylib is a simple and easy-to-use library to enjoy videogames programming.

raylib is highly inspired by Borland BGI graphics lib and by XNA framework and
it's especially well suited for prototyping, tooling, graphical applications,
embedded systems and education.

NOTE for ADVENTURERS: raylib is a programming library to enjoy videogames
                      programming; no fancy interface, no visual helpers,
                      no debug button
                      ...just coding in the most pure spartan-programmers way.

Ready to learn? Jump to https://www.raylib.com/examples.html


# Devel subapackage
%package devel
Summary: Devel files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires: libXcursor-devel
Requires: libXi-devel
Requires: libXinerama-devel
Requires: libXrandr-devel
Requires: mesa-libGL-devel
Requires: wayland-devel
Requires: libxkbcommon-devel
Requires: wayland-protocols-devel


%description devel
The %{name}-devel package contains header files for developing with %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -DBUILD_EXAMPLES=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DUSE_EXTERNAL_GLFW=OFF \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DUSE_WAYLAND=ON \
    -DBUILD_EXAMPLES=ON \
    -DPLATFORM=Desktop

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%doc CHANGELOG
%doc FAQ.md
%doc HISTORY.md
%{_libdir}/libraylib.so.5.5.0
%{_libdir}/libraylib.so.550

%files devel
%doc BINDINGS.md
%doc CONTRIBUTING.md
%doc CONVENTIONS.md
%doc ROADMAP.md
%{_includedir}/%{name}.h
%{_includedir}/rlgl.h
%{_includedir}/raymath.h
%{_libdir}/libraylib.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/raylib/


%changelog
%autochangelog
