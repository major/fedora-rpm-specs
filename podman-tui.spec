%global with_check 0
%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global goipath github.com/containers/podman-tui
Version: 0.5.0
%global tag v0.5.0
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
Source0: %{gosource}

BuildRequires: gcc
BuildRequires: golang >= 1.18.2
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git-core
BuildRequires: go-rpm-macros
BuildRequires: make
BuildRequires: gpgme-devel
BuildRequires: device-mapper-devel
BuildRequires: libassuan-devel
%if ! 0%{?centos}
BuildRequires: btrfs-progs-devel
%endif
%if 0%{?fedora} >= 35
BuildRequires: shadow-utils-subid-devel
%endif

# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/blang/semver)) = v3.5.1+incompatible
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.1.0
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.1.2
Provides: bundled(golang(github.com/chzyer/readline)) = v0.0.0_20180603132655_2972be24d48e
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.3
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.4
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.11.4
Provides: bundled(golang(github.com/containers/buildah)) = v1.26.1
Provides: bundled(golang(github.com/containers/common)) = v0.48.0
Provides: bundled(golang(github.com/containers/image/v5)) = v5.21.1
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20200511145503_9c3a6c22cd9a
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.4
Provides: bundled(golang(github.com/containers/podman/v4)) = v4.1.1
Provides: bundled(golang(github.com/containers/psgo)) = v1.7.2
Provides: bundled(golang(github.com/containers/storage)) = v1.41.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.3_0.20220203105225_a9a7ef127534
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/disiqueira/gotree/v3)) = v3.0.2
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.1+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.6.4
Provides: bundled(golang(github.com/docker/docker)) = v20.10.17+incompatible
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.1_0.20210727194412_58542c764a11
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/docker/go_units)) = v0.4.0
Provides: bundled(golang(github.com/docker/libnetwork)) = v0.8.0_dev.2.0.20190625141545_5a177b73e316
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.5.4
Provides: bundled(golang(github.com/gdamore/encoding)) = v1.0.0
Provides: bundled(golang(github.com/gdamore/tcell/v2)) = v2.4.1_0.20210905002822_f057f0a857a1
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/google/go_intervals)) = v0.0.2
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.0
Provides: bundled(golang(github.com/gorilla/schema)) = v1.2.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/hinshun/vt10x)) = v0.0.0_20220301184237_5011da428d02
Provides: bundled(golang(github.com/imdario/mergo)) = v0.3.12
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.0
Provides: bundled(golang(github.com/jinzhu/copier)) = v0.3.5
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = v1.15.4
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.5
Provides: bundled(golang(github.com/lucasb_eyer/go_colorful)) = v1.2.0
Provides: bundled(golang(github.com/manifoldco/promptui)) = v0.9.0
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.12
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.14
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.13
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = v1.0.2_0.20181231171920_c182affec369
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.5.2
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.2
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.1.1
Provides: bundled(golang(github.com/mistifyio/go_zfs)) = v2.1.2_0.20190413222219_f784269be439+incompatible
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.6.1
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20210619224110_3f7ff695adc6
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/navidys/tvxwidgets)) = v0.1.0
Provides: bundled(golang(github.com/nxadm/tail)) = v1.4.8
Provides: bundled(golang(github.com/onsi/ginkgo/v2)) = v2.1.4
Provides: bundled(golang(github.com/onsi/gomega)) = v1.19.0
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.3_0.20220114050600_8b9d41f48198
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.1
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20211214071223_8958f93039ab
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20220110225228_7e2d60f1e41f
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.1
Provides: bundled(golang(github.com/ostreedev/ostree_go)) = v0.0.0_20210805093236_719684c64e4f
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.1
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.11.1
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.2.0
Provides: bundled(golang(github.com/prometheus/common)) = v0.30.0
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.7.3
Provides: bundled(golang(github.com/rivo/tview)) = v0.0.0_20220307222120_9994674d60a8
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.2.0
Provides: bundled(golang(github.com/rs/zerolog)) = v1.27.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/spf13/cobra)) = v1.5.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20201008174630_78d3cae3a980
Provides: bundled(golang(github.com/sylabs/sif/v2)) = v2.7.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/tchap/go_patricia)) = v2.3.0+incompatible
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.10
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.4.1
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0

%description
%{common_description}

%prep
%goprep

mkdir _depbundle
pushd _depbundle
/usr/bin/gzip -dc %{SOURCE0} | /usr/bin/tar -xof -
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
%{__install} -m 0755 -vd %{gobuilddir}/src/
# copy required bundled libraries
%{__cp} -rp %{goname}-%{version}/vendor/* %{gobuilddir}/src/
popd
%{_bindir}/rm -rf _depbundle

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}/

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if 0%{?with_check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc     
%{_bindir}/*

%changelog
%autochangelog