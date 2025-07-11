Name:    whipper
Version: 0.10.0
Release: %autorelease
Summary: Python CD-DA ripper preferring accuracy over speed
URL:     https://github.com/whipper-team/whipper
License: GPL-3.0-or-later
Source:  https://github.com/whipper-team/%{name}/archive/v%{version}.tar.gz

# Fix now deprecated usage of dump in ruamel.yaml causing crash (https://github.com/whipper-team/whipper/issues/626)
# Cherry pick commit fixing this from upstream
Patch:         https://patch-diff.githubusercontent.com/raw/whipper-team/whipper/pull/543.patch

BuildRequires: gcc
BuildRequires: libsndfile-devel
BuildRequires: libappstream-glib
BuildRequires: python3dist(musicbrainzngs)
BuildRequires: python3dist(mutagen)
BuildRequires: python3dist(pycdio)
BuildRequires: python3dist(pygobject)
BuildRequires: python3dist(ruamel-yaml)
BuildRequires: python3dist(twisted)

Requires: cdrdao
Requires: flac
Requires: libcdio-paranoia
Requires: python3dist(discid)
Requires: python3dist(musicbrainzngs)
Requires: python3dist(mutagen)
Requires: python3dist(pycdio)
Requires: python3dist(pygobject)
Requires: python3dist(ruamel-yaml)
Requires: sox


# Exclude s390x due to missing cdrdao dep
ExcludeArch: s390x


%description
CD ripper preferring accuracy over speed


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l %{name} 'accuraterip*'

%if "%_metainfodir" != "%{_datadir}/metainfo"
mv %{buildroot}%{_datadir}/metainfo/ \
   %{buildroot}%{_metainfodir}/
%endif

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml


%check
%pyproject_check_import


%files -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%{_bindir}/whipper
%{_bindir}/accuraterip-checksum
%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml


%changelog
%autochangelog
