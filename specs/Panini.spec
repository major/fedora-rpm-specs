%global  src_name  panini

Name:       Panini
Version:    0.73.0
Release:    19%{?dist}
Summary:    A tool for creating perspective views from panoramic and wide angle images
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://lazarus-pkgs.github.io/lazarus-pkgs/%{src_name}.html
Source0:    https://github.com/lazarus-pkgs/%{src_name}/archive/v%{version}/%{src_name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  desktop-file-utils
BuildRequires:  gcc gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libappstream-glib
BuildRequires:  zlib-devel

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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.73.0-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.73.0-12
- Execute qmake inside %%build

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Jeff Law <law@redhat.com> - 0.73.0-5
- Drop build requirement for qt5-devel

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.73.0-1
- Release 0.73.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.72.0-1
- Update to latest upstream release
- Add gcc/g++ to BRs
- Remove unneeded patch
- Remove unneeded sources
- Use qt5
- Update appdata info

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.71.104-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71.104-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71.104-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71.104-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.71.104-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.71.104-6
- use %%qmake_qt4 macro to ensure proper build flags

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.104-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.71.104-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.71.104-3
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.71.104-1
- Updated to latest upstream release

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.103-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.103-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.103-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 28 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.71.103-8
- Update FTBFS patch to include libGLU: rhbz#843252

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.103-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.103-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.103-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.71.103-4
- fix for FTBFS # 565127

* Fri Jul 24 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.71.103-3
- used png for icon
* Thu Jul 23 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.71.103-2
- Corrected License tag
- used icon from source
* Fri Jul 17 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.71.103-1
- initial rpm build with new source with clearified License.
* Wed Jul 8 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.71.102-1
- Initial RPM build
