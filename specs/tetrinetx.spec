Name:           tetrinetx
Version:        1.13.16
Release:        43%{?dist}
Summary:        The GNU TetriNET server

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://tetrinetx.sourceforge.net/
Source0:        http://switch.dl.sourceforge.net/sourceforge/tetrinetx/%{name}-%{version}+qirc-1.40c.tar.gz
Source1:        tetrinetx.init
Source2:        tetrinetx.logrotate
Source3:        tetrinetx.service
Source4:        %{name}-tmpfiles.conf

%{?systemd_requires}
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
BuildRequires:  adns-devel
Requires:       logrotate


%description
Tetrinetx is the GNU TetriNET server written in C. It includes IRC and
Spectator supports. As many other tetrinet servers, it uses IP independent
decryption which allows the server to run behind a router.

TetriNET is a network-based, multiplayer falling bricks game. This package
contains a server for hosting TetriNET games over a public or private network.


%prep
%setup -q -n %{name}-%{version}+qirc-1.40c
# Modify the compile script to use correct directories and use "tetrinetx" as
# the program name
sed -i "s:/usr/local:%{_prefix}:g; s/tetrix\\.linux/tetrinetx/g" -i src/compile.linux

# Modify the default config file to use the correct pid file location
sed -i "s:game\\.pid:%{_localstatedir}/run/tetrinetx/game.pid:" bin/game.conf

# Modify config.h to use correct directories for config files, etc
sed -i "s:game\\.log:%{_localstatedir}/log/tetrinetx/game\\.log:;
        s:game\\.pid:%{_localstatedir}/run/tetrinetx/game\\.pid:;
        s:game\\.winlist:%{_localstatedir}/games/tetrinetx/game\\.winlist:g;
        s:\"game:\"%{_sysconfdir}/tetrinetx/game:g" src/config.h

# Create a sysusers.d config file
cat >tetrinetx.sysusers.conf <<EOF
u tetrinetx - 'Tetrinetx service account' %{_localstatedir}/games/tetrinetx -
EOF


%build
%undefine _fortify_level
cd src
./compile.linux "%{optflags}"
cd ..


%install
# Install executable
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin/tetrinetx %{buildroot}%{_bindir}/
# Install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.conf %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.motd %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.pmotd %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 600 bin/game.secure %{buildroot}%{_sysconfdir}/tetrinetx
# Install system init script
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/tetrinetx.service
# Install logrotate.d entry
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/tetrinetx
# Log files are placed under /var/log/tetrinetx
mkdir -p %{buildroot}%{_localstatedir}/log/tetrinetx
# State data (winlists, etc) for the game will be placed in /var/games/tetrinetx
mkdir -p %{buildroot}%{_localstatedir}/games/tetrinetx
# Tetrinetx pid file goes here
mkdir -p %{buildroot}%{_tmpfilesdir}/
install -p -m 644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/tetrinetx

install -m0644 -D tetrinetx.sysusers.conf %{buildroot}%{_sysusersdir}/tetrinetx.conf



%post
%systemd_post tetrinetx.service

%preun
%systemd_preun tetrinetx.service

%postun
%systemd_postun_with_restart tetrinetx.service

%files
%doc AUTHORS ChangeLog README README.qirc.spectators bin/game.allow.example bin/game.ban.compromise.example bin/game.ban.example
%license COPYING
%{_bindir}/tetrinetx
#{_initrddir}/tetrinetx
%{_unitdir}/tetrinetx.service
%dir %{_sysconfdir}/tetrinetx
%config(noreplace) %{_sysconfdir}/logrotate.d/tetrinetx
%dir %attr(-,tetrinetx,tetrinetx) %{_localstatedir}/log/tetrinetx/
%dir %attr(-,tetrinetx,tetrinetx) %{_localstatedir}/games/tetrinetx/
%dir %attr(-,tetrinetx,tetrinetx) %{_localstatedir}/run/tetrinetx/
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/tetrinetx/*
%{_sysusersdir}/tetrinetx.conf


%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.13.16-43
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13.16-41
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Siddhesh Poyarekar <siddhesh@redhat.com> - 1.13.16-36
- Use _fortify_level macro instead of twiddling with optflags.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.13.16-32
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Sérgio Basto <sergio@serjux.com> - 1.13.16-30
- Typos fixes and remove D_FORTIFY_SOURCE from optflags because breaks tetrinetx

* Sun Aug 09 2020 Sérgio Basto <sergio@serjux.com> - 1.13.16-29
- Add tmpfiles to work out of the box

* Fri Aug 07 2020 Sérgio Basto <sergio@serjux.com> - 1.13.16-28
- Install tetrinet.service

* Fri Aug 07 2020 Jeff Law <law@redhat.com> - 1.13.16-27
- Properly quote arguments passed to compile.linux

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 23 2016 Sérgio Basto <sergio@serjux.com> - 1.13.16-16
- Add Packaging:Systemd
- Spec clean up, add License tag.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.13.16-4
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Francois Aucamp <faucamp@fedoraproject.org> - 1.13.16-3
- Changed initscript to comply with LSB standard
- Fixed package License field

* Tue Mar 13 2007 Francois Aucamp <faucamp@csir.co.za> - 1.13.16-2
- Cleaned up sed scripts in %%prep
- Replaced config.h patch with sed script in order to support RPM macros
- Removed trademarked names from %%description

* Tue Jan 30 2007 Francois Aucamp <faucamp@csir.co.za> - 1.13.16-1
- Initial RPM build
- Created patch to make config.h refer to correct directories
- Created tetrinetx init script
- Created tetrinetx logrotate.d entry
