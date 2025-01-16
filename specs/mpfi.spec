Name:           mpfi
Version:        1.5.4
Release:        7%{?dist}
Summary:        An interval arithmetic library based on MPFR

# Most files have an LGPL-2.1-or-later notice.  Exceptions:
# src/clears.c: LGPL-3.0-or-later
# src/inits.c: LGPL-3.0-or-later
# src/inits2.c: LGPL-3.0-or-later
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://perso.ens-lyon.fr/nathalie.revol/software.html
VCS:            git:https://gitlab.inria.fr/mpfi/mpfi.git
Source:         https://perso.ens-lyon.fr/nathalie.revol/softwares/%{name}-%{version}.tar.xz
# Fix possible use of initialized variables
Patch:          %{name}-uninit.patch
# Fix mismatched type declarations
Patch:          %{name}-mismatched-type.patch
# Fix incorrect use of the address-of operator
Patch:          %{name}-bad-ref.patch
# Fix a missing #include in a test file
Patch:          %{name}-test.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  gmp-devel

%description
MPFI is intended to be a portable library written in C for arbitrary
precision interval arithmetic with intervals represented using MPFR
reliable floating-point numbers. It is based on the GNU MP library and
on the MPFR library and is part of the latter. The purpose of an
arbitrary precision interval arithmetic is on the one hand to get
"guaranteed" results, thanks to interval computation, and on the other
hand to obtain accurate results, thanks to multiple precision
arithmetic. The MPFI library is built upon MPFR in order to benefit
from the correct roundings provided by MPFR. Further advantages of
using MPFR are its portability and compliance with the IEEE 754
standard for floating-point arithmetic.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library for %{name}

%description    static
The %{name}-static package contains the static %{name} library.

%prep
%autosetup -p1

%conf
# In the 1.5.4 release, these two tests try to call functions with mismatched
# signatures, then segfault.  It is not clear to me how to fix them.
sed -i 's/ tdiv_ext\$(EXEEXT)//;s/ trec_sqrt\$(EXEEXT)//' tests/Makefile.in

# In the 1.5.4 release, the data file needed by this test is missing.
sed -i 's/texp10\$(EXEEXT) //' tests/Makefile.in

# Fix the pkgconfig file
sed -i 's/ -lmpfr -lgmp/\nLibs.private:&/' mpfi.pc.in

%build
%configure
%make_build

%install
%make_install

# Remove libtool archives
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Remove dir file in the info directory
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Remove license files from doc
rm %{buildroot}%{_docdir}/mpfi/COPYING*

%check
make check

%files
%doc AUTHORS NEWS TODO
%license COPYING COPYING.LESSER
%{_libdir}/libmpfi.so.0*

%files devel
%{_includedir}/mpfi.h
%{_includedir}/mpfi_io.h
%{_infodir}/%{name}.info*
%{_libdir}/libmpfi.so
%{_libdir}/pkgconfig/mpfi.pc

%files static
%{_libdir}/lib%{name}.a

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.5.4-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 1.5.4-1
- Version 1.5.4
- Add patches to fix compiler warnings and errors: -uninit, -mismatched-type,
  -bad-ref, and -test
- Disable 3 tests with upstream problems
- Disable 1 test on 32-bit ARM

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 1.5.3-5
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- New upstream version
- Drop upstreamed -aarch64 patch

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jerry James <loganjerry@gmail.com> - 1.5.1-4
- Add aarch64 support (bz 926172)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- New upstream version
- Drop upstreamed Debian patch

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 1.5-3
- Rebuild for GCC 4.7

* Wed Nov  2 2011 Jerry James <loganjerry@gmail.com> - 1.5-2
- Rebuild for new gmp.

* Mon Apr 25 2011 Jerry James <loganjerry@gmail.com> - 1.5-1
- New upstream version.
- Drop BuildRoot tag, clean script, and clean at start of install script.
- Drop texinfo patch, upstreamed.
- Move static library into -static subpackage.
- Add check script.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-0.8.RC3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-0.7.RC3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.6.RC3
- Add missing BR on texinfo.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-0.5.RC3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 19 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.4.RC3
- Attempt to preserve timestamps with install -p.
- Remove some useless %%docs.
- Give install-info more respect like it deserves.

* Tue Oct 14 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.4-0.3.RC3
- Use %%{_infodir} in %%preun/%%post.
- Move %%preun/%%post to *-devel.
- Remove R: from *-devel.

* Mon Oct 13 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.2.RC3
- Oops, fix the requires.
- Don't ship a base package.

* Mon Oct 13 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4-0.1.RC3
- Fix version to follow NEVR guidelines (I don't want to bump the epoch
  since it's not even in Fedora yet).
- Install infos correctly.

* Sun Oct 12 2008 Conrad Meyer <konrad@tylerc.org> - 1.3.4RC3-1
- Initial package.
