Name:          waffle
Version:       1.8.3
Release:       %autorelease
Summary:       Platform independent GL API layer

License:       MIT
URL:           http://www.waffle-gl.org/releases.html
Source0:       https://gitlab.freedesktop.org/mesa/waffle/-/archive/v%{version}/waffle-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxslt
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

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
%{name}-related software (man pages are in the -devel package).


%package examples
Summary:    Example programs using %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description examples
Example programs using %{name}.


%prep
%autosetup -p1
ln -sf waffle-1.5.0.txt doc/release-notes/waffle-1.5.0-rc2.txt


%build
%meson -Dbuild-manpages=true
%meson_build


%install
%meson_install
# Fedora now uses unversioned doc dirs, make install shouldn't try to
# install there anyway.
rm -rf %{buildroot}%{_docdir}/%{name}*


%check
%meson_test


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/wflinfo
%{_libdir}/lib%{name}-1.so.0*
%{_datadir}/bash-completion/completions/wflinfo
%{_datadir}/zsh/site-functions/_wflinfo
%{_mandir}/man1/wflinfo.1*

%files doc
%doc doc/html/

%files devel
%doc doc/release-notes/
%{_includedir}/waffle-1/
%{_libdir}/lib%{name}-1.so
%{_libdir}/pkgconfig/%{name}-1.pc
%{_libdir}/cmake/Waffle/
%{_mandir}/man3/waffle*.3*
%{_mandir}/man7/waffle*.7*


%files examples
%doc examples/


%changelog
%autochangelog
