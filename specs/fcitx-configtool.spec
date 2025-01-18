Name:		fcitx-configtool
Version:	0.4.10
Release:	22%{?dist}
Summary:	Gtk+-based configuring tools for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/fcitx/fcitx-configtool
Source0:	http://download.fcitx-im.org/fcitx-configtool/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libxml2-devel
BuildRequires:	gtk2-devel, iso-codes-devel, libtool, unique-devel
BuildRequires:	gtk3-devel, unique3-devel
Requires:	fcitx


%description
fcitx-config-gtk and fcitx-config-gtk3 are Gtk based configuring tools for
Fcitx.


%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DENABLE_GTK3=ON -DENABLE_GTK2=ON
%cmake_build


%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc README
%license COPYING
%{_bindir}/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.10-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0.4.10-11
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.4.10-4
- BR gcc for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb  3 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.4.10-2
- Rebuild for SONAME bump of libfcitx-gclient.so

* Sun Sep 24 2017 Robin Lee <cheeselee@fedoraproject> - 0.4.10-1
- Update to 0.4.10

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.4.9-1
- Update to 0.4.9

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  1 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.4.8-1
- Update to 0.4.8 (BZ#1230892)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Liang Suilong <liangsuilong@gmail.com> - 0.4.7-1
- Upstream to fcitx-configtool-0.4.7

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 28 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.5.1-1
- Upstream to fcitx-configtool-0.4.5.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.4-1
- Upstream to fcitx-configtool-0.4.4

* Sat May 12 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.3-2
- Fix Segenttation Fault on GTK3

* Sat May 12 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.3-1
- Upstream to 0.4.3

* Fri Mar 09 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.1-1
- Upstream to 0.4.1

* Sun Feb 26 2012 Liang Suilong <liangsuilong@gmail.com> - 0.4.0-1
- Initial Package
