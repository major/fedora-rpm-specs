Summary:        Dynamic Kernel Module Support Framework
Name:           dkms
Version:        3.1.6
Release:        %autorelease
License:        GPL-2.0-or-later
URL:            http://linux.dell.com/dkms

BuildArch:      noarch

Source0:        https://github.com/dell/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  systemd-rpm-macros

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

%if 0%{?rhel} && 0%{?rhel} < 10
%{?systemd_requires}
%else
%{?systemd_ordering}
%endif

Recommends:     openssl

%description
This package contains the framework for the Dynamic Kernel Module Support (DKMS)
method for installing module RPMS as originally developed by Dell.

%prep
%autosetup -p1

%install
make install-redhat \
    SBIN=%{_bindir} \
    DESTDIR=%{buildroot}

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
%{_bindir}/%{name}
%{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/framework.conf
%dir %{_sysconfdir}/%{name}/framework.conf.d
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
