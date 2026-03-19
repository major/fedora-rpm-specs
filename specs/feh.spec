Name:           feh
Version:        3.11.3
Release:        %autorelease
Summary:        Fast command line image viewer using Imlib2
License:        MIT
URL:            https://feh.finalrewind.org
Source0:        https://feh.finalrewind.org/%{name}-%{version}.tar.bz2
Patch0:         feh-1.10.1-dejavu.patch

BuildRequires:  gcc
BuildRequires:  imlib2-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  perl-Test-Command
BuildRequires:  perl-Test-Harness

Requires:       dejavu-sans-fonts

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slide-show or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
%autosetup -p1

%build
# Propagate values into config.mk
sed -i \
  -e "s|^doc_dir =.*$|doc_dir = \$(DESTDIR)%{_pkgdocdir}|" \
  -e "s|^example_dir =.*$|example_dir = \$(doc_dir)/examples|" \
  config.mk

%set_build_flags
%make_build PREFIX="%{_prefix}" VERSION="%{version}" \
    curl=1 exif=1 test=1 xinerama=1

%install
%make_install PREFIX="%{_prefix}"

rm -f %{buildroot}%{_datadir}/%{name}/fonts/yudit.ttf
find %{buildroot} -type f -name "*.la" -delete
rm -f %{buildroot}%{_pkgdocdir}/examples/find-lowres

%check
%make_build test

%files
%license COPYING
%{_pkgdocdir}/
%{_bindir}/feh
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/feh.1*
%{_datarootdir}/icons/hicolor/48x48/apps/feh.png
%{_datarootdir}/icons/hicolor/scalable/apps/feh.svg

%changelog
%autochangelog
