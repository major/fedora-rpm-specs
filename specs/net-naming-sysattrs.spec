%global dracutmoddir %{_prefix}/lib/dracut/modules.d

Name:           net-naming-sysattrs
Version:        263
Release:        1%{?dist}
Summary:        Mechanism to emulate older network device naming behavior

License:        MIT
URL:            https://gitlab.com/mschmidt2/%{name}
Source0:        https://gitlab.com/mschmidt2/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(udev)
Requires:       systemd-udev
Requires:       dracut

# RHEL 9 had this stuff in the package "rhel-net-naming-sysattrs",
# versioned together with systemd, so rhel-net-naming-sysattrs-252-*
Obsoletes:      rhel-net-naming-sysattrs < 253
Provides:       rhel-net-naming-sysattrs = %{version}-%{release}

%description
This package provides hwdb and udev rules to filter the sysfs attributes used
by systemd-udev for network device naming.

Historically, the introduction of the "phys_port_name" attribute in newer
kernels caused interface names to change for certain drivers. While these names
can be manually reconfigured with systemd.link files or custom udev rules, this
package offers a streamlined mechanism to emulate the naming behavior of older
distribution releases (RHEL 9.0 and later).

The desired naming scheme can be specified on the kernel command line:
  net.naming-scheme=rhel-9.6
(Default: rhel-9.0)

%prep
%autosetup -n %{name}-v%{version}

%build
# nothing

%check
make test

%install
%make_install

%files
%license LICENSE
%doc README
%{_udevrulesdir}/70-net-naming-sysattrs.rules
%{_udevhwdbdir}/50-net-naming-sysattr-allowlist.hwdb
%dir %{dracutmoddir}/70net-naming-sysattrs
%{dracutmoddir}/70net-naming-sysattrs/module-setup.sh

%changelog
%autochangelog
