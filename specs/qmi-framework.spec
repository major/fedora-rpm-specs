Name:		qmi-framework
Version:	0.1.4
Release:	%autorelease
Summary:	Qualcomm messaging interface

License:	BSD-3-Clause
URL:		https://github.com/qualcomm/qmi-framework
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/qualcomm/qmi-framework/pull/20
Patch0:		20.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libtool

%description
QMI framework provides the Client Common Interface (CCI) library for QMI
communication between applications and remote subsystems.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package	utils
Summary:	%{name} test utilities
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	utils
QMI framework provides sample applications to test QMI communication between
applications and remote subsystems.

%prep
%autosetup -p1

%conf
autoreconf -fiv
%configure

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libqcci.so.*
%{_libdir}/libqcsi.so.*
%{_libdir}/libqmi_common.so.*
%{_libdir}/libqencdec.so.*

%files devel
%{_includedir}/qmi_framework
%{_libdir}/libqcci.so
%{_libdir}/libqcsi.so
%{_libdir}/libqmi_common.so
%{_libdir}/libqencdec.so
%{_libdir}/pkgconfig/%{name}.pc

%files utils
%{_bindir}/qcci_test
%{_bindir}/qcsi_test

%changelog
%autochangelog
