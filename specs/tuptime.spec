Name:		tuptime
Version:	5.2.4
Release:	2%{?dist}
Summary:	Report historical system real time

License:	GPL-2.0-or-later
BuildArch:	noarch
URL:		https://github.com/rfmoz/tuptime/
Source0:	https://github.com/rfmoz/tuptime/archive/%{version}.tar.gz

%{?systemd_requires}
# Check for EPEL Python (python34, python36)
%if 0%{?python3_pkgversion}
BuildRequires:	python%{python3_pkgversion}-devel
%else
BuildRequires:	python3-devel
%endif
%if 0%{?el7}
BuildRequires:	systemd
%else
BuildRequires:	systemd-rpm-macros
%endif
Requires:	systemd
Requires(pre):	shadow-utils


%description
Tuptime track and report historical and statistical real time of the
system, keeping the uptime and downtime between shutdowns.


%prep
%autosetup
# Fix python shebang
%if %{?py3_shebang_fix:1}%{!?py3_shebang_fix:0}
%py3_shebang_fix src/tuptime
%else
# EPEL7 does not have py3_shebang_fix
/usr/bin/pathfix.py -pni "%{__python3} -s" src/tuptime
%endif


%pre
# Conversion to new group and usernames for previously installed version
getent group tuptime >/dev/null && groupmod --new-name _tuptime tuptime
getent passwd tuptime >/dev/null && usermod --login _tuptime tuptime
getent group _tuptime >/dev/null || groupadd --system _tuptime
getent passwd _tuptime >/dev/null || useradd --system --gid _tuptime --home-dir "/var/lib/tuptime" --shell '/sbin/nologin' --comment 'Tuptime execution user' _tuptime > /dev/null


%build


%install
install -d %{buildroot}%{_bindir}/
install -d %{buildroot}%{_unitdir}/
install -d %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_sharedstatedir}/tuptime/
install -d %{buildroot}%{_datadir}/tuptime/
cp src/tuptime %{buildroot}%{_bindir}/
cp src/systemd/tuptime.service %{buildroot}%{_unitdir}/
cp src/systemd/tuptime-sync.service %{buildroot}%{_unitdir}/
cp src/systemd/tuptime-sync.timer %{buildroot}%{_unitdir}/
cp src/man/tuptime.1 %{buildroot}%{_mandir}/man1/
cp misc/scripts/* %{buildroot}%{_datadir}/tuptime/
chmod +x %{buildroot}%{_datadir}/tuptime/*.sh
chmod +x %{buildroot}%{_datadir}/tuptime/*.py


%post
# Create and initialise the tuptime DB with consistent permissions, etc.
su -s /bin/sh _tuptime -c "(umask 0022 && /usr/bin/tuptime -q)"
%systemd_post tuptime.service
%systemd_post tuptime-sync.service
%systemd_post tuptime-sync.timer


%preun
%systemd_preun tuptime.service
%systemd_preun tuptime-sync.service
%systemd_preun tuptime-sync.timer


%postun
%systemd_postun_with_restart tuptime.service
%systemd_postun_with_restart tuptime-sync.service
%systemd_postun_with_restart tuptime-sync.timer


%files
%{_unitdir}/tuptime.service
%{_unitdir}/tuptime-sync.service
%{_unitdir}/tuptime-sync.timer
%attr(0755, root, root) %{_bindir}/tuptime
%dir %attr(0755, _tuptime, _tuptime) %{_sharedstatedir}/tuptime/
%doc tuptime-manual.txt
%doc CHANGELOG README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/tuptime.1.*
%dir %{_datadir}/tuptime
%{_datadir}/tuptime/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Frank Crawford <frank@crawford.emu.id.au> - 5.2.4-1
- New upstream release

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Frank Crawford <frank@crawford.emu.id.au> - 5.2.3-1
- New upstream release

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Frank Crawford <frank@crawford.emu.id.au> - 5.2.2-2
- Update from -x to -q in setup

* Sat Jan 07 2023 Frank Crawford <frank@crawford.emu.id.au> - 5.2.2-1
- New upstream release

* Mon Nov 21 2022 Frank Crawford <frank@crawford.emu.id.au> - 5.2.1-3
- SPDX license update

* Sat Aug 27 2022 Frank Crawford <frank@crawford.emu.id.au> - 5.2.1-1
- New upstream release

* Sat Aug 20 2022 Frank Crawford <frank@crawford.emu.id.au> - 5.2.0-1
- New upstream release

* Sat Aug 20 2022 Frank Crawford <frank@crawford.emu.id.au> - 5.2.0-1
- New upstream release
- Rename systemd unit files from tuptime-cron to tuptime-sync

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 23 2022 Frank Crawford <frank@crawford.emu.id.au> 5.1.0-1
- New upstream release

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Frank Crawford <frank@crawford.emu.id.au> 5.0.2-5
- First offical release in Fedora

* Tue Jan 04 2022 Frank Crawford <frank@crawford.emu.id.au> 5.0.2-4
- Futher updates to spec file following review comments

* Mon Dec 13 2021 Frank Crawford <frank@crawford.emu.id.au> 5.0.2-3
- Update spec file following review comments

* Sun Sep 26 2021 Frank Crawford <frank@crawford.emu.id.au> 5.0.2-2
- Update spec file for Fedora package review
- Copy all relevant documentation

* Sat Jan 02 2021 Ricardo Fraile <rfraile@rfraile.eu> 5.0.2-1
- RPM release
