Summary:        Dynamic Kernel Module Support Framework
Name:           dkms
Version:        3.0.12
Release:        2%{?dist}
License:        GPLv2+
URL:            http://linux.dell.com/dkms

BuildArch:      noarch

Source0:        https://github.com/dell/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  systemd

Requires:       coreutils
Requires:       cpio
Requires:       elfutils-libelf-devel
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       gcc
Requires:       grep
Requires:       gzip
Requires:       kmod
Requires:       make
Requires:       sed
Requires:       tar
Requires:       which

Requires:       (kernel-debug-devel-matched if kernel-debug-core)
Requires:       (kernel-devel-matched if kernel-core)
Requires:       (kernel-lpae-devel-matched if kernel-lpae-core)

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

Recommends:     openssl

%description
This package contains the framework for the Dynamic Kernel Module Support (DKMS)
method for installing module RPMS as originally developed by Dell.

%prep
%autosetup -p1

%install
make install-redhat DESTDIR=%{buildroot}

# Move 40-dkms.install to read only area (no configuration file):
mkdir -p %{buildroot}%{_prefix}/lib/kernel/
mv %{buildroot}%{_sysconfdir}/kernel/install.d %{buildroot}%{_prefix}/lib/kernel/

sed -i -e 's/# modprobe_on_install="true"/modprobe_on_install="true"/g' %{buildroot}%{_sysconfdir}/%{name}/framework.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%license COPYING
%doc README.md images
%{_prefix}/lib/%{name}
%{_prefix}/lib/kernel/install.d/40-%{name}.install
%{_mandir}/man8/dkms.8*
%{_sbindir}/%{name}
%{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/framework.conf
%dir %{_sysconfdir}/%{name}/framework.conf.d
%{_sysconfdir}/kernel/postinst.d/%{name}
%{_sysconfdir}/kernel/prerm.d/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_unitdir}/%{name}.service

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 3.0.12-1
- Update to 3.0.12.
- Drop support for building from snapshots in SPEC file.
- Trim changelog.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 02 2023 Simone Caronni <negativo17@gmail.com> - 3.0.11-1
- Update to 3.0.11.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Simone Caronni <negativo17@gmail.com> - 3.0.10-2
- Recommend OpenSSL for MOK key management.

* Tue Jan 03 2023 Simone Caronni <negativo17@gmail.com> - 3.0.10-1
- Update to 3.0.10.

* Tue Dec 06 2022 Simone Caronni <negativo17@gmail.com> - 3.0.9-2
- Fix modprobe_on_install variable.

* Mon Dec 05 2022 Simone Caronni <negativo17@gmail.com> - 3.0.9-1
- Update to 3.0.9.

* Fri Oct 28 2022 Simone Caronni <negativo17@gmail.com> - 3.0.8-1
- Update to 3.0.8.

* Tue Sep 27 2022 Simone Caronni <negativo17@gmail.com> - 3.0.7-1
- Update to 3.0.7.

* Tue Aug 09 2022 Simone Caronni <negativo17@gmail.com> - 3.0.6-3
- Adjust kernel devel subpackage requirements.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Simone Caronni <negativo17@gmail.com> - 3.0.6-1
- Update to 3.0.6.

* Wed Jun 29 2022 Simone Caronni <negativo17@gmail.com> - 3.0.5-1
- Update to 3.0.5.

* Sat Jun 18 2022 Simone Caronni <negativo17@gmail.com> - 3.0.4-1
- Update to 3.0.4.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
