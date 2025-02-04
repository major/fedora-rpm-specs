Name:		nip2
Version:	8.9.1
Release:	%autorelease
Summary:	Interactive tool for working with large images

License:	GPL-2.0-or-later
URL:		https://libvips.github.io/libvips/
Source0:	https://github.com/libvips/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Do not re-declare statfs(), declare function arguments
# FTBFS https://bugzilla.redhat.com/show_bug.cgi?id=2340934
Patch0:         https://github.com/libvips/nip2/pull/123.patch

BuildRequires: make
BuildRequires:	pkgconfig(vips)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(libgvc)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	gcc
BuildRequires:	shared-mime-info gnome-icon-theme-devel
BuildRequires:	flex bison intltool gettext
BuildRequires:	desktop-file-utils xdg-utils
BuildRequires:	libappstream-glib


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
mv $RPM_BUILD_ROOT%{_datadir}/appdata $RPM_BUILD_ROOT%{_datadir}/metainfo

# delete doc (we will get it later)
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/nip2

# locale stuff
%find_lang nip2

# icon
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
cp -a share/nip2/data/vips-128.png	\
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/nip2.png


%check
# metainfo
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/nip2.appdata.xml

# desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/nip2.desktop

%files -f nip2.lang
%doc doc/html doc/pdf AUTHORS ChangeLog NEWS THANKS TODO
%license COPYING
%{_bindir}/nip2
%{_datadir}/nip2
%{_mandir}/man1/nip2.1.gz
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/nip2.appdata.xml
%{_datadir}/applications/nip2.desktop
%{_datadir}/mime/packages/nip2.xml


%changelog
%autochangelog
