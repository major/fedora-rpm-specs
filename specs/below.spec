# some tests fail on Koji but pass locally
# build with --with all_tests locally to verify they still pass
%bcond all_tests 0

Name:           below
Version:        0.11.0
Release:        %autorelease
Summary:        Interactive tool to view and record historical system data

SourceLicense:  Apache-2.0
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# LGPL-2.1-only OR BSD-2-Clause
# MIT
# MIT OR Apache-2.0
# MPL-2.0 OR MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    Apache-2.0
    AND ((MIT OR Apache-2.0) AND Unicode-3.0)
    AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016)
    AND 0BSD
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND BSD-2-Clause
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND (LGPL-2.1-only OR BSD-2-Clause)
    AND MIT
    AND (MPL-2.0 OR MIT OR Apache-2.0)
    AND (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/facebookincubator/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-fix-metadata.diff
# fix incompatible type error in BPF code with Clang 22
Patch:          https://github.com/facebookincubator/below/pull/8280.patch#/below-fix-bpf-clang22.patch
# trivial change; WARN -> WARNING. will upstream
Patch:          below-fix-tests.diff

# below assumes 64-bit architecture
ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros

Recommends:     logrotate

%description
below is an interactive tool to view and record historical system data. It has
support for:

- information regarding hardware resource utilization
- viewing the cgroup hierarchy
- cgroup and process information
- pressure stall information (PSI)
- record mode to record system data
- replay mode to replay historical system data
- live mode to view live system data
- dump subcommand to report script-friendly information (e.g. JSON and CSV)

below does not have support for cgroup1.

The name "below" stems from the fact that the below developers rejected many of
atop's design and style decisions.


%prep
%autosetup -p1
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -t


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
install -Dpm 0755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 etc/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 etc/logrotate.conf %{buildroot}%{_sysconfdir}/logrotate.d/%{name}.conf
install -dm 1777 %{buildroot}%{_localstatedir}/log/%{name} 

%check
%if %{with all_tests}
%cargo_test
%else
# btrfs_api::sudotest: SysError(EPERM)
# test::test_dump_tc_content: flaky in Koji
%global skipped_tests %{shrink:
    --skip btrfs_api::sudotest::ino_lookup_test
    --skip btrfs_api::sudotest::find_root_backref_test
    --skip btrfs_api::sudotest::logical_ino_test
    --skip test::test_dump_tc_content
}
%cargo_test -- -- --exact %{skipped_tests}
%endif


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}.conf
%dir %{_localstatedir}/log/%{name}


%changelog
%autochangelog
