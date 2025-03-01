Name:           libXpresent
Version:        1.0.0
Release:        %autorelease
Summary:        A Xlib-compatible API for the Present extension

License:        MIT
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXpresent-%{version}.tar.bz2

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: gettext
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(presentproto)
BuildRequires: pkgconfig(xextproto)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrandr)

%description
This package contains header files and documentation for the Present
extension.  Library and server implementations are separate.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libXpresent.so.1
%{_libdir}/libXpresent.so.1.0.0

%files devel
%{_includedir}/X11/extensions/Xpresent.h
%{_libdir}/libXpresent.so
%{_libdir}/pkgconfig/xpresent.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
