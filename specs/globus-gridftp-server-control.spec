Name:		globus-gridftp-server-control
%global _name %(tr - _ <<< %{name})
Version:	9.3
Release:	9%{?dist}
Summary:	Grid Community Toolkit - Globus GridFTP Server Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
#		https://github.com/gridcf/gct/pull/223
Patch0:		0001-Handle-64-bit-time_t-on-32-bit-systems.patch
#		https://github.com/gridcf/gct/pull/226
Patch1:		0001-Passing-argument-from-incompatible-pointer-type.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-xio-gsi-driver-devel >= 2
BuildRequires:	globus-xio-pipe-driver-devel >= 2
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 10
BuildRequires:	globus-gsi-openssl-error-devel >= 2
BuildRequires:	globus-gssapi-error-devel >= 4

Requires:	globus-xio-gsi-driver%{?_isa} >= 2
Requires:	globus-xio-pipe-driver%{?_isa} >= 2

%package devel
Summary:	Grid Community Toolkit - Globus GridFTP Server Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus GridFTP Server Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus GridFTP Server Library Development Files

%prep
%setup -q -n %{_name}-%{version}
%patch -P0 -p4
%patch -P1 -p4

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
%{_libdir}/libglobus_gridftp_server_control.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gridftp_server_control.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.3-8
- Handle 64 bit time_t on 32 bit systems
- Fix passing argument from incompatible pointer

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.3-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.2-3
- Fix some compiler warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.2-1
- Typo fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.1-1
- Use example message from RFC 2428 for response to EPSV
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.0-1
- Clean up old GPT references (8.1)
- Add AC_CONFIG_MACRO_DIR and ACLOCAL_AMFLAGS (8.2)
- Fix problems between dual-stack (IPv4/IPv6) servers and IPv4-only clients
  (9.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.0-1
- Switch upstream to Grid Community Toolkit
- Grid Community Toolkit merged a number of outstanding pull requests (7.0)
  - Add option to send IPv6 address in EPSV response
  - Add function to get the command string
  - Terminate the connection if server fails to write the 220 banner
  - Fix typo in GridFTP server response type
- First Grid Community Toolkit release (7.1)
- Merge GT6 update 6.2 into GCT (7.2)
- Merge GT6 update 6.3 into GCT (7.3)
- Merge GT6 update 7.0 into GCT (8.0)
- Drop patches globus-gridftp-server-control-epsv-ip.patch,
  -cmd-string.patch and -tcp-rst-stuck.patch (accepted upstream)

* Thu Aug 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.0-1
- GT6 update: Add support for x.abspath

* Sun Jul 15 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3-1
- GT6 update: Force encryption on TLS control channel

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2-1
- GT6 update:
  - Prevent client from requesting clear control channel
  - CIPHERS config will now apply to control channel

* Sat Apr 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1-1
- GT6 update: Don't error if acquire_cred fails when vhost env is set

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0-3
- Terminate the connection if server fails to write the 220 banner

* Fri Oct 20 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0-2
- Fix for IPv4 mapped addresses

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0-1
- GT6 update: Add support for control channel over TLS

* Fri Aug 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2-1
- GT6 update: Allow 400 responses to stat failures

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 5.1-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Fri Jul 28 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.1-1
- GT6 update: Fix mem error on empty mlsc responses

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0-3
- Add patches from DPM developers:
  - Add an optional IPv6 address to EPSV response
  - Get command string

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0-2
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Mar 17 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0-1
- GT6 update: Extend response_type to allow for ftp error codes

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.2-1
- GT6 update

* Fri May 06 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.1-1
- GT6 update: Spelling

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-1
- GT6 update (Add correct behavior for data auth error code)

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.7-1
- GT6 update (Remove dead code)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.6-2
- Implement updated license packaging guidelines

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.6-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 2.10-2
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.10-1
- Update to Globus Toolkit 5.2.5
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-3
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-2
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 20 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.8-1
- Update to Globus Toolkit 5.2.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-2
- Specfile clean-up

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.7-1
- Update to Globus Toolkit 5.2.2
- Drop patch globus-gridftp-server-control-pw195.patch (was backport)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.5-2
- Backport security fix for JIRA ticket GT-195

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.5-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-gridftp-server-control-deps.patch (fixed upstream)

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.3-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.3-1
- Update to Globus Toolkit 5.2.0
- Drop patch globus-gridftp-server-control.patch (fixed upstream)

* Sun Jun 05 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.46-1
- Update to Globus Toolkit 5.0.4

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.45-2
- Add README file
- Add missing dependencies

* Fri Feb 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.45-1
- Update to Globus Toolkit 5.0.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.43-1
- Update to Globus Toolkit 5.0.2

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.42-1
- Update to Globus Toolkit 5.0.1

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.40-1
- Update to Globus Toolkit 5.0.0

* Tue Jul 28 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.36-1
- Autogenerated
