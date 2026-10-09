%global forgeurl    https://github.com/musicbrainz/picard/
%global commit      3f1d44b00e680f3e17c4f9a2e879e02f42f0a33f

Name:           picard
Version:        3.0.1
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
BuildRequires:  python3-devel
Requires:       hicolor-icon-theme
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

sed -i 's/"PyJWT~=2\.12"/"PyJWT~=2.0"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
export PICARD_DISABLE_AUTOUPDATE=1
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files picard

desktop-file-install \
  --delete-original --remove-category="Application"   \
  --dir=%{buildroot}%{_datadir}/applications      \
  %{buildroot}%{_datadir}/applications/*

%check

%files -f %{pyproject_files}
%doc AUTHORS.txt
%license COPYING.txt

%{_bindir}/picard
%{_bindir}/picard-cli

%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.*
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml


%changelog
%autochangelog
