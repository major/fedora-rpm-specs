%global makeflags VERSION=%{version} PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} SYSTEMDUNITDIR=%{_unitdir}

Name: earlyoom
Version: 1.9.0
Release: %autorelease

License: MIT
URL: https://github.com/rfjakob/%{name}
Summary: Early OOM Daemon for Linux
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.conf

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: pandoc
BuildRequires: gcc
BuildRequires: make

%description
User-space OOM killer daemon that can avoid the system going into the
unresponsive state. It checks the amount of available memory and
free swap up to 10 times a second (less often if there is a lot of free
memory) and kills the largest processes with the highest oom_score.

Percentages are configured through the configuration file.

%prep
%autosetup -p1
cp -f %{SOURCE1} %{name}.default
sed -e '/systemctl/d' -i Makefile

%build
%set_build_flags
%make_build %{makeflags}

%install
%make_install %{makeflags}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%config(noreplace) %{_sysconfdir}/default/%{name}

%changelog
%autochangelog
