Name:		globus-xio-gsi-driver
%global _name %(tr - _ <<< %{name})
Version:	5.4
Release:	9%{?dist}
Summary:	Grid Community Toolkit - Globus XIO GSI Driver

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-gss-assist-devel >= 11
BuildRequires:	globus-gssapi-error-devel >= 4
BuildRequires:	globus-gssapi-gsi-devel >= 13
BuildRequires:	globus-common-devel >= 15
BuildRequires:	doxygen
BuildRequires:	perl-interpreter
BuildRequires:	perl(strict)

Requires:	globus-gss-assist%{?_isa} >= 11
Requires:	globus-gssapi-gsi%{?_isa} >= 13

%package devel
Summary:	Grid Community Toolkit - Globus XIO GSI Driver Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus XIO GSI Driver Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus XIO GSI Driver

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus XIO GSI Driver Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus XIO GSI Driver Documentation Files

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

%ldconfig_scriptlets

%files
# This is a loadable module (plugin)
%{_libdir}/libglobus_xio_gsi_driver.so
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4-1
- Typo fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3-1
- Minor fixes to makefiles
- Add BuildRequires perl-interpreter
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2-1
- Update documentation links to always point to the latest documentation

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.1-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-1
- GT6 update: Add SNI and ALPN support via cntls

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.11-1
- GT6 update: Fix crash when checking for anonymous GSS name when name
  comparison fails

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.10-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 11 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.10-1
- GT6 update: Fix anonymous auth in strict mode
- Drop patch globus-xio-gsi-driver-anon.patch (accepted upstream)

* Wed May 11 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.9-2
- Fix broken anonymous authentication

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.9-1
- GT6 update: Propagate error back to caller when name mismatch occurs
  on server instead of just closing the handle

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.8-1
- GT6 update
- GT-615: GSI XIO driver uses resolved IP address when importing names

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.7-1
- GT6 update (handle anonymous targets in GSI RFC2818 mode)

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.6-2
- Implement updated license packaging guidelines

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.6-1
- GT6 update
- Drop patch globus-xio-gsi-driver-doxygen.patch (fixed upstream)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.5-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 2.4-2
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.4-1
- Update to Globus Toolkit 5.2.5
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.3-6
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.3-5
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.3-3
- Add build requires for TexLive 2012

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.3-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-xio-gsi-driver-doxygen.patch (fixed upstream)

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-1
- Update to Globus Toolkit 5.2.0
- Drop patches globus-xio-gsi-driver-deps.patch,
  globus-xio-gsi-driver-funcgrp.patch,
  globus-xio-gsi-driver-type-punned-pointer.patch and
  globus-xio-gsi-driver-wrong-dep.patch (fixed upstream)

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-7
- Add README file
- Add missing dependencies
- Clear dependency libs in .la file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-5
- Update to Globus Toolkit 5.0.1

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-4
- Update to Globus Toolkit 5.0.0

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Thu Jun 04 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-2
- Update to official Fedora Globus packaging guidelines

* Wed Apr 29 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball
- Fix changed dependency namespace

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-0.3
- Adapt to updated GPT package

* Tue Oct 21 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-0.2
- Update to Globus Toolkit 4.2.1

* Tue Jul 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4-0.1
- Autogenerated
