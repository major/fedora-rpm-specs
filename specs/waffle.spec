%global gitver 49abc7cb5f73cc6852136c91da49ea3a338960e4
Name:          waffle
Version:       1.8.1
Release:       %autorelease
Summary:       Platform independent GL API layer

License:       MIT
URL:           http://www.waffle-gl.org/releases.html
Source0:       https://gitlab.freedesktop.org/mesa/waffle/-/archive/v%{version}/waffle-%{version}.tar.bz2

BuildRequires: meson ninja-build
BuildRequires: libxslt docbook-style-xsl libxcb-devel
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
%autosetup -n waffle-v%{version}-%{gitver} -p1


%build
%meson
%meson_build

%install
%meson_install
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
%{_datadir}/zsh/site-functions/_wflinfo

%files doc
%doc doc/html/

%files devel
%doc doc/release-notes/
%{_includedir}/waffle*
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}*
#{_mandir}/man*/*


%files examples
%doc examples/


%changelog
%autochangelog
