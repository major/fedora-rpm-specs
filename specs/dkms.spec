Summary:        Dynamic Kernel Module Support Framework
Name:           dkms
Version:        3.1.4
Release:        3%{?dist}
License:        GPL-2.0-or-later
URL:            http://linux.dell.com/dkms

BuildArch:      noarch

Source0:        https://github.com/dell/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-Fix-472-capture-error-output.patch

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
Requires:       patch
Requires:       sed
Requires:       tar
Requires:       which

Requires:       (kernel-debug-devel-matched if kernel-debug-core)
Requires:       (kernel-devel-matched if kernel-core)
# RT kernel has no matched:
Requires:       (kernel-rt-devel if kernel-rt-core)
Requires:       (kernel-rt-debug-devel if kernel-rt-debug-core)

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
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_unitdir}/%{name}.service

%changelog
* Mon Dec 30 2024 Simone Caronni <negativo17@gmail.com> - 3.1.4-3
- Fix patch application.

* Mon Dec 30 2024 Simone Caronni <negativo17@gmail.com> - 3.1.4-2
- Fix for #2333382.

* Thu Dec 19 2024 Simone Caronni <negativo17@gmail.com> - 3.1.4-1
- Update to 3.1.4.

* Fri Nov 29 2024 Simone Caronni <negativo17@gmail.com> - 3.1.3-1
- Update to 3.1.3, fixes removal of leftover folders when uninstalling kernel.
- Trim changelog.

* Tue Nov 26 2024 Simone Caronni <negativo17@gmail.com> - 3.1.2-1
- Update to 3.1.2.

* Mon Oct 21 2024 Simone Caronni <negativo17@gmail.com> - 3.1.1-1
- Update to 3.1.1.

* Sat Oct 05 2024 Simone Caronni <negativo17@gmail.com> - 3.1.0-2
- Add fix from upstream.

* Tue Oct 01 2024 Simone Caronni <negativo17@gmail.com> - 3.1.0-1
- Update to 3.1.0.

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.13-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 06 2024 Simone Caronni <negativo17@gmail.com> - 3.0.13-1
- Update to 3.0.13.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

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
