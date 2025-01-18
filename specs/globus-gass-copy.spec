Name:		globus-gass-copy
%global _name %(tr - _ <<< %{name})
Version:	10.13
Release:	3%{?dist}
Summary:	Grid Community Toolkit - Globus Gass Copy

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-ftp-client-devel >= 7
BuildRequires:	globus-ftp-control-devel >= 4
BuildRequires:	globus-gsi-sysconfig-devel >= 4
BuildRequires:	globus-gass-transfer-devel >= 7
BuildRequires:	globus-io-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 9
BuildRequires:	globus-gssapi-error-devel >= 4
BuildRequires:	openssl-devel
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	globus-gridftp-server-devel >= 7
BuildRequires:	globus-gridftp-server-progs >= 7
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

%package progs
Summary:	Grid Community Toolkit - Globus Gass Copy Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package devel
Summary:	Grid Community Toolkit - Globus Gass Copy Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus Gass Copy Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus Gass Copy

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Globus Gass Copy Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus Gass Copy Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus Gass Copy Documentation Files

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
GLOBUS_HOSTNAME=localhost %make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_gass_copy.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_bindir}/globus-url-copy
%doc %{_mandir}/man1/globus-url-copy.1*

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gass_copy.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.13-1
- New GCT release v6.2.20240202

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.12-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.10-4
- Use sha256 hash when generating test certificates
- Fix some compiler and doxygen warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 10.10-2
- Rebuilt with OpenSSL 3.0.0

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.10-1
- Typo fixes

* Tue Aug 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.9-1
- Fix segmentation fault with ~

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.8-1
- Minor fixes to makefiles (10.6)
- Use -nameopt sep_multiline to derive certificate subject string (10.7)
- Document environment variables in globus-url-copy manpage (10.8)
- Add BuildRequires perl-interpreter
- Add additional perl dependencies for tests
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.5-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.5-3
- Add additional perl build dependencies due to perl package split

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.5-1
- Document guc/dcpriv behaviour with servers not supporting DC encryption

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.4-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.3-2
- Bump GCT release version to 6.2

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.3-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (10.0)
- Use 2048 bit RSA key for tests (10.1)
- Merge GT6 update 9.29 into GCT (10.2)
- Split guc-cc.pl test into smaller tests (10.3)

* Sat Sep 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.29-1
- GT6 update: Use 2048 bit keys to support openssl 1.1.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.28-1
- GT6 update

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.27-1
- GT6 update:
  - Don't attempt sshftp data protection without creds (9.24)
  - Checksum verification based on contribution from IBM (9.24)
  - Fix uninitialized field related crash (9.25)
  - Remove checksum data from public handle (9.26)
  - Prevent some race conditions (9.27)

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.23-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Drop the globus-gass-copy-openssl098.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.23-1
- GT6 update: Updated man pages

* Thu Oct 13 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.22-2
- Rebuild for openssl 1.1.0 (Fedora 26)

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.22-1
- GT6 update: Updates for OpenSSL 1.1.0

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.19-1
- GT6 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.18-2
- Extra rebuild for EPEL 7 ppc64le

* Tue Nov 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.18-1
- GT6 update (updated tests)

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.16-1
- GT6 update (Improve error handling, Fix non-terminated string)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.15-1
- GT6 update (user-specified data channel stack handling, documentation)

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.13-2
- Implement updated license packaging guidelines
- Set GLOBUS_HOSTNAME during make check and enable tests on EPEL5 and EPEL6

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.13-1
- GT6 update

* Sun Oct 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.12-1
- GT6 update
- Drop patch globus-gass-copy-doxygen.patch (fixed upstream)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.11-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks
- Disable checks on EPEL5 and EPEL6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 8.6-8
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Fri Oct 25 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-7
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-5
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-4
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-2
- Add build requires for TexLive 2012

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-1
- Update to Globus Toolkit 5.2.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.4-1
- Update to Globus Toolkit 5.2.1
- Drop patches globus-gass-copy-deps.patch, globus-gass-copy-format.patch
  and globus-gass-copy-doxygen.patch (fixed upstream)
- Drop manpage from packaging, now available in upstream source

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.2-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.2-1
- Update to Globus Toolkit 5.2.0
- Drop patches globus-gass-copy-doxygen.patch, globus-gass-copy-mingw.patch
  and globus-gass-copy-pathmax.patch (fixed upstream)

* Sun Oct 02 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.14-3
- Add contributed man page

* Sun Jun 26 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.14-2
- Rebuild

* Fri Jun 03 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.14-1
- Update to Globus Toolkit 5.0.4

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.10-2
- Add README file

* Thu Feb 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.10-1
- Update to Globus Toolkit 5.0.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.7-1
- Update to Globus Toolkit 5.0.2

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.4-1
- Update to Globus Toolkit 5.0.1

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-1
- Update to Globus Toolkit 5.0.0

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.14-4
- rebuilt with new openssl

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Thu Jun 04 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-2
- Update to official Fedora Globus packaging guidelines

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-0.3
- Adapt to updated GPT package

* Tue Oct 21 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.14-0.2
- Update to Globus Toolkit 4.2.1

* Tue Jul 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.10-0.1
- Autogenerated
