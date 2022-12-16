Name:           zn_poly
Version:        0.9.2
Release:        8%{?dist}
Summary:        C library for polynomial arithmetic

# All files released under "GPLv2 or GPLv3", except:
# - include/wide_arith.h is part LGPLv2+ and part GPLv2+
# - include/profiler.h is part GPLv2+
License:        (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.com/sagemath/%{name}
Source0:        https://gitlab.com/sagemath/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  python3

%description
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n is
any modulus that fits into an unsigned long.


%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n is
any modulus that fits into an unsigned long.

This package contains the development files.


%package static
Summary:        Development files for %{name}
Requires:       %{name}-devel = %{version}-%{release}
%description static
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n is
any modulus that fits into an unsigned long.

This package contains the static library.


%prep
%autosetup -p0

sed -i "s|typedef unsigned long  ulong;|\/\/typedef unsigned long  ulong;|g" include/zn_poly.h


%build
python3 makemakefile.py --cflags="%{build_cflags} -fPIC" --prefix=%{_prefix} \
    --gmp-prefix=%{_prefix} \
    --disable-tuning \
    > makefile

%make_build all libzn_poly.so libzn_poly-%{version}.so LDFLAGS='%{build_ldflags}'


%install
# install manually, because makefile does not honor DESTDIR
mkdir -p %{buildroot}%{_includedir}/zn_poly/
mkdir -p %{buildroot}%{_libdir}
cp -pv include/*.h %{buildroot}%{_includedir}/zn_poly/
cp -pv libzn_poly.a %{buildroot}%{_libdir}
cp -pv libzn_poly-%{version}.so %{buildroot}%{_libdir}
ln -s libzn_poly-%{version}.so %{buildroot}%{_libdir}/libzn_poly-0.9.so
ln -s libzn_poly-0.9.so %{buildroot}%{_libdir}/libzn_poly.so

%check
make test LDFLAGS='%{build_ldflags}'
./test/test all


%files
%doc COPYING gpl-?.0.txt
%doc demo/bernoulli/bernoulli.c doc/REFERENCES
%{_libdir}/libzn_poly-%{version}.so
%{_libdir}/libzn_poly-0.9.so


%files devel
%{_libdir}/libzn_poly.so
%{_includedir}/zn_poly/


%files static
%{_libdir}/libzn_poly.a


%changelog
* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 0.9.2-8
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Jerry James <loganjerry@gmail.com> - 0.9.2-2
- Fix library symlinks

* Mon Jan  6 2020 Jerry James <loganjerry@gmail.com> - 0.9.2-1
- Version 0.9.2
- Drop upstreamed -python3 patch
- Link with Fedora flags

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  8 2018 Jerry James <loganjerry@gmail.com> - 0.9.1-1
- Switch to sagemath gitlab repository URLs
- New 0.9.1 release
- Use python3 instead of python2 to generate the makefile
- Minor specfile cleanups for recent guidelines changes

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-18.2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9-5.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 0.9-5.1
- rebuild with new gmp

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jun 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9-4
- revert last change (fix flint instead)

* Sun Jun 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9-3
- flint wants to have headers in %%{_includedir}/zn_poly/src/

* Sun Jun 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9-2
- make libzn_poly.so a symlink to libzn_poly-%%{version}.so
- use directly makemakefile.py instead of configure
- preserve timestamps

* Sat Jun 26 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9-1
- initial package
