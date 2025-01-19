Name:           mint-y-icons
Version:        1.8.0
Release:        2%{?dist}
Summary:        The Mint-Y icon theme

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  fdupes

Requires:       filesystem
Requires:       mint-x-icons
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup


%build

%install
%{__cp} -pr ${PWD}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}


%transfiletriggerin -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%transfiletriggerpostun -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%files
%license debian/copyright
%doc debian/changelog
%doc README.md
%{_datadir}/icons/Mint-*/
%{_datadir}/folder-color-switcher/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 Leigh Scott <leigh123linux@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Fri Dec 06 2024 Leigh Scott <leigh123linux@gmail.com> - 1.7.9-1
- Update to 1.7.9

* Tue Nov 26 2024 Leigh Scott <leigh123linux@gmail.com> - 1.7.8-1
- Update to 1.7.8

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.7-2
- convert license to SPDX

* Sat Jul 20 2024 Leigh Scott <leigh123linux@gmail.com> - 1.7.7-1
- Update to 1.7.7

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Leigh Scott <leigh123linux@gmail.com> - 1.7.6-1
- Update to 1.7.6

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 1.7.5-1
- Update to 1.7.5

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Leigh Scott <leigh123linux@gmail.com> - 1.7.2-1
- New upstream release

* Thu Dec 21 2023 Leigh Scott <leigh123linux@gmail.com> - 1.7.1-1
- New upstream release

* Thu Nov 30 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6.9-1
- New upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 09 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6.7-1
- New upstream release

* Mon Jun 05 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6.6-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Leigh Scott <leigh123linux@gmail.com> - 1.6.5-1
- New upstream release

* Tue Nov 22 2022 Leigh Scott <leigh123linux@gmail.com> - 1.6.2-1
- New upstream release

* Sun Aug 21 2022 Leigh Scott <leigh123linux@gmail.com> - 1.6.1-1
- New upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Leigh Scott <leigh123linux@gmail.com> - 1.6.0-1
- New upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.9-1
- New upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.8-1
- New upstream release

* Fri Jun 11 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.3-1
- New upstream release

* Thu Jun 10 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.2-1
- New upstream release

* Fri Jun 04 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.1-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.0-1
- New upstream release

* Sat Jan  2 2021 Leigh Scott <leigh123linux@gmail.com> - 1.4.9-1
- New upstream release

* Tue Dec 29 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.8-1
- New upstream release

* Tue Dec  8 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.6-1
- New upstream release

* Thu Dec  3 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.5-1
- New upstream release

* Thu Dec  3 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.4-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.3-1
- New upstream release

* Sat Jun 06 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.2-1
- New upstream release

* Sun May 24 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.1-1
- New upstream release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.0-1
- New upstream release

* Tue Apr 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.3.8-1
- New upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.7-1
- New upstream release

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.6-1
- New upstream release

* Sun Nov 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.5-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.4-1
- New upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.3-1
- New upstream release

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- New upstream release

* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.6-1
- New upstream release

* Thu Jun 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.5-1
- New upstream release

* Sat Jun 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.3-1
- New upstream release

* Tue May 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- New upstream release

* Mon May 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- New upstream release

* Mon May 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.9-1
- New upstream release

* Sun May 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.5-1
- New upstream release

* Fri Apr 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-1
- New upstream release

* Mon Apr 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-0.2.20180321git415a843
- Update to git snapshot

* Sat Feb 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-0.1.20180224git9204077
- Update to git snapshot (adds hidpi icons)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Björn Esser <besser82@fedoraproject.org> - 1.1.3-2
- Use rpm filetriggers on Fedora and/or RHEL >= 8

* Fri Nov 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-1
- New upstream release

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-3
- Fix dir descriptions in index.theme

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-2
- Backported new action and app icons from upstream

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-1
- New upstream release (rhbz#1515227)

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-2
- Add explicit Requires on {gnome,hicolor}-icon-theme
- Simplify scriptlets

* Wed Nov 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-1
- New upstream release (rhbz#1512346)

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.9-1
- New upstream release (rhbz#1509754)

* Fri Sep 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-6
- Add eye-candy for online-accounts

* Sun Aug 27 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-5
- Adjustments for building on EPEL

* Sun Aug 27 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-4
- Create symlinks for modem-manager-gui

* Fri Aug 25 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-3
- Create symlinks for tilix

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-1
- New upstream release (rhbz#1463454)

* Wed May 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.7-1
- New upstream release (rhbz#1450541)

* Mon May 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.5-1
- New upstream release (rhbz#1448743)

* Sat Apr 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-6
- Create symlinks for additional apps with script in sources

* Sat Apr 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-5
- Add icons for lightdm-settings

* Sun Feb 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-4
- Fix License GPLv3+  --->  CC-BY-SA

* Sun Feb 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-3
- Symlink files to save disk-space

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-2
- Add icons for dnfdragora

* Mon Jan 09 2017 Björn Esser <bjoern.esser@gmail.com> - 1.0.4-1
- Initial rpm-release (rhbz#1411153)

* Sun Jan 08 2017 Björn Esser <bjoern.esser@gmail.com> - 1.0.4-0.1
- Initial package (rhbz#1411153)
