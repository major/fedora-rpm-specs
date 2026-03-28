Name:    startup-notification
Version: 0.12
Release: %autorelease
Summary: Library for tracking application startup

License: LGPL-2.0-or-later AND MIT
URL:     https://www.freedesktop.org/wiki/Software/startup-notification/
Source0: http://www.freedesktop.org/software/startup-notification/releases/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: make
BuildRequires: pkgconfig(xcb-event)

%description
This package contains libstartup-notification which implements a
startup notification protocol. Using this protocol a desktop
environment can track the launch of an application and provide
feedback such as a busy cursor, among other features.

%package devel
Summary: Development portions of startup-notification
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libX11-devel

%description devel
Header files and static libraries for libstartup-notification.

%prep
%autosetup
mkdir examples
cp -p test/*.c test/*.h examples

%build
%configure --disable-static
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%doc doc/startup-notification.txt
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_libdir}/libstartup-notification-1.so.0{,.*}

%files devel
%doc examples 
%{_libdir}/libstartup-notification-1.so
%{_libdir}/pkgconfig/libstartup-notification-1.0.pc
%{_includedir}/startup-notification-1.0/

%changelog
%autochangelog
