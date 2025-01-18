#
# Copyright (c) Contributors to the Apptainer project, established as
#   Apptainer a Series of LF Projects LLC.
#   For website terms of use, trademark policy, privacy policy and other
#   project policies see https://lfprojects.org/policies
# Copyright (c) 2017-2022, SyLabs, Inc. All rights reserved.
# Copyright (c) 2017, SingularityWare, LLC. All rights reserved.
#
# Copyright (c) 2015-2017, Gregory M. Kurtzer. All rights reserved.
#
# Copyright (c) 2016, The Regents of the University of California, through
# Lawrence Berkeley National Laboratory (subject to receipt of any required
# approvals from the U.S. Dept. of Energy).  All rights reserved.
#
# This software is licensed under a customized 3-clause BSD license.  Please
# consult LICENSE file distributed with the sources of this project regarding
# your rights to use or distribute this software.
#
# NOTICE.  This Software was developed under funding from the U.S. Department of
# Energy and the U.S. Government consequently retains certain rights. As such,
# the U.S. Government has been granted for itself and others acting on its
# behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software
# to reproduce, distribute copies to the public, prepare derivative works, and
# perform publicly and display publicly, and to permit other to do so.
#
#

# Disable debugsource packages; otherwise it ends up with an empty %%files
#   file in debugsourcefiles.list on Fedora
%undefine _debugsource_packages

# This can be slightly different than %%{version}.
# For example, it has dash instead of tilde for release candidates.
%global package_version 1.3.6

%global gocryptfs_version 2.4.0
%global squashfuse_version 0.5.1
%global e2fsprogs_version 1.47.0
%global fuse_overlayfs_version 1.13

# The last singularity version number in EPEL/Fedora
%global last_singularity_version 3.8.7-3

Summary: Application and environment virtualization formerly known as Singularity
Name: apptainer
Version: 1.3.6
Release: 2%{?dist}
# See LICENSE.md for first party code (BSD-3-Clause and LBNL BSD)
# See LICENSE_THIRD_PARTY.md for incorporated code (ASL 2.0)
# See LICENSE_DEPENDENCIES.md for dependencies
# License identifiers taken from: https://fedoraproject.org/wiki/Licensing
# Automatically converted from old format: BSD and LBNL BSD and ASL 2.0 - review is highly recommended.
License: LicenseRef-Callaway-BSD AND BSD-3-Clause-LBNL AND Apache-2.0
URL: https://apptainer.org
Source: https://github.com/%{name}/%{name}/releases/download/v%{package_version}/%{name}-%{package_version}.tar.gz

%if "%{?gocryptfs_version}" != ""
# In order to build offline, this source tarball needs to have the "vendor"
# directory added, which can be done by unpacking it, doing the command
#   go mod vendor
# and then recreating the tarball.  Use scripts/download-dependencies.
Source10: https://github.com/rfjakob/gocryptfs/archive/v%{gocryptfs_version}/gocryptfs-%{gocryptfs_version}.tar.gz
%endif
%if "%{?squashfuse_version}" != ""
Source11: https://github.com/vasi/squashfuse/archive/%{squashfuse_version}/squashfuse-%{squashfuse_version}.tar.gz
%endif
%if "%{?e2fsprogs_version}" != ""
# URL: https://github.com/tytso/e2fsprogs/archive/refs/tags/v%%{e2fsprogs_version}.tar.gz
Source12: e2fsprogs-%{e2fsprogs_version}.tar.gz
# URL: https://github.com/tytso/e2fsprogs/commit/5598a96.patch
Patch121: e2fsprogs-1.patch
# URL: https://github.com/tytso/e2fsprogs/commit/1ac0061.patch
Patch122: e2fsprogs-2.patch
# URL: https://github.com/tytso/e2fsprogs/commit/448a3f8.patch
Patch123: e2fsprogs-3.patch
%endif
Source13: https://github.com/containers/fuse-overlayfs/archive/v%{fuse_overlayfs_version}/fuse-overlayfs-%{fuse_overlayfs_version}.tar.gz

# This Conflicts is in case someone tries to install the main apptainer
# package when an old singularity package is installed.  An Obsoletes is on
# the apptainer-suid subpackage below.  If an Obsoletes were here too, it
# would get different behavior with yum and dnf: a "yum install apptainer"
# on EL7 would install only apptainer but a "dnf install apptainer" on EL8
# or greater would install both apptainer and apptainer-suid.  With this
# Conflicts, both yum and dnf consistently install both apptainer and
# apptainer-suid when apptainer is requested while singularity is installed.
Conflicts: singularity <= %{last_singularity_version}

# In the singularity 2.x series there was a singularity-runtime package
#  that could have been installed independently, but starting in 3.x
#  there was only one package
Obsoletes: singularity-runtime < 3.0

# Multiple packages contain /usr/bin/singularity and /usr/bin/run-singularity,
# which are necessary to run SIF images.  Use a pivot provides/conflicts to
# avoid them all needing to conflict with each other.
Provides: sif-runtime
Conflicts: sif-runtime

Provides: bundled(gocryptfs) = %{gocryptfs_version}
Provides: bundled(squashfuse) = %{squashfuse_version}
Provides: bundled(e2fsprogs) = %{e2fsprogs_version}
Provides: bundled(fuse2fs) = %{e2fsprogs_version}
Provides: bundled(fuse-overlayfs) = %{fuse_overlayfs_version}
Provides: bundled(golang(github.com/AdamKorcz/go_fuzz_headers)) = v0.0.0_20210319161527_f761c2329661
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20230124172434_306776ec8161
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.3.2
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.1
Provides: bundled(golang(github.com/Netflix/go_expect)) = v0.0.0_20220104043353_73e0943537d2
Provides: bundled(golang(github.com/ProtonMail/go_crypto)) = v1.0.0
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/adigunhammedolalekan/registry_auth)) = v0.0.0_20200730122110_8cde180a3a60
Provides: bundled(golang(github.com/alexflint/go_filemutex)) = v1.3.0
Provides: bundled(golang(github.com/apex/log)) = v1.9.0
Provides: bundled(golang(github.com/apptainer/container_key_client)) = v0.8.0
Provides: bundled(golang(github.com/apptainer/container_library_client)) = v1.4.6
Provides: bundled(golang(github.com/apptainer/sif/v2)) = v2.15.2
Provides: bundled(golang(github.com/asaskevich/govalidator)) = v0.0.0_20230301143203_a9d515a09cc2
Provides: bundled(golang(github.com/astromechza/etcpwdparse)) = v0.0.0_20170319193008_f0e5f0779716
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/blang/semver/v4)) = v4.0.0
Provides: bundled(golang(github.com/buger/goterm)) = v1.0.4
Provides: bundled(golang(github.com/buger/jsonparser)) = v1.1.1
Provides: bundled(golang(github.com/cenkalti/backoff/v4)) = v4.2.1
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.2.0
Provides: bundled(golang(github.com/cilium/ebpf)) = v0.9.1
Provides: bundled(golang(github.com/cloudflare/circl)) = v1.3.7
Provides: bundled(golang(github.com/containerd/containerd)) = v1.7.11
Provides: bundled(golang(github.com/containerd/log)) = v0.1.0
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.15.1
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.1.2
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.4.1
Provides: bundled(golang(github.com/containers/image/v5)) = v5.30.1
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20230121012942_c1716e8a8d01
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.10
Provides: bundled(golang(github.com/containers/storage)) = v1.53.0
Provides: bundled(golang(github.com/coreos/go_iptables)) = v0.7.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.5.0
Provides: bundled(golang(github.com/cpuguy83/go_md2man/v2)) = v2.0.3
Provides: bundled(golang(github.com/creack/pty)) = v1.1.21
Provides: bundled(golang(github.com/cyberphone/json_canonicalization)) = v0.0.0_20231217050601_ba74d44ecf5f
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.5
Provides: bundled(golang(github.com/d2g/dhcp4)) = v0.0.0_20170904100407_a1d1b6c41b1c
Provides: bundled(golang(github.com/d2g/dhcp4client)) = v1.0.0
Provides: bundled(golang(github.com/distribution/reference)) = v0.5.0
Provides: bundled(golang(github.com/docker/cli)) = v25.0.4+incompatible
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.3+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v25.0.5+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.8.1
Provides: bundled(golang(github.com/docker/go_connections)) = v0.5.0
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/docker/libtrust)) = v0.0.0_20160708172513_aabc10ec26b7
Provides: bundled(golang(github.com/fatih/color)) = v1.16.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = v1.0.4
Provides: bundled(golang(github.com/garyburd/redigo)) = v0.0.0_20150301180006_535138d7bcd7
Provides: bundled(golang(github.com/go_jose/go_jose/v3)) = v3.0.3
Provides: bundled(golang(github.com/go_log/log)) = v0.2.0
Provides: bundled(golang(github.com/go_logr/logr)) = v1.4.1
Provides: bundled(golang(github.com/go_logr/stdr)) = v1.2.2
Provides: bundled(golang(github.com/go_openapi/analysis)) = v0.21.4
Provides: bundled(golang(github.com/go_openapi/errors)) = v0.21.1
Provides: bundled(golang(github.com/go_openapi/jsonpointer)) = v0.19.6
Provides: bundled(golang(github.com/go_openapi/jsonreference)) = v0.20.2
Provides: bundled(golang(github.com/go_openapi/loads)) = v0.21.2
Provides: bundled(golang(github.com/go_openapi/runtime)) = v0.26.0
Provides: bundled(golang(github.com/go_openapi/spec)) = v0.20.9
Provides: bundled(golang(github.com/go_openapi/strfmt)) = v0.22.2
Provides: bundled(golang(github.com/go_openapi/swag)) = v0.22.10
Provides: bundled(golang(github.com/go_openapi/validate)) = v0.22.1
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.3
Provides: bundled(golang(github.com/google/go_cmp)) = v0.6.0
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.19.1
Provides: bundled(golang(github.com/google/uuid)) = v1.6.0
Provides: bundled(golang(github.com/gorilla/handlers)) = v1.5.1
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.1
Provides: bundled(golang(github.com/gosimple/slug)) = v1.14.0
Provides: bundled(golang(github.com/gosimple/unidecode)) = v1.0.1
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.1.0
Provides: bundled(golang(github.com/josharian/intern)) = v1.0.0
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = v1.17.7
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.6
Provides: bundled(golang(github.com/letsencrypt/boulder)) = v0.0.0_20230907030200_6d76a0f91e1e
Provides: bundled(golang(github.com/mailru/easyjson)) = v0.7.7
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.13
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.20
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.15
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/mattn/go_sqlite3)) = v1.14.22
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = v1.0.4
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.1.1
Provides: bundled(golang(github.com/mitchellh/go_homedir)) = v1.1.0
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = v1.5.0
Provides: bundled(golang(github.com/moby/patternmatcher)) = v0.5.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.7.1
Provides: bundled(golang(github.com/moby/sys/sequential)) = v0.5.0
Provides: bundled(golang(github.com/moby/sys/user)) = v0.1.0
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/networkplumbing/go_nft)) = v0.4.0
Provides: bundled(golang(github.com/oklog/ulid)) = v1.3.1
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.1.0
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.12
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.2.0
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20221107090550_2e043c6bd626
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.11.0
Provides: bundled(golang(github.com/opencontainers/umoci)) = v0.4.7
Provides: bundled(golang(github.com/pelletier/go_toml/v2)) = v2.1.1
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.3
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.17.0
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.5.0
Provides: bundled(golang(github.com/prometheus/common)) = v0.44.0
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.11.1
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.4.7
Provides: bundled(golang(github.com/rootless_containers/proto)) = v0.1.0
Provides: bundled(golang(github.com/russross/blackfriday/v2)) = v2.1.0
Provides: bundled(golang(github.com/safchain/ethtool)) = v0.3.0
Provides: bundled(golang(github.com/samber/lo)) = v1.39.0
Provides: bundled(golang(github.com/seccomp/containers_golang)) = v0.6.0
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.10.0
Provides: bundled(golang(github.com/secure_systems_lab/go_securesystemslib)) = v0.8.0
Provides: bundled(golang(github.com/shopspring/decimal)) = v1.3.1
Provides: bundled(golang(github.com/sigstore/fulcio)) = v1.4.3
Provides: bundled(golang(github.com/sigstore/rekor)) = v1.2.2
Provides: bundled(golang(github.com/sigstore/sigstore)) = v1.8.3
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.3
Provides: bundled(golang(github.com/spf13/cobra)) = v1.8.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20201008174630_78d3cae3a980
Provides: bundled(golang(github.com/sylabs/json_resp)) = v0.9.2
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/titanous/rocacheck)) = v0.0.0_20171023193734_afe73141d399
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.11
Provides: bundled(golang(github.com/urfave/cli)) = v1.22.14
Provides: bundled(golang(github.com/vbatts/go_mtree)) = v0.5.0
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.5
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = v8.7.3
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.2.1_beta.2
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.4
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(go.mongodb.org/mongo_driver)) = v1.14.0
Provides: bundled(golang(go.mozilla.org/pkcs7)) = v0.0.0_20210826202110_33d05740a352
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = v0.45.0
Provides: bundled(golang(go.opentelemetry.io/otel)) = v1.19.0
Provides: bundled(golang(go.opentelemetry.io/otel/metric)) = v1.19.0
Provides: bundled(golang(go.opentelemetry.io/otel/trace)) = v1.19.0
Provides: bundled(golang(golang.org/x/crypto)) = v0.22.0
Provides: bundled(golang(golang.org/x/exp)) = v0.0.0_20240222234643_814bf88cf225
Provides: bundled(golang(golang.org/x/mod)) = v0.15.0
Provides: bundled(golang(golang.org/x/net)) = v0.22.0
Provides: bundled(golang(golang.org/x/sync)) = v0.6.0
Provides: bundled(golang(golang.org/x/sys)) = v0.19.0
Provides: bundled(golang(golang.org/x/term)) = v0.19.0
Provides: bundled(golang(golang.org/x/text)) = v0.14.0
Provides: bundled(golang(golang.org/x/tools)) = v0.18.0
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc)) = v0.0.0_20240123012728_ef4313101c80
Provides: bundled(golang(google.golang.org/grpc)) = v1.62.0
Provides: bundled(golang(google.golang.org/protobuf)) = v1.33.0
Provides: bundled(golang(gopkg.in/go_jose/go_jose.v2)) = v2.6.3
Provides: bundled(golang(gopkg.in/yaml.v2)) = v2.4.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = v3.0.1
Provides: bundled(golang(gotest.tools/v3)) = v3.5.1
Provides: bundled(golang(mvdan.cc/sh/v3)) = v3.7.1_0.20231014181306_8b673862efc6

%if "%{_target_vendor}" == "suse"
BuildRequires: binutils-gold
%endif
BuildRequires: golang
BuildRequires: git
BuildRequires: gcc
BuildRequires: make
BuildRequires: libseccomp-devel
BuildRequires: cryptsetup
BuildRequires: fuse3-devel
%if ("%{?squashfuse_version}" != "") || ("%{e2fsprogs_version}" != "") || ("%{fuse_overlayfs_version}" != "")
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: zlib-devel
%endif
%if "%{_target_vendor}" == "suse"
Requires: squashfs
Recommends: fakeroot
%else
Requires: squashfs-tools
Requires: fakeroot
%endif

%description
Apptainer provides functionality to make portable
containers that can be used across host environments.

%package suid
Summary: Setuid component of Apptainer
Requires: %{name} = %{version}-%{release}
# The singularity package was renamed to apptainer.  The Obsoletes is
# on this subpackage for greater compatibility after an update from the
# old singularity.
Obsoletes: singularity <= %{last_singularity_version}
# FESCo asked to have this form of Provides
Provides: alternative-for(singularity)

%description suid
Provides the optional setuid-root portion of Apptainer.

%prep
%setup -n %{name}-%{package_version}
# don't need to setup dependent source packages and patches because
# that is done by the compile-dependencies script

%build
%if "%{?SOURCE1}" != ""
GOVERSION="$(echo %SOURCE1|sed 's,.*/,,;s/go//;s/\.src.*//')"
if ! ./mlocal/scripts/check-min-go-version go $GOVERSION; then
	# build the go tool chain, the existing version is too old
	pushd ..
	tar -xf %SOURCE1
	cd go/src
	./make.bash
	cd ../..
	export PATH=$PWD/go/bin:$PATH
	popd
fi
%endif

./scripts/compile-dependencies $(dirname %{SOURCE10})

# Not all of these parameters currently have an effect, but they might be
#  used someday.  They are the same parameters as in the configure macro.
./mconfig %{?mconfig_opts} -V %{version}-%{release} --with-suid \
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
        --infodir=%{_infodir}

%make_build -C builddir V= old_config=

%install
%if "%{?SOURCE1}" != ""
export PATH=$PWD/go/bin:$PATH
%endif

%make_install -C builddir V=

%if "%{?gocryptfs_version}" != ""
install -m 755 gocryptfs-%{gocryptfs_version}/gocryptfs %{buildroot}%{_libexecdir}/%{name}/bin/gocryptfs
%endif

%if "%{?squashfuse_version}" != ""
install -m 755 squashfuse-%{squashfuse_version}/squashfuse_ll %{buildroot}%{_libexecdir}/%{name}/bin/squashfuse_ll
%endif

%if "%{?e2fsprogs_version}" != ""
install -m 755 e2fsprogs-%{e2fsprogs_version}/fuse2fs %{buildroot}%{_libexecdir}/%{name}/bin/fuse2fs
%endif

%if "%{?fuse_overlayfs_version}" != ""
install -m 755 fuse-overlayfs-%{fuse_overlayfs_version}/fuse-overlayfs %{buildroot}%{_libexecdir}/%{name}/bin/fuse-overlayfs
%endif

%post
# $1 in %%posttrans cannot distinguish between fresh installs and upgrades,
# so check it here and create a file to pass the knowledge to that step
if [ "$1" -eq 1 ] && [ -d %{_sysconfdir}/singularity ]; then
	touch %{_sysconfdir}/%{name}/.singularityupgrade
fi

%posttrans
# clean out empty directories under /etc/singularity
rmdir %{_sysconfdir}/singularity/* %{_sysconfdir}/singularity 2>/dev/null || true
if [ -f %{_sysconfdir}/%{name}/.singularityupgrade ]; then
	pushd %{_sysconfdir}/%{name} >/dev/null
	rm .singularityupgrade
	# This is the first install of apptainer after removal of singularity.
	# Import any singularity configurations that remain, which were left
	# because they were non-default.
	find %{_sysconfdir}/singularity ! -type d 2>/dev/null|while read F; do
		B="$(echo $F|sed 's,%{_sysconfdir}/singularity/,,;s/\.rpmsave//')"
		if [ "$B" == singularity.conf ]; then
			echo "info: renaming $PWD/%{name}.conf to $PWD/%{name}.conf.rpmorig" >&2
			mv %{name}.conf %{name}.conf.rpmorig
			echo "info: converting configuration from $F into $PWD/%{name}.conf" >&2
			%{_bindir}/%{name} confgen $F %{name}.conf
		elif [ "$B" == remote.yaml ]; then
			echo "info: renaming $PWD/$B to $PWD/$B.rpmorig" >&2
			mv $B $B.rpmorig
			echo "info: merging $F into $PWD/$B" >&2
			(
			sed -n '1p' $F
			sed -n '2,$p' $B.rpmorig
			sed -n '3,$p' $F
			) >$B
		else
			if [ -f "$B" ]; then
				echo "info: renaming $PWD/$B to $PWD/$B.rpmorig" >&2
				mv $B $B.rpmorig
			fi
			echo "info: copying $F into $PWD/$B" >&2
			cp $F $B
		fi
	done
	popd >/dev/null
fi

# Define `%%license` tag if not already defined.
# This is needed for EL 7 compatibility.
%{!?_licensedir:%global license %doc}

%files
%{_bindir}/%{name}
%{_bindir}/singularity
%{_bindir}/run-singularity
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/bin
%{_libexecdir}/%{name}/bin/starter
%if "%{?gocryptfs_version}" != ""
%{_libexecdir}/%{name}/bin/gocryptfs
%endif
%if "%{?squashfuse_version}" != ""
%{_libexecdir}/%{name}/bin/squashfuse_ll
%endif
%if "%{?e2fsprogs_version}" != ""
%{_libexecdir}/%{name}/bin/fuse2fs
%endif
%if "%{?fuse_overlayfs_version}" != ""
%{_libexecdir}/%{name}/bin/fuse-overlayfs
%endif
%{_libexecdir}/%{name}/cni
%{_libexecdir}/%{name}/lib
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/bash-completion/completions/*
%dir %{_sharedstatedir}/%{name}
%dir %{_sharedstatedir}/%{name}/mnt
%dir %{_sharedstatedir}/%{name}/mnt/session
%{_mandir}/man1/%{name}*
%{_mandir}/man1/singularity*
%license LICENSE.md
%license LICENSE_THIRD_PARTY.md
%license LICENSE_DEPENDENCIES.md
%doc README.md
%doc CHANGELOG.md

%files suid
%attr(4755, root, root) %{_libexecdir}/%{name}/bin/starter-suid

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec  4 2024 Dave Dykstra <dwd@cern.ch> - 1.3.6
- Update to upstream 1.3.6

* Wed Oct 30 2024 Dave Dykstra <dwd@cern.ch> - 1.3.5
- Update to upstream 1.3.5

* Thu Sep  5 2024 Dave Dykstra <dwd@cern.ch> - 1.3.4
- Update to upstream 1.3.4

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.3-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul  3 2024 Dave Dykstra <dwd@cern.ch> - 1.3.3
- Update to upstream 1.3.3

* Tue May 28 2024 Dave Dykstra <dwd@cern.ch> - 1.3.2
- Update to upstream 1.3.2

* Wed Apr 24 2024 Dave Dykstra <dwd@fnal.gov> - 1.3.1
- Update to upstream 1.3.1

* Wed Mar 13 2024 Dave Dykstra <dwd@fnal.gov> - 1.3.0
- Update to upstream 1.3.0

* Thu Feb 15 2024 Dave Dykstra <dwd@fnal.gov> - 1.3.0~rc.2
- Update to upstream 1.3.0-rc.2

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 1.3.0~rc.1-4
- Rebuild for golang 1.22.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0~rc.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0~rc.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Dave Dykstra <dwd@fnal.gov> - 1.3.0~rc.1
- Update to upstream 1.3.0-rc.1

* Wed Nov 22 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.5
- Update to upstream 1.2.5

* Wed Oct 11 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.4
- Update to upstream 1.2.4

* Thu Sep 14 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.3
- Update to upstream 1.2.3

* Thu Jul 27 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.2
- Update to upstream 1.2.2

* Mon Jul 24 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.1
- Update to upstream 1.2.1

* Wed Jul 19 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.0
- Update to upstream 1.2.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0~rc.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul  6 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.0~rc.1-2
- Update to upstream 1.2.0-rc.2

* Thu Jun  8 2023 Dave Dykstra <dwd@fnal.gov> - 1.2.0~rc.1-1
- Update to upstream 1.2.0-rc.1

* Wed Jun  7 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.9-1
- Update to upstream 1.1.9.

* Tue Apr 25 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.8-1
- Update to upstream 1.1.8, a security release.

* Wed Mar 29 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.7-1
- Update to upstream 1.1.7.

* Tue Feb 14 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.6-1
- Update to upstream 1.1.6.

* Thu Feb  9 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.5-3
- Add Provides: alternative-for(singularity) to apptainer-suid package.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.5-1
- Update to upstream 1.1.5, including changing the obsoletes on the main
  apptainer package to conflicts.

* Wed Jan  4 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.4-3
- Restore the singularity obsoletes on the apptainer main package, so
  that now it is on both the main package and suid subpackage.

* Wed Dec 14 2022 Carl George <carl@george.computer> - 1.1.4-2
- Add pivot provides/conflict of sif-runtime
- Reduce singularity obsoletes upper bound
- Remove singularity provides due to incompatibilities introduced in apptainer
- Add the word singularity to the summary so it shows up in dnf search results
- Move obsoletes to suid subpackage

* Tue Dec 13 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.4
- Update to upstream 1.1.4.

* Wed Dec  7 2022 Florian Weimer <fweimer@redhat.com> - 1.1.3-2
- Port squashfuse configure script to C99

* Tue Oct 25 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.3
- Update to upstream 1.1.3.

* Thu Oct 06 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.2
- Update to upstream 1.1.2.

* Tue Sep 27 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0
- Update to upstream 1.1.0.  Uncomment the requiring of fuse2fs on el7.

* Tue Sep 06 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0-rc.3
- Update to upstream 1.1.0~rc.3.  Uncomment setting squashfuse_version and
  the requiring of fuse2fs on el7.

* Thu Sep 01 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0-rc.2+37-g1f91ff3
- Test build

* Wed Aug 17 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0~rc.2
- Update to upstream 1.1.0~rc.2.  Remove customizations put into
  1.1.0-rc.1 packaging except for f35 inclusion of golang source.

* Tue Aug  2 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0~rc.1-2
- Add patch for 32-bit compilation

* Tue Aug  2 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0~rc.1
- Update to upstream 1.1.0~rc.1
- Require fuse2fs package on el7
- Require fuse-overlayfs everywhere for cases that kernel overlayfs
  does not support 

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul  6 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.3
- Update to upstream 1.0.3

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-2
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Tue May 10 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.2
- Update to upstream 1.0.2

* Wed Mar 16 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.1
- Update to upstream 1.0.1
- Remove patch from pr 299, not needed anymore

* Thu Mar 03 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.0
- Initial release from upstream 1.0.0
