Name:		lis
Version:	2.0.21
Release:	15%{?dist}
Summary:	A library for solving linear equations and eigenvalue problems
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.ssisc.org/lis/index.en.html
Source0:	http://www.ssisc.org/lis/dl/lis-%{version}.zip
# Disable use of -O3 -fomit-frame-pointer
Patch0:		lis-1.5.60-optflags.patch

BuildRequires:	autoconf
BuildRequires:	chrpath
BuildRequires:	gcc-gfortran
BuildRequires: make

%description
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

%package bin
Summary:	lis executables

%description bin
This package contains binaries shipped with the lis library.

%package devel
Summary:	Development headers and library for lis
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

This package contains the development headers and library.

%package doc
Summary:	Developer documentation for lis
BuildArch:  noarch

%description doc
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

This package contains the developer documentation for lis.

%prep
%setup -q
%patch -P0 -p0 -b .optflags

%build
export CC=gcc
autoconf --force

mkdir -p omp
pushd omp
%global _configure ../configure
%configure --disable-static --enable-shared \
    --enable-saamg \
    --enable-quad --disable-rpath
make %{?_smp_mflags}
popd

%install
make -C omp install DESTDIR=%{buildroot}

# Get rid of RPATHs
# https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
chrpath --delete %{buildroot}%{_bindir}/*

# Get rid of .la file
rm %{buildroot}%{_libdir}/liblis.la

# .. and examples
rm -rf %{buildroot}%{_datadir}/examples

%ldconfig_scriptlets

%files
%doc AUTHORS
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/liblis.so.*

%files bin
%{_bindir}/esolve
%{_bindir}/gesolve
%{_bindir}/esolver
%{_bindir}/gesolver
%{_bindir}/lsolve
%{_bindir}/spmvtest?
%{_bindir}/spmvtest?b
%{_bindir}/hpcg_kernel
%{_bindir}/hpcg_spmvtest
%{_mandir}/man1/esolve.1.*
%{_mandir}/man1/gesolve.1.*
%{_mandir}/man1/esolver.1.*
%{_mandir}/man1/gesolver.1.*
%{_mandir}/man1/lsolve.1.*
%{_mandir}/man1/spmvtest?.1.*
%{_mandir}/man1/spmvtest?b.1.*
%{_mandir}/man1/hpcg_kernel.1.*
%{_mandir}/man1/hpcg_spmvtest.1.*

%files devel
%{_includedir}/lis.h
%{_includedir}/lis_config.h
%{_includedir}/lisf.h
%{_libdir}/liblis.so

%files doc
%doc doc/*.pdf
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_mandir}/man3/lis*.3.*
%{_mandir}/man3/lis*.3f.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.21-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Florian Lehner <dev@der-flo.net> - 2.0.21-3
- Fix date in changelog

* Sat Apr 18 2020 Florian Lehner <dev@der-flo.net> - 2.0.21-2
- Fix whitespace in changelog

* Sat Apr 18 2020 Florian Lehner <dev@der-flo.net> - 2.0.21-1
- Update to 2.0.21

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Florian Lehner <dev@der-flo.net> - 2.0.14-1
- Update to 2.0.14

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.7-1
- bump to 2.0.7 fixes rhbz #1404677 & silent rpmlint + spec cleanup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 11 2017 Florian Lehner <dev@der-flo.net> - 2.0.3-2
- Include new binaries

* Sat Nov 11 2017 Florian Lehner <dev@der-flo.net> - 2.0.3-1
- Update to 2.0.3

* Sun Aug 13 2017 Florian Lehner <dev@der-flo.net> - 1.8.3-1
- Update Update to 1.8.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun  1 2017 Florian Lehner <dev@der-flo.net> - 1.7.30-1
- Update to 1.7.30

* Mon Feb 27 2017 Florian Lehner <dev@der-flo.net> - 1.7.27-2
- Add new gcc-gfortran to BR

* Mon Feb 27 2017 Florian Lehner <dev@der-flo.net> - 1.7.27-1
- Update to 1.7.27

* Mon Feb  6 2017 Florian Lehner <dev@der-flo.net> - 1.7.25-1
- Update to 1.7.25
- remove obsolete omp test

* Thu Feb  2 2017 Florian Lehner <dev@der-flo.net> - 1.7.24-2
- remove OpenMP

* Thu Feb  2 2017 Florian Lehner <dev@der-flo.net> - 1.7.24-1
- Update to 1.7.24
- remove fortran dependency

* Tue Dec 20 2016 Florian Lehner <dev@der-flo.net> - 1.7.20-1
- Update to 1.7.20

* Sat Dec 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.7.16-1
- Rebuilt for new upstream release 1.7.16, fixes rhbz #1051419

* Sun Dec 04 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.7.14-1
- Rebuilt for new upstream release 1.7.14, fixes rhbz #1051419
- Fix .gitignore file and remove old useless sources

* Mon Nov 28 2016 Florian Lehner <dev@der-flo.net> 1.7.13-1
- Update to 1.7.13

* Fri Oct 28 2016 Florian Lehner <dev@der-flo.net> 1.7.4-2
- Add new binaries

* Fri Oct 28 2016 Florian Lehner <dev@der-flo.net> 1.7.4-1
- Update to 1.7.4

* Tue Oct 18 2016 David Abdurachmanov <david.abdurachmanov@gmail.com> 1.6.24-2
- Define _configure instead of creating symlink.
  Required to get config.{sub,guess} updated, for correct build on riscv64.

* Sat Oct  1 2016 Florian Lehner <dev@der-flo.net> 1.6.24-1
- Update to 1.6.24

* Wed Sep 14 2016 Florian Lehner <dev@der-flo.net> 1.6.10-1
- Update to 1.6.10

* Tue Sep  6 2016 Florian Lehner <dev@der-flo.net> 1.6.2-1
- Update to 1.6.2

* Sun Sep  4 2016 Florian Lehner <dev@der-flo.net> 1.6.0-1
- Update to 1.6.0

* Thu Sep  1 2016 Florian Lehner <dev@der-flo.net> 1.5.76-1
- Update to 1.5.76

* Sun Aug 21 2016 Florian Lehner <dev@der-flo.net> 1.5.68-1
- Update to 1.5.68

* Fri Jun 17 2016 Florian Lehner <dev@der-flo.net> 1.5.66-1
- Update to 1.5.66

* Sun Mar 20 2016 Florian Lehner <dev@der-flo.net> 1.5.65-1
- Update to 1.5.65

* Sat Mar 19 2016 Florian Lehner <dev@der-flo.net> 1.5.64-1
- Update to 1.5.64

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Florian Lehner <dev@der-flo.net> - 1.5.63-1
- Update to 1.5.63

* Thu Jan 28 2016 Florian Lehner <dev@der-flo.net> - 1.5.62-2
- Get rid of RPATHs
- Use license-macro

* Tue Jan 19 2016 Florian Lehner <dev@der-flo.net> - 1.5.62-1
- Update to 1.5.62

* Thu Jan  7 2016 Florian Lehner <dev@der-flo.net> - 1.5.61-1
- Update to 1.5.61

* Sat Jan  2 2016 Florian Lehner <dev@der-flo.net> - 1.5.60-1
- Update to 1.5.60

* Tue Dec 15 2015 Florian Lehner <dev@der-flo.net> - 1.5.59-1
- Update to 1.5.59

* Tue Dec  1 2015 Florian Lehner <dev@der-flo.net> - 1.5.58-1
- Update to 1.5.58

* Fri Jul 10 2015 Florian Lehner <dev@der-flo.net> - 1.5.57-1
- Update to 1.5.57

* Thu Jun 25 2015 Florian Lehner <dev@der-flo.net> - 1.5.56-1
- Update to 1.5.56

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May  1 2015 Florian Lehner <dev@der-flo.net> - 1.5.54-1
- Update to 1.5.54

* Sun Apr  5 2015 Florian Lehner <dev@der-flo.net> - 1.5.53-1
- Update to 1.5.53

* Sun Mar 29 2015 Florian Lehner <dev@der-flo.net> - 1.5.52-1
- Update to 1.5.52

* Tue Feb 10 2015 Florian Lehner <dev@der-flo.net> - 1.5.50-1
- Update to 1.5.50

* Fri Jan 16 2015 Florian Lehner <dev@der-flo.net> - 1.5.47-1
- Update to 1.5.47

* Sat Dec 27 2014 Florian Lehner <dev@der-flo.net> - 1.5.43-1
- Update to 1.5.43

* Tue Dec 23 2014 Florian Lehner <dev@der-flo.net> - 1.5.41-1
- Update to 1.5.41
- Drop privileges is fixed upstream

* Mon Dec 22 2014 Florian Lehner <dev@der-flo.net> - 1.5.40-1
- Update to 1.5.40

* Sun Dec 14 2014 Florian Lehner <dev@der-flo.net> - 1.5.37-1
- Update to 1.5.37
- Update Patch after renaming configure.in to configure.ac

* Sat Dec 13 2014 Florian Lehner <dev@der-flo.net> - 1.5.36-1
- Update to 1.5.36

* Sun Dec  7 2014 Florian Lehner <dev@der-flo.net> - 1.5.33-1
- Update to 1.5.33

* Wed Dec  3 2014 Florian Lehner <dev@der-flo.net> - 1.5.31-1
- Update to 1.5.31

* Thu Nov 27 2014 Florian Lehner <dev@der-flo.net> - 1.5.24-1
- Update to 1.5.24

* Wed Nov 26 2014 Florian Lehner <dev@der-flo.net> - 1.5.23-1
- Update to 1.5.23

* Tue Nov 25 2014 Florian Lehner <dev@der-flo.net> - 1.5.22-1
- Update to 1.5.22

* Fri Nov 21 2014 Florian Lehner <dev@der-flo.net> - 1.5.19-1
- Update to 1.5.19

* Fri Nov 21 2014 Florian Lehner <dev@der-flo.net> - 1.5.18-1
- Update to 1.5.18

* Sat Nov 15 2014 Florian Lehner <dev@der-flo.net> - 1.5.13-1
- Update to 1.5.13

* Wed Nov 12 2014 Florian Lehner <dev@der-flo.net> - 1.5.11-1
- Update to 1.5.11

* Tue Nov  4 2014 Florian Lehner <dev@der-flo.net> - 1.5.4-1
- Update to 1.5.4

* Sat Nov  1 2014 Florian Lehner <dev@der-flo.net> - 1.5.2-1
- Update to 1.5.2

* Tue Oct 28 2014 Florian Lehner <dev@der-flo.net> - 1.4.67-1
- Update to 1.4.67

* Mon Oct 27 2014 Florian Lehner <dev@der-flo.net> - 1.4.66-1
- Update to 1.4.66

* Tue Oct 21 2014 Florian Lehner <dev@der-flo.net> - 1.4.64-1
- Update to 1.4.64

* Mon Oct 20 2014 Florian Lehner <dev@der-flo.net> - 1.4.63-1
- Update to 1.4.63

* Sat Oct 18 2014 Florian Lehner <dev@der-flo.net> - 1.4.62-1
- Update to 1.4.62

* Fri Sep 19 2014 Florian Lehner <dev@der-flo.net> - 1.4.61-1
- Update to 1.4.61

* Wed Sep 17 2014 Florian Lehner <dev@der-flo.net> - 1.4.60-1
- Update to 1.4.60

* Wed Sep 10 2014 Florian Lehner <dev@der-flo.net> - 1.4.59-1
- Update to 1.4.59

* Wed Aug 27 2014 Florian Lehner <dev@der-flo.net> - 1.4.58-1
- Update to 1.4.58

* Mon Aug 18 2014 Florian Lehner <dev@der-flo.net> - 1.4.57-1
- Update to 1.4.57

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Florian Lehner <dev@der-flo.net> - 1.4.56-1
- Update to 1.4.56
- Drop group-tag
- Fix permission for AUTHORS and COPYING

* Mon Aug 11 2014 Florian Lehner <dev@der-flo.net> - 1.4.55-1
- Update to 1.4.55
- Add noarch to subpackage doc
- Remove requires from subpackage doc

* Sun Aug 10 2014 Florian Lehner <dev@der-flo.net> - 1.4.53-2
- Remove defattr at the beginning of the files-section
- Use default buildroot instead of making its own
- Remove unnecessary clean-section
- Use pushd and popd instead of cd

* Sat Aug  9 2014 Florian Lehner <dev@der-flo.net> - 1.4.53-1
- Update to 1.4.53

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 15 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.20-1
- Update to 1.4.20.

* Mon Sep 09 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.13-1
- Update to 1.4.13.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.32-1
- Update to 1.3.32.

* Mon Mar 04 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.31-1
- Update to 1.3.31.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.115-1
- Update to 1.2.115.

* Tue Aug 07 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.92-1
- Update to 1.2.92. Enabled SAMG.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.68-1
- Update to 1.2.68.

* Wed Jun 20 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.66-1
- Update to 1.2.66.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.58-1
- Update to 1.2.58.

* Tue Nov 08 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.56-1
- Update to 1.2.56.

* Wed Nov 02 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.54-1
- Update to 1.2.54.

* Sun Sep 18 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.53-3
- Include COPYING in -doc.

* Thu Sep 15 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.53-2
- Enabled quadruple precision support.

* Mon Sep 12 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.53-1
- First release.
