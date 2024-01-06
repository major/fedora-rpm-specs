%define __cmake_in_source_build 1

Name:    lxqt-admin
Summary: LXQt system administration tool
Version: 1.4.0
Release: 1%{?dist}
License: LGPLv2+
URL:     https://lxqt-project.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  pkgconfig(lxqt) >= 1.1.0
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(glib-2.0)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

Requires:       polkit

%description
This package provides tools to adjust settings of the operating system
LXQt is running on. Both can be launched from GUI "Configuration Center".

GUI "Time and date configuration", binary lxqt-admin-time, can be used
to adjust the system time of the operating system as well as the timezone.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-admin
Requires:       lxqt-admin
%description l10n
This package provides translations for the lxqt-admin package.

%prep
%autosetup -p1 

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

%{cmake_lxqt} -DUSE_QT5=TRUE -DPULL_TRANSLATIONS=NO ..
make %{?_smp_mflags} -C %{_vpath_builddir}

%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_vpath_builddir}

for admfile in user time; do
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}-${admfile}.desktop

%find_lang lxqt-admin-${admfile} --with-qt
done

%files 
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/polkit-1/actions/*.policy

%files l10n -f lxqt-admin-user.lang -f lxqt-admin-time.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/lxqt-admin-user
%dir %{_datadir}/lxqt/translations/lxqt-admin-time
%{_datadir}/lxqt/translations/lxqt-admin-user/lxqt-admin-user_arn.qm
%{_datadir}/lxqt/translations/lxqt-admin-user/lxqt-admin-user_ast.qm
%{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_arn.qm
%{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_ast.qm

%changelog
* Sun Dec 24 2023 Zamir SUN <sztsian@gmail.com> - 1.4.0-1
- Update version to 1.4.0

* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 1.3.0-1
- Update version to 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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

* Sat Aug 07 2021 Zamir SUN <sztsian@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.16.0-4
- Fix FTBFS
- Fixes RHBZ#1987685

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

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

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Raphael Groner <projects.rg@smart.ms> - 0.11.1-5
- add upstram patch to avoid duplicates, rhbz#1459642

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Sat Aug 06 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-3.20160729git2f95601
- new git snapshot
- fix unlicensed files

* Wed Jul 06 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-2.20160705git8acfd2a
- new git snapshot
- drop dependency to liboobs
- add polkit
- adjust license

* Tue Jun 07 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-1.20160531git0f9ab3a
- initial
