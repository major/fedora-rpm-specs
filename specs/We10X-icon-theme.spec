Name:    We10X-icon-theme
Summary: Colorful icon theme inspired by Microsoft Windows 10 aesthetic
License: GPL-3.0-only

%global git_date    20230413
%global git_commit  4c244fcd7302bc62e4a74a7f7300f0ed2293772f
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:8})

Version: 0
Release: 33.%{git_date}git%{git_commit_short}%{?dist}

URL: https://github.com/yeyushengfan258/%{name}
Source0: %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildArch: noarch

Requires: hicolor-icon-theme

%description
We10X is a colorful icon theme inspired
by the aesthetic of Microsoft Windows 10.

Comes in a regular and dark variant.


%prep
%autosetup -n %{name}-%{git_commit}

# Remove spurious executable bits found on some files
chmod 644 ./AUTHORS ./COPYING
find links/ src/ -executable -type f -exec chmod -v -- a-x '{}' '+'

# Remove broken links
find links/ -follow -type l -printf 'deleted broken symlink "%p" -> "%l"\n' -delete

# Remove empty directories
for FILE in $(find ./ -name '.directory'); do
	DIR="$(dirname "${FILE}")"
	rm "${FILE}"
	rmdir "${DIR}" || true
done

# Do not call gtk-update-icon-cache during install
sed  \
	-e '/gtk-update-icon-cache/d'  \
	-i install.sh


%build
# Nothing to do here


%install
install -m 755 -d '%{buildroot}%{_datadir}/icons'
./install.sh --dest '%{buildroot}%{_datadir}/icons'

for VARIANT in '' '-dark'; do
	THEME="%{buildroot}%{_datadir}/icons/We10X${VARIANT}"
	touch "${THEME}/icon-theme.cache"

	rm "${THEME}/AUTHORS"
	rm "${THEME}/COPYING"
done


%transfiletriggerin -- %{_datadir}/icons/We10X
gtk-update-icon-cache --force %{_datadir}/icons/We10X &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/We10X-dark
gtk-update-icon-cache --force %{_datadir}/icons/We10X-dark &>/dev/null || :


%files
%doc AUTHORS
%license COPYING

# -- normal variant

%dir %{_datadir}/icons/We10X
%ghost %{_datadir}/icons/We10X/icon-theme.cache
%{_datadir}/icons/We10X/index.theme

%{_datadir}/icons/We10X/actions
%{_datadir}/icons/We10X/actions@2x
%{_datadir}/icons/We10X/animations
%{_datadir}/icons/We10X/animations@2x
%{_datadir}/icons/We10X/apps
%{_datadir}/icons/We10X/apps@2x
%{_datadir}/icons/We10X/categories
%{_datadir}/icons/We10X/categories@2x
%{_datadir}/icons/We10X/devices
%{_datadir}/icons/We10X/devices@2x
%{_datadir}/icons/We10X/emblems
%{_datadir}/icons/We10X/emblems@2x
%{_datadir}/icons/We10X/mimes
%{_datadir}/icons/We10X/mimes@2x
%{_datadir}/icons/We10X/places
%{_datadir}/icons/We10X/places@2x
%{_datadir}/icons/We10X/status
%{_datadir}/icons/We10X/status@2x

# -- dark variant

%dir %{_datadir}/icons/We10X-dark
%ghost %{_datadir}/icons/We10X-dark/icon-theme.cache
%{_datadir}/icons/We10X-dark/index.theme

%{_datadir}/icons/We10X-dark/actions
%{_datadir}/icons/We10X-dark/actions@2x
%{_datadir}/icons/We10X-dark/animations
%{_datadir}/icons/We10X-dark/animations@2x
%{_datadir}/icons/We10X-dark/apps
%{_datadir}/icons/We10X-dark/apps@2x
%{_datadir}/icons/We10X-dark/categories
%{_datadir}/icons/We10X-dark/categories@2x
%{_datadir}/icons/We10X-dark/devices
%{_datadir}/icons/We10X-dark/devices@2x
%{_datadir}/icons/We10X-dark/emblems
%{_datadir}/icons/We10X-dark/emblems@2x
%{_datadir}/icons/We10X-dark/mimes
%{_datadir}/icons/We10X-dark/mimes@2x
%{_datadir}/icons/We10X-dark/places
%{_datadir}/icons/We10X-dark/places@2x
%{_datadir}/icons/We10X-dark/status
%{_datadir}/icons/We10X-dark/status@2x


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-33.20230413git4c244fcd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-32.20230413git4c244fcd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-31.20230413git4c244fcd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-30.20230413git4c244fcd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-29.20230413git4c244fcd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-28.20230413git4c244fcd
- Update to latest git snapshot (2023-04-13)
- Convert License tag to SPDX

* Mon Mar 13 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-27.20230309git12934034
- Update to latest git snapshot (2023-03-09)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20220917git3ffc38fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-25.20220917git3ffc38fe
- Update to latest git snapshot (2022-09-17)

* Sun Jul 24 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-24.20220721gite891e9b8
- Update to latest git snapshot (2022-07-21)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20220606gitefde529d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 12 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-22.20220606gitefde529d
- Update to latest git snapshot (2022-06-06)

* Mon Apr 25 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-21.20220424git99befee5
- Update to latest git snapshot (2022-04-24)

* Mon Feb 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-20.20220210gitbd21e213
- Update to latest git snapshot (2022-02-10)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20211227gitbd21e213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-18.20211227gitebd21e21
- Update to latest git snapshot (2021-12-27)

* Mon Oct 18 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-17.20211016gite23d4d82
- Update to latest upstream git snapshot

* Mon Aug 30 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-16.20210827gitea2dfa5e
- Update to latest upstream git snapshot

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20210617git8738028b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 20 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-14.20210617git8738028b
- Update to latest upstream git snapshot

* Fri Apr 09 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-13.20210409git89d8aa7b
- Update to latest upstream git snapshot
- Fix paths in package trigger scripts

* Wed Mar 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-12.20210302gitbd2c6848
- Update to latest upstream git snapshot

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20201226git75b5af72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-10.20201226git75b5af72
- Update to latest upstream git snapshot

* Fri Nov 20 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-9.20201119git001360fa
- Update to latest upstream git snapshot

* Thu Oct 22 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-8.20201021gitf6b397a2
- Update to latest upstream git snapshot

* Thu Sep 24 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-7.20200922git9ab1efdd
- Update to latest upstream git snapshot

* Thu Sep 10 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-6.20200910git9ba7a59b
- Update to latest upstream git snapshot

* Fri Aug 28 2020 Artur Iwicki <fedora@svgames.pl> - 0-5.20200824git3391e427
- Update to latest upstream snapshot
- Don't edit install.sh to preserve file timestamps (fixed upstream)

* Thu Aug 20 2020 Artur Iwicki <fedora@svgames.pl> - 0-4.20200818git3010fa4a
- Update to latest upstream git snapshot
- Remove broken symlinks before install
- Remove empty directories before install

* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0-3.20200621gitdd69e31a
- Update to latest upstream git snapshot

* Sun May 24 2020 Artur Iwicki <fedora@svgames.pl> - 0-2.20200522git1e951299
- Update to latest upstream git snapshot

* Tue May 05 2020 Artur Iwicki <fedora@svgames.pl> - 0-1.20200504git4b95b047
- Initial packaging
