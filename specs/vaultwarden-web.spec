Name:           vaultwarden-web
Version:        2026.4.1
Release:        1%{?dist}
Summary:        Web vault for vaultwarden

License:        GPL-3.0-only AND MIT AND BSD-3-Clause AND (MIT OR GPL-3.0-only)
URL:            https://github.com/dani-garcia/bw_web_builds
Source0:        %{url}/releases/download/v%{version}/bw_web_v%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch

# these are all included static js libs
Provides:       bundled(npm(@bitwarden/sdk-internal)) = 0.2.0~main.622
Provides:       bundled(npm(angular)) = 20.3.18
Provides:       bundled(npm(base64-js)) = 1.5.1
Provides:       bundled(npm(big-integer)) = 1.6.52
Provides:       bundled(npm(buffer)) = 6.0.3
Provides:       bundled(npm(core-js)) = 3.48.0
Provides:       bundled(npm(crypto-js)) = 4.2.0
Provides:       bundled(npm(ieee754)) = 1.2.1
Provides:       bundled(npm(jszip)) = 3.10.1
Provides:       bundled(npm(lunr)) = 2.3.9
Provides:       bundled(npm(node-forge)) = 1.3.2
Provides:       bundled(npm(pako)) = 1.0.11
Provides:       bundled(npm(papaparse)) = 5.5.3
Provides:       bundled(npm(qrious)) = 4.0.2
Provides:       bundled(npm(zone.js)) = 0.15.1


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
%license app/*.js.LICENSE.txt
%license scripts/*.js.LICENSE.txt
%{_datadir}/%{name}/


%changelog
* Wed Jun 03 2026 Jonathan Wright <jonathan@almalinux.org> - 2026.4.1-1
- update to 2026.4.1 rhbz#2387335
- Fixes CVE-2026-27803 Unauthorized collection management operations due to improper access control
- Fixes CVE-2026-27801 Two-factor authentication bypass allows unauthorized access and data deletion
- Fixes CVE-2026-27802 Privilege Escalation via Unauthorized Bulk Permission Update
- Fixes CVE-2026-27898 Information disclosure via API partial update

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2025.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Jul 29 2025 Jonathan Wright <jonathan@almalinux.org> - 2025.7.0-1
- update to 2025.7.0 rhbz#2357235

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2025.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 30 2025 Jonathan Wright <jonathan@almalinux.org> - 2025.1.1-1
- update to 2025.1.1 rhbz#2334734

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
