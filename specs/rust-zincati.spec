# Generated by rust2rpm 26
%bcond_without check

# Whether to use vendor tarball. This should stay off in the steady state
# when all versioned crate depedencies are packaged, but can be occasionally
# enabled in order to decouple lifecycles.
%global with_bundled 1

%global crate zincati

Name:           rust-zincati
Version:        0.0.30
Release:        4%{?dist}
Summary:        Update agent for Fedora CoreOS

License:        Apache-2.0
URL:            https://crates.io/crates/zincati
Source0:        %{crates_source}
Source1:        https://github.com/coreos/%{crate}/releases/download/v%{version}/%{crate}-%{version}-vendor.tar.gz
%if ! 0%{?with_bundled}
# Fedora-specific crates overrides, generated with:
# git diff --no-prefix zincati-*/Cargo.toml
#Patch0:         fedora-zincati-cargo-manifest-overrides.diff
%endif

Patch0:         0001-cincinnati-fix-updates-nodes-comparison-logic.patch

# Skip 32 bits architectures, see
# https://bugzilla.redhat.com/show_bug.cgi?id=2046993
ExcludeArch:    armv7hl i686

BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)
# for Building ostree-ext
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  glib2-devel
BuildRequires:  ostree-devel

%global _description %{expand:
Update agent for Fedora CoreOS.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR BSD-2-Clause
# MIT OR Apache-2.0 OR Zlib
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR BSD-2-Clause) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

Requires:       polkit

%description -n %{crate} %{_description}

%files       -n %{crate}
%license COPYRIGHT
%license LICENSE
%license LICENSE.dependencies
%if 0%{?with_bundled}
%license cargo-vendor.txt
%endif
%doc README.md
%{_libexecdir}/zincati
%{_bindir}/zincati-update-now
%dir %{_prefix}/lib/%{crate}
%dir %{_prefix}/lib/%{crate}/config.d
%{_prefix}/lib/%{crate}/config.d/*.toml
%attr(0775, zincati, zincati) %ghost /run/%{crate}
%attr(0775, zincati, zincati) %ghost /run/%{crate}/config.d
%attr(0770, zincati, zincati) %ghost /run/%{crate}/private
%attr(0775, zincati, zincati) %ghost /run/%{crate}/public
%attr(0755, zincati, zincati) %ghost /run/%{crate}/public/metrics.promsock
%ghost /run/%{crate}/private/metrics.promsock
%dir %{_sysconfdir}/%{crate}
%dir %{_sysconfdir}/%{crate}/config.d
%{_unitdir}/zincati.service
%{_sysusersdir}/50-zincati.conf
%{_tmpfilesdir}/zincati.conf
%{_datadir}/polkit-1/rules.d/zincati.rules
%{_datadir}/polkit-1/actions/org.coreos.zincati.*
%{_datadir}/dbus-1/system.d/*.conf

%post        -n %{crate}
%systemd_post zincati.service

%preun       -n %{crate}
%systemd_preun zincati.service

%postun      -n %{crate}
%systemd_postun_with_restart zincati.service

%prep
%if 0%{?with_bundled}
%autosetup -N -n %{crate}-%{version} -a1
%cargo_prep -v vendor
%else
%autosetup -N -n %{crate}-%{version}
%cargo_prep
%endif
%autopatch -p1

%if ! 0%{?with_bundled}
%generate_buildrequires
%cargo_generate_buildrequires
%endif

%build
%cargo_build
%{?cargo_license_summary}
%{?cargo_license} > LICENSE.dependencies
%if 0%{?with_bundled}
%{cargo_vendor_manifest}
%endif

%install
%cargo_install
# `zincati` should not be executed directly by users, so we move the binary
# out of `/usr/bin`. See: https://github.com/coreos/fedora-coreos-tracker/issues/244
mkdir -p %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/zincati %{buildroot}%{_libexecdir}/zincati
install -Dpm0755 -t %{buildroot}%{_bindir} dist/bin/zincati-update-now
install -Dpm0644 -t %{buildroot}%{_prefix}/lib/%{crate}/config.d \
  dist/config.d/*.toml
mkdir -p %{buildroot}%{_sysconfdir}/%{crate}/config.d
install -Dpm0644 -t %{buildroot}%{_unitdir} \
  dist/systemd/system/*.service
install -Dpm0644 -t %{buildroot}%{_sysusersdir} \
  dist/sysusers.d/*.conf
install -Dpm0644 -t %{buildroot}%{_tmpfilesdir} \
  dist/tmpfiles.d/*.conf
install -Dpm0644 -t %{buildroot}%{_datadir}/polkit-1/rules.d \
  dist/polkit-1/rules.d/*.rules
install -Dpm0644 -t %{buildroot}%{_datadir}/polkit-1/actions \
  dist/polkit-1/actions/org.coreos.zincati.*
install -Dpm0644 -t %{buildroot}%{_datadir}/dbus-1/system.d \
  dist/dbus-1/system.d/*.conf

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 05 2025 Jean-Baptiste Trystram <jbtrystram@redhat.com> - 0.0.30-3
- Backport patch to fix rollback not sticking from https://github.com/coreos/zincati/pull/1293
  See https://github.com/coreos/fedora-coreos-tracker/issues/1938

* Wed Apr 16 2025 Tiago Bueno <49003339+tlbueno@users.noreply.github.com> - 0.0.30-2
- Add install zincati-update-now file into spec

* Mon Mar 17 2025 Steven Presti <spresti@redhat.com> - 0.0.30-1
- update to 0.0.30

* Mon Mar 17 2025 Dusty Mabe <dusty@dustymabe.com> - 0.0.29-2
- Backport polkit rules patch for CVE-2025-27512

* Fri Jan 24 2025 Huijing Hei <hhei@redhat.com> - 0.0.29-1
- Update to 0.0.29

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 08 2023 Jonathan Lebon <jonathan@jlebon.com> - 0.0.27-1
- Update to 0.0.27

* Mon Nov 06 2023 Colin Walters <walters@verbum.org> - 0.0.26-3
- Cherry pick patch to unblock
  https://github.com/coreos/fedora-coreos-config/pull/2711

* Tue Oct 17 2023 Colin Walters <walters@verbum.org> - 0.0.26-2
- Update to 0.0.26

* Fri Oct 06 2023 Fabio Valentini <decathorpe@gmail.com> - 0.0.25-8
- Update spec for rust-packaging v25.

* Mon Sep 18 2023 Fabio Valentini <decathorpe@gmail.com> - 0.0.25-7
- Refresh for latest Rust package template; update license tag for SPDX.

* Tue Aug 15 2023 Aashish Radhakrishnan <aaradhak@redhat.com> - 0.0.25-6
- Backport patch for handling new output format for loginctl

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 10 2023 Fabio Valentini <decathorpe@gmail.com> - 0.0.25-4
- Stop using long-deprecated __global_rustflags_toml macro.

* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 0.0.25-3
- Rebuild for fixed frame pointer compiler flags in Rust RPM macros.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Luca BRUNO <lucab@lucabruno.net> - 0.0.25-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.25

* Tue Sep 20 2022 Luca BRUNO <lucab@lucabruno.net> - 0.0.24-6
- Add explicit service unit ordering, after multi-user.target
  Backports: https://github.com/coreos/zincati/pull/831

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.24-4
- Rebuild with package notes

* Thu Jan 27 2022 Luca BRUNO <lucab@lucabruno.net> - 0.0.24-3
- Stop building on 32 bits architectures
  Resolves: #2046993

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Luca BRUNO <lucab@lucabruno.net> - 0.0.24-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.24

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.0.23-2
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 06 2021 Luca BRUNO <lucab@lucabruno.net> - 0.0.23-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.23

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Luca BRUNO <lucab@lucabruno.net> - 0.0.22-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.22
- Temporarily use bundled crates from vendor tarball

* Thu Jul 01 2021 Luca BRUNO <lucab@lucabruno.net> - 0.0.21-2
- Mark runtime/ephemeral file entries as 'ghost'

* Fri May 21 2021 Luca BRUNO <lucab@lucabruno.net> - 0.0.21-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.21
- Turn off the usage of bundled crates, all in Fedora now

* Tue May 04 2021 Luca BRUNO <lucab@lucabruno.net> - 0.0.20-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.20
- Temporarily use bundled crates from vendor tarball

* Tue Mar 23 2021 Kelvin Fan <kfan@redhat.com> - 0.0.19-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.19

* Wed Mar 03 2021 Kelvin Fan <kfan@redhat.com> - 0.0.18-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.18

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.17-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 09 2021 Luca BRUNO <lucab@lucabruno.net> - 0.0.17-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.17

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 13:55:25 UTC 2020 Luca BRUNO <lucab@lucabruno.net> - 0.0.14-1
- New upstream version
  https://github.com/coreos/zincati/releases/tag/v0.0.14

* Tue Sep 29 2020 Dusty Mabe <dusty@dustymabe.com> - 0.0.13-1
- Update to 0.0.13

* Wed Sep 23 2020 Kelvin Fan <kfan@redhat.com> - 0.0.12-6
- Remove unnecessary usage of systemd RPM macro in 'pre'

* Sun Aug 16 15:01:58 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.12-5
- Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Robert Fairley <rfairley@redhat.com> - 0.0.12-2
- Correct date in previous changelog

* Mon Jun 29 2020 Robert Fairley <rfairley@redhat.com> - 0.0.12-1
- Update to 0.0.12

* Fri May 22 12:14:40 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.11-1
- Update to 0.0.11

* Mon May 18 12:56:53 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.10-3
- Update mockito to 0.25
- Update fail to 0.4
- Update libsystemd to 0.2

* Wed Apr 15 18:22:39 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.10-2
- Update envsubst

* Wed Apr 15 2020 Robert Fairley <rfairley@redhat.com> - 0.10.0-1
- Update to 0.0.10

* Wed Mar 25 2020 Robert Fairley <rfairley@redhat.com> - 0.0.9-2
- Fix metrics socket symlink: make absolute

* Tue Mar 24 2020 Robert Fairley <rfairley@redhat.com> - 0.0.9-1
- Update to 0.0.9

* Sun Feb 23 10:42:48 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.8-1
- Update to 0.0.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Robert Fairley <rfairley@redhat.com> - 0.0.6-1
- Update to 0.0.6

* Wed Sep 11 2019 Robert Fairley <rfairley@redhat.com> - 0.0.5-1
- Update to 0.0.5
- Install binary under /usr/libexec

* Fri Aug 02 2019 Robert Fairley <rfairley@redhat.com> - 0.0.4-1
- Update to 0.0.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Robert Fairley <rfairley@redhat.com> - 0.0.3-1
- Update to 0.0.3
- Temporarily relax futures to 0.1.27 and env_logger to 0.6.1

* Thu Jul 04 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-7
- Require the polkit package, rather than the rules.d directory

* Thu Jul 04 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-6
- Add polkit rule to authorize zincati to perform upgrades https://github.com/coreos/zincati/pull/59

* Tue Jul 02 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-5
- Add missing owned directories, tidy owned files list

* Tue Jul 02 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-4
- Add runtime directories ownership by zincati sysuser

* Wed Jun 26 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-3
- Patch to use liboverdrop-0.0.2

* Wed Jun 26 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-2
- Fix specfile log, and macro in comment

* Wed Jun 26 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-1
- Update to 0.0.2

* Tue Jun 18 13:38:53 UTC 2019 Robert Fairley <rfairley@redhat.com> - 0.0.1-1
- Initial package
