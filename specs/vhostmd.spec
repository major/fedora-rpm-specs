%global have_xen 0

Summary:       Virtualization host metrics daemon
Name:          vhostmd
Version:       1.1
Release:       18%{?dist}
License:       LGPL-2.1-or-later

URL:           https://github.com/vhostmd/vhostmd

Source0:       https://github.com/vhostmd/vhostmd/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       vhostmd.conf

# Prevents updates from previous versions with the old config file
# from breaking (RHBZ#1782897).
# https://github.com/vhostmd/vhostmd/commit/83cc269f6892852be94467cea771b3ad1da8a369
Patch0001:     0001-Relax-virtio-requirement-in-config-file.patch
Patch0002:     0002-libmetrics-Set-pointer-NULL-after-free.patch
Patch0003:     0003-libmetrics-Initialize-local-variable-ret-to-failure.patch
Patch0004:     0004-libmetrics-Check-return-value-of-asprintf.patch
Patch0005:     0005-libmetrics-Remove-unsafe-XML_PARSE_NOENT-option.patch
Patch0006:     0006-libmetrics-Ensure-libmetrics-mutex-is-unlocked-in-er.patch
Patch0007:     0007-libmetrics-Fix-potential-memory-leak.patch
Patch0008:     0008-libmetrics-Use-proper-conversion-specifier-when-call.patch
Patch0009:     0009-libmetrics-Fix-potential-leak-of-FILE-pointer.patch
Patch0010:     0010-util-Add-missing-call-to-va_end.patch
Patch0011:     0011-util-Fix-potential-memory-leak.patch
Patch0012:     0012-util-Check-return-value-of-strstr.patch
Patch0013:     0013-Check-return-value-of-asprintf.patch
Patch0014:     0014-vhostmd-Fix-memory-leak-in-parse_transports.patch
Patch0015:     0015-vhostmd-Remove-unsafe-XML_PARSE_NOENT-option.patch
Patch0016:     0016-vhostmd-Check-return-value-of-file-functions.patch
Patch0017:     0017-vhostmd-Check-for-valide-file-handle-before-calling-.patch
Patch0018:     0018-vhostmd-Fix-memory-leak-in-vhostmd_run.patch
Patch0019:     0019-virtio-Fix-strncpy-length-parameter.patch
# https://github.com/vhostmd/vhostmd/pull/13
Patch0020:     0020-implicit-function-declarations.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: chrpath
BuildRequires: perl-generators
BuildRequires: pkgconfig
BuildRequires: libxml2-devel
BuildRequires: libvirt-devel
BuildRequires: autoconf, automake, libtool
BuildRequires: git
%{?systemd_requires}
BuildRequires: systemd

%if %{have_xen}
BuildRequires: xen-devel
%endif

# This is hopefully temporary, but required to run vhostmd.xml as
# currently written.  For more information see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1897130
Requires:      libvirt


%description 
vhostmd provides a "metrics communication channel" between a host and
its hosted virtual machines, allowing limited introspection of host
resource usage from within virtual machines.


%package -n    vm-dump-metrics
Summary:       Virtualization host metrics dump 


%description -n vm-dump-metrics
Executable to dump all available virtualization host metrics to stdout
or a file.


%package -n    vm-dump-metrics-devel
Summary:       Virtualization host metrics dump development 
Requires:      vm-dump-metrics = %{version}-%{release}
Requires:      pkgconfig


%description -n vm-dump-metrics-devel
Header and libraries necessary for metrics gathering development


%prep
%autosetup -S git


%build
autoreconf -i
%configure \
%if %{have_xen} == 0
  --without-xenstore \
%endif
  --with-init-script=systemd \
  --enable-shared --disable-static
make %{_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT%{_libdir}/libmetrics.la

chrpath --delete $RPM_BUILD_ROOT%{_sbindir}/vm-dump-metrics

# Remove docdir - we'll make a proper one ourselves.
rm -r $RPM_BUILD_ROOT%{_docdir}/vhostmd

# Remove metric.dtd from /etc.
rm $RPM_BUILD_ROOT%{_sysconfdir}/vhostmd/metric.dtd

# The default configuration file is great for Xen, not so great
# for anyone else.  Replace it with one which is better for libvirt
# users.
rm $RPM_BUILD_ROOT%{_sysconfdir}/vhostmd/vhostmd.conf
cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/vhostmd/vhostmd.conf

%if 0%{?rhel}
# Remove Perl script (https://bugzilla.redhat.com/show_bug.cgi?id=749875)
rm $RPM_BUILD_ROOT%{_datadir}/vhostmd/scripts/pagerate.pl
%endif


%pre
# UID:GID 112:112 reserved, see RHBZ#534109.
%sysusers_create_inline u vhostmd 112 "Virtual Host Metrics Daemon" %{_datadir}/vhostmd /sbin/nologin


%post
%systemd_post vhostmd.service


%preun
%systemd_preun vhostmd.service


%postun
%systemd_postun_with_restart vhostmd.service


%files
%doc AUTHORS ChangeLog COPYING README
%doc mdisk.xml metric.dtd vhostmd.dtd vhostmd.xml

%{_sbindir}/vhostmd

%dir %{_sysconfdir}/vhostmd
%config(noreplace) %{_sysconfdir}/vhostmd/vhostmd.conf
%config %{_sysconfdir}/vhostmd/vhostmd.dtd

%{_unitdir}/vhostmd.service

%dir %{_datadir}/vhostmd
%dir %{_datadir}/vhostmd/scripts
%if !0%{?rhel}
%{_datadir}/vhostmd/scripts/pagerate.pl
%endif

%{_mandir}/man8/vhostmd.8.gz


%files -n vm-dump-metrics
%doc COPYING
%{_sbindir}/vm-dump-metrics
%{_libdir}/libmetrics.so.0
%{_libdir}/libmetrics.so.0.0.0
%{_mandir}/man1/vm-dump-metrics.1.gz


%files -n vm-dump-metrics-devel
%doc README
%{_libdir}/libmetrics.so
%dir %{_includedir}/vhostmd
%{_includedir}/vhostmd/libmetrics.h


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1-10
- Miscellaneous upstream fixes.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 09 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1-7
- Unify vhostmd.conf with RHEL 8.4 (RHBZ#1924966).

* Thu Feb 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1-6
- Increase release so > RHEL 8 (RHBZ#1924966).
- Unify spec files between RHEL and Fedora.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-1
- Upstream version 1.1.
- Remove patches, since all included 1.1.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0-2
- Upstream version 1.0.
- Remove patches, since all included 1.0.
- Add patches since 1.0.
- Fix Source0 URL, hosted on github.
- Remove old Source1 and Source2, not used.

* Tue Oct 16 2018 Richard W.M. Jones <rjones@redhat.com> - 0.5-19
- Include all upstream patches since 0.5.
- Enable systemd init scripts (RHBZ#1592400).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Richard W.M. Jones <rjones@redhat.com> - 0.5-17
- Remove ldconfig
  https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/SU3LJVDZ7LUSJGZR5MS72BMRAFP3PQQL/

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5-16
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Richard Jones <rjones@redhat.com> - 0.5-11
- Remove useless defattr in files section.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.5-7
- Perl 5.18 rebuild

* Mon Jul 29 2013 Richard W.M. Jones <rjones@redhat.com> - 0.5-6
- Completely disable Xen.  APIs seem to have changed incompatibly.
- Add commits from upstream since 0.5.
- Remove pagerate.pl when building on RHEL.
- Modernize the spec file.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.5-5
- Perl 5.18 rebuild

* Thu May 23 2013 Richard W.M. Jones <rjones@redhat.com> - 0.5-4
- Disable Xen support on RHEL >= 6 (RHBZ#927853).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Richard W.M. Jones <rjones@redhat.com> - 0.5-1
- New upstream version 0.5.
- Remove -ldl patch which is now upstream.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Richard W.M. Jones <rjones@redhat.com> - 0.4-11
- /etc/sysconfig/vhostmd: Default to KVM.

* Tue Jul 13 2010 Richard W.M. Jones <rjones@redhat.com> - 0.4-10
- Patch Makefile.in directly so we don't need to run autotools.

* Tue Jul  6 2010 Richard W.M. Jones <rjones@redhat.com> - 0.4-9
- Updated vhostmd.conf from Dr. Joachim Schneider at SAP.
- Run aclocal.

* Tue Apr 27 2010 Richard W.M. Jones <rjones@redhat.com> - 0.4-6
- Updated vhostmd.conf file which enables TotalCPUTime metric.

* Tue Feb 16 2010 Richard W.M. Jones <rjones@redhat.com> - 0.4-5
- Add a patch to link tests explicitly with -ldl (RHBZ#565096).

* Thu Dec 10 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-2
- Fix the PagedOutMemory and PagedInMemory stats to report MB instead
  of pages (fixes supplied by Joachim Schneider).

* Wed Dec  9 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-1
- vhostmd didn't chdir ("/") when daemonizing.  Fixed in this 0.4 release.

* Tue Nov 17 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-0.9.gite9db007b
- Add a timestamp to the metrics.
- Fix a typo in MemoryAllocatedToVirtualServers metric
  (https://bugzilla.redhat.com/show_bug.cgi?id=532070#c7)
- %%{_sysconfdir}/sysconfig/vhostmd: Use libvirt default URI
  (https://bugzilla.redhat.com/show_bug.cgi?id=537828)
- %%{_sysconfdir}/init.d/vhostmd: If using libvirt's default URI, then pass
  the root URI to vhostmd (the default URI changes in some circumstances
  when vhostmd switches to the non-root user).

* Wed Nov 11 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-0.8.gite9db007b
- Use fixed UID:GID 112:112 (RHBZ#534109).

* Tue Nov 10 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-0.7.gite9db007b
- vm-dump-metrics-devel package should require version and release of
  base package.

* Mon Nov  2 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-0.6.gite9db007b
- Some changes to the default configuration file suggested by SAP to
  make it more CIM standards compliant.

* Fri Oct 16 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-0.5.gite9db007b
- New upstream based on git e9db007b.
- Fix segfault in vm-dump-metrics (RHBZ#529348).
- On error, vm-dump-metrics now exits with status code 1.

* Thu Oct 15 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-0.2.gitea2f772d
- New upstream based on git ea2f772d.
- Update the configuration file based on upstream changes to how virsh
  has to be run.
- vhostmd should run non-root as user 'vhostmd'.
- Allow libvirt URI to be configured.

* Tue Oct 13 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4-0.1.git326f0012172
- Move to pre-release of 0.4, self-built tarball.
- Disable xenstore on non-x86 platforms.
- Add patch to fix --without-xenstore option.
- Use have_xen RPM macro.

* Mon Oct 12 2009 Richard W.M. Jones <rjones@redhat.com> - 0.3-3
- Remove metric.dtd file from /etc (fixes rpmlint warning), but
  vhostmd.dtd has to remain because it is needed to validate the
  XML configuration file.
- Remove ExclusiveArch, instead conditionally depend on xen-devel.
- Use a better, less noisy, more minimal configuration file which
  doesn't depend on Xen.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.3-1
- New upstream version 0.3.

* Fri Aug 14 2009 Richard W.M. Jones <rjones@redhat.com> - 0.2-1
- Initial packaging for Fedora, based on SuSE package.
