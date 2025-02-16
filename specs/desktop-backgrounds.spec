%global rh_backgrounds_version 15
%global waves_version 0.1.2
%global fedora_release_name f42
%global gnome_default default
%global picture_ext jxl

Name:           desktop-backgrounds
Version:        42.0.0
Release:        %autorelease
Summary:        Desktop backgrounds

License:        LGPL-2.0-only
Source0:        redhat-backgrounds-%{rh_backgrounds_version}.tar.bz2
Source2:        Propaganda-1.0.0.tar.gz
Source3:        README.Propaganda
Source5:        waves-%{waves_version}.tar.bz2
Source6:        FedoraWaves-metadata.desktop
BuildArch:      noarch
%if "x%{?picture_ext}" != "xjxl"
BuildRequires:   ImageMagick
BuildRequires:   %{fedora_release_name}-backgrounds-base
%endif

%description
The desktop-backgrounds package contains artwork intended to be used as
desktop background image.


%package        basic
Summary:        Desktop backgrounds
Provides:       desktop-backgrounds = %{version}-%{release}
Obsoletes:      desktop-backgrounds < %{version}-%{release}

%description    basic
The desktop-backgrounds-basic package contains artwork intended to be used as
desktop background image.

%package        budgie
Summary:        The default Fedora wallpaper from Budgie desktop
Requires:       %{fedora_release_name}-backgrounds-budgie
Requires:       gsettings-desktop-schemas >= 2.91.92
Provides:       system-backgrounds-budgie = %{version}-%{release}
License:        CC-BY-SA

%description    budgie
The desktop-backgrounds-budgie package sets default background in budgie.

%package        gnome
Summary:        The default Fedora wallpaper from GNOME desktop
Requires:       %{fedora_release_name}-backgrounds-gnome
# starting with this release, gnome uses picture-uri instead of picture-filename
# see gnome bz #633983
Requires:       gsettings-desktop-schemas >= 2.91.92
Provides:       system-backgrounds-gnome = %{version}-%{release}
License:        CC-BY-SA

%description    gnome
The desktop-backgrounds-gnome package sets default background in gnome.

%package        compat
Summary:        The default Fedora wallpaper for less common DEs
Requires:       %{fedora_release_name}-backgrounds-base
Provides:       system-backgrounds-compat = %{version}-%{release}
License:        CC-BY-SA

%description    compat
The desktop-backgrounds-compat package contains file-names used
by less common Desktop Environments such as LXDE to set up the
default wallpaper.

%package        waves
Summary:        Desktop backgrounds for the Waves theme

%description    waves
The desktop-backgrounds-waves package contains the "Waves" desktop backgrounds
which were used in Fedora 9.


%prep
%autosetup -n redhat-backgrounds-%{rh_backgrounds_version}

# move things where %%doc can find them
cp -a %{SOURCE3} .
mv images/space/*.ps .
mv images/space/README* .

# add propaganda
(cd tiles && tar zxf %{SOURCE2})

# add waves
tar xjf %{SOURCE5}

%install
mkdir -p %{buildroot}%{_prefix}/share/backgrounds
cd %{buildroot}%{_prefix}/share/backgrounds

cp -a %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/images .
cp -a %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/tiles .

mkdir waves
# copy actual image files
cp -a %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/waves-%{waves_version}/*.png waves
# copy animation xml file
cp -a %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/waves-%{waves_version}/waves.xml waves

mkdir -p %{buildroot}%{_datadir}/gnome-background-properties
cp -a %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/desktop-backgrounds-basic.xml %{buildroot}%{_prefix}/share/gnome-background-properties
cp -a %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/waves-%{waves_version}/desktop-backgrounds-waves.xml %{buildroot}%{_prefix}/share/gnome-background-properties

mkdir -p %{buildroot}%{_datadir}/mate-background-properties
sed -e '/DOCTYPE/s/gnome/mate/' \
    %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/desktop-backgrounds-basic.xml \
    > %{buildroot}%{_prefix}/share/mate-background-properties/desktop-backgrounds-basic.xml
sed -e '/DOCTYPE/s/gnome/mate/' \
    %{_builddir}/redhat-backgrounds-%{rh_backgrounds_version}/waves-%{waves_version}/desktop-backgrounds-waves.xml \
    > %{buildroot}%{_prefix}/share/mate-background-properties/desktop-backgrounds-waves.xml

bgdir=%{buildroot}%{_datadir}/backgrounds
for I in tiles/Propaganda images/dewdop_leaf.jpg images/dragonfly.jpg images/frosty_pipes.jpg images/in_flight.jpg images/leaf_veins.jpg \
        images/leafdrops.jpg images/lightrays-transparent.png images/lightrays.png images/lightrays2.png images/raingutter.jpg images/riverstreet_rail.jpg \
        images/sneaking_branch.jpg images/space images/yellow_flower.jpg; do
        rm -rf ${bgdir}/${I}
done

# FedoraWaves theme for KDE4
mkdir -p %{buildroot}%{_datadir}/wallpapers/Fedora_Waves/contents/images
install -m 644 -p %{SOURCE6} %{buildroot}%{_datadir}/wallpapers/Fedora_Waves/metadata.desktop
(cd %{buildroot}%{_datadir}/wallpapers/Fedora_Waves/contents/;
ln -s ../../../backgrounds/waves/waves-eeepc-3-night.png screenshot.png
cd %{buildroot}%{_datadir}/wallpapers/Fedora_Waves/contents/images
ln -s ../../../../backgrounds/waves/waves-normal-3-night.png 1024x768.png
ln -s ../../../../backgrounds/waves/waves-wide-3-night.png 1280x800.png
# FIXME: there doesn't seem to be a 5:4 image in the latest iteration
ln -s ../../../../backgrounds/waves/waves-wide-3-night.png 1280x1024.png
ln -s ../../../../backgrounds/waves/waves-wide-3-night.png 1440x900.png
ln -s ../../../../backgrounds/waves/waves-normal-3-night.png 1600x1200.png
ln -s ../../../../backgrounds/waves/waves-wide-3-night.png 1920x1200.png
)

# Defaults for various desktops:

#   for Budgie, sets for: gnome desktop, gnome screensaver, and slick-greeter
#   set to 30, 20 is used by upstream and budgie branding package uses 10

mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
/bin/echo '[org.gnome.desktop.background:Budgie]' > \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.background.fedora.gschema.override
/bin/echo "picture-uri='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-day.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.background.fedora.gschema.override
/bin/echo "picture-uri-dark='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-night.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.background.fedora.gschema.override

/bin/echo '[org.gnome.desktop.screensaver:Budgie]' > \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.screensaver.fedora.gschema.override
/bin/echo "picture-uri='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-day.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.screensaver.fedora.gschema.override
/bin/echo "picture-uri-dark='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-night.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.screensaver.fedora.gschema.override

/bin/echo '[x.dm.slick-greeter:Budgie]' > \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_x.dm.slick_greeter.fedora.gschema.override
/bin/echo "background='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-day.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/30_budgie_x.dm.slick_greeter.fedora.gschema.override

#   for GNOME

mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
/bin/echo '[org.gnome.desktop.background]' > \
    %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.background.fedora.gschema.override
/bin/echo "picture-uri='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-day.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.background.fedora.gschema.override
/bin/echo "picture-uri-dark='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-night.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.background.fedora.gschema.override

# Use the Fedora background on the GNOME lockscreen as well. Would be awesome to
# have a separate image here to complement the default Fedora background, rather
# than using the same image in both places, but previously we've mixed Fedora
# desktop backgrounds with GNOME lockscreens, and they just do not match at all.

/bin/echo '[org.gnome.desktop.screensaver]' > \
    %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.screensaver.fedora.gschema.override
/bin/echo "picture-uri='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-day.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.screensaver.fedora.gschema.override
/bin/echo "picture-uri-dark='file://%{_datadir}/backgrounds/%{fedora_release_name}/%{gnome_default}/%{fedora_release_name}-01-night.%{picture_ext}'" >> \
    %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.screensaver.fedora.gschema.override

#   for KDE, this is handled in kde-settings
#   for XFCE, LXDE, etc.

%if "x%{?picture_ext}" == "xjxl"
  (cd %{buildroot}%{_datadir}/backgrounds/images;
  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-day.%{picture_ext} \
      default.%{picture_ext}
  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-day.%{picture_ext} \
      default-5_4.%{picture_ext}
  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-day.%{picture_ext} \
      default-16_9.%{picture_ext}
  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-day.%{picture_ext} \
      default-16_10.%{picture_ext}

  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-night.%{picture_ext} \
      default-dark.%{picture_ext}
  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-night.%{picture_ext} \
      default-dark-5_4.%{picture_ext}
  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-night.%{picture_ext} \
      default-dark-16_9.%{picture_ext}
  ln -s ../%{fedora_release_name}/default/%{fedora_release_name}-01-night.%{picture_ext} \
      default-dark-16_10.%{picture_ext}

  cd ..
  ln -s ./%{fedora_release_name}/default/%{fedora_release_name}-01-day.%{picture_ext} \
      default.%{picture_ext}
  ln -s ./%{fedora_release_name}/default/%{fedora_release_name}-01-night.%{picture_ext} \
      default-dark.%{picture_ext}
  )
%else
  (cd %{buildroot}%{_datadir}/backgrounds/images;
  convert %{_datadir}/backgrounds/%{fedora_release_name}/default/%{fedora_release_name}.%{picture_ext} \
        -alpha off default.jxl
  convert %{_datadir}/backgrounds/%{fedora_release_name}/default/%{fedora_release_name}.%{picture_ext} \
        -alpha off default-5_4.jxl
  convert %{_datadir}/backgrounds/%{fedora_release_name}/default/%{fedora_release_name}.%{picture_ext} \
        -alpha off default-16_9.jxl
  convert %{_datadir}/backgrounds/%{fedora_release_name}/default/%{fedora_release_name}.%{picture_ext} \
        -alpha off default-16_10.jxl
  )
%endif

# symlink for a default.xml background
  cd %{buildroot}%{_datadir}/backgrounds;
  ln -s %{fedora_release_name}/default/%{fedora_release_name}.xml\
      default.xml

%files basic
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/tiles
%dir %{_datadir}/backgrounds/images
%{_datadir}/backgrounds/tiles/*.png
%{_datadir}/backgrounds/tiles/*jpg
%{_datadir}/backgrounds/images/earth_from_space.jpg
%{_datadir}/backgrounds/images/flowers_and_leaves.jpg
%{_datadir}/backgrounds/images/ladybugs.jpg
%{_datadir}/backgrounds/images/stone_bird.jpg
%{_datadir}/backgrounds/images/tiny_blast_of_red.jpg
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/desktop-backgrounds-basic.xml
%dir %{_datadir}/mate-background-properties
%{_datadir}/mate-background-properties/desktop-backgrounds-basic.xml
%dir %{_datadir}/wallpapers

%files waves
%dir %{_datadir}/backgrounds/waves
%{_datadir}/backgrounds/waves/*.png
%{_datadir}/backgrounds/waves/waves.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-waves.xml
%{_datadir}/mate-background-properties/desktop-backgrounds-waves.xml
%{_datadir}/wallpapers/Fedora_Waves

%files budgie
%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.background.fedora.gschema.override
%{_datadir}/glib-2.0/schemas/30_budgie_org.gnome.desktop.screensaver.fedora.gschema.override
%{_datadir}/glib-2.0/schemas/30_budgie_x.dm.slick_greeter.fedora.gschema.override

%files gnome
%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.background.fedora.gschema.override
%{_datadir}/glib-2.0/schemas/10_org.gnome.desktop.screensaver.fedora.gschema.override

%files compat
%dir %{_datadir}/backgrounds/images/
%{_datadir}/backgrounds/images/default*
%{_datadir}/backgrounds/default.%{picture_ext}
%{_datadir}/backgrounds/default-dark.%{picture_ext}
%{_datadir}/backgrounds/default.xml

%changelog
%autochangelog
