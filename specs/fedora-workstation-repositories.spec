Name:		fedora-workstation-repositories
Version:	38
Release:	%autorelease
Summary:	Repository files for searchable repositories

License:	MIT
URL:		https://fedoraproject.org/wiki/Workstation/Third_Party_Software_Repositories
# Only available for x86_64
Source0:	_copr:copr.fedorainfracloud.org:phracek:PyCharm.repo
# Only available for x86_64
Source1:	google-chrome.repo
# Only available for aarch64, armfp, ppc64le, x86_64
Source2:	rpmfusion-nonfree-nvidia-driver.repo
# Only available for x86_64
Source3:	rpmfusion-nonfree-steam.repo

# For rpmfusions-nonfree repo keys
Requires:	distribution-gpg-keys

Requires:       fedora-third-party

# For /etc/yum.repos.d
Requires:	fedora-repos

%description
Repository files that make some select non-Fedora software available
via search in gnome-software.

%prep

%build
# Hook up the repositories to the global third-party enablement toggle
tee -a >> fedora-workstation.conf << EOF
%ifarch x86_64
[google-chrome]
type=dnf

[copr:copr.fedorainfracloud.org:phracek:PyCharm]
type=dnf

[rpmfusion-nonfree-steam]
type=dnf

%endif
%ifarch aarch64 ppc64le x86_64
[rpmfusion-nonfree-nvidia-driver]
type=dnf
%endif
EOF

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
%ifarch x86_64
cp %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
%endif
%ifarch aarch64 ppc64le x86_64
cp %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
%endif
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/fedora-third-party/conf.d
cp fedora-workstation.conf $RPM_BUILD_ROOT%{_prefix}/lib/fedora-third-party/conf.d/

%files
%ifarch x86_64
%config(noreplace) %{_sysconfdir}/yum.repos.d/_copr:copr.fedorainfracloud.org:phracek:PyCharm.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/google-chrome.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-steam.repo
%endif
%ifarch aarch64 ppc64le x86_64
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-nvidia-driver.repo
%endif
%{_prefix}/lib/fedora-third-party/conf.d/*.conf

%changelog
%autochangelog
