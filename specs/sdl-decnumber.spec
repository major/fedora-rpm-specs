%global srcname decNumber
%global date 20250324
%global commit 995184583107625015bb450228a5f3fb781d9502
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
The decNumber library implements the General Decimal Arithmetic Specification
in ANSI C. This specification defines a decimal arithmetic which meets the
requirements of commercial, financial, and human-oriented applications. It
also matches the decimal arithmetic in the IEEE 754 Standard for Floating
Point Arithmetic.

The library fully implements the specification, and hence supports integer,
fixed-point, and floating-point decimal numbers directly, including infinite,
NaN (Not a Number), and subnormal values. Both arbitrary-precision and
fixed-size representations are supported.

This version is a fork by SoftDevLabs (SDL) to support the SDL-Hercules-390
emulator.}

Name:           sdl-decnumber
Version:        3.68.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        ANSI C General Decimal Arithmetic Library (SDL version)

License:        MIT
URL:            https://github.com/SDL-Hercules-390/%{srcname}
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# Renamed from decnumber, remove once f40 and el8 are EOL
Provides:       decnumber-devel%{?_isa} = %{version}-%{release}
Obsoletes:      decnumber-devel < 1.0.0-11
Provides:       decnumber-static%{?_isa} = %{version}-%{release}
Obsoletes:      decnumber-static < 1.0.0-11

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
# Renamed from decnumber, remove once f40 and el8 are EOL
Provides:       decnumber-doc = %{version}-%{release}
Obsoletes:      decnumber-doc < 1.0.0-11

%description    doc
The %{name}-doc package contains documentation and examples for %{name}.

%prep
%autosetup -n %{srcname}-%{commit}
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-doc:g'

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-doc/decnumber.ICU-license.html .

%files devel
%license decnumber.ICU-license.html
%doc README.md
%{_includedir}/*.h
%{_libdir}/lib%{srcname}*.a

%files doc
%license decnumber.ICU-license.html
%doc %{_docdir}/%{name}-doc/decnumber.*
%doc examples

%changelog
%autochangelog
