%bcond_without check
%bcond_without cli
%bcond_without gui

Summary:       File Access Policy Analyzer
Name:          fapolicy-analyzer
Version:       1.5.0
Release:       4%{?dist}

SourceLicense: GPL-3.0-or-later
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# ISC
# ISC AND OpenSSL AND MIT
# MIT
# MIT OR Apache-2.0
# MIT OR X11 OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
License:       GPL-3.0-or-later AND Apache-2.0 AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OpenSSL AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR X11 OR Apache-2.0) AND (Unlicense OR MIT)

URL:           https://github.com/ctc-oss/fapolicy-analyzer
Source0:       %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# this tarball contains documentation used to generate help docs
Source1:       %{url}/releases/download/v%{version}/vendor-docs-%{version}.tar.gz

Patch:         0001-pyo3-0.23-support.patch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(wheel)
BuildRequires: python3dist(babel)
BuildRequires: dbus-devel
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: desktop-file-utils

BuildRequires: clang
BuildRequires: audit-libs-devel

BuildRequires: cargo-rpm-macros
BuildRequires: python3dist(setuptools-rust)

Requires:      %{name}-cli
Requires:      %{name}-gui

%description
Tools to assist with the configuration and management of fapolicyd.


%package cli
Summary:       File Access Policy Analyzer CLI

%description cli
CLI Tools to assist with the configuration and management of fapolicyd.

%package gui
Summary:       File Access Policy Analyzer GUI

Requires:      python3
Requires:      python3-gobject
Requires:      python3-configargparse
Requires:      python3-more-itertools
Requires:      python3-rx
Requires:      python3-importlib-metadata
Requires:      python3-toml
Requires:      python3-matplotlib-gtk3

Requires:      gtk3
Requires:      gtksourceview3
Requires:      gnome-icon-theme

# runtime required for rendering user guide
Requires:      mesa-dri-drivers
%if 0%{?fedora} < 40
Requires:      webkit2gtk3
%else
Requires:      webkit2gtk4.1
%endif

%global module          fapolicy_analyzer
# pep440 versions handle dev and rc differently, so we call them out explicitly here
%global module_version  %{lua: v = string.gsub(rpm.expand("%{?version}"), "~dev", ".dev"); \
                               v = string.gsub(v, "~rc",  "rc"); print(v) }

%description gui
GUI Tools to assist with the configuration and management of fapolicyd.

%prep
%autosetup -n %{name} -p1
%cargo_prep

%if %{without cli}
# disable tools crate
sed -i '/tools/d' Cargo.toml
%endif

%if %{without gui}
# disable pyo3 crate
sed -i '/pyo3/d' Cargo.toml
%endif

# extract our doc sourcs
tar xvzf %{SOURCE1}

# our setup.py looks up the version from git describe
# this overrides that check to use the RPM version
echo %{module_version} > VERSION

# capture build info
scripts/build-info.py --os --time

# enable the audit feature for 39 and up
%if 0%{?fedora} >= 39
echo "audit" > FEATURES
%endif

%generate_buildrequires
%cargo_generate_buildrequires -a

%build

%if %{with cli}
cargo build --bin tdb --release
cargo build --bin faprofiler --release
cargo build --bin rulec --release --features pretty
%endif

%if %{with gui}
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%{build_rustflags}"

%{python3} setup.py compile_catalog -f
%{python3} help build
%{python3} setup.py bdist_wheel

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%endif

%install

%if %{with cli}
install -D target/release/tdb %{buildroot}/%{_sbindir}/%{name}-cli-trust
install -D target/release/faprofiler %{buildroot}/%{_sbindir}/%{name}-cli-profiler
install -D target/release/rulec %{buildroot}/%{_sbindir}/%{name}-cli-rules
%endif

%if %{with gui}
%{py3_install_wheel %{module}-%{module_version}*%{_target_cpu}.whl}
%{python3} help install --dest %{buildroot}/%{_datadir}/help
install -D bin/%{name} %{buildroot}/%{_sbindir}/%{name}
install -D data/%{name}.8 -t %{buildroot}/%{_mandir}/man8/
install -D data/%{name}-cli-*.8 -t %{buildroot}/%{_mandir}/man8/
install -D data/config.toml -t %{buildroot}%{_sysconfdir}/%{name}/
desktop-file-install data/%{name}.desktop
find locale -name %{name}.mo -exec cp --parents -rv {} %{buildroot}/%{_datadir} \;
%find_lang %{name} --with-gnome
%endif

%check
%if %{with gui}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%endif

%files cli
%attr(755,root,root) %{_sbindir}/%{name}-cli-trust
%attr(755,root,root) %{_sbindir}/%{name}-cli-profiler
%attr(755,root,root) %{_sbindir}/%{name}-cli-rules

%files gui
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{module_version}*
%attr(755,root,root) %{_sbindir}/%{name}
%attr(644,root,root) %{_mandir}/man8/%{name}.8*
%attr(644,root,root) %{_mandir}/man8/%{name}-cli-*.8*
%attr(755,root,root) %{_datadir}/applications/%{name}.desktop
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/%{name}/config.toml
%ghost %attr(640,root,root) %verify(not md5 size mtime) %{_localstatedir}/log/%{name}/%{name}.log

%files -f %{name}.lang
%doc scripts/srpm/README
%license LICENSE
%license LICENSE.dependencies

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.14

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 John Wass <jwass3@gmail.com> 1.5.0-1
- New release

* Tue Jul 30 2024 John Wass <jwass3@gmail.com> 1.4.0-2
- Fix requires version for webkit

* Sun Jul 28 2024 John Wass <jwass3@gmail.com> 1.4.0-1
- New release

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 John Wass <jwass3@gmail.com> 1.3.0-1
- New release

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 John Wass <jwass3@gmail.com> 1.2.2-1
- Update to 1.2.2

* Fri Nov 17 2023 John Wass <jwass3@gmail.com> 1.2.1-1
- Update to 1.2.1

* Mon Nov 06 2023 John Wass <jwass3@gmail.com> 1.2.0-1
- Release 1.2.0

* Thu Oct 26 2023 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-3
- Update packaging for latest Rust and Legal Guidelines.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 John Wass <jwass3@gmail.com> 1.1.0-1
- Release v1.1.0

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.12

* Mon May 29 2023 John Wass <jwass3@gmail.com> 1.0.3-1
- Release v1.0.3

* Fri Apr 28 2023 John Wass <jwass3@gmail.com> 1.0.2-1
- Release v1.0.2

* Mon Apr 10 2023 John Wass <jwass3@gmail.com> 1.0.1-1
- Release v1.0.1

* Wed Mar 15 2023 John Wass <jwass3@gmail.com> 1.0.0-1
- Release v1.0

* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-2
- Ensure standard Rust compiler flags are set.

* Wed Jan 11 2023 John Wass <jwass3@gmail.com> 0.6.8-1
- New release
