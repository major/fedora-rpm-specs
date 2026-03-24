%bcond  tests   1

Name:           swayimg
Version:        5.0
Release:        %autorelease
Summary:        Lightweight image viewer for Wayland display servers

License:        MIT
URL:            https://github.com/artemsen/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch:          %{url}/commit/5c2d958.patch#/swayimg-5.0-missing-includes.patch

# Exclude x86 and all the platforms where luajit is not available
ExcludeArch:    %{ix86} riscv64 ppc64 ppc64le

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
%if %{with tests}
BuildRequires:  glibc-langpack-en
%endif
BuildRequires:  meson >= 1.1

BuildRequires:  giflib-devel
# BuildRequires:  pkgconfig(OpenEXR) >= 3.4
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
%if %{with tests}
BuildRequires:  pkgconfig(gtest)
%endif
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.46
BuildRequires:  pkgconfig(libsixel)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.35
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       hicolor-icon-theme

# src/external/json: MIT
Provides:       bundled(json) = 3.12.0
# src/external/luabridge: MIT
Provides:       bundled(luabridge) = 3.0~rc4^20240929g713c1f5

%description
Swayimg is a lightweight image viewer for Wayland display servers.


%prep
%autosetup -p1


%build
%meson \
    -Dexr=disabled \
    -Dlicense=false \
    -Dtests=%[%{with tests}?"enabled":"disabled"] \
    -Dversion=%{version}
%meson_build


%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/swayimg.desktop
%if %{with tests}
%ifarch s390x
# A few tests fail on s390x (endianness?)
%global gtest_exclude ImageLoadTest.*
%else
# HEIF test requires libheif-freeworld from rpmfusion
%global gtest_exclude ImageLoadTest.heif
%endif

export LANG=en_US.UTF-8 # ImageListTest.SortAlphaUnicode fails with LANG=C
%meson_test --test-args='--gtest_filter=-%{gtest_exclude}'
%endif


%files
%license LICENSE
%doc %{_pkgdocdir}/*.md
%{_bindir}/swayimg
%{_mandir}/man1/swayimg.1*
%{_datadir}/applications/swayimg.desktop
%{_datadir}/icons/hicolor/*/apps/swayimg.png
%dir %{_datadir}/swayimg
%{_datadir}/swayimg/*.lua
%{bash_completions_dir}/swayimg
%{zsh_completions_dir}/_swayimg


%changelog
%autochangelog
