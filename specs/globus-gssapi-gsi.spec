Name:		globus-gssapi-gsi
%global _name %(tr - _ <<< %{name})
Version:	14.20
Release:	8%{?dist}
Summary:	Grid Community Toolkit - GSSAPI library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-openssl-module-devel >= 3
BuildRequires:	globus-gsi-openssl-error-devel >= 2
BuildRequires:	globus-gsi-cert-utils-devel >= 8
BuildRequires:	globus-gsi-credential-devel >= 5
BuildRequires:	globus-gsi-callback-devel >= 4
BuildRequires:	globus-gsi-proxy-core-devel >= 8
BuildRequires:	globus-gsi-sysconfig-devel >= 8
BuildRequires:	openssl-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)

Requires:	globus-gsi-sysconfig%{?_isa} >= 8
%if %{?rhel}%{!?rhel:0} == 7
Requires:	openssl-libs >= 1.0.2
%endif

%package devel
Summary:	Grid Community Toolkit - GSSAPI library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GSSAPI library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GSSAPI library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GSSAPI library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GSSAPI library Documentation Files

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
%{_libdir}/libglobus_gssapi_gsi.so.*
%config(noreplace) %{_sysconfdir}/grid-security/gsi.conf
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gssapi_gsi.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 14.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.20-1
- New GCT release v6.2.20220524
- Drop patches included in the release
- Disable sending session tickets after the TLS 1.3 handshake

* Sun Mar 06 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.17-4
- Better logic for TLS 1.3 special handling
- Use sha256 hash when generating test certificates
- Don't test TLS 1.0 and 1.1 when using openssl 3.0.1 or later

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 14.17-2
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.17-1
- Compatibility with TLS v1.3 (14.15)
- Compatibility with the dcache server implementation (14.16)
- Minimize session ticket size since we don't use them (14.16)
- OpenSSL 3.0 fixes (14.17)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.14-1
- Disallow TLS 1.0/1.1 by default again (14.12)
- Minor fixes to makefiles (14.13)
- Fix output payload check in gss_init_sec_context() after SSL handshake
  (14.14)
- Add BuildRequires perl-interpreter
- Add additional perl dependencies for tests
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.11-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.11-1
- Keep peers in sync after SSL handshake failure in gssapi

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.10-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.9-1
- Allow TLS 1.0/1.1
- Fix leaks
- Drop patch globus-gssapi-gsi-allow-tls-1.0-1.1.patch accepted upstream

* Sat Sep 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.7-2
- Allow TLS 1.0 and 1.1
- Require openssl-libs >= 1.0.2 on EPEL 7 (for SSL_set_alpn_protos)

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.7-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (14.0)
  - Put back use of SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS
- Use 2048 bit RSA key for tests (14.1)
- Avoid TLS 1.3 - needs porting (14.2)
- Merge GT6 update 13.6 into GCT (14.3)
- Merge GT6 update 13.8 into GCT (14.4)
- Fix globus-gsi-proxy-core version dependency in configure.ac (14.5)
- Merge GT6 update 13.9 into GCT (14.6)
- Merge GT6 update 13.10 into GCT (14.7)
- Drop patch globus-gssapi-gsi-empty-frag.patch (accepted upstream)

* Sat Sep 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.10-1
- GT6 update:
  - Set the default minimum TLS version to 1.2. 1.0 and 1.1 are deprecated.
  - Set the maximum TLS version default to 1.2. 1.3 is not yet supported.
  - Use 2048 bit keys to support openssl 1.1.1 (13.9)
  - Fix resource leak when loading cert directories (13.10)
- Drop patch globus-gssapi-gsi-no-tls13.patch (accepted upstream)

* Sun Aug 26 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.8-3
- Avoid TLS 1.3 - needs porting

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.8-1
- GT6 update: Add context inquire OID support to get TLS version and cipher

* Fri Jun 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.6-1
- GT6 update: Enable ECDH ciphers for openssl < 1.1.0

* Sat Apr 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.5-1
- GT6 update: Don't check uid on win

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.4-1
- GT6 update: Improve vhost support

* Tue Oct 31 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.3-1
- GT6 update: Allow configuration of non-root user to own credentials for root
  services

* Sun Oct 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.2-1
- GT6 update: fix make clean rule, fix alpn mismatch test

* Tue Sep 26 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.1-1
- GT6 update:
  - Use X509_VHOST_CRED_DIR if set when accepting
  - Fix race condition
- Drop patch globus-gssapi-gsi-race.patch (accepted upstream)

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.0-2
- Fix race condition in the Makefile in test directory

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 13.0-1
- GT6 update:
  - Add SNI vhost cred dir support
  - Add optional ALPN processing

* Fri Jul 28 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.17-3
- Restore usage of SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS option

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.17-1
- GT6 update: Fix indicate_mechs_test when using openssl v1.1.0

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.16-1
- GT6 update:
  - Don't unlock unlocked mutex (12.14)
  - Remove legacy SSLv3 support (12.15)
  - Test fixes (12.16)
- Drop patch globus-gssapi-gsi-mutex-unlock.patch (fixed upstream 12.14)

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.13-4
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Drop the globus-gssapi-gsi-openssl098.patch

* Fri Mar 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.13-3
- Don't unlock unlocked mutex

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.13-1
- GT6 update: Skip mech v1 tests for OpenSSL >= 1.1.0

* Wed Nov 09 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.12-1
- GT6 update: More updates for mech negotiation

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.11-1
- GT6 update: Add support for new mech oid for different MIC formats

* Thu Oct 13 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.9-2
- Rebuild for openssl 1.1.0 (Fedora 26)

* Fri Sep 23 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.9-1
- GT6 update
  - Add backward compatibility fallback in verify_mic (12.7)
  - Fix hash detection (12.8)
  - Fix bad index references (12.9)
- Drop patch globus-gssapi-gsi-compat-mic.patch (fixed upstream 12.7)

* Fri Sep 16 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.5-2
- Use backward compatible mic by default for now

* Wed Sep 07 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.5-1
- GT6 update
  - Updates for mic handling without using internal openssl structs (12.4)
  - More tweaks to get_mic/verify_mic for 1.0.1 (12.5)
- Drop patch globus-gssapi-gsi-no-mic-test.patch

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 12.3-1
- GT6 update: Updates for OpenSSL 1.1.0

* Fri May 06 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 12.1-1
- GT6 update: Change default host verification mode to strict

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.29-1
- GT6 update: Add support for certificates without a CN

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.26-1
- GT6 update
- Fix FORCE_TLS setting to allow TLSv1.1 and TLS1.2, not just TLSv1.0

* Wed Jan 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.25-1
- GT6 update: support loading mutiple extra CA certs

* Thu Dec 10 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.24-1
- GT6 update: Don't call SSLv3_method unless it is available

* Wed Sep 09 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.22-1
- GT6 update: GT-627: gss_import_cred crash
- Enable checks on EPEL6 ppc64 - no longer fails with above fix

* Wed Jul 29 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.20-1
- GT6 update
- GT-614: GLOBUS_GSS_C_NT_HOST_IP doesn't allow host-only imports and
  comparisons

* Sat Jun 20 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.19-1
- GT6 update (export config file values into environment if not set already)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.18-1
- GT6 update (Change the name compatibility mode in gsi.conf to HYBRID to
  match the behavior in 11.14 and earlier. Also some test fixes.)

* Fri May 29 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.16-1
- GT6-update (SSL cipher configuration)

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.14-2
- Implement updated license packaging guidelines

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.14-1
- GT6 update
- Drop patch globus-gssapi-gsi-doxygen.patch (fixed upstream)

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.13-1
- GT6 update
- Update patch globus-gssapi-gsi-doxygen.patch

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.12-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks
- Disable checks on EPEL6 ppc64

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 10.10-3
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Dec 05 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.10-2
- Remove directory man page

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.10-1
- Update to Globus Toolkit 5.2.5
- Drop patch globus-gssapi-gsi-doxygen.patch (fixed upstream)
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.7-5
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.7-4
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.7-2
- Add build requires for TexLive 2012

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.7-1
- Update to Globus Toolkit 5.2.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.6-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-gssapi-gsi-deps.patch, globus-gssapi-gsi-format.patch
  and globus-gssapi-gsi-doxygen.patch (fixed upstream)

* Mon Jan 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-1
- Update to Globus Toolkit 5.2.0

* Fri Jun 03 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 7.8-1
- Update to Globus Toolkit 5.0.4

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 7.6-2
- Add README file

* Fri Feb 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 7.6-1
- Update to Globus Toolkit 5.0.3

* Fri Feb 11 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 7.5-1
- Update to Globus Toolkit 5.0.1
- Drop patch globus-gssapi-gsi-openssl.patch (fixed upstream)

* Mon Feb 08 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 7.0-2
- Update openssl 1.0.0 patch based on RIC-29 branch in upstream CVS

* Fri Jan 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 7.0-1
- Update to Globus Toolkit 5.0.0

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 5.9-5
- rebuilt with new openssl

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-4
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Wed Jun 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-3
- Update to official Fedora Globus packaging guidelines

* Tue May 12 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-2
- Change the License tag to take the library/ssl_locl.h file into account

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-0.3
- Adapt to updated GPT package

* Wed Oct 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-0.1
- Autogenerated
