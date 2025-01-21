Name: seahorse-adventures
Summary: Help barbie the seahorse float on bubbles to the moon
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later

Version: 1.4
Release: 8%{?dist}

URL: http://www.imitationpickles.org/barbie/

%global git_tag Release-%{version}
Source0: https://github.com/dulsi/seahorse-adventures/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme
Requires: python3-pygame

# Game can work without Gamerzilla, so let's not make it a hard requirement
Recommends: pylibgamerzilla

%global fontlist font(bitstreamverasans)
BuildRequires: fontconfig
BuildRequires: %{fontlist}
Requires: %{fontlist}


%description
Help barbie the seahorse float on bubbles to the moon. This is a retro-side
scroller game. It won the teams category in pyweek 4. Includes original
soundtrack, graphics, and 15 levels!


%prep
%autosetup -p1 -n %{name}-%{git_tag}
sed \
	-e 's|#![ ]*/usr/bin/python|#!%{_bindir}/python3|' \
	-e 's|#![ ]*/usr/bin/env python|#!%{_bindir}/python3|' \
	-i create-upload.py leveledit.py run_game.py tileedit.py


%build
# nothing to build, pure python code only


%install
install -m 755 -d %{buildroot}%{_datadir}/%{name}
install -m 755 -p leveledit.py run_game.py tileedit.py %{buildroot}%{_datadir}/%{name}/
cp -a data/ lib/ %{buildroot}%{_datadir}/%{name}

VERA_PATH="$(fc-match -f "%%{file}" "Bitstream Vera Sans")"
find %{buildroot}%{_datadir}/%{name}/ -name 'Vera.ttf' \
	-exec ln -sf "${VERA_PATH}" '{}' ';'

install -m 755 -d %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/run_game.py %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p ./%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p ./%{name}.metainfo.xml %{buildroot}%{_metainfodir}/

for ICON_SIZE in 32 64 128; do
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/apps"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "./icon${ICON_SIZE}.png" "${ICON_DIR}/%{name}.png"
done


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%doc CHANGES.txt LEVELS.txt NOTES.txt README.txt TODO.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.4-1
- Update to v1.4
- Drop Source1 (desktop file - now provided by upstream)
- Drop Source2 (AppStream metainfo file - now provided by upstream)
- Drop Patch1 (Python syntax errors at runtime - fixed upstream)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3-1
- Update to v1.3
- Drop Patch0 (support for symlinked executable - fixed upstream)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 19 2020 Artur Iwicki <fedora@svgames.pl> - 1.2-2
- Use fc-match to find font locations instead of hard-coding paths

* Sun May 10 2020 Artur Iwicki <fedora@svgames.pl> - 1.2-1
- Update to v.1.2
- Fix license in AppData file, add OARS info

* Sat May 02 2020 Artur Iwicki <fedora@svgames.pl> - 1.1-3.20200502git0f342d34
- Switch the main source to a Python3 fork

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Hans de Goede <hdegoede@redhat.com> 1.1-1
- New upstream release 1.1 (rhbz#1510103)
- Fix FTBFS (rhbz#1675983)
- Add appdata

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-19
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-12
- Remove --vendor from desktop-file-install in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep  9 2010 Hans de Goede <hdegoede@redhat.com> 1.0-7
- Fix FTBFS (#631296)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Hans de Goede <hdegoede@redhat.com> 1.0-4
- Adjust font requires for font rename (rh 480472)

* Sat Dec 27 2008 Hans de Goede <hdegoede@redhat.com> 1.0-3
- Replace included vera font copies with symlinks to dejavu (rh 477456)

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-2
- Update License tag for new Licensing Guidelines compliance

* Wed Apr 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-1
- Initial Fedora Extras package
