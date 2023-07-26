# Disable tests by default since VMs can't run in containerized Fedora builds.
%bcond_with check

# The RPM macro cargo_target can be defined to specify the Rust target to use
# during the build.  When undefined, the distro's default target is used.

# Assume that musl targets produce static binaries by default, which determines
# if the jailer program is usable.  It should still build successfully with any
# linkage setting, so this conditional allows forcing it to build or not.
%if %{lua:print(rpm.expand("%{cargo_target}"):match("musl") and "1" or "0")}
%bcond_without jailer
%else
%bcond_with jailer
%endif

Name:           firecracker
Version:        1.4.0
Release:        2%{?dist}

Summary:        Secure and fast microVMs for serverless computing
License:        Apache-2.0 AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND Unicode-DFS-2016
URL:            https://firecracker-microvm.github.io/

Source0:        https://github.com/firecracker-microvm/firecracker/archive/v%{version}/%{name}-%{version}.tar.gz

# Bundle forked versions of existing crates to avoid conflicts with upstreams.
Source1:        https://github.com/firecracker-microvm/kvm-bindings/archive/e8359204b41d5c2e7c5af9ae5c26283b62337740/kvm-bindings-e835920.tar.gz
Source2:        https://github.com/firecracker-microvm/micro-http/archive/4b18a043e997da5b5f679e3defc279fec908753e/micro_http-4b18a04.tar.gz

# kvm-bindings: Apache-2.0
Provides:       bundled(crate(kvm-bindings)) = 0.6.0^gite835920
# micro_http: Apache-2.0
Provides:       bundled(crate(micro_http)) = 0.1.0^git4b18a04

# Edit crate dependencies to track what is packaged in Fedora.
# These patches do not make sense to send upstream given their purpose.
Patch:          %{name}-1.4.0-remove-aws-lc-rs.patch
Patch:          %{name}-1.4.0-remove-cargo_toml.patch
Patch:          %{name}-1.4.0-remove-criterion.patch
Patch:          %{name}-1.4.0-remove-device_tree.patch
Patch:          %{name}-1.4.0-upgrade-kvm-ioctls.patch
Patch:          %{name}-1.4.0-upgrade-linux-loader.patch

BuildRequires:  cargo-rpm-macros >= 24
%if %defined cargo_target
BuildRequires:  rust-std-static-%{cargo_target}
%endif

# Currently only these architectures are supported.  See the README.
ExclusiveArch:  aarch64 x86_64

%description
Firecracker is an open source virtualization technology that is purpose-built
for creating and managing secure, multi-tenant container and function-based
services that provide serverless operational models.  Firecracker runs
workloads in lightweight virtual machines, called microVMs, which combine the
security and isolation properties provided by hardware virtualization
technology with the speed and flexibility of containers.
%{!?with_jailer:
This package does not include all of the security features of an official
release.  It is not production ready without additional sandboxing.}


%prep
%autosetup -p1

# Extract the bundled forked crates and point their users at the paths.
mkdir forks
tar --transform='s,^[^/]*,kvm-bindings,' -C forks -xzf %{SOURCE1}
tar --transform='s,^[^/]*,micro_http,' -C forks -xzf %{SOURCE2}
sed -i -e 's@^\(kvm-bindings\|micro_http\) = {.*\(, features =.*\| }$\)@\1 = { path = "../../forks/\1"\2@' Cargo.toml src/*/Cargo.toml
sed -i -e 's,../../forks,forks,' Cargo.toml

%cargo_prep

%generate_buildrequires
# Unconditionally include dev-dependencies to avoid build failures.
cargo2rpm --path Cargo.toml buildrequires --with-check

%build
%cargo_build -- --package={cpu-template-helper,firecracker,%{?with_jailer:jailer,}rebase-snap,seccompiler} %{?cargo_target:--target=%{cargo_target}}
%{cargo_license} > LICENSE.dependencies

%install
install -pm 0755 -Dt %{buildroot}%{_bindir} target/%{?cargo_target}/release/{cpu-template-helper,firecracker,%{?with_jailer:jailer,}rebase-snap,seccompiler-bin}

# Ship the built-in seccomp JSON as an example that can be edited and compiled.
ln -fn resources/seccomp/%{cargo_target}.json seccomp-filter.json ||
ln -fn resources/seccomp/unimplemented.json seccomp-filter.json

# Prune unused images from the documentation directory prior to installation.
for image in docs/images/*
do grep --exclude-dir=images -FIqre "${image##*/}" docs *.md || rm -f "$image"
done

%if %{with check}
%check
%cargo_test -- %{!?with_jailer:--exclude=jailer} %{?cargo_target:--target=%{cargo_target}} --workspace
%endif


%files
%{_bindir}/cpu-template-helper
%{_bindir}/firecracker
%{?with_jailer:%{_bindir}/jailer}
%{_bindir}/rebase-snap
%{_bindir}/seccompiler-bin
%doc seccomp-filter.json
%doc src/api_server/swagger/firecracker.yaml
%doc docs CHANGELOG.md CHARTER.md CODE_OF_CONDUCT.md CONTRIBUTING.md CREDITS.md FAQ.md MAINTAINERS.md README.md SECURITY.md SPECIFICATION.md
%license LICENSE LICENSE.dependencies NOTICE THIRD-PARTY


%changelog
* Mon Jul 24 2023 David Michael <fedora.dm0@gmail.com> - 1.4.0-2
- Backport updates for the kvm-ioctls, linux-loader, and vm-memory crates.

* Wed Jul 19 2023 David Michael <fedora.dm0@gmail.com> - 1.4.0-1
- Update to the 1.4.0 release.

* Wed May 24 2023 David Michael <fedora.dm0@gmail.com> - 1.3.3-1
- Update to the 1.3.3 release.

* Thu Apr 27 2023 David Michael <fedora.dm0@gmail.com> - 1.3.2-1
- Update to the 1.3.2 release.

* Mon Mar 06 2023 David Michael <fedora.dm0@gmail.com> - 1.3.1-1
- Initial package.
