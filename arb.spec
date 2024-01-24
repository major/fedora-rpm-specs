Name:           arb
Version:        2.23.0
Release:        6%{?dist}
Summary:        Arbitrary-precision floating point ball arithmetic

License:        LGPL-2.1-or-later
URL:            https://arblib.org/
Source0:        https://github.com/fredrik-johansson/arb/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  %{py3_dist sphinx}

%description
Arb is a C library for arbitrary-precision floating-point ball
arithmetic.  It supports efficient high-precision computation with
polynomials, power series, matrices and special functions over the real
and complex numbers, with automatic, rigorous error control.

%package devel
Summary:        Headers for developing with arb
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}

%description devel
Header files and library links for developing with arb.

%package doc
Summary:        Documentation for arb
BuildArch:      noarch
# In addition to the project license, the Javascript and CSS bundled with the
# documentation has the following licenses:
# - searchindex.js: BSD-2-Clause
# - _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/classic.css: BSD-2-Clause
# - _static/doctools.js: BSD-2-Clause
# - _static/documentation_options.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/plus.png: BSD-2-Clause
# - _static/searchtools.js: BSD-2-Clause
# - _static/sidebar.js: BSD-2-Clause
# - _static/underscore*.js: MIT
License:        LGPL-2.1-or-later AND MIT AND BSD-2-Clause
Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description doc
Documentation for developers using the arb library.

%prep
%autosetup

# Let optflags specify the abi flag and do not set rpaths
sed -i '/ABI_FLAG="-m.."/d;/rpath/d' configure

# Preserve timestamps
sed -i 's/cp \$/cp -p $/' Makefile.in

# Use the classic sphinx theme
sed -i "s/'default'/'classic'/" doc/source/conf.py

# Avoid a name clash with a C library function
sed -i.orig 's/index(/index_smooth(/g' acb_dirichlet/powsum_smooth.c
touch -r acb_dirichlet/powsum_smooth.c.orig acb_dirichlet/powsum_smooth.c
rm acb_dirichlet/powsum_smooth.c.orig

%build
# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure --prefix=%{_prefix} --disable-static --with-flint=%{_prefix} \
  ABI=%{__isa_bits} CFLAGS="%{build_cflags}"
%make_build verbose LDFLAGS="%{build_ldflags}"
make -C doc html

%install
%make_install LIBDIR=%{_lib}

# Move the headers into a private directory
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/%{name}

# Fix permissions
chmod 0755 %{buildroot}%{_libdir}/libarb.so.*.*.*

# Remove hidden documentation build artifacts
rm -f doc/build/html/.buildinfo

%files
%doc README.md
%license LICENSE
%{_libdir}/libarb.so.2
%{_libdir}/libarb.so.2.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libarb.so

%files doc
%doc doc/build/html
%license LICENSE

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Jerry James <loganjerry@gmail.com> - 2.23.0-2
- Convert License tag to SPDX
- Note additional licenses for the doc subpackage

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 2.23.0-1
- Version 2.23.0

* Wed Jun  1 2022 Jerry James <loganjerry@gmail.com> - 2.22.1-1
- Version 2.22.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 2.20.0-3
- Rebuild for flint 2.8.0

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 2.20.0-2
- Rebuild to fix flint dependency

* Wed Jul 28 2021 Jerry James <loganjerry@gmail.com> - 2.20.0-1
- Version 2.20.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Jerry James <loganjerry@gmail.com> - 2.19.0-3
- Rebuild for flint 2.7.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 2.19.0-1
- Version 2.19.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 2.18.1-1
- Version 2.18.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 2.17.0-1
- New upstream version

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 2.16.0-4
- Rebuild for mpfr 4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec  8 2018 Jerry James <loganjerry@gmail.com> - 2.16.0-1
- New upstream version

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 2.15.1-1
- New upstream version

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 2.15.0-1
- New upstream version

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 2.14.0-1
- New upstream version (bz 1607183)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 2.13.0-1
- New upstream version (bz 1548596)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jerry James <loganjerry@gmail.com> - 2.11.1-1
- New upstream version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 2.10.0-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 2.8.1-4
- Rebuild for ntl 9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 2.8.1-3
- Rebuild for ntl 9.6.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Jerry James <loganjerry@gmail.com> - 2.8.1-1
- New upstream version (bz 1295018)

* Tue Dec 29 2015 Jerry James <loganjerry@gmail.com> - 2.8.0-1
- New upstream version

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 2.7.0-3
- Rebuild for ntl 9.6.2

* Fri Oct 23 2015 Jerry James <loganjerry@gmail.com> - 2.7.0-2
- Build with hardening ld flags

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- Initial RPM
