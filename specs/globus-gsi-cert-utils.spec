Name:		globus-gsi-cert-utils
%global _name %(tr - _ <<< %{name})
Version:	10.11
Release:	3%{?dist}
Summary:	Grid Community Toolkit - Globus GSI Cert Utils Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-openssl-module-devel >= 3
BuildRequires:	globus-gsi-openssl-error-devel >= 2
BuildRequires:	openssl-devel
BuildRequires:	openssl
BuildRequires:	doxygen
BuildRequires:	perl-generators

%package progs
Summary:	Grid Community Toolkit - Globus GSI Cert Utils Library Programs
Requires:	openssl
BuildArch:	noarch

%package devel
Summary:	Grid Community Toolkit - Globus GSI Cert Utils Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus GSI Cert Utils Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus GSI Cert Utils Library

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Globus GSI Cert Utils Library Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus GSI Cert Utils Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus GSI Cert Utils Library Documentation Files

%prep
%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export GLOBUS_VERSION=6.2
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
%{_libdir}/libglobus_gsi_cert_utils.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_bindir}/grid-cert-info
%{_bindir}/grid-cert-request
%{_bindir}/grid-change-pass-phrase
%{_sbindir}/globus-update-certificate-dir
%{_sbindir}/grid-default-ca
%doc %{_mandir}/man1/grid-cert-info.1*
%doc %{_mandir}/man1/grid-cert-request.1*
%doc %{_mandir}/man1/grid-change-pass-phrase.1*
%doc %{_mandir}/man8/globus-update-certificate-dir.8*
%doc %{_mandir}/man8/grid-default-ca.8*
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gsi_cert_utils.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.11-1
- New GCT release v6.2.20240202
- Drop patches included in the release

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.10-5
- Fix handling of certificate expire dates after 2050

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.10-1
- New GCT release v6.2.20220524

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 10.8-2
- Rebuilt with OpenSSL 3.0.0

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.8-1
- Typo fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.7-1
- Minor fixes to makefiles (10.4)
- Remove old replace-version.xsl file (10.5)
- Fix format for grid-cert-info -issuer (10.6)
- Use -nameopt sep_multiline to derive certificate subject string (10.7)
- Specfile updates
- Drop ancient Obsoletes tags

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.3-1
- Update additional old document references

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.2-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.1-1
- Fix broken subject in grid-cert-request
- Bump GCT release version to 6.2

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.16-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Drop the globus-gsi-cert-utils-openssl098.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.16-1
- GT6 update: Add const qualifier to avoid casting with OpensSL 1.1.0

* Tue Nov 08 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.15-2
- Add BR openssl

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.15-1
- GT6 update: Updated man pages

* Thu Oct 13 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.14-2
- Rebuild for openssl 1.1.0 (Fedora 26)

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.14-1
- GT6 update: Updates for OpenSSL 1.1.0

* Fri May 06 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.12-1
- GT6 update: Spelling

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.11-1
- GT6 update (Fix encoding for CN=(limited) proxy, globus-gsi-cert-utils crash)
- Enable checks

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.10-2
- Implement updated license packaging guidelines

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.10-1
- GT6 update
- Drop patches globus-gsi-cert-utils-deps.patch and
  globus-gsi-cert-utils-doxygen.patch (fixed upstream)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.9-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Brent Baude <baude@us.ibm.com> - 8.6-3
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Dec 05 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-2
- Remove directory man page

* Wed Nov 06 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-1
- Update to Globus Toolkit 5.2.5
- Drop patches globus-gsi-cert-utils-ac.patch and
  globus-gsi-cert-utils-doxygen.patch (accepted upstream)
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.3-6
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.3-5
- Add aarch64 to the list of 64 bit platforms
- Don't use AM_CONFIG_HEADER (automake 1.13)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.3-3
- Add build requires for TexLive 2012

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.3-1
- Update to Globus Toolkit 5.2.1
- Drop patches globus-gsi-cert-utils-msg.patch,
  globus-gsi-cert-utils-deps.patch and globus-gsi-cert-utils-format.patch
  (fixed upstream)

* Mon Jan 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1-2
- Fix broken links in README file

* Tue Dec 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1-1
- Update to Globus Toolkit 5.2.0
- Drop patch globus-gsi-cert-utils-ca-setup.patch (fixed upstream)

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.7-2
- Add README file

* Fri Feb 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.7-1
- Update to Globus Toolkit 5.0.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.6-1
- Update to Globus Toolkit 5.0.2
- Drop patch globus-gsi-cert-utils-oid.patch (fixed upstream)

* Mon May 31 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.5-2
- Fix OID registration pollution

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.5-1
- Update to Globus Toolkit 5.0.1

* Fri Jan 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.4-1
- Update to Globus Toolkit 5.0.0

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 5.5-4
- rebuilt with new openssl

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Wed Jun 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-2
- Update to official Fedora Globus packaging guidelines

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-1
- Change defines to globals
- Remove explicit requires on library packages

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-0.4
- Add s390x to the list of 64 bit platforms
- Update to upstream update release 5.5
- Drop the environment elimination patch (accepted upstream)

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0-0.3
- Adapt to updated GPT package

* Tue Oct 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.1-0.1
- Autogenerated
