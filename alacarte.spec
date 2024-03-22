Name:           alacarte
Version:        3.52.0
Release:        %autorelease
Summary:        Menu editor for the GNOME desktop
License:        LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/alacarte
Source0:        https://download.gnome.org/sources/alacarte/3.52/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(libgnome-menu-3.0) >= 3.5.3
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel

Requires:       gnome-menus >= 3.5.3
Requires:       gtk3
Requires:       python3-gobject


%description
Alacarte is a graphical menu editor that lets you edit, add, and delete
menu entries. It follows the freedesktop.org menu specification and
should work with any desktop environment that uses this specification.


%prep
%autosetup -p1
autoreconf -i -f


%build
%configure
%make_build


%install
%make_install

desktop-file-install \
  --delete-original \
  --add-only-show-in=GNOME \
  --remove-not-show-in=KDE \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS NEWS
%{python3_sitelib}/Alacarte
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_mandir}/man1/*.1*


%changelog
%autochangelog
