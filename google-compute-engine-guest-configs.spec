%global         srcname     guest-configs

%global         forgeurl    https://github.com/GoogleCloudPlatform/%{srcname}
Version:        20230403.00
%global         tag         %{version}
%forgemeta

Name:           google-compute-engine-guest-configs
Release:        %autorelease
Summary:        Google Compute Engine guest environment tools
License:        ASL 2.0
URL:            %forgeurl
Source0:        %forgesource

ExcludeArch:    %{ix86}
BuildArch:      noarch

Requires:       dhcp-client
Requires:       dracut

BuildRequires:  systemd-rpm-macros

Obsoletes:      google-compute-engine-tools < 2.8.12-11
Provides:       google-compute-engine-tools = 2.8.12-11
Provides:       google-compute-engine = %{version}-%{release}

%description
This package contains scripts, configuration, and init files for features
specific to the Google Compute Engine cloud environment.


%package rsyslog
Summary:        rsyslog configuration for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       rsyslog

%description rsyslog
The %{name}-udev package contains
rsyslog configuration which are specific to the Google Cloud Platform.


%package udev
Summary:        udev rules for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       nvme-cli
Requires:       systemd-udev

%description udev
The %{name}-udev package contains udev rules
which are specific to the Google Cloud Platform.


%prep
%forgeautosetup

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


%files
%license LICENSE
%doc README.md
%attr(0755,-,-) %{_bindir}/google_optimize_local_ssd
%attr(0755,-,-) %{_bindir}/google_set_hostname
%attr(0755,-,-) %{_bindir}/google_set_multiqueue
%attr(0755,-,-) /etc/dhcp/dhclient.d/google_hostname.sh
%{_prefix}/lib/dracut/dracut.conf.d/gce.conf
%{_prefix}/lib/modprobe.d/gce-blacklist.conf
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
%{_udevrulesdir}/64-gce-disk-removal.rules


%changelog
%autochangelog
