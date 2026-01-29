%global abi_ver 0

Name:           libnsbmp
Version:        0.1.7
Release:        %autorelease
Summary:        Decoding library for BMP and ICO image file formats
License:        MIT
URL:            http://www.netsurf-browser.org/projects/libnsbmp/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  netsurf-buildsystem

%description
Libnsbmp is a decoding library for BMP and ICO image file formats written in
C. It was developed as part of the NetSurf project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%global make_vars %{shrink:
    COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q=
    OPTCFLAGS='' OPTLDFLAGS=''
}

%prep
%autosetup -p1
sed -i -e s@-Werror@@ Makefile

%build
%make_build %{make_vars}

%install
%make_install %{make_vars}

%check
%make_build test %{make_vars}

%files
%license COPYING
%{_libdir}/%{name}.so.%{abi_ver}{,.*}

%files devel
%doc src/README
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
