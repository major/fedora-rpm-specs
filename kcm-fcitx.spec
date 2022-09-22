%undefine __cmake_in_source_build
Name:		kcm-fcitx
Version:	0.5.6
Release:	6%{?dist}
Summary:	KDE Config Module for Fcitx
License:	GPLv2+
URL:		https://github.com/fcitx/kcm-fcitx
Source0:	http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	fcitx-devel gettext libxkbfile-devel
BuildRequires:	qt5-qtbase-devel qt5-qtx11extras-devel
BuildRequires:	fcitx-qt5-devel
BuildRequires:	desktop-file-utils
BuildRequires:	extra-cmake-modules
BuildRequires:	kf5-rpm-macros kf5-kcoreaddons-devel kf5-kwidgetsaddons-devel kf5-kcmutils-devel kf5-kitemviews-devel kf5-ki18n-devel kf5-kio-devel kf5-knewstuff-devel
Requires:	fcitx kf5-filesystem

Patch0: gcc10.patch

%description
Kcm-fcitx is a System Settings module to manage Fcitx. You can config fcitx
through "Personalization" - "Regional Settings" - "Input Method" now.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-kde


%files -f %{name}.lang
%license COPYING
%{_bindir}/kbd-layout-viewer
%{_kf5_qtplugindir}/kcm_fcitx.so
%{_kf5_datadir}/kservices5/kcm_fcitx.desktop
%{_datadir}/applications/kbd-layout-viewer.desktop

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Qiyu Yan <yanqiyu01@gmail.com> - 0.5.6-1
- update to upstream

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@fedoraproject.org> - 0.5.5-6
- Fix narrowing conversion issue catch by gcc-10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Robin Lee <cheeselee@fedoraproject> - 0.5.5-1
- Update to 0.5.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Robin Lee <cheeselee@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3

* Sat Nov 14 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.5.2-1
- Update 0.5.2
- URL and description revised

* Thu Oct  1 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1, using KF5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.3-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Liang Suilong <liangsuilong@gmail.com> - 0.4.3-1
- Upstream to kcm-fcitx-0.4.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.1-1
- Upstream to kcm-fcitx-0.4.1

* Sun Jul 29 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.0-3
- Fix spec error 

* Sun Jul 29 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.0-2
- Add kbd-layout-viewer

* Sun Jul 29 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.0-1
- Upstream to kcm-fcitx-0.4.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Liang Suilong <liangsuilong@gmail.com> - 0.3.3-1
- Upstream to kcm-fcitx-0.3.3

* Sun Feb 19 2012 Liang Suilong <liangsuilong@gmail.com> - 0.3.0-1
- Initial Release
