%ifarch ppc64le
%global bootstrap 1
%endif

Name: mlton
Version: 20180207
Release: 19%{?dist}
Summary: Optimizing compiler for Standard ML

License: MIT
URL: http://mlton.org/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tgz

# Generated sources (non-binary) for bootstrapping.
# See http://mlton.org/PortingMLton#_bootstrap
Source100: mlton-bootstrap-ppc64le-redhat-linux.tar.gz

BuildRequires: make
BuildRequires: gcc gmp-devel tex(latex)

%if ! 0%{?bootstrap}
BuildRequires: mlton
%endif

Requires: gmp-devel gcc

# https://github.com/MLton/mlton/pull/250
Patch1: 0001-Lift-customized-variables-to-top-of-.-bin-mlton-scri.patch
Patch2: 0002-Add-LIB_REL_BIN-customizable-variable-to-.-bin-mlton.patch
Patch3: 0003-Set-LIB_REL_BIN-in-mlton-script-when-installing.patch
Patch4: 0004-Fix-use-of-MKDIR-and-RM-variables-in-.-Makefile.bina.patch
Patch5: 0005-Set-LIB_REL_BIN-in-mlton-script-when-installing.patch

# https://github.com/MLton/mlton/pull/255
Patch10: 0001-Enable-ppc64le-variant-in-bin-platform.patch

# https://github.com/MLton/mlton/pull/258
Patch20: 0001-Introduce-RISC-V-support.patch

# Filter out false dependencies.
%global __provides_exclude_from ^(%{_docdir}|%{_libdir}/mlton/sml)/.*$
%global __requires_exclude_from ^(%{_docdir}|%{_libdir}/mlton/sml)/.*$


# Description taken from the Debian package by Stephen Weeks.
%description
MLton is a whole-program optimizing compiler for Standard ML.  MLton
generates standalone executables with excellent runtime performance,
is SML 97 compliant, and has a complete basis library. MLton has
source-level profiling, a fast C FFI, an interface to the GNU
multiprecision library, and lots of useful libraries.


%prep
%autosetup -T -b 0 -p1

# https://fedoraproject.org/wiki/Packaging:Guidelines#Shebang_lines
sed -i -e '1 s;^#! */usr/bin/env *;#!/usr/bin/;' bin/*

%if 0%{?bootstrap}

%ifarch ppc64le
%setup -T -D -q -a 100
%endif

%endif


%build
%if 0%{?bootstrap}
# Build mlton-compile from the bootstrap sources.
make dirs runtime CFLAGS="$RPM_OPT_FLAGS"

# We need the -O1 here or else RHEL 7 GCC miscompiles the bootstrap source.
for s in mlton/mlton.*.c; do
  gcc $RPM_OPT_FLAGS -O1 -c -Ibuild/lib/mlton/include \
     -Ibuild/lib/mlton/targets/self/include -w "${s}"
done
gcc $RPM_OPT_FLAGS -o build/lib/mlton/mlton-compile \
    -Lbuild/lib/mlton/targets/self \
    -L/usr/local/lib \
    mlton.*.o \
    -lmlton -lgmp -lgdtoa -lm

make basis-no-check script constants libraries tools CFLAGS="$RPM_OPT_FLAGS"

# Install this to a local location and clean. Then continue on with a
# regular build with PATH.
make install PREFIX=$(pwd)/../bootstrap
export PATH=$PATH:$(pwd)/../bootstrap/bin
make clean
%endif

make all docs PREFIX=%{_prefix} libdir=%{_libdir} CFLAGS="$RPM_OPT_FLAGS"


%install
make install-no-strip install-docs PREFIX=%{_prefix} libdir=%{_libdir} \
     docdir=%{_pkgdocdir} DESTDIR=$RPM_BUILD_ROOT

# Remove unnecessary regression test.
rm -rf $RPM_BUILD_ROOT%{_libdir}/mlton/sml/ckit-lib/regression


%files
%doc %{_pkgdocdir}
%license %{_pkgdocdir}/license/*
%{_bindir}/ml*
%{_libdir}/mlton
%{_mandir}/man1/*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Adam Goode <adam@spicenitz.org> - 20180207-11
- Add missing patch and re-bootstrap for ppc64le (RHBZ #1676288)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Adam Goode <adam@spicenitz.org> - 20180207-9
- BuildRequires: gcc
- Remove bootstrap

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180207-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr  4 2018 Adam Goode <adam@spicenitz.org> - 20180207-7
- Bootstrap RISC-V

* Sun Apr  1 2018 Adam Goode <adam@spicenitz.org> - 20180207-6
- Finalize bootstrap

* Sun Apr  1 2018 Adam Goode <adam@spicenitz.org> - 20180207-5
- Fix EPEL build
- Modernize the specfile

* Sun Apr  1 2018 Adam Goode <adam@spicenitz.org> - 20180207-4
- Bootstrap the remaining Fedora and RHEL7 arches

* Sat Mar 31 2018 Adam Goode <adam@spicenitz.org> - 20180207-3
- Remove broken release workaround

* Sat Mar 31 2018 Adam Goode <adam@spicenitz.org> - 20180207-2
- Fix busted 20180207-1 release
- Remove bootstrap stuff for now

* Mon Mar 19 2018 Adam Goode <adam@spicenitz.org> - 20180207-1
- New upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130715-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130715-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130715-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 20130715-11
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130715-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 20130715-9
- Add ExcludeArch until those arches are bootstrapped (rhbz 1056365)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130715-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130715-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130715-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130715-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Adam Goode <adam@spicenitz.org> - 20130715-4
- Fix recent regression of not using RPM_OPT_FLAGS #1013323

* Sat Sep 28 2013 Adam Goode <adam@spicenitz.org> - 20130715-3
- Use pkgdocdir instead of docdir

* Thu Sep 26 2013 Adam Goode <adam@spicenitz.org> - 20130715-2
- Switch to unversioned docdir

* Thu Sep 26 2013 Adam Goode <adam@spicenitz.org> - 20130715-1
- New upstream release: http://mlton.org/Release20130715

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100608-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 27 2013 Adam Goode <adam@spicenitz.org> - 20100608-17
- MLton is too big for polyml, so bootstrap arm, armhfp, ppc, ppc64 with mlton
- Don't use htmldoc anymore, it often crashes
- Remove max-heap workaround

* Mon Apr 22 2013 Adam Goode <adam@spicenitz.org> - 20100608-16
- Scrap all the arch-specific bootstrapping, use polyml to do it

* Sun Apr 21 2013 Adam Goode <adam@spicenitz.org> - 20100608-15
- Try a more generalized bootstrap approach

* Sat Apr 20 2013 Adam Goode <adam@spicenitz.org> - 20100608-14
- Really fix builds by more intelligently setting max-heap

* Sat Apr 20 2013 Adam Goode <adam@spicenitz.org> - 20100608-13
- Fix ppc64 bootstrap

* Sat Apr 20 2013 Adam Goode <adam@spicenitz.org> - 20100608-12
- Bootstrap ppc64

* Fri Apr 19 2013 Adam Goode <adam@spicenitz.org> - 20100608-11
- Bootstrap ppc

* Thu Apr 18 2013 Adam Goode <adam@spicenitz.org> - 20100608-10
- Constrain max-heap to a fixed value during building, otherwise 70% of physical
  ram is used
- Fix detection of ppc64

* Mon Apr 15 2013 Adam Goode <adam@spicenitz.org> - 20100608-9
- Fix for #914188 FTBFS
- Update source link
- Remove ExclusiveArch, per packaging recommendations

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100608-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100608-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100608-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 20100608-5.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 20100608-5.1
- rebuild with new gmp

* Fri Aug 12 2011 Adam Goode <adam@spicenitz.org> - 20100608-5
- Clean up auto dependences

* Fri Mar 11 2011 Dan Horák <dan[at]danny.cz> - 20100608-4
- set ExclusiveArch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100608-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 11 2010 Adam Goode <adam@spicenitz.org> - 20100608-2
- Change location of upstream source

* Fri Jun 11 2010 Adam Goode <adam@spicenitz.org> - 20100608-1
- New upstream release, see http://mlton.org/Release20100608

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070826-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Adam Goode <adam@spicenitz.org> - 20070826-19
- Add forgotten changelog entry

* Sun May 31 2009 Adam Goode <adam@spicenitz.org> - 20070826-18
- ARM is bootstrapped, build again

* Sun May 31 2009 Adam Goode <adam@spicenitz.org> - 20070826-17
- Use non-trunk version of MLton to bootstrap ARM

* Tue May 26 2009 Adam Goode <adam@spicenitz.org> - 20070826-16
- Add missing ARM patch

* Tue May 26 2009 Adam Goode <adam@spicenitz.org> - 20070826-15
- Bootstrap ARM

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070826-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Adam Goode <adam@spicenitz.org> - 20070826-13
- RPM 4.6 fix for patch tag
- Update LaTeX build requires

* Sat Feb  9 2008 Adam Goode <adam@spicenitz.org> - 20070826-12
- Introduce patch to not call mprotect with PROT_EXEC

* Fri Jan 18 2008 Adam Goode <adam@spicenitz.org> - 20070826-11
- Rebuild for new GCC

* Thu Sep 27 2007 Adam Goode <adam@spicenitz.org> - 20070826-10
- Disable bootstrap

* Thu Sep 27 2007 Adam Goode <adam@spicenitz.org> - 20070826-9
- Re-bootstrap ppc

* Wed Sep 26 2007 Adam Goode <adam@spicenitz.org> - 20070826-8
- Really fix SRPM conditionals

* Wed Sep 26 2007 Adam Goode <adam@spicenitz.org> - 20070826-7
- Work around strange SRPM problem in conditionals
- Fix changelog (forgot release 5?)

* Wed Sep 26 2007 Adam Goode <adam@spicenitz.org> - 20070826-6
- Build on ppc now that #247407 is fixed

* Thu Sep 13 2007 Adam Goode <adam@spicenitz.org> - 20070826-4
- Do not condition bootstrap source tag

* Thu Sep 13 2007 Adam Goode <adam@spicenitz.org> - 20070826-3
- Bootstrap x86_64

* Mon Aug 27 2007 Adam Goode <adam@spicenitz.org> - 20070826-2
- Exclude ppc for now (GCC internal compiler error!)

* Sun Aug 26 2007 Adam Goode <adam@spicenitz.org> - 20070826-1
- Update to new release

* Wed Aug 22 2007 Adam Goode <adam@spicenitz.org> - 20061107-4
- Exclude ppc64 for now

* Wed Aug 22 2007 Adam Goode <adam@spicenitz.org> - 20061107-3
- Update license tag
- Rebuild for buildid

* Fri Nov 24 2006 Adam Goode <adam@spicenitz.org> - 20061107-2
- Use RPM_OPT_FLAGS
- Correctly instantiate version
- Adjust patches

* Sun Nov 12 2006 Adam Goode <adam@spicenitz.org> - 20061107-1
- New release, taken from svn://mlton.org/mlton/tags/on-20061107

* Thu Aug 31 2006 Adam Goode <adam@spicenitz.org> - 20051202-8.1
- Mass rebuild

* Sun Jul  9 2006 Adam Goode <adam@spicenitz.org> - 20051202-8
- Conditionalize bootstrapping and disable it

* Sat Jul  1 2006 Adam Goode <adam@spicenitz.org> - 20051202-7
- Fix macro in changelog
- Remove mixed use of tabs and spaces

* Sun Jun 25 2006 Adam Goode <adam@spicenitz.org> - 20051202-6
- Build runtime with -g, but not -gstabs+
- Re-enable debuginfo packages

* Wed Jun 21 2006 Adam Goode <adam@spicenitz.org> - 20051202-5
- Disable empty debuginfo packages

* Wed Jun 21 2006 Adam Goode <adam@spicenitz.org> - 20051202-4
- Be more specific about license
- Add "which" to BuildRequires until everyone is running new mock

* Tue Jun 20 2006 Adam Goode <adam@spicenitz.org> - 20051202-3
- Create PDF documentation for mlyacc and mllex (instead of .ps.gz)
- Move ckit-lib/doc and smlnj-lib/Doc to %%{_docdir}
- Remove regression files from ckit

* Thu Jun  8 2006 Adam Goode <adam@spicenitz.org> - 20051202-2
- Change to use bootstrap

* Wed Jun  7 2006 Adam Goode <adam@spicenitz.org> - 20051202-1
- Initial release for FC5
