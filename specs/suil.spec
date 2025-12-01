%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:       suil
Version:    0.10.24
Release:    %autorelease
Summary:    A lightweight C library for loading and wrapping LV2 plugin UIs

License:    ISC
URL:        https://drobilla.net/software/%{name}
Source0:    https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gnupg2
BuildRequires:  lv2-devel >= 1.18.3
BuildRequires:  meson >= 0.56
# We need to track changes to these toolkits manually due to the
# required filtering below.
BuildRequires:  gtk2-devel >= 2.18.0
BuildRequires:  gtk3-devel >= 3.14.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core) >= 5.1.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.1.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.1.0
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme
BuildRequires:  python-sphinxygen

# Lets not necessarily pull in toolkits dependencies. They will be provided by
# the host and/or the plugin.
%define __requires_exclude ^lib.*$

%description
%{name} makes it possible to load a UI of any toolkit in a host using any other
toolkit (assuming the toolkits are both supported by %{name}). Hosts do not need
to build against or link to foreign toolkit libraries to use UIs written with
that toolkit (%{name} performs its magic at runtime using dynamically
loaded modules).

%package devel
Summary:    Development libraries and headers for %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
This package contains the headers and development libraries for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson -Dcocoa=disabled -Dsinglehtml=disabled
%meson_build

%install
%meson_install
install -d "%{buildroot}%{_pkgdocdir}"
mv -f "%{buildroot}%{_docdir}/%{name}-%{maj}" "%{buildroot}%{_pkgdocdir}/"

%files
%doc AUTHORS NEWS README.md
%exclude %{_pkgdocdir}/%{name}-%{maj}
%license COPYING
%dir %{_libdir}/%{name}-%{maj}
%{_libdir}/lib%{name}-*.so.%{maj}*
%{_libdir}/%{name}-%{maj}/lib%{name}_x11_in_gtk2.so
%{_libdir}/%{name}-%{maj}/lib%{name}_x11_in_qt5.so
%{_libdir}/%{name}-%{maj}/lib%{name}_x11.so
%{_libdir}/%{name}-%{maj}/lib%{name}_x11_in_gtk3.so
%{_libdir}/%{name}-%{maj}/lib%{name}_x11_in_qt6.so

%files devel
%{_libdir}/lib%{name}-%{maj}.so
%{_libdir}/pkgconfig/%{name}-%{maj}.pc
%{_includedir}/%{name}-%{maj}/
%{_pkgdocdir}/%{name}-%{maj}

%changelog
%autochangelog
