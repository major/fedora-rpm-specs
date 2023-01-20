Name:           CSFML
Version:        2.5.1
Release:        7%{?dist}
Summary:        C Interface for the Simple and Fast Multimedia Library

License:        zlib
URL:            https://www.sfml-dev.org/download/csfml/
Source0:        https://www.sfml-dev.org/files/CSFML-%{version}-sources.zip

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SFML-devel

%description
CSFML is the official C interface for the SFML library (written in C++),
allowing to develop applications using C instead of C++.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains developer documentation (in HTML format) for %{name}.


%prep
%setup -q


%build
%cmake -DCSFML_BUILD_DOC=TRUE
%cmake_build


%install
%cmake_install

# Fix documentation being installed in wrong directory
install -m 755 -d %{buildroot}%{_datadir}/doc
mv \
	%{buildroot}%{_datadir}/%{name}/doc \
	%{buildroot}%{_datadir}/doc/%{name}

# Remove license.txt and readme.txt - rely on %%license and %%doc macros
rm %{buildroot}%{_datadir}/%{name}/license.txt
rm %{buildroot}%{_datadir}/%{name}/readme.txt


%ldconfig_scriptlets


%files
%license license.txt
%doc readme.txt
%{_libdir}/libcsfml-*.so.2*

%files devel
%{_includedir}/SFML/
%{_libdir}/libcsfml-*.so

%files doc
%license license.txt
%doc %{_datadir}/doc/%{name}/


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-6
- Fix CMake-related FTBFS

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-3
- Do not install multiple copies of license.txt and readme.txt

* Thu Aug 12 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-2
- Change wildcard for .so files to protect against SONAME changes
- Fix license file not being installed properly
- Fix documentation being installed under wrong path
- Move documentation to -doc subpackage

* Mon Aug 02 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5.1-1
- Update to v2.5.1

* Fri Jul 09 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5-1
- Initial packaging
