Name:           Maelstrom
Version:        3.0.7
Release:        %autorelease
Summary:        A space combat game

# See Maelstrom-Content-License.txt for details on the updated content licensing
License:        GPL-2.0-or-later AND CC-BY-3.0
URL:            http://www.libsdl.org/projects/Maelstrom/
Source0:        http://www.libsdl.org/projects/Maelstrom/src/Maelstrom-%{version}.tar.gz
Source1:        maelstrom.png
Source2:        Maelstrom.desktop
Source3:        Maelstrom-Content-License.txt
Source4:        Maelstrom.appdata.xml
Patch:          setgid.patch
Patch:          gcc34.patch
Patch:          64bit.patch
Patch:          install.patch
Patch:          gcc5.patch
Patch:          netd-c99.patch
Patch:          Makefile.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:      make
BuildRequires:      gcc-c++
BuildRequires:      SDL2_net-devel, desktop-file-utils, libtool
Requires(post):     coreutils
Requires(postun):   coreutils

%description
Maelstrom is a space combat game, originally ported from the Macintosh 
platform. Brave pilots get to dodge asteroids and fight off other ships 
at the same time.


%prep
%autosetup -p1
cp %{SOURCE3} .


%build
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-write-strings"
%configure
make %{?_smp_mflags}


%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE2}

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_bindir}/{Maelstrom-netd,macres,playwave,snd2wav}

mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

mkdir -p -m 755 %{buildroot}%{_datadir}/appdata
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/appdata

find %{buildroot} -name "Makefile*" -exec rm -f {} \;


%files
%doc CREDITS.txt README* Changelog Docs
%license Maelstrom-Content-License.txt COPYING*
%attr(2755,root,games) %{_bindir}/Maelstrom
%{_datadir}/Maelstrom
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/appdata/Maelstrom.appdata.xml
%ghost %config(noreplace) %attr(0664,root,games) %{_localstatedir}/lib/games/Maelstrom-Scores


%changelog
%autochangelog
