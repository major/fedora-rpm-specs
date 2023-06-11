Name:       lpsolve
Version:    5.5.2.11
Release:    1%{?dist}
Summary:    Mixed Integer Linear Programming (MILP) solver
# bfp/bfp_LUSOL/lp_LUSOL.c:             LGPL-2.1-or-later
# colamd/colamd.c:  ??? (free with attribution in Matlab)
#                   Waiting on an identifier
#                   <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/230>
# colamd/colamd.h:  ??? (free with attribution in Matlab)
#                   Waiting on an identifier
#                   <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/230>
# lp_crash.c:       LGPL-2.1-or-later
# lp_lib.c:         LGPL-2.1-or-later
# lp_lib.h:         LGPL-2.1-or-later
# lp_matrix.c:      LGPL-2.1-or-later
# lp_MDO.c:         LGPL-2.1-or-later
# lp_mipbb.c:       LGPL-2.1-or-later
# lp_presolve.c:    LGPL-2.1-or-later
# lp_price.c:       LGPL-2.1-or-later
# lp_pricePSE.c:    LGPL-2.1-or-later
# lp_report.c:      LGPL-2.1-or-later
# lp_rlp.c:         GPL-2.0-or-later WITH Bison-exception-2.2
#                   Waiting on an approval
#                   <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/232>
# lp_scale.c:       LGPL-2.1-or-later
# lp_simplex.c:     LGPL-2.1-or-later
# lp_SOS.c:         LGPL-2.1-or-later
# lp_utils.c:       LGPL-2.1-or-later
# README.txt:       LGPL-2.1-or-later
## Unused and nonpackaged
# bfp/bfp_LUSOL/LUSOL/hbio.c:           xlock-like
# configure:        FSFUL
License:    LGPL-2.1-or-later AND GPL-2.0-or-later WITH Bison-exception-2.2
# There is a mailing list at <https://groups.google.com/g/lp_solve>.
URL:        https://sourceforge.net/projects/lpsolve
# A separate documention at
# <https://downloads.sourceforge.net/lpsolve/lp_solve_%%{version}_doc.tar.gz>
# contains proprietary JavaScript files and javascript trackers.
Source:     https://downloads.sourceforge.net/lpsolve/lp_solve_%{version}_source.tar.gz
# Use system-wide compiler, compiler and linker flags
Patch0:     lp_solve-5.5.2.11-Respect-CC-CFLAGS-and-LDFLAGS.patch
# Port to C99, GCC 14 will remove support for previous standards, proposed to
# an upstream <https://groups.google.com/g/lp_solve/c/WjVf0dxrwfQ/m/rKMwf57tAwAJ>.
Patch1:     lp_solve-5.5.2.11-Port-to-C99.patch
# Do not duplicate library code in the the tool
Patch2:     lp_solve-5.5.2.11-Link-a-tool-to-a-shared-library.patch
BuildRequires:  bash
# binutils for ar and ranlib
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  sed
# Tests:
BuildRequires:  grep

%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure linear,
(mixed) integer/binary, semi-continuous and special ordered sets (SOS) models.

%package devel
License:    LGPL-2.1-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}
Summary:    Files for developing with lpsolve

%description devel
Header files for developing with lpsolve library.

%prep
%autosetup -p1 -n lp_solve_5.5
sed -n -e '/Authors:/,/http:\/\/www\.cise\.ufl/p' < colamd/colamd.c \
    > colamd/colamd_license
chmod -x lp_lib.h

%build
%set_build_flags
pushd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
popd
pushd lp_solve
sh -x ccc
popd

%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_includedir}/lpsolve
install -p -m 755 \
        lp_solve/bin/ux*/lp_solve %{buildroot}%{_bindir}
install -p -m 755 \
        lpsolve55/bin/ux*/liblpsolve55.so %{buildroot}%{_libdir}
install -p -m 644 \
        lp*.h %{buildroot}%{_includedir}/lpsolve

%check
LP_PATH="$(echo lpsolve55/bin/ux*)"
# Verify lp_solve tool works
echo 'max: x; x < 42;' | \
    LD_LIBRARY_PATH="$LP_PATH" ./lp_solve/bin/ux*/lp_solve -S1 | \
    grep -e ': 42\.0*$'
# Verify a demo code is buildable
%set_build_flags
${CC} ${CFLAGS} -I. demo/demo.c ${LDFLAGS} -L"$LP_PATH" -llpsolve55
LD_LIBRARY_PATH="$LP_PATH" ./a.out </dev/null

%files
%license colamd/colamd_license
%doc README.txt
%{_bindir}/lp_solve
%{_libdir}/liblpsolve55.so

%files devel
%doc demo/demo.c
%{_includedir}/lpsolve

%changelog
* Wed Jun 07 2023 Petr Pisar <ppisar@redhat.com> - 5.5.2.11-1
- 5.5.2.11 bump
- Link lp_solve tool dynamically

* Wed Jun 07 2023 Petr Pisar <ppisar@redhat.com> - 5.5.2.0-33
- Modernize a spec file
- Partially correct a license tag

* Thu Feb 23 2023 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-32
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 5.5.2.0-30
- Port the ccc build configuration tool to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-20
- Related: rhbz#1548689 ... and LDFLAGS

* Mon Feb 26 2018 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-19
- Related: rhbz#1548689 there are two build scripts that need adjusting

* Mon Feb 26 2018 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-18
- Resolves: rhbz#1548689 use fedora compile/link flags

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 15 2016 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-13
- Resolves: rhbz#1307751 FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-9
- Resolves: rhbz#1109265 lpsolve.i686 missing in x86_64 repo

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Dan Horák <dan[at]danny.cz> - 5.5.2.0-2
- fix build on s390(x)

* Fri Aug 13 2010 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-1
- latest version

* Mon Dec 21 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-3
- Preserve timestamps

* Thu Nov 05 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-2
- upstream source silently changed content

* Sat Sep 12 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.14-2
- defuzz patch

* Mon Feb 02 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.14-1
- latest version

* Fri Jan 02 2009 Dennis Gilmore <dennis@ausil.us> - 5.5.0.13-2
- use -fPIC on sparc and s390 arches

* Mon Aug 04 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.13-1
- latest version

* Sat Aug 02 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.12-2
- Mar 20 upstream tarball now differs from Mar 14 tarball

* Fri Mar 14 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.12-1
- latest version

* Wed Feb 20 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.11-1
- initial version
