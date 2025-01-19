Name:           netsurf
Version:        3.9
Release:        17%{?dist}
Summary:        Compact graphical web browser

# There are MIT licensed bits as well as LGPL-licensed talloc, but most
# files are GPLv2 and that is the computed effective license.
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://www.netsurf-browser.org/
Source0:        https://download.netsurf-browser.org/netsurf/releases/source-full/netsurf-all-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gperf
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  openssl-devel
BuildRequires:  gtk3-devel
BuildRequires:  expat-devel
BuildRequires:  curl-devel
BuildRequires:  libpng-devel
BuildRequires:  /usr/bin/xxd
BuildRequires:  /usr/bin/hostname
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-util)

%description
NetSurf is a compact graphical web browser which aims for HTML5, CSS and
JavaScript support.

This package ships the version with GTK3 frontend that most users will
want to use.


%package fb
Summary:        Compact graphical web browser (framebuffer frontend)

Requires:       dejavu-sans-fonts >= 2.37-5
Requires:       dejavu-serif-fonts >= 2.37-5
Requires:       dejavu-sans-mono-fonts >= 2.37-5

%description fb
NetSurf is a compact graphical web browser which aims for HTML5, CSS and
JavaScript support.

This package ships the version with a special-purpose framebuffer frontend.


%prep
%setup -q -n netsurf-all-%{version}


%global common_make_opts V=1 PREFIX=%{_prefix} \\\
        NETSURF_USE_WEBP=YES \\\
        NETSURF_USE_NSSVG=YES \\\
        NETSURF_USE_ROSPRITE=NO \\\
        NETSURF_USE_NSPSL=YES \\\
        NETSURF_USE_NSLOG=YES \\\
        NETSURF_USE_HARU_PDF=NO \\\
        NETSURF_USE_VIDEO=NO

%global fb_make_opts %{common_make_opts} TARGET=framebuffer \\\
        NETSURF_USE_RSVG=NO \\\
        NETSURF_USE_FREETYPE2=YES \\\
        NETSURF_FB_FONTLIB=freetype \\\
        NETSURF_FB_FONT_SANS_SERIF=dejavu-sans-fonts/DejaVuSans.ttf \\\
        NETSURF_FB_FONT_SANS_SERIF_BOLD=dejavu-sans-fonts/DejaVuSans-Bold.ttf \\\
        NETSURF_FB_FONT_SANS_SERIF_ITALIC=dejavu-sans-fonts/DejaVuSans-Oblique.ttf \\\
        NETSURF_FB_FONT_SANS_SERIF_ITALIC_BOLD=dejavu-sans-fonts/DejaVuSans-BoldOblique.ttf \\\
        NETSURF_FB_FONT_SERIF=dejavu-serif-fonts/DejaVuSerif.ttf \\\
        NETSURF_FB_FONT_SERIF_BOLD=dejavu-serif-fonts/DejaVuSerif-Bold.ttf \\\
        NETSURF_FB_FONT_MONOSPACE=dejavu-sans-mono-fonts/DejaVuSansMono.ttf \\\
        NETSURF_FB_FONT_MONOSPACE_BOLD=dejavu-sans-mono-fonts/DejaVuSansMono-Bold.ttf \\\
        NETSURF_FB_FONT_CURSIVE=dejavu-serif-fonts/DejaVuSerif-Italic.ttf \\\
        NETSURF_FB_FONT_FANTASY=dejavu-sans-fonts/DejaVuSansCondensed-Bold.ttf \\\
        NETSURF_FB_FONTPATH=/usr/share/fonts

%global gtk_make_opts %{common_make_opts} TARGET=gtk3 \\\
        NETSURF_USE_RSVG=YES


%build
# Abort the build if there's a new font we should substitute
[ $(grep NETSURF_FB_FONT_ netsurf/frontends/framebuffer/Makefile.defaults |wc -l) = 10 ]

export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
make %{?_smp_mflags} %{fb_make_opts}
make %{?_smp_mflags} %{gtk_make_opts}


%install
%make_install %{fb_make_opts}
%make_install %{gtk_make_opts}

mkdir -p %{buildroot}%{_datadir}/pixmaps \
        %{buildroot}%{_datadir}/applications
install -pm644 netsurf/frontends/gtk/res/netsurf.xpm \
        %{buildroot}%{_datadir}/pixmaps
sed 's/Exec=netsurf-gtk/Exec=netsurf-gtk3/;s/netsurf.png/netsurf/' \
        <netsurf/frontends/gtk/res/netsurf-gtk.desktop \
        >%{buildroot}%{_datadir}/applications/netsurf-gtk.desktop
desktop-file-validate \
        %{buildroot}%{_datadir}/applications/netsurf-gtk.desktop


%files
%{_bindir}/netsurf-gtk3
%{_datadir}/netsurf
%{_datadir}/applications/netsurf-gtk.desktop
%{_datadir}/pixmaps/netsurf.xpm


%files fb
%{_bindir}/netsurf-fb
%{_datadir}/netsurf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.9-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.9-8
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Lubomir Rintel <lkundrak@v3.sk> - 3.9-4
- Update paths to fb fonts

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Lubomir Rintel <lkundrak@v3.sk> - 3.9-2
- Add fb subpackage

* Sun Jan 12 2020 Lubomir Rintel <lkundrak@v3.sk> - 3.9-1
- Initial packaging
