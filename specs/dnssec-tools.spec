# OpenSSL ENGINE support deprecated in Fedora 41 onwards
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
%if 0%{?fedora} > 40
%global _preprocessor_defines %{?_preprocessor_defines} -DOPENSSL_NO_ENGINE
%endif


Summary: A suite of tools for managing dnssec aware DNS usage
Name: dnssec-tools
Version: 2.2.3
Release: 30%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.dnssec-tools.org/
#Source0: https://www.dnssec-tools.org/download/%%{name}-%%{version}.tar.gz
Source0: https://www.hardakers.net/software/%{name}-%{version}.tar.gz
Source1: dnssec-tools-dnsval.conf
Source2: libval-config
# Require note: the auto-detection for perl-Net-DNS-SEC will not work since
# the tools do run time tests for their existence.  But most of the tools
# are much more useful with the modules in place, so we hand require them.
Requires: dnssec-tools-perlmods, bind, perl(Getopt::GUI::Long)
Requires: perl(GraphViz)
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(Test) perl(ExtUtils::MakeMaker)
BuildRequires: make
# Makes the code installation linux filesystem friendly
Patch5: dnssec-tools-linux-conf-paths-1.13.patch
Patch13: dnssec-tools-2.0-autoconf-for-aarch64.patch
Patch17: dnssec-tools-new-2017-key.patch
Patch18: dnssec-tools-new-openssl-APIs.patch
# Update Makefile to respect users LDFLAGS
# https://github.com/DNSSEC-Tools/DNSSEC-Tools/commit/7287c6b96422e499560fb10b95c1a481ea82656d
Patch19: 7287c6b96422e499560fb10b95c1a481ea82656d.patch
# link libval-threads with libs
Patch20: dnssec-tools-2.2.3-link-libval-threads-with-libs.patch
Patch21: dnssec-tools-2.2.3-add_ifdedf_to_engine.patch

%description

The goal of the DNSSEC-Tools project is to create a set of tools,
patches, applications, wrappers, extensions, and plugins that will
help ease the deployment of DNSSEC-related technologies.

%package perlmods
Summary: Perl modules supporting DNSSEC (needed by the dnssec-tools)
Requires: perl(Getopt::GUI::Long)

%description perlmods

The dnssec-tools project comes with a number of perl modules that are
required by the DNSSEC tools themselves as well as modules that are
useful for other developers.

%package libs
Summary: C-based libraries for dnssec aware tools
Requires: openssl

%description libs
C-based libraries useful for developing dnssec aware tools.

%package libs-devel
Summary: C-based development libraries for dnssec aware tools
Requires: dnssec-tools-libs = %{version}-%{release}

%description libs-devel
C-based libraries useful for developing dnssec aware tools.

%prep
%setup -q

%patch -P5 -p0 
#%%patch6 -p2
#%%patch12 -p2
#%%patch13 -p2
#%%patch14 -p2
#%%patch15 -p2
#%%patch16 -p2
#%%patch17 -p2
#%%patch18 -p2
%patch -P19 -p2
%patch -P20 -p1 -b .link-with-libs
%patch -P21 -p1

%build
%configure --with-validator-testcases-file=%{_datadir}/dnssec-tools/validator-testcases --with-perl-build-args="INSTALLDIRS=vendor OPTIMIZE='$RPM_OPT_FLAGS'" --sysconfdir=/etc --with-root-hints=/etc/dnssec-tools/root.hints --with-resolv-conf=/etc/dnssec-tools/resolv.conf --disable-static --with-nsec3 --with-ipv6 --with-dlv --disable-bind-checks
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' validator/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' validator/libtool
# makefile dependencies are broken; we can't use smp_mflags:
#make %%{?_smp_mflags} CCFLAGS="-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
make CCFLAGS="-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf %{buildroot}
make install DESTCONFDIR=%{buildroot}/etc/dnssec-tools/ DESTDIR=%{buildroot} QUIET=

%{__install} -m 644 %{SOURCE1} %{buildroot}/etc/dnssec-tools/dnsval.conf
%{__install} -m 644 validator/etc/root.hints %{buildroot}/etc/dnssec-tools/root.hints

# remove unneeded perl install files
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
# remove empty directories
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
rm -f %{buildroot}%{_libdir}/*.la

# Move the architecture dependent config file to its own place
# (this allows multiple architecture rpms to be installed at the same time)
mv ${RPM_BUILD_ROOT}/%{_bindir}/libval-config ${RPM_BUILD_ROOT}/%{_bindir}/libval-config-%{_arch}
# Add a new wrapper script that calls the right file at run time
install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}/%{_bindir}/libval-config

%ldconfig_scriptlets libs

%files
%doc README.md INSTALL COPYING

%dir %{_sysconfdir}/dnssec-tools/
%config(noreplace) %{_sysconfdir}/dnssec-tools/dnssec-tools.conf

%{_bindir}/dnspktflow
%{_bindir}/donuts
%{_bindir}/donutsd
%{_bindir}/drawvalmap
%{_bindir}/expchk
%{_bindir}/genkrf
%{_bindir}/getdnskeys
%{_bindir}/getds
%{_bindir}/lskrf
%{_bindir}/maketestzone
%{_bindir}/mapper
%{_bindir}/zonesigner
# this doesn't use %%{_datadir} because patch6 above uses this exact path
/usr/share/dnssec-tools
#/usr/share/dnssec-tools/donuts
#/usr/share/dnssec-tools/donuts/rules
#/usr/share/dnssec-tools/donuts/rules/*

%{_bindir}/dtck
%{_bindir}/dtconfchk
%{_bindir}/dtconf
%{_bindir}/dtdefs
%{_bindir}/dtinitconf
%{_bindir}/fixkrf
%{_bindir}/tachk
%{_bindir}/timetrans

%{_bindir}/lsroll
%{_bindir}/rollchk
%{_bindir}/rollctl
%{_bindir}/rollerd
%{_bindir}/rollinit
%{_bindir}/rollset
%{_bindir}/keyarch
%{_bindir}/cleanarch

%{_bindir}/dt-libval_check_conf
%{_bindir}/dt-validate
# configure above 
#%%{_datadir}/dnssec-tools/validator-testcases
%{_bindir}/dt-getaddr
%{_bindir}/dt-gethost
%{_bindir}/dt-getname
%{_bindir}/dt-getquery
%{_bindir}/dt-getrrset
%{_bindir}/dt-danechk

%{_bindir}/trustman
%{_bindir}/blinkenlights
%{_bindir}/lights
%{_bindir}/cleankrf
%{_bindir}/krfcheck
%{_bindir}/rolllog
%{_bindir}/signset-editor
%{_bindir}/rollrec-editor

# new in 1.13
%{_bindir}/buildrealms
%{_bindir}/check-zone-expiration
%{_bindir}/dtrealms
%{_bindir}/grandvizier
%{_bindir}/keymod
%{_bindir}/lsrealm
%{_bindir}/realmchk
%{_bindir}/realmctl
%{_bindir}/realminit
%{_bindir}/realmset

%{_bindir}/lsdnssec

%{_bindir}/bubbles
%{_bindir}/convertar

%{_mandir}/man1/dnssec-tools.1.gz
%{_mandir}/man1/dnspktflow.1.gz
%{_mandir}/man1/donuts.1.gz
%{_mandir}/man1/donutsd.1.gz
%{_mandir}/man1/drawvalmap.1.gz
%{_mandir}/man1/expchk.1.gz
%{_mandir}/man1/genkrf.1.gz
%{_mandir}/man1/getdnskeys.1.gz
%{_mandir}/man1/getds.1.gz
%{_mandir}/man1/lskrf.1.gz
%{_mandir}/man1/keyarch.1.gz
%{_mandir}/man1/maketestzone.1.gz
%{_mandir}/man1/mapper.1.gz
%{_mandir}/man1/zonesigner.1.gz
%{_mandir}/man1/dt-validate.1.gz
%{_mandir}/man1/dt-getaddr.1.gz
%{_mandir}/man1/dt-gethost.1.gz
%{_mandir}/man1/dt-getname.1.gz
%{_mandir}/man1/dt-getquery.1.gz
%{_mandir}/man1/dt-getrrset.1.gz

%{_mandir}/man1/dtconfchk.1.gz
%{_mandir}/man1/dtdefs.1.gz
%{_mandir}/man1/dtinitconf.1.gz
%{_mandir}/man1/fixkrf.1.gz
%{_mandir}/man1/tachk.1.gz
%{_mandir}/man1/timetrans.1.gz

%{_mandir}/man1/bubbles.1.gz
%{_mandir}/man1/convertar.1.gz

%{_mandir}/man1/lsroll.1.gz
%{_mandir}/man1/rollchk.1.gz
%{_mandir}/man1/rollctl.1.gz
%{_mandir}/man1/rollerd.1.gz
%{_mandir}/man1/rollinit.1.gz
%{_mandir}/man1/rollset.1.gz
%{_mandir}/man1/lsdnssec.1.gz
%{_mandir}/man1/cleanarch.1.gz
%{_mandir}/man1/blinkenlights.1.gz
%{_mandir}/man1/lights.1.gz
%{_mandir}/man1/cleankrf.1.gz
%{_mandir}/man1/krfcheck.1.gz
%{_mandir}/man1/rolllog.1.gz
%{_mandir}/man1/signset-editor.1.gz
%{_mandir}/man1/trustman.1.gz
%{_mandir}/man1/dtck.1.gz
%{_mandir}/man1/dtconf.1.gz
%{_mandir}/man1/rollrec-editor.1.gz
%{_mandir}/man3/p_ac_status.3.gz
%{_mandir}/man3/p_val_status.3.gz

# new in 1.13
%{_mandir}/man1/buildrealms.1.gz
%{_mandir}/man1/check-zone-expiration.1.gz
%{_mandir}/man1/dt-libval_check_conf.1.gz
%{_mandir}/man1/dtrealms.1.gz
%{_mandir}/man1/grandvizier.1.gz
%{_mandir}/man1/keymod.1.gz
%{_mandir}/man1/lsrealm.1.gz
%{_mandir}/man1/realmchk.1.gz
%{_mandir}/man1/realmctl.1.gz
%{_mandir}/man1/realminit.1.gz
%{_mandir}/man1/realmset.1.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::realm.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::realmmgr.3pm.gz

%files perlmods
# perl-Net-DNS-SEC is noarch and cannot own this directory:
%dir %{perl_vendorarch}/Net/DNS/SEC

%{perl_vendorarch}/Net/DNS/SEC/Tools
%{perl_vendorarch}/Net/addrinfo*
%{perl_vendorarch}/Net/DNS/SEC/*.pm
%{perl_vendorarch}/Net/DNS/SEC/*.pl
%{perl_vendorarch}/auto/Net/DNS/SEC/Validator
%{perl_vendorarch}/auto/Net/addrinfo/
%{perl_vendorarch}/Net/DNS/ZoneFile/
%{perl_vendorlib}/Net/DNS/SEC/Tools/

%{_mandir}/man3/Net::DNS::SEC::Tools::QWPrimitives.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::BootStrap.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::conf.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::keyrec.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::rollmgr.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::rollrec.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::defaults.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::timetrans.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::tooloptions.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::dnssectools.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Validator.3pm.gz
%{_mandir}/man3/Net::addrinfo.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::Donuts::Rule.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::rolllog.3pm.gz

%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Bind.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Csv.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Dns.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Dump.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Itar.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Libval.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Mf.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::TrustAnchor::Secspider.3pm.gz

# obsolete module still in upstream source:
%{_mandir}/man3/Net::DNS::ZoneFile::Fast.3pm.gz

%files libs
%{_libdir}/*.so.*
%config(noreplace) %{_sysconfdir}/dnssec-tools
#%%config(noreplace) %%{_sysconfdir}/dnssec-tools/dnsval.conf
#%%config(noreplace) %%{_sysconfdir}/dnssec-tools/root.hints

%files libs-devel
%{_includedir}/validator
%{_libdir}/*.so

%{_bindir}/libval-config*

%{_mandir}/man3/libval.3.gz
%{_mandir}/man3/libval_shim.3.gz
%{_mandir}/man3/val_free_answer_chain.3.gz
%{_mandir}/man3/val_get_rrset.3.gz
%{_mandir}/man3/val_getaddrinfo.3.gz
%{_mandir}/man3/val_gethostbyname.3.gz
%{_mandir}/man3/dnsval.conf.3.gz
%{_mandir}/man3/dnsval_conf_get.3.gz
%{_mandir}/man3/dnsval_conf_set.3.gz
%{_mandir}/man3/libsres.3.gz
%{_mandir}/man3/root_hints_get.3.gz
%{_mandir}/man3/root_hints_set.3.gz
%{_mandir}/man3/resolv_conf_get.3.gz
%{_mandir}/man3/resolv_conf_set.3.gz
%{_mandir}/man3/val_create_context.3.gz
%{_mandir}/man3/val_free_context.3.gz
%{_mandir}/man3/val_free_result_chain.3.gz
%{_mandir}/man3/val_istrusted.3.gz
%{_mandir}/man3/val_resolve_and_check.3.gz
%{_mandir}/man3/val_gethostbyaddr.3.gz
%{_mandir}/man3/val_gethostbyaddr_r.3.gz
%{_mandir}/man3/val_gethostbyname2.3.gz
%{_mandir}/man3/val_gethostbyname2_r.3.gz
%{_mandir}/man3/val_gethostbyname_r.3.gz
%{_mandir}/man3/val_getnameinfo.3.gz
%{_mandir}/man3/val_isvalidated.3.gz
%{_mandir}/man3/val_res_query.3.gz
%{_mandir}/man3/val_res_search.3.gz
#%%{_mandir}/man3/val_addrinfo.3.gz
%{_mandir}/man3/val_add_valpolicy.3.gz
%{_mandir}/man3/val_context_setqflags.3.gz
%{_mandir}/man3/val_does_not_exist.3.gz
%{_mandir}/man3/val_free_response.3.gz
%{_mandir}/man3/val_freeaddrinfo.3.gz

# new in 2.1
%{_mandir}/man1/dt-danechk.1.gz
%{_mandir}/man3/Net::DNS::SEC::Tools::Donuts.3pm.gz
%{_mandir}/man3/Net::DNS::SEC::examples.3pm.gz
%{_mandir}/man3/libval_async.3.gz
%{_mandir}/man3/p_dane_error.3.gz
%{_mandir}/man3/val_async_cancel.3.gz
%{_mandir}/man3/val_async_cancel_all.3.gz
%{_mandir}/man3/val_async_check_wait.3.gz
%{_mandir}/man3/val_async_select_info.3.gz
%{_mandir}/man3/val_async_submit.3.gz
%{_mandir}/man3/val_dane_check.3.gz
%{_mandir}/man3/val_dane_match.3.gz
%{_mandir}/man3/val_dane_submit.3.gz
%{_mandir}/man3/val_free_dane.3.gz
%{_mandir}/man3/val_getdaneinfo.3.gz


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-29
- Perl 5.42 rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 05 2024 Michal Josef Špaček <mspacek@redhat.com> - 2.2.3-27
- Build without OpenSSL ENGINE support on Fedora 41 onwards

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.3-26
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-24
- Perl 5.40 rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-20
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-18
- Add BR perl-generators to automatically generates run-time dependencies
  for installed Perl files

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-16
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.2.3-14
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-12
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Petr Pisar <ppisar@redhat.com> - 2.2.3-10
- Build-require perl-macros for Perl RPM macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-8
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Tom Callaway <spot@fedoraproject.org> - 2.2.3-6
- fix libval-threads to link with dependent libs
- use LDFLAGS

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-4
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 4 2018 Wes Hardaker <wjhns174@hardakers.net> - 2.2.3-2
- update default dnsval.conf

* Wed Aug 29 2018 Wes Hardaker <wjhns174@hardakers.net> - 2.2.3-1
- match upstream version

* Wed Aug 29 2018 Wes Hardaker <wjhns174@hardakers.net> - 2.2.1-2
- add Mail::Send

* Mon Jul 30 2018 Wes Hardaker <wjhns174@hardakers.net> - 2.2.1-1
- fix build issues

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-9
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-5
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-3
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 30 2015 Wes Hardaker <wjhns174@hardakers.net> - 2.2-1
- new upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.1-3
- Perl 5.22 rebuild

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.1-2
- Perl 5.20 mass

* Fri Sep 05 2014 Wes Hardaker <wjhns174@hardakers.net> - 2.1-1
- upgrade to 2.1

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-12
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Wes Hardaker <wjhns174@hardakers.net> - 2.0-9
- fix bug #1056277 about nsec3 parsing with new versions of bindw

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0-7
- Perl 5.18 rebuild

* Thu Jun 20 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-6
- Require GraphViz

* Thu May 23 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-5
- Added a fix for various Zonefile::Fast bugs

* Thu Apr 18 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-4
- update configure from autoconf 2.69 for aarch64 support

* Thu Apr 18 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-3
- Patch to support NSEC3 records from newer versions of bind

* Wed Mar  6 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-2
- Added ownership of the /etc/dnssec-tools package

* Wed Feb 20 2013 Wes Hardaker <wjhns174@hardakers.net> - 2.0-1
- Release of version 2.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.14-1
- updated to upstream 1.14

* Mon Oct  1 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.13-5
- Rename the -config program to be unique per arch

* Mon Sep 24 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.13-4
- Fix ZoneFile::Fast module for newer bind versions

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.13-2
- Perl 5.16 rebuild

* Thu Jun 21 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.13-1
- New 1.13 upstream release

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.12.1-3
- Perl 5.16 rebuild

* Thu May 24 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.12.1-2
- move validate to dt-validate to avoid a conflict

* Fri May 18 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.12.1-1
- Upgraded to 1.12.1

* Fri Jan 27 2012 Wes Hardaker <wjhns174@hardakers.net> - 1.12-1
- Upgraded to version 1.12
- Added a patch to fix the perl validator

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.11-1
- Upgrade to the upstream 1.11

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.10-3
- Perl mass rebuild

* Thu Jul 21 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.10-2
- rebuild for perl again

* Sun Jul  3 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.10-1
- Upgrade to 1.10

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.9-5
- Perl mass rebuild

* Fri May  6 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.9-4
- per request, change the default resolv.conf to /etc/dnssec-tools so it's possible to override the internal default, which internally falls back to /etc/resolv.conf

* Fri May  6 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.9-3
- move libval specific configs to the -libs package

* Thu Mar 24 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.9-1
- Upgrade to 1.9 from upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.8-4
- Require getop

* Tue Oct  5 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.8-3
- Added the . trust anchor and set default policy

* Tue Oct  5 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.8-2
- Added nsec3 option

* Fri Sep 24 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.8-1
- Update to the upstream 1.8 release

* Thu Jul  1 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.7-1
- Update to upstream version 1.7

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.6-4
- Mass rebuild with perl-5.12.0

* Fri May 21 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6-3
- disable static libs
- cleanup filelist to avoid duplication

* Mon Apr  5 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.6-2
- version bump

* Mon Apr  5 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.6-1
- Updated to 1.6

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.5-4
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5-2
- Fix unowned directories (#483339).

* Fri Mar  6 2009 Wes Hardaker <wjhns174@hardakers.net> - 1.5-1
- Update to 1.5

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb  4 2009 Wes Hardaker <wjhns174@hardakers.net> - 1.4.1-6
- make the perlmods module directly require the needed perl mods
  mainly for directory ownership.

* Mon Jan 26 2009 Wes Hardaker <wjhns174@hardakers.net> - 1.4.1-5
- Fixed arpa header compile conflict

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.1-4
- rebuild with new openssl

* Mon Dec  1 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.4.1-3
- Added package directories we own, left out ones we don't.

* Tue Jul 22 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.4.1-2
- Added missing log message for security release

* Tue Jul 22 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.4.1-1
- Update to upstream 1.4.1 which fixes the random port issue being
  broadcast about every resolver known to man including this one; note
  that DNSSEC itself will actually protect against the attack but
  libval is vulnerable to non-DNSSEC-protected zones without this fix.

* Tue May 27 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.4.rc1-1
- Update to upstream 1.4

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.2-2
Rebuild for new perl

* Fri Feb 15 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.3.2-1
- Jump to upstream to grab latest identical fixes

* Fri Feb 15 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.3.1-2
- Fix top level makefile for bulid dirs

* Fri Feb 15 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.3.1-1
- Update to 1.3.1 to fix:
- A security bug in parent surrounding trust anchor checking in the
  libval library.
- Small fixes with donuts
- Small fixes with the ZoneFile::Fast parser

* Mon Jan  7 2008 Wes Hardaker <wjhns174@hardakers.net> - 1.3-7
- Fix donuts hard-coded rules path

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.3-6
- Rebuild for deps

* Tue Nov 27 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.3-5
- Added a libval-config wrapper to get around a multi-arch issue

* Mon Nov 19 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.3-4
- Bogus release bump to fix fedora tag issue

* Mon Nov 19 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.3-3
- dnsval.conf syntax fix

* Mon Nov 19 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.3-2
- New dnssec-tools.org dnskey

* Wed Oct 31 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.3-1
- Update to 1.3

* Wed Aug  8 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.2-6
- Actually apply the patch (sigh).

* Wed Aug  8 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.2-5
- Fix make -jN support for the top level makefile

* Thu Jul 12 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.2-4
- patch to fix a donuts rule for newer perl-Net::DNS update
- patch for maketestzone to work around a bug in Net::DNS::RR::DS

* Wed Jul 11 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.2-3
- Added more Requires and better BuildRequires

* Thu May 31 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.2-2
- fixed missing destdir in validator/Makefile.in
- add optimize flags to perl build
- syntatic ordering cleanup of the find argument

* Tue May 22 2007 Wes Hardaker <wjhns174@hardakers.net> - 1.2-1
- Update to 1.2 release

* Wed Apr 18 2007  Wes Hardaker <wjhns174@hardakers.net> - 1.1.1-4
- Fix changelog so it doesn't have a macro in the documentation
- Added a dnsval.conf starting file.
- Remove include subdir wildcard expansion since the entire directory
  is owned.

* Wed Apr 18 2007  Wes Hardaker <wjhns174@hardakers.net> - 1.1.1-3
- Add patch to make Net::DNS::SEC optional
- Fix date in previous log

* Wed Apr 18 2007  Wes Hardaker <wjhns174@hardakers.net> - 1.1.1-2
- Pointed Source0 at the sourceforge server instead of a local file
- Set License to BSD-like
- Took ownership of includedir/validator

* Tue Apr 10 2007  Wes Hardaker <wjhns174@hardakers.net> - 1.1.1-1
- Updated to upstream version 1.1.1

* Tue Mar 20 2007  Wes Hardaker <wjhns174@hardakers.net> - 1.1-2
- cleaned up spec file further for future submission to Fedora Extras
- made -libs-devel depend on exact version of -libs
- remove installed .la files
- added patch to use proper DESTDIR passing in the top Makefile

* Mon Mar 19 2007  Wes Hardaker <wjhns174@hardakers.net> - 1.1-1
- Updated to 1.1 and fixed rpmlint issues

* Mon Dec 04 2006   Wes Hardaker <wjhns174@hardakers.net> - 1.0
- updated to 1.0

* Mon Jun 19 2006   Wes Hardaker <wjhns174@hardakers.net> - 0.9.2-4
- updated to 0.9.2
- modified installation paths as appropriate to 

* Mon Jun 19 2006   Wes Hardaker <wjhns174@hardakers.net> - 0.9.1-1
- updated to 0.9.1

* Thu Feb  9 2006  Wes Hardaker <wjhns174@hardakers.net> - 0.9.0
- initial rpm
