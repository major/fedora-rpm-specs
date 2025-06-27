%global project beetbrainz
%global goipath codeberg.org/gbcox/%{project}
%global forgeurl https://codeberg.org/gbcox/%{project}/
%global commit ef649cdd613a867a723ad1c62df61c857958ccbe

%global golicenses LICENSE.md
%global godocs     README.md

%global common_description %{expand:
%{project} is a lightweight Go-based webhook listener designed to bridge
the gap between your media server playback and your MusicBrainz
scrobbling via ListenBrainz.}

%gometa

Name:           %{goname}
Version:        1.0.12
Release:        %autorelease
Summary:        Provides webhook integration for ListenBrainz scrobbling with %{project}
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang > 1.24
BuildRequires:  systemd
# If building for Fedora ≤ 42 or beets is available
# Required because rawhide isn't ready
# Hard requirement for stable releases, skip in Rawhide (F43)
%if 0%{?fedora} < 43
Requires: beets
%endif

%description %common_description

%prep
%goprep

%build

export GOFLAGS="-mod=readonly"
export LDFLAGS='\
    -X main.appVersion=%{version} \
    -X main.commit=%{commit} \
    -X main.shortCommit=%{shortcommit} \
    -linkmode external -extldflags "-pie -fPIE %{build_ldflags}"'
%gobuild -o %{project} .

%install
install -Dm755 %{project} %{buildroot}%{_bindir}/%{project}
install -Dm644 %{project}.service %{buildroot}%{_unitdir}/%{project}.service
install -Dm644 %{project}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{project}
mkdir -p %{buildroot}%{_mandir}/man8
install -p %{project}.8 %{buildroot}%{_mandir}/man8

%check
# No upstream tests provided.
# If tests are added upstream in the future, they should be included here.

%post
%systemd_post %{project}.service

%preun
%systemd_preun %{project}.service

%files
%license %{golicenses}
%doc %{godocs}
%config(noreplace) %{_sysconfdir}/sysconfig/%{project}
%{_bindir}/%{project}
%{_unitdir}/%{project}.service
%{_mandir}/man8/%{project}.8*

%changelog
%autochangelog
