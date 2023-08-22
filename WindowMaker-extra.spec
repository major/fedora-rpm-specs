Name:           WindowMaker-extra
Version:        0.1
Release:        %autorelease
Summary:        Extra icons and themes for WindowMaker

License:        GPL-2.0-only
URL:            http://www.windowmaker.org
Source0:        http://windowmaker.org/pub/source/release/WindowMaker-extra-0.1.tar.gz
BuildArch:      noarch

BuildRequires:  make
Requires:       WindowMaker

%description
This is the extra data package for Window Maker. For now it only contains some
icons and a few themes.

%prep
%autosetup

%build
%configure

%install
%make_install

%files
%doc COPYING README
%{_datadir}/WindowMaker/Icons/Ant.xpm
%{_datadir}/WindowMaker/Icons/Antennae.xpm
%{_datadir}/WindowMaker/Icons/Bee48x48.xpm
%{_datadir}/WindowMaker/Icons/Beer.xpm
%{_datadir}/WindowMaker/Icons/Bird.xpm
%{_datadir}/WindowMaker/Icons/Book.xpm
%{_datadir}/WindowMaker/Icons/Bookshelf.xpm
%{_datadir}/WindowMaker/Icons/Brain.xpm
%{_datadir}/WindowMaker/Icons/BulletHole.xpm
%{_datadir}/WindowMaker/Icons/CashRegister.xpm
%{_datadir}/WindowMaker/Icons/Clipboard.xpm
%{_datadir}/WindowMaker/Icons/Cola.xpm
%{_datadir}/WindowMaker/Icons/ColorGNU.xpm
%{_datadir}/WindowMaker/Icons/Correspondence.dir.xpm
%{_datadir}/WindowMaker/Icons/CrystalSkull.dir.xpm
%{_datadir}/WindowMaker/Icons/Daemon.xpm
%{_datadir}/WindowMaker/Icons/Detergent.dir.xpm
%{_datadir}/WindowMaker/Icons/DoomII.xpm
%{_datadir}/WindowMaker/Icons/Draw.xpm
%{_datadir}/WindowMaker/Icons/EscherCube.xpm
%{_datadir}/WindowMaker/Icons/EscherTriangle.xpm
%{_datadir}/WindowMaker/Icons/Fish5.dir.xpm
%{_datadir}/WindowMaker/Icons/Football.xpm
%{_datadir}/WindowMaker/Icons/FootballUS.xpm
%{_datadir}/WindowMaker/Icons/Gear.xpm
%{_datadir}/WindowMaker/Icons/Ghost.xpm
%{_datadir}/WindowMaker/Icons/HP-16C-48.xpm
%{_datadir}/WindowMaker/Icons/HandOpen.xpm
%{_datadir}/WindowMaker/Icons/HandPointing.xpm
%{_datadir}/WindowMaker/Icons/HandPointingLeft.xpm
%{_datadir}/WindowMaker/Icons/HandPunch.xpm
%{_datadir}/WindowMaker/Icons/HandReach.xpm
%{_datadir}/WindowMaker/Icons/HeroSandwich.dir.xpm
%{_datadir}/WindowMaker/Icons/LadyBug48x48.xpm
%{_datadir}/WindowMaker/Icons/Microphone.xpm
%{_datadir}/WindowMaker/Icons/Netscape.xpm
%{_datadir}/WindowMaker/Icons/NewsAgent.xpm
%{_datadir}/WindowMaker/Icons/PDF.xpm
%{_datadir}/WindowMaker/Icons/Padlock.xpm
%{_datadir}/WindowMaker/Icons/Paint.xpm
%{_datadir}/WindowMaker/Icons/Pencils.24.xpm
%{_datadir}/WindowMaker/Icons/Penguin.xpm
%{_datadir}/WindowMaker/Icons/Radio.xpm
%{_datadir}/WindowMaker/Icons/Reference.xpm
%{_datadir}/WindowMaker/Icons/Rumi.xpm
%{_datadir}/WindowMaker/Icons/Snail.xpm
%{_datadir}/WindowMaker/Icons/T2-Film.xpm
%{_datadir}/WindowMaker/Icons/TagIcon.xpm
%{_datadir}/WindowMaker/Icons/TapeIcon1.xpm
%{_datadir}/WindowMaker/Icons/TrueDie48.xpm
%{_datadir}/WindowMaker/Icons/WheelbarrowFull.xpm
%{_datadir}/WindowMaker/Icons/WordEditor.xpm
%{_datadir}/WindowMaker/Icons/Wrench-12bit.xpm
%{_datadir}/WindowMaker/Icons/bomb2.xpm
%{_datadir}/WindowMaker/Icons/inspect.xpm
%{_datadir}/WindowMaker/Icons/monitor.xpm
%{_datadir}/WindowMaker/Icons/paint.xpm
%{_datadir}/WindowMaker/Icons/tile.black.xpm
%{_datadir}/WindowMaker/Icons/tile.snow.xpm
%{_datadir}/WindowMaker/Icons/tile.xpm
%{_datadir}/WindowMaker/Icons/tile2.xpm
# included with WindowMaker
%exclude %{_datadir}/WindowMaker/Icons/xv.xpm
%{_datadir}/WindowMaker/Themes/Checker.themed/
%{_datadir}/WindowMaker/Themes/LeetWM.themed/
%{_datadir}/WindowMaker/Themes/Night.themed/
%{_datadir}/WindowMaker/Themes/STEP2000.themed/



%changelog
%autochangelog
