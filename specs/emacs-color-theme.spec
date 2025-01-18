%global pkg color-theme
%global pkgname Emacs Color Themes

Name:		emacs-%{pkg}
Version:	6.6.0
Release:	31%{?dist}
Summary:	Color themes for Emacs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.nongnu.org/color-theme
Source0:	http://ftp.twaren.net/Unix/NonGNU/color-theme/%{pkg}-%{version}.tar.gz
Source1:	emacs-color-theme-init.el
#Patches are submitted to upstream
#http://lists.nongnu.org/archive/html/color-theme-devel/2010-04/msg00000.html
#Patch to fix Makefile
Patch0:		emacs-%{pkg}-fix-compile.patch
#Patch to fix README
Patch1:		emacs-%{pkg}-fix-readme.patch
#Patch to fix License file
Patch2:		emacs-%{pkg}-fix-copying-eol.patch

BuildArch:	noarch
BuildRequires:	emacs
BuildRequires: make
Requires:	emacs(bin) >= %{_emacs_version}

Obsoletes:      %{name}-el < 6.6.0-28
Provides:       %{name}-el = %{version}-%{release}

%description
%{pkgname} is an add-on package for GNU Emacs.
It provides a lot of different color themes to skin your Emacs greatly
improving the editing experience. It also includes a neat framework to
help you creating new themes from your current emacs customization's.
Also features an easy way to share your custom themes with the world.  

%prep
%setup -q -n %{pkg}-%{version}
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}/themes
mkdir -p %{buildroot}%{_emacs_sitestartdir}/
cp %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
cp *.el *.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}
cp themes/*.el themes/*.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}/themes

%files
%doc COPYING README
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/themes/*.el
%{_emacs_sitelispdir}/%{pkg}/themes/*.elc
%dir %{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/emacs-color-theme-init.el

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 6.6.0-30
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 15 2024 Tim Landscheidt <tim@tim-landscheidt.de> - 6.6.0-28
- Obsolete -el subpackage (#1234527, #1542630)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 9 2010 Arun SAG <sagarun@gmail.com> - 6.6.0-3
- clean section removed
- Added startup file emacs-color-theme-init.el
- 
* Sat Apr 17 2010 Arun SAG <sagarun@gmail.com> - 6.6.0-2
- Spec adjusted to obey latest emacs packaging guidelines
- License field corrected to GPLv2+

* Thu May 15 2009 Filippo Argiolas <fargiolas@gnome.org> - 6.6.0-1
- Initial packaging
