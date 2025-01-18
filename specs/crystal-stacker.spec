Name:           crystal-stacker
Version:        1.5
Release:        44%{?dist}
Summary:        Falling blocks, match 3 or more of the same color crystals
# Automatically converted from old format: Crystal Stacker - review is highly recommended.
License:        CrystalStacker
URL:            http://www.t3-i.com/cstacker.htm
Source0:        http://www.t3-i.com/games/crystal_stacker/downloads/crystal_stacker-1.5-src.zip
Source1:        %{name}.desktop
Source2:        %{name}-theme-editor.desktop
Source3:        %{name}-48.png
Source4:        %{name}-128.png
Source5:        %{name}.appdata.xml
Patch0:         crystal-stacker-1.5-ImplicitDSOLinking.patch
Patch1:         crystal-stacker-1.5-fcommon-fix.patch
BuildRequires:  gcc allegro-devel dumb-devel
BuildRequires:  ImageMagick desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
If you've played Columns then you know what Crystal Stacker is all about.
Match 3 or more of the same color crystals either horizontally, vertically,
or diagonally to destroy them. For every 45 crystals you destroy, the level
increases and the crystals fall faster. The higher the level, the more points
you are awarded for destroying crystals.


%package theme-editor
Summary:        Themes editor for Crystal Stacker
Requires:       %{name} = %{version}

%description theme-editor
Create new Themes for Crystal Stacker


%prep
%autosetup -p1 -c
%{__sed} -i 's/\r//' ce/*.txt cs/*.txt


%build
pushd cs/source
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
popd

pushd ce/source
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-char-subscripts"
popd

convert cs/cs.ico %{name}.png
convert ce/ce.ico %{name}-theme-editor.png


%install
pushd cs/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

pushd ce/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{name}.png %{name}-theme-editor.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc cs/*.txt
%{_bindir}/crystal-stacker
%dir %{_datadir}/crystal-stacker
%{_datadir}/crystal-stacker/cs.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files theme-editor
%doc ce/*.txt
%{_bindir}/crystal-stacker-theme-editor
%{_datadir}/crystal-stacker/ce.dat
%{_datadir}/applications/%{name}-theme-editor.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}-theme-editor.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-43
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar  4 2020 Hans de Goede <hdegoede@redhat.com> - 1.5-31
- Fix FTBFS (rhbz#1799264)
- Add 48x48 and 128x128 icons
- Add appdata

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-25
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 14 2013 Hans de Goede <hdegoede@redhat.com> - 1.5-17
- Fix Source0 URL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5-15
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Hans de Goede <hdegoede@redhat.com> - 1.5-11
- Rebuild for new allegro-4.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 15 2010 Hans de Goede <hdegoede@redhat.com> 1.5-9
- Fix FTBFS (#565102)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5-6
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-5
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-4
- Update License tag for new Licensing Guidelines compliance
- Fix invalid desktop file (fix building with latest desktop-file-utils)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-3
- FE6 Rebuild

* Thu Jul  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-2
- Rebuild against new allegro to remove executable stack requirement caused
  by previous versions of allegro.

* Sat May  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-1
- New upstream release 1.5 (final).

* Sat Apr  8 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-0.pre.2
- Updated Patch0 to not unnescesarry pause the music when selecting
  a new theme and using pthreads to play the music.

* Fri Apr  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.5-0.pre.1
- Initial Fedora Extras package
