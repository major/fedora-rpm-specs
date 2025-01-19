%global hash 8f8654809ca5
%global bbrepo jeromerobert

Name:           k4dirstat
Version:        3.2.0
Release:        12%{?dist}
Summary:        Graphical Directory Statistics for Used Disk Space

# Automatically converted from old format: GPLv2 and LGPLv2 - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2
URL:            https://bitbucket.org/jeromerobert/k4dirstat/wiki/Home

Source0:        https://bitbucket.org/jeromerobert/k4dirstat/get/%{name}-%{version}.tar.bz2

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: extra-cmake-modules cmake gcc-c++
BuildRequires: pkgconfig(zlib)
# kf5 deps
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-kiconthemes-devel
# qt deps
BuildRequires: pkgconfig(Qt5Widgets)

%description
KDirStat (KDE Directory Statistics) is a utility program that sums up
disk usage for directory trees - very much like the Unix 'du' command.
It can also help you clean up used space.

%prep
%setup -qn %{bbrepo}-%{name}-%{hash}

%build

%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} || touch %{name}.lang

cd %{buildroot}%{_kde4_bindir}
ln -s k4dirstat kdirstat

%check
desktop-file-validate \
  %{buildroot}/%{_datadir}/applications/k4dirstat.desktop

%files -f %{name}.lang
%license COPYING COPYING.LIB
%doc AUTHORS CREDITS
%{_kde4_bindir}/k4dirstat
%{_kde4_bindir}/kdirstat
%{_kde4_datadir}/applications/k4dirstat.desktop
%{_kde4_datadir}/man/man1/*
%{_kde4_datadir}/config.kcfg/k4dirstat.kcfg
%{_kde4_docdir}/HTML/en/k4dirstat/
%{_kde4_iconsdir}/hicolor/*/apps/k4dirstat.png
%{_kde4_iconsdir}/hicolor/scalable/apps/k4dirstat.svgz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.0-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Dmitrij S. Kryzhevich <kruzhev@ispms.ru> - 3.2.0-1
- Update to 3.2.0.
- kde4 -> kf5 macroses.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 03 2016 Dmitrij S. Kryzhevich <kruzhev@ispms.ru> - 3.1.2-1
- Update to 3.1.2 version.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.8-1
- Change to new upstream.
- Update to new 2.7.8.
- Drop prerelease kdirstat-quotes.patch.
- Drop snapshot script as bitbucket provides similar functionality.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.7.0-0.17.20101010git6c0a9e6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-0.16.20101010git6c0a9e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-0.15.20101010git6c0a9e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.14.20101010git6c0a9e6
- kdebase-devel turn into kde-baseapps-devel (BR).

* Thu Mar 20 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.13.20101010git6c0a9e6
- Add (now) mandatory cmake BuildRequires.

* Wed Mar 19 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.12.20101010git6c0a9e6
- Fix bogus date (Tue Dec 16 2010 -> Thu Dec 16 2010).

* Wed Mar 19 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.11.20101010git6c0a9e6
- Fix CVE-2014-2527.
- Delete defatr entry in files section.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-0.10.20101010git6c0a9e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-0.9.20101010git6c0a9e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-0.8.20101010git6c0a9e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-0.7.20101010git6c0a9e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-0.6.20101010git6c0a9e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.5.20101010git6c0a9e6
- Add symlink kdirstat -> k4dirstat.

* Sat Dec 04 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.4.20101010git6c0a9e6
- Cleanup spec.

* Mon Oct 11 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.3.20101010git6c0a9e6
- Sources update to git 6c0a9e6.
- Zlib patch dropped.
- Add obsoletes for kdirstat.

* Sun Oct 10 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.2.20101010gitdd2de8e
- Change kdebase-devel to kdebase4-devel for sure.

* Sun Oct 10 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 2.7.0-0.1.20101010gitdd2de8e
- Sources update.
- %%fles clean up.
- Add script for getting sources.
- Add LGPLv2 to License.
- Add kdebase-devel to BR.
- Move desktop-file-validate to %%check.
- Update zlib patch.

* Tue Jun  8 2010  <Laurent.Rineau__fedora@normalesup.org> - 0-0.6.20100304gitec01dd42
- %%{_kde4_docdir}/HTML/en/k4dirstat/ must be owned.

* Tue Jun  8 2010  <Laurent.Rineau__fedora@normalesup.org> - 0-0.5.20100304gitec01dd42
- Fix the changelog (bad email and bad use of %%{?dist}).

* Tue Jun  8 2010  <Laurent.Rineau__fedora@normalesup.org> - 0-0.4.20100304gitec01dd42
- Patch0 for F-13: link explicitly with zlib.
- Add a comment on Source0.

* Sat Mar  6 2010  <Laurent.Rineau__fedora@normalesup.org> - 0-0.3.20100304gitec01dd42
- New upstream version.
- New doc files (added upstream). Among them: COPYING, README, AUTHORS.
- Patch0 is merged upstream.

* Tue Mar  2 2010  <Laurent.Rineau__fedora@normalesup.org> - 0-0.2.20100223gitd3b530af3
- Use kde4 rpm macros.

* Tue Mar  2 2010  <Laurent.Rineau__fedora@normalesup.org> - 0-0.1.20100223gitd3b530af3
- Initial build.
