Name:		globus-authz
%global _name %(tr - _ <<< %{name})
Version:	4.6
Release:	9%{?dist}
Summary:	Grid Community Toolkit - Globus authz library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-callout-devel >= 2
BuildRequires:	globus-gssapi-gsi-devel >= 9
BuildRequires:	globus-authz-callout-error-devel >= 2
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	openssl

%package devel
Summary:	Grid Community Toolkit - Globus authz library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus authz library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus authz library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus authz library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus authz library Documentation Files

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
%{_libdir}/libglobus_authz.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_authz.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.6-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.4-5
- Use sha256 hash when generating test certificates
- Fix some compiler warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.4-1
- Minor fixes to makefiles
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.3-1
- Clean up old GPT references

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.2-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (4.0)
- Use 2048 bit RSA key for tests (4.1)

* Sat Sep 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.16-1
- GT6 update: Use 2048 bit keys to support openssl 1.1.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.15-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.15-1
- GT6 update

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.14-1
- GT6 update: Updates for OpenSSL 1.1.0

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.12-1
- GT6 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.11-2
- Extra rebuild for EPEL 7 ppc64le

* Wed Nov 25 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.11-1
- GT6 update (updated tests)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.10-2
- Implement updated license packaging guidelines

* Sun Oct 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.10-1
- GT6 update
- Drop patches globus-authz-doxygen.patch and globus-authz-deps.patch
  (fixed upstream)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.9-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 2.2-9
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Fri Oct 25 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-8
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-6
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-5
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-3
- Add build requires for TexLive 2012

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-authz-doxygen.patch (fixed upstream)

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-1
- Update to Globus Toolkit 5.2.0
- Drop patch globus-authz-deps.patch (fixed upstream)

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.7-4
- Add README file
- Add missing dependencies

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.7-2
- Update to Globus Toolkit 5.0.0

* Tue Jul 28 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.7-1
- Autogenerated
