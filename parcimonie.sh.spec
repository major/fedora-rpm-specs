%global commit 5aa21efa3f5f20eb02a44a9681ec91bf2a380628
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout 20170704git%{shortcommit}

Name:           parcimonie.sh
Version:        0
Release:        0.19.%{checkout}%{?dist}
Summary:        Refresh your GnuPG keyring over Tor

License:        WTFPL
URL:            https://github.com/EtiennePerot/parcimonie.sh
Source0:        https://github.com/EtiennePerot/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  systemd
BuildArch:      noarch

Requires:       torsocks
Requires:       gnupg


%description
parcimonie.sh refreshes individual keys in your GnuPG keyring at randomized
intervals. Each key is refreshed over a unique, single-use Tor circuit.


%prep
%setup -q -n %{name}-%{commit}


%build
# nothing to to here


%install
install -p -D -m755 parcimonie.sh %{buildroot}/%{_datadir}/%{name}/parcimonie.sh
install -p -D -m644 pkg/parcimonie.sh@.service %{buildroot}/%{_unitdir}/parcimonie.sh@.service
install -p -D -m644 pkg/all-users.conf %{buildroot}/%{_sysconfdir}/parcimonie.sh.d/all-users.conf
mkdir -p %{buildroot}/%{_bindir}
ln -sf %{_datadir}/%{name}/parcimonie.sh %{buildroot}/%{_bindir}/parcimonie.sh


%files
%license LICENSE
%doc README.md
%doc pkg/sample-configuration.conf.sample
%{_datadir}/%{name}/
%{_unitdir}/*
%config(noreplace) %{_sysconfdir}/parcimonie.sh.d
%{_bindir}/parcimonie.sh


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20170704git5aa21ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Till Hofmann <till.hofmann@posteo.de> - 0-0.8.20170704git5aa21ef
- Update to latest upstream commit 5aa21ef

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20160427gitfb8eab7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 27 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.6.20160427gitfb8eab7
- Update to newest upstream commit

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20150804gitc009937
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.4.20150804gitc009937
- Update to newest upstream commit with fixed license header

* Mon Jul 27 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.3.20150710gitd7d83f0
- Preserve timestamps during install

* Fri Jul 10 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.2.20150710gitd7d83f0
- Install systemd unit file in the right location

* Fri Jul 10 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0-0.1.20150710gitd7d83f0
- Initial package
