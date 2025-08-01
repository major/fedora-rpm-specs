# Generated by go2rpm 1.14.0.post0
# With manual changes by maintainer

# Do not edit this spec file. (Re-)Generate using newrelease

%bcond check 1

# **** release metadata ****
# populated by envsubst in newrelease
%global crio_spec_name  cri-o1.32
%global crio_spec_ver   1.32.6
# Uncomment if needed for commit based release
# %%global crio_commit     
%global crio_tag        v1.32.6
%global golangver       1.23.4

# Related: github.com/cri-o/cri-o/issues/3684
%global build_timestamp %(date -u +'%Y-%m-%dT%H:%M:%SZ')_Release:%{release}

# set service name - removes dash from cri-o
%global service_name    crio

# Commit for the builds
# Uncomment if needed for commit based release
# %%global commit0 %%{crio_commit}
%{?crio_commit:%global commit0 %{crio_commit}}

# https://github.com/cri-o/cri-o
%global goipath           github.com/cri-o/cri-o
Version:                  %{crio_spec_ver}
%{!?commit0:%global tag   %{crio_tag}}

%gometa -L -f

%global common_description %{expand:
Open Container Initiative-based implementation of Kubernetes Container Runtime
Interface.}

Name:           %{crio_spec_name}
Release:        %autorelease
Summary:        Open Container Initiative-based implementation of Kubernetes Container Runtime Interface

# Generated by go-vendor-tools
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        %{gosource}
# Generated by go-vendor-tools
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml

BuildRequires:  golang >= %{golangver}
BuildRequires:  go-vendor-tools
BuildRequires:  btrfs-progs-devel
BuildRequires:  device-mapper-devel
BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-static
BuildRequires:  go-md2man
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
BuildRequires:  libseccomp-devel
BuildRequires:  marshalparser
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  runc
BuildRequires:  crun
BuildRequires:  conmon >= 2.0.2-1
BuildRequires:  iptables
Requires(pre):  container-selinux
Requires:       containers-common >= 1:0.1.31-14
Recommends:     crun
Suggests:       containernetworking-plugins >= 1.0.0-1
Requires:       conmon >= 2.0.2-1
Requires:       socat
Requires:       iptables

Obsoletes:      ocid <= 0.3
Provides:       ocid = %{version}-%{release}

# block install of other versioned cri-o rpms
Provides:       %{service_name} = %{version}-%{release}
Conflicts:      %{service_name}

%description %{common_description}

# **********************************
%prep
%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
# %%autopatch -p1

%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}

# remove local from service file path
sed -i 's/\/local//' contrib/systemd/%{service_name}.service
sed -i 's/\/local//' contrib/systemd/%{service_name}-wipe.service

# **********************************
%build

# See https://github.com/cri-o/cri-o/issues/8860. The linker setting
# resolves the error noted in this issue. See
# /usr/share/doc/redhat-rpm-config/buildflags.md for more information.
%global __golang_extldflags -Wl,-z,undefs

# buildtags, create global to reuse in check section
%global buildtags  $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh) $(hack/seccomp_tag.sh) $(hack/selinux_tag.sh) $(hack/libsubid_tag.sh) exclude_graphdriver_devicemapper

export GO_BUILDTAGS="%{buildtags}"
export GO_LDFLAGS=" -X  %{goipath}/internal/version.buildDate=%{build_timestamp} "

# remove default go macro ldflag settings for version, tag, commit
%global currentgoldflags   %{nil}

# crio currently only subdirectory
%gobuild -o %{gobuilddir}/bin/%{service_name} %{goipath}/cmd/%{service_name}
# for cmd in cmd/* ; do
#  %%gobuild -trimpath -o %%{gobuilddir}/bin/$(basename $cmd) %%{goipath}/$cmd
# done

# generate pinns
%if 0%{?fedora}
%set_build_flags
%endif
export CFLAGS="$CFLAGS -std=c99"
%make_build bin/pinns

# generate man pages
GO_MD2MAN=go-md2man %make_build docs


# **********************************
%install

# generate systemd unit files
sed -i 's/\/local//' contrib/systemd/%{service_name}.service
%{gobuilddir}/bin/%{service_name} \
      --selinux \
      --cni-plugin-dir /opt/cni/bin \
      --cni-plugin-dir "%{_libexecdir}/cni" \
      --enable-metrics \
      --metrics-port 9537 \
      config > %{service_name}.conf

%go_vendor_license_install -c %{S:2}

# binary install
# makefile output for pinns hard coded to ../bin
install -m 0755 -vd                        %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/crio %{buildroot}%{_bindir}/
install -m 0755 -vp ./bin/pinns            %{buildroot}%{_bindir}/

# libexec
install -m 0755 -vd                %{buildroot}%{_libexecdir}/%{service_name}

# shared state
install -m 0755 -vd                %{buildroot}%{_sharedstatedir}/containers

# refresh shell completion syntax and install
echo "+++ INSTALLING shell completion"
# bash
%{buildroot}%{_bindir}/%{service_name} complete bash >   ./completions/bash/crio
install -d -m 0755    %{buildroot}%{bash_completions_dir}
install -D -m 0644 -t %{buildroot}%{bash_completions_dir} ./completions/bash/crio

# fish
%{buildroot}%{_bindir}/%{service_name} complete fish >   ./completions/fish/crio.fish
install -d -m 0755    %{buildroot}%{fish_completions_dir}
install -D -m 0644 -t %{buildroot}%{fish_completions_dir} ./completions/fish/crio.fish

# zsh
%{buildroot}%{_bindir}/%{service_name} complete zsh >   ./completions/zsh/_crio
install -d -m 0755    %{buildroot}%{zsh_completions_dir}
install -D -m 0644 -t %{buildroot}%{zsh_completions_dir} ./completions/zsh/_crio

echo "+++ INSTALLING config files"
install -d -m 0755    %{buildroot}%{_sysconfdir}
install -D -m 0644 -t %{buildroot}%{_sysconfdir}  crictl.yaml

install -dp %{buildroot}%{_sysconfdir}/cni/net.d
install -p -m 0644 contrib/cni/10-crio-bridge.conflist %{buildroot}%{_sysconfdir}/cni/net.d/100-crio-bridge.conflist
install -p -m 0644 contrib/cni/99-loopback.conflist %{buildroot}%{_sysconfdir}/cni/net.d/200-loopback.conflist

echo "+++ INSTALLING service files"
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{service_name}
install -dp %{buildroot}%{_datadir}/containers/oci/hooks.d
install -dp %{buildroot}%{_datadir}/oci-umount/oci-umount.d
install -p -m 0644 crio.conf %{buildroot}%{_sysconfdir}/%{service_name}
install -p -m 0644 crio-umount.conf %{buildroot}%{_datadir}/oci-umount/oci-umount.d/%{service_name}-umount.conf

echo "+++ INSTALLING systemd files"
install -d -m 0755 %{buildroot}%{_unitdir}
install -p -m 0644 contrib/systemd/crio.service %{buildroot}%{_unitdir}/%{service_name}.service
install -p -m 0644 contrib/systemd/crio-wipe.service %{buildroot}%{_unitdir}/%{service_name}-wipe.service


echo "+++ INSTALLING manpages"
# make places these in ./docs
install -d -m 0755 %{buildroot}%{_mandir}/man5
install -p -m 0644 docs/*.5 %{buildroot}%{_mandir}/man5

install -d -m 0755 %{buildroot}%{_mandir}/man8
install -p -m 0644 docs/*.8 %{buildroot}%{_mandir}/man8


# **********************************
%check
%go_vendor_license_check -c %{S:2}

%if %{with check}

# use and extend build tags and substitute commas for whitespace
TEST_TAGS=$((echo "test rpm_crashtraceback %{buildtags}") | sed -e 's/\s\+/,/g')
# echo "++++ Test Tags: $TEST_TAGS"

# go test flags. GO_MOD_VENDOR is from Makefile testunit. Not defined anywhere
%global gotestflags     %{gocompilerflags} -tags $TEST_TAGS${GO_MOD_VENDOR:+,$GO_MOD_VENDOR}

# test/nri skipped in makefile testunit target
#
# all skipped tests below work via make in source directory
# but fail in gocheck and fail running make under mock
# internal/factory/container - tests pass via go test
#   and makefile so some sort of container and mock interaction
#   that triggers a permission block
# internal/oci - mkdir /var/run/crio permission error. Tests work manually.
# server - mkdir /var/run/crio permission error. Tests work manually.
%gocheck -t test/nri -t internal/factory/container -t internal/oci -t server

# same tests via make
# %%make_build testunit
%endif

# **********************************
%files -f %{go_vendor_license_filelist}
%license vendor/modules.txt
%doc docs ADOPTERS.md CONTRIBUTING.md GOVERNANCE.md
%doc MAINTAINERS.md README.md SECURITY.md awesome.md
%doc code-of-conduct.md cri.md

%{_bindir}/%{service_name}
%{_bindir}/pinns

%{_mandir}/man5/%{service_name}.conf*5*
%{_mandir}/man8/%{service_name}*.8*

%dir %{_sysconfdir}/%{service_name}
%config(noreplace) %{_sysconfdir}/%{service_name}/%{service_name}.conf
%config(noreplace) %{_sysconfdir}/cni/net.d/100-%{service_name}-bridge.conflist
%config(noreplace) %{_sysconfdir}/cni/net.d/200-loopback.conflist
%config(noreplace) %{_sysconfdir}/crictl.yaml
%dir %{_libexecdir}/%{service_name}
%{_unitdir}/%{service_name}.service
%{_unitdir}/%{service_name}-wipe.service
%dir %{_sharedstatedir}/containers
%dir %{_datadir}/containers
%dir %{_datadir}/containers/oci
%dir %{_datadir}/containers/oci/hooks.d
%dir %{_datadir}/oci-umount
%dir %{_datadir}/oci-umount/oci-umount.d
%{_datadir}/oci-umount/oci-umount.d/%{service_name}-umount.conf
%{bash_completions_dir}/%{service_name}*
%{fish_completions_dir}/%{service_name}*.fish
%{zsh_completions_dir}/_%{service_name}*


# **********************************
%changelog
%autochangelog
