# Disable debugsource packages; otherwise it ends up with an empty %%files
# file in debugsourcefiles.list on Fedora
%undefine _debugsource_packages

Name: singularity-ce
Version: 3.10.5
Release: 2%{?dist}
Summary: Application and environment virtualization

# See LICENSE.md for first party code (BSD-3-Clause and BSD-3-Clause-LBNL)
# See LICENSE_THIRD_PARTY.md for incorporated code (Apache-2.0)
# See LICENSE_DEPENDENCIES.md for bundled dependencies
# License identifiers taken from: https://fedoraproject.org/wiki/Licensing
License: BSD-3-Clause AND BSD-3-Clause-LBNL AND Apache-2.0

URL: https://www.sylabs.io/singularity/
Source: https://github.com/sylabs/singularity/releases/download/v%{version}/singularity-ce-%{version}.tar.gz

BuildRequires: golang >= 1.18
BuildRequires: gcc
BuildRequires: make
BuildRequires: libseccomp-devel
BuildRequires: glib2-devel
# Paths to runtime dependencies detected by mconfig, so must be present at build time.
BuildRequires: cryptsetup
BuildRequires: squashfs-tools

Requires: conmon >= 2.0.24
Requires: cryptsetup
Requires: runc
Requires: shadow-utils
Requires: squashfs-tools

ExclusiveArch: %{go_arches}

# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/AdamKorcz/go_fuzz_headers)) = v0.0.0_20210319161527_f761c2329661
Provides: bundled(golang(github.com/adigunhammedolalekan/registry_auth)) = v0.0.0_20200730122110_8cde180a3a60
Provides: bundled(golang(github.com/alexflint/go_filemutex)) = v1.1.0
Provides: bundled(golang(github.com/apex/log)) = v1.9.0
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/blang/semver)) = v3.5.1+incompatible
Provides: bundled(golang(github.com/blang/semver/v4)) = v4.0.0
Provides: bundled(golang(github.com/buger/jsonparser)) = v1.1.1
Provides: bundled(golang(github.com/bugsnag/bugsnag_go)) = v1.5.1
Provides: bundled(golang(github.com/bugsnag/panicwrap)) = v1.2.0
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.2.0
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.1.2
Provides: bundled(golang(github.com/cilium/ebpf)) = v0.7.0
Provides: bundled(golang(github.com/cloudflare/circl)) = v1.1.0
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.4
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.15
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.1.2
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.1.1
Provides: bundled(golang(github.com/containers/common)) = v0.50.1
Provides: bundled(golang(github.com/containers/image/v5)) = v5.23.1
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20200511145503_9c3a6c22cd9a
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.5
Provides: bundled(golang(github.com/containers/storage)) = v1.43.0
Provides: bundled(golang(github.com/coreos/go_iptables)) = v0.6.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.4.0
Provides: bundled(golang(github.com/cpuguy83/go_md2man/v2)) = v2.0.2
Provides: bundled(golang(github.com/creack/pty)) = v1.1.18
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/d2g/dhcp4client)) = v1.0.0
Provides: bundled(golang(github.com/d2g/dhcp4)) = v0.0.0_20170904100407_a1d1b6c41b1c
Provides: bundled(golang(github.com/docker/cli)) = v20.10.21+incompatible
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.1+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.7.0
Provides: bundled(golang(github.com/docker/docker)) = v20.10.22+incompatible
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.0
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/docker/libtrust)) = v0.0.0_20160708172513_aabc10ec26b7
Provides: bundled(golang(github.com/fatih/color)) = v1.13.0
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/gofrs/uuid)) = v4.0.0+incompatible
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/go_log/log)) = v0.2.0
Provides: bundled(golang(github.com/google/go_cmp)) = v0.5.9
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.12.1
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.0
Provides: bundled(golang(github.com/gorilla/websocket)) = v1.5.0
Provides: bundled(golang(github.com/gosimple/slug)) = v1.13.1
Provides: bundled(golang(github.com/gosimple/unidecode)) = v1.0.1
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.1
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/kardianos/osext)) = v0.0.0_20190222173326_2bc1f35cddc0
Provides: bundled(golang(github.com/klauspost/compress)) = v1.15.11
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.5
Provides: bundled(golang(github.com/kr/pty)) = v1.1.8
Provides: bundled(golang(github.com/letsencrypt/boulder)) = v0.0.0_20221109233200_85aa52084eaf
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.13
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.16
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.14
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = v1.0.4
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.0
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.6
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.1.1
Provides: bundled(golang(github.com/moby/locker)) = v1.0.1
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.6.2
Provides: bundled(golang(github.com/moby/sys/mount)) = v0.2.0
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20221205130635_1aeaba878587
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/morikuni/aec)) = v1.0.0
Provides: bundled(golang(github.com/Netflix/go_expect)) = v0.0.0_20190729225929_0e00d9168667
Provides: bundled(golang(github.com/networkplumbing/go_nft)) = v0.2.0
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.1.0_rc2
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.4
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20210326190908_1c3f411f0417
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20220714195903_17b3287fafb7
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.2
Provides: bundled(golang(github.com/opencontainers/umoci)) = v0.4.7
Provides: bundled(golang(github.com/pelletier/go_toml)) = v1.9.5
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.3
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.13.0
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.3.0
Provides: bundled(golang(github.com/prometheus/common)) = v0.37.0
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.8.0
Provides: bundled(golang(github.com/ProtonMail/go_crypto)) = v0.0.0_20221026131551_cf6655e29de4
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.2.0
Provides: bundled(golang(github.com/rootless_containers/proto)) = v0.1.0
Provides: bundled(golang(github.com/russross/blackfriday/v2)) = v2.1.0
Provides: bundled(golang(github.com/safchain/ethtool)) = v0.0.0_20210803160452_9aa261dae9b1
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.10.0
Provides: bundled(golang(github.com/secure_systems_lab/go_securesystemslib)) = v0.4.0
Provides: bundled(golang(github.com/shopspring/decimal)) = v1.3.1
Provides: bundled(golang(github.com/sigstore/sigstore)) = v1.4.6
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.0
Provides: bundled(golang(github.com/spf13/cobra)) = v1.6.1
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20201008174630_78d3cae3a980
Provides: bundled(golang(github.com/sylabs/json_resp)) = v0.8.2
Provides: bundled(golang(github.com/sylabs/scs_build_client)) = v0.7.5
Provides: bundled(golang(github.com/sylabs/scs_key_client)) = v0.7.2
Provides: bundled(golang(github.com/sylabs/scs_library_client)) = v1.4.2
Provides: bundled(golang(github.com/sylabs/sif/v2)) = v2.9.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/theupdateframework/go_tuf)) = v0.5.2_0.20220930112810_3890c1e7ace4
Provides: bundled(golang(github.com/titanous/rocacheck)) = v0.0.0_20171023193734_afe73141d399
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.10
Provides: bundled(golang(github.com/urfave/cli)) = v1.22.5
Provides: bundled(golang(github.com/vbatts/go_mtree)) = v0.5.0
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.5.3
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = v8.1.4
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.1.1_0.20210330154013_f5de75959ad5
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.0_20210104183010_2eb08e3e575f
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(github.com/yvasiyarov/go_metrics)) = v0.0.0_20150112132944_c25f46c4b940
Provides: bundled(golang(github.com/yvasiyarov/gorelic)) = v0.0.6
Provides: bundled(golang(github.com/yvasiyarov/newrelic_platform_go)) = v0.0.0_20160601141957_9c099fbc30e9
Provides: bundled(golang(mvdan.cc/sh/v3)) = v3.6.0
Provides: bundled(golang(oras.land/oras_go)) = v1.2.2

# Multiple packages contain /usr/bin/singularity and /usr/bin/run-singularity,
# which are necessary to run SIF images.  Use a pivot provides/conflicts to
# avoid them all needing to conflict with each other.
Provides: sif-runtime
Conflicts: sif-runtime

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
        --without-conmon

%make_build -C builddir old_config= V=

%install
%make_install -C builddir V=

%files
%attr(4755, root, root) %{_libexecdir}/singularity/bin/starter-suid
%{_bindir}/singularity
%{_bindir}/run-singularity
%dir %{_libexecdir}/singularity
%dir %{_libexecdir}/singularity/bin
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
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/*
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
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 David Trudgian <dtrudg@sylabs.io> - 3.10.5-1
- Upgrade to 3.10.5 upstream version.
- Addresses CVE-2022-23538 / GHSA-7p8m-22h4-9pj7

* Tue Dec 13 2022 Carl George <carl@george.computer> - 3.10.4-2
- Add pivot provides/conflict of sif-runtime

* Mon Nov 28 2022 David Trudgian <dtrudg@sylabs.io> - 3.10.4-1
- Initial packaging of SingularityCE 3.10.4
