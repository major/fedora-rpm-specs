Name:		mindless
Version:	1.0.0
Release:	%autorelease
Summary:	Find the secret code
Summary(de):	Finden Sie den Geheimcode
Summary(sv):	Hitta den hemliga koden

License:	GPL-2.0-or-later
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
%autosetup -p 0

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
%autochangelog
