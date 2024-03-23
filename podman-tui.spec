%bcond_without check
%bcond_without bundled
%if 0%{?rhel}
%bcond_without bundled
%endif

%if %{defined rhel} && !%{defined eln}
%define gobuild(o:) go build -buildmode pie -compiler gc -tags="rpm_crashtraceback libtrust_openssl ${BUILDTAGS:-}" -ldflags "-linkmode=external -compressdwarf=false ${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'" -a -v -x %{?**};
%endif

%if %{with bundled}
%global gomodulesmode   GO111MODULE=on
%endif

# https://github.com/containers/podman-tui
%global goipath github.com/containers/podman-tui
Version: 1.0.0
%gometa

%global goname podman-tui

%global common_description %{expand:
%{goname} is a terminal user interface for Podman v4.
%{goname} is using podman.socket service to communicate with podman environment
and SSH to connect to remote podman machines.
}

%global golicenses LICENSE
%global godocs CODE-OF-CONDUCT.md CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}

Name: %{goname}
Release: %autorelease
Summary: Podman Terminal User Interface

License: ASL 2.0 and BSD and ISC and MIT and MPLv2.0
URL: %{gourl}
Source:         %{gosource}
Source:         vendor-%{version}.tar.gz
Source:         bundle_go_deps_for_rpm.sh

BuildRequires: gcc
BuildRequires: golang
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git-core
BuildRequires: go-rpm-macros
BuildRequires: make

%if 0%{?fedora} >= 35
BuildRequires: shadow-utils-subid-devel
%endif

%description
%{common_description}

%prep
%goprep %{?with_bundledc:-k}
%if %{with bundled}
%setup -q -T -D -a 1 -n %{name}-%{version}
%endif
%autopatch -p1

%if %{without bundled}
%generate_buildrequires
%go_generate_buildrequires
%endif

%build
%if %{with bundled}
export GOFLAGS="-mod=vendor"
%endif

export BUILDTAGS="exclude_graphdriver_devicemapper exclude_graphdriver_btrfs btrfs_noversion containers_image_openpgp remote"

%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%endif

%files
%license %{golicenses}
%doc     
%{_bindir}/*

%changelog
%autochangelog
