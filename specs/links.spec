Name:           links
Version:        2.30
Release:        %autorelease
Epoch:          1
Summary:        Web browser running in both graphics and text mode
License:        GPL-2.0-or-later
URL:            https://links.twibright.com/
Source0:        https://links.twibright.com/download/%{name}-%{version}.tar.bz2
Source1:        links.desktop
Patch:          links-gcc16.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gpm-devel
BuildRequires:  libavif-devel
BuildRequires:  libevent-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

Provides:       webclient

%description
Links is a web browser capable of running in either graphics or text mode.
It provides a pull-down menu system, renders complex pages, has partial HTML
4.0 support (including tables, frames and support for multiple character sets
and UTF-8), supports color and monochrome terminals and allows horizontal
scrolling.

%prep
%autosetup -p1
iconv -f ISO-8859-1 -t UTF-8 AUTHORS >converted.AUTHORS
touch -r AUTHORS converted.AUTHORS
mv converted.AUTHORS AUTHORS

%build
%configure --enable-graphics --with-ssl
%make_build

%install
%make_install
mv %{buildroot}%{_bindir}/links %{buildroot}%{_bindir}/links2
mv %{buildroot}%{_mandir}/man1/links.1 %{buildroot}%{_mandir}/man1/links2.1
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -D -p Links_logo.png %{buildroot}%{_datadir}/pixmaps/links.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/links.desktop

%post
for ext in .gz .zst .bz2 .xz ""; do
  if [ -f %{_mandir}/man1/links2.1${ext} ]; then
    %{_sbindir}/update-alternatives \
      --install %{_bindir}/links links %{_bindir}/links2 80 \
      --slave %{_mandir}/man1/links.1${ext} links-man %{_mandir}/man1/links2.1${ext}
    break
  fi
done

%preun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove links %{_bindir}/links2
fi

%files
%license COPYING
%doc doc/* AUTHORS KEYS README
%{_bindir}/links2
%{_mandir}/man1/links2.1*
%{_datadir}/pixmaps/links.png
%{_datadir}/applications/links.desktop
%ghost %{_bindir}/links
%ghost %{_mandir}/man1/links.1*

%changelog
%autochangelog
