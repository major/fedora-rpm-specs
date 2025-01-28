%global app_id  com.thomasokken.free42

Name:           free42
Epoch:          1
Version:        3.2
Release:        %autorelease
License:        GPL-2.0-only AND BSD-3-Clause
Summary:        42S Calculator Simulator
URL:            https://www.thomasokken.com/free42/
Source:         https://www.thomasokken.com/free42/upstream/free42-nologo-%{version}.tgz
Patch0:         free42-makefile.patch
Patch1:         free42-intel-lib-arches.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make

%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
# for XPM icon loading
Requires:       gdk-pixbuf2-modules-extra%{?_isa}
%endif

Provides:       bundled(IntelRDFPMathLib) = 2.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Free42 is a complete re-implementation of the 42S calculator and the
82240 printer.  It was written from scratch, without using any HP code.

%prep
%autosetup -p1 -n free42-nologo-%{version}

%build
cd gtk
# inteldecimal F128_CFLAGS uses this instead of CFLAGS
export CFLAGS_OPT="%{optflags}"
# make fails when using %{?_smp_mflags}
make BCD_MATH=1 AUDIO_ALSA=1

convert icon-48x48.xpm icon-48x48.png
sed -i -e 's/IvoryBlack/#231F20/' icon-128x128.xpm
convert icon-128x128.xpm icon-128x128.png

cat <<EOF >%{app_id}.desktop
[Desktop Entry]
Name=Free42
GenericName=Free42 calculator simulator
Exec=free42dec
Icon=free42
Terminal=false
Type=Application
Categories=Utility;Calculator;
StartupWMClass=%{name}dec
EOF

cat <<EOF >%{app_id}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>%{app_id}</id>
    <name>Free42</name>
    <summary>42S Calculator Simulator</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-2.0</project_license>
    <description>
        <p>
            Free42 is a complete re-implementation of the 42S calculator and the
            82240 printer.  It was written from scratch, without using any HP code.
        </p>
    </description>
    <launchable type="desktop-id">free42.desktop</launchable>
    <provides>
        <binary>free42dec</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>Thomas Okken</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <url type="homepage">https://www.thomasokken.com/free42/</url>
</component>
EOF

%install
install -D -p -m 755 gtk/free42dec %{buildroot}%{_bindir}/free42dec
install -D -p -m 644 gtk/icon-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 gtk/icon-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -p -m 644 gtk/%{app_id}.desktop %{buildroot}%{_datadir}/applications/%{app_id}.desktop
install -D -p -m 644 gtk/%{app_id}.appdata.xml %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%files
%doc CREDITS HISTORY README
%license COPYING gtk/IntelRDFPMathLib20U1/eula.txt
%{_bindir}/free42dec
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
