Name:           sirocco
Version:        2.1.0
Release:        6%{?dist}
Summary:        ROot Certified COntinuator

# See https://github.com/miguelmarco/SIROCCO2/issues/1
License:        GPL-3.0-only
URL:            https://github.com/miguelmarco/SIROCCO2
Source0:        %{url}/releases/download/%{version}/lib%{name}-%{version}.tar.gz
# Fix some mixed signed/unsigned expressions
Patch0:         %{name}-signed.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mpfr-devel

%description
This is a library for computing homotopy continuation of a given root of
one dimensional sections of bivariate complex polynomials.  The output
is a piecewise linear approximation of the path followed by the root,
with the property that there is a tubular neighborhood, with square
transversal section, that contains the actual path, and there is a three
times thicker tubular neighborhood guaranteed to contain no other root
of the polynomial.  This second property ensures that the piecewise
linear approximation computed from all roots of a polynomial form a
topologically correct deformation of the actual braid, since the inner
tubular neighborhoods cannot intersect.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p0 -n lib%{name}-%{version}

%build
export CFLAGS="%{build_cflags} -frounding-math"
export CXXFLAGS="%{build_cxxflags} -frounding-math"
%configure --disable-static --disable-silent-rules

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool

%make_build

%install
%make_install

# We do not want the libtool files
rm %{buildroot}%{_libdir}/*.la

# Fix an incorrect symlink
rm %{buildroot}%{_libdir}/libsirocco.so
ln -s libsirocco.so.0 %{buildroot}%{_libdir}/libsirocco.so

%check
make check

%files
%license LICENSE
%doc README.md
%{_libdir}/libsirocco.so.0
%{_libdir}/libsirocco.so.0.*

%files devel
%{_includedir}/sirocco.h
%{_libdir}/libsirocco.so

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-4
- Upstream states that the license is GPL-3.0-only
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  1 2021 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Version 2.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Jerry James <loganjerry@gmail.com> - 2.0.2-1
- Version 2.0.2

* Tue Feb 11 2020 Jerry James <loganjerry@gmail.com> - 2.0.1-1
- Version 2.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2.0-4
- Update to latest git snapshot

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Jerry James <loganjerry@gmail.com> - 2.0-1
- Initial RPM
