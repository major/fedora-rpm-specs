Summary:        Tools collection to control LXI enabled instruments
Name:           lxi-tools
Version:        2.1
Release:        2%{?dist}
License:        BSD
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1.gpg
Patch0:         https://github.com/lxi-tools/lxi-tools/commit/d55f9393388aff4b0c63b20f668c451e6c998465.patch#/lxi-tools-2.1-readline.patch
Patch1:         https://github.com/lxi-tools/lxi-tools/commit/8319ca0f9af088acd4f7a784a37e31c99aeb47bd.patch#/lxi-tools-2.1-lua.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.2
BuildRequires:  readline-devel
BuildRequires:  liblxi-devel >= 1.13
BuildRequires:  lua-devel >= 5.1
BuildRequires:  bash-completion
%if 0%{?gui}
BuildRequires:  glib2-devel >= 2.70
BuildRequires:  gtk4-devel >= 4.5.0
BuildRequires:  gtksourceview5-devel >= 5.3.3
BuildRequires:  libadwaita-devel >= 1.0.1
BuildRequires:  %{_bindir}/desktop-file-validate
BuildRequires:  %{_bindir}/appstream-util
%endif

%description
LXI tools are a collection of open source software tools for GNU/Linux
systems that enable control of LXI enabled instruments such as modern
oscilloscopes, power supplies, spectrum analyzers etc.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch0 -p1 -b .readline
%patch1 -p1 -b .lua

%build
%meson %{?gui:-Dgui=true}
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/lxi
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/lxi*
%{_mandir}/man1/lxi.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Robert Scheck <robert@fedoraproject.org> 2.1-1
- Upgrade to 2.1 (#2049045)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Robert Scheck <robert@fedoraproject.org> 1.21-1
- Upgrade to 1.21

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20-4
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Robert Scheck <robert@fedoraproject.org> 1.20-1
- Upgrade to 1.20

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Robert Scheck <robert@fedoraproject.org> 1.12-1
- Upgrade to 1.12

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.5-1
- Upgrade to 1.5

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.4-1
- Upgrade to 1.4

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.3-1
- Upgrade to 1.3

* Sun Oct 08 2017 Robert Scheck <robert@fedoraproject.org> 1.1-1
- Upgrade to 1.1
- Initial spec file for Fedora and Red Hat Enterprise Linux
