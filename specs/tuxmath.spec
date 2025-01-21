Name:           tuxmath
Version:        2.0.3
Release:        20%{?dist}
Summary:        Educational math tutor for children

License:        GPL-3.0-or-later AND CC-BY-1.0 AND OFL-1.1
URL:            http://tux4kids.alioth.debian.org/
Source0:        https://alioth.debian.org/frs/download.php/3271/%{name}_w_fonts-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch0:         tuxmath_w_fonts-2.0.1-gcc5.patch
Patch1:         pointer-types.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_net-devel
BuildRequires:  librsvg2-devel
BuildRequires:	t4k_common-devel
Requires:       hicolor-icon-theme

%description
TuxMath is an educational math tutor for children. It features several
different types of gameplay, at a variety of difficulty levels.


%prep
%setup -q -n %{name}_w_fonts-%{version}
# remove unneeded font files
rm -f data/fonts/*.ttf
%patch -P 0 -p1
%patch -P 1 -p0


%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
make %{?_smp_mflags}


%install
%make_install
%find_lang %{name}

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 data/images/icons/icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/images/icons/tuxmath.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%{_pkgdocdir}
%{_bindir}/%{name}*
%{_bindir}/generate_lesson
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.0.3-18
- Patch for stricter flags

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.0.3-15
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.0.3-8
- Fix FTBFS.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.3-2
- Remove obsolete scriptlets

* Tue Nov 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.0.3-1
- 2.0.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Hans de Goede <hdegoede@redhat.com> - 2.0.1-10
- Add a patch fixing a crash when the powerup comet appears (rhbz#1293606)
- Install icons in the proper place
- Add an appdata file

* Fri Jul 24 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-9
- Add tuxmath_w_fonts-2.0.1-gcc5.patch (Fix F23FTBFS, RHBZ#1240080).
- Modernize spec.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.1-1
- 2.0.1
- Patch to use system scandir rather than conflicting removed from t4k_common.

* Wed Dec 29 2010 Jon Ciesla <limb@jcomserv.net> - 1.9.0-1
- 1.9.0

* Sat May 01 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.8.0-1
- 1.8.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.7.2-4
- remove fonts licence as shipped fonts has been removed

* Tue May 19 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.7.2-3
- fix end-of-line-encoding issue

* Mon May 18 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.7.2-2
- remove fonts

* Sun May 17 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.7.2-1
- initial packaging
