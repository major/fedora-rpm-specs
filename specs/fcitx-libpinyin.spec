Name:		fcitx-libpinyin
Version:	0.5.4
Release:	12%{?dist}
Summary:	Libpinyin Wrapper for Fcitx
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Libpinyin
Source0:	http://download.fcitx-im.org/fcitx-libpinyin/%{name}-%{version}_dict.tar.xz

BuildRequires:	gcc
BuildRequires:	libpinyin-devel >= 1.9.91
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libpinyin-devel
BuildRequires:	libpinyin-tools, glib2-devel, fcitx
BuildRequires:	qt5-qtwebengine-devel, dbus-devel
BuildRequires:	fcitx-qt5-devel >= 1.1
Requires:	fcitx
# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
ExclusiveArch: %{qt5_qtwebengine_arches}

%description
Fcitx-libpinyin is a libpinyin Wrapper for Fcitx.

Libpinyin is a Frontend of the Intelligent Pinyin IME Backend.


%prep
%setup -q -n %{name}-%{version}


%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/fcitx/%{name}.so
%{_libdir}/fcitx/qt/*.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/imicon/*
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/inputmethod/*-libpinyin.conf
%{_datadir}/fcitx/libpinyin/
%{_datadir}/icons/hicolor/48x48/status/fcitx-*.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 Peng Wu <pwu@redhat.com> - 0.5.4-7
- Migrate to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Peng Wu <pwu@redhat.com> - 0.5.4-5
- Rebuild for libpinyin soname bump

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 0.5.4-1
- update to 0.5.4 upstream release (#1922484)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0.5.3-11
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.5.3-4
- BR gcc for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-2
- Remove obsolete scriptlets

* Sun Sep 24 2017 Robin Lee <cheeselee@fedoraproject> - 0.5.3-1
- Update to 0.5.3

* Fri Aug 25 2017 Peng Wu <pwu@redhat.com> - 0.5.1-5
- Rebuilt for libpinyin 2.1.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun  9 2017 Peng Wu <pwu@redhat.com> - 0.5.1-2
- Rebuilt for libpinyin 2.0.91

* Fri May 12 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1
- ExclusiveArch set to %%qt5_qtwebengine_arches

* Fri Mar  3 2017 Peng Wu <pwu@redhat.com> - 0.4.1-4
- Rebuilt for Fedora 27

* Wed Mar  1 2017 Peng Wu <pwu@redhat.com> - 0.4.1-3
- Rebuilt for libpinyin 1.9.91

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  3 2017 Peng Wu <pwu@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Thu Dec  8 2016 Peng Wu <pwu@redhat.com> - 0.4.0-1
- Update to 0.4.0
- Rebuilt for libpinyin 1.7.0

* Tue Nov  1 2016 Peng Wu <pwu@redhat.com> - 0.3.91-3
- Rebuilt for libpinyin 1.6.91

* Wed Aug  3 2016 Peng Wu <pwu@redhat.com> - 0.3.91-2
- Rebuilt for libpinyin 1.5.92

* Fri Jul 22 2016 Peng Wu <pwu@redhat.com> - 0.3.91-1
- Update 0.3.91

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Tue Jul 14 2015 Peng Wu <pwu@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 12 2015 Peng Wu <pwu@redhat.com> - 0.3.1-4
- Rebuilt for libpinyin

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 23 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1
- Update URL and Source0 URL
- BR: qt-devel, dbus-devel, qtwebkit-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  8 2013 Peng Wu <pwu@redhat.com> - 0.2.92-1
- Upstream to 0.2.92

* Mon Mar 18 2013 Liang Suilong <liangsuilong@gmail.com> - 0.2.90-1
- Upstream to 0.2.90

* Fri Mar 08 2013 Liang Suilong <liangsuilong@gmail.com> - 0.2.1-3
- Rebuilt for the latest libpinyin

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 Liang Suilong <liangsuilong@gmail.com> - 0.2.1-1
- Upstream to 0.2.1

* Sun Jul 29 2012 Liang Suilong <liangsuilong@gmail.com> - 0.2.0-1
- Upstream to 0.2.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Liang Suilong <liangsuilong@gmail.com> - 0.1.1-1
- Upstream to 0.1.1

* Wed Feb 08 2012 Liang Suilong <liangsuilong@gmail.com> - 0.1.0-1
- Initial Package
