# PackIt can't access this repo without opening the firewall
# global forgeurl https://git.skyjake.fi/gemini/lagrange
%global forgeurl https://github.com/skyjake/lagrange
%global appid fi.skyjake.Lagrange

# Ensure we are not built and installed with a too-old the_Foundation
%global min_foundation_ver 1.7.0

# this seems buggy on Wayland: see https://github.com/skyjake/lagrange/issues/575
%bcond_with x11_xlib

Name:           lagrange
Version:        1.17.6
Release:        %autorelease
Summary:        A Beautiful Gemini Client

License:        BSD-2-Clause
URL:            https://gmi.skyjake.fi/lagrange/
# Source:         %%{forgeurl}/releases/download/v%%{version}/%%{name}-%%{version}.tar.gz
Source:         %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(the_Foundation) >= %{min_foundation_ver}
# for checks
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       the_foundation%{_isa} >= %{min_foundation_ver}

%description
Lagrange is a desktop GUI client for browsing Geminispace. It offers modern
conveniences familiar from web browsers, such as smooth scrolling, inline image
viewing, multiple tabs, visual themes, Unicode fonts, bookmarks, history, and
page outlines.

Like Gemini, Lagrange has been designed with minimalism in mind. It depends on a
small number of essential libraries. It is written in C and uses SDL for
hardware-accelerated graphics. OpenSSL is used for secure communications.


%prep
%autosetup -p1
# remove bundled libs
rm -rf lib
%if 0%{?el8}
# EL8 appdata does not support this, remove
sed -i -e '/<url type="contact">/d' res/fi.skyjake.Lagrange.appdata.xml
%endif


%build
%cmake \
  -DENABLE_POPUP_MENUS:BOOL=NO \
%if %{without x11_xlib}
  -DENABLE_X11_XLIB:BOOL=NO \
%endif

%cmake_build


%install
%cmake_install


%check
desktop-file-validate \
  %{buildroot}/%{_datadir}/applications/%{appid}.desktop

appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{appid}.appdata.xml


%files
%license LICENSE.md
%doc AUTHORS.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{appid}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources.lgr
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{appid}.appdata.xml

%changelog
%autochangelog
