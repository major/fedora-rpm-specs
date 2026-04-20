# Add a rebuild comment to force a new build
#
# This commit forces a rebuild due to infrastructure changes or similar.
# No functional changes are present in this commit.

%global project beetbrainz
%global goipath codeberg.org/gbcox/%{project}
%global forgeurl https://codeberg.org/gbcox/%{project}/
%global commit 4083325d835f1e49eba4128161af31569a7731e3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global golicenses LICENSE.md
%global godocs     README.md

%global common_description %{expand:
%{project} is a lightweight Go-based webhook listener designed to bridge
the gap between your media server playback and your MusicBrainz
scrobbling via ListenBrainz.}

%gometa

Name:           %{goname}
Version:        1.12.1
Release:        %autorelease
Summary:        Provides webhook integration for ListenBrainz scrobbling with %{project}
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang > 1.24
BuildRequires:  systemd-rpm-macros
Requires: beets

%description %common_description

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build

export GOFLAGS="-mod=readonly"

export LDFLAGS="\
  -X main.AppVersionFull=%{version} \
  -X main.CommitFull=%{commit} \
  -X main.ShortCommitFull=%{shortcommit} \
  -linkmode external -extldflags '-pie -fPIE %{build_ldflags}'"

%gobuild -o %{project} .

%install
install -Dm755 %{project} %{buildroot}%{_bindir}/%{project}
install -Dm755 %{project}-replay %{buildroot}%{_bindir}/%{project}-replay
install -Dm644 %{project}.service %{buildroot}%{_userunitdir}/%{project}.service
install -Dm644 %{project}-replay.service %{buildroot}%{_userunitdir}/%{project}-replay.service
install -Dm644 %{project}-replay.timer %{buildroot}%{_userunitdir}/%{project}-replay.timer
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 -p %{project}.8 %{buildroot}%{_mandir}/man8
install -m644 -p %{project}-replay.8 %{buildroot}%{_mandir}/man8

%check
%{buildroot}%{_bindir}/%{project} --version
bash -n %{buildroot}%{_bindir}/%{project}-replay

%post
%systemd_user_post %{project}.service %{project}-replay.service %{project}-replay.timer

%preun
%systemd_user_preun %{project}.service %{project}-replay.service %{project}-replay.timer

%postun
%systemd_user_postun %{project}.service %{project}-replay.service %{project}-replay.timer

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/%{project}
%{_bindir}/%{project}-replay
%{_userunitdir}/%{project}.service
%{_userunitdir}/%{project}-replay.service
%{_userunitdir}/%{project}-replay.timer
%{_mandir}/man8/%{project}.8*
%{_mandir}/man8/%{project}-replay.8*

%changelog
%autochangelog
