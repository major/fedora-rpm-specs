%global clap_ver 0.11.0
%global zigini_ver 0.5.0
%global ini_ver 0.1.0
%global translate_c_ver 0.0.0
%global aro_ver 0.0.0
%global clap_hash clap-0.11.0-oBajB7foAQC3Iyn4IVCkUdYaOVVng5IZkSncySTjNig1
%global zigini_hash zigini-0.5.0-BSkB7e9WAACfyCBABNZiWL3gFMw18GKn3qBcPs8L1Ec1
%global ini_hash ini-0.1.0-YCQ9YiwsAACghqF8LZyjAF2H_NnL6n29QLuCe0fsmPTo
%global termbox2_hash N-V-__8AAAUXBQD6Fwpi9m0MBqWXFFaqW5l1lVrJC2Ynj7a-
%global translate_c_hash translate_c-0.0.0-Q_BUWvP1BgCjAk6PWv5286tOlvzD9-X-NkuTzh0KxY0Q
%global aro_hash aro-0.0.0-JSD1Qi7QNgDnfcrdEJf82v3o6MhZySjYVrtdfEf3E4Se

Name:           ly
Version:        1.4.0
Release:        %autorelease
Summary:        Lightweight TUI display manager

License:        WTFPL AND MIT
URL:            https://codeberg.org/fairyglade/ly
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/vendor.tar.zst#/%{name}-%{version}-vendor.tar.zst
Patch0:         0001-build-enable-pie.patch

ExclusiveArch:  %{zig_arches}

BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zig >= 0.16
BuildRequires:  zig-rpm-macros
BuildRequires:  zig-srpm-macros

Requires(post):      policycoreutils
Requires(posttrans): policycoreutils

# Right now there is no established way of managing Zig dependencies systemwide,
# so for the time being they are bundled as part of the project.
Provides:       bundled(zig-clap) = %{clap_ver}
Provides:       bundled(zigini) = %{zigini_ver}
Provides:       bundled(ini) = %{ini_ver}
Provides:       bundled(termbox2)
Provides:       bundled(zig-translate-c) = %{translate_c_ver}
Provides:       bundled(aro) = %{aro_ver}

Recommends:     brightnessctl

%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD
designed with portability in mind and doesn't require systemd to run.

%prep
%autosetup -n %{name} -a 1 -p1
%zig_fetch zig-pkg/%{clap_hash}
%zig_fetch zig-pkg/%{zigini_hash}
%zig_fetch zig-pkg/%{ini_hash}
%zig_fetch zig-pkg/%{termbox2_hash}
%zig_fetch zig-pkg/%{translate_c_hash}
%zig_fetch zig-pkg/%{aro_hash}

%build
%zig_build

%install
%zig_build \
    installexe \
    -Ddest_directory=%{buildroot}

# setup.sh is an setup hook.  Keep it under /etc as configuration, but invoke
# it through /bin/sh so it does not need to be an executable config file.
sed -i '1{/^#!/d}' %{buildroot}%{_sysconfdir}/ly/setup.sh
sed -i 's|%{_sysconfdir}/ly/setup.sh|/bin/sh %{_sysconfdir}/ly/setup.sh|' \
    %{buildroot}%{_sysconfdir}/ly/config.ini
sed -i '1{/^#!/d}' %{buildroot}%{_sysconfdir}/ly/startup.sh
sed -i 's|%{_sysconfdir}/ly/startup.sh|/bin/sh %{_sysconfdir}/ly/startup.sh|' \
    %{buildroot}%{_sysconfdir}/ly/config.ini

rm -f %{buildroot}%{_sysconfdir}/ly/config.ini.example

mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr -o %{buildroot}%{_mandir}/man1/ly.1 %{buildroot}%{_bindir}/ly

install -d %{buildroot}%{_licensedir}/ly
install -pm0644 license.md %{buildroot}%{_licensedir}/ly/LICENSE-ly.md
install -pm0644 zig-pkg/%{clap_hash}/LICENSE %{buildroot}%{_licensedir}/ly/LICENSE-zig-clap
install -pm0644 zig-pkg/%{zigini_hash}/LICENSE %{buildroot}%{_licensedir}/ly/LICENSE-zigini
install -pm0644 zig-pkg/%{ini_hash}/LICENCE %{buildroot}%{_licensedir}/ly/LICENSE-ini
install -pm0644 zig-pkg/%{termbox2_hash}/LICENSE %{buildroot}%{_licensedir}/ly/LICENSE-termbox2

%post
%systemd_post ly@.service ly-kmsconvt@.service

# https://codeberg.org/fairyglade/ly/issues/494
%{_sbindir}/semanage fcontext -a -t xdm_exec_t %{_bindir}/ly 2>/dev/null || \
%{_sbindir}/semanage fcontext -m -t xdm_exec_t %{_bindir}/ly 2>/dev/null || :
%{_sbindir}/restorecon %{_bindir}/ly 2>/dev/null || :

%preun
%systemd_preun ly@.service ly-kmsconvt@.service

if [ $1 -eq 0 ]; then
    %{_sbindir}/semanage fcontext -d %{_bindir}/ly 2>/dev/null || :
fi

%files
%license %{_licensedir}/ly/LICENSE-ly.md
%license %{_licensedir}/ly/LICENSE-zig-clap
%license %{_licensedir}/ly/LICENSE-zigini
%license %{_licensedir}/ly/LICENSE-ini
%license %{_licensedir}/ly/LICENSE-termbox2
%doc readme.md

%{_bindir}/ly
%{_mandir}/man1/ly.1*
%{_unitdir}/ly@.service
%{_unitdir}/ly-kmsconvt@.service
%dir %{_sysconfdir}/ly
%dir %{_sysconfdir}/ly/custom-sessions
%dir %{_sysconfdir}/ly/lang
%config(noreplace) %{_sysconfdir}/pam.d/ly
%config(noreplace) %{_sysconfdir}/pam.d/ly-autologin
%config(noreplace) %{_sysconfdir}/ly/config.ini
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/ly/setup.sh
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/ly/startup.sh
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/ly/example.dur
%config(noreplace) %{_sysconfdir}/ly/custom-sessions/README
%config(noreplace) %{_sysconfdir}/ly/lang/*.ini

%changelog
%autochangelog
