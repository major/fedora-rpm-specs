# Generated by rust2rpm 27
# * many tests don't work when virtualized / containerized
%bcond check 0
%global debug_package %{nil}

%global crate nix

Name:           rust-nix0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust friendly bindings to *nix APIs

License:        MIT
URL:            https://crates.io/crates/nix
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          nix-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rust friendly bindings to *nix APIs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+acct-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+acct-devel %{_description}

This package contains library source intended for building other packages which
use the "acct" feature of the "%{crate}" crate.

%files       -n %{name}+acct-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+aio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+aio-devel %{_description}

This package contains library source intended for building other packages which
use the "aio" feature of the "%{crate}" crate.

%files       -n %{name}+aio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dir-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dir-devel %{_description}

This package contains library source intended for building other packages which
use the "dir" feature of the "%{crate}" crate.

%files       -n %{name}+dir-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+env-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+env-devel %{_description}

This package contains library source intended for building other packages which
use the "env" feature of the "%{crate}" crate.

%files       -n %{name}+env-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+event-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+event-devel %{_description}

This package contains library source intended for building other packages which
use the "event" feature of the "%{crate}" crate.

%files       -n %{name}+event-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fanotify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fanotify-devel %{_description}

This package contains library source intended for building other packages which
use the "fanotify" feature of the "%{crate}" crate.

%files       -n %{name}+fanotify-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+feature-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+feature-devel %{_description}

This package contains library source intended for building other packages which
use the "feature" feature of the "%{crate}" crate.

%files       -n %{name}+feature-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fs-devel %{_description}

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%files       -n %{name}+fs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hostname-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hostname-devel %{_description}

This package contains library source intended for building other packages which
use the "hostname" feature of the "%{crate}" crate.

%files       -n %{name}+hostname-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+inotify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+inotify-devel %{_description}

This package contains library source intended for building other packages which
use the "inotify" feature of the "%{crate}" crate.

%files       -n %{name}+inotify-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ioctl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ioctl-devel %{_description}

This package contains library source intended for building other packages which
use the "ioctl" feature of the "%{crate}" crate.

%files       -n %{name}+ioctl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kmod-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kmod-devel %{_description}

This package contains library source intended for building other packages which
use the "kmod" feature of the "%{crate}" crate.

%files       -n %{name}+kmod-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+memoffset-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memoffset-devel %{_description}

This package contains library source intended for building other packages which
use the "memoffset" feature of the "%{crate}" crate.

%files       -n %{name}+memoffset-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mman-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mman-devel %{_description}

This package contains library source intended for building other packages which
use the "mman" feature of the "%{crate}" crate.

%files       -n %{name}+mman-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mount-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mount-devel %{_description}

This package contains library source intended for building other packages which
use the "mount" feature of the "%{crate}" crate.

%files       -n %{name}+mount-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mqueue-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mqueue-devel %{_description}

This package contains library source intended for building other packages which
use the "mqueue" feature of the "%{crate}" crate.

%files       -n %{name}+mqueue-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+net-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+net-devel %{_description}

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%files       -n %{name}+net-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+personality-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+personality-devel %{_description}

This package contains library source intended for building other packages which
use the "personality" feature of the "%{crate}" crate.

%files       -n %{name}+personality-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pin-utils-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pin-utils-devel %{_description}

This package contains library source intended for building other packages which
use the "pin-utils" feature of the "%{crate}" crate.

%files       -n %{name}+pin-utils-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+poll-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+poll-devel %{_description}

This package contains library source intended for building other packages which
use the "poll" feature of the "%{crate}" crate.

%files       -n %{name}+poll-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+process-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+process-devel %{_description}

This package contains library source intended for building other packages which
use the "process" feature of the "%{crate}" crate.

%files       -n %{name}+process-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pthread-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pthread-devel %{_description}

This package contains library source intended for building other packages which
use the "pthread" feature of the "%{crate}" crate.

%files       -n %{name}+pthread-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ptrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ptrace-devel %{_description}

This package contains library source intended for building other packages which
use the "ptrace" feature of the "%{crate}" crate.

%files       -n %{name}+ptrace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+quota-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quota-devel %{_description}

This package contains library source intended for building other packages which
use the "quota" feature of the "%{crate}" crate.

%files       -n %{name}+quota-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reboot-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reboot-devel %{_description}

This package contains library source intended for building other packages which
use the "reboot" feature of the "%{crate}" crate.

%files       -n %{name}+reboot-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+resource-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+resource-devel %{_description}

This package contains library source intended for building other packages which
use the "resource" feature of the "%{crate}" crate.

%files       -n %{name}+resource-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sched-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sched-devel %{_description}

This package contains library source intended for building other packages which
use the "sched" feature of the "%{crate}" crate.

%files       -n %{name}+sched-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+signal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signal-devel %{_description}

This package contains library source intended for building other packages which
use the "signal" feature of the "%{crate}" crate.

%files       -n %{name}+signal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+socket-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+socket-devel %{_description}

This package contains library source intended for building other packages which
use the "socket" feature of the "%{crate}" crate.

%files       -n %{name}+socket-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+term-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+term-devel %{_description}

This package contains library source intended for building other packages which
use the "term" feature of the "%{crate}" crate.

%files       -n %{name}+term-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ucontext-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ucontext-devel %{_description}

This package contains library source intended for building other packages which
use the "ucontext" feature of the "%{crate}" crate.

%files       -n %{name}+ucontext-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+uio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uio-devel %{_description}

This package contains library source intended for building other packages which
use the "uio" feature of the "%{crate}" crate.

%files       -n %{name}+uio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+user-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+user-devel %{_description}

This package contains library source intended for building other packages which
use the "user" feature of the "%{crate}" crate.

%files       -n %{name}+user-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zerocopy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zerocopy-devel %{_description}

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

%files       -n %{name}+zerocopy-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
