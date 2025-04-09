%global srcname SoftFloat
%global date 20250324
%global commit e053494d988ec0648c92f683abce52597bfae745
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
Berkeley SoftFloat is a software implementation of binary floating-point that
conforms to the IEEE Standard for Floating-Point Arithmetic. The current
release supports five binary formats: 16-bit half-precision, 32-bit
single-precision, 64-bit double-precision, 80-bit double-extended- precision,
and 128-bit quadruple-precision.

This version is a fork by SoftDevLabs (SDL) to support the SDL-Hercules-390
emulator.}

Name:           sdl-softfloat
Version:        3.5.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Berkeley IEEE Binary Floating-Point Library (SDL version)

License:        BSD-3-Clause
URL:            https://github.com/SDL-Hercules-390/%{srcname}
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# Renamed from softfloat, remove once f40 and el8 are EOL
Provides:       softfloat-devel%{?_isa} = %{version}-%{release}
Obsoletes:      softfloat-devel < 3.5.0-11
Provides:       softfloat-static%{?_isa} = %{version}-%{release}
Obsoletes:      softfloat-static < 3.5.0-11

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{commit}
sed -i extra.txt \
  -e 's:DESTINATION  .:DESTINATION share/doc/%{name}-devel:g' \
  -e 's:DESTINATION doc:DESTINATION share/doc/%{name}-devel:g' \

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-devel/softfloat.LICENSE.txt .

%files devel
%license softfloat.LICENSE.txt
%doc README.md CHANGELOG.txt
%doc %{_docdir}/%{name}-devel/softfloat.README.*
%doc %{_docdir}/%{name}-devel/%{srcname}*.html
%{_includedir}/*.h
%{_libdir}/lib%{srcname}*.a

%changelog
%autochangelog
