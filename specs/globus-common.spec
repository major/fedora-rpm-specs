Name:		globus-common
%global _name %(tr - _ <<< %{name})
Version:	18.14
Release:	3%{?dist}
Summary:	Grid Community Toolkit - Common Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libtool-ltdl-devel
BuildRequires:	doxygen
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter

#		Obsolete dropped packages from GCT
Obsoletes:	globus-usage < 6

%package progs
Summary:	Grid Community Toolkit - Common Library Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package devel
Summary:	Grid Community Toolkit - Common Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libtool-ltdl-devel
#		Obsolete dropped packages from GCT
Obsoletes:	globus-usage-devel < 6

%package doc
Summary:	Grid Community Toolkit - Common Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Common Library

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Common Library Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Common Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Common Library Documentation Files

%prep
%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export GLOBUS_VERSION=6.2
export SH=/bin/sh
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-backward-compatibility-hack

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

# Remove environment scripts
rm %{buildroot}%{_datadir}/globus-user-env.csh
rm %{buildroot}%{_datadir}/globus-user-env.sh

%check
%make_build check NO_EXTERNAL_NET=1

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_common.so.*
%{_libdir}/libglobus_memory_debug.so.*
# This is a loadable module (plugin)
%{_libdir}/libglobus_thread_pthread.so
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/Core
%{perl_vendorlib}/Globus/Core/Config.pm
%{perl_vendorlib}/Globus/Core/Paths.pm
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_bindir}/globus-domainname
%{_bindir}/globus-hostname
%{_bindir}/globus-sh-exec
%{_bindir}/globus-version
%{_sbindir}/globus-libc-hostname
%{_sbindir}/globus-redia
%dir %{_datadir}/globus
%{_datadir}/globus/config.guess
%{_datadir}/globus/globus-args-parser-header
%{_datadir}/globus/globus-script-initializer*
%{_datadir}/globus/globus-sh-tools.sh
%{_datadir}/globus/globus-sh-tools-vars.sh
%doc %{_mandir}/man1/globus-domainname.1*
%doc %{_mandir}/man1/globus-hostname.1*
%doc %{_mandir}/man1/globus-sh-exec.1*
%doc %{_mandir}/man1/globus-version.1*

%files devel
%dir %{_includedir}/globus
%{_includedir}/globus/*
%{_libdir}/libglobus_common.so
%{_libdir}/libglobus_memory_debug.so
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/globus-makefile-header

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 18.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.14-1
- New GCT release v6.2.20240202

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.13-2
- Rebuild with correct perl version (EPEL 8)

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 18.13-2
- Perl 5.36 rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.13-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.11-3
- Fix some compiler and doxygen warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.11-1
- Typo fixes

* Tue Aug 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.10-1
- Doxygen fix

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 18.9-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.9-1
- For pure IP addresses globus-domainname should be empty (18.6)
- Minor fixes to makefiles (18.7)
- Remove unused doxygen filter (18.8)
- Check for LTO use in CFLAGS instead of LDFLAGS (18.9)
- Specfile updates
- Drop patch globus-common-check-lto-in-cflags.patch (accepted upstream)
- Drop ancient Obsoletes tags

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.5-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.5-4
- Check for LTO in CFLAGS instead of LDFLAGS
- Add BuildRequires perl-interpreter

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 18.5-3
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.5-1
- Clean up old GPT reference (18.3)
- Make symbol versioning work with link time optimization (LTO) (18.4)
- Remove unused perlmoduledir reference (18.5)
- Obsolete globus-usage packages

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 18.2-2
- Perl 5.30 rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.2-1
- Doxygen fixes (18.1)
- Fix FTBR (failed to build reproducibly) (18.2)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.0-2
- Bump GCT release version to 6.2

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 18.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release
- Drop the globus-core.pc file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 17.4-2
- Perl 5.28 rebuild

* Sat Apr 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 17.4-1
- GT6 update:
  - Use win compatible unsetenv (17.3)
  - win32 fix (17.4)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 17.2-1
- GT6 update: Fix regex for perl 5.26 compatibility
- Drop patch globus-common-perl-5.26.patch (accepted upstream)

* Fri Aug 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 17.1-6
- Adapt to perl 5.26 syntax

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 17.1-3
- Perl 5.26 rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 17.1-2
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Mar 17 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 17.1-1
- GT6 update: Add additional error handling api

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 16.9-1
- GT6 update: Fix crash in globus_eval_path

* Thu Nov 03 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 16.8-1
- GT6 update: Updated man pages

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 16.7-1
- GT6 update: Updates for running thread tests without installing

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 16.4-2
- Perl 5.24 rebuild

* Fri May 06 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 16.4-1
- GT6 update: Spelling

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 16.3-1
- GT6 update

* Tue Mar 15 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 16.2-1
- GT6 update: Fix missing doxygen comment header

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 16.0-1
- GT6 update (add globus_extension_get_module_version)

* Sat Jun 20 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 15.30-1
- GT6 update (make globus-version executable during build time)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 15.29-2
- Perl 5.22 rebuild

* Wed Apr 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 15.29-1
- GT6 update
- Drop patch globus-common-disable-network-tests.patch
  Use NO_EXTERNAL_NET environment variable implemented upstream instead

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 15.27-2
- Implement updated license packaging guidelines

* Wed Jan 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 15.27-1
- GT6 update (globus_list_from_string)

* Sun Oct 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 15.26-1
- GT6 update
- Drop patches globus-common-doxygen.patch and globus-common-pkgconfig.patch
  (fixed upstream)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 15.25-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 14.10-6
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Brent Baude <baude@us.ibm.com> - 14.10-3
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Dec 05 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.10-2
- Remove directory man page

* Wed Nov 06 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.10-1
- Update to Globus Toolkit 5.2.5
- Drop patch globus-common-ac.patch (accepted upstream)
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.9-5
- Implement updated packaging guidelines

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 14.9-4
- Perl 5.18 rebuild

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.9-3
- Add aarch64 to the list of 64 bit platforms
- Don't use AM_CONFIG_HEADER (automake 1.13)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.9-1
- Update to Globus Toolkit 5.2.3

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.7-1
- Update to Globus Toolkit 5.2.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 14.6-2
- Perl 5.16 rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.6-1
- Update to Globus Toolkit 5.2.1
- Drop patches globus-common-initializers.patch, globus-common-format.patch,
  globus-common-doxygen.patch and globus-common-sh-env.patch implemented
  upstream
- Drop manpages from packaging that are now included in upstream sources

* Thu Feb 02 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-4
- Add missing default to GLOBUS_SH_* variables

* Sat Jan 28 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-3
- Add dependency on -progs to -devel for globus-makefile-header

* Mon Jan 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-2
- Fix broken links in README file

* Tue Dec 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-1
- Update to Globus Toolkit 5.2.0
- Drop patches implemented upstream

* Sun Oct 02 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.6-5
- Add contributed manpages

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 11.6-4
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 11.6-3
- Perl 5.14 mass rebuild

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.6-2
- Add README file

* Wed Feb 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.6-1
- Update to Globus Toolkit 5.0.3
- Try to ensure that most of globus-sh-tools-vars.sh gets filled

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 06 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.5-3
- Updated pthread exception patch for better compatibility with boost's headers

* Sun Aug 08 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.5-2
- Fix perl dependencies (use vs. require)

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.5-1
- Update to Globus Toolkit 5.0.2

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 11.4-2
- Mass rebuild with perl-5.12.0

* Tue Apr 13 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.4-1
- Update to Globus Toolkit 5.0.1

* Wed Feb 24 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.2-2
- Make the globus-version script return the right value

* Thu Jan 21 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.2-1
- Update to Globus Toolkit 5.0.0

* Fri Dec 04 2009 Stepan Kasal <skasal@redhat.com> - 10.2-9
- rebuild against perl 5.10.1

* Sun Nov 08 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-8
- Let globus-makefile-header fail gracefully when GPT is not present
- Workaround a bug in doxygen

* Mon Aug 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-7
- Patch globus_location function to allow unset GLOBUS_LOCATION
- Put back config.guess file

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-6
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch
- Replace /usr/bin/env shebangs

* Tue Jun 02 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-5
- Update to official Fedora Globus packaging guidelines

* Mon Apr 27 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-4
- Rebuild with updated libtool

* Tue Apr 21 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-3
- Put GLOBUS_LICENSE file in extracted source tarball

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-2
- Remove config.guess file

* Tue Apr 07 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-1
- Change defines to globals

* Mon Apr 06 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.6
- Make comment about source retrieval more explicit

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.4
- Add s390x to the list of 64 bit platforms
- Move globus-makefile-header to devel package

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.3
- Adapt to updated GPT package

* Wed Oct 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.1
- Autogenerated
