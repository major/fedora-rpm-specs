Name:           lpairs
Summary:        Classical memory game with cards
Version:        1.0.5
Release:        16%{?dist}
# Automatically converted from old format: GPLv2+ and CC-BY-SA and Freely redistributable without restriction - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Fedora-UltraPermissive
URL:            https://lgames.sourceforge.net/index.php?project=LPairs
Source0:        https://downloads.sourceforge.net/lgames/lpairs-%{version}.tar.gz
#there is a problem with data dir
#the author said it would be hard for him to fix it at autoconf level
Patch0:         lpairs-1.0.3-datadir.diff
Patch1:         lpairs-1.0.4-desktop.diff
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  SDL-devel
BuildRequires:  gettext
BuildRequires: make

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed
will be counted but there is no highscore chart or limit to this.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build
# FIXME: Package suffers from c11/inline issues
# Workaround by appending -std=gnu89 to CFLAGS
# Proper fix would be to fix the source-code
CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"

%configure inst_dir="%{_datadir}/%{name}"
make %{?_smp_mflags}

%install
rm -fr %{buildroot}
make DESTDIR=%{buildroot} inst_dir="%{_datadir}/%{name}" install
%find_lang %{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp lpairs.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        lpairs.desktop

%files -f %{name}.lang
%{_bindir}/lpairs
%{_datadir}/%{name}
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.5-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.5-1
- Upgrade to 1.0.5 (Bug 1653264)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.4-16
- Append -std=gnu89 to CFLAGS (Fix F23FTBFS, RHBZ#1239657)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 7 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.4-6
- removed macros from changelog
- removed spaces introduces during last changes (instead of tabs)

* Sat Mar 7 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.4-5
- changed licence tag to cover sounds (suggested by Alexey Torkhov)
- removed redundant attr()
- fixed desktop-file-utils dependency

* Wed Mar 4 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.4-4
- added CC-BY-SA to the license tag (tango icons)
- changed defattr to those recomended by packaging guidelines

* Tue Mar 3 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.4-3
- applied suggestion from Alexey Torkhov and  Michael Schwendt (all below)
- removed %%makeinstall
- added desktop-file-utils to BuildRequires
- removed "--vendor fedora"
- removed update-desktop-database form %%pre and %%post
- removed SDL from Requires

* Mon Jan 5 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.4-2
- cleaned up SPEC file before submition to Fedora repository

* Sun Sep 14 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.4-1
- updated to 1.0.4
- added icon file

* Sat Aug 23 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.3-1
- initial release

