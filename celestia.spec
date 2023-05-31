#%%global gittag 1.6.2
%global commit 7cf93d9a8cb193ee11aec0f0f0cd86be022190be
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230515

Name:           celestia
%if "%{?gittag}"
Version:        1.6.2
%else
Version:        1.7.0~%{date}%{shortcommit}
%endif
Release:        %autorelease
Summary:        OpenGL real-time visual space simulation
# Bundled R128 is under Unlicense
License:        GPL-2.0-or-later AND MIT AND Unlicense
URL:            https://celestia.space/
%if "%{?gittag}"
Source0:        https://github.com/CelestiaProject/Celestia/archive/%{gittag}/Celestia-%{version}.tar.gz
%else
Source0:        https://github.com/CelestiaProject/Celestia/archive/%{commit}/Celestia-%{shortcommit}.tar.gz
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  ImageMagick

BuildRequires:  ffmpeg-free-devel
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
%ifarch x86_64 aarch64
BuildRequires:  pkgconfig(luajit)
%else
BuildRequires:  pkgconfig(lua)
%endif

Provides:       bundled(r128) = 1.6.0


%description
Celestia is a real-time space simulation which lets you experience the
universe in three dimensions. Celestia does not confine you to the
surface of the Earth, it allows you to travel throughout the solar
system, to any of over 100,000 stars, or even beyond the galaxy.

Travel in Celestia is seamless; the exponential zoom feature lets
you explore space across a huge range of scales, from galaxy clusters
down to spacecraft only a few meters across. A 'point-and-goto'
interface makes it simple to navigate through the universe to the
object you want to visit.


%package        common
Summary:        Common files for %{name}
Requires:       celestia-data
Requires:       google-noto-sans-fonts

Obsoletes:      %{name} < 1.6.3

%description    common
This package provides files common to all GUIs for %{name}.


%package        qt
Summary:        QT interface for %{name}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

%description    qt
This package provides the QT GUI for %{name}.


%package        gtk
Summary:        GTK interface for %{name}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

Provides:       %{name} = %{version}-%{release}

BuildRequires:  cairo-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkglext-devel

%description    gtk
This package provides the GTK GUI for %{name}.


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n Celestia-%{commit} -p1
%endif

# Change default config
sed -i 's|# LeapSecondsFile "|LeapSecondsFile "|g' celestia.cfg
sed -i 's|DejaVuSans.ttf,9"|%{_datadir}/fonts/google-noto/NotoSans-Regular.ttf,9"|g' celestia.cfg
sed -i 's|DejaVuSans-Bold.ttf,15"|%{_datadir}/fonts/google-noto/NotoSans-Bold.ttf,15"|g' celestia.cfg


%build
%cmake -DENABLE_DATA=ON \
       -DENABLE_QT5=OFF \
       -DENABLE_QT6=ON \
       -DENABLE_GTK=ON \
       -DENABLE_FFMPEG=ON \
       -DENABLE_LIBAVIF=ON \
       -DUSE_WAYLAND=ON \
       -DGIT_COMMIT="%{shortcommit}"
#       -DENABLE_GLES=ON \ Disabled due to missing support on QT
#       -DUSE_GTK3=ON \ is broken

%cmake_build

# create standard size icons
convert src/celestia/qt/Celestia.ico hi-apps-celestia.png


%install
%cmake_install

# fix icon name used in GTK app
mv %{buildroot}%{_datadir}/pixmaps/celestia{,-logo}.png
# use standard size and location for desktop icons
for f in hi-apps-celestia-*.png ; do
  d=$(identify -format "%wx%h" $f) ;
  install -D -m0644 $f %{buildroot}%{_datadir}/icons/hicolor/$d/apps/celestia.png ;
done

%find_lang %{name} --all-name

rm %{buildroot}%{_datadir}/celestia/COPYING

# Use system provided fonts
rm -Rf %{buildroot}%{_datadir}/%{name}/fonts


%check
# Menu entry
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-{gtk,qt6}.desktop

# Appdata file check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/space.%{name}.%{name}_{gtk,qt6}.metainfo.xml


# No file in the main celestia package
# it's just a metapackage to provide a clean upgrade path from celestia < 1.7
# requiring by default celestia-gtk

%files common -f %{name}.lang
%doc AUTHORS ChangeLog README coding-standards.html
%doc CONTRIBUTING.md devguide.txt
%license COPYING
%{_libdir}/lib%{name}.so.1.7*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}-logo.png
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/help

%files qt
%{_bindir}/%{name}-qt6
%{_mandir}/man1/%{name}-qt6.1*
%{_datadir}/metainfo/space.%{name}.%{name}_qt6.metainfo.xml
%{_datadir}/applications/%{name}-qt6.desktop

%files gtk
%{_bindir}/%{name}-gtk
%{_mandir}/man1/%{name}-gtk.1*
%{_datadir}/metainfo/space.%{name}.%{name}_gtk.metainfo.xml
%{_datadir}/applications/%{name}-gtk.desktop

%files doc
%{_datadir}/%{name}/help


%changelog
%autochangelog
