# build and test everything, not just shipped tools
%bcond build_and_test_all 1

# not shipping dbranch as it's not that useful in Fedora
%global tools %{shrink:
  cbspkg
  cpu-sig-tracker
  ebranch
  fedora-cve-triage
  fedora-review-digest
  fesco-chair
  hs-intake
  hs-meetings
  hs-relmon
  koji-diff
  koji-lag
  poi-tracker
  sandogasa-hattrack
  sandogasa-pkg-acl
  sandogasa-pkg-health
  sandogasa-report
}

Name:           sandogasa
Version:        0.28.1
Release:        %autorelease
Summary:        A collection of Fedora and CentOS packaging tools

# zone1970.tab from tzdata is in the Public Domain
SourceLicense:  (Apache-2.0 OR MIT) AND LicenseRef-Fedora-Public-Domain
# (MIT OR Apache-2.0) AND Unicode-3.0
# Apache-2.0
# Apache-2.0 AND ISC AND (MIT OR Apache-2.0)
# Apache-2.0 AND MIT
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# ISC
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
License:        %{shrink:
    (Apache-2.0 OR MIT) AND
    LicenseRef-Fedora-Public-Domain AND
    Unicode-3.0 AND
    Apache-2.0 AND ISC AND 
    MIT AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    BSD-3-Clause AND
    MPL-2.0 AND
    (Unlicense OR MIT) AND
    Zlib
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/slopfest/sandogasa
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Only binary tools are shipped, no source-only -devel packages for other
# packages to build against, so nothing needs them on i686. Since 0.28.1,
# compiling ebranch's tests also runs LLVM out of 32-bit address space.
ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core

Requires:       koji
# ebranch check-update reads the licenses of bundled Go and Rust
# dependencies with askalono
Recommends:     askalono-cli
Recommends:     bodhi-client
Recommends:     createrepo_c
Recommends:     fedora-packager
Recommends:     fedrq
# ebranch reads the base of an EPEL minor still in freeze from the
# CentOS Stream snapshot repos its build tag inherits. That is RHEL
# pre-release content rather than SIG content, so unlike the two SIG
# configs it carries no Supplements and this is what pulls it in.
Recommends:     fedrq-config-centos-snapshot
# ebranch queries the newest EPEL minor, which builds against the
# moving CentOS Stream, as c10.Ns; fedrq's own epel10.N branch only
# works for released minors. Not SIG content either, so no Supplements.
Recommends:     fedrq-config-centos-stream-minor
# for multimedia packages, ebranch can flag if counterpart packages
# need to be updated in RPM Fusion as well
Recommends:     fedrq-config-rpmfusion
# cbspkg srpm and mockbuild build locally. fedora-packager pulls these
# in, but a system set up only for CentOS work may not have it
Recommends:     mock
Recommends:     rpm-build
Recommends:     tzdata
# CentOS work: mock-centos-sig-configs (or centos-packager) marks a
# system used for CentOS packaging. cbspkg and cpu-sig-tracker use
# cbs and centos-cert from centos-packager, and cbspkg upload-sources
# and cpu-sig-tracker mr run centpkg, which centos-packager does not
# pull in.
Recommends:     (centos-packager if mock-centos-sig-configs)
Recommends:     (centpkg if (centos-packager or mock-centos-sig-configs))
Suggests:       centos-packager

# ebranch is in Fedora <= 44 and EPEL <= 9
# poi-tracker is in Fedora <= 44 and EPEL 10
Obsoletes:      ebranch < 0.0.4-1
Obsoletes:      poi-tracker < 0.0.2-1

%description
A collection of tools and libraries for Fedora package maintenance
and contributor activity tracking, built around shared API clients
for Bugzilla, Bodhi, NVD, dist-git, Discourse, FASJSON, and HyperKitty.

The name **sandogasa** (菅笠) refers to a Japanese straw hat often
associated with "slum" or post-apocalyptic robots in popular culture.

%package -n fedrq-config-centos-hyperscale
Summary:        CentOS Hyperscale SIG repositories for fedrq
License:        Apache-2.0 OR MIT

BuildArch:      noarch

Requires:       fedrq

# the previous name was too generic
# keep in Fedora until F46 is EOL
# and keep in EPEL until EPEL 10 is EOL
Provides:       fedrq-config-hyperscale = %{version}-%{release}
Obsoletes:      fedrq-config-hyperscale < 0.25.0

Supplements:    (fedrq and mock-centos-sig-configs)

%description -n fedrq-config-centos-hyperscale
Repository definitions to allow querying CentOS Hyperscale SIG
packages with fedrq.

%package -n fedrq-config-centos-proposed-updates
Summary:        CentOS Proposed Updates SIG repositories for fedrq
License:        Apache-2.0 OR MIT

BuildArch:      noarch

Requires:       fedrq
Supplements:    (fedrq and mock-centos-sig-configs)

%description -n fedrq-config-centos-proposed-updates
Repository definitions to allow querying CentOS Proposed Updates
packages with fedrq.

%package -n fedrq-config-centos-snapshot
Summary:        CentOS snapshot repositories for fedrq
License:        Apache-2.0 OR MIT

BuildArch:      noarch

Requires:       fedrq

%description -n fedrq-config-centos-snapshot
Repository definitions to allow querying CentOS snapshot (RHEL minor
pre-release) packages with fedrq.

%package -n fedrq-config-centos-stream-minor
Summary:        CentOS Stream with its newest EPEL minor for fedrq
License:        Apache-2.0 OR MIT

BuildArch:      noarch

Requires:       fedrq

%description -n fedrq-config-centos-stream-minor
Repository definitions to allow querying CentOS Stream together with
the EPEL minor release that builds against it (e.g. c10.4s) with fedrq.

%package -n fedrq-config-rpmfusion
Summary:        RPM Fusion repositories for fedrq
License:        Apache-2.0 OR MIT

BuildArch:      noarch

Requires:       fedrq

%description -n fedrq-config-rpmfusion
Repository definitions to allow querying RPM Fusion packages with
fedrq, free and nonfree, for both Fedora and EL.


%prep
%autosetup -p1
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -t


# We don't ship dbranch (it's not in %%{tools}) and its tests require a live
# git/network environment, so exclude it from the build and test entirely.
# %%cargo_build/%%cargo_test pass trailing args straight to cargo, and cargo's
# --exclude requires --workspace.
%build
%if %{with build_and_test_all}
%cargo_build
%else
%cargo_build -- --workspace --exclude dbranch
%endif
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
install -dm 0755 %{buildroot}%{_bindir}
install -dm 0755 %{buildroot}%{_mandir}/man1
install -dm 0755 %{buildroot}%{_datadir}/ebranch
install -dm 0755 %{buildroot}%{_datadir}/koji-lag
for tool in %{tools}; do
  install -pm 0755 target/rpm/${tool} %{buildroot}%{_bindir}/
  cp -p tools/${tool}/README.md README.${tool}.md
  cp -p tools/${tool}/man/${tool}.1 %{buildroot}%{_mandir}/man1/
  install -dm 0755 %{buildroot}%{_sysconfdir}/${tool}
done

# fedrq repos
for r in centos-{hyperscale,proposed-updates,snapshot,stream-minor} rpmfusion; do
  for f in ${r}.toml repos/${r}.repo; do
    install -Dpm 0644 configs/fedrq/${f} \
      %{buildroot}%{_sysconfdir}/fedrq/${f}
  done
done

# koji-lag scripts
for action in backup fetch publish vacuum; do
  install -pm 0755 scripts/${action}-store.sh %{buildroot}%{_bindir}/koji-lag-${action}-store
done
for i in FINDINGS.md notebooks queries; do
  cp -pr tools/koji-lag/${i} %{buildroot}%{_datadir}/koji-lag/
done
cp -pr configs/rpmfusion %{buildroot}%{_datadir}/ebranch/
cp -p configs/fedora-cve-triage/run.toml %{buildroot}%{_sysconfdir}/fedora-cve-triage/
cp -p configs/fesco-chair/config.toml %{buildroot}%{_sysconfdir}/fesco-chair/

# One block of %%files per tool, so a new tool only needs adding to
# %%{tools}. A tool whose config.toml is shipped (fesco-chair) owns it
# as a real %%config; the rest leave it as a %%ghost for the admin.
for tool in %{tools}; do
  echo "%{_bindir}/${tool}"
  echo "%{_mandir}/man1/${tool}.1*"
  echo "%%dir %{_sysconfdir}/${tool}"
  if [ -e %{buildroot}%{_sysconfdir}/${tool}/config.toml ]; then
    echo "%%config(noreplace) %{_sysconfdir}/${tool}/config.toml"
  else
    echo "%%ghost %%attr(0644,root,root) %%config(noreplace) %{_sysconfdir}/${tool}/config.toml"
  fi
done > tools.files


%check
%if %{with build_and_test_all}
%cargo_test
%else
%cargo_test -- --workspace --exclude dbranch
%endif


%files -f tools.files
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%doc README.md README.*.md CHANGELOG.md
%doc configs/hs-relmon configs/sandogasa-pkg-acl configs/sandogasa-report
%{_bindir}/koji-lag-backup-store
%{_bindir}/koji-lag-fetch-store
%{_bindir}/koji-lag-publish-store
%{_bindir}/koji-lag-vacuum-store
%config(noreplace) %{_sysconfdir}/fedora-cve-triage/run.toml
%{_datadir}/ebranch/
%{_datadir}/koji-lag/

%files -n fedrq-config-centos-hyperscale
%license LICENSE-APACHE
%license LICENSE-MIT
%dir %{_sysconfdir}/fedrq
%config(noreplace) %{_sysconfdir}/fedrq/centos-hyperscale.toml
%dir %{_sysconfdir}/fedrq/repos
%config(noreplace) %{_sysconfdir}/fedrq/repos/centos-hyperscale.repo

%files -n fedrq-config-centos-proposed-updates
%license LICENSE-APACHE
%license LICENSE-MIT
%dir %{_sysconfdir}/fedrq
%config(noreplace) %{_sysconfdir}/fedrq/centos-proposed-updates.toml
%dir %{_sysconfdir}/fedrq/repos
%config(noreplace) %{_sysconfdir}/fedrq/repos/centos-proposed-updates.repo

%files -n fedrq-config-centos-snapshot
%license LICENSE-APACHE
%license LICENSE-MIT
%dir %{_sysconfdir}/fedrq
%config(noreplace) %{_sysconfdir}/fedrq/centos-snapshot.toml
%dir %{_sysconfdir}/fedrq/repos
%config(noreplace) %{_sysconfdir}/fedrq/repos/centos-snapshot.repo

%files -n fedrq-config-centos-stream-minor
%license LICENSE-APACHE
%license LICENSE-MIT
%dir %{_sysconfdir}/fedrq
%config(noreplace) %{_sysconfdir}/fedrq/centos-stream-minor.toml
%dir %{_sysconfdir}/fedrq/repos
%config(noreplace) %{_sysconfdir}/fedrq/repos/centos-stream-minor.repo

%files -n fedrq-config-rpmfusion
%license LICENSE-APACHE
%license LICENSE-MIT
%dir %{_sysconfdir}/fedrq
%config(noreplace) %{_sysconfdir}/fedrq/rpmfusion.toml
%dir %{_sysconfdir}/fedrq/repos
%config(noreplace) %{_sysconfdir}/fedrq/repos/rpmfusion.repo


%changelog
%autochangelog
