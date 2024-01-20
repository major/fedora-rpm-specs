%global abi_ver 0
# Test suite currently fails with
#     For xge event (131, 27): Expected (null), got GesturePinchBegin
#     For xcb xge wire event 27: Expected (null), got GesturePinchBegin
# I don't expect that to be fixed.
%bcond_with     check

Name:           xcb-util-errors
Version:        1.0.1
Release:        %autorelease
Summary:        XCB utility library that gives readable names to error, event, & request codes

License:        X11
URL:            http://xcb.freedesktop.org
Source0:        %{url}/dist/%{name}-%{version}.tar.xz
Source1:        %{url}/dist/%{name}-%{version}.tar.xz.sig
# Alan Coopersmith <alan.coopersmith@oracle.com>
Source2:        gpgkey-A2FB9E081F2D130E.gpg

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.16.0
%if %{with check}
BuildRequires:  /usr/bin/xvfb-run
%endif

%description
xcb-util-errors is a utility library that gives human readable names to error
codes and event codes and also to major and minor numbers. The necessary
information is drawn from xcb-proto's protocol descriptions.
This library is especially useful when working with extensions and is mostly
useful for debugging.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
autoreconf -fiv
%configure --disable-static
%make_build


%install
%make_install
# Remove libtool archives on RHEL 9
find %{buildroot}%{_libdir} -name '*.la' -delete

%if %{with check}
%check
xvfb-run %make_build check
%endif


%files
%license COPYING
%{_libdir}/libxcb-errors.so.%{abi_ver}{,.*}

%files devel
%{_includedir}/xcb/xcb_errors.h
%{_libdir}/libxcb-errors.so
%{_libdir}/pkgconfig/xcb-errors.pc

%changelog
%autochangelog
