Name:           candy-icon-theme
Summary:        Sweet gradient icon theme
License:        GPL-3.0-only

%global git_repo    candy-icons
%global git_url     https://github.com/EliverLara/%{git_repo}
%global git_commit  2cab33ee1e27dcee13e43621693db7dd2c5e63c8
%global git_date    20241128

%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:7})

Version:        0^%{git_date}.%{git_commit_short}
Release:        2%{?dist}

URL:            https://www.opendesktop.org/p/1305251/
Source0:        %{git_url}/archive/%{git_commit}/%{git_repo}-%{git_commit}.tar.gz

BuildArch:      noarch

Requires:       adwaita-icon-theme
Requires:       breeze-icon-theme
Requires:       hicolor-icon-theme

%description
Candy Icons is a simplistic, vector, gradient icon theme.


%prep
%autosetup -n %{git_repo}-%{git_commit}

# Use a prettier name for the theme
sed \
  -e 's|^Name=candy-icons$|Name=Candy Icons|' \
  -i index.theme


%build
# Nothing to do here


%install
CANDY_DIR="%{buildroot}%{_datadir}/icons/Candy"
install -m 755 -d "${CANDY_DIR}"
install -m 644 index.theme "${CANDY_DIR}/"

cp -a -t "${CANDY_DIR}/" \
  apps devices mimetypes places preferences status

touch "${CANDY_DIR}/icon-theme.cache"


%transfiletriggerin -- %{_datadir}/icons/Candy
gtk-update-icon-cache --force %{_datadir}/icons/Candy &>/dev/null || :


%files
%license LICENSE
%dir %{_datadir}/icons/Candy
%{_datadir}/icons/Candy/index.theme
%{_datadir}/icons/Candy/**/*
%ghost %{_datadir}/icons/Candy/icon-theme.cache


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20241128.2cab33e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 29 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20241128.2cab33e-1
- Update to latest git snapshot (2024-11-28)

* Sat Aug 31 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20240825.b92b133-1
- Update to latest git snapshot (2024-08-25)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20240507.f41d894-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 07 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20240507.f41d894-1
- Update to latest git snapshot (2024-05-07)

* Fri Feb 16 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20240215.788b6a5-1
- Update to latest git snapshot (2024-02-15)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231104.1b11884-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231104.1b11884-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 12 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20231104.1b11884-1
- Update to latest git snapshot (2023-11-04)

* Fri Sep 15 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20230904.1c5b81a-1
- Update to latest git snapshot (2023-09-04)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-37.20230412gita017160b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-36.20230412gita017160b
- Update to latest git snapshot (2023-04-12)

* Wed Mar 22 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-35.20230309git01255451
- Update to latest git snapshot (2023-03-09)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-34.20230107gitc27f6da2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-33.20230107gitc27f6da2
- Update to latest upstream snapshot
- Migrate License tag to SPDX

* Wed Sep 21 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-32.20220919gita14330c7
- Update to latest upstream snapshot

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-31.20220713git8bbfb04e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-30.20220713git8bbfb04e
- Update to latest upstream snapshot

* Sun Jun 12 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-29.20220611git45ab5293
- Update to latest upstream snapshot

* Mon Apr 25 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-28.20220423git8c4df109
- Update to latest upstream snapshot

* Mon Mar 07 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-27.20220228gitff09c1fd
- Update to latest upstream snapshot
- Include mimetype icons in the package

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20211226gitb1a79d8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-25.20211226gitb1a79d8e
- Update to latest upstream snapshot

* Mon Oct 18 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-24.20211003gitdfd05c13
- Update to latest upstream snapshot

* Sun Aug 01 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-23.20210725git98c17711
- Update to latest upstream snapshot

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.20210316git03abc12f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 17 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-21.20210316git03abc12f
- Update to latest upstream snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20201211git1bc770ee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-19.20201211git1bc770ee
- Update to latest upstream snapshot

* Tue Nov 03 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-18.20201031git4c80adb4
- Update to latest upstream snapshot

* Mon Sep 28 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-17.20200926gitb68fb3b6
- Update to latest upstream snapshot

* Fri Aug 07 2020 Artur Iwicki <fedora@svgames.pl> - 0-16.20200731git5df1fcdf
- Update to latest upstream snapshot

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20200704git8c144f59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Artur Iwicki <fedora@svgames.pl> - 0-14.20200704git8c144f59
- Update to latest upstream snapshot

* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0-13.20200620git4be1a05e
- Update to latest upstream snapshot

* Wed May 20 2020 Artur Iwicki <fedora@svgames.pl> - 0-12.20200514git9d5b05d0
- Update to latest upstream snapshot

* Fri Apr 24 2020 Artur Iwicki <fedora@svgames.pl> - 0-11.20200423git3fbc68f8
- Update to latest upstream snapshot
- Do not move the files around, stick to upstream directory hierarchy
- Add dependency on breeze-icon-theme

* Fri Apr 17 2020 Artur Iwicki <fedora@svgames.pl> - 0-10.20200403gita9a4cdf7
- Update to latest upstream snapshot

* Sun Mar 22 2020 Artur Iwicki <fedora@svgames.pl> - 0-9.20200312gitfc3fbcad
- Upate to latest upstream snapshot

* Fri Feb 21 2020 Artur Iwicki <fedora@svgames.pl> - 0-8.20200220gita6e938f8
- Update to latest upstream snapshot

* Sun Feb 02 2020 Artur Iwicki <fedora@svgames.pl> - 0-7.20200131git8f853b2e
- Update to latest upstream snapshot
- Fix symlinks not being preserved in packaging

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20200110git4e63197c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Artur Iwicki <fedora@svgames.pl> - 0-5.20200110git4e63197c
- Update to latest upstream snapshot

* Sat Dec 21 2019 Artur Iwicki <fedora@svgames.pl> - 0-4.20191220gitd8f73028
- Update to latest upstream snapshot

* Wed Dec 11 2019 Artur Iwicki <fedora@svgames.pl> - 0-3.20191210gitd68a12e8
- Update to latest upstream snapshot
- Preserve timestamps for icon files

* Sat Nov 30 2019 Artur Iwicki <fedora@svgames.pl> - 0-2.20191129gite14463b4
- Update to latest upstream snapshot
- Change "Requires:" to match "Inherits=" from index.theme

* Fri Nov 15 2019 Artur Iwicki <fedora@svgames.pl> - 0-1.20191113gita9f7014e
- Initial packaging
