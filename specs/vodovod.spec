Name:		vodovod
Version:	1.10r22
Release:	27%{?dist}
Summary:	A pipe connecting game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://home.gna.org/vodovod/
#Source:	http://download.gna.org/vodovod/%%{name}-%%{version}-src.tar.gz
# svn export -r 22 svn://svn.gna.org/svn/vodovod/trunk vodovod
# tar czvf vodovod-1.10r22-src.tar.gz vodovod
Source:		%{name}-%{version}-src.tar.gz
Patch0:		vodovod-1.10r22-locales.patch
Patch1:		vodovod-1.10r22-format-string.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils SDL-devel SDL_image-devel SDL_mixer-devel
BuildRequires:	SDL_ttf-devel gettext ImageMagick

# Automate finding font file paths
%global fonts font(dejavusansmono)
Requires:	%{fonts}
BuildRequires:  fontconfig %{fonts}

Requires(post): coreutils
Requires(postun): coreutils

%description
A free cross-platform pipe connecting game. You get a limited number
of pipes on each level and need to combine them to lead the water from
the house at the top of the screen to the storage tank at the bottom.

%description -l cs_CZ.UTF-8
Svobodná, multiplatformní logická hra založená na propojování potrubí.
Každá úroveň začíná s omezeným množstvím trubek, které je potřeba umístit
tak, aby svedly vodu z domku na vrchu obrazovky do nádrže dole.

%description -l sk_SK.UTF-8
Slobodná, multiplatformná logická hra založená na spojovaní potrubia.
Každá úroveň začína s obmedzeným množstvom trubiek, ktoré musíte umiestniť tak,
aby viedli vodu z domčeka v hornej časti obrazovky do nádrže v dolnej časti.


%prep
#%%setup -q -n %%{name}-%%{version}-src
%setup -q -n %{name}
# update locales
%patch -P0 -p1
# fix bug #1037377
%patch -P1 -p1

%build
make PREFIX=%{_prefix} HIGHSCOREDIR=%{_localstatedir}/games \
	%{?_smp_mflags} CXX="%{__cxx}" CXXFLAGS="%{optflags}"
# .desktop file 
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=Vodovod
GenericName=Logic Game
GenericName[cs]=Logická hra
GenericName[sk]=Logická hra
Comment=A pipe connecting game
Comment[cs]=Propojování potrubí
Comment[sk]=Spojovanie potrubia
Exec=vodovod
Icon=vodovod
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF


%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
# replace the bundled font usage with the one provided by font package
ln -f -s $(fc-match -f "%{file}" "dejavusansmono") \
        %{buildroot}%{_datadir}/%{name}/data/font1.ttf
# since the game sources do not come with the hiscore file, we have to create it
# this will result in empty hiscore table, but it is not such a big deal
mkdir -p %{buildroot}%{_localstatedir}/games
touch %{buildroot}%{_localstatedir}/games/%{name}.sco
# add icon and .desktop file
mkdir -p -m 0755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert data/abicon.bmp %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/vodovod.xpm
desktop-file-install  \
	--dir=%{buildroot}%{_datadir}/applications %{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc CHANGES COPYING html
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%config(noreplace) %attr (0664,root,games) %{_localstatedir}/games/%{name}.sco


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10r22-26
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Bruno Wolff III <bruno@wolff.to> - 1.10r22-16
- Automate font path finding during build

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 09 2016 Karel Volný <kvolny@redhat.com> 1.10r22-7
- Fixed rpmlint warnings about macros
- For rpmlint errors, see bug #1305794

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10r22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.10r22-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Karel Volný <kvolny@redhat.com> 1.10r22-1
- New development snapshot
- Adds Chinese, Serbian and Swedish translations
- Added patch to update Czech and to add Slovak translations
- Added Slovak %%description
- Added patch for bug #1037377

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.10r19-11
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-9
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.10r19-5
- Build with $RPM_OPT_FLAGS.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10r19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Karel Volny <kvolny@redhat.com> 1.10r19-3
- Required font package got renamed to dejavu-sans-mono-fonts (bug #480478)

* Thu Jan 15 2009 Karel Volny <kvolny@redhat.com> 1.10r19-2
- Use dejavu-fonts-sans-mono instead of bundling the font file (bug #477480)

* Thu Dec 11 2008 Karel Volny <kvolny@redhat.com> 1.10r19-1
- Added coreutils to post(un) (fixes bug #475921)
- New version requires SDL_ttf-devel

* Wed Mar 05 2008 Karel Volny <kvolny@redhat.com> 1.10r13-1
- development version
- Removed gcc43 patch (fixed upstream)
- Removed wrapper stuff and harcoded paths, upstream now uses variables
- Use hiscore file %%{_localstatedir}/games/%%{name}.sco
- Added language files handling
- Added Czech localisation

* Mon Feb 04 2008 Karel Volny <kvolny@redhat.com> 1.10-2
- Some fixes as per bug #428973:
- Fixed summary
- Added gtk-update-icon-cache
- Added patch to compile with gcc 4.3
- Modified compiler flags

* Wed Jan 16 2008 Karel Volny <kvolny@redhat.com> 1.10-1
- Initial release
