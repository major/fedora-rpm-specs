%global giturl  https://github.com/snwh/%{name}

Name:           paper-icon-theme
Version:        1.5.0
Release:        11%{?dist}
Summary:        Modern freedesktop icon theme

License:        CC-BY-SA
URL:            https://snwh.org/paper
Source0:        %{giturl}/archive/v.%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  xmlstarlet

Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
Paper is a modern freedesktop icon theme whose design is based around
the use of bold colors and simple geometric shapes to compose icons.
Each icon has been meticulously designed for pixel-perfect viewing.

While it does take some inspiration from the icons in Google's
Material Design, some aspects have been adjusted to better suit a
desktop environment.


%prep
%autosetup -n %{name}-v.%{version}

# remove stray executable bit from files
find -executable -type f -exec chmod -x {} +

# Find files that use 'osb:' attributes but do not have the 'xmlns:osb' namespace defined and fix them.
for FILE in $(grep --include '*.svg' --recursive --files-with-matches -e 'osb:' ./ --null | xargs --null grep -e 'xmlns:osb' --files-without-match); do
       TEMPNAME="$(mktemp --tmpdir paper.XXXXXXXX)"
       xmlstarlet ed \
               -N svg='http://www.w3.org/2000/svg' \
               --insert '/svg:svg' \
               --type attr \
               -n 'xmlns:osb' \
               -v 'http://www.openswatchbook.org/uri/2009/osb' \
               < "${FILE}" > "${TEMPNAME}" 2>/dev/null
       mv "${TEMPNAME}" "${FILE}"
done


%build
%meson
%meson_build


%install
%meson_install

touch %{buildroot}/%{_datadir}/icons/Paper/icon-theme.cache
touch %{buildroot}/%{_datadir}/icons/Paper-Mono-Dark/icon-theme.cache


%transfiletriggerin -- %{_datadir}/icons/Paper %{_datadir}/icons/Paper-Mono-Dark
gtk-update-icon-cache --force %{_datadir}/icons/Paper &>/dev/null || :
gtk-update-icon-cache --force %{_datadir}/icons/Paper-Mono-Dark &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Paper %{_datadir}/icons/Paper-Mono-Dark
gtk-update-icon-cache --force %{_datadir}/icons/Paper &>/dev/null || :
gtk-update-icon-cache --force %{_datadir}/icons/Paper-Mono-Dark &>/dev/null || :


%files
%license COPYING LICENSE
%doc AUTHORS README.md

%{_datadir}/icons/Paper/index.theme
%{_datadir}/icons/Paper/cursor.theme
%{_datadir}/icons/Paper/*/

%{_datadir}/icons/Paper-Mono-Dark/index.theme
%{_datadir}/icons/Paper-Mono-Dark/*/

%ghost %{_datadir}/icons/Paper/icon-theme.cache
%ghost %{_datadir}/icons/Paper-Mono-Dark/icon-theme.cache


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Artur Iwicki <fedora@svgames.pl> - 1.5.0-7
- Fix some SVG icons containing invalid XML markup

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-3
- Disable deduplication to fix problems with flatpak apps.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.0-1
- Update to version 1.5.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Björn Esser <besser82@fedoraproject.org> - 1.4.0-2
- Use rpm filetriggers on Fedora and/or RHEL >= 8

* Sun Dec 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.0-1
- Initial import (#1529758)

* Sun Dec 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.0-0.3
- Add some git-format-patches from upstream

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.0-0.2
- Fix file permissions
- Fix spelling in %%description

* Fri Dec 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.0-0.1
- Initial rpm release (#1529758)

