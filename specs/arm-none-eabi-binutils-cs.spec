%global processor_arch arm
%global target         %{processor_arch}-none-eabi

Name:           %{target}-binutils-cs
Epoch:          1
Version:        2.43
Release:        2%{?dist}
Summary:        GNU Binutils for cross-compilation for %{target} target
# Most of the sources are licensed under GPLv3+ with these exceptions:
# LGPLv2+ bfd/hosts/x86-64linux.h, include/demangle.h, include/xregex2.h,
# GPLv2+  gprof/cg_print.h
# BSD     gprof/cg_arcs.h, gprof/utils.c, ld/elf-hints-local.h,
# Public Domain libiberty/memmove.c
# Automatically converted from old format: GPLv2+ and GPLv3+ and LGPLv2+ and BSD - review is highly recommended.
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:            http://www.codesourcery.com/sgpp/lite/%{processor_arch}

Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.xz

Source1:        README.fedora
BuildRequires:  gcc flex bison ppl-devel cloog
BuildRequires:  autoconf
BuildRequires:  texinfo texinfo-tex perl-podlators
BuildRequires:  make zlib-devel
Provides:       %{target}-binutils = %{version}

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# ppl-devel is no longer available for 32bit, so we have to skip it too
ExcludeArch:    %{ix86}
%endif

%description
This is a cross-compilation version of GNU Binutils, which can be used to
assemble and link binaries for the %{target} platform.  

Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%prep
%autosetup -p1 -n binutils-%{version}
cp -p %{SOURCE1} .
rm -rf gdb sim

%build
# We call configure directly rather than via macros, thus if
# we are using LTO, we have to manually fix the broken configure
# scripts
pushd libiberty
#autoconf -f
popd
%if 0%{?fedora} || 0%{?rhel} > 8
[ %{_lto_cflags}x != x ] && %{_fix_broken_configure_for_lto}
%endif

./configure CFLAGS="$RPM_OPT_FLAGS" \
            --target=%{target} \
            --enable-interwork \
            --enable-multilib \
            --enable-plugins \
            --disable-nls \
            --disable-shared \
            --disable-threads \
            --with-gcc --with-gnu-as --with-gnu-ld \
            --with-system-zlib \
            --prefix=%{_prefix} \
            --libdir=%{_libdir} \
            --mandir=%{_mandir} \
            --infodir=%{_infodir} \
            --with-docdir=share/doc/%{name} \
            --disable-werror \
            --with-pkgversion="Fedora %{version}-%{release}" \
            --with-bugurl="https://bugzilla.redhat.com/"
make %{?_smp_mflags}

%check
%ifnarch s390x
make check
%endif
echo "completed"

%install
make install DESTDIR=$RPM_BUILD_ROOT
# these are for win targets only
rm    $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,windres}.1
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/libdep* ||:


%files
%license COPYING*
%doc ChangeLog README.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.43-1
- updated to 2.43

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:2.42-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.42-2
- drop i686 build as ppl-devel.i686 is no longer available

* Wed Mar 06 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.42-1
- updated to 2.42

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.41-1
- updated to 2.41

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.40-1
- updated to 2.40

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Florian Weimer <fweimer@redhat.com> - 1:2.39-2
- C99 compatibility fixes for the configure script

* Wed Aug 31 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.39-1
- updated to 2.39

* Wed Aug 24 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1:2.38-3
- Fix build on EPEL 8

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 09 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.38-1
- updated to 2.38

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 06 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.37-3
- temp. disable autoconf as 2.71 is not compatible

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.37-1
- updated to 2.37

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.36.1-1
- updated to 2.36.1

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.36-1
- updated to 2.36

* Mon May 03 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.35-4
- bump release for rebuild

* Mon Apr 12 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.35-3
- add explicit requirement for autoconf 2.69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Michal Hlavinka <mhlavink@redhat.com> - 1:2.35-1
- updated to 2.35

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Jeff Law <law@redhat.com> - 1:2.32-4
- Fix broken configure files compromised by LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:2.32-1
- updated to 2.32

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Michal Hlavinka <mhlavink@redhat.com> - 1:2.30-2
- add gcc buildrequire

* Tue Feb 06 2018 Michal Hlavinka <mhlavink@redhat.com> - 1:2.30-1
- updated to 2.30

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 Michal Hlavinka <mhlavink@redhat.com> - 1:2.28-1
- updated to 2.28

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:2.27-1
- updated to 2.27

* Tue Jun 28 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:2.26-1
- update binutils to 2.26

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:2.25-1
- updated to vanila 2.25

* Thu Nov 13 2014 Michal Hlavinka <mhlavink@redhat.com> - 2014.05.28-3
- fix CVE-2014-8738: out of bounds memory write

* Wed Nov 12 2014 Michal Hlavinka <mhlavink@redhat.com> - 2014.05.28-2
- fix directory traversal vulnerability (#1162657)
- fix CVE-2014-8501: out-of-bounds write when parsing specially crafted PE executable
- fix CVE-2014-8502: heap overflow in objdump
- fix CVE-2014-8503: stack overflow in objdump when parsing specially crafted ihex file
- fix CVE-2014-8504: stack overflow in the SREC parser

* Wed Aug 20 2014 Michal Hlavinka <mhlavink@redhat.com> - 2014.05.28-1
- updated to 2014.05-28

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Michal Hlavinka <mhlavink@redhat.com> - 2013.11.24-1
- updated to 2013.11-24

* Wed Aug 21 2013 Michal Hlavinka <mhlavink@redhat.com> - 2013.05.23-1
- updated to 2013.05-23

* Thu Aug 08 2013 Michal Hlavinka <mhlavink@redhat.com> - 2012.09.63-5
- use unversioned docdir (#993677)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.09.63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Michal Hlavinka <mhlavink@redhat.com> - 2012.09.63-3
- add provides, so we can combine CodeSourcery and upstream versions

* Wed Feb 20 2013 Michal Hlavinka <mhlavink@redhat.com> - 2012.09.63-2
- make it build with new texinfo

* Mon Dec 03 2012 Michal Hlavinka <mhlavink@redhat.com> - 2012.09.63-1
- new spec for arm-none-eabi using CodeSourcery release
