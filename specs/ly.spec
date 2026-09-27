%global clap_hash clap-0.11.0-oBajB7foAQC3Iyn4IVCkUdYaOVVng5IZkSncySTjNig1
%global zigini_hash zigini-0.5.0-BSkB7e9WAACfyCBABNZiWL3gFMw18GKn3qBcPs8L1Ec1
%global ini_hash ini-0.1.0-YCQ9YiwsAACghqF8LZyjAF2H_NnL6n29QLuCe0fsmPTo
%global termbox2_hash N-V-__8AAAUXBQD6Fwpi9m0MBqWXFFaqW5l1lVrJC2Ynj7a-
%global translate_c_hash translate_c-1.0.0-Q_BUWo_5BgD4flHdUhA31zOz0XvZk9k7lQv1ouzyNXj2
%global zlua_hash zlua-0.1.0-hGRpC2aABQD4D9PBVH3wAW8k32-I4969MRQ0CpOwoley
%global luajit_hash N-V-__8AAODpQgCVrpfzE2ze9FA_rOuByh3WKyIyk5iS_o9a

%global selinuxtype targeted

Name:           ly
Version:        1.5.0~rc1
Release:        %autorelease
Summary:        Lightweight TUI display manager

%global upstream_version %{gsub %{version} ~ -}

License:        WTFPL AND MIT
URL:            https://codeberg.org/fairyglade/ly
Source0:        %{url}/archive/v%{upstream_version}.tar.gz#/%{name}-%{upstream_version}.tar.gz
Source1:        %{url}/releases/download/v%{upstream_version}/vendor.tar.zst#/%{name}-%{upstream_version}-vendor.tar.zst
# SELinux policy module, https://codeberg.org/fairyglade/ly/issues/494
Source2:        ly.te
Source3:        ly.fc
# Fedora requires position independent executables
Patch0:         0001-build-enable-pie.patch
# Link against the system LuaJIT instead of the bundled copy
Patch1:         0002-build-use-system-luajit.patch

ExclusiveArch:  %{zig_arches}
# LuaJIT is not available on riscv64
ExcludeArch:    riscv64

BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pam-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zig >= 0.16
BuildRequires:  zig-rpm-macros

# ly@.service launches ly through agetty
Requires:       util-linux-core
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})

# Right now there is no established way of managing Zig dependencies systemwide,
# so for the time being they are bundled as part of the project.
Provides:       bundled(zig-clap) = 0.11.0
Provides:       bundled(zigini) = 0.5.0
Provides:       bundled(ini) = 0.1.0
Provides:       bundled(termbox2)
Provides:       bundled(zig-translate-c) = 1.0.0
Provides:       bundled(zig-translate-c) = 0.0.0
Provides:       bundled(aro) = 0.0.0
Provides:       bundled(ziglua) = 0.1.0

Recommends:     brightnessctl

%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD
designed with portability in mind and doesn't require systemd to run.

%package        selinux
Summary:        SELinux policy module for ly
License:        MIT
BuildArch:      noarch
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
%{?selinux_requires}

%description    selinux
SELinux policy module that runs ly in the display manager domain.

%prep
%autosetup -n %{name} -a 1 -p1
rm -r zig-pkg/%{luajit_hash}

mkdir licenses
cp -p zig-pkg/%{clap_hash}/LICENSE licenses/LICENSE-zig-clap
cp -p zig-pkg/%{zigini_hash}/LICENSE licenses/LICENSE-zigini
cp -p zig-pkg/%{ini_hash}/LICENCE licenses/LICENSE-ini
cp -p zig-pkg/%{termbox2_hash}/LICENSE licenses/LICENSE-termbox2
cp -p zig-pkg/%{translate_c_hash}/LICENSE licenses/LICENSE-zig-translate-c
cp -p zig-pkg/%{zlua_hash}/license licenses/LICENSE-ziglua

%build
%zig_build

mkdir selinux
cp -p %{SOURCE2} %{SOURCE3} selinux/
%make_build -C selinux -f %{_datadir}/selinux/devel/Makefile ly.pp

%install
%zig_build \
    installexe \
    -Ddest_directory=%{buildroot}

# setup.sh and startup.sh are hooks.  Keep them under /etc as configuration, but
# invoke them through /bin/sh so they do not need to be executable config files.
# Keep the save file out of /etc as well.
sed -i '1{/^#!/d}' %{buildroot}%{_sysconfdir}/ly/{setup,startup}.sh
sed -i -E \
    -e 's@%{_sysconfdir}/ly/(setup|startup)\.sh@/bin/sh &@' \
    -e 's@^save_file_dir = .*@save_file_dir = %{_sharedstatedir}/ly@' \
    %{buildroot}%{_sysconfdir}/ly/config.ini
install -d %{buildroot}%{_sharedstatedir}/ly

rm %{buildroot}%{_sysconfdir}/ly/config.ini.example

mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr -o %{buildroot}%{_mandir}/man1/ly.1 %{buildroot}%{_bindir}/ly

install -Dpm0644 selinux/ly.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/ly.pp

%check
%{buildroot}%{_bindir}/ly --validate-config %{buildroot}%{_sysconfdir}/ly/config.ini

%post
%systemd_post ly@.service ly-kmsconvt@.service

%preun
%systemd_preun ly@.service ly-kmsconvt@.service

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/ly.pp
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} ly
    %selinux_relabel_post -s %{selinuxtype}
fi

%files
%license license.md licenses/*
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
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/ly/example.lua
%config(noreplace) %{_sysconfdir}/ly/custom-sessions/README
%config(noreplace) %{_sysconfdir}/ly/lang/*.ini
%dir %{_sharedstatedir}/ly

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/ly.pp
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/ly

%changelog
%autochangelog
