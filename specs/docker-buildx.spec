# Generated by go2rpm 1.11.0
%bcond_without check

# https://github.com/docker/buildx
%global goipath         github.com/docker/buildx
Version:                0.26.1
%global tag             v%{gsub %{version} ~ -}

%gometa -L -f

%global common_description %{expand:
Docker CLI plugin for extended build capabilities with BuildKit.}

Name:           docker-buildx
Release:        %autorelease
Summary:        Docker CLI plugin for extended build capabilities with BuildKit

# Generated by go-vendor-tools
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unicode-DFS-2016
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{archivename}-vendor.tar.bz2
# Generated by go-vendor-tools
Source2:        go-vendor-tools.toml

Patch:          0001-build-remove-go-build-trimpath-usage.patch

BuildRequires:  moby-rpm-macros
BuildRequires:  go-vendor-tools
%if %{with check}
BuildRequires:  git-core
%endif

# Require the Docker CLI
Requires:       docker-cli

%description %{common_description}

%prep
%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}

%build
# temporary fix for go 1.25 rc2
%if 0%{?fedora} >= 43
export GOEXPERIMENT=nodwarf5
%endif
GO_LDFLAGS="" GO_BUILDTAGS=""
CGO_ENABLED=1 \
GO_EXTRA_FLAGS="%{gocompilerflags} -a -v -x" \
GO_EXTRA_LDFLAGS=%{gobuild_ldflags_shescaped} \
REVISION=%{release} \
VERSION=%{version} \
    ./hack/build

%install
%go_vendor_license_install -c %{S:2}
install -Dpm 0755 ./bin/build/docker-buildx %{buildroot}%{moby_cli_plugins_dir}/docker-buildx

%check
%go_vendor_license_check -c %{S:2}
%if %{with check}
# Disable integration tests
rm tests/integration_test.go
# gitutil tests require a git repository
%gocheck -d util/gitutil
%endif

%files -f %{go_vendor_license_filelist}
%license vendor/modules.txt
%doc README.md
%{moby_cli_plugins_dir}/docker-buildx


%changelog
%autochangelog
