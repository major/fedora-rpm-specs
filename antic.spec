Name:           antic
Version:        0.2.5
Release:        2%{?dist}
Summary:        Algebraic Number Theory In C

License:        LGPL-2.1-or-later
URL:            https://github.com/wbhart/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  flint-devel
BuildRequires:  gmp-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(mpfr)

%description
Antic is an algebraic number theory library written in C.

%package        devel
Summary:        Development files for antic
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

# Fix end-of-line encodings
sed -i.orig 's/\r//' NEWS
touch -r NEWS.orig NEWS
rm NEWS.orig

# Fix install location on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i '/DESTINATION/s/lib/%{_lib}/g' CMakeLists.txt
fi

%build
%cmake -DBUILD_TESTING:BOOL=YES
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc AUTHORS NEWS README
%license LICENSE
%{_libdir}/libantic.so.0*

%files          devel
%{_includedir}/%{name}/
%{_libdir}/libantic.so

%changelog
* Thu Aug 11 2022 Jerry James <loganjerry@gmail.com> - 0.2.5-2
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 0.2.5-1
- Build with cmake

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 0.2.5-1
- Version 0.2.5

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 0.2.4-3
- Rebuild for flint 2.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul  5 2021 Jerry James <loganjerry@gmail.com> - 0.2.4-1
- Version 0.2.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 0.2.2-1
- Version 0.2.2

* Thu Jul 30 2020 Jerry James <loganjerry@gmail.com> - 0.2.1-1
- Initial RPM
