%global luv Lüv

Name: luv-icon-theme
Summary: Flat, but complex, icon theme
License: CC-BY-SA-4.0

%global git_date    20241024
%global git_commit  e6fd660605ec738437dfb441a1f8f5d0f84e54cf
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:7})

# Version number taken from 'debian/changelog' file
Version: 0.6.3.1^%{git_date}.%{git_commit_short}
Release: 2%{?dist}

URL: https://github.com/Nitrux/%{name}
Source0: %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildArch: noarch

Requires: hicolor-icon-theme
Suggests: luv-wallpapers


%description
%{luv} is the spiritual successor to Flattr, a flat but complex icon theme.


%package -n luv-wallpapers
Summary: Wallpapers to accompany the %{luv} icon theme
BuildArch: noarch

%global paper_count 6

%description -n luv-wallpapers
A set of %{paper_count} different wallpapers to use alongside the %{luv} icon theme.


%prep
%autosetup -n %{name}-%{git_commit}

# Remove extra permission bits found on some files
find Luv/ -executable -type f -exec chmod --verbose a-x '{}' ';'

# Remove "dummy" directories
for DUMMY in $(find Luv/ -name 'dummy.txt'); do
	DUMMY_DIR="$(dirname "${DUMMY}")"
	rm "${DUMMY}"

	# Not doing rm -rf on the dir so we don't remove anything by mistake
	rmdir "${DUMMY_DIR}"
done


%build
# Nothing to do here


%install
# -- icons
ICON_DIR="%{buildroot}%{_datadir}/icons"
install -m 755 -d "${ICON_DIR}"
cp -a Luv/ "${ICON_DIR}/"

rm "${ICON_DIR}/Luv/LICENSE"

# -- wallpapers
PAPER_DIR="%{buildroot}%{_datadir}/wallpapers"
install -m 755 -d "${PAPER_DIR}"
cp -a Wallpapers "${PAPER_DIR}/"
mv "${PAPER_DIR}/Wallpapers" "${PAPER_DIR}/Luv"


%check
PAPERS=$(find %{buildroot}%{_datadir}/wallpapers/Luv/ -mindepth 1 -maxdepth 1 -type d | wc -l)
if [[ "$PAPERS" -ne "%{paper_count}" ]]; then
	echo "Error: The luv-wallpapers package says there are %{paper_count} wallpapers, but ${PAPERS} were found" >&2
	exit 1
fi


%transfiletriggerin -- %{_datadir}/icons/Luv
gtk-update-icon-cache --force %{_datadir}/icons/Luv &>/dev/null || :


%files
%license Luv/LICENSE

%dir %{_datadir}/icons/Luv
%{_datadir}/icons/Luv/*/

%{_datadir}/icons/Luv/index.theme
%ghost %{_datadir}/icons/Luv/icon-theme.cache


%files -n luv-wallpapers
%license Luv/LICENSE
%{_datadir}/wallpapers/Luv


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3.1^20241024.e6fd660-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 29 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.3.1^20241024.e6fd660-1
- Update to latest git snapshot (2024-10-24)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1^20231224.cd15ec2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.1^20231224.cd15ec2-1
- Update to latest git snapshot (2023-12-24)
- Migrate License tag to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0^20230826.abffcdc-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0^20230826.abffcdc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.0^20230826.abffcdc-1
- Update to latest git snapshot (2023-08-26)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3.20220805git782a3009
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2.20220805git782a3009
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.6-1.20220805git782a3009
- Update to latest git snapshot (2022-08-05)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2.20220515git52c4573b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 12 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.2-1.20220515git52c4573b
- Update to latest git snapshot (2022-05-15)

* Mon Apr 25 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.2-1.20220411gitf7c9e810
- Update to latest git snapshot (2022-04-11)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.99-2.20211225git147c0833
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.9.99-1.20211225git147c0833
- Update to latest git snapshot (2021-12-25)

* Mon Oct 18 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.9.88-1.20210930git202eaa66
- Update to latest git snapshot (2021-09-30)

* Wed Sep 01 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.9.87-1.20210831gitb71714b1
- Update to latest git snapshot (2021-08-31)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.31-7.20210305git04d47f13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 06 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.9.31-6.20210305git04d47f13
- Update to latest git snapshot (2021-03-05)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.31-5.20200920gitc9fbcb0b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.9.31-4.20200920gitc9fbcb0b
- Update to latest git snapshot

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.31-3.20200623git42387fe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0.4.9.31-2.20200623git42387fe9
- Update to latest git snapshot
- Remove executable bits found on some files
- Don't install "dummy" directories
- Check if the actual wallpaper count matches what's in luv-wallpapers description

* Tue May 05 2020 Artur Iwicki <fedora@svgames.pl> - 0.4.9.31-1.20200504git6f0fb464
- Initial packaging
