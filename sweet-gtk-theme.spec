Name: sweet-gtk-theme
Summary: Light and dark, colorful GTK+ theme
License: GPL-3.0-only
URL: https://www.gnome-look.org/p/1253385/

%global git_date_master 20230410
%global git_commit_master 670c20d034891ad026cba75253ae139e7c570093

%global git_date_ambar 20230410
%global git_commit_ambar d3a99c0fd5545575637085344349d66dd33c7138

%global git_date_ambar_blue 20230410
%global git_commit_ambar_blue 271a150e9fc78234205701295a307aeac4982748

%global git_date_mars 20230410
%global git_commit_mars 9a774a45cec35fcc928510be95e5368beb1b946c

%global git_date_nova 20230410
%global git_commit_nova e19223f9ccea49703bf2e60570b13d01918e4464

%global git_date %( \
	( \
		echo '%{git_date_master}'; \
		echo '%{git_date_ambar}'; \
		echo '%{git_date_ambar_blue}'; \
		echo '%{git_date_mars}'; \
		echo '%{git_date_nova}'; \
	) | sort -rn | head -n1)

Version: 3.0
Release: 10.%{git_date}%{?dist}

%global repo_name  Sweet
%global repo_url   https://github.com/EliverLara/%{repo_name}

Source0: %{repo_url}/archive/%{git_commit_master}/%{repo_name}-Master-%{git_commit_master}.tar.gz
Source1: %{repo_url}/archive/%{git_commit_ambar}/%{repo_name}-Ambar-%{git_commit_ambar}.tar.gz
Source2: %{repo_url}/archive/%{git_commit_ambar_blue}/%{repo_name}-Ambar-Blue-%{git_commit_ambar_blue}.tar.gz
Source3: %{repo_url}/archive/%{git_commit_mars}/%{repo_name}-Mars-%{git_commit_mars}.tar.gz
Source4: %{repo_url}/archive/%{git_commit_nova}/%{repo_name}-Nova-%{git_commit_nova}.tar.gz
Source99: get-sweet-sources.sh

BuildArch: noarch

BuildRequires: sassc

Recommends: candy-icon-theme


%description
Sweet is a light and dark, colorful GTK+ theme that can be used with
Gnome Shell, Cinnamon, Metacity, xfwm4, and other window managers.

Sweet works great when used together with the Candy icon theme.


%prep
%setup -q -c %{repo_name}-%{version} -T -a 0
%setup -q -c %{repo_name}-%{version} -T -D -a 1
%setup -q -c %{repo_name}-%{version} -T -D -a 2
%setup -q -c %{repo_name}-%{version} -T -D -a 3
%setup -q -c %{repo_name}-%{version} -T -D -a 4

# Rename the directories from "repo-commit" to "branch"
mv "%{repo_name}-%{git_commit_master}" master
mv "%{repo_name}-%{git_commit_ambar}" ambar
mv "%{repo_name}-%{git_commit_ambar_blue}" ambar-blue
mv "%{repo_name}-%{git_commit_mars}" mars
mv "%{repo_name}-%{git_commit_nova}" nova

# Remove executable bits from everything that's not a shell/python script
find ./ -type f -executable \
	'!' '(' -name '*.sh' -o -name '*.fish' -o -name '*.py' ')' \
	-exec chmod --verbose a-x '{}' '+'


%build
# Upstream uses Gulp for building, but it is not available in Fedora.
# The Gulpfile takes care of compiling SASS files, but not much else.
# ...so let's just do that ourselves!
for VARIANT in master ambar ambar-blue mars nova; do
	pushd "${VARIANT}"
	for FILE in \
		gtk-4.0/gtk gtk-4.0/gtk-dark \
		gtk-3.0/gtk gtk-3.0/gtk-dark \
		gnome-shell/gnome-shell \
		cinnamon/cinnamon cinnamon/cinnamon-dark \
	; do
		SCSS_DIR="$(dirname "${FILE}")"
		SCSS_SOURCE="$(basename "${FILE}").scss"
		SCSS_TARGET="${SCSS_SOURCE/scss/css}"

		pushd "${SCSS_DIR}"
		sassc --style=compressed "${SCSS_SOURCE}" "${SCSS_TARGET}"
		popd
	done
	popd
done


%install
for VARIANT in master ambar ambar-blue mars nova; do
	THEME_DIR="%{buildroot}%{_datadir}/themes/Sweet-${VARIANT}"
	install -m 755 -d "${THEME_DIR}"

	pushd "${VARIANT}"
	for FILE in assets cinnamon gnome-shell gtk-2.0 gtk-3.0 gtk-4.0 metacity-1 xfwm4 index.theme; do
		cp -a "${FILE}" "${THEME_DIR}/${FILE}"
	done
	popd

	# Remove all SCSS source files
	# and any executable files that we might have installed by accident
	pushd "${THEME_DIR}"
	find ./ -name '*.scss' -exec rm --verbose '{}' '+'
	find ./ -type f -executable -exec rm --verbose '{}' '+'
	popd
done

# Rename "master" to "classic"
mv "%{buildroot}%{_datadir}/themes/Sweet-master" "%{buildroot}%{_datadir}/themes/Sweet-classic"


%files
%license master/LICENSE
%{_datadir}/themes/Sweet-classic
%{_datadir}/themes/Sweet-ambar
%{_datadir}/themes/Sweet-ambar-blue
%{_datadir}/themes/Sweet-mars
%{_datadir}/themes/Sweet-nova


%changelog
* Wed Apr 19 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0-10.20230410
- Update to latest git snapshots

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9.20230107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0-8.20230107
- Update to latest git snapshots
- Migrate License tag to SPDX

* Wed Sep 21 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0-7.20220915
- Update to latest git snapshots

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6.20220607
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 12 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0-5.20220607
- Update to latest git snapshots

* Mon Apr 25 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0-4.20220423
- Update to latest git snapshots

* Mon Feb 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0-3.20220212
- Update to latest git snapshots
- Build and install GTK4 theme

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2.20211121
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0-1.20211121
- Update to v3.0

* Mon Oct 18 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0-5.20211015
- Update to latest git snapshots

* Sun Aug 01 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0-4.20210728
- Update to latest git snapshots

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3.20210602
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0-2.20210602
- Update to latest git snapshots
- Fix source URLs

* Mon Apr 05 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0-1.20210402
- Update to v2.0
- Include color variants

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-5.20201025gita1641414
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.5-4.20201025gita1641414
- Update to latest git snapshot

* Mon Oct 12 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.5-3.20201004gite3ee1783
- Update to latest git snapshot (now with support for Cinnamon)

* Sat Sep 19 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.5-2.20200913git10aefff0
- Update to latest git snapshot
- Do not re-render the assets during build
- Remove SCSS sources from the final install

* Sun Dec 01 2019 Artur Iwicki <fedora@svgames.pl> - 1.10.5-1.20191118gitb8e8b7d7
- Initial packaging
