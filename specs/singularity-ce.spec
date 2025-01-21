# Disable debugsource packages; otherwise it ends up with an empty %%files
# file in debugsourcefiles.list on Fedora
%undefine _debugsource_packages

Name: singularity-ce
Version: 4.2.2
Release: 2%{?dist}
Summary: Application and environment virtualization

# See LICENSE.md for first party code (BSD-3-Clause and BSD-3-Clause-LBNL)
# See LICENSE_THIRD_PARTY.md for incorporated code (Apache-2.0)
# See LICENSE_DEPENDENCIES.md for bundled dependencies
# License identifiers taken from: https://fedoraproject.org/wiki/Licensing
License: BSD-3-Clause AND BSD-3-Clause-LBNL AND Apache-2.0

URL: https://www.sylabs.io/singularity/
Source: https://github.com/sylabs/singularity/releases/download/v%{version}/singularity-ce-%{version}.tar.gz

BuildRequires: golang >= 1.22.5
BuildRequires: gcc
BuildRequires: make
BuildRequires: libseccomp-devel
BuildRequires: glib2-devel
# Paths to runtime dependencies detected by mconfig, so must be present at build time.
BuildRequires: cryptsetup
BuildRequires: squashfs-tools >= 4.5.0
# For building bundled squashfuse 0.5.0, required for uid= support.
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: fuse3-devel
BuildRequires: libattr-devel
BuildRequires: libtool
BuildRequires: zlib-devel

Requires: conmon >= 2.0.24
Requires: crun
Requires: cryptsetup
Requires: fuse
Requires: fuse3
Requires: shadow-utils
Requires: squashfs-tools >= 4.5.0

ExclusiveArch: %{go_arches}
ExcludeArch: %{ix86}

# Required for uid= support, not present in Fedora packaged version.
Provides: bundled(squashfuse) = 0.5.0

# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/AdaLogics/go_fuzz_headers)) = v0.0.0_20230811130428_ced1acdcaa24
Provides: bundled(golang(github.com/AdamKorcz/go_fuzz_headers)) = v0.0.0_20210319161527_f761c2329661
Provides: bundled(golang(github.com/adigunhammedolalekan/registry_auth)) = v0.0.0_20200730122110_8cde180a3a60
Provides: bundled(golang(github.com/agext/levenshtein)) = v1.2.3
Provides: bundled(golang(github.com/alexflint/go_filemutex)) = v1.3.0
Provides: bundled(golang(github.com/anchore/go_struct_converter)) = v0.0.0_20221118182256_c68fdcfa2092
Provides: bundled(golang(github.com/apex/log)) = v1.9.0
Provides: bundled(golang(github.com/armon/circbuf)) = v0.0.0_20190214190532_5111143e8da2
Provides: bundled(golang(github.com/astromechza/etcpwdparse)) = v0.0.0_20170319193008_f0e5f0779716
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20230124172434_306776ec8161
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/blang/semver/v4)) = v4.0.0
Provides: bundled(golang(github.com/buger/goterm)) = v1.0.4
Provides: bundled(golang(github.com/buger/jsonparser)) = v1.1.1
Provides: bundled(golang(github.com/cenkalti/backoff/v4)) = v4.3.0
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.3.0
Provides: bundled(golang(github.com/cilium/ebpf)) = v0.16.0
Provides: bundled(golang(github.com/cloudflare/circl)) = v1.3.7
Provides: bundled(golang(github.com/containerd/cgroups/v3)) = v3.0.3
Provides: bundled(golang(github.com/containerd/console)) = v1.0.4
Provides: bundled(golang(github.com/containerd/containerd/api)) = v1.7.19
Provides: bundled(golang(github.com/containerd/containerd)) = v1.7.24
Provides: bundled(golang(github.com/containerd/continuity)) = v0.4.5
Provides: bundled(golang(github.com/containerd/errdefs/pkg)) = v0.3.0
Provides: bundled(golang(github.com/containerd/errdefs)) = v0.3.0
Provides: bundled(golang(github.com/containerd/fifo)) = v1.1.0
Provides: bundled(golang(github.com/containerd/go_cni)) = v1.1.10
Provides: bundled(golang(github.com/containerd/go_runc)) = v1.1.0
Provides: bundled(golang(github.com/containerd/log)) = v0.1.0
Provides: bundled(golang(github.com/containerd/nydus_snapshotter)) = v0.14.0
Provides: bundled(golang(github.com/containerd/platforms)) = v0.2.1
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.15.1
Provides: bundled(golang(github.com/containerd/ttrpc)) = v1.2.5
Provides: bundled(golang(github.com/containerd/typeurl/v2)) = v2.2.3
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.2.3
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.5.1
Provides: bundled(golang(github.com/containers/image/v5)) = v5.33.0
Provides: bundled(golang(github.com/containers/storage)) = v1.56.0
Provides: bundled(golang(github.com/coreos/go_iptables)) = v0.7.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.5.0
Provides: bundled(golang(github.com/cpuguy83/go_md2man/v2)) = v2.0.5
Provides: bundled(golang(github.com/creack/pty)) = v1.1.23
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.3.6
Provides: bundled(golang(github.com/d2g/dhcp4client)) = v1.0.0
Provides: bundled(golang(github.com/d2g/dhcp4)) = v0.0.0_20170904100407_a1d1b6c41b1c
Provides: bundled(golang(github.com/distribution/reference)) = v0.6.0
Provides: bundled(golang(github.com/docker/cli)) = v27.4.1+incompatible
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.3+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.8.2
Provides: bundled(golang(github.com/docker/docker)) = v27.4.1+incompatible
Provides: bundled(golang(github.com/docker/go_connections)) = v0.5.0
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/docker/libtrust)) = v0.0.0_20160708172513_aabc10ec26b7
Provides: bundled(golang(github.com/fatih/color)) = v1.18.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = v1.0.4
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.7.0
Provides: bundled(golang(github.com/garyburd/redigo)) = v0.0.0_20150301180006_535138d7bcd7
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/gofrs/flock)) = v0.12.1
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/go_jose/go_jose/v4)) = v4.0.4
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.4
Provides: bundled(golang(github.com/go_log/log)) = v0.2.0
Provides: bundled(golang(github.com/go_logr/logr)) = v1.4.2
Provides: bundled(golang(github.com/go_logr/stdr)) = v1.2.2
Provides: bundled(golang(github.com/google/go_cmp)) = v0.6.0
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.20.2
Provides: bundled(golang(github.com/google/shlex)) = v0.0.0_20191202100458_e7afc7fbc510
Provides: bundled(golang(github.com/google/uuid)) = v1.6.0
Provides: bundled(golang(github.com/gorilla/handlers)) = v1.5.1
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.1
Provides: bundled(golang(github.com/gorilla/websocket)) = v1.5.3
Provides: bundled(golang(github.com/gosimple/slug)) = v1.14.0
Provides: bundled(golang(github.com/gosimple/unidecode)) = v1.0.1
Provides: bundled(golang(github.com/grpc_ecosystem/grpc_gateway/v2)) = v2.20.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_cleanhttp)) = v0.5.2
Provides: bundled(golang(github.com/hashicorp/go_immutable_radix/v2)) = v2.1.0
Provides: bundled(golang(github.com/hashicorp/golang_lru/v2)) = v2.0.7
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.1.0
Provides: bundled(golang(github.com/in_toto/in_toto_golang)) = v0.9.0
Provides: bundled(golang(github.com/klauspost/compress)) = v1.17.11
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.6
Provides: bundled(golang(github.com/letsencrypt/boulder)) = v0.0.0_20240620165639_de9c06129bec
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.13
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.20
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.16
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.2
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.12.9
Provides: bundled(golang(github.com/mitchellh/go_homedir)) = v1.1.0
Provides: bundled(golang(github.com/mitchellh/hashstructure/v2)) = v2.0.2
Provides: bundled(golang(github.com/moby/buildkit)) = v0.18.2
Provides: bundled(golang(github.com/moby/docker_image_spec)) = v1.3.1
Provides: bundled(golang(github.com/moby/locker)) = v1.0.1
Provides: bundled(golang(github.com/moby/patternmatcher)) = v0.6.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.7.2
Provides: bundled(golang(github.com/moby/sys/mount)) = v0.3.4
Provides: bundled(golang(github.com/moby/sys/sequential)) = v0.6.0
Provides: bundled(golang(github.com/moby/sys/signal)) = v0.7.1
Provides: bundled(golang(github.com/moby/sys/userns)) = v0.1.0
Provides: bundled(golang(github.com/moby/sys/user)) = v0.3.0
Provides: bundled(golang(github.com/moby/term)) = v0.5.0
Provides: bundled(golang(github.com/morikuni/aec)) = v1.0.0
Provides: bundled(golang(github.com/muesli/cancelreader)) = v0.2.2
Provides: bundled(golang(github.com/munnerz/goautoneg)) = v0.0.0_20191010083416_a7dc8b61c822
Provides: bundled(golang(github.com/Netflix/go_expect)) = v0.0.0_20220104043353_73e0943537d2
Provides: bundled(golang(github.com/networkplumbing/go_nft)) = v0.4.0
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.1.0
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.2.3
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.2.0
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20230914150019_408c51e934dc
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.11.1
Provides: bundled(golang(github.com/opencontainers/umoci)) = v0.4.7
Provides: bundled(golang(github.com/package_url/packageurl_go)) = v0.1.1_0.20220428063043_89078438f170
Provides: bundled(golang(github.com/pelletier/go_toml)) = v1.9.5
Provides: bundled(golang(github.com/pelletier/go_toml/v2)) = v2.2.3
Provides: bundled(golang(github.com/pierrec/lz4/v4)) = v4.1.21
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/planetscale/vtprotobuf)) = v0.6.1_0.20240319094008_0393e58bdf10
Provides: bundled(golang(github.com/pmezard/go_difflib)) = v1.0.1_0.20181226105442_5d4384ee4fb2
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.20.2
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.6.1
Provides: bundled(golang(github.com/prometheus/common)) = v0.57.0
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.15.1
Provides: bundled(golang(github.com/ProtonMail/go_crypto)) = v1.1.3
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.4.7
Provides: bundled(golang(github.com/rootless_containers/proto)) = v0.1.0
Provides: bundled(golang(github.com/russross/blackfriday/v2)) = v2.1.0
Provides: bundled(golang(github.com/safchain/ethtool)) = v0.4.0
Provides: bundled(golang(github.com/samber/lo)) = v1.47.0
Provides: bundled(golang(github.com/sebdah/goldie/v2)) = v2.5.5
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.10.0
Provides: bundled(golang(github.com/secure_systems_lab/go_securesystemslib)) = v0.8.0
Provides: bundled(golang(github.com/sergi/go_diff)) = v1.3.1
Provides: bundled(golang(github.com/shibumi/go_pathspec)) = v1.3.0
Provides: bundled(golang(github.com/shopspring/decimal)) = v1.4.0
Provides: bundled(golang(github.com/sigstore/sigstore)) = v1.8.11
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.3
Provides: bundled(golang(github.com/spdx/tools_golang)) = v0.5.3
Provides: bundled(golang(github.com/spf13/cobra)) = v1.8.1
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stretchr/objx)) = v0.5.2
Provides: bundled(golang(github.com/sylabs/json_resp)) = v0.9.4
Provides: bundled(golang(github.com/sylabs/oci_tools)) = v0.16.1
Provides: bundled(golang(github.com/sylabs/scs_build_client)) = v0.9.15
Provides: bundled(golang(github.com/sylabs/scs_key_client)) = v0.7.7
Provides: bundled(golang(github.com/sylabs/scs_library_client)) = v1.4.11
Provides: bundled(golang(github.com/sylabs/sif/v2)) = v2.20.2
Provides: bundled(golang(github.com/sylabs/squashfs)) = v1.0.4
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/therootcompany/xz)) = v1.0.1
Provides: bundled(golang(github.com/titanous/rocacheck)) = v0.0.0_20171023193734_afe73141d399
Provides: bundled(golang(github.com/tonistiigi/dchapes_mode)) = v0.0.0_20241001053921_ca0759fec205
Provides: bundled(golang(github.com/tonistiigi/fsutil)) = v0.0.0_20241121093142_31cf1f437184
Provides: bundled(golang(github.com/tonistiigi/go_archvariant)) = v1.0.0
Provides: bundled(golang(github.com/tonistiigi/go_csvvalue)) = v0.0.0_20240710180619_ddb21b71c0b4
Provides: bundled(golang(github.com/tonistiigi/units)) = v0.0.0_20180711220420_6950e57a87ea
Provides: bundled(golang(github.com/tonistiigi/vt100)) = v0.0.0_20240514184818_90bafcd6abab
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.12
Provides: bundled(golang(github.com/vbatts/go_mtree)) = v0.5.0
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.6
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = v8.8.3
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.3.0
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.4
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(mvdan.cc/sh/v3)) = v3.10.0
Provides: bundled(golang(sigs.k8s.io/yaml)) = v1.4.0
Provides: bundled(golang(tags.cncf.io/container_device_interface/specs_go)) = v0.8.0
Provides: bundled(golang(tags.cncf.io/container_device_interface)) = v0.8.0

# Multiple packages contain /usr/bin/singularity and /usr/bin/run-singularity,
# which are necessary to run SIF images.  Use a pivot provides/conflicts to
# avoid them all needing to conflict with each other.
Provides: sif-runtime
Conflicts: sif-runtime

# User-choice upgrade path from singularity -> singularity-ce / apptainer.
# https://pagure.io/fesco/issue/2934#comment-839598
Provides: alternative-for(singularity)

%description
SingularityCE is the Community Edition of Singularity, an open source
container platform designed to be simple, fast, and secure.

%prep
%autosetup

%build
# Configure to use distro provided conmon.
# Note --localstatedir= is set to ensure session dir is in /var/lib.
# See discussion at https://bugzilla.redhat.com/show_bug.cgi?id=2145834
./mconfig -V %{version}-%{release} \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_sharedstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --without-conmon \

%make_build -C builddir old_config= V=

%install
%make_install -C builddir V=

%files
%attr(4755, root, root) %{_libexecdir}/singularity/bin/starter-suid
%{_bindir}/singularity
%{_bindir}/run-singularity
%dir %{_libexecdir}/singularity
%dir %{_libexecdir}/singularity/bin
%{_libexecdir}/singularity/bin/singularity-buildkitd
%{_libexecdir}/singularity/bin/squashfuse_ll
%{_libexecdir}/singularity/bin/starter
%dir %{_libexecdir}/singularity/cni
%{_libexecdir}/singularity/cni/*
%dir %{_sysconfdir}/singularity
%config(noreplace) %{_sysconfdir}/singularity/*.conf
%config(noreplace) %{_sysconfdir}/singularity/*.toml
%config(noreplace) %{_sysconfdir}/singularity/*.json
%config(noreplace) %{_sysconfdir}/singularity/*.yaml
%config(noreplace) %{_sysconfdir}/singularity/global-pgp-public
%dir %{_sysconfdir}/singularity/cgroups
%config(noreplace) %{_sysconfdir}/singularity/cgroups/*
%dir %{_sysconfdir}/singularity/network
%config(noreplace) %{_sysconfdir}/singularity/network/*
%dir %{_sysconfdir}/singularity/seccomp-profiles
%config(noreplace) %{_sysconfdir}/singularity/seccomp-profiles/*
%{_datadir}/bash-completion/completions/singularity
%dir %{_sharedstatedir}/singularity
%dir %{_sharedstatedir}/singularity/mnt
%dir %{_sharedstatedir}/singularity/mnt/session
%{_mandir}/man1/singularity*
%license LICENSE.md
%license LICENSE_THIRD_PARTY.md
%license LICENSE_DEPENDENCIES.md
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 David Trudgian <dtrudg@sylabs.io> - 4.2.2-1
- Upgrade to 4.2.2 upstream version.

* Tue Sep 24 2024 David Trudgian <dtrudg@sylabs.io> - 4.2.1-1
- Upgrade to 4.2.1 upstream version.

* Thu Sep 5 2024 David Trudgian <dtrudg@sylabs.io> - 4.2.0-1
- Upgrade to 4.2.0 upstream version.

* Mon Aug 19 2024 David Trudgian <dtrudg@sylabs.io> - 4.1.5-1
- Upgrade to 4.1.5 upstream version.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 3 2024 David Trudgian <dtrudg@sylabs.io> - 4.1.4-1
- Upgrade to 4.1.4 upstream version.

* Thu May 9 2024 David Trudgian <dtrudg@sylabs.io> - 4.1.3-1
- Upgrade to 4.1.3 upstream version.

* Wed Mar 6 2024 David Trudgian <dtrudg@sylabs.io> - 4.1.2-1
- Upgrade to 4.1.2 upstream version.

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 4.1.1-2
- Rebuild for golang 1.22.0

* Thu Feb 1 2024 David Trudgian <dtrudg@sylabs.io> - 4.1.1-1
- Upgrade to 4.1.1 upstream version.

* Mon Jan 29 2024 David Trudgian <dtrudg@sylabs.io> - 4.1.0-1
- Upgrade to 4.1.0 upstream version.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 David Trudgian <dtrudg@sylabs.io> - 4.0.3-1
- Upgrade to 4.0.3 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Thu Nov 16 2023 David Trudgian <dtrudg@sylabs.io> - 4.0.2-1
- Upgrade to 4.0.2 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Mon Oct 16 2023 David Trudgian <dtrudg@sylabs.io> - 4.0.1-1
- Upgrade to 4.0.1 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Mon Oct 9 2023 David Trudgian <dtrudg@sylabs.io> - 4.0.0-1
- Upgrade to 4.0.0 upstream version.

* Mon Sep 18 2023 David Trudgian <dtrudg@sylabs.io> - 3.11.5-1
- Upgrade to 3.11.5 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 David Trudgian <dtrudg@sylabs.io> - 3.11.4-1
- Upgrade to 3.11.4 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Fri May 5 2023 David Trudgian <dtrudg@sylabs.io> - 3.11.3-1
- Upgrade to 3.11.3 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Tue May 2 2023 David Trudgian <dtrudg@sylabs.io> - 3.11.2-1
- Upgrade to 3.11.2 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Tue Mar 14 2023 David Trudgian <dtrudg@sylabs.io> - 3.11.1-1
- Upgrade to 3.11.1 upstream version.
- This is a compatible upgrade to a new upstream patch version.

* Tue Feb 21 2023 David Trudgian <dtrudg@sylabs.io> - 3.11.0-1
- Upgrade to 3.11.0 upstream version.
- This is a compatible upgrade to a new upstream minor version.

* Wed Feb 8 2023 David Trudgian <dtrudg@sylabs.io> - 3.10.5-3
- Add Provides: alternative-for(singularity)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 David Trudgian <dtrudg@sylabs.io> - 3.10.5-1
- Upgrade to 3.10.5 upstream version.
- Addresses CVE-2022-23538 / GHSA-7p8m-22h4-9pj7

* Tue Dec 13 2022 Carl George <carl@george.computer> - 3.10.4-2
- Add pivot provides/conflict of sif-runtime

* Mon Nov 28 2022 David Trudgian <dtrudg@sylabs.io> - 3.10.4-1
- Initial packaging of SingularityCE 3.10.4
