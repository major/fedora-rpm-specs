Name:		globus-xio
%global _name %(tr - _ <<< %{name})
Version:	6.6
Release:	8%{?dist}
Summary:	Grid Community Toolkit - Globus XIO Framework

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	doxygen
BuildRequires:	perl-interpreter
BuildRequires:	perl(strict)
#		Additional requirements for make check
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(lib)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)

%package devel
Summary:	Grid Community Toolkit - Globus XIO Framework Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus XIO Framework Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus XIO Framework

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus XIO Framework Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus XIO Framework Documentation Files

%prep
%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

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

%check
GLOBUS_HOSTNAME=localhost %make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_xio.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_xio.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.6-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5-3
- Fix some compiler and doxygen warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5-1
- Typo fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.4-1
- Minor fixes to makefiles (6.3)
- Fix spelling (6.4)
- Add BuildRequires perl-interpreter
- Add additional perl dependencies for tests
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2-3
- Add additional perl build dependencies due to perl package split

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2-1
- Clean up old GPT references

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.17-1
- GT6 update: Fix udp dual stack sockets when ipv6only is the default

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.16-1
- GT6 update:
  - Don't rely on globus_error_put(NULL) to be GLOBUS_SUCCESS (5.15)
  - Fix crash in error handling in http driver (5.16)

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.14-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.14-1
- GT6 update: Don't crash when GLOBUS_TCP_PORT_RANGE has the same min and max

* Fri Sep 02 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.13-1
- GT6 update

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.12-1
- GT6 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.11-1
- GT6 update (Fix failures connecting to IPv4 mapped addresses on
  systems that disable dual stack sockets by default)

* Fri Nov 06 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.10-1
- GT6 update
  - Clarify documentation for timeouts
  - Remove NET+OS fragments

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-1
- GT6 update
  - Allow const string option names
  - Fix miscount of string length in GLOBUS_XIO_GET_STRING_OPTIONS
  - Fix some error handling bugs
  - Remove some unused variables

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8-1
- GT6 update (Check push result in globus_xio_driver_list_to_stack_attr)

* Tue Feb 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.7-1
- GT6 update (Prefer IPv6 address)

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.4-1
- Implement updated license packaging guidelines
- GT6 update (test fixes)

* Wed Jan 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2-1
- GT6 update (GLOBUS_XIO_GET_STRING_OPTIONS, GLOBUS_XIO_GET_DRIVER_NAME)
- Set GLOBUS_HOSTNAME during make check

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.17-1
- GT6 update
- Drop patches globus-xio-http-tests-localhost.patch and
  globus-xio-http-tests-header-name-value.patch (fixed upstream)

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.15-1
- GT6 update
- Drop patch globus-xio-doxygen.patch (fixed upstream)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 3.6-3
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Dec 05 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.6-2
- Remove directory man pages

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.6-1
- Update to Globus Toolkit 5.2.5
- Drop patches globus-xio-ac.patch and globus-xio-doxygen.patch (fixed
  upstream)
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.3-6
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.3-5
- Add aarch64 to the list of 64 bit platforms
- Don't use AM_CONFIG_HEADER (automake 1.13)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.3-3
- Add build requires for TexLive 2012

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.3-1
- Update to Globus Toolkit 5.2.1

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-1
- Update to Globus Toolkit 5.2.0
- Drop patches globus-xio-bad-age.patch, globus-xio-doxygen.patch,
  globus-xio-format.patch, globus-xio-mingw.patch and
  globus-xio-type-punned-pointer.patch (fixed upstream)

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-4
- Add README file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-2
- Update to Globus Toolkit 5.0.0

* Wed Jul 29 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-1
- Update to upstream update release 2.8

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-5
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Wed Jun 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-4
- Update to official Fedora Globus packaging guidelines

* Mon Apr 27 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-3
- Rebuild with updated libtool

* Mon Apr 20 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-2
- Put GLOBUS_LICENSE file in extracted source tarball

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-0.3
- Adapt to updated GPT package

* Mon Oct 20 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-0.1
- Autogenerated
