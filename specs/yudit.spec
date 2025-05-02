Name: yudit
Version: 3.1.0
Release: %autorelease
License: GPL-2.0-only AND GPL-2.0-or-later 
URL: https://www.yudit.org
Source0: https://yudit.org/download/%{name}-%{version}.tar.gz
Summary: Unicode Text Editor
BuildRequires: pkgconfig(freetype2)
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(x11)
BuildRequires: dos2unix
BuildRequires: desktop-file-utils
BuildRequires: cups-client
BuildRequires: gettext 
BuildRequires: libappstream-glib
Requires: yudit-data
Requires:yudit-fonts  
Recommends: yudit-doc

%global desc %{expand:

Yudit is a Unicode text editor for the X Window System. It can do True Type
font rendering, printing, transliterated keyboard input and handwriting
recognition with no dependencies on external engines. Its conversion utilities
can convert text between various encodings. Keyboard input maps can also
act like text converters. There is no need for a preinstalled
multi-lingual environment.Menus are translated into many languages.
}
%description %desc

%package data
BuildArch: noarch
Requires: hicolor-icon-theme
Summary: Yudit Unicode Text Processor - data files
%description data %desc
 This package is arch- independent data component of Yudit.


%package doc  
Summary: Yudit Unicode Text Processor - documentation 
BuildArch: noarch
License: GPL-2.0-only AND GFDL-1.1-no-invariants-or-later
%description doc %desc   
This package is additional documentation component of Yudit.


%prep
%setup -q
for i in doc/HOWTO-baybayin.txt COPYING.TXT README.TXT doc/HOWTO-devanagari.txt  doc/HOWTO-syntax.txt  
do
    dos2unix $i
done
sed -i '/install-sh/s/ -s//' Makefile.conf.in

%conf
%configure

%build 
%make_build

%install
%make_install 
#%%exclude %{_datadir}/yudit/fonts
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yudit/
touch $RPM_BUILD_ROOT%{_sysconfdir}/yudit/yudit.conf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -m 644 yudit.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/yudit.svg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 644 yudit48x48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/yudit.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat >$RPM_BUILD_ROOT%{_datadir}/applications/org.yudit.yudit.desktop <<EOF
[Desktop Entry]
Exec=yudit %%F
Icon=yudit
Terminal=false
Type=Application
Name=Yudit
GenericName=Text Editor
Comment=View and edit files
Categories=Utility;TextEditor;
MimeType=text/utf8;text/plain;
Keywords=Unicode
EOF
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.yudit.yudit.desktop
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat >$RPM_BUILD_ROOT%{_metainfodir}/org.yudit.yudit.metainfo.xml<<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2023 Gaspar Sinai <gaspar@yudit.org> -->
<component type="desktop-application">
  <id>org.yudit.yudit.desktop</id>>
  <metadata_license>GPL-2.0-only</metadata_license>
  <project_license>GPL-2.0-only AND GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later</project_license>
  <name>Yudit</name>
  <summary>Unicode Text Editor</summary>
  <description>
    <p>
      Yudit is a Unicode text editor for the X Window System. It can do True Type
      font rendering, printing, transliterated keyboard input and handwriting
      recognition with no dependencies on external engine.
    </p>
    <p>
     Its conversion utilities can convert text between various encodings.
     Keyboard input maps can also act like text converters
    </p>
  </description>
  <screenshots>
    <screenshot type="default"> 
      <image>https://www.yudit.org/images/yudit-3.0.9-scale-2.0.png</image>
    </screenshot>
    <screenshot>
      <image>https://www.yudit.org/images/yudit-3.0.7-linux.png</image>
    </screenshot>
  </screenshots>
  <url type="homepage">http://www.yudit.org</url>
  <provides>
    <binary>mytool</binary>
    <binary>uniconv</binary>
    <binary>uniprint</binary>
    <binary>yudit</binary>
  </provides>
  <update_contact>yudit-maintainers@fedoraproject.org</update_contact>
</component>
EOF
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.yudit.yudit.metainfo.xml
mkdir -p $RPM_BUILD_ROOT%{_fontdir}/yudit/fonts
mv $RPM_BUILD_ROOT%{_datadir}/yudit/fonts/* $RPM_BUILD_ROOT%{_fontdir}/yudit/fonts
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/uniconv
%{_bindir}/uniprint 
%{_bindir}/yudit
%{_datadir}/yudit/config/
%{_bindir}/mytool
%{_mandir}/man1/*
%dir %{_sysconfdir}/yudit/
%config(noreplace) %{_sysconfdir}/yudit/*
%license COPYING.TXT   

%files data
%dir %{_datadir}/yudit
%{_datadir}/yudit/data
%{_datadir}/yudit/syntax
 %{_datadir}/applications/org.yudit.yudit.desktop
%{_datadir}/icons/hicolor/scalable/apps/yudit.svg
%{_datadir}/icons/hicolor/48x48/apps//yudit.png
%{_metainfodir}/org.yudit.yudit.metainfo.xml

%files doc 
%{_datadir}/yudit/src 
%{_datadir}/yudit/doc 
%license doc/cs/COPYING-DOCS
%doc doc/cs/README-DOCS.TXT
%changelog
%autochangelog
