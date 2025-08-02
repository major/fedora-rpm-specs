%global  src_name  panini

Name:       Panini
Version:    0.74.0
Release:    %autorelease
Summary:    A tool for creating perspective views from panoramic and wide angle images
License:    GPL-3.0-or-later
URL:        https://lazarus-pkgs.github.io/lazarus-pkgs/%{src_name}.html
Source0:    https://github.com/lazarus-pkgs/%{src_name}/archive/v%{version}/%{src_name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libappstream-glib
BuildRequires: zlib-devel

%description
Panini can load most common photo and panoramic formats from image files such
as those created with hugin or QuickTimeVR (QTVR .mov) files.  Like all pano
viewers, it then shows a linear perspective view that can be panned and zoomed.
But Panini can also display a range of wide angle perspectives via the
stereographic and "Pannini" vedutismo families of projections, and shift,
rotate, and stretch the image like a software view camera.

%prep
%autosetup -n %{src_name}-%{version}
sed -i.backup "s|PREFIX = /usr|PREFIX = %{buildroot}%{_prefix}|" panini.pro
sed -e 's|0.73.0|0.74.0|g' -i panini.pro
chmod -x src/*cpp src/*h

for txt in *.txt ; do
    sed 's/\r//' $txt > $txt.new
    touch -r $txt $txt.new
    mv $txt.new $txt
done

%build
%{qmake_qt5} panini.pro
%make_build

%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{src_name}.desktop

# Remove appdata file from upstream
rm -f %{buildroot}%{_metainfodir}/*.appdata.xml

cat > %{buildroot}%{_metainfodir}/%{src_name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop">
  <id>panini.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-3.0+</project_license>
  <name>Panini</name>
  <summary>Create perspective views from panoramic and wide angle images</summary>
  <description>
    <p>
      Panini is a tool for creating perspective views from panoramic and wide angle images.
    </p>
    <p>
      Panini can load most common photo and panoramic formats from image files such
      as those created with hugin or QuickTimeVR (QTVR .mov) files.  Like all pano
      viewers, it then shows a linear perspective view that can be panned and zoomed.
      But Panini can also display a range of wide angle perspectives via the
      stereographic and "Pannini" vedutismo families of projections, and shift,
      rotate, and stretch the image like a software view camera.
    </p>
    <p>
      Panini can do those things because it paints the picture on a three dimensional
      surface, either a sphere or a cylinder, which you then view in perspective.
      Shifting the point of view changes the apparent perspective of the image, and
      other controls let you frame the view to your liking.  Then you can save the
      screen image to a file at higher-than-screen resolution.
    </p>
  </description>
  <!-- no screenshots -->
  <url type="homepage">https://lazarus-pkgs.github.io/lazarus-pkgs/panini.html</url>
  <updatecontact>jubalh AT iodoru DOT org</updatecontact>
</component>
EOF

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc README.md NEWS USAGE.md
%license GPLversion3.txt
%{_bindir}/%{src_name}
%{_datadir}/pixmaps/*.png
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*

%changelog
%autochangelog
