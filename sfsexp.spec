Name:		sfsexp
%global libname	libsexp
Version:	1.4.1
%global soname	1
%global sominor	0.0
Release:	%autorelease
Summary:	Small Fast S-Expression Library

License:	LGPL-2.1-or-later
URL:		https://github.com/mjsottile/sfsexp
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
Buildrequires:	perl-interpreter

%description
This library is intended for developers who wish to manipulate (read,
parse, modify, and create) symbolic expressions (s-expressions)from C
or C++ programs.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%configure --disable-static
%make_build

%check
pushd tests
/bin/sh dotests.sh
popd

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING LICENSE_LGPL
%{_libdir}/%{libname}.so.%{soname}
%{_libdir}/%{libname}.so.%{soname}.%{sominor}

%files devel
%doc README*
%{_includedir}/%{name}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
