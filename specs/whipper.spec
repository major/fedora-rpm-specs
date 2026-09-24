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

BuildRequires: /usr/bin/rst2man
BuildRequires: gcc
BuildRequires: libsndfile-devel
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: python3dist(musicbrainzngs)
BuildRequires: python3dist(mutagen)
BuildRequires: python3dist(pycdio)
BuildRequires: python3dist(pygobject)
BuildRequires: python3dist(ruamel-yaml)
BuildRequires: python3dist(twisted)
BuildRequires: python3-pkg-resources

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

cd man
%make_build
cd -


%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l %{name} 'accuraterip*'

%if "%_metainfodir" != "%{_datadir}/metainfo"
mv %{buildroot}%{_datadir}/metainfo/ \
   %{buildroot}%{_metainfodir}/
%endif

install -m0644 -pD -t %{buildroot}%{_mandir}/man1/ man/*.1


%check
%pyproject_check_import

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml


%files -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%{_bindir}/whipper
%{_bindir}/accuraterip-checksum
%{_mandir}/man1/whipper-accurip.1*
%{_mandir}/man1/whipper-cd-info.1*
%{_mandir}/man1/whipper-cd-rip.1*
%{_mandir}/man1/whipper-cd.1*
%{_mandir}/man1/whipper-drive-analyze.1*
%{_mandir}/man1/whipper-drive-list.1*
%{_mandir}/man1/whipper-drive.1*
%{_mandir}/man1/whipper-image-verify.1*
%{_mandir}/man1/whipper-image.1*
%{_mandir}/man1/whipper-mblookup.1*
%{_mandir}/man1/whipper-offset-find.1*
%{_mandir}/man1/whipper-offset.1*
%{_mandir}/man1/whipper.1*
%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml


%changelog
%autochangelog
