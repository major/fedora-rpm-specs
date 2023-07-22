%global commit 46b5b9e4bfb75fbccc5043b07ef5c76a3cc72ce3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          ibus-unikey
Version:       0.6.1
Release:       31.20190311git46b5b9e%{?dist}
Summary:       Vietnamese engine for IBus input platform

License:       GPLv3
URL:           https://github.com/vn-input/ibus-unikey/
Source0:       https://github.com/vn-input/ibus-unikey/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: ibus-devel
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: pkgconf-pkg-config

Requires: ibus

%description
A Vietnamese engine for IBus input platform that uses Unikey.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}


%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_datadir}/%{name}/
%{_datadir}/ibus/component/unikey.xml
%{_libexecdir}/ibus-engine-unikey
%{_libexecdir}/ibus-setup-unikey
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.unikey.gschema.xml

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-31.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-30.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-29.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-28.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-27.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-26.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.6.1-25.20190311git46b5b9e
- Update for new cmake macros (out of source builds)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-24.20190311git46b5b9e
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-23.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-22.20190311git46b5b9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.6.1-21.20190311git46b5b9e
- Update the latest commit from upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-20.20181109git2a4f630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-19.20181109git2a4f630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.6.1-18.20181109git2a4f630
- Update to latest upstream 2a4f630

* Thu Nov 08 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.6.1-17.20180817git4fbe9b1
- Fix the compilation failure
- Update to latest packaging guidelines

* Wed Sep 12 2018 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.6.1-16
- Update the latest commit from upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.1-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 09 2012 Takao Fujiwara <tfujiwar@redhat.com> - 0.6.1-2
- Rebuild for ibus 1.4.99

* Fri Mar 02 2012 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.6.1-1
- Update release 0.6.1 from upstream for ibus 1.4.1 compatibilty and getting some bugs fixed

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 25 2011 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.6.0-1
- Update release 0.6.0 from upstream

* Mon Mar 28 2011 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.5.1-5
- Changing the .spec file to apply the Patch0 conditionally (Fedora >= 15 only)

* Mon Feb 21 2011 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.5.1-4
- Rewrite ChangeLog to meet the Packaging Guidelines as comment #11, bug #662604.

* Mon Feb 21 2011 Daiki Ueno <dueno@redhat.com> - 0.5.1-3
- Add a patch to build with ibus-1.4.

* Mon Dec 20 2010 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.5.1-2
- Use find_lang instead of {_datadir}/locale/...
- {_datadir}/{name}/* will only own the files inside that folder, use {_datadir}/{name}/ instead.
- Since ibus is a dependency of this package it should only own {_datadir}/ibus/component/unikey.xml.

* Mon Dec 13 2010 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.5.1-1
- Initial release 0.5.1 getting from upstream.

