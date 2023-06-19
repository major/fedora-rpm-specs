%global commit d13097419acb336a8f0631f2f856c6b364f738ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout 20230617git%{shortcommit}

Name:           parcimonie.sh
Version:        0
Release:        %autorelease -p -s %{checkout}
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
install -p -D -m644 -t %{buildroot}/%{_unitdir}/ pkg/parcimonie.sh@.service pkg/parcimonie.sh.user.service
install -p -D -m644 -t %{buildroot}/%{_sysconfdir}/parcimonie.sh.d/ pkg/all-users.conf
install -p -D -m755 -t %{buildroot}/%{_bindir} parcimonie.sh


%files
%license LICENSE
%doc README.md
%doc pkg/sample-configuration.conf.sample
%{_unitdir}/*
%config(noreplace) %{_sysconfdir}/parcimonie.sh.d
%{_bindir}/parcimonie.sh


%changelog
%autochangelog
