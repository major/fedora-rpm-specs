%global commit0 627468b537befb16c0d04e426450b2fe7eb85c9f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0   20170903

Name:           openconnect-gateway
Version:        0 
Release:        0.9.%{date0}git%{shortcommit0}%{?dist}
Summary:        Connect to a VPN without routing everything through the VPN

License:        MIT
URL:            https://github.com/millermatt/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
Requires:       ca-certificates openconnect wget      

%description
%{summary}.
Some sample scripts to run in shell.
See readme.md for proper usage.

%prep
%autosetup -n%{name}-%{commit0}

%build
# no

%install
mkdir -p %{buildroot}/%{_bindir}
cp -av connect.sh %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc readme.md
%doc Vagrantfile
%doc *.sh
%{_bindir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20170903git627468b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20170903git627468b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20170903git627468b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170903git627468b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20170903git627468b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170903git627468b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170903git627468b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Raphael Groner <raphgro@fedoraproject.org> - 0-0.2.20170903git627468b
- minor fixes for review

* Thu Mar 04 2021 Raphael Groner <raphgro@fedoraproject.org> - 0-0.1.20170903git627468b
- initial
