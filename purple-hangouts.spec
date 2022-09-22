%global plugin_name hangouts

%global commit0 55b9f01d040b240b794700f44d9c21a6cb51251e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20210629

Name: purple-%{plugin_name}
Version: 0
Release: 79.%{date}git%{shortcommit0}%{?dist}
Epoch: 1

License: GPLv3+
Summary: Hangouts plugin for libpurple
URL: https://github.com/EionRobb/%{name}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(zlib)

BuildRequires: gcc
BuildRequires: make

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Hangouts protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Hangouts to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Hangouts protocol implemented by
hangouts-purple.

%prep
%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
%set_build_flags
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%license gpl3.txt
%doc README.md

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-79.20210629git55b9f01
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-78.20210629git55b9f01
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1:0-77.20210629git55b9f01
- Rebuilt for protobuf 3.19.0

* Wed Oct 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-76.20210629gitefa7a53
- Updated to latest snapshot.

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 1:0-75.20200710gitefa7a53
- Rebuilt for protobuf 3.18.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-74.20200710gitefa7a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-73.20200710gitefa7a53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Adrian Reber <adrian@lisas.de> - 1:0-72.20200710gitefa7a53
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1:0-71.20200710gitefa7a53
- Rebuilt for protobuf 3.13

* Wed Aug 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-70.20200710gitefa7a53
- Switched upstream URL from BitBucket to GitHub.
- Updated to latest snapshot.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-69.20200423hg789eaca
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1:0-68.20200423hg789eaca
- Rebuilt for protobuf 3.12

* Wed May 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-67.20200423hg789eaca
- Updated to latest snapshot.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-66.20190607hg3f7d89b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-65.20190607hg3f7d89b
- Updated to latest snapshot.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-64.20190303hgeffc9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-63.20190303hgeffc9b4
- Updated to latest snapshot.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-62.20181118hg833609a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-61.20181118hg833609a
- Updated to latest snapshot.

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-60.20180731hge4ccf26
- Updated to latest snapshot.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-59.20180419hg9d008f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-58.20180419hg9d008f2
- Updated to latest snapshot.

* Wed Apr 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-57.20180328hg0e137e6
- Updated to latest snapshot.

* Sat Feb 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-56.20180218hga4beeb3
- Updated to latest snapshot.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-55.20180128hg73089d2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-54.20180128hg73089d2
- Updated to latest snapshot.

* Tue Jan 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-53.20171023hg4ce9b33
- Fixed build under Fedora Rawhide.

* Wed Nov 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-52.20171023hg4ce9b33
- Fixed build under EPEL7.

* Wed Nov 08 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-51.20171023hg4ce9b33
- Updated to latest snapshot.

* Sat Sep 09 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-50.20170803hg65f3f51
- Updated to latest snapshot.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-49.20170427hg0dc1213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-48.20170427hg0dc1213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-47.20170427hg0dc1213
- Updated to latest snapshot.

* Mon Apr 10 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-46.20170409hg0b17daa
- Updated to latest snapshot.

* Tue Mar 14 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-45.20170313hg462bb55
- Updated to latest snapshot.

* Sat Mar 11 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-44.20170308hga755fcc
- Updated to latest snapshot.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0-43.20161222hg7c0a620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-42.20161222hg7c0a620
- Updated to latest snapshot.

* Sun Dec 04 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-41.20161128hg4c2de0f
- Updated to latest snapshot.

* Tue Nov 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-40.20161122hgb80a0e1
- Updated to latest snapshot.

* Mon Oct 24 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-39.20161023hgf66236a
- Updated to latest snapshot.

* Sat Oct 01 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-38.20160924hg00e28b7
- Updated to latest snapshot.

* Sun Sep 25 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-37.20160924hg6b1ec4a
- Updated to latest snapshot.

* Thu Aug 25 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-36.20160821hgfbd4536
- Updated to latest snapshot.

* Fri Aug 05 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-35.20160803hgc5f97d3
- Updated to latest snapshot.

* Tue Jul 19 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-34.20160714hgd6eb7fe
- Updated to latest snapshot.

* Tue Jul 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-33.20160712hg2c60a5e
- Updated to latest snapshot.

* Sun Jul 10 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-32.20160710hg5378549
- Fixed Requires for pidgin subpackage. Replaced Perl to sed in prep section.

* Sun Jul 10 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0-31.20160710hg5378549
- Fixed version. Updated SPEC file.

* Sun Jul 10 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-30.20160710hg5378549
- Updated to latest snapshot. Updated install section due upstream changes.

* Tue Jun 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-29.20160621hg38f0731
- Added missing LDFLAGS to build.

* Tue Jun 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-28.20160621hg38f0731
- Updated to latest Git snapshot.

* Fri Jun 17 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-27.20160615hg2059439
- Updated to latest snapshot. Removed patch.

* Sun Jun 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-26.20160609hg90c515d
- Updated to latest snapshot. Removed empty configure script.

* Mon Jun 06 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-25.20160601hgf362605
- Updated to latest snapshot.

* Fri May 27 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-24.20160527hge643cc7
- Updated to latest snapshot. Updated patch.

* Thu May 26 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-23.20160526hg8cafb7a
- Updated to latest snapshot. Updated patch.

* Fri May 13 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-22.20160512hg7a23ed5
- Updated to latest snapshot.

* Tue May 10 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-21.20160510hg78a9c80
- Updated to latest snapshot. Updated patch.

* Sat May 07 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-20.20160507hg2095ac0
- Updated to latest snapshot.

* Thu May 05 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-19.20160505hg4cf1d50
- Updated to latest snapshot.

* Wed May 04 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-18.20160504hge8c30b6
- Updated to latest snapshot.

* Tue May 03 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-17.20160502hg2631ad2
- Updated to latest snapshot. Added patch for Fedora.

* Tue Apr 26 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-16.20160426hgac1741f
- Updated to latest snapshot.

* Thu Apr 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-15.20160421hg6f76943
- Updated to latest snapshot.

* Sun Apr 17 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-14.20160417hg635f50c
- Updated to latest snapshot.

* Fri Apr 15 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-13.20160413hg92bfbf1
- Updated to latest snapshot.

* Sun Apr 10 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-12.20160410hga5b0e60
- Updated to latest snapshot.

* Sat Apr 09 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-11.20160409hg7442ecd
- Updated to latest snapshot.

* Wed Apr 06 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-10.20160406hgab7c25a
- Added license section. Updated to latest snapshot.

* Tue Apr 05 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-9.20160405hgbd3b2be
- Fixed SPEC. Updated to latest snapshot.

* Sun Apr 03 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-8.20160403hg0f3cbbd
- Updated to latest snapshot.

* Fri Apr 01 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-7.20160401hg8b37dcc
- Updated to latest snapshot.

* Tue Mar 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-6.20160322hg735b7f8
- Updated to latest snapshot.

* Thu Mar 17 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-5.20160316hgfde2d8a
- Updated to latest snapshot.

* Tue Mar 15 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20160315hg694bd41
- Updated to latest snapshot.

* Tue Mar 08 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20160306hgb7ba81f
- Updated to latest snapshot.

* Fri Mar 04 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20160303hg4789156
- Updated to latest snapshot.

* Mon Feb 29 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20160227hga2c9af3
- First SPEC version.
