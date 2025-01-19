Name:		libdfp
Version:	1.0.16
Release:	12%{?dist}
Summary:	Decimal Floating Point C Library
License:	LGPL-2.1-or-later
Url:		https://github.com/libdfp/libdfp
Source0:	https://github.com/libdfp/libdfp/releases/download/%{version}/%{name}-%{version}.tar.gz
#
# Patches from upstream
#
Patch1: bz2045793.patch
Patch2: bz2261309.patch

# Be explicit about the soname in order to avoid unintentional changes.
%global soname libdfp.so.1

# Select which different cpu variants are build in addition to the default one
%ifarch ppc ppc64
%global cpu_variants power6
%endif

ExclusiveArch:	ppc ppc64 ppc64le s390 s390x x86_64
BuildRequires: make
BuildRequires:	gcc, python3
%if 0%{?cpu_variants:1}
BuildRequires:	execstack
%endif

%description
The "Decimal Floating Point C Library" is an implementation of ISO/IEC
Technical report  "ISO/IEC TR 24732" which describes the C-Language library
routines necessary to provide the C library runtime support for decimal
floating point data types introduced in IEEE 754-2008, namely _Decimal32,
_Decimal64, and _Decimal128.

%package	devel
Summary:	Development files for %{name}
# Use _isa to specify an arch-specific requirement.
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	static
Summary:	Static libraries for %{name}
License:	LGPL-2.1-or-later AND GPL-3.0-or-later WITH GCC-exception-3.1
# Use _isa to specify an arch-specific requirement.
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	static
The %{name}-static package contains static libraries for developing
applications that use %{name}.

%prep
%autosetup -p1

%define subdir_configure \
cat >configure <<'EOF'\
#!/bin/sh\
exec ../${0##*/} "$@"\
EOF\
chmod +x configure \
%configure

%build
# This package uses ASMs for symbol versioning.  It needs to be using
# the symbol verioning attribute instead.  Until then disable LTO
%define _lto_cflags %{nil}

mkdir Build
pushd Build
%subdir_configure --disable-static
%make_build
popd
%if 0%{?cpu_variants:1}
for cpu in %{cpu_variants}; do
  mkdir Build-$cpu
  pushd Build-$cpu
  %subdir_configure --disable-static --with-cpu=$cpu
  make %{?_smp_mflags}
  popd
done
%endif

%check
pushd Build
make -k %{?_smp_mflags} check
popd
%if 0%{?cpu_variants:1}
for cpu in %{cpu_variants}; do
  pushd Build-$cpu
  make -k %{?_smp_mflags} check
  popd
done
%endif

%install
pushd Build
%make_install
popd
%if 0%{?cpu_variants:1}
for cpu in %{cpu_variants}; do
  pushd Build-$cpu
  mkdir -p %{buildroot}%{_libdir}/$cpu
  install -m 755 libdfp-%{version}.so %{buildroot}%{_libdir}/$cpu
  ldconfig -l %{buildroot}%{_libdir}/$cpu/libdfp-%{version}.so
  execstack -c %{buildroot}%{_libdir}/$cpu/libdfp-%{version}.so
  if test $cpu = power6; then
    mkdir -p %{buildroot}%{_libdir}/${cpu}x
    pushd %{buildroot}%{_libdir}/${cpu}x
    ln -sf ../$cpu/*.so .
    cp -a ../$cpu/*.so.* .
    popd
  fi
  popd
done
%endif

%ldconfig_scriptlets

%files
%{_libdir}/%{soname}
%{_libdir}/%{name}-%{version}.so
%if 0%{?cpu_variants:1}
%(for cpu in %{cpu_variants}; do echo %dir %{_libdir}/$cpu; test $cpu = power6 && echo %dir %{_libdir}/${cpu}x; done)
%{_libdir}/*/%{soname}
%{_libdir}/*/%{name}-%{version}.so
%endif
%doc %{_docdir}/dfp/README
%doc %{_docdir}/dfp/ChangeLog.md
%license COPYING.txt
%doc %{_docdir}/dfp/COPYING.txt
%doc %{_docdir}/dfp/COPYING.libdfp.txt
%doc %{_docdir}/dfp/COPYING.libdecnumber.txt
%doc %{_docdir}/dfp/COPYING3
%doc %{_docdir}/dfp/COPYING.RUNTIME

%files devel
%{_includedir}/dfp/*
%{_libdir}/*.so
%exclude %{_libdir}/*-*.so
%{_libdir}/pkgconfig/libdfp.pc

%files static
%{_includedir}/decnumber/*
%{_libdir}/libdecnumber.a
%{_libdir}/pkgconfig/libdecnumber.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Paul E. Murphy <murphyp@linux.ibm.com> - 1.0.16-10
- Fix upstream issue #189

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 1.0.16-6
- Update licenses to SPDX indentifiers.
- Add the license GPL-3.0-or-later WITH GCC-exception-3.1 in order to cover
  libdecnumber distributed in the -static package.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.16-3
- Fix bug 2045793.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.16-1
- Update to libdfp 1.0.16.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.15-8
- Fix bug #1923668 after Fedora started to use GCC 11.
- Add a patch to ignore test failures when LTO is enabled even if LTO is not
  enabled yet. This may help to solve test failures on s390x.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.15-6
- Move libdecnumber to the static package.

* Thu Aug 06 2020 Jeff Law <law@redhat.com> - 1.0.15-5
- Disable LTO

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.15-2
- Enable builds for x86_64.

* Tue Jul 14 2020 Stefan Liebler <stli@linux.ibm.com> - 1.0.15-1
- Update to new release libdfp 1.0.15

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.14-7
- Re-add _isa to the requirement of the devel package.

* Wed Oct 09 2019 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.14-6
- Removed parameter -n from the prep section.
- Removed defattr usage from the devel files.

* Tue Oct 08 2019 Tulio Magno Quites Machado Filho <tuliom@linux.ibm.com> - 1.0.14-5
- Add support for DESTDIR.
- Remove extra license patch in order to use license.
- Make usage of scriptlets make_build, make_install and
  ldconfig_scriptlets.
- Prevent unintentional soname bumps by specifying it via soname.
- Use global instead of define for cpu_variants.
- Remove unintentional usage of _isa.

* Wed Sep 04 2019 Stefan Liebler <stli@linux.ibm.com> - 1.0.14-4
- Fix License tag.
- Package COPYING.txt and use it with license macro.
  (see libdfp-license.patch and upstream pull-request
  https://github.com/libdfp/libdfp/pull/86)
- Remove Group and BuildRoot tags.
- Use buildroot macro instead of RPM_BUILD_ROOT variable.
- Do not remove buildroot during install step.
- Use pushd/popd instead of cd commands.
- Remove clean section.
- Fix changelog in order to not include macros.
- Print summary of failing tests in the output of make check.
  (see libdfp-tests.patch and upstream pull-request
  https://github.com/libdfp/libdfp/pull/87)

* Tue Aug 20 2019 Tulio Magno <tuliom@linux.ibm.com> - 1.0.14-3
- Run the tests on all cpu_variants.

* Tue Aug 20 2019 Stefan Liebler <stli@linux.ibm.com> - 1.0.14-2
- Remove prelink build requirement.  Prevent execstack from being required
  when macro cpu_variants is not set.
  Remove z9-ec from macro cpu_variants.

* Wed Aug 14 2019 Tulio Magno <tuliom@linux.ibm.com> - 1.0.14-1
- Rebase to libdfp-1.0.14.  Improve package description.
  Enable execstack for ppc64le.
  Enable execution of tests.

* Wed Feb 19 2014 Jeff Law <schwab@redhat.com> - 1.0.9-1
- Rebase to libdfp-1.0.9-1 to bring in ppc64le support.
  Requires disabling execstack for ppc64le due to lack of
  availability

* Wed Feb 19 2014 Jeff Law <law@redhat.com> - 1.0.8-5
- Clear executable stack on the cpu_variants builds since
  they may contain objects built from assembly which do not
  contain the magic tags.  BuildRequires: prelink (#804765)

* Mon Feb  3 2014 Daniel Mach <dmach@redhat.com> - 1.0.8-4
- Mass rebuild 2014-01-24

* Fri Oct 26 2012 Jeff Law <law@redhat.com> - 1.0.8-3
- Bump release in the hopes it'll make package wrangler
  import the new bits and do the right thing.

* Fri Sep 7 2012 Jeff Law <law@redhat.com> - 1.0.8-2
- Add URL tag to spec file.

* Mon Jun 11 2012 Jeff Law <law@redhat.com> - 1.0.8-1
- resync with upstream sources r17008 (#804765)

* Wed May 12 2010 Andreas Schwab <schwab@redhat.com> - 1.0.1-2
- Enable building on s390/s390x (#464229)

* Wed Jan 27 2010 Andreas Schwab <schwab@redhat.com> - 1.0.1-1
- Initial version 1.0.1
