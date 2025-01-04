Name: timg
Version: 1.6.1
Release: %autorelease
Summary: A terminal image and video viewer

License: GPL-2.0-only AND MIT AND (MIT OR Unlicense)
# The following are under different terms.
#
# - third_party/qoi is MIT
# - third_party/stb is MIT OR Unlicense

URL: https://github.com/hzeller/timg
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cairo
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: GraphicsMagick-c++-devel
BuildRequires: libavcodec-free-devel
BuildRequires: libavdevice-free-devel
BuildRequires: libavformat-free-devel
BuildRequires: libdeflate-devel
BuildRequires: libexif-devel
BuildRequires: librsvg2-devel
BuildRequires: libsixel-devel
BuildRequires: libswscale-free-devel
BuildRequires: openslide-devel
BuildRequires: pandoc
BuildRequires: pkg-config
BuildRequires: poppler-glib-devel
BuildRequires: qoi-devel
BuildRequires: stb_image-devel
BuildRequires: stb_image_resize-devel
BuildRequires: turbojpeg-devel

%description
A user-friendly terminal image viewer that uses graphic capabilities of
terminals (Sixel, Kitty or iTerm2), or 24-bit color capabilities and Unicode
character blocks if these are not available. On terminals that implement the
Sixel protocol, the Kitty Graphics Protocol, or the iTerm2 Graphics Protocol,
this displays images in full resolution.

%prep
%autosetup -n %{name}-%{version}
rm -rf third_party

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/timg
%{_mandir}/man1/timg.1*

%changelog
%autochangelog
