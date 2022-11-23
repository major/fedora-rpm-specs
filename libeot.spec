Name: libeot
Version: 0.01
Release: %autorelease
Summary: A library for parsing Embedded OpenType font files

License: MPL-2.0
URL: https://github.com/umanwizard/libeot
Source: http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: make

%description
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tools to transform EOT font files into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform EOT font files into other formats. Only TTF is
supported currently.

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc PATENTS
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/eot2ttf

%changelog
%autochangelog
