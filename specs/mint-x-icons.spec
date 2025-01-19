%bcond_without  nm_icons


Name:           mint-x-icons
Version:        1.7.2
Release:        2%{?dist}
Summary:        Icon theme for Linux Mint

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://linuxmint.com
Source0:        http://packages.linuxmint.com/pool/main/m/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  fdupes

Requires:       filesystem
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -c


%build
%if %{with nm_icons}
# Remove icons for nm-applet, because they are ugly.
%{_bindir}/find %{name}%{_prefix} -name "nm-*" -type f -delete
%{_bindir}/find %{name}%{_prefix} -name "nm-*" -xtype l			\
  -exec %{_bindir}/unlink {} \;
%{_bindir}/find %{name}%{_prefix} -name 'gnome-netstatus*' -xtype l	\
  -exec %{__file} {} \; | %{__grep} 'broken' |			\
  %{__sed} -e 's!:[ \t]\+.*$!!g' |				\
  %{_bindir}/xargs --max-args=1 %{_bindir}/unlink
%endif


%install
%{__cp} -pr %{name}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}


%transfiletriggerin -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%transfiletriggerpostun -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%files
%license %{name}/debian/copyright
%doc %{name}/debian/changelog
%{_datadir}/icons/Mint-X*
%{_datadir}/folder-color-switcher/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Leigh Scott <leigh123linux@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.1-2
- convert license to SPDX

* Sat Jul 20 2024 Leigh Scott <leigh123linux@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Leigh Scott <leigh123linux@gmail.com> - 1.6.9-1
- Update to 1.6.9

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 1.6.8-1
- Update to 1.6.8

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Leigh Scott <leigh123linux@gmail.com> - 1.6.5-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Leigh Scott <leigh123linux@gmail.com> - 1.6.4-1
- New upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Leigh Scott <leigh123linux@gmail.com> - 1.6.3-1
- New upstream release

* Thu Jun 10 2021 Leigh Scott <leigh123linux@gmail.com> - 1.6.1-1
- New upstream release

* Fri Jun 04 2021 Leigh Scott <leigh123linux@gmail.com> - 1.6.0-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 Leigh Scott <leigh123linux@gmail.com> - 1.5.9-1
- New upstream release

* Tue Dec 29 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.8-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.5.5-1
- New upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.5.3-1
- New upstream release

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.5.2-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.5.1-1
- New upstream release

* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.9-1
- New upstream release

* Mon May 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.8-1
- New upstream release

* Fri Apr 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.7-1
- New upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Björn Esser <besser82@fedoraproject.org> - 1.4.6-5
- Use rpm filetriggers on Fedora and/or RHEL >= 8

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-4
- Re-add the NetworkManager related icons

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-3
- Just delete the ones related to NetworkManager

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-2
- Fix dangling-relative-symlinks

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.6-1
- New upstream release (rhbz#1515233)

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.5-2
- Simplify scriptlets

* Wed Nov 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.5-1
- New upstream release (rhbz#1512345)

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.4-1
- New upstream release (rhbz#1509753)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.3-1
- New upstream release (rhbz#1460844)

* Sun May 14 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.4.2-4
- Remove NetworkManager related icons symlinks

* Fri May 12 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.2-3
- Fully remove all NetworkManager related icons
- Add needed Requires: {gnome,hicolor}-icon-theme

* Thu May 11 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.2-2
- Remove icons for nm-applet, because they are ugly

* Mon May 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.2-1
- New upstream release (rhbz#1448742)

* Wed Mar 22 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.1-1
- New upstream release (rhbz#1434631)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.0-2
- Symlink files to save disk-space

* Mon Jan 09 2017 Björn Esser <bjoern.esser@gmail.com> - 1.4.0-1
- Initial rpm-release (rhbz#1411152)

* Sun Jan 08 2017 Björn Esser <bjoern.esser@gmail.com> - 1.4.0-0.1
- Initial package (rhbz#1411152)
