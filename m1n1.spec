%global debug_package %{nil}

Name:           m1n1
Version:        1.3.2
Release:        %autorelease
Summary:        Bootloader and experimentation playground for Apple Silicon

# m1n1 proper is MIT licensed, but it relies on a number of vendored projects
# See the "License" section in README.md for the breakdown
License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later)
URL:            https://github.com/AsahiLinux/m1n1
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# PR#173: m1n1.asm: make it work again with gcc
Patch:          %{url}/pull/173.patch

%ifarch aarch64
# On aarch64 do a native build
BuildRequires:  gcc
%global buildflags RELEASE=1 ARCH=
%else
# By default m1n1 does a cross build
BuildRequires:  gcc-aarch64-linux-gnu
%global buildflags RELEASE=1
%endif
BuildRequires:  make

# For the bootloader logos and the framebuffer console
BuildRequires:  adobe-source-code-pro-fonts
BuildRequires:  system-logos
BuildRequires:  ImageMagick
BuildRequires:  zopfli

# For the udev rule
BuildRequires:  systemd-rpm-macros

# These are bundled, modified and statically linked into m1n1
Provides:       bundled(arm-trusted-firmware)
Provides:       bundled(dwc3)
Provides:       bundled(dlmalloc)
Provides:       bundled(PDCLib)
Provides:       bundled(libfdt)
Provides:       bundled(minilzlib)
Provides:       bundled(tinf)

%description
m1n1 is the bootloader developed by the Asahi Linux project to bridge the Apple
(XNU) boot ecosystem to the Linux boot ecosystem.

%package        tools
Summary:        Developer tools for m1n1
Requires:       %{name} = %{version}-%{release}
Requires:       python3
Requires:       python3dist(construct)
Requires:       python3dist(pyserial)
Requires:       systemd-udev
BuildArch:      noarch

%description    tools
This package contains various developer tools for m1n1.

%prep
%autosetup -p1

# Use our logos
# https://pagure.io/fedora-logos/pull-request/21
# https://pagure.io/generic-logos/pull-request/2
pushd data
rm bootlogo_{128,256}.{bin,png}
convert -background none -resize 128x128 -gravity center -extent 128x128 \
  %{_datadir}/pixmaps/fedora-logo-sprite.svg bootlogo_128.png
zopflipng -ym bootlogo_128.png bootlogo_128.png
convert -background none -resize 256x256 -gravity center -extent 256x256 \
  %{_datadir}/pixmaps/fedora-logo-sprite.svg bootlogo_256.png
zopflipng -ym bootlogo_256.png bootlogo_256.png
./makelogo.sh
popd

# Use our fonts
font="%{_fontbasedir}/adobe-source-code-pro/SourceCodePro-Bold.otf"
pushd font
rm SourceCodePro-Bold.ttf font.bin font_retina.bin
./makefont.sh 8 16 12 "$font" font.bin
./makefont.sh 16 32 25 "$font" font_retina.bin
popd

%build
%make_build %{buildflags}

%install
install -Dpm0644 -t %{buildroot}%{_libdir}/%{name} build/%{name}.{bin,macho}
install -Ddpm0755 %{buildroot}%{_libexecdir}/%{name}
cp -pr proxyclient tools %{buildroot}%{_libexecdir}/%{name}/
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} udev/80-m1n1.rules

%files
%license LICENSE 3rdparty_licenses/LICENSE.*
%doc README.md
%{_libdir}/%{name}

%files tools
%{_libexecdir}/%{name}
%{_udevrulesdir}/80-m1n1.rules

%changelog
%autochangelog
