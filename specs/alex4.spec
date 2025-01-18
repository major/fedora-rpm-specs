Name:           alex4
Version:        1.0
Release:        45%{?dist}
Summary:        Alex the Allegator 4 - Platform game
License:        GPL-1.0-or-later
URL:            https://obiot.github.io/Alex4-WE/readme.html
Source0:        http://downloads.sf.net/allegator/Alex4/source%20and%20data/alex4src_data.zip
Source1:        alex4.desktop
Source2:        alex4.png
Source3:        alex4.appdata.xml
Patch0:         alex4-unix.patch
Patch1:         alex4-allegro-4.2.patch
Patch2:         alex4-dot-files-endian-clean.patch
Patch3:         alex4-fsf-address.patch
Patch4:         alex4-ini-comment.patch
Patch5:         alex4src-warnings.patch
Patch6:         alex4-fcommon-fix.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel dumb-devel desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
In the latest installment of the series Alex travels through the jungle in
search of his kidnapped girlfriend. Plenty of classic platforming in four
nice colors guaranteed!


%prep
%autosetup -p1 -n alex4src
sed -i 's/\r//' *.txt *.ini


%build
pushd src
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations -Wno-unused-result -DALLEGRO_FIX_ALIASES"
popd


%install
pushd src
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc license.txt readme.txt alex4.ini
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-43
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Hans de Goede <hdegoede@redhat.com> - 1.0-32
- Fix FTBFS (rhbz#1799146)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0-28
- Rebuild with fixed binutils

* Sun Jul 29 2018 Hans de Goede <hdegoede@redhat.com> - 1.0-27
- Fix FTBFS (rhbz#1603365)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-24
- Remove obsolete scriptlets

* Fri Sep 08 2017 Hans de Goede <hdegoede@redhat.com> - 1.0-23
- Run windowed rather then fullscreen by default
- Add example alex4.ini to the documentation (for e.g. setting fullscreen mode)
- Add appdata

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0-14
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Hans de Goede <hdegoede@redhat.com> - 1.0-11
- Rebuild for new allegro-4.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 1.0-7
- Fix patch fuzz build failure

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-6
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-5
- Several patches from Debian (Thanks Peter De Wachter)
  - endian clean dot-files code
  - fsf address corrected
  - no longer use deprecated allegro functions

* Thu Aug  2 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-4
- Update License tag for new Licensing Guidelines compliance

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-3
- Fixup .desktop file categories for games-menus usage

* Fri Nov  3 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-2
- Updated alex4-unix.patch to take big endian machines into account when
  loading maps

* Thu Nov  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-1
- Initial Fedora Extras package
