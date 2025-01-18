Name:		biniax
Version:	1.2
Release:	41%{?dist}
Summary:	A unique arcade logic game

License:	Zlib
URL:		http://www.biniax.com/
Source0:	http://mordred.dir.bg/%{name}/%{name}-src.zip
Source1:	%{name}.desktop
# Icon taken from the source, icon.ico
Source2:	%{name}.png
# Fixes the path in gfx.c, snd.c. and creates a ~/.biniax subdir 
# with "autosave" and "highscore" data. Patches send to upstream!
Patch0:		%{name}-%{version}-gfx.patch
Patch1:		%{name}-%{version}-snd.patch
Patch2:		%{name}-%{version}-save.patch
Patch3:		%{name}-%{version}-optflags.patch
Patch4:		%{name}-%{version}-close.patch

Requires:	hicolor-icon-theme
BuildRequires:  gcc
BuildRequires:	SDL-devel SDL_mixer-devel desktop-file-utils
BuildRequires: make

%description
The gaming field is 5x7 pairs of elements. Every pair consists of two elements 
out of four possible types (colors). Player is a single element, who can move on
empty fields or can take a pair, if the player's element is present in the pair.
If a pair is taken, the player's element is swapped to the other element of the 
pair. The field is scrolling down on time event or after certain moves are spend
(depending on the game mode). Game over is when there is no move for the player.


%prep
%setup -q -c -n %{name}
%patch -P0 -p0 -b .gfx
%patch -P1 -p0 -b .snd
%patch -P2 -p0 -b .save
%patch -P3 -p0 -b .optflags
%patch -P4 -p0 -b .close
# Needed because of this rpmlint warning "W: wrong-file-end-of-line-encoding"
sed -i 's/\r//' Readme.txt LICENSE.txt
# Set datadir prefix, snd.patch and gfx.patch
sed -i 's!@DATADIR@!%{_datadir}!' desktop/gfx.c
sed -i 's!@DATADIR@!%{_datadir}!' desktop/snd.c


%build

make %{?_smp_mflags}


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/data

install -p -m 755 biniax %{buildroot}%{_bindir}/%{name}
install -p -m 644 data/* %{buildroot}%{_datadir}/%{name}/data/


# below the desktop file and icon stuff
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files
%doc LICENSE.txt Readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2-36
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.2-28
- Fix FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-22
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 08 2012 Jon Ciesla <limburgher@gmail.com> - 1.2-12
- Patch fix.

* Wed Aug 08 2012 Jon Ciesla <limburgher@gmail.com> - 1.2-11
- Allow closing with x button in window manager, BZ 513416.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 26 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 1.2-7
- Re-import to Fedora

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 1.2-4
- Add datadir prefix, snd.patch and gfx.patch
- Remove obsolete desktop-file-install --vendor="fedora"

* Sat Oct 25 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 1.2-3
- Cosmetic corrections

* Sat Oct 18 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 1.2-2
- Add fix for "W: wrong-file-end-of-line-encoding"
- Add RPM_OPT_FLAGS patch
- Add more macros to spec
- Add more info to .desktop file
- Changed summary
- Remove BuildRequires: dos2unix

* Tue Aug 05 2008 Stefan Posdzich <cheekyboinc@foresightlinux.org> - 1.2-1
- Initial SPEC file
