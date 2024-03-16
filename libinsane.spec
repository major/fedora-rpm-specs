Name:           libinsane
Version:        1.0.10
Release:        %autorelease
Summary:        Cross-platform access to image scanners

License:        LGPL-3.0-or-later
URL:            https://doc.openpaper.work/libinsane/latest/
Source0:        https://gitlab.gnome.org/World/OpenPaperwork/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  doxygen
BuildRequires:  pkgconfig(cunit)
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif

%description
Libinsane is the library to access scanners on both Linux and Windows. It's
cross-platform, cross-programming languages, cross-scanners :-). It takes care
of all the quirks of all the platforms and scanners.


%package devel
Summary:        Development files for libinsane

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and header files for libinsane.


%package gobject
Summary:        GObject access to image scanners

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gobject
Libinsane is the library to access scanners on both Linux and Windows. It's
cross-platform, cross-programming languages, cross-scanners :-). It takes care
of all the quirks of all the platforms and scanners.

This package provides GObject wrappers around the main library.


%package gobject-devel
Summary:        Development files for libinsane-gobject

Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-gobject%{?_isa} = %{version}-%{release}

%description gobject-devel
Development libraries and header files for libinsane-gobject.


%package vala
Summary:        Vala bindings for libinsane

BuildArch:      noarch

BuildRequires:  vala

Requires:       %{name}-gobject-devel = %{version}-%{release}

%description vala
Vala bindings for libinsane.


%prep
%autosetup -p1


%build
%meson
%meson_build
%meson_build doc


%install
%meson_install


%check
%meson_test -v -t 10


%files
%doc README.markdown ChangeLog
%license LICENSE
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*

%files devel
%doc doc
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files gobject
%{_libdir}/%{name}_gobject.so.1
%{_libdir}/%{name}_gobject.so.1.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Libinsane-1.0.typelib

%files gobject-devel
%{_includedir}/%{name}-gobject
%{_libdir}/%{name}_gobject.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Libinsane-1.0.gir
%{_datadir}/gtk-doc

%files vala
%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi


%changelog
%autochangelog
