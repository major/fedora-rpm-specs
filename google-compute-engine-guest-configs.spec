%global srcname guest-configs

Name: google-compute-engine-guest-configs
Version: 20230217.01
Release: %autorelease
Summary: Google Compute Engine guest environment tools
License: ASL 2.0
URL: https://github.com/GoogleCloudPlatform/%{srcname}
Source0: %{url}/archive/%{version}.tar.gz

ExcludeArch: %{ix86}
BuildArch: noarch

Requires: dhcp-client
Requires: dracut
Requires: google-compute-engine-oslogin
Requires: google-guest-agent
Requires: rsyslog
Requires: nvme-cli
BuildRequires: systemd
Obsoletes: google-compute-engine-tools < 2.8.12-11
Provides: google-compute-engine-tools = 2.8.12-11
Provides: google-compute-engine = %{version}-%{release}

%description
This package contains scripts, configuration, and init files for features
specific to the Google Compute Engine cloud environment.

%prep
%autosetup -n %{srcname}-%{version}

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
%attr(0755,-,-) %{_bindir}/*
%attr(0755,-,-) /etc/dhcp/dhclient.d/google_hostname.sh
%attr(0755,-,-) %{_udevrulesdir}/../google_nvme_id
%{_udevrulesdir}/*
%{_prefix}/lib/dracut/dracut.conf.d/*.conf
%{_prefix}/lib/modprobe.d/*.conf
%config(noreplace) /etc/rsyslog.d/*
%config(noreplace) /etc/sysctl.d/*

%changelog
%autochangelog
