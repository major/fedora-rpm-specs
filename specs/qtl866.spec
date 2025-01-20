%global commit 544d42c6f4f56e641f179ba24b638d017e5ab217
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           qtl866
Version:        0
Release:        0.20161050git%{shortcommit}%{?dist}
Summary:        GUI driver for the TL866 (MiniPRO) chip programmer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/wd5gnr/qtl866
Source0:        https://github.com/wd5gnr/qtl866/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

# https://github.com/wd5gnr/qtl866/pull/9
Patch0:         https://github.com/lkundrak/qtl866/commit/6eb0fd70.patch#/0001-Fix-build.patch
Patch1:         https://github.com/lkundrak/qtl866/commit/cdcdc2c9.patch#/0002-Fix-a-typo.patch
Patch2:         https://github.com/lkundrak/qtl866/commit/42d15fb1.patch#/0003-Load-qtparts-on-build.patch

# https://github.com/wd5gnr/qtl866/pull/8
Patch3:         https://github.com/lkundrak/qtl866/commit/9f7553d4.patch#/0004-Add-a-desktop-file-and-an-icon.patch
Patch4:         https://github.com/lkundrak/qtl866/commit/7b3f233b.patch#/0005-Add-AppStream-metadata.patch

# Not upstreamable
Patch5:         https://github.com/lkundrak/qtl866/commit/6a4fe197.patch#/0006-Use-my-clone-in-AppData-for-now.patch
Patch6:         https://github.com/lkundrak/qtl866/commit/006d5dfa.patch#/0007-Make-it-somehow-work-with-Wayland.patch

BuildRequires: make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git
Requires:       minipro
Requires:       bless

%description
GUI for a programming utility compatible with Minipro TL866CS and Minipro
TL866A chip programmers. Supports more than 13000 target devices
(including AVRs, PICs, various BIOSes and EEPROMs).


%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# The binary patch needs to be applied with git
git --git-dir=. apply --unsafe-paths --directory=. --apply %{PATCH4}
%patch -P5 -p1
%patch -P6 -p1


%build
%{_qt5_qmake}
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
install binhexedit %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -pm644 qtl866.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications qtl866.desktop
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm644 qtl866.appdata.xml %{buildroot}%{_datadir}/appdata/
make install INSTALL_ROOT=%{buildroot}


%check
appstream-util --nonet validate-relax %{buildroot}%{_datadir}/appdata/qtl866.appdata.xml


%files
%{_bindir}/qtl866
%{_bindir}/binhexedit
%{_datadir}/applications/qtl866.desktop
%{_datadir}/icons/hicolor
%{_datadir}/appdata/qtl866.appdata.xml
%doc README.md
%license COPYING


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161050git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.20161049git544d42c
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161048git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161047git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161046git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161045git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161044git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161043git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161042git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161041git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161040git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161039git544d42c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161038git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161037git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161036git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161035git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161034git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161033git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161032git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161031git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20161030git544d42c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 0-0.20161029git7bb1d95
- Initial packaging
