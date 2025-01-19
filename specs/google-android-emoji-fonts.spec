%global fontname google-android-emoji
%global checkout 20120228git
%global archivename %{name}-%{checkout}

Name:    %{fontname}-fonts
# No sane versionning upstream, use git clone timestamp
Version: 1.01
Release: %autorelease
Summary: Android Emoji font released by Google

License:   Apache-2.0
URL:       https://android.googlesource.com/platform/frameworks/base.git/+/jb-release/data/fonts/
Source0:   %{archivename}.tar.xz
Source1:   get-source-from-git.sh
Source2:   AndroidEmoji.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
Requires:      fontpackages-filesystem


%description
The Android Emoji typeface contains a number of pictographs and smileys,
popularly used in instant messages and chat forums.  The style of the
typeface is playful.  It is taken from Google's Android Jelly Bean
mobile phone operating system.

This font hasn’t been updated since 2012.  You may well be better served
by its replacement, google-noto-emoji-fonts.


%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p AndroidEmoji.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/metainfo


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/AndroidEmoji.metainfo.xml


%_font_pkg *.ttf
%doc README.txt NOTICE
%{_datadir}/metainfo/AndroidEmoji.metainfo.xml


%changelog
%autochangelog
