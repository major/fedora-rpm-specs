%global   paintowncommit 8a71ac86c585d8029709a10865c0e97dc4d3d2d1
%global   shortcommit %(c=%{paintowncommit}; echo ${c:0:7})
%global   rtech1commit 6636b452f5a9b55d2831bcb74c23eb991c12ee50
%global   date 20180113

Name: paintown
Version: 3.6.1
Release: 0.4.%{date}git%{shortcommit}%{?dist}
Summary: 2D fighting game

# LGPLv2+ (r-tech1/src/libs/[gme + hawknl]/*)
# BSD (r-tech1/scr/libs/pcre/*)
# BSD is main license for paintown and r-tech1
# CC0 (media files)
# Public Domain (data/paintown-title.png, image files, fonts)
License: CC0 and Public Domain and BSD and LGPLv2+
URL: http://paintown.org
Source0: https://github.com/kazzmir/paintown/archive/%{paintowncommit}/%{name}-%{paintowncommit}.tar.gz
Source1: https://github.com/kazzmir/paintown/releases/download/v3.6.0/data-3.6.0.zip#/%{name}-data-3.6.0.zip
Source2: https://github.com/kazzmir/r-tech1/archive/%{rtech1commit}/r-tech1-%{rtech1commit}.tar.gz
Source3: %{name}.desktop
Source4: %{name}.appdata.xml

# Modify SConstruct for using default Fedora compiler/linker flags
Patch0: paintown-fix_compiler_flags.patch

BuildRequires: scons
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel, glibc-headers
%{?fedora:BuildRequires: pkgconf-pkg-config}
%{?el7:BuildRequires: pkgconfig}
BuildRequires: SDL-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: freetype-devel
BuildRequires: libvorbis-devel
BuildRequires: libogg-devel
BuildRequires: mpg123-devel
BuildRequires: fontpackages-devel
BuildRequires: desktop-file-utils
BuildRequires: python2-devel
# TODO get rid of this:
BuildRequires: /usr/bin/python
BuildRequires: libappstream-glib
# r-tech1 library is still bundled
#BuildRequires: r-tech1-devel
%if 0%{?rhel}
BuildRequires: allegro-devel
%else
BuildRequires: allegro5-devel
BuildRequires: allegro5-addon-ttf-devel
BuildRequires: allegro5-addon-audio-devel
BuildRequires: allegro5-addon-image-devel
BuildRequires: allegro5-addon-video-devel
BuildRequires: allegro5-addon-acodec-devel
BuildRequires: allegro5-addon-dialog-devel
BuildRequires: allegro5-addon-physfs-devel
%endif

Requires: %{name}-data = %{version}-%{release}
Requires: hicolor-icon-theme

%description
Paintown is a 2D fighting game in the same style as Double Dragon and TMNT.
Paintown is very extensible and comes with editors to help design new levels
and animations.

####################
%package data
Summary:   2D Fighting Game (Data Files)
BuildArch: noarch
Requires:  %{name}-fonts = %{version}-%{release}

%description data
Paintown is a 2D fighting game in the same style as Double Dragon and TMNT.
Paintown is very extensible and comes with editors to help design new levels
and animations.
####################

####################
%package fonts
Summary: Fonts used by %{name}
BuildArch: noarch
License:   Public Domain
Requires:  fontpackages-filesystem

%description fonts
Fonts used by %{name}.

####################

%prep
%setup -q -a 1 -a 2 -n %{name}-%{paintowncommit}
%autopatch

# Paintown code recognizes 'r-tech1' directory
mv r-tech1-%{rtech1commit} r-tech1

# Preserve the logo
cp -p misc/logo-256x256.png %{name}.png

# Remove unneeded directories 
rm -rf misc debian

# r-tech1's license file
cp -p r-tech1/LICENSE r-tech1-LICENSE

# Set compiler/linker flags
sed -e 's|@@optflags@@|"%{optflags}"|g' -i SConstruct
sed -e 's|@@LDFLAGS@@|%{__global_ldflags}|g' -i SConstruct

%build
export PREFIX=%{_prefix}
scons %{?_smp_mflags} verbose=1 LINKFLAGS=-static \
 USE_ALLEGRO5=1 USE_SDL=1

%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{name} %{buildroot}%{_bindir}/%{name}-bin
chmod 0755 %{buildroot}%{_bindir}/%{name}-bin

mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}
cp -a data-3.6.0 %{buildroot}%{_datadir}/%{name}-%{version}/data
cp -a data/shaders %{buildroot}%{_datadir}/%{name}-%{version}/data/

cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
echo "Running Paintown"
%{_bindir}/%{name}-bin -d %{_datadir}/%{name}-%{version}/data "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

# Fonts
mkdir -p %{buildroot}%{_fontdir}
install -pm 644 %{buildroot}%{_datadir}/%{name}-%{version}/data/fonts/*.* %{buildroot}%{_fontdir}/
for i in `ls %{buildroot}%{_datadir}/%{name}-%{version}/data/fonts`; do
 ln -fs %{_fontdir}/$i %{buildroot}%{_datadir}/%{name}-%{version}/data/fonts/$i
done

# Icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -pm 644 %{name}.png  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

# Desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install -m 644 %{SOURCE3} --dir=%{buildroot}%{_datadir}/applications

# Fix permissions
for i in `find %{buildroot}%{_datadir}/%{name}-%{version}/data -perm /755 -type f \( -name "*.def" -o -name "*.air" -o -name "*.cmd" -o -name "*.cns" -o -name "*.txt" -o -name "*.xml" \)`; do
 chmod 0644 $i
done

## Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 644 %{SOURCE4} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license LEGAL LICENSE r-tech1-LICENSE
%doc TODO
%{_bindir}/%{name}*
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.appdata.xml

%files data
%{_datadir}/%{name}-%{version}/

%_font_pkg -n fonts *.ttf *.otf
%dir %{_fontdir}

%changelog
* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-0.4.20180113git8a71ac8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-0.3.20180113git8a71ac8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-0.2.20180113git8a71ac8
- Fix License

* Thu Mar 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-0.1.20180113git8a71ac8
- First rpm
