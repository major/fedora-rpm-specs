%global __pytest xwfb-run -- pytest
%global app_id  io.github.fract4d

Name:           gnofract4d
Version:        4.4
Release:        %autorelease
Summary:        Gnofract 4D is a Gnome-based program to draw fractals
License:        BSD-3-Clause

URL:            https://fract4d.github.io/gnofract4d/
Source0:        https://github.com/fract4d/gnofract4d/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{app_id}.metainfo.xml

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  rsvg-pixbuf-loader
BuildRequires:  meson
BuildRequires:  gtk4
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  python3-devel
# -base is not enough, need gi._gi_cairo for tests
BuildRequires:  gobject-introspection
BuildRequires:  python3-gobject
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  xwayland-run

Requires:       gcc
Requires:       hicolor-icon-theme
Requires:       libgcc%{?_isa}
Requires:       glibc-devel%{?_isa}
Requires:       python3-gobject
Requires:       gobject-introspection
Requires:       gtk4

%description
Gnofract 4D is a free, open source program which allows anyone to create
beautiful images called fractals.  The images are automatically created
by the computer based on mathematical principles.  These include the
Mandelbrot and Julia sets and many more.  You don't need to do any math:
you can explore a universe of images just using a mouse.

%prep
%autosetup -p1

# fix python installation
sed -i -e 's|pymod\.find_installation(|&pure: false|' meson.build

# Fix the desktop file
sed -e "s/Categories.*/Categories=Graphics;GTK;GNOME;Education;Science;Math;/" \
    -e "s/MimeType.*/&;/" \
    -i.orig %{app_id}.desktop
touch -r %{app_id}.desktop.orig %{app_id}.desktop
rm %{app_id}.desktop.orig

%build
%meson -Dstrip=false
%meson_build

%install
%meson_install

# Check the desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

# Remove the shebangs
for fil in `find %{buildroot}%{python3_sitearch} -perm 644 -name '*.py'`; do
  sed '\|^#!/usr/bin.*python|d' $fil > $fil.new
  touch -r $fil $fil.new
  mv -f $fil.new $fil
done

# Remove duplicated docs
rm -rf %{buildroot}%{_docdir}/%{name}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/%{name}.1 %{buildroot}%{_mandir}/man1

%check
# The test_main_window test hangs in mock
%pytest -v --ignore fract4dgui/tests/test_main_window.py

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitearch}/fract4d*
%{_datadir}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/mime/packages/%{name}-mime.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}*
%{_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
