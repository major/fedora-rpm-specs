Summary:        Simple TTY terminal I/O application
Name:           tio
Version:        3.8
Release:        2%{?dist}
License:        GPL-2.0-or-later
URL:            https://tio.github.io/
Source0:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.2
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  lua-devel >= 5.1

%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc AUTHORS NEWS README.md examples/*
%{_bindir}/%{name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Robert Scheck <robert@fedoraproject.org> 3.8-1
- Upgrade to 3.8 (#2329609)

* Fri Sep 06 2024 Robert Scheck <robert@fedoraproject.org> 3.7-1
- Upgrade to 3.7 (#2309659)

* Fri Jul 19 2024 Robert Scheck <robert@fedoraproject.org> 3.6-1
- Upgrade to 3.6 (#2298905)

* Fri Jul 05 2024 Robert Scheck <robert@fedoraproject.org> 3.5-1
- Upgrade to 3.5 (#2295740)

* Sun Jun 16 2024 Robert Scheck <robert@fedoraproject.org> 3.4-1
- Upgrade to 3.4 (#2292587)

* Fri May 17 2024 Robert Scheck <robert@fedoraproject.org> 3.3-1
- Upgrade to 3.3 (#2280941)

* Sun May 05 2024 Robert Scheck <robert@fedoraproject.org> 3.1-1
- Upgrade to 3.1 (#2277784)

* Wed May 01 2024 Robert Scheck <robert@fedoraproject.org> 3.0-1
- Upgrade to 3.0 (#2277784)

* Mon Apr 15 2024 Robert Scheck <robert@fedoraproject.org> 2.8-1
- Upgrade to 2.8 (#2275155)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 23 2023 Robert Scheck <robert@fedoraproject.org> 2.7-1
- Upgrade to 2.7 (#2240300)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 10 2023 Robert Scheck <robert@fedoraproject.org> 2.6-1
- Upgrade to 2.6 (#2213990)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Robert Scheck <robert@fedoraproject.org> 2.5-1
- Upgrade to 2.5 (#2154614)

* Sat Dec 03 2022 Robert Scheck <robert@fedoraproject.org> 2.4-1
- Upgrade to 2.4 (#2150475)

* Thu Nov 03 2022 Robert Scheck <robert@fedoraproject.org> 2.3-1
- Upgrade to 2.3 (#2139343)

* Wed Oct 19 2022 Robert Scheck <robert@fedoraproject.org> 2.2-1
- Upgrade to 2.2 (#2135930)

* Sun Oct 16 2022 Robert Scheck <robert@fedoraproject.org> 2.1-1
- Upgrade to 2.1 (#2135115)

* Tue Sep 13 2022 Robert Scheck <robert@fedoraproject.org> 2.0-1
- Upgrade to 2.0 (#2126235)

* Sun Jul 24 2022 Robert Scheck <robert@fedoraproject.org> 1.47-1
- Upgrade to 1.47 (#2108938)

* Wed Jul 20 2022 Robert Scheck <robert@fedoraproject.org> 1.46-1
- Upgrade to 1.46 (#2108938)

* Sun Jul 17 2022 Robert Scheck <robert@fedoraproject.org> 1.45-1
- Upgrade to 1.45 (#2106978)

* Fri Jul 15 2022 Robert Scheck <robert@fedoraproject.org> 1.44-1
- Upgrade to 1.44 (#2106978)

* Sun Jul 10 2022 Robert Scheck <robert@fedoraproject.org> 1.43-1
- Upgrade to 1.43 (#2105681)

* Tue Jul 05 2022 Robert Scheck <robert@fedoraproject.org> 1.42-1
- Upgrade to 1.42 (#2104164)

* Sat Jun 18 2022 Robert Scheck <robert@fedoraproject.org> 1.40-1
- Upgrade to 1.40 (#2098148)

* Sun Jun 12 2022 Robert Scheck <robert@fedoraproject.org> 1.39-1
- Upgrade to 1.39 (#2096097)

* Sat Jun 04 2022 Robert Scheck <robert@fedoraproject.org> 1.38-1
- Upgrade to 1.38 (#2092955)

* Thu Apr 14 2022 Robert Scheck <robert@fedoraproject.org> 1.37-1
- Upgrade to 1.37 (#2075385)

* Tue Mar 22 2022 Robert Scheck <robert@fedoraproject.org> 1.36-1
- Upgrade to 1.36 (#2066516)

* Sun Feb 20 2022 Robert Scheck <robert@fedoraproject.org> 1.35-1
- Upgrade to 1.35 (#2054902)

* Wed Feb 16 2022 Robert Scheck <robert@fedoraproject.org> 1.34-1
- Upgrade to 1.34 (#2054902)

* Sun Feb 13 2022 Robert Scheck <robert@fedoraproject.org> 1.33-1
- Upgrade to 1.33 (#2053967)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Robert Scheck <robert@fedoraproject.org> 1.32-1
- Upgrade to 1.32 (#1720889)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Robert Scheck <robert@fedoraproject.org> 1.27-1
- Upgrade to 1.27

* Mon Oct 16 2017 Robert Scheck <robert@fedoraproject.org> 1.25-1
- Upgrade to 1.25

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-2
- Changes to match with Fedora Packaging Guidelines (#1497549)

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-1
- Upgrade to 1.24
- Initial spec file for Fedora and Red Hat Enterprise Linux
