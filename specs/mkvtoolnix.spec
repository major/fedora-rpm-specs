Summary: Matroska container manipulation utilities
Name: mkvtoolnix
Version: 89.0
Release: %autorelease
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Source0: https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz
Source1: https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz.sig
Source2: https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt
URL: https://mkvtoolnix.download/
BuildRequires: boost-devel
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: desktop-file-utils
BuildRequires: docbook-style-xsl
BuildRequires: fmt-devel >= 8.0.0
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gmp-devel
BuildRequires: gnupg2
BuildRequires: gtest-devel
BuildRequires: json-devel
BuildRequires: libappstream-glib
BuildRequires: libvorbis-devel
BuildRequires: po4a
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(libcmark)
BuildRequires: pkgconfig(libebml) >= 1.4.4
BuildRequires: pkgconfig(libmatroska) >= 1.7.1
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(zlib)
BuildRequires: rubygem-drake
BuildRequires: rubygem-json
BuildRequires: utf8cpp-devel >= 3.2-2
BuildRequires: /usr/bin/qmake6
BuildRequires: /usr/bin/xsltproc
Requires: libebml%{_isa} >= 1.4.4
Requires: libmatroska%{_isa} >= 1.7.1
# bundles a modified avilib GPLv2+
Provides: bundled(avilib) = 0.6.10
# https://www.bunkus.org/videotools/librmff/index.html LGPLv2+
Provides: bundled(librmff) = 0.6.0

%description
Mkvtoolnix is a set of utilities to mux and demux audio, video and subtitle
streams into and from Matroska containers.

%package gui
Summary: QT Graphical interface for Matroska container manipulation
Requires: %{name} = %{version}-%{release}
Requires: hicolor-icon-theme

%description gui
Mkvtoolnix is a set of utilities to mux and demux audio, video and subtitle
streams into and from Matroska containers.

This package contains the QT graphical interface for these utilities.

%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q
rm -rf lib/{fmt,libebml,libmatroska,nlohmann-json,pugixml,utf8-cpp}
rm -rf rake.d/vendor drake

%build
%configure \
  --disable-optimization \
  --disable-update-check \
  --with-boost-libdir=%{_libdir} \
  || cat config.log
drake %{?_smp_mflags} V=1

%install
drake DESTDIR=$RPM_BUILD_ROOT TOOLS=1 install
desktop-file-validate %{buildroot}%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.bunkus.mkvtoolnix-gui.appdata.xml

install -pm 755 src/tools/{base64tool,diracparser,ebml_validator,vc1parser} $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name}
%find_lang mkvextract --with-man
%find_lang mkvmerge --with-man
%find_lang mkvpropedit --with-man
%find_lang mkvinfo --with-man
cat mkv{extract,info,merge,propedit}.lang >> mkvtoolnix.lang

%find_lang mkvtoolnix-gui --with-man

%check
drake tests:run_unit

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%{_bindir}/base64tool
%{_bindir}/diracparser
%{_bindir}/ebml_validator
%{_bindir}/mkvextract
%{_bindir}/mkvinfo
%{_bindir}/mkvmerge
%{_bindir}/mkvpropedit
%{_bindir}/vc1parser
%{_mandir}/man1/mkvextract.1*
%{_mandir}/man1/mkvinfo.1*
%{_mandir}/man1/mkvmerge.1*
%{_mandir}/man1/mkvpropedit.1*

%files gui -f mkvtoolnix-gui.lang
%{_bindir}/mkvtoolnix-gui
%{_mandir}/man1/mkvtoolnix-gui.1*
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_metainfodir}/org.bunkus.mkvtoolnix-gui.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/mime/packages/org.bunkus.mkvtoolnix-gui.xml
%{_datadir}/mkvtoolnix

%changelog
%autochangelog
