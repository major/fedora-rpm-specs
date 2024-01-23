# without tirpc dependency
# if you wish to build without tirpc library, use below command
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without tirpc
%bcond_without tirpc

# without glusterfs dependency
# if you wish to exclude gluster handler in RPM, use below command
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without gluster
%bcond_without gluster

# without azblk dependency
# if you wish to build without azblk library, use below command
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without azblk
%bcond_without azblk

Name:          nbd-runner
Summary:       A daemon that handles the NBD device's IO requests in server side
License:       GPLv2 or LGPLv3+
Version:       0.5.3
Release:       14%{?dist}
URL:           https://github.com/nbd-runner/nbd-runner

Source0:       https://github.com/nbd-runner/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: kmod-devel
BuildRequires: libnl3-devel
BuildRequires: libevent-devel
BuildRequires: glib2-devel
BuildRequires: json-c-devel
BuildRequires: systemd

%if %{with tirpc}
BuildRequires: libtirpc-devel >= 1.0.0
BuildRequires: rpcgen
%endif

%if %{with gluster}
BuildRequires: glusterfs-api-devel
%endif

%if %{with azblk}
BuildRequires: libcurl-devel
BuildRequires: libuv-devel
%endif

Requires:      kmod
Requires:      json-c
Requires:      rsyslog
Requires:      %{name}-utils = %{version}-%{release}

%description
A daemon that handles the userspace side of the NBD (Network Block Device)
back-store.

%prep
%autosetup -p 1

%build
echo v%{version}-%{release} > VERSION
./autogen.sh
%if ( 0%{!?rhel} )
export CFLAGS="%build_cflags -fPIC"
export CPPFLAGS="%build_cxxflags -fPIC"
%endif
%configure %{?_without_tirpc} %{?_without_gluster} %{?_without_azblk}
%make_build

%install
%make_install
find %{buildroot}%{_libdir}/nbd-runner/ -name '*.a' -delete
find %{buildroot}%{_libdir}/nbd-runner/ -name '*.la' -delete

%ldconfig_scriptlets -n nbd-runner-utils

%post
%systemd_post nbd-runner.service nbd-clid.service

%preun
%systemd_preun nbd-runner.service nbd-clid.service

%postun
%systemd_postun_with_restart nbd-runner.service nbd-clid.service

%files
%{_sbindir}/nbd-runner
%{_unitdir}/nbd-runner.service
%{_mandir}/man8/nbd-runner.8.*
%doc README.md
%license COPYING-GPLV2 COPYING-LGPLV3
%config(noreplace) %{_sysconfdir}/sysconfig/nbd-runner
%ghost %attr(0600,-,-) %{_localstatedir}/log/nbd-runner/nbd-runner.log

######## nbd-runner-utils package ########
%package -n nbd-runner-utils
Summary:  A common utils library

%description -n nbd-runner-utils
The common utils library.

%files -n nbd-runner-utils
%dir %{_libdir}/nbd-runner/
%exclude %{_libdir}/nbd-runner/libutils.so
%{_libdir}/nbd-runner/libutils.so.*
%license COPYING-GPLV2 COPYING-LGPLV3
%doc README.md
######## End ########

######## nbd-cli package ########
%package -n nbd-cli
Summary:  A client side service and a command utility
Requires: nbd-runner-utils = %{version}-%{release}

%description -n nbd-cli
A client side service and a command utility.

%files -n nbd-cli
%{_sbindir}/nbd-cli
%{_sbindir}/nbd-clid
%{_unitdir}/nbd-clid.service
%{_mandir}/man8/nbd-cli*.8.*
%doc README.md
%license COPYING-GPLV2 COPYING-LGPLV3
%config(noreplace) %{_sysconfdir}/sysconfig/nbd-clid
%ghost %attr(0600,-,-) %{_localstatedir}/log/nbd-runner/nbd-clid.log
######## End ########

######## gluster handler package ########
%if %{with gluster}
%package -n nbd-runner-gluster-handler
Summary:  Gluster back-store handler
Requires: %{name} = %{version}-%{release}
Requires: glusterfs-api >= 6.6

%description -n nbd-runner-gluster-handler
gluster-handler provide a library for processing the Gluster storage stuff.

%files -n nbd-runner-gluster-handler
%license COPYING-GPLV2 COPYING-LGPLV3
%{_libdir}/nbd-runner/libgluster_handler.so
%doc README.md
%ghost %attr(0600,-,-) %{_localstatedir}/log/nbd-runner/nbd-runner-glfs.log
%endif
######## End ########

######## azblk handler package ########
%if %{with azblk}
%package -n nbd-runner-azblk-handler
Summary:  Azblk back-store handler
Requires: %{name} = %{version}-%{release}

%description -n nbd-runner-azblk-handler
azblk-handler provide a library for processing the Azure storage stuff.

%files -n nbd-runner-azblk-handler
%license COPYING-GPLV2 COPYING-LGPLV3
%{_libdir}/nbd-runner/libazblk_handler.so
%doc README.md
%endif
######## End ########

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 0.5.3-8
- Rebuild for versioned symbols in json-c

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.3-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 20:37:54 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.3-5
- Rebuilt for libevent 2.1.12

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.5.3-3
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Xiubo Li <xiubli@redhat.com> - 0.5.3-1
- Update to 0.5.3-1
- Update the URL to nbd-runner/nbd-runner

* Wed Sep 18 2019 Xiubo Li <xiubli@redhat.com> - 0.5.3-0
- Update to 0.5.3-0
- spec: disable devel library
- server: fix use after free
- azblk: Recover from Azure tcp RST
- map: to reconfigure the dead socket without unmapping the nbd device
- map: make sure the new index is not differ from the existing one
- map: specify a dead connection timeout to resume connections gracefully

* Mon Sep 02 2019 Xiubo Li <xiubli@redhat.com> - 0.5.2-1
- Update to 0.5.2-1
- Disable the devel library

* Tue Aug 27 2019 Xiubo Li <xiubli@redhat.com> - 0.5.2-0
- Update to 0.5.2-0
- Fix the required packages

* Mon Aug 26 2019 Xiubo Li <xiubli@redhat.com> - 0.5.1-0
- Update to 0.5.1-0
- Split to separate rpm packages

* Mon Aug 26 2019 Xiubo Li <xiubli@redhat.com> - 0.5-0
- Update to 0.5-0

* Wed Apr 24 2019 Xiubo Li <xiubli@redhat.com> - 0.4-0
- Initial package
