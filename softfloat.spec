%global forgeurl https://github.com/SDL-Hercules-390/SoftFloat
%global commit 42f2f99a479a724de5b601a0551e46678a5e3c57
%forgemeta

# Needed for f32 and epel8
%undefine __cmake_in_source_build
%global _vpath_srcdir %{_builddir}/%{name}-%{version}/SoftFloat-%{commit}
%global _vpath_builddir %{_builddir}/%{name}-%{version}/SoftFloat%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
Berkeley SoftFloat is a software implementation of binary floating-point that
conforms to the IEEE Standard for Floating-Point Arithmetic. The current
release supports five binary formats: 16-bit half-precision, 32-bit
single-precision, 64-bit double-precision, 80-bit double-extended- precision,
and 128-bit quadruple-precision.}

Name:           softfloat
Version:        3.5.0
Release:        6%{?dist}
Summary:        Berkeley IEEE Binary Floating-Point Library

License:        BSD
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
%{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
%{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c
tar xzf %{SOURCE0}
pushd SoftFloat-%{commit}
mv README.md CHANGELOG.txt ..
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
%doc %{_docdir}/%{name}-devel/SoftFloat*.html
%{_includedir}/*.h
%{_libdir}/libSoftFloat*.a

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 29 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.5.0-2.20210321git42f2f99
- Fix build on f32 and epel8

* Sun Mar 21 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.5.0-1.20210321git42f2f99
- Initial package
