Name:           links
Version:        2.30
Release:        %autorelease
Epoch:          1
Summary:        Web browser running in both graphics and text mode
License:        GPL-2.0-or-later
URL:            https://links.twibright.com/
Source0:        https://links.twibright.com/download/%{name}-%{version}.tar.bz2
Source1:        links.desktop
Patch0:         links-gcc16.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gpm-devel
BuildRequires:  libavif-devel
BuildRequires:  libevent-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives
Requires(preun): %{_sbindir}/alternatives

Provides:       webclient


%description
Links is a web browser capable of running in either graphics or text mode.
It provides a pull-down menu system, renders complex pages, has partial HTML
4.0 support (including tables, frames and support for multiple character sets
and UTF-8), supports color and monochrome terminals and allows horizontal
scrolling.


%prep
%autosetup


%build
iconv -f ISO-8859-1 -t UTF-8 AUTHORS >converted.AUTHORS
touch -r AUTHORS converted.AUTHORS
mv converted.AUTHORS AUTHORS

%configure --enable-graphics --with-ssl
%make_build


%install
%make_install
mv %{buildroot}/%{_bindir}/links $RPM_BUILD_ROOT/%{_bindir}/links2
mv %{buildroot}/%{_mandir}/man1/links.1 $RPM_BUILD_ROOT/%{_mandir}/man1/links2.1
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
install -D -p Links_logo.png %{buildroot}/%{_datadir}/pixmaps/links.png


%postun
[ $1 = 0 ] && exit 0
[ $(readlink %{_sysconfdir}/alternatives/links) = %{_bindir}/links2 ] &&
        %{_sbindir}/alternatives --set links %{_bindir}/links2
exit 0


%preun
[ $1 = 0 ] || exit 0
%{_sbindir}/alternatives --remove links %{_bindir}/links2


%post
%{_sbindir}/alternatives \
        --install %{_bindir}/links links %{_bindir}/links2 80 \
        --slave %{_mandir}/man1/links.1.gz links-man %{_mandir}/man1/links2.1.gz
[ $(readlink %{_sysconfdir}/alternatives/links) = %{_bindir}/links2 ] &&
        %{_sbindir}/alternatives --set links %{_bindir}/links2
exit 0


%files
%doc doc/* AUTHORS KEYS README COPYING
%{_bindir}/links2
%{_mandir}/man1/links2.1*
%{_datadir}/pixmaps/links.png
%{_datadir}/applications/links.desktop
%ghost %attr(0755,root,root) %{_bindir}/links
%ghost %attr(0644,root,root) %{_mandir}/man1/links.1.gz


%changelog
%autochangelog
