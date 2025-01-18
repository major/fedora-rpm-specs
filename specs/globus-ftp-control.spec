Name:		globus-ftp-control
%global _name %(tr - _ <<< %{name})
Version:	9.10
Release:	8%{?dist}
Summary:	Grid Community Toolkit - GridFTP Control Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gss-assist-devel >= 11
BuildRequires:	globus-gssapi-gsi-devel >= 13
BuildRequires:	globus-io-devel >= 11
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-gssapi-error-devel >= 4
BuildRequires:	globus-xio-gsi-driver-devel >= 4
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	openssl

Requires:	globus-gss-assist%{?_isa} >= 11
Requires:	globus-gssapi-gsi%{?_isa} >= 13
Requires:	globus-io%{?_isa} >= 11
Requires:	globus-xio-gsi-driver%{?_isa} >= 4

%package devel
Summary:	Grid Community Toolkit - GridFTP Control Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GridFTP Control Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GridFTP Control Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GridFTP Control Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GridFTP Control Library Documentation Files

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
%{_libdir}/libglobus_ftp_control.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_ftp_control.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.10-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.7-3
- Use sha256 hash when generating test certificates
- Fix some compiler and doxygen warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.7-1
- Typo fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.6-1
- Minor fixes to makefiles (9.5)
- Use -nameopt sep_multiline to derive certificate subject string (9.6)
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.4-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.3-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (9.0)
- Use 2048 bit RSA key for tests (9.1)
- Merge GT6 update 8.4 into GCT (9.2)
- Merge GT6 update 8.5 into GCT (9.3)

* Sat Sep 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.6-1
- GT6 update: Use 2048 bit keys to support openssl 1.1.1

* Sun Jul 15 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.5-1
- GT6 update: Force encryption on TLS control channel

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.4-1
- GT6 update: Check for missing signing policy req flag

* Sat Apr 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.3-1
- GT6 update: Default to host authz when using TLS control channel

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2-1
- GT6 update: Fix leak

* Sun Sep 24 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.1-1
- GT6 update: Reading when EOF will result in callback indicating EOF instead
  of error

* Mon Sep 11 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.0-2
- Correct misspelled _isa macro

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.0-1
- GT6 update: Add function globus_ftp_control_use_tls() for TLS control channel

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 7.8-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Fri Jul 28 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.8-1
- GT6 update: Fix hang/failure when using udt driver with local client transfer

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.7-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.7-1
- GT6 update: Improve forced ordering

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.4-1
- GT6 update: Updates for OpenSSL 1.1.0

* Tue Jul 26 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.2-1
- GT6 update (Add buffering to data ordering mode)

* Fri Jul 15 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.1-1
- GT6 update (Add forced ordering option)

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.10-1
- GT6 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.8-1
- GT6 update (GT-594: enable keepalives)

* Mon Jul 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.7-1
- GT6 update (Fix old-style function definitions, Fix variable scope)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.6-1
- Implement updated license packaging guidelines
- GT6 update (test fixes, missing return value)
- Set GLOBUS_HOSTNAME during make check

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.3-1
- GT6 update
- Drop patches globus-ftp-control-memleak.patch and
  globus-ftp-control-tests-localhost.patch (fixed upstream)

* Sun Oct 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.12-1
- GT6 update
- Drop patch globus-ftp-control-doxygen.patch (fixed upstream)

* Tue Sep 30 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.11-2
- Fix memory leak

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.11-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 4.7-2
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.7-1
- Update to Globus Toolkit 5.2.5
- Drop patch globus-ftp-control-authinfo.patch (fixed upstream)
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.5-4
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.5-3
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 27 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.5-2
- Fix modification to wrong authinfo object

* Wed Feb 20 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.5-1
- Update to Globus Toolkit 5.2.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.4-3
- Add build requires for TexLive 2012

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.4-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-ftp-control-deps.patch (fixed upstream)

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.2-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.2-1
- Update to Globus Toolkit 5.2.0
- Drop patches globus-ftp-control-backcompat.patch,
  globus-ftp-control-doxygen.patch, globus-ftp-control-format.patch and
  globus-ftp-control-type-punned-pointer.patch (fixed upstream)

* Thu Jun 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.12-2
- Fix backward incompatibility

* Fri Jun 03 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.12-1
- Update to Globus Toolkit 5.0.4

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.11-3
- Add README file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.11-1
- Update to Globus Toolkit 5.0.0

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Thu Jun 04 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-2
- Update to official Fedora Globus packaging guidelines

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-0.3
- Adapt to updated GPT package

* Mon Oct 20 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-0.2
- Update to Globus Toolkit 4.2.1

* Tue Jul 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-0.1
- Autogenerated
