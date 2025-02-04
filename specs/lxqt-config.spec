Name:          lxqt-config
Summary:       Config tools for LXQt desktop suite
Version:       2.1.0
Release:       3%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(xcursor)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(KF6Screen)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: desktop-file-utils
BuildRequires: xorg-x11-drv-libinput-devel
BuildRequires: lxqt-menu-data
BuildRequires: perl

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-config
Requires:       lxqt-config
%description l10n
This package provides translations for the lxqt-config package.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
for cfgapp in monitor input file-associations appearance cursor brightness locale; do
if [ -f %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop ]; then
sed -i "/^GenericName.*/d" %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
sed -i "/^Comment.*/d" %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/lxqt-config-${cfgapp}.desktop
fi
done
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/lxqt-config.desktop


%find_lang lxqt-config --with-qt
%find_lang lxqt-config-appearance --with-qt
%find_lang lxqt-config-brightness --with-qt
%find_lang lxqt-config-cursor --with-qt
%find_lang lxqt-config-file-associations --with-qt
%find_lang lxqt-config-input --with-qt
%find_lang lxqt-config-locale --with-qt
%find_lang lxqt-config-monitor --with-qt

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/lxqt-config
%{_bindir}/lxqt-config-brightness
%{_bindir}/lxqt-config-appearance
%{_bindir}/lxqt-config-file-associations
%{_bindir}/lxqt-config-input
%{_bindir}/lxqt-config-monitor
%{_bindir}/lxqt-config-locale
%{_datadir}/applications/lxqt-config-appearance.desktop
%{_datadir}/applications/lxqt-config-file-associations.desktop
%{_datadir}/applications/lxqt-config-input.desktop
%{_datadir}/applications/lxqt-config-monitor.desktop
%{_datadir}/applications/lxqt-config-locale.desktop
%{_datadir}/applications/lxqt-config.desktop
%{_datadir}/applications/lxqt-config-brightness.desktop
%{_libdir}/lxqt-config/liblxqt-config-cursor.so
%{_datadir}/icons/*/*
%{_datadir}/lxqt/icons/*
%{_mandir}/man1/lxqt-config*

%files l10n -f lxqt-config.lang -f lxqt-config-appearance.lang -f lxqt-config-brightness.lang -f lxqt-config-cursor.lang -f lxqt-config-file-associations.lang -f lxqt-config-input.lang -f lxqt-config-locale.lang -f lxqt-config-monitor.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-config
%dir %{_datadir}/lxqt/translations/lxqt-config-appearance
%dir %{_datadir}/lxqt/translations/lxqt-config-brightness
%dir %{_datadir}/lxqt/translations/lxqt-config-cursor
%dir %{_datadir}/lxqt/translations/lxqt-config-file-associations
%dir %{_datadir}/lxqt/translations/lxqt-config-input
%dir %{_datadir}/lxqt/translations/lxqt-config-locale
%{_datadir}/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-brightness/lxqt-config-brightness_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-cursor/lxqt-config-cursor_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-file-associations/lxqt-config-file-associations_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-input/lxqt-config-input_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-input/lxqt-config-input_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-locale/lxqt-config-locale_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-locale/lxqt-config-locale_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-monitor/lxqt-config-monitor_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-monitor/lxqt-config-monitor_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-appearance/lxqt-config-appearance_ast.qm
%{_datadir}/lxqt/translations/lxqt-config/lxqt-config_arn.qm
%{_datadir}/lxqt/translations/lxqt-config/lxqt-config_ast.qm

%changelog
* Sun Feb 02 2025 Steve Cossette <farchord@gmail.com> - 2.1.0-3
- Rebuild for Qt incompatibility

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 2.1.0-1
- 2.1.0

* Thu Apr 18 2024 Steve Cossette <farchord@gmail.com> - 2.0.0-1
- 2.0.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Zamir SUN <sztsian@gmail.com> - 1.4.0-1
- Update version to 1.4.0

* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 1.3.0-1
- Update version to 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 2 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-3
- Pull upstream review pull request to build with libkscreen 5.26.90

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 1.2.0-1
- Update version to 1.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 1.1.0-1
- new version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 Zamir SUN <sztsian@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat Aug 07 2021 Zamir SUN <sztsian@gmail.com> - 0.17.1-1
- Update to 0.17.1

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.16.0-4
- Fix FTBFS
- Fixes RHBZ#1987690

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-8
- Fix FTBFS (cmake): https://github.com/lxde/lxqt/issues/1277

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-4
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- moved translations to lxqt-l10n

* Wed Jan 11 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- Doesn't build on epel7 with aarch64

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-2
- Fix rpmlint issues

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Mon Apr 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-6
- rebuild

* Mon Apr 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-5
- rebuild (kscreen2)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Remove razorqt conflicts

* Wed Dec 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt macro to enable epel 7

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-config as migrated to lxqt

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Proper add locale for Qt tm files

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Preparing for 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Rebuild against new Qt 5.4.0

* Sun Dec 21 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- Unify naming as discussed on Fedora IRC

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update on review https://bugzilla.redhat.com/show_bug.cgi?id=1159882

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Update to Fedora package review 

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
