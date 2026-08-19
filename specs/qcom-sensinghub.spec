%global prj_name sensinghub

Name:		qcom-sensinghub
Version:	2.2.3
Release:	%autorelease
Summary:	Qualcomm sensing-hub API library

License:	BSD-3-Clause
URL:		https://github.com/qualcomm/sensinghub
Source:		%{url}/archive/v%{version}/%{prj_name}-%{version}.tar.gz

# https://github.com/qualcomm/sensinghub/pull/54
Patch0:		54.patch

ExclusiveArch:	%{arm64}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	nanopb-devel
BuildRequires:	nanopb-python3

%description
Qualcomm Sensing Hub (QSH) is an always-on, low-power interface designed to
collect, process, and combine sensor and contextual data. It offers stable APIs
that enable applications and services to interact with the hub efficiently,
reducing the need for frequent application processor wake ups.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup -p1 -n %{prj_name}-%{version}

%conf
autoreconf -fiv
%configure CFLAGS="%{build_cflags} -I/usr/include/nanopb" \
	CXXFLAGS="%{build_cxxflags} -I/usr/include/nanopb"

%build
%make_build LDFLAGS="%{build_ldflags} -lprotobuf-nanopb"

%install
%make_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/SessionClient
%{_libdir}/libqshUtil.so.*
%{_libdir}/libsensinghubapi-c.so.*
%{_libdir}/libsensinghubapi.so.*
%{_libdir}/libsensinghublogger.so.*
%{_libdir}/libsensinghubsession.so.*

%files devel
%{_includedir}/%{prj_name}
%{_libdir}/libqshUtil.so
%{_libdir}/libsensinghubapi-c.so
%{_libdir}/libsensinghubapi.so
%{_libdir}/libsensinghublogger.so
%{_libdir}/libsensinghubsession.so
%{_libdir}/pkgconfig/sensinghub.pc
%{_libdir}/pkgconfig/sensinghub-cpp.pc
%{_datadir}/%{prj_name}

%changelog
%autochangelog
