# filter provides and requires from examples directory RHBZ#1263969
%{?perl_default_filter}

%global enable_tests 0

Name:       statsd
Version:    0.8.6
Release:    11%{?dist}
Summary:    A simple, lightweight network daemon to collect metrics over UDP
License:    MIT
URL:        https://github.com/statsd/statsd
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    statsd.service

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  dos2unix
BuildRequires:  nodejs-packaging
BuildRequires:  perl-generators

%if 0%{?enable_tests}
BuildRequires:  npm(temp)
BuildRequires:  nodeunit
BuildRequires:  npm(underscore)
%endif

Requires(pre):  shadow-utils

BuildRequires:      systemd
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd


%description
A network daemon that runs on the Node.js platform and listens for statistics, 
like counters and timers, sent over UDP or TCP and sends aggregates to one or 
more pluggable backend services (e.g., Graphite).


%prep
%autosetup -n %{name}-%{version}

%nodejs_fixdep generic-pool 2.x

# fix end of line encodings
/usr/bin/dos2unix examples/go/statsd.go
/usr/bin/dos2unix examples/csharp_example.cs

# set Graphitehost to localhost in default config
sed -i 's/graphite\.example\.com/localhost/' exampleConfig.js


%build
#nothing to do


%install
%{__mkdir_p} %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json proxy.js stats.js utils %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr backends lib bin servers %{buildroot}%{nodejs_sitelib}/%{name}

%{__mkdir_p} %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}
cp -pr exampleConfig.js %{buildroot}%{_sysconfdir}/%{name}/config.js

%{__install} -Dp -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
./run_tests.sh
%endif


%pre
getent group statsd >/dev/null || groupadd -r statsd
getent passwd statsd >/dev/null || \
    useradd -r -g statsd -d / -s /sbin/nologin \
    -c "statsd daemon user" statsd
exit 0


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README.md CONTRIBUTING.md Changelog.md exampleConfig.js exampleProxyConfig.js docs/ examples/
%license LICENSE
%{nodejs_sitelib}/%{name}
%{_bindir}/statsd
%{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.js

%{_unitdir}/%{name}.service


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.6-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Piotr Popieluch <piotr1212@gmail.com> - 0.8.6-1
- Update upstream from etsy/statsd to statsd/statsd
  Update to 8.6
  Conditionalize buildrequires

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9.8d5363c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8.8d5363c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7.8d5363c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6.8d5363c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5.8d5363c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4.8d5363c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Piotr Popieluch <piotr1212@gmail.com> - 0.8.0-3
- add missing servers directory
- fix systemd installation
- fix selinux issues

* Wed Jun 13 2018 Piotr Popieluch <piotr1212@gmail.com> - 0.8.0-2
- fixdep generic-pool

* Wed Jun 13 2018 Piotr Popieluch <piotr1212@gmail.com> - 0.8.0-1
- Update to 0.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-10
- Add "Wants=network.target" to unitfile RHBZ#1502746

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-6
- filter perl provides and requires RHBZ#1263969
- move license to license tag

* Tue Jul 07 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-5
- set correct ExclusiveArch for EPEL

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec  2 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-3
- fix end of line encodings

* Tue Nov 18 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-2
- added epel6 support

* Sat Nov 15 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.7.2-1
- Initial package
