# The RPM macro cargo_target can be defined to specify the Rust target to use
# during the build.  When undefined, the distro's default target is used.

# Disable tests by default since VMs can't run in containerized Fedora builds.
%bcond check    0

# The jailer's documentation says only musl targets are supported.
%bcond jailer   %{lua:print(rpm.expand("%{?cargo_target}"):find("musl") or 0)}

Name:           firecracker
Version:        1.10.1
Release:        2%{?dist}

Summary:        Secure and fast microVMs for serverless computing
SourceLicense:  Apache-2.0
License:        Apache-2.0 AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Unlicense) AND Unicode-DFS-2016
URL:            https://firecracker-microvm.github.io/

Source0:        https://github.com/firecracker-microvm/firecracker/archive/v%{version}/%{name}-%{version}.tar.gz

# Bundle forked versions of existing crates to avoid conflicts with upstreams.
Source1:        https://github.com/firecracker-microvm/micro-http/archive/8182cd5523b63ceb52ad9d0e7eb6fb95683e6d1b/micro_http-8182cd5.tar.gz
Provides:       bundled(crate(micro_http)) = 0.1.0^git8182cd5

# Edit crate dependencies to track what is packaged in Fedora.
Patch:          %{name}-1.10.0-remove-aws-lc-rs.patch
Patch:          %{name}-1.10.0-remove-criterion.patch
Patch:          %{name}-1.10.0-remove-device_tree.patch

BuildRequires:  cargo-rpm-macros >= 24
%if %{defined cargo_target}
BuildRequires:  rust-std-static-%{cargo_target}
%endif

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
mkdir forks
tar --transform='s,^[^/]*,micro_http,' -C forks -xzf %{SOURCE1}
sed -i -e 's,^\(micro_http\) = .*,\1 = { path = "../../forks/\1" },' src/*/Cargo.toml
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build -- --package={cpu-template-helper,firecracker,%{?with_jailer:jailer,}rebase-snap,seccompiler,snapshot-editor} %{?cargo_target:--target=%{cargo_target}}
%{cargo_license} > LICENSE.dependencies

%install
install -pm 0755 -Dt %{buildroot}%{_bindir} target/%{?cargo_target}/rpm/{cpu-template-helper,firecracker,%{?with_jailer:jailer,}rebase-snap,seccompiler-bin,snapshot-editor}

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
%{_bindir}/snapshot-editor
%doc seccomp-filter.json
%doc src/firecracker/swagger/firecracker.yaml
%doc docs CHANGELOG.md CHARTER.md CODE_OF_CONDUCT.md CONTRIBUTING.md CREDITS.md FAQ.md MAINTAINERS.md README.md SECURITY.md SPECIFICATION.md
%license LICENSE LICENSE.dependencies NOTICE THIRD-PARTY


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 David Michael <fedora.dm0@gmail.com> - 1.10.1-1
- Update to the 1.10.1 release.

* Thu Nov 07 2024 David Michael <fedora.dm0@gmail.com> - 1.10.0-1
- Update to the 1.10.0 release.

* Thu Oct 03 2024 David Michael <fedora.dm0@gmail.com> - 1.9.1-1
- Update to the 1.9.1 release.

* Mon Sep 02 2024 David Michael <fedora.dm0@gmail.com> - 1.9.0-1
- Update to the 1.9.0 release.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 David Michael <fedora.dm0@gmail.com> - 1.8.0-1
- Update to the 1.8.0 release.

* Thu Apr 25 2024 David Michael <fedora.dm0@gmail.com> - 1.7.0-2
- Sync vm-superio with the upstream version fixing the vmm-sys-util CVE.

* Mon Mar 18 2024 David Michael <fedora.dm0@gmail.com> - 1.7.0-1
- Update to the 1.7.0 release.

* Sun Jan 28 2024 David Michael <fedora.dm0@gmail.com> - 1.6.0-6
- Sync linux-loader with the upstream version fixing the vmm-sys-util CVE.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 David Michael <fedora.dm0@gmail.com> - 1.6.0-4
- Backport the userfaultfd update for its unrecognized ioctl fixes.

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 David Michael <fedora.dm0@gmail.com> - 1.6.0-2
- Backport changes to update vmm-sys-util for CVE-2023-50711.

* Wed Dec 20 2023 David Michael <fedora.dm0@gmail.com> - 1.6.0-1
- Update to the 1.6.0 release.

* Tue Dec 05 2023 David Michael <fedora.dm0@gmail.com> - 1.5.1-1
- Update to the 1.5.1 release.

* Thu Oct 12 2023 David Michael <fedora.dm0@gmail.com> - 1.5.0-1
- Update to the 1.5.0 release.

* Sun Oct 01 2023 Fabio Valentini <decathorpe@gmail.com> - 1.4.1-3
- Rebuild for aes-gcm v0.10.3 / CVE-2023-42811.

* Tue Sep 19 2023 Fabio Valentini <decathorpe@gmail.com> - 1.4.1-2
- Rebuild for vm-memory v0.12.2 / CVE-2023-41051.

* Wed Aug 09 2023 David Michael <fedora.dm0@gmail.com> - 1.4.1-1
- Update to the 1.4.1 release.

* Mon Jul 24 2023 David Michael <fedora.dm0@gmail.com> - 1.4.0-2
- Backport updates for the kvm-ioctls, linux-loader, and vm-memory crates.
- Port arm64 to the new kvm-ioctls CPU register API.

* Wed Jul 19 2023 David Michael <fedora.dm0@gmail.com> - 1.4.0-1
- Update to the 1.4.0 release.

* Wed May 24 2023 David Michael <fedora.dm0@gmail.com> - 1.3.3-1
- Update to the 1.3.3 release.

* Thu Apr 27 2023 David Michael <fedora.dm0@gmail.com> - 1.3.2-1
- Update to the 1.3.2 release.

* Mon Mar 06 2023 David Michael <fedora.dm0@gmail.com> - 1.3.1-1
- Update to the 1.3.1 release.

* Thu Mar 02 2023 David Michael <fedora.dm0@gmail.com> - 1.3.0-1
- Initial package.
