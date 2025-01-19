# Ubuntu calls their own software netplan.io in the archive due to name conflicts
%global ubuntu_name netplan.io

# If this isn't defined, define it
%{?!_systemdgeneratordir:%global _systemdgeneratordir /usr/lib/systemd/system-generators}

# Netplan library soversion major
%global libsomajor 0

# networkd is not available everywhere
%if 0%{?rhel} && ! 0%{?epel}
%bcond_with networkd_support
%else
%bcond_without networkd_support
%endif

# Disable tests as they currently require nose, which is deprecated
%bcond_with tests

Name:           netplan
Version:        0.105
Release:        10%{?dist}
Summary:        Network configuration tool using YAML
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://netplan.io/
Source0:        https://github.com/canonical/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream

# Proposed upstream
Patch0101:      netplan-glib-2.56-compat-rhel8.patch

# Downstream only
Patch1001:      netplan-fallback-renderer.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  /usr/bin/pandoc
%if %{with tests}
# For tests
BuildRequires:  /usr/sbin/ip
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(netifaces)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(pyflakes)
BuildRequires:  python3dist(pyyaml)
%endif

# /usr/sbin/netplan is a Python 3 script that requires netifaces and PyYAML
Requires:       python3dist(netifaces)
Requires:       python3dist(pyyaml)
# 'ip' command is used in netplan apply subcommand
Requires:       /usr/sbin/ip
# netplan ships dbus files
Requires:       dbus-common

# Netplan requires a backend for configuration
Requires:       %{name}-default-backend
# Prefer NetworkManager
Suggests:       %{name}-default-backend-NetworkManager

# Netplan requires its core libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# Provide the package name that Ubuntu uses for it too...
Provides:       %{ubuntu_name} = %{version}-%{release}
Provides:       %{ubuntu_name}%{?_isa} = %{version}-%{release}

%description
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

Currently supported backends are NetworkManager and systemd-networkd.

%files
%license COPYING
%doc %{_docdir}/%{name}/
%{_sbindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/dbus-1/system-services/io.netplan.Netplan.service
%{_datadir}/dbus-1/system.d/io.netplan.Netplan.conf
%{_systemdgeneratordir}/%{name}
%{_mandir}/man5/%{name}.5*
%{_mandir}/man8/%{name}*.8*
%dir %{_sysconfdir}/%{name}
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/generate
%{_prefix}/lib/%{name}/%{name}-dbus
%{_datadir}/bash-completion/completions/%{name}

# ------------------------------------------------------------------------------------------------

%package libs
Summary:        Network configuration tool using YAML (core library)

%description libs
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package provides Netplan's core libraries.

%files libs
%license COPYING
%{_libdir}/libnetplan.so.%{libsomajor}{,.*}

# ------------------------------------------------------------------------------------------------

%package devel
Summary:        Network configuration tool using YAML (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package provides development headers and libraries for building applications using Netplan.

%files devel
%{_includedir}/%{name}/
%{_libdir}/libnetplan.so

# ------------------------------------------------------------------------------------------------

%package default-backend-NetworkManager
Summary:        Network configuration tool using YAML (NetworkManager backend)
Requires:       %{name} = %{version}-%{release}
# Netplan requires NetworkManager for configuration
Requires:       NetworkManager
# Disable NetworkManager's autoconfiguration
Requires:       NetworkManager-config-server

# Generally, if linux-firmware-whence is installed, we want Wi-Fi capabilities
Recommends:     (NetworkManager-wifi if linux-firmware-whence)
Suggests:       NetworkManager-wifi

# One and only one default backend permitted
Conflicts:      %{name}-default-backend
Provides:       %{name}-default-backend

BuildArch:      noarch

%description default-backend-NetworkManager
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package configures Netplan to use NetworkManager as its backend.

%files default-backend-NetworkManager
%{_prefix}/lib/%{name}/00-netplan-default-renderer-nm.yaml

# ------------------------------------------------------------------------------------------------

%if %{with networkd_support}
%package default-backend-networkd
Summary:        Network configuration tool using YAML (systemd-networkd backend)
Requires:       %{name} = %{version}-%{release}
# Netplan requires systemd-networkd for configuration
Requires:       systemd-networkd

# Generally, if linux-firmware-whence is installed, we want Wi-Fi capabilities
Recommends:     (wpa_supplicant if linux-firmware-whence)
Suggests:       wpa_supplicant

# One and only one default backend permitted
Conflicts:      %{name}-default-backend
Provides:       %{name}-default-backend

BuildArch:      noarch

%description default-backend-networkd
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package configures Netplan to use systemd-networkd as its backend.

%files default-backend-networkd
%{_prefix}/lib/%{name}/00-netplan-default-renderer-networkd.yaml
%endif

# ------------------------------------------------------------------------------------------------

%prep
%autosetup -p1

# Drop -Werror to avoid the following error:
# /usr/include/glib-2.0/glib/glib-autocleanups.h:28:3: error: 'ip_str' may be used uninitialized in this function [-Werror=maybe-uninitialized]
sed -e "s/-Werror//g" -i Makefile


%build
%make_build CFLAGS="%{build_cflags}"


%install
%make_install ROOTPREFIX=%{_prefix} LIBDIR=%{_libdir} LIBEXECDIR=%{_libexecdir}

# Ensure that libnetplan gets picked up by the dependency generators in RHEL 8
chmod +x %{buildroot}%{_libdir}/libnetplan.so.%{libsomajor}*

# Pre-create the config directory
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

# Generate Netplan default renderer configuration
cat > %{buildroot}%{_prefix}/lib/%{name}/00-netplan-default-renderer-nm.yaml <<EOF
network:
  renderer: NetworkManager
EOF
%if %{with networkd_support}
cat > %{buildroot}%{_prefix}/lib/%{name}/00-netplan-default-renderer-networkd.yaml <<EOF
network:
  renderer: networkd
EOF
%endif


%if %{with tests}
%check
make check
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.105-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.105-3
- Fix libnetplan.so permissions so dependency generation works

* Wed Sep 14 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.105-2
- Fix configuration snippet file ownership

* Tue Aug 23 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.105-1
- Update to 0.105

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Miro Hrončok <mhroncok@redhat.com> - 0.104-2
- Don't require Python packages for explicit Python versions

* Sun Feb 20 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.104-1
- Rebase to 0.104
- Drop EL7 support

* Sat Oct 13 2018 Neal Gompa <ngompa13@gmail.com> - 0.40.3-0
- Rebase to 0.40.3

* Tue Mar 13 2018 Neal Gompa <ngompa13@gmail.com> - 0.34-0.1
- Update to 0.34

* Wed Mar  7 2018 Neal Gompa <ngompa13@gmail.com> - 0.33-0.1
- Rebase to 0.33

* Sat Nov  4 2017 Neal Gompa <ngompa13@gmail.com> - 0.30-1
- Rebase to 0.30

* Sun Jul  2 2017 Neal Gompa <ngompa13@gmail.com> - 0.23~17.04.1-1
- Initial packaging
