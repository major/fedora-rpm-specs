%global srcname whipper
%global sum Python CD-DA ripper preferring accuracy over speed
%global desc CD ripper preferring accuracy over speed


Name:    %{srcname}
Version: 0.10.0
Release: %autorelease
Summary: %{sum}
URL:     https://github.com/whipper-team/whipper
License: GPL-3.0-or-later

Source0: https://github.com/whipper-team/%{srcname}/archive/v%{version}.tar.gz
# Fix now deprecated usage of dump in ruamel.yaml causing crash (https://github.com/whipper-team/whipper/issues/626)
# Cherry pick commit fixing this from upstream
Patch:         https://patch-diff.githubusercontent.com/raw/whipper-team/whipper/pull/543.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: gcc
BuildRequires: libsndfile-devel
BuildRequires: libappstream-glib

Requires: cdrdao
Requires: libcdio-paranoia
Requires: gobject-introspection
Requires: python3-gobject
Requires: python3-setuptools
Requires: python3-musicbrainzngs
Requires: python3-mutagen
Requires: python3-requests
Requires: python3-ruamel-yaml
Requires: python3-pycdio
Requires: python3-discid
Requires: flac
Requires: sox


# Exclude s390x due to missing cdrdao dep
ExcludeArch: s390x

%description
%{desc}

%prep
%autosetup -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%if "%_metainfodir" != "%{_datadir}/metainfo"
mv %{buildroot}%{_datadir}/metainfo/ \
   %{buildroot}%{_metainfodir}/
%endif

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml

%files
%{_bindir}/whipper
%{_bindir}/accuraterip-checksum
%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/accuraterip*
%license LICENSE
%doc README.md TODO CHANGELOG.md HACKING COVERAGE

%changelog
%autochangelog
