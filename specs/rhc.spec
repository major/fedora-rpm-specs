%bcond check 1

%global goipath         github.com/redhatinsights/rhc
Version:                0.3.5

%gometa -L -f

Name:           rhc
Release:        %autorelease
Summary:        Tool for registering to Red Hat services
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml

BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  golang
BuildRequires:  go-rpm-macros
%if %{with check}
BuildRequires:  /usr/bin/dbus-launch
%endif

Requires: subscription-manager
%if 0%{?fedora}
Recommends: insights-client
%else
Requires: insights-client
%endif
Requires: yggdrasil >= 0.4
Requires: yggdrasil-worker-package-manager

%description
Client tool to register Fedora, CentOS Stream or Red Hat Enterprise Linux
to Red Hat Subscription Management and Red Hat Lightspeed.

%prep
%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}

%build
export GO_LDFLAGS="-X main.Version=%{version} -X main.ServiceName=yggdrasil"
%gobuild -o %{gobuilddir}/bin/rhc %{goipath}/cmd/rhc

# Generate man page
%{gobuilddir}/bin/rhc --generate-man-page > rhc.1

%install
%go_vendor_license_install -c %{S:2}
# Binaries
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp _build/bin/*        %{buildroot}%{_bindir}/
# Bash completion
install -m 0755 -vd                     %{buildroot}%{_datadir}/bash-completion/completions
install -m 0644 -vp data/completion/rhc.bash %{buildroot}%{_datadir}/bash-completion/completions/rhc
# Man page
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp rhc.1               %{buildroot}%{_mandir}/man1/
# Systemd files
install -m 0755 -vd                     %{buildroot}%{_unitdir}
install -m 0644 -vp data/systemd/rhc-canonical-facts.*  %{buildroot}%{_unitdir}/

%check
%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2
%endif

%post
%systemd_post rhc-canonical-facts.timer

%preun
%systemd_preun rhc-canonical-facts.timer

%postun
%systemd_postun_with_restart rhc-canonical-facts.timer

%files -f %{go_vendor_license_filelist}
# Binaries
%{_bindir}/rhc
# Bash completion
%{_datadir}/bash-completion/completions/rhc
# Man page
%{_mandir}/man1/*
# Systemd
%{_unitdir}/rhc-canonical-facts.*

%changelog
%autochangelog
