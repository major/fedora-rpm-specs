# Whether to package the compatibility .so from the previous release.
# This installs self as a build dependency and copies the files.
# Once disabled, it can only be built when the previous version is tagged in.
# It is required to be able to rebuild Pythons with the new library.
%bcond compat 0

Name:           mpdecimal
Version:        4.0.0
Release:        %autorelease
Summary:        Library for general decimal arithmetic
License:        BSD-2-Clause

URL:            https://www.bytereef.org/mpdecimal/index.html
Source0:        https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-%{version}.tar.gz
Source1:        https://speleotrove.com/decimal/dectest.zip

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  unzip
%if %{with compat}
BuildRequires:  %{name}
%endif

%description
The package contains a library libmpdec implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package -n %{name}++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Library for general decimal arithmetic (C++)

%description -n %{name}++
The package contains a library libmpdec++ implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}++%{?_isa} = %{version}-%{release}
Summary:        Development headers for mpdecimal library

%description devel
The package contains development headers for the mpdecimal library.

%prep
%autosetup
unzip -d tests/testdata %{SOURCE1}

%build
%configure --disable-static
# Set LDXXFLAGS to properly pass the buildroot
# linker flags to the C++ extension.
%make_build LDXXFLAGS="%{build_ldflags}"

%check
%make_build check

%install
%make_install

# license will go into dedicated directory
rm %{buildroot}%{_docdir}/%{name}/COPYRIGHT.txt

%if %{with compat}
cp -a %{_libdir}/libmpdec.so.2.5.1 %{buildroot}%{_libdir}/libmpdec.so.3
%endif

%files
%doc README.txt CHANGELOG.txt
%license COPYRIGHT.txt
%{_libdir}/libmpdec.so.%{version}
%{_libdir}/libmpdec.so.4
%if %{with compat}
%{_libdir}/libmpdec.so.3
%endif

%files -n %{name}++
%{_libdir}/libmpdec++.so.%{version}
%{_libdir}/libmpdec++.so.4

%files devel
%{_libdir}/libmpdec.so
%{_libdir}/libmpdec++.so
%{_includedir}/mpdecimal.h
%{_includedir}/decimal.hh
%{_libdir}/pkgconfig/libmpdec.pc
%{_libdir}/pkgconfig/libmpdec++.pc
%{_mandir}/man3/libmpdec.3*
%{_mandir}/man3/libmpdec++.3*
%{_mandir}/man3/mpdecimal*.3*

%changelog
%autochangelog
