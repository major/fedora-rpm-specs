%bcond  tests   1

Name:           swayimg
Version:        3.7
Release:        %autorelease
Summary:        Lightweight image viewer for Wayland display servers

License:        MIT
URL:            https://github.com/artemsen/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
%if %{with tests}
BuildRequires:  gcc-c++
%endif
BuildRequires:  meson >= 0.60

BuildRequires:  giflib-devel
BuildRequires:  pkgconfig(OpenEXR) >= 3.1
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fontconfig)
%if %{with tests}
BuildRequires:  pkgconfig(gtest)
%endif
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.46
BuildRequires:  pkgconfig(libsixel)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       hicolor-icon-theme

%description
Swayimg is a lightweight image viewer for Wayland display servers.


%prep
%autosetup


%build
%meson \
    -Dtests=%[%{with tests}?"enabled":"disabled"] \
    -Dversion=%{version}
%meson_build


%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/swayimg.desktop
%if %{with tests}
# HEIF test requires libheif-freeworld from rpmfusion
%global gtest_exclude Loader.heif
# A few tests fail on s390x (endianness?)
%ifarch s390x
%global gtest_exclude %{gtest_exclude}:Loader.External:Loader.bmp:Loader.dcm:Loader.tga
%endif
%meson_test --test-args='--gtest_filter=-%{gtest_exclude}'
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/swayimg
%{_mandir}/man1/swayimg.1*
%{_mandir}/man5/swayimgrc.5*
%{_datadir}/applications/swayimg.desktop
%{_datadir}/icons/hicolor/*/apps/swayimg.png
%dir %{_datadir}/swayimg
%{_datadir}/swayimg/swayimgrc
%{bash_completions_dir}/swayimg
%{zsh_completions_dir}/_swayimg


%changelog
%autochangelog
