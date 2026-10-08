Name:		fedora-third-party-repos
Version:	45
Release:	%autorelease
Summary:	Repository files for searchable repositories

License:	MIT
URL:		https://docs.fedoraproject.org/en-US/fesco/Third_Party_Repository_Policy/

# Only available for aarch64 and x86_64
Source0:	google-chrome.repo
# Only available for aarch64, armfp, ppc64le, x86_64
Source1:	rpmfusion-nonfree-nvidia-driver.repo
# Only available for x86_64
Source2:	rpmfusion-nonfree-steam.repo

%description
Repository files that make some select non-Fedora software available
via search in software centers.

%dnl ---------------------------------------------------------------

%package -n fedora-workstation-repositories
Summary:	Repository files for searchable repositories
URL:		https://docs.fedoraproject.org/en-US/workstation-working-group/third-party-repos/

# For rpmfusions-nonfree repo keys
Requires:	distribution-gpg-keys

# For support for repo configs in /usr
Requires:       fedora-third-party >= 0.11

# For /usr/share/dnf5/repos.d
Requires:	fedora-repos

%description -n fedora-workstation-repositories
Repository files that make some select non-Fedora software available
via search in gnome-software.

%files -n fedora-workstation-repositories
%ifarch %{x86_64}
%{_datadir}/dnf5/repos.d/rpmfusion-nonfree-steam.repo
%endif
%ifarch %{arm64} %{x86_64}
%config(noreplace) %{_sysconfdir}/default/google-chrome
%{_datadir}/dnf5/repos.d/google-chrome.repo
%endif
%ifarch %{arm64} ppc64le %{x86_64}
%{_datadir}/dnf5/repos.d/rpmfusion-nonfree-nvidia-driver.repo
%endif
%{_prefix}/lib/fedora-third-party/conf.d/fedora-workstation.conf

%dnl ---------------------------------------------------------------

%prep
# Nothing to do

%build
# Hook up the repositories to the global third-party enablement toggle
tee -a >> fedora-workstation.conf << EOF
%ifarch %{arm64} %{x86_64}
[google-chrome]
type=dnf

%endif
%ifarch %{x86_64}
[rpmfusion-nonfree-steam]
type=dnf

%endif
%ifarch %{arm64} ppc64le %{x86_64}
[rpmfusion-nonfree-nvidia-driver]
type=dnf
%endif
EOF

%install
mkdir -p %{buildroot}%{_datadir}/dnf5/repos.d
%ifarch %{x86_64}
cp %{SOURCE2} %{buildroot}%{_datadir}/dnf5/repos.d/
%endif
%ifarch %{arm64} %{x86_64}
cp %{SOURCE0} %{buildroot}%{_datadir}/dnf5/repos.d/
mkdir -p %{buildroot}%{_sysconfdir}/default
# Disable the rpm's own repo-adding function
echo 'repo_add_once="false"' > %{buildroot}%{_sysconfdir}/default/google-chrome
%endif
%ifarch %{arm64} ppc64le %{x86_64}
cp %{SOURCE1} %{buildroot}%{_datadir}/dnf5/repos.d/
%endif
mkdir -p %{buildroot}%{_prefix}/lib/fedora-third-party/conf.d
cp fedora-workstation.conf %{buildroot}%{_prefix}/lib/fedora-third-party/conf.d/

%changelog
%autochangelog
