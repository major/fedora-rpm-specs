%if 0%{?fedora} || 0%{?rhel} == 6
%global with_debug 0
%global with_check 1
%else
%global with_debug 0
%global with_check 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         estesp
%global repo            manifest-tool
# https://github.com/estesp/manifest-tool
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit         a28af2b6bf3748859149bf161eb0630e677c3906
%global shortcommit    %(c=%{commit}; echo ${c:0:7})

Name:           manifest-tool
Version:        2.0.8
Release:        7%{?dist}
#Release:        5.git{shortcommit}{?dist}
Summary:        A command line tool used for creating manifest list objects
License:        Apache-2.0
URL:            https://%{provider_prefix}
#Source:         https://{provider_prefix}/archive/{commit}/{repo}-{shortcommit}.tar.gz
Source:         https://%{provider_prefix}/%{repo}-%{version}.tar.gz
Patch0:         go-mod.patch

ExclusiveArch:  x86_64 aarch64 ppc64le s390x
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git make
Provides:       %{repo} = %{version}-%{release}
Provides:       bundled(golang(github.com/containerd))
Provides:       bundled(golang(github.com/docker/cli))
Provides:       bundled(golang(github.com/docker/distribution))
Provides:       bundled(golang(github.com/docker))
Provides:       bundled(golang(github.com/fatih/color))
Provides:       bundled(golang(github.com/opencontainers/go-digest))
Provides:       bundled(golang(github.com/opencontainers/image-spec))
Provides:       bundled(golang(github.com/pkg/errors))
Provides:       bundled(golang(github.com/sirupsen/logrus))
Provides:       bundled(golang(github.com/urfave/cli))
Provides:       bundled(golang(gopkg.in/yaml.v3))
Provides:       bundled(golang(oras.land/oras-go/v2))

Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2/md2man))
Provides:       bundled(golang(github.com/docker/docker-credential-helpers))
Provides:       bundled(golang(github.com/golang/protobuf))
Provides:       bundled(golang(github.com/klauspost/compress))
Provides:       bundled(golang(github.com/kr/text))
Provides:       bundled(golang(github.com/mattn/go-colorable))
Provides:       bundled(golang(github.com/mattn/go-isatty))
Provides:       bundled(golang(github.com/moby/locker))
Provides:       bundled(golang(github.com/niemeyer/pretty))
Provides:       bundled(golang(github.com/russross/blackfriday/v2))
Provides:       bundled(golang(github.com/xrash/smetrics))
Provides:       bundled(golang(golang.org/x/net))
Provides:       bundled(golang(golang.org/x/sync))
Provides:       bundled(golang(golang.org/x/sys))
Provides:       bundled(golang(google.golang.org/genproto))
Provides:       bundled(golang(google.golang.org/grpc))
Provides:       bundled(golang(google.golang.org/protobuf))
Provides:       bundled(golang(gopkg.in/check.v1))

%description
This tool was mainly created for the purpose of viewing, creating, and
pushing the new manifests list object type in the Docker registry. Manifest
lists are defined in the v2.2 image specification and exist mainly for the
purpose of supporting multi-architecture and/or multi-platform images within
a Docker registry.

%prep
#autosetup -Sgit -n {name}-{commit}
%autosetup -n %{name}-%{version}
#patch0 -p1

%build
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s $(dirs +1 -l) src/%{import_path}
popd

export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make binary

%install
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make DESTDIR=%{buildroot} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 2.0.8-5
- Rebuild for golang 1.22.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.8-1
- Update to latest upstream release
- Fixes RhBug 2174535 CVE-2023-25173

* Mon Feb 13 2023 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.3-6
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.0.3-3
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.3-2
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Wed Mar 23 2022 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.3-1
- New upstream release (RhBug 2064713)

* Tue Feb 15 2022 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.0-1
- New upstream release (RhBug 2054676)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.3-3
- Adjust for go 1.16 temporarily

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 release

* Mon Mar 09 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.rc2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.0-0.rc2
- Update to 1.0.0-rc2 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Josh Boyer <jwboyer@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0 upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5.gita28af2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4.gita28af2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-3.gita28af2b
- Add bundled provides (rhbz 1467322)

* Wed Jul 05 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-2.gita28af2b
- Cleanup with_bundled and license macro definitions (rhbz 1467322)

* Sun Jul 02 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-1.gita28af2b
- Initial package for manifest-tool
