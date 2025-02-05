#remove once using %%configure again
%global debug_package %{nil}
%define apricotsdir %{_datadir}/apricots
Name: apricots
Version:  0.2.9
Release:  1%{?dist}
Summary: 2D air combat game

License: GPL-2.0-only
URL: https://github.com/moggers87/apricots
Source0: %{url}/archive/v%{version}/apricots-%{version}.tar.gz       
Source1: apricots.png
#Icon created from screenshot on website
Source2: apricots.desktop

BuildRequires: gcc gcc-c++
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils
BuildRequires: openal-soft-devel
BuildRequires: alure-devel
BuildRequires: autoconf automake
BuildRequires: make
ExcludeArch: ppc64le aarch64

%description
It's a game where you fly a little plane around the screen and
shoot things and drop bombs on enemy targets, and it's meant to be quick 
and fun.

%prep
%setup -q

%build
./bootstrap
#Use %%configure once --as-needed is fixed, and fix debug at top of spec.
./configure --prefix=%{_prefix}
%make_build


%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 apricots/data/apricots.cfg %{buildroot}%{_sysconfdir}
rm %{buildroot}%{_datadir}/apricots/apricots.cfg
ln -s ../../..%{_sysconfdir}/apricots.cfg %{buildroot}%{_datadir}/apricots/apricots.cfg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps


%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/apricots
%{_datadir}/apricots
%{_datadir}/applications/apricots.desktop
%{_datadir}/icons/hicolor/24x24/apps/apricots.png
%config(noreplace) %{_sysconfdir}/apricots.cfg


%changelog
* Mon Feb 03 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.2.9-1
- 0.2.9

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.2.7-6
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.2.7-1
- 0.2.7, new upstream.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.6-27
- Fix AP_PATH.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.6-25
- Fix FTBFS.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.2.6-23
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.6-20
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.6-14
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.2.6-10
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-8
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 20 2009 Jon Ciesla <limb@jcomserv.net> - 0.2.6-5
- Rebuild for openal-soft.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Jon Ciesla <limb@jcomserv.net> - 0.2.6-2
- Re-base off of pristine tarball, md5 error in review.

* Tue Aug 26 2008 Jon Ciesla <limb@jcomserv.net> - 0.2.6-1
- Initial packaging.
