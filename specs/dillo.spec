%bcond_without tests

# Workaround for GCC 10
# * https://gcc.gnu.org/gcc-10/porting_to.html#common
%define _legacy_common_support 1

Name:           dillo
Version:        3.2.0
Release:        %autorelease
Summary:        A multi-platform graphical web browser

License:        GPL-3.0-or-later
URL:            https://dillo-browser.github.io/
Source0:        https://github.com/%{name}-browser/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  cmake(fltk) >= 1.3.0
BuildRequires:  cmake(libjpeg-turbo)
BuildRequires:  cmake(NanoSVG)
BuildRequires:  cmake(WebP)
BuildRequires:  pkgconfig(libpng) >= 1.2.0
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(zlib)
%if %{with tests}
BuildRequires:  ImageMagick
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xwd
BuildRequires:  xwininfo
%endif

Requires:       hicolor-icon-theme
Requires:       wget%{?_isa}

Provides:       webclient

%description
Dillo is a multi-platform graphical web browser, known for its speed and small
footprint, that is developed with a focus on personal security and privacy. It
is built with the FLTK 1.3 GUI toolkit.


%prep
%autosetup
autoreconf -vif

%build
%configure \
    --disable-dependency-tracking \
    --enable-ipv6 \
    --enable-tls \
    %if %{with tests}
    --enable-html-tests \
    %endif
    %{nil}
%make_build


%install
%make_install
rm -f doc/Makefile*

# included with doc
rm -fr %{buildroot}%{_datadir}/doc/%{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc AUTHORS README.md ChangeLog doc/ NEWS
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/%{name}-install-hyphenation
%{_bindir}/dpid
%{_bindir}/dpidc
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_libdir}/%{name}/
%{_mandir}/man1/*.1*


%changelog
%autochangelog
