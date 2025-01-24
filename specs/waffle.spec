Name:          waffle
Version:       1.8.0
Release:       %autorelease
Summary:       Platform independent GL API layer

License:       MIT
URL:           http://www.waffle-gl.org/releases.html
Source0:       https://gitlab.freedesktop.org/mesa/waffle/-/archive/v%{version}/waffle-%{version}.tar.bz2

Patch0:        0001-wayland-fix-build-against-version-1.20.patch
Patch1:        fix-bash.patch

BuildRequires: cmake libxslt docbook-style-xsl libxcb-devel
BuildRequires: gcc-c++
BuildRequires: libX11-devel mesa-libGL-devel mesa-libGLU-devel
BuildRequires: chrpath
BuildRequires: mesa-libEGL-devel
%if 0%{?rhel} > 6 || 0%{?fedora} > 0
BuildRequires: mesa-libGLES-devel
BuildRequires: systemd-devel
%endif
BuildRequires: mesa-libgbm-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
Waffle is a cross-platform C library that allows one to defer
selection of GL API and of window system until runtime.


%package devel
Summary:    Development headers and libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains the header files, and libraries required for development of
%{name}-related software.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description doc
Contains HTML version of the developer documentation for development of
%{name}-related software (manpages are in the -devel package).


%package examples
Summary:    Example programs using %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description examples
Example programs using %{name}.


%prep
%autosetup -n waffle-v1.7.0-905c6c10f2483adf0cbfa024e2d3c2ed541fb300 -p1


%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_defaultdocdir}/%{name}-%{version} \
    -DCMAKE_BUILD_STRIP=FALSE \
    -Dwaffle_has_glx=1 -Dwaffle_has_gbm=1 \
    -Dwaffle_has_wayland=1 \
    -Dwaffle_build_manpages=1 -Dwaffle_build_htmldocs=1

%cmake_build

# We don’t want to install binary files in %%docdir
rm -rf examples/CMakeFiles

%install
%cmake_install
# Fedora now uses unversioned doc dirs, make install shouldn’t try to
# install there anyway.
rm -rf %{buildroot}%{_docdir}/%{name}*

%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}*.so.*
%{_bindir}/wflinfo
%{_datadir}/bash-completion/completions/wflinfo

%files doc
%doc doc/html/

%files devel
%doc doc/release-notes/
%{_includedir}/waffle*
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}*
%{_libdir}/cmake/Waffle/*
%{_mandir}/man*/*


%files examples
%doc examples/


%changelog
%autochangelog
