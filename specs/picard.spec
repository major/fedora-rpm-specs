%global forgeurl    https://github.com/musicbrainz/picard/
%global commit      f0b6669ae74921f953227154a4dea5b1f6160c7a

%define setup              setup.py
%define autoupdate_on      'disable-autoupdate', None
%define autoupdate_off     'disable-autoupdate', True
%define selfauto_on        self.disable_autoupdate = None
%define selfauto_off       self.disable_autoupdate = True

Name:           picard
Version:        2.13.2
Release:        %autorelease
Summary:        MusicBrainz-based audio tagger
License:        GPL-2.0-or-later

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        picard.rpmlintrc
BuildRequires:  gcc
BuildRequires:  pyproject-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-charset-normalizer
BuildRequires:  %{py3_dist makefun pytest}
Requires:       hicolor-icon-theme
Requires:       python3-qt5
Requires:       python3-dateutil
Requires:       python3-libdiscid
Requires:       python3-mutagen >= 1.37
Requires:       python3-markdown
Requires:       qt5-qtmultimedia
Recommends:     rsgain

%if 0%{?rhel}
ExcludeArch:    ppc64
%endif

%description
Picard is an audio tagging application using data from the MusicBrainz
database. The tagger is album or release oriented, rather than
track-oriented.

%prep
%forgesetup
%autosetup -n %{archivename}


%generate_buildrequires
%pyproject_buildrequires

%build
sed -r -i -e "s|%{autoupdate_on}|%{autoupdate_off}|g" \
  -e "s|%{selfauto_on}|%{selfauto_off}|g" \
  %{setup}
%pyproject_wheel

%install
%pyproject_install

desktop-file-install \
  --delete-original --remove-category="Application"   \
  --dir=%{buildroot}%{_datadir}/applications      \
  %{buildroot}%{_datadir}/applications/*

%find_lang %{name}
%find_lang %{name}-attributes
%find_lang %{name}-constants
%find_lang %{name}-countries

%check

%files -f %{name}.lang -f %{name}-attributes.lang -f %{name}-constants.lang -f %{name}-countries.lang
%doc AUTHORS.txt
%license COPYING.txt
%{_bindir}/picard
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.*
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml
%{python3_sitearch}/*dist-info
%{python3_sitearch}/picard/

%changelog
%autochangelog
