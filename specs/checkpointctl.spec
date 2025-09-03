%global with_debug 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project checkpoint-restore
%global repo checkpointctl
# https://github.com/checkpoint-restore/checkpointctl
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}
%global git0 https://github.com/checkpoint-restore/checkpointctl

%global built_tag v1.4.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: %{repo}
Epoch: 1
Version: %{gen_version}
Release: %autorelease
Summary: A command-line tool for in-depth analysis of container checkpoints
License: Apache-2.0
URL: %{git0}
Source0: %{git0}/archive/%{built_tag}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{golang_arches_future}
BuildRequires: golang
BuildRequires: asciidoctor
BuildRequires: make
# vendored libraries
Provides: bundled(golang(github.com/checkpoint_restore/go_criu/v7)) = v7.0.0
Provides: bundled(golang(github.com/containers/storage)) = v1.51.0
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.1.0
Provides: bundled(golang(github.com/klauspost/compress)) = v1.17.2
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.6
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.9
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.7.1
Provides: bundled(golang(github.com/olekukonko/tablewriter)) = v0.0.5
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.10
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.1.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.3
Provides: bundled(golang(github.com/spf13/cobra)) = v1.8.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.11
Provides: bundled(golang(github.com/xlab/treeprint)) = v1.2.0

%description
The checkpointctl command can be used for in-depth analysis of
container checkpoints created with Podman and Kubernetes.

%prep
%autosetup -n %{name}-%{version}

%build
%set_build_flags
export CGO_CFLAGS=$CFLAGS

# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

# Strip the installed binary
%if 0%{?with_debug} == 0
/usr/bin/strip %{buildroot}%{_bindir}/%{name}
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
%autochangelog
