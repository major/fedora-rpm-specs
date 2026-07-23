# build and test everything, not just shipped tools
%bcond build_and_test_all 1

# not shipping dbranch as it's not that useful in Fedora
%global tools %{shrink:
  cpu-sig-tracker
  ebranch
  fedora-cve-triage
  fedora-review-digest
  fesco-chair
  hs-intake
  hs-meetings
  hs-relmon
  koji-diff
  poi-tracker
  sandogasa-hattrack
  sandogasa-pkg-acl
  sandogasa-pkg-health
  sandogasa-report
}

Name:           sandogasa
Version:        0.18.0
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
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/slopfest/sandogasa
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
%if %{with build_and_test_all}
# needed by dbranch
BuildRequires:  git-core
%endif

Requires:       koji
Recommends:     fedora-packager
Recommends:     fedrq
Recommends:     tzdata
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
for tool in %{tools}; do
  install -Dpm 0755 target/rpm/${tool} -t %{buildroot}%{_bindir}
  cp -p tools/${tool}/README.md README.${tool}.md
done

%check
%if %{with build_and_test_all}
%cargo_test
%else
%cargo_test -- --workspace --exclude dbranch
%endif


%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%doc README.md README.*.md CHANGELOG.md
%{_bindir}/cpu-sig-tracker
%{_bindir}/ebranch
%{_bindir}/fedora-cve-triage
%{_bindir}/fedora-review-digest
%{_bindir}/fesco-chair
%{_bindir}/hs-intake
%{_bindir}/hs-meetings
%{_bindir}/hs-relmon
%{_bindir}/koji-diff
%{_bindir}/poi-tracker
%{_bindir}/sandogasa-hattrack
%{_bindir}/sandogasa-pkg-acl
%{_bindir}/sandogasa-pkg-health
%{_bindir}/sandogasa-report


%changelog
%autochangelog
