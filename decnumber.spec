%global forgeurl https://github.com/SDL-Hercules-390/decNumber
%global commit da6650957d7dea21b5647c1fa80fa432f2891550
%forgemeta

# Needed for f32 and epel8
%undefine __cmake_in_source_build
%global _vpath_srcdir %{_builddir}/%{name}-%{version}/decNumber-%{commit}
%global _vpath_builddir %{_builddir}/%{name}-%{version}/decNumber%{__isa_bits}.Release
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
fixed-size representations are supported.}

Name:           decnumber
Version:        3.68.0
Release:        7%{?dist}
Summary:        ANSI C General Decimal Arithmetic Library

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
%{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
%{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation and examples for %{name}.

%prep
%setup -q -c
tar xzf %{SOURCE0}
pushd decNumber-%{commit}
mv README.md examples ..
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
%{_libdir}/libdecNumber*.a

%files doc
%license decnumber.ICU-license.html
%doc %{_docdir}/%{name}-doc/decnumber.*
%doc examples

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.68.0-2.20210321gitda66509
- Fix build on f32 and epel8

* Sun Mar 28 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.68.0-1.20210321gitda66509
- Initial package
