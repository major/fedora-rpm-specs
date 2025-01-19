# -*- rpm-spec -*-

%define with_qemu 1

# RHEL does not provide the 9p.ko kernel module
# nor the virtio-9p KVM backend driver.
%if 0%{?rhel}
%define with_qemu 0
%endif

%define libvirt_version 1.0.2

Name: libvirt-sandbox
Version: 0.8.0
Release: 18%{?dist}
Summary: libvirt application sandbox framework
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: http://libvirt.org/
Source0: ftp://libvirt.org/libvirt/sandbox/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: libvirt-gobject-devel >= 0.2.1
BuildRequires: gobject-introspection-devel
BuildRequires: glibc-static
BuildRequires: /usr/bin/pod2man
BuildRequires: intltool
BuildRequires: libselinux-devel
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: xz-devel >= 5.0.0, xz-static
BuildRequires: zlib-devel >= 1.2.0, zlib-static
%if 0%{fedora} > 27
BuildRequires: libtirpc-devel
BuildRequires: rpcgen
%endif
Requires: %{name}-libs = %{version}-%{release}

%package libs
Summary: libvirt application sandbox framework libraries
# So we get the full libvirtd daemon, not just client libs
%if %{with_qemu}
 %ifarch %{ix86} x86_64
Requires: libvirt-daemon-kvm >= %{libvirt_version}
 %else
Requires: libvirt-daemon-qemu >= %{libvirt_version}
 %endif
%endif
Requires: libvirt-daemon-lxc >= %{libvirt_version}

%package devel
Summary: libvirt application sandbox framework development files
Requires: %{name}-libs = %{version}-%{release}

%description
This package provides a command for running applications within
a sandbox using libvirt.

%description libs
This package provides a framework for building application sandboxes
using libvirt.

%description devel
This package provides development header files and libraries for
the libvirt sandbox

%prep
%setup -q

%build

%configure --enable-introspection
%__make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
chmod a-x examples/*.py examples/*.pl examples/*.js
%__make install  DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt-sandbox-1.0.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt-sandbox-1.0.la

%find_lang %{name}

%ldconfig_scriptlets libs

%files
%{_bindir}/virt-sandbox
%{_mandir}/man1/virt-sandbox.1*

%files libs -f %{name}.lang
%doc README COPYING AUTHORS ChangeLog NEWS
%dir %{_sysconfdir}/libvirt-sandbox
%dir %{_sysconfdir}/libvirt-sandbox/scratch
%config %{_sysconfdir}/libvirt-sandbox/scratch/README
%{_libexecdir}/libvirt-sandbox-init-common
%{_libexecdir}/libvirt-sandbox-init-lxc
%{_libexecdir}/libvirt-sandbox-init-qemu
%{_libdir}/libvirt-sandbox-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtSandbox-1.0.typelib

%files devel
%doc examples/virt-sandbox.pl
%doc examples/virt-sandbox.py
%doc examples/virt-sandbox.js
%doc examples/virt-sandbox-mkinitrd.py
%{_libdir}/libvirt-sandbox-1.0.so
%{_libdir}/pkgconfig/libvirt-sandbox-1.0.pc
%dir %{_includedir}/libvirt-sandbox-1.0
%dir %{_includedir}/libvirt-sandbox-1.0/libvirt-sandbox
%{_includedir}/libvirt-sandbox-1.0/libvirt-sandbox/libvirt-sandbox.h
%{_includedir}/libvirt-sandbox-1.0/libvirt-sandbox/libvirt-sandbox-*.h
%{_datadir}/gir-1.0/LibvirtSandbox-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-sandbox

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 30 2024 Jonathan Wright <jonathan@almalinux.org> - 0.8.0-15
- Rebuild to ensure backdoored XZ libs arn't present

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun  8 2018 Daniel P. Berrangé <berrange@redhat.com> - 0.8.0-1
- Update to 0.8.0 release

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 1  2015 Daniel P. Berrange <berrange@redhat.com> - 0.6.0-1
- Update to 0.6.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.5.1-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.1-1
- Update to 0.5.1 release

* Thu Oct  3 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.0-3
- Add fully versioned dep between libvirt-sandbox & libvirt-sandbox-libs

* Tue Oct  1 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.0-2
- Fix boot with Linux 3.11 kernel

* Thu Aug  1 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.0-1
- Update to 0.5.0 release

* Tue Jul  9 2013 Daniel P. Berrange <berrange@redhat.com> - 0.2.1-1
- Update to 0.2.1 release

* Tue May  7 2013 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-1
- Update to 0.2.0 release

* Tue Mar  5 2013 Daniel P. Berrange <berrange@redhat.com> - 0.1.2-1
- Update to 0.1.2 release

* Fri Feb 22 2013 Daniel P. Berrange <berrange@redhat.com> - 0.1.1-4
- Add dep on pod2man

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Daniel P. Berrange <berrange@redhat.com> - 0.1.1-2
- Conditionalize dep on libvirt-daemon-qemu

* Mon Dec 10 2012 Daniel P. Berrange <berrange@redhat.com> - 0.1.1-1
- Update to 0.1.1 release

* Mon Aug 13 2012 Daniel P. Berrange <berrange@redhat.com> - 0.1.0-1
- Update to 0.1.0 release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-2
- Rebuild for libvirt-gobject update

* Fri Apr 13 2012 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-1
- Update to 0.0.3 release

* Thu Jan 12 2012 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-1
- Update to 0.0.2 release

* Wed Jan 11 2012 Daniel P. Berrange <berrange@redhat.com> - 0.0.1-1
- Initial package

