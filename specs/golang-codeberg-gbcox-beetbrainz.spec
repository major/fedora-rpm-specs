%global project beetbrainz
%global goipath codeberg.org/gbcox/%{project}
%global forgeurl https://codeberg.org/gbcox/%{project}/
%global commit c373d5ec1d7cef3ec94f2f165489805dd29b1c89
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global golicenses LICENSE.md
%global godocs     README.md

%global common_description %{expand:
%{project} is a lightweight Go-based webhook listener designed to bridge
the gap between your media server playback and your MusicBrainz
scrobbling via ListenBrainz.}

%gometa

Name:           %{goname}
Version:        1.3.1
Release:        %autorelease
Summary:        Provides webhook integration for ListenBrainz scrobbling with %{project}
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang > 1.24
BuildRequires:  systemd-rpm-macros
# If building for Fedora ≤ 42 or beets is available
# Required because rawhide isn't ready
# Hard requirement for stable releases, skip in Rawhide (F43)
%if 0%{?fedora} < 43
Requires: beets
%endif

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
install -Dm644 %{project}.service %{buildroot}%{_userunitdir}/%{project}.service
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 -p %{project}.8 %{buildroot}%{_mandir}/man8

%check
%{buildroot}%{_bindir}/%{project} --version

%post
%systemd_user_post %{project}.service

%preun
%systemd_user_preun %{project}.service

%postun
%systemd_user_postun %{project}.service

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/%{project}
%{_userunitdir}/%{project}.service
%{_mandir}/man8/%{project}.8*

%changelog
%autochangelog
