%global sblim_testsuite_version 1.2.4
%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1

Name:           sblim-gather
Version:        2.2.9
Release:        38%{?dist}
Summary:        SBLIM Gatherer

License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        gather-config.h.prepend
Source2:        gather-config.h
Source3:        sblim-gather.tmpfiles
Source4:        missing-providers.tgz
Source5:        gatherer.service
Source6:        reposd.service

BuildRequires: make
BuildRequires:  sblim-cmpi-devel
BuildRequires:  sblim-cmpi-base-devel
BuildRequires:  libsysfs-devel
BuildRequires:  libvirt-devel
BuildRequires:  xmlto
BuildRequires:  gcc
BuildRequires:  systemd-units
# for missing providers
BuildRequires:  cmake
Patch1:         sblim-gather-2.2.7-missing_providers.patch
Patch2:         sblim-gather-2.2.7-typos.patch
Patch8:         sblim-gather-2.2.9-remove-cxx-check.patch

# Patch3: removes version from docdir
Patch3:         sblim-gather-2.2.8-docdir.patch
# Patch4: fixes multilib conflicts
Patch4:         sblim-gather-2.2.8-multilib.patch
# Patch5: use Pegasus root/interop instead of root/PG_Interop
Patch5:         sblim-gather-2.2.9-pegasus-interop.patch
# Patch6: call systemctl in provider registration
Patch6:         sblim-gather-2.2.9-prov-reg-sfcb-systemd.patch
# Patch7: remove conflicting assoc class Linux_MetricElementConformsToProfile
# from Linux_MetricProfile.mof (already included in Linux_Metric.mof)
Patch7:         sblim-gather-2.2.9-remove-assoc-conflict.patch
# Patch9: fix link fail with gcc-10 (patch by Jeff Law)
Patch9:         sblim-gather-2.2.9-inline.patch
# Patch10: fixes multiple definiton of variables (FTBFS with GCC 10)
Patch10:        sblim-gather-2.2.9-fix-multiple-definition.patch
# Patch11: fix issues found by coverity scan
Patch11:        sblim-gather-2.2.9-covscan-fixes.patch
# Patch12: fix incorrect use of temporary paths
Patch12:        sblim-gather-2.2.9-fix-use-of-temp-paths.patch
# Patch13: fix FTBFS with GCC 15
Patch13:        sblim-gather-2.2.9-gcc15-fix.patch
# Patch14: suppress msg when repeated value is detected
# see https://sourceforge.net/p/sblim/bugs/2739/
Patch14:        sblim-gather-2.2.9-suppress-repeated-value-msg.patch

Requires:       cim-server
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Standards Based Linux Instrumentation for Manageability
Performance Data Gatherer Base.
This package contains the agents and control programs for gathering
and providing performance data.

%package        provider
Summary:        SBLIM Gatherer Provider
Requires:       %{name} = %{version}-%{release}
Requires:       sblim-cmpi-base
Requires:       cim-server

%description    provider
The CIM (Common Information Model) Providers for the
SBLIM (Standards Based Linux Instrumentation for Manageability)
Gatherer.

%package        devel
Summary:        SBLIM Gatherer Development Support
Requires:       %{name} = %{version}-%{release}
Requires:       cim-server

%description    devel
This package is needed to develop new plugins for the
SBLIM (Standards Based Linux Instrumentation for Manageability)
Gatherer.

%if 0%{?with_test_subpackage}
%package        test
Summary:        SBLIM Gatherer Testcase Files
Requires:       %{name}-provider = %{version}-%{release}
Requires:       sblim-testsuite
Requires:       cim-server

%description    test
Gatherer Testcase Files for the
SBLIM (Standards Based Linux Instrumentation for Manageability)
Testsuite
%endif

%prep
%setup -q
# for missing providers
tar xfvz %{SOURCE4}
%autopatch -p1

%build
%ifarch s390 s390x ppc ppc64
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char -fno-strict-aliasing"
%else
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%endif
%configure \
%if 0%{?with_test_subpackage}
        TESTSUITEDIR=%{_datadir}/sblim-testsuite \
%endif
%ifarch s390 s390x
        --enable-z \
%endif
        PROVIDERDIR=%{provider_dir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

# for missing providers
pushd missing-providers
  %{cmake}
  pushd redhat-linux-build
    make %{?_smp_mflags}
  popd
popd

%install
make install DESTDIR=$RPM_BUILD_ROOT
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
rm -f $RPM_BUILD_ROOT/%{provider_dir}/*a
rm -f $RPM_BUILD_ROOT/%{_libdir}/gather/*plug/*a
# Install a redirection so that the arch-specific autoconf stuff continues to
# work but doesn't create multilib conflicts.
cat %{SOURCE1} \
        $RPM_BUILD_ROOT/%{_includedir}/gather/gather-config.h > \
        $RPM_BUILD_ROOT/%{_includedir}/gather/gather-config-%{_arch}.h
chmod 644 $RPM_BUILD_ROOT/%{_includedir}/gather/gather-config.h
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_includedir}/gather/

mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -p -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_tmpfilesdir}/sblim-gather.conf

# shared libraries
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/cmpi" > $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# for missing providers
make install/fast DESTDIR=$RPM_BUILD_ROOT -C missing-providers/redhat-linux-build
mkdir -p $RPM_BUILD_ROOT/var/lib/gather

# remove init script, install service files
rm $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/gatherer
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/gatherer.service
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/reposd.service

%files
%config(noreplace) %{_sysconfdir}/*.conf
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%{_unitdir}/gatherer.service
%{_unitdir}/reposd.service
%docdir %{_datadir}/doc/%{name}
%{_bindir}/*
%{_datadir}/doc/%{name}
%{_tmpfilesdir}/sblim-gather.conf
%ghost /var/run/gather
%{_libdir}/lib[^O]*.so.*
%dir %{_libdir}/gather
%{_libdir}/gather/mplug
%{_libdir}/gather/rplug
%{_mandir}/*/*

%files provider
%{_libdir}/gather/cplug
%{_libdir}/libOSBase_MetricUtil.so
%{_libdir}/libOSBase*.so.*
%{_libdir}/cmpi
%{_datadir}/%{name}
%dir /var/lib/gather

%files devel
%{_libdir}/lib[^O]*.so
%{_includedir}/gather

%if 0%{?with_test_subpackage}
%files test
%{_datadir}/sblim-testsuite/cim/Linux*
%{_datadir}/sblim-testsuite/system/linux/Linux*
%{_datadir}/sblim-testsuite/system/linux/gather-systemname.sh
%{_datadir}/sblim-testsuite/test-gather.sh
%endif

%global GATHER_1ST_SCHEMA %{_datadir}/%{name}/Linux_Metric.mof %{_datadir}/%{name}/Linux_MetricProfile.mof
%global GATHER_1ST_REGISTRATION %{_datadir}/%{name}/Linux_Metric.registration %{_datadir}/%{name}/Linux_MetricProfile.registration

%global G_GLOB_IGNORE */Linux_Metric.*

%global SCHEMA %{_datadir}/%{name}/*.mof
%global REGISTRATION %{_datadir}/%{name}/*.registration

%post
install -d -m 0755 -o root -g root /var/run/gather
%{?ldconfig}
%systemd_post gatherer.service
%systemd_post reposd.service

%preun
%systemd_preun gatherer.service
%systemd_preun reposd.service
if [ $1 -eq 0 ]; then
  rm -rf /var/run/gather
  rm -rf /var/lib/gather
fi

%postun
%{?ldconfig}
%systemd_postun_with_restart gatherer.service
%systemd_postun_with_restart reposd.service

%pre provider
function unregister()
{
  # don't let registration failure when server not running fail upgrade!
  GLOBIGNORE=%{G_GLOB_IGNORE}
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{SCHEMA} -r %{REGISTRATION} #> /dev/null 2>&1 || :;
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{GATHER_1ST_SCHEMA} -r %{GATHER_1ST_REGISTRATION} #> /dev/null 2>&1 || :;
}

# if upgrading, deregister old version
if [ $1 -gt 1 ]; then
  unregistered=no
  if [ -e /usr/sbin/cimserver ]; then
    unregister "-t pegasus";
    unregistered=yes
  fi
  if [ -e /usr/sbin/sfcbd ]; then
    unregister "-t sfcb";
    unregistered=yes
  fi
  if [ "$unregistered" != yes ]; then
    unregister
  fi
fi

%post provider
function register()
{
  # don't let registration failure when server not running fail install!
  %{_datadir}/%{name}/provider-register.sh -v $1 -m %{GATHER_1ST_SCHEMA} -r %{GATHER_1ST_REGISTRATION} > /dev/null 2>&1 || :;
  GLOBIGNORE=%{G_GLOB_IGNORE}
  %{_datadir}/%{name}/provider-register.sh -v $1 -m %{SCHEMA} -r %{REGISTRATION} > /dev/null 2>&1 || :;
}

%{?ldconfig}
if [ $1 -ge 1 ]; then
  registered=no
  if [ -e /usr/sbin/cimserver ]; then
    register "-t pegasus";
    registered=yes
  fi
  if [ -e /usr/sbin/sfcbd ]; then
    register "-t sfcb";
    registered=yes
  fi
  if [ "$registered" != yes ]; then
    register
  fi
fi

%preun provider
function unregister()
{
  # don't let registration failure when server not running fail upgrade!
  GLOBIGNORE=%{G_GLOB_IGNORE}
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{SCHEMA} -r %{REGISTRATION} > /dev/null 2>&1 || :;
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{GATHER_1ST_SCHEMA} -r %{GATHER_1ST_REGISTRATION} > /dev/null 2>&1 || :;
}

if [ $1 -eq 0 ]; then
  unregistered=no
  if [ -e /usr/sbin/cimserver ]; then
    unregister "-t pegasus";
    unregistered=yes
  fi
  if [ -e /usr/sbin/sfcbd ]; then
    unregister "-t sfcb";
    unregistered=yes
  fi
  if [ "$unregistered" != yes ]; then
    unregister
  fi
fi

%ldconfig_postun provider

%changelog
* Wed Feb 05 2025 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-38
- Suppress msg when repeated value is detected
- Fix bin/sbin merge related build warning

* Wed Jan 22 2025 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-37
- Fix FTBFS with GCC 15

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-35
- Make test subpackage optional

* Tue Aug 06 2024 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-34
- Fix undefined symbol in libmetricKvm

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-31
- Fix tmpfiles path

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 25 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-29
- SPDX migration

* Mon Feb 27 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-28
- Add systemd-units to BR (fixes FTBFS)
  Resolves: #2171724

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-24
- Fix license
- Fix issues found by static analysis
- Fix incorrect use of temporary paths

* Wed Aug 04 2021 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-23
- Fix FTBFS
  Resolves: #1987989

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.9-21
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-19
- Fix FTBFS
  Resolves: #1865457

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 13 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-16
- Fix multiple definiton of variables (FTBFS with GCC 10)
  Resolves: #1800073

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-14
- Fix link fail with gcc-10 (patch by Jeff Law)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-10
- Add BuildRequires gcc, remove cxx check from cmake
- Remove Group tag
- Enable System Z specific providers for s390 and s390x architecture
- Silence providers (un)registration

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-3
- Update provider registration script to use systemctl to stop/start sfcb
- Fix registration/deregistration
- Require cim-server instead of tog-pegasus, don't BuildRequire tog-pegasus-devel

* Thu Jan 15 2015 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-2
- Fix packaging of tmpfiles

* Mon Oct 13 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.9-1
- Update to sblim-gather-2.2.9
- Use Pegasus root/interop instead of root/PG_Interop

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.8-7
- Fix failing scriptlets when CIMOM is not running

* Mon Mar 17 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.8-6
- Fix multilib conflicts

* Tue Feb 04 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.8-5
- Fix sblim-gather FTBFS if "-Werror=format-security" flag is used
  Resolves: #1037318

* Wed Aug 28 2013 Vitezslav Crhonek <vcrhonek@redhat.com> -  2.2.8-4
- Fix for unversioned docdir change
  Resolves: #994086

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.8-2
- Add -fno-strict-aliasing
- Do not ship old init script, add systemd support

* Mon Mar 18 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.8-1
- Update to sblim-gather-2.2.8

* Wed Feb 27 2013 Roman Rakus <rrakus@redhat.com> - 2.2.7-3
- Fixed a typo
- Added missing providers
- improved providers registration
- Fixed owning of filesystem's directories (man)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.7-1
- Update to sblim-gather-2.2.7
- Add man page BuildRequires, ship man pages

* Thu Sep 06 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.6-2
- Fix issues found by fedora-review utility in the spec file

* Wed Aug 15 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.6-1
- Update to sblim-gather-2.2.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.5-1
- Update to sblim-gather-2.2.5

* Wed Jan 04 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-1
- Update to sblim-gather-2.2.4

* Wed May 18 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.3-1
- Update to sblim-gather-2.2.3

* Thu Mar 24 2011 Vitezlsav Crhonek <vcrhonek@redhat.com> - 2.2.2-3
- Use %%ghost for /var/run/gather
  Resolves: #656686

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.2-1
- Update to sblim-gather-2.2.2

* Mon Jun  7 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-2
- Fix broken dependency because of missing libOSBase_MetricUtil.so

* Wed Jun  2 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-1
- Update to sblim-gather-2.2.1

* Tue Oct 13 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.9-1
- Initial support
