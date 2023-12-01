%global apiversion 0.6

Name: libcmis
Version: 0.6.2
Release: %autorelease
Summary: A C/C++ client library for CM interfaces

License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
URL: https://github.com/tdf/libcmis
Source: https://github.com/tdf/libcmis/releases/download/v%{version}/%{name}-%{version}.tar.xz
# https://github.com/tdf/libcmis/issues/51
Patch:  libxmis-0.6.2-libxml2-2.12.0-includes.patch

BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: xmlto
BuildRequires: make

%description
LibCMIS is a C/C++ client library for working with CM (content management)
interfaces. The primary supported interface (which gave the library its
name) is CMIS, which allows applications to connect to any ECM behaving
as a CMIS server (Alfresco or Nuxeo are examples of open source ones).
Another supported interface is Google Drive.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Command line tool to access CMIS
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains a tool for accessing CMIS from the
command line.

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static --disable-werror \
    DOCBOOK2MAN='xmlto man'
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check

%files
%doc AUTHORS NEWS
%license COPYING.*
%{_libdir}/%{name}-%{apiversion}.so.*
%{_libdir}/%{name}-c-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_includedir}/%{name}-c-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/%{name}-c-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc
%{_libdir}/pkgconfig/%{name}-c-%{apiversion}.pc

%files tools
%{_bindir}/cmis-client
%{_mandir}/man1/cmis-client.1*

%changelog
%autochangelog
