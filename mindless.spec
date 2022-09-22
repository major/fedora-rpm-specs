Name:		mindless
Version:	1.0.0
Release:	32%{?dist}
Summary:	Find the secret code
Summary(de):	Finden Sie den Geheimcode
Summary(sv):	Hitta den hemliga koden

License:	GPLv2+
# This URL no longer works.  It is the last known place
Source0:	http://www.lysator.liu.se/~mbrx/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.6
Source3:	http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Source4:	%{name}.appdata.xml
Patch:		%{name}.fontconfig.patch

BuildRequires: make
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:  gcc-c++
BuildRequires:	fontconfig-devel
BuildRequires:	desktop-file-utils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  libappstream-glib

Requires:	gnu-free-sans-fonts

%global desktopdir %{_datadir}/applications
%global icontop %{_datadir}/icons/hicolor

%description
Mindless is a simple game for two players using the rules of Mastermind.
You can play in human vs. human, human vs. computer or computer
vs. computer mode.  The goal of the game is to crack a secret code
consisting of four balls which can each be one of eight colors.

%description -l de
Mindless ist ein kleines Spiel für zwei Teilnehmer, das nach den Regeln
von Mastermind gespielt wird. Die Kombinationen Mensch gegen Mensch,
Mensch gegen Rechner oder Rechner gegen Rechner sind möglich.  Ziel
des Spiels ist es, einen durch vier verschieden farbige Kugeln
dargestellten Geheimcode zu knacken.

%description -l sv
Mindless är ett enkelt spel för två spelare som använder reglerna för
Mastermind.  Du kan spela i lägena människa mot människa, människa mot
dator eller dator mot dator.  Spelets mål är att avslöja en hemlig kod
som består av fyra kulor som var och en kan ha en av åtta färger.

%prep
%setup -q
%patch

%build
autoreconf --install
%configure
make %{?_smp_mflags}
# Use a version of the GPL with a current address.
cp -p %{SOURCE3} COPYING

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{desktopdir}
# Use system version of the FreeSans font, rather than bundling one.
rm -r %{buildroot}/%{_datadir}/%{name}/fonts
desktop-file-install --dir=%{buildroot}%{desktopdir} %{SOURCE1}
for res in 32x32 48x48 64x64
do  install -d %{buildroot}%{icontop}/$res/apps
    cp -p share/icons/%{name}-$res.png \
	  %{buildroot}%{icontop}/$res/apps/%{name}.png
done
install -d %{buildroot}%{_mandir}/man6 %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE2} %{buildroot}%{_mandir}/man6
cp -p %{SOURCE4} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/mindless.appdata.xml

%files
%doc ChangeLog COPYING NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{desktopdir}/%{name}.desktop
%{icontop}/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Göran Uddeborg <goeran@uddeborg.se> - 1.0.0-23
- Add an explicit build requirement on gcc.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-21
- Remove obsolete scriptlets

* Sun Sep 17 2017 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-20
- Appdata added.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 19 2014 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-11
- With current "autoreconf", an --install option is obviously also needed.

* Mon Jan  6 2014 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-10
- The URL is dead.  According to the author, there is no replacement.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-8
- Run autoreconf to add support for aarch64 (Bz 926147)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 21 2011 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-4
- German summary and description provided by 
  Mario Blättermann <mariobl@freenet.de>.
- Reconfigure using automake 1.7 instead of 1.6.  The latter has been removed
  in Fedora 16.

* Sat Aug 20 2011 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-3
- Add braces around the names of all variable-like macros.

* Mon Aug 15 2011 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-2
- Remove defattr declaration.
- Provide a manual page based on the README file.
- Use fontconfig to find the system version of FreeSans, and use that instead
  of the bundled.
- Update the COPYING document with one from FSF with their current address.

* Fri Aug 12 2011 Göran Uddeborg <goeran@uddeborg.se> 1.0.0-1
- First RPM packaging.
