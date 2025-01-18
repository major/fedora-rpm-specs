Name:           vaultwarden-web
Version:        2024.6.2c
Release:        1%{?dist}
Summary:        Web vault for vaultwarden

License:        GPL-3.0-only AND MIT AND BSD-3-Clause AND (MIT OR GPL-3.0-only)
URL:            https://github.com/dani-garcia/bw_web_builds
Source0:        %{url}/releases/download/v%{version}/bw_web_v%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch

# these are all included static js libs
Provides:       bundled(npm(buffer)) = 6.0.3
Provides:       bundled(npm(jszip)) = 3.10.1
Provides:       bundled(npm(papaparse)) = 5.4.1
Provides:       bundled(npm(lunr)) = 2.3.9
Provides:       bundled(npm(bootstrap) = 4.6.0
Provides:       bundled(npm(jquery)) = 3.7.1
Provides:       bundled(npm(ieee754))
Provides:       bundled(npm(popper.js)) = 1.16.1
Provides:       bundled(npm(qrious)) = 4.0.2


%description
%{summary}.


%prep
%autosetup -n web-vault


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/
cp -ra * %{buildroot}/%{_datadir}/%{name}
install -pm644 %{SOURCE1} %{_builddir}/web-vault/


%check
# nothing to do


%files
%license LICENSE.txt
%license *.js.LICENSE.txt
%license app/*.js.LICENSE.txt
%license scripts/*.js.LICENSE.txt
%{_datadir}/%{name}/


%changelog
* Thu Jan 16 2025 Jonathan Wright <jonathan@almalinux.org> - 2024.6.2c-1
- update to 2024.6.2c

* Sun Aug 11 2024 Jonathan Wright <jonathan@almalinux.org> - 2024.6.2b-1
- update to 2024.6.2b rhbz#2303667

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Jonathan Wright <jonathan@almalinux.org> - 2024.5.1-1
- update to 2024.5.1 rhbz#2295182

* Tue May 21 2024 Jonathan Wright <jonathan@almalinux.org> - 2024.5.0-1
- initial package build rhbz#2282767
