Name:		globus-gss-assist
%global _name %(tr - _ <<< %{name})
Version:	12.7
Release:	8%{?dist}
Summary:	Grid Community Toolkit - GSSAPI Assist library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gsi-sysconfig-devel >= 7
BuildRequires:	globus-gsi-cert-utils-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 13
BuildRequires:	globus-callout-devel >= 2
BuildRequires:	globus-gsi-credential-devel >= 6
BuildRequires:	doxygen
BuildRequires:	perl-generators
#		Additional requirements for make check
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(English)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)

Requires:	globus-gsi-sysconfig%{?_isa} >= 7
Requires:	globus-gssapi-gsi%{?_isa} >= 13

%package progs
Summary:	Grid Community Toolkit - GSSAPI Assist library Programs
BuildArch:	noarch

%package devel
Summary:	Grid Community Toolkit - GSSAPI Assist library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GSSAPI Assist library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GSSAPI Assist library

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
GSSAPI Assist library Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GSSAPI Assist library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GSSAPI Assist library Documentation Files

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
%make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_gss_assist.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_sbindir}/grid-mapfile-add-entry
%{_sbindir}/grid-mapfile-check-consistency
%{_sbindir}/grid-mapfile-delete-entry
%doc %{_mandir}/man8/grid-mapfile-add-entry.8*
%doc %{_mandir}/man8/grid-mapfile-check-consistency.8*
%doc %{_mandir}/man8/grid-mapfile-delete-entry.8*
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gss_assist.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.7-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.6-3
- Use sha256 hash when generating test certificates

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.6-1
- Typo fixes

* Tue Aug 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.5-1
- Minor bug fixes and code maintenance

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.4-1
- Minor fixes to makefiles (12.3)
- Add force option to grid-mapfile-add-entry if the users do not exist (12.4)
- Add BuildRequires perl-interpreter
- Add additional perl dependencies for tests
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.2-4
- Add additional perl build dependencies due to perl package split

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.2-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.1-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (12.0)
- Use 2048 bit RSA key for tests (12.1)

* Sat Sep 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.2-1
- GT6 update: Use 2048 bit keys to support openssl 1.1.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.1-1
- GT6 update: race condition and dependency packaging fixes
- Drop patches globus-gss-assist-deps.patch and globus-gss-assist-race.patch
  (accepted upstream)

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.0-2
- Fix race condition in the Makefile in test directory

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.0-1
- GT6 update: Add new function gss_assist_read_vhost_cred_dir() for SNI server

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.21-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.21-1
- GT6 update: Slow grid-mapfile-delete-entry (issue #84)

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.20-1
- GT6 update: Updated man pages

* Sat Sep 03 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.19-1
- GT6 update: Fix grid-mapfile-add-entry is slow (issue #69)

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.17-1
- GT6 update: Updates for OpenSSL 1.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.15-1
- GT6 update (Fix gridmap parsing error)

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.14-1
- GT6 update (Fix uninitialized variable)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.13-2
- Implement updated license packaging guidelines

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.13-1
- GT6 update
- Drop patch globus-gss-assist-doxygen.patch (fixed upstream)

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.12-1
- GT6 update
- Update patch globus-gss-assist-doxygen.patch

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.11-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 9.0-2
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.0-1
- Update to Globus Toolkit 5.2.5
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.7-4
- Implement updated packaging guidelines

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 8.7-3
- Perl 5.18 rebuild

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.7-2
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 20 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.7-1
- Update to Globus Toolkit 5.2.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-2
- Add build requires for TexLive 2012

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-1
- Update to Globus Toolkit 5.2.2
- Drop patch globus-gss-assist-mingw.patch (fixed upstream)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.5-1
- Update to Globus Toolkit 5.2.1
- Drop patches globus-gss-assist-doxygen.patch, globus-gss-assist-deps.patch
  and globus-gss-assist-format.patch (fixed upstream)

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1-1
- Update to Globus Toolkit 5.2.0
- Drop patches globus-gss-assist-normalization.patch and
  globus-gss-assist-gridmapdir.patch (fixed upstream)

* Fri Jun 03 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.10-1
- Update to Globus Toolkit 5.0.4
- Fix doxygen markup

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-4
- Add README file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 18 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-2
- Move client man pages to progs package

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-1
- Update to Globus Toolkit 5.0.2

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8-1
- Update to Globus Toolkit 5.0.1

* Fri Jan 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-1
- Update to Globus Toolkit 5.0.0

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Wed Jun 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-2
- Update to official Fedora Globus packaging guidelines

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.3
- Adapt to updated GPT package

* Wed Oct 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.25-0.1
- Autogenerated
