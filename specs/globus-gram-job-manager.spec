Name:		globus-gram-job-manager
%global _name %(tr - _ <<< %{name})
Version:	15.8
Release:	9%{?dist}
Summary:	Grid Community Toolkit - GRAM Jobmanager

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
#		https://github.com/gridcf/gct/pull/223
Patch0:		0001-Handle-64-bit-time_t-on-32-bit-systems.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gsi-credential-devel >= 5
BuildRequires:	globus-gass-cache-devel >= 8
BuildRequires:	globus-gass-transfer-devel >= 7
BuildRequires:	globus-gram-protocol-devel >= 11
BuildRequires:	globus-gssapi-gsi-devel >= 10
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	globus-callout-devel >= 2
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-xio-popen-driver-devel >= 2
BuildRequires:	globus-rsl-devel >= 9
BuildRequires:	globus-gram-job-manager-callout-error-devel >= 2
BuildRequires:	globus-scheduler-event-generator-devel >= 4
BuildRequires:	openssl-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl-interpreter
#		Additional requirements for make check
BuildRequires:	globus-io-devel >= 9
BuildRequires:	globus-gram-client-devel >= 3
BuildRequires:	globus-gass-server-ez-devel >= 2
BuildRequires:	globus-common-progs >= 15
BuildRequires:	globus-gatekeeper >= 9
BuildRequires:	globus-gram-client-tools >= 10
BuildRequires:	globus-gass-copy-progs >= 8
BuildRequires:	globus-gass-cache-program >= 5
BuildRequires:	globus-gram-job-manager-scripts >= 6
BuildRequires:	globus-proxy-utils >= 5
BuildRequires:	globus-gsi-cert-utils-progs
BuildRequires:	globus-gram-job-manager-fork-setup-poll
BuildRequires:	openssl
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Globus::Core::Paths)
BuildRequires:	perl(Globus::GRAM::Error)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

Requires:	globus-xio-popen-driver%{?_isa} >= 2
Requires:	globus-common-progs >= 15
Requires:	globus-gatekeeper >= 9
Requires:	globus-gram-client-tools >= 10
Requires:	globus-gass-copy-progs >= 8
Requires:	globus-gass-cache-program >= 5
Requires:	globus-gram-job-manager-scripts >= 6
Requires:	globus-proxy-utils >= 5
Requires:	globus-gsi-cert-utils-progs
Requires:	globus-seg-job-manager%{?_isa} = %{version}-%{release}
Requires:	logrotate

%package -n globus-seg-job-manager
Summary:	Grid Community Toolkit - Scheduler Event Generator Job Manager
Requires:	%{name} = %{version}-%{release}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GRAM Jobmanager

%description -n globus-seg-job-manager
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-seg-job-manager package contains:
Scheduler Event Generator Job Manager

%prep
%setup -q -n %{_name}-%{version}
%patch -P0 -p4

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

%if %{?rhel}%{!?rhel:0} == 6
# Remove su option from logrotate file in EPEL 6 (not supported)
sed '/ su /d' -i %{buildroot}%{_sysconfdir}/logrotate.d/globus-job-manager
%endif

%check
GLOBUS_HOSTNAME=localhost %make_build check

%ldconfig_scriptlets -n globus-seg-job-manager

%files
%{_bindir}/globus-personal-gatekeeper
%{_sbindir}/globus-gram-streamer
%{_sbindir}/globus-job-manager
%{_sbindir}/globus-job-manager-lock-test
%{_sbindir}/globus-rvf-check
%{_sbindir}/globus-rvf-edit
%dir %{_datadir}/globus
%dir %{_datadir}/globus/%{_name}
%{_datadir}/globus/%{_name}/globus-gram-job-manager.rvf
%config(noreplace) %{_sysconfdir}/logrotate.d/globus-job-manager
%dir %{_localstatedir}/lib/globus
%dir %{_localstatedir}/lib/globus/gram_job_state
%dir %{_localstatedir}/log/globus
%dir %{_sysconfdir}/globus
%config(noreplace) %{_sysconfdir}/globus/globus-gram-job-manager.conf
%doc %{_mandir}/man1/globus-personal-gatekeeper.1*
%doc %{_mandir}/man5/rsl.5*
%doc %{_mandir}/man8/globus-job-manager.8*
%doc %{_mandir}/man8/globus-rvf-check.8*
%doc %{_mandir}/man8/globus-rvf-edit.8*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files -n globus-seg-job-manager
# This is a loadable module (plugin)
%{_libdir}/libglobus_seg_job_manager.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 15.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.8-8
- Handle 64 bit time_t on 32 bit systems

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.8-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.6-4
- Use sha256 hash when generating test certificates
- Fix some compiler warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 15.6-2
- Rebuilt with OpenSSL 3.0.0

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.6-1
- Typo fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.5-1
- Remove remnants of dropped documentation package
- Add BuildRequires perl-interpreter
- Add additional perl dependencies for tests
- Specfile updates
- Add logrotate dependency (fixes rpmlint error)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.4-4
- Add additional perl build dependencies due to perl package split

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.4-1
- Doxygen fixes (15.2)
- Remove usage statistics collection support (15.3)
- Add su option to logrotate file (15.4)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.1-2
- Bump GCT release version to 6.2

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 15.1-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (15.0)
  - Disable usage statistics reporting by default
  - Workaround non-implemented features on GNU/Hurd (socket buffer size)
  - Move grid-proxy-destroy call to before starting personal gatekeeper in
    the test wrapper
- Use 2048 bit RSA key for tests (15.1)
- Move globus-seg-job-manager plugin to a separate package
- Drop patches globus-gram-job-manager-socket-buffer-size.patch and
  globus-gram-job-manager-proxy.patch (accepted upstream)

* Sat Sep 01 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.37-1
- GT6 update: Use 2048 bit keys to support openssl 1.1.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.36-1
- GT6 update: Default to running personal gatekeeper on an ephemeral port

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.35-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Drop the globus-gram-job-manager-openssl098.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.35-1
- GT6 update: Updated man pages

* Thu Oct 13 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.33-2
- Rebuild for openssl 1.1.0 (Fedora 26)

* Wed Sep 07 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.33-1
- GT6 Update: Fix issue #71: test leaves process behind
- Drop patch globus-gram-job-manager-process.patch

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 14.32-1
- GT6 update: Updates for OpenSSL 1.1.0
- Test fixes

* Wed Feb 10 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.27-3
- Add missing perl(Test) BuildRequires (used to be part of main perl package)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.27-1
- GT6 update: GT-619: Uninitialized data in job manager cause crash

* Sat Jun 20 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.26-1
- GT6 update (fix state info for running jobs, man pages updates)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.25-2
- Implement updated license packaging guidelines
- Set GLOBUS_HOSTNAME during make check and enable tests on EPEL5 and EPEL6

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.25-1
- GT6 update
- Drop patch globus-gram-job-manager-personal-gk.patch (fixed upstream)

* Tue Oct 28 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.22-2
- Fixes to the globus-personal-gatekeeper (fixes parallel make check)

* Sun Oct 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.22-1
- GT6 update
- Includes improvements from Open Science Grid (OSG)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.20-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks
- Remove documentation package
- Disable checks on EPEL5 and EPEL6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.53-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 13.53-3
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Fri Dec 13 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.53-2
- Proper ownership of /etc/globus

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.53-1
- Update to Globus Toolkit 5.2.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.51-4
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.51-3
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.51-1
- Update to Globus Toolkit 5.2.3

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.48-1
- Update to Globus Toolkit 5.2.2
- Drop patch globus-gram-job-manager-porting.patch (fixed upstream)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.33-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-gram-job-manager-deps.patch (fixed upstream)

* Wed Jan 18 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.14-2
- Add missing BuildRequires: globus-common-progs and libxml2-devel
- Portability fixes
- Fix broken links in README file

* Thu Dec 15 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 13.14-1
- Update to Globus Toolkit 5.2.0
- Drop patches globus-gram-job-manager-doxygen.patch,
  globus-gram-job-manager.patch, globus-gram-job-manager-pathmax.patch and
  globus-gram-job-manager-undefined.patch (fixed upstream)

* Sun Jun 05 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.70-1
- Update to Globus Toolkit 5.0.4
- Fix doxygen markup

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.67-3
- Add README file

* Tue Apr 19 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.67-2
- Updated patch

* Thu Feb 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.67-1
- Update to Globus Toolkit 5.0.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 18 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.59-2
- Move client and server man pages to main package

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.59-1
- Update to Globus Toolkit 5.0.2

* Sat Jun 05 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.42-2
- Additional portability fixes

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.42-1
- Update to Globus Toolkit 5.0.1

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.17-1
- Update to Globus Toolkit 5.0.0

* Thu Jul 30 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.15-1
- Autogenerated
