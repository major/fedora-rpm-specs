Name: dapl
Version: 2.1.9
Release: 24%{?dist}
Summary: Library providing access to the DAT 2.0 API
# Automatically converted from old format: GPLv2 or BSD or CPL - review is highly recommended.
License: GPL-2.0-only OR LicenseRef-Callaway-BSD OR CPL-1.0
Url: https://www.openfabrics.org/
Source0: https://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
Patch0: dapl-c99.patch
BuildRequires: libibverbs-devel >= 1.2.1
BuildRequires: librdmacm-devel >= 1.1.0
BuildRequires: ibacm-devel
BuildRequires: gcc
BuildRequires: make
Requires: rdma
# Platforms missing in dapl/udapl/linux/dapl_osd.h
ExcludeArch: s390, armv7hl
%description
Along with the RDMA kernel drivers, libdat and libdapl provide
a user-space RDMA API that supports DAT 2.0 specification and IB
transport extensions for atomic operations and RDMA write with
immediate data.

%package devel
Summary: Development files for the libdat and libdapl libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files for libdat and libdapl libraries.

%package static
Summary: Static libdat and libdapl libraries
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static versions of the libdat and libdapl libraries.

%package utils
Summary: Test suites for dapl libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Useful test suites to validate the dapl library APIs and operation.

%prep
%autosetup -p1
find . -type f -iname '*.[ch]' -exec chmod a-x '{}' ';'

%build
%configure --sysconfdir=/etc/rdma
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/rdma/dat.conf
%doc AUTHORS README ChangeLog README.mcm
%license COPYING LICENSE.txt LICENSE2.txt LICENSE3.txt

%files devel
%{_libdir}/*.so
%dir %{_includedir}/dat2
%{_includedir}/dat2/*

%files static
%{_libdir}/*.a

%files utils
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.9-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Florian Weimer <fweimer@redhat.com> - 2.1.9-17
- C99 compatibility fix (#2155655)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Honggang Li <honli@redhat.com> - 2.1.9-3
- Remove unnecessary configuration parameters
- Fix spelling issues
- Add Requires against rdma package
- Resolves: bz1397643

* Sat Nov 26 2016 Honggang Li <honli@redhat.com> - 2.1.9-2
- Drop all the Obsoletes lines
- Removing rpath by patching local libtool
- Add BuildRequires for the C compiler
- Resolves: bz1397643

* Wed Nov 16 2016 Honggang Li <honli@redhat.com> - 2.1.9-1
- Import dapl for Fedora.

* Thu Apr 21 2016 Honggang Li <honli@redhat.com> - 2.1.5-2
- Ensure dapltest with no argument working in ppc64 arch.
- Resolves: bz1056487

* Tue Jun 09 2015 Doug Ledford <dledford@redhat.com> - 2.1.5-1
- Update to latest upstream release
- Include support for s390x
- Include support for aarch64
- Drop old fix for NULL not defined, upstream has it resolved
- Resolves: bz1182180, bz1197216, bz1172462, bz1044727, bz1056487

* Tue Oct 28 2014 Doug Ledford <dledford@redhat.com> - 2.0.39-5
- Bump and rebuild after retagging the latest libibverbs and librdmacm
  into the build root
- Related: bz1123996

* Tue Oct 28 2014 Doug Ledford <dledford@redhat.com> - 2.0.39-4
- Switch from ExclusiveArch to ExcludeArch
- Related: bz1123996

* Tue Sep 09 2014 Dan Horák <dhorak@redhat.com> - 2.0.39-3
- enable on ppc64le
- Resolves: #1123996

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.0.39-2
- Mass rebuild 2013-12-27

* Wed Dec 18 2013 Jay Fenlason <fenlason@redhat.com> - 2.0.39-1
- Upgrade to latest version
  Resolves: rhbz#985117
- Fix a compile problem with NULL not being defined
  Resolves: rhbz#1029509

* Mon Jan 23 2012 Doug Ledford <dledford@redhat.com> - 2.0.34-1
- Update to latest upstream version
- Rebuild against new libibverbs (FDR link speed capable and IBoE enabled)
- Related: bz750609

* Fri Jul 22 2011 Doug Ledford <dledford@redhat.com> - 2.0.32-1
- Update to latest upstream version (2.0.25 -> 2.0.32)
- Remove 4 patches folded into upstream release
- Rebuild against new libibverbs and librdmacm
- Update exclusive arch to accommodate i686 arch
- Related: bz724896, bz725016

* Fri Jan 28 2011 Jay Fenlason <fenlason@redhat.com> 2.0.25-5.2.el6
- Actually install the signal-handler patch
  Resolves: bz667742	Error mapping bug in dapls_wait_comp_channel

* Thu Jan 27 2011 Jay Fenlason <fenlason@redhat.com> 2.0.25-5.1.el6
- dapl-2.0.25-signal-handler.patch
  Resolves: bz667742	Error mapping bug in dapls_wait_comp_channel
- dapl-2.0.25-new-providers.patch
  Resolves: bz636596
- dapl-2.0.25-dat_ia_open_hang.patch
  Resolves: bz649360
- dapl-2.0.25-cleanup-cr-linkings-after-dto-error-on-ep.patch
  Resolves: bz626541
- dapl-2.0.25-verbs-cq-completion-channels-leak.patch
  Resolves: bz637980

* Sun Mar 07 2010 Doug Ledford <dledford@redhat.com> - 2.0.25-5.el6
- I missed that the license was in an invalid form, correct that
- Related: bz555835

* Sun Mar 07 2010 Doug Ledford <dledford@redhat.com> - 2.0.25-4.el6
- Clean up rpmlint warnings about unversioned obsoletes
- Make setup quite
- Include COPYING file in docs
- Fix naked macro in changelog
- Related: bz555835

* Thu Jan 21 2010 Doug Ledford <dledford@redhat.com> - 2.0.25-3.el6
- Update config directory for rhel6 (from /etc/ofed to /etc/rdma)
- Remove compat-dapl and split it off to its own rpm
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 2.0.25-2.el5
- Fix up file lists for upstream binary name changes

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 2.0.25-1.el5
- Update to latest upstream version
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 2.0.19-2
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Fri Jun 19 2009 Doug Ledford <dledford@redhat.com> - 2.0.19-1
- Recompile against non-XRC libibverbs
- Update to OFED 1.4.1 final bits
- Related: bz506258, bz506097

* Fri Apr 24 2009 Doug Ledford <dledford@redhat.com> - 2.0.17-2
- Add -fno-strict-aliasing to CFLAGS

* Thu Apr 16 2009 Doug Ledford <dledford@redhat.com> - 2.0.17-1
- Move the dat-1.2 conf file to /etc/ofed/compat-dapl/dat.conf
- Update to ofed 1.4.1-rc3 versions of dapl
- Related: bz459652

* Thu Oct 16 2008 Doug Ledford <dledford@redhat.com> - 2.0.13-4
- Import the upstream fix for bug 465840
- Related: bz465840

* Mon Oct 13 2008 Doug Ledford <dledford@redhat.com> - 2.0.13-3
- Add a compat-dapl-utils package so people can test their dapl-1.2
  setups
- Even though we tell dapl to look for its config in /etc/ofed, it wasn't
  actually looking there.  Fix that.
- Resolves: bz465841, bz465840

* Wed Sep 17 2008 Doug Ledford <dledford@redhat.com> - 2.0.13-2
- I don't know what I was thinking putting the version into the compat
  dapl packages names...makes upgrades not work and makes things like
  buildrequire compat-dapl-devel not work.  Removed, and we now obsolete
  the existing compat-dapl*-{version} packages.

* Wed Sep 17 2008 Doug Ledford <dledford@redhat.com> - 2.0.13-1
- Update to latest upstream versions for both dapl and compat-dapl
- Resolves: bz451468

* Thu Apr 03 2008 Doug Ledford <dledford@redhat.com> - 2.0.7-2
- Need a new brew build in order to get the filelist correct in the errata
- Related: bz428197

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 2.0.7-1
- Update to same dapl versions as OFED 1.3 final bits
- Upstream modified dapl-1.2 and dapl-2.0 to coexist, so undo the changes we
  made in order for them to coexist in our package
- Related: bz428197

* Tue Jan 29 2008 Doug Ledford <dledford@redhat.com> - 2.0.3-3
- Make dapl-1.2 and dapl-2.0 devel environments coexist, and make dapl-1.2
  the default lib so that unported apps continue to build, and ported apps
  build properly by adding -L%%{_libdir}/dat -ldat to their LDFLAGS.

* Tue Jan 15 2008 Doug Ledford <dledford@redhat.com> - 2.0.3-2
- Import upstream package, gut spec file, copy over dapl spec from openib spec
- Merge dapl 1.2 and 2.0 support into a single rpm
- Related: bz428197

* Tue Nov 20 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.3
- DAT/DAPL Version 2.0.3 Release 1

* Tue Oct 30 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.2
- DAT/DAPL Version 2.0.2 Release 1

* Tue Sep 18 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.1-1
- OFED 1.3-alpha, co-exist with DAT 1.2 library package.  

* Wed Mar 7 2007 Arlin Davis <ardavis@ichips.intel.com> - 2.0.0.pre
- Initial release of DAT 2.0 APIs, includes IB extensions 
