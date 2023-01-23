Name:		sfsexp
%global libname	libsexp
Version:	1.4.0
%global soname	1
%global sominor	0.0
Release:	5%{?dist}
Summary:	Small Fast S-Expression Library

License:	LGPL-2.1-or-later
URL:		https://github.com/mjsottile/sfsexp
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# included in the repo but not the distribution archive (until a new release is
# cut containing https://github.com/mjsottile/sfsexp/pull/20) :
Source1:	LICENSE_LGPL

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
cp -p %{SOURCE1} .

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
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.4.0-4
- SPDX migration

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.4.0-2
- take into account review issues

* Fri Jun 10 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.4.0-1
- rebase with upstream 1.4.0

* Wed Jan 12 2022 Michael J Gruber <mjg@fedoraproject.org> - 1.3.1-1
- initial test package
