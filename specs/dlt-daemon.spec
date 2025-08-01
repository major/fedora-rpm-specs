%if (0%{?rhel} == 10)
%global docs 0
%else
%global docs 1
%endif

Name: dlt-daemon
Version: 2.18.10
Release: 6%{?dist}
Summary: DLT - Diagnostic Log and Trace
Group: System Environment/Base
License: MPL-2.0
URL: https://github.com/COVESA/dlt-daemon
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: dlt-daemon-config.patch
Patch1: dlt-daemon-cmake.patch

BuildRequires: cmake
%if 0%{?docs}
BuildRequires: pandoc
%endif

BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: gcc-c++
%if ((0%{?fedora} >= 38) || (0%{?rhel} >= 10))
BuildRequires: zlib-ng-compat-devel
%else
BuildRequires: zlib-devel
%endif

Requires(pre): shadow-utils

%description
This component provides a standardised log and trace interface, based on the
standardised protocol specified in the AUTOSAR standard 4.0 DLT.
This component can be used by GENIVI components and other applications as
logging facility providing
- the DLT shared library
- the DLT daemon, including startup scripts
- the DLT daemon adaptors
- the DLT client console utilities
- the DLT test applications

%package -n dlt-libs-devel
Summary:        DLT - Diagnostic Log and Trace: Development files
Requires:       dlt-libs = %{version}-%{release}
%description -n dlt-libs-devel
%{summary}.

%package -n dlt-libs
Summary:        DLT - Diagnostic Log and Trace: Libraries
%description -n dlt-libs
%{summary}.

%package -n dlt-tools
Summary:        DLT - Diagnostic Log and Trace: Tools
Recommends:     %{name} = %{version}-%{release}
%description -n dlt-tools
%{summary}.

%package -n dlt-examples
Summary:        DLT - Diagnostic Log and Trace: Examples
Requires:       %{name} = %{version}-%{release}
%description -n dlt-examples
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p1

# Create a sysusers.d config file
cat >dlt-daemon.sysusers.conf <<EOF
u dlt-daemon - 'User for dlt-daemon' /var/lib/dlt-daemon -
EOF

%build
mkdir -p build
cd build
%cmake .. -Wno-dev \
        -DDLT_USER=dlt-daemon \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DWITH_DLT_USE_IPv6=OFF \
        -DDLT_IPC=UNIX_SOCKET \
%if 0%{?docs}
        -DWITH_MAN=ON \
%endif
        -DWITH_SYSTEMD=ON \
        -DWITH_SYSTEMD_WATCHDOG=ON \
        -DWITH_SYSTEMD_JOURNAL=ON \
        -DWITH_DLT_ADAPTOR=ON \
        -DWITH_DLT_SYSTEM=ON \
        -DDLT_USER_IPC_PATH=/run/dlt
%cmake_build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0644 -D dlt-daemon.sysusers.conf %{buildroot}%{_sysusersdir}/dlt-daemon.conf
cd build
%cmake_install

# Home directory for the 'dlt-daemon' user
mkdir -p $RPM_BUILD_ROOT/var/lib/dlt-daemon

%ldconfig_scriptlets -n dlt-libs

%files
%license LICENSE
%doc AUTHORS README.md ReleaseNotes.md
%attr(755,dlt-daemon,dlt-daemon) %dir /var/lib/dlt-daemon
%config(noreplace) %{_sysconfdir}/dlt.conf
%config(noreplace) %{_sysconfdir}/dlt_gateway.conf
%{_unitdir}/dlt.service
%attr(0755,root,root)
%{_bindir}/dlt-daemon
%if 0%{?docs}
%{_mandir}/man1/dlt-daemon.1*
%{_mandir}/man5/dlt.conf.5*
%{_mandir}/man5/dlt_gateway.conf.5*
%endif
%{_sysusersdir}/dlt-daemon.conf

%files -n dlt-examples
# The binaries do not have man pages but do have markdown documents.
%doc doc/dlt-qnx-system.md doc/dlt_build_options.md doc/dlt_cdh.md doc/dlt_demo_setup.md doc/dlt_design_specification.md doc/dlt_example_user.md doc/dlt_extended_network_trace.md doc/dlt_filetransfer.md doc/dlt_for_developers.md doc/dlt_glossary.md doc/dlt_kpi.md doc/dlt_multinode.md doc/dlt_offline_logstorage.md
%{_bindir}/dlt-example-filetransfer
%{_bindir}/dlt-example-user
%{_bindir}/dlt-example-user-common-api
%{_bindir}/dlt-example-user-func
%{_bindir}/dlt-test-client
%{_bindir}/dlt-test-filetransfer
%{_bindir}/dlt-test-fork-handler
%{_bindir}/dlt-test-init-free
%{_bindir}/dlt-test-multi-process
%{_bindir}/dlt-test-multi-process-client
%{_bindir}/dlt-test-non-verbose
%{_bindir}/dlt-test-preregister-context
%{_bindir}/dlt-test-stress
%{_bindir}/dlt-test-stress-client
%{_bindir}/dlt-test-stress-user
%{_bindir}/dlt-test-user
%{_datadir}/dlt-filetransfer/dlt-test-filetransfer-file
%{_datadir}/dlt-filetransfer/dlt-test-filetransfer-image.png
%{_unitdir}/dlt-example-user.service

%files -n dlt-tools
%{_bindir}/dlt-adaptor-stdin
%{_bindir}/dlt-adaptor-udp
%{_bindir}/dlt-control
%{_bindir}/dlt-convert
%{_bindir}/dlt-logstorage-ctrl
%{_bindir}/dlt-passive-node-ctrl
%{_bindir}/dlt-receive
%{_bindir}/dlt-sortbytimestamp
%{_bindir}/dlt-system
%config(noreplace) %{_sysconfdir}/dlt-system.conf
%{_unitdir}/dlt-receive.service
%{_unitdir}/dlt-system.service
%{_unitdir}/dlt-adaptor-udp.service
%if 0%{?docs}
%{_mandir}/man1/dlt-adaptor-stdin.1*
%{_mandir}/man1/dlt-adaptor-udp.1*
%{_mandir}/man1/dlt-control.1*
%{_mandir}/man1/dlt-convert.1*
%{_mandir}/man1/dlt-logstorage-ctrl.1*
%{_mandir}/man1/dlt-passive-node-ctrl.1*
%{_mandir}/man1/dlt-receive.1*
%{_mandir}/man1/dlt-sortbytimestamp.1*
%{_mandir}/man1/dlt-system.1*
%{_mandir}/man5/dlt-system.conf.5*
%endif

%files -n dlt-libs
%{_libdir}/libdlt.so.*

%files -n dlt-libs-devel
%{_includedir}/dlt/*.h
%{_libdir}/pkgconfig/automotive-dlt.pc
%{_libdir}/libdlt.so
%{_libdir}/cmake/automotive-dlt/*.cmake

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Apr 9 2025 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.10-3
- Unify EL9,EL10,F42,rawhide

* Thu Mar 20 2025 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.10-2
- EL10 does not have pandoc so man pages cant be made

* Wed Mar 19 2025 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.10-1
- Update to final 2.18.10 version

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.18.9-7
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 17 2023 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.9-1
- Update to final 2.18.9 version

* Mon Mar  6 2023 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.8-6.20230306git0a06fcb
- Update code to latest upstream git commit
- migrated to SPDX license
- Update patchset for fat finger problem in upstream on udp package.

* Wed Mar 2 2022 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.8-4
- Make temporary changes to remove pandoc requirements. This removes
  man pages from the EPEL-9 package.

* Tue Feb 22 2022 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.8-3
- Require shadow-utils in pre for user creation
- Add markdown documentation for examples
- Add config(noreplace) to sysconfdir items.

* Tue Feb 22 2022 Alexander Larsson <alexl@redhat.com> - 2.18.8-2
- Marked config files
- Change config to store data in /var/lib/dlt-daemon instead of /tmp
- Store sockets in /run/dlt, not in /tmp
- Tweak source url to get better named source tarballs

* Tue Dec 14 2021 Stephen Smoogen <smooge@fedoraproject.org> - 2.18.8-1
- Upgrade to 2.18.8 from upstream
- Start rpmlint clean

* Wed May 12 2021 Alexander Larsson <alexl@redhat.com> - 2.18.6-2
- Enable more features and split up subpackages

* Wed May 12 2021 Mark Kirichenko <mark.kirichenko@daimler.com> - 2.18.6-1
- Initial version of the .spec file
