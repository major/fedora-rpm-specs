%global fullname net.sourceforge.Lifeograph

Name:       lifeograph
Version:    3.0.2
Release:    %autorelease
Summary:    A diary program

License:    GPL-3.0-or-later
URL:        http://%{name}.wikidot.com/start
Source0:    https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  enchant2-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtkmm4.0-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libchamplain-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libshumate-devel
BuildRequires:  meson
Requires:       hicolor-icon-theme

%description
Lifeograph is a diary program to take personal notes on life. It has all
essential functionality expected in a diary program and strives to have
a clean and streamlined user interface.


%prep
%autosetup
sed -i 's|<build_time.h>|"build_time.h"|' src/lifeograph.cpp
# We don't want it do anything, so we clear it out
echo "#!/usr/bin/python3" > meson_post_install.py
echo "print('no op')" >> meson_post_install.py

%build
./create_time_build_time_header.sh %{name} ./src/ ./src/
find . -name "build_time.h" -print

%meson
%meson_build

%install
%meson_install

%find_lang %{fullname}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{fullname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{fullname}.lang
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{fullname}.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-lifeographdiary.png
%{_datadir}/icons/hicolor/scalable/apps/%{fullname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{fullname}-symbolic.svg

%{_datadir}/%{fullname}
%{_datadir}/applications/%{fullname}.desktop
%{_metainfodir}/%{fullname}.metainfo.xml
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/*%{name}*

%changelog
%autochangelog
