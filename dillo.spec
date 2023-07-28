# Workaround for GCC 10
# * https://gcc.gnu.org/gcc-10/porting_to.html#common
%define _legacy_common_support 1

Name:           dillo
Version:        3.0.5
Release:        %autorelease
Summary:        Very small and fast GUI web browser

License:        GPLv3+
URL:            https://www.dillo.org
Source0:        %{url}/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-openssl.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel >= 1.3.0
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libjpeg-devel = 6b
BuildRequires:  libpng-devel >= 1.2.0
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  zlib-devel

Requires:       wget%{?_isa}

# #676710 dillo requires iso8859 fonts
Requires:       xorg-x11-fonts-ISO8859-1-100dpi
Requires:       xorg-x11-fonts-ISO8859-1-75dpi

Provides:       webclient

%description
Dillo is a very small and fast web browser using GTK. Currently: no frames,
https, javascript.


%prep
%setup -q
%patch 0 -p1 -b.dso
autoreconf -vif

%build
%configure --disable-dependency-tracking --enable-ipv6 --enable-ssl
%make_build


%install
%make_install
rm -f doc/Makefile*

%{__install} -d -m 0755 %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%{__install} -Dp -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# included with doc
rm -fr %{buildroot}%{_datadir}/doc/%{name}

# silence rpmlint and convert to utf8
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
pushd doc
iconv -f iso8859-1 -t utf-8 Cache.txt > Cache.txt.conv && mv -f Cache.txt.conv Cache.txt
iconv -f iso8859-1 -t utf-8 Cookies.txt > Cookies.txt.conv && mv -f Cookies.txt.conv Cookies.txt
popd


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc AUTHORS README ChangeLog doc/
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/%{name}-install-hyphenation
%{_bindir}/dpid
%{_bindir}/dpidc
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_libdir}/%{name}/
%{_mandir}/man1/*.1*


%changelog
%autochangelog
