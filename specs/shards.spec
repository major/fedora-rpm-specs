Name:           shards
Version:        0.20.0
Release:        %autorelease
Summary:        Dependency manager for the Crystal programming language

# Note: licensecheck reports BSD-2-Clause on spec/unit/spec_spec.cr, which is a
# false positive matching a YAML test fixture string ("license: BSD-2-Clause")
# in the unit test suite (and not installed in the binary package).
License:        Apache-2.0 AND MIT
URL:            https://github.com/crystal-lang/shards
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  crystal >= 0.35.0
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel

Requires:       crystal >= 0.35.0
Requires:       git-core

# Bundled copy of molinillo resolver algorithm
Provides:       bundled(crystal-molinillo) = 0.2.0
Provides:       bundled(crystal-shard(molinillo)) = 0.2.0

%description
Shards is the official dependency manager for the Crystal programming language.
It resolves, installs, and updates shard libraries and development tools from
remote Git repositories and local directories based on declarative manifests
and lock files.


%prep
%autosetup -p1
cp -p lib/molinillo/LICENSE LICENSE-molinillo


%build
%set_build_flags
%make_build release=1 debug=1 \
    CRYSTAL=crystal \
    FLAGS="--link-flags=\"%{build_ldflags}\""


%install
%make_install \
    PREFIX=%{_prefix} \
    MANDIR=%{_mandir}


%check
make test_unit \
    CRYSTAL=crystal \
    skip_fossil=1 \
    skip_hg=1


%files
%license LICENSE LICENSE-molinillo
%doc CHANGELOG.md README.md SPEC.md
%{_bindir}/shards
%{_mandir}/man1/shards.1*
%{_mandir}/man5/shard.yml.5*


%changelog
%autochangelog
