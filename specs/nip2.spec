Name:           nip2
Version:        8.9.1
Release:        %autorelease
Summary:        Interactive tool for working with large images

License:        GPL-2.0-or-later
URL:            https://libvips.github.io/libvips/
Source0:        https://github.com/libvips/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Do not re-declare statfs(), declare function arguments
# FTBFS https://bugzilla.redhat.com/show_bug.cgi?id=2340934
Patch0:         https://github.com/libvips/nip2/pull/123.patch
# Fix void value error in IM_FREEF with GCC 15
Patch1:         nip2-IM_FREEF.patch

BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnome-icon-theme-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(vips)
BuildRequires:  shared-mime-info
BuildRequires:  xdg-utils

# description taken from Debian package
%description
nip2 is a graphical front end to the VIPS package.
With nip2, rather than directly editing images, you build
relationships between objects in a spreadsheet-like fashion. When you
make a change somewhere, nip2 recalculates the objects affected by
that change. Since it is demand-driven this update is very fast, even
for very, very large images. nip2 is very good at creating pipelines
of image manipulation operations. It is not very good for image
editing tasks like touching up photographs. For that, a tool like the
GIMP should be used instead.


%prep
%autosetup -p1


%build
%configure --disable-update-desktop
%make_build


%install
%make_install

# AppStream spec changed its install directory
mv %{buildroot}%{_datadir}/appdata %{buildroot}%{_datadir}/metainfo

# delete doc (we will get it later)
rm -rf %{buildroot}%{_datadir}/doc/nip2

# locale stuff
%find_lang %{name}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cp -a share/nip2/data/vips-128.png \
        %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/nip2.png


%check
# metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/nip2.appdata.xml

# desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/nip2.desktop

%files -f %{name}.lang
%doc doc/html doc/pdf AUTHORS ChangeLog NEWS THANKS TODO
%license COPYING
%{_bindir}/nip2
%{_datadir}/nip2
%{_mandir}/man1/nip2.1*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/nip2.appdata.xml
%{_datadir}/applications/nip2.desktop
%{_datadir}/mime/packages/nip2.xml


%changelog
%autochangelog
