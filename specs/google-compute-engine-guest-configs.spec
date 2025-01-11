%global         srcname     guest-configs
%global         dracutlibdir %{_prefix}/lib/dracut

Name:           google-compute-engine-guest-configs
Version:        20250107.00
Release:        %autorelease
Summary:        Google Compute Engine guest environment tools
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/%{srcname}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

ExcludeArch:    %{ix86}
BuildArch:      noarch

Requires:       dracut

BuildRequires:  systemd-rpm-macros

Obsoletes:      google-compute-engine-tools < 2.8.12-11
Provides:       google-compute-engine-tools = 2.8.12-11
Provides:       google-compute-engine = %{version}-%{release}

Requires:       %name-rsyslog = %version-%release
Requires:       %name-udev = %version-%release

%description
This package contains scripts, configuration, and init files for features
specific to the Google Compute Engine cloud environment.


%package rsyslog
Summary:        rsyslog configuration for %{name}
Requires:       rsyslog

%description rsyslog
The %{name}-udev package contains
rsyslog configuration which are specific to the Google Cloud Platform.


%package udev
Summary:        udev rules for %{name}
Requires:       nvme-cli
Requires:       coreutils

%description udev
The %{name}-udev package contains udev rules
which are specific to the Google Cloud Platform.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove APT configs (for Debian and Ubuntu).
rm -rf src/etc/apt
# Remove script for EL6.
rm -f  src/sbin/google-dhclient-script

# Move dracut and modprobe.d from /etc to /usr/lib to allow
# user to put modifications in /etc that will be retained
# after update.
# https://bugzilla.redhat.com/show_bug.cgi?id=1925323
mkdir -p src/usr/lib/dracut
mv src/etc/dracut.conf.d src/usr/lib/dracut
mv src/etc/modprobe.d src/usr/lib

%build


%install
cp -vpR                     src/{etc,usr}                   %{buildroot}
install -m 0755 -vdp        %{buildroot}%{_udevrulesdir}
cp -vp                      src/lib/udev/rules.d/*          %{buildroot}%{_udevrulesdir}
cp -vp                      src/lib/udev/google_nvme_id     %{buildroot}%{_udevrulesdir}/../
# dracut module for udev package
install -m 0755 -vdp %{buildroot}%{dracutlibdir}/modules.d/30gcp-udev-rules
cp -vp  src/lib/dracut/modules.d/30gcp-udev-rules/module-setup.sh %{buildroot}%{dracutlibdir}/modules.d/30gcp-udev-rules/


%files
%license LICENSE
%doc README.md
%attr(0755,-,-) %{_bindir}/gce-nic-naming
%attr(0755,-,-) %{_bindir}/google_optimize_local_ssd
%attr(0755,-,-) %{_bindir}/google_set_hostname
%attr(0755,-,-) %{_bindir}/google_set_multiqueue
%attr(0755,-,-) /etc/dhcp/dhclient.d/google_hostname.sh
%{_prefix}/lib/dracut/dracut.conf.d/gce.conf
%{_prefix}/lib/modprobe.d/gce-blacklist.conf
%{_prefix}/lib/networkd-dispatcher/routable.d/google_hostname.sh
%{_sysconfdir}/sysconfig/network/scripts/google_up.sh
%{_sysconfdir}/systemd/resolved.conf.d/gce-resolved.conf
%{_sysconfdir}/NetworkManager/dispatcher.d/google_hostname.sh
%config(noreplace) /etc/sysctl.d/60-gce-network-security.conf


%files rsyslog
%license LICENSE
%doc README.md
%config(noreplace) /etc/rsyslog.d/90-google.conf


%files udev
%license LICENSE
%doc README.md
%attr(0755,-,-) %{_udevrulesdir}/../google_nvme_id
%{_udevrulesdir}/65-gce-disk-naming.rules
%{_udevrulesdir}/75-gce-network.rules
%attr(0755,-,-) %{dracutlibdir}/modules.d/30gcp-udev-rules/module-setup.sh


%changelog
%autochangelog
