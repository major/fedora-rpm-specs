%global srcname flatpak-module-tools
%global project_version 1.0.2

Name:		%{srcname}
Version:	1.0.2
Release:	3%{?dist}
Summary:	Tools for maintaining Flatpak applications and runtimes as Fedora modules

License:	MIT
URL:		https://pagure.io/flatpak-module-tools
Source0:	https://releases.pagure.org/flatpak-module-tools/flatpak-module-tools-%{project_version}.tar.gz

BuildArch:	noarch
# i386 is not supported by flatpak_module_tools.utils.Arch
ExcludeArch:    i386 i686

BuildRequires: python3-build
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm+toml
BuildRequires: python3-wheel

# For tests
BuildRequires: createrepo_c
BuildRequires: flatpak
BuildRequires: git-core
BuildRequires: libappstream-glib
BuildRequires: libmodulemd
BuildRequires: librsvg2
BuildRequires: ostree
BuildRequires: python3-click
BuildRequires: python3-gobject-base
BuildRequires: python3-pytest-cov
BuildRequires: python3-jinja2
BuildRequires: python3-koji
BuildRequires: python3-networkx
BuildRequires: python3-pytest
BuildRequires: python3-requests
BuildRequires: python3-responses
BuildRequires: python3-rpm
BuildRequires: python3-yaml
BuildRequires: python3-zstandard
BuildRequires: zstd

Requires: python3-%{srcname} = %{version}-%{release}
Requires: python3-jinja2
Requires: python3-koji
Requires: python3-networkx
Requires: python3-requests-toolbelt
# for pkg_resources
Requires: python3-setuptools
Requires: python3-solv

%description
flatpak-module-tools is a set of command line tools (all accessed via a single
'flatpak-module' executable) for operations related to maintaining Flatpak
applications and runtimes as Fedora modules.

%package -n python3-%{srcname}
Summary: Shared code for building Flatpak applications and runtimes from Fedora modules

# Note - pythonN-flatpak-modules-tools subpackage contains all the Python files from
# the upstream distribution, but some of them are only useful for the CLI, not
# for using this as a library for atomic-reactor. The dependencies here are those
# needed for library usage, the main package has the remainder.

Requires: createrepo_c
Requires: flatpak
# For appstream-compose
Requires: libappstream-glib
# for SVG gdk-pixbuf loader
Requires: librsvg2
Requires: ostree
Requires: python3-click
Requires: python3-requests
Requires: python3-rpm
Requires: python3-yaml
Requires: python3-zstandard
Requires: zstd

# Output changed from <nvr>.oci.tar.gz to <nvr>.oci.tar
Conflicts: koji-flatpak <= 0.2

%description -n python3-%{srcname}
Python3 library for Flatpak handling

%prep
%autosetup -p1 -n %{srcname}-%{project_version}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{project_version}
%pyproject_wheel


%check
# Tests using RPM don't work well inside %%check
%pytest -k "not test_create_rpm_manifest"


%install
%pyproject_install


%files
%license LICENSE
%doc README.md
%{_bindir}/flatpak-module
%{_bindir}/flatpak-module-depchase


%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Owen Taylor <otaylor@redhat.com> - 1.0.2-1
- Fix network access during tests

* Thu Jul 11 2024 Owen Taylor <otaylor@redhat.com> - 1.0-1
- Version 1.0
- Add 'flatpak-module init'
- Support zstd compressed repository metadata
- Disable min-free-space check for ostree repositories
- Handle RPMs with different versions for different subpackages
- Provide a better error message during dependency resolution when
  the runtime is out of date.

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 1.0~a9-5
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0~a9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0~a9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a9-2
- Add a dependency on zstd tool (used to compress intermediate tarball)

* Mon Sep 25 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a9-1
- Fix tests in environments without git config set up

* Mon Sep 25 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a8-1
- Add flatpak-module build-container
- Use f<N>-updates-testing-pending as the source tag
- Speed up build process for large Flatpaks by reducing zlib time
  (output name changes from .oci.tar.gz to .oci.tar)
- Properly handle 'platforms: only' and 'platforms: not' in container.yaml

* Thu Aug 24 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a7-1
- Fixes cleanup-commands not working at all
- Run script create from cleanup-commands under 'sh -ex'

* Thu Aug 24 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a6-1
- Version 1.0~a6
- Fixes bugs with local builds in fresh directories
- Other bug fixes for local builds

* Tue Aug 22 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a5-1
- Version 1.0~a5
- Fix operation when the main package is a subpackage
- Add --local-repo option to CLI
- Fix up Requires:

* Tue Aug 15 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a3-1
- New version
- Fixes problem with triggers from flatpak-runtime-config not running for apps
- Fixes local RPMs not working for 'flatpak-module build-container-local'
- Makes bwrap invocation check more exact

* Tue Aug 15 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a2-4
- Add a patch to debug why the test for working bwrap isn't working on the
  Koji builders.
- Add some missing requires for flatpak-module-depchase

* Thu Aug 10 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a2-3
- Build on x86_64 to avoid test failures

* Thu Aug 10 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a2-2
- Avoid building on i386 to avoid test failures

* Thu Aug 10 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a2-1
- Update to 1.0a2 - fixes Python-3.12 compatibility

* Thu Aug 10 2023 Owen Taylor <otaylor@redhat.com> - 1.0~a1-1
- Update to 1.0a1 - this is a major change that removes support for buiding
  Flatpaks with modules from the command line (the parts used by OSBS are
  still present in the Python API.)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.13-8
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13-5
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13-2
- Rebuilt for Python 3.10

* Tue Feb 23 2021 Owen Taylor <otaylor@redhat.com> - 0.13-1
- Version 0.13

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Owen Taylor <otaylor@redhat.com> - 0.12.1-1
- Version 0.12.1 - fixes bug with long filenames
- Remove outdated patch
- Run tests in %check

* Mon Oct 05 2020 Kalev Lember <klember@redhat.com> - 0.12-3
- Fix argument passing for app end-of-life/end-of-life-rebase

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fedora <otaylor@redhat.com> - 0.12-1
- Version 0.12 - fix installing Flatpaks created by flatpak-1.6

* Tue Jul 14 2020 Owen Taylor <otaylor@redhat.com> - 0.11.5-1
- Version 0.11.5 - compatibility fixes for recent dnf and mock

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.3-4
- Rebuilt for Python 3.9

* Mon May 11 2020 Kalev Lember <klember@redhat.com> - 0.11.3-3
- Add xa.metadata as ostree commit metadata for runtimes
- Add support for end-of-life and end-of-life-rebase

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Owen Taylor <otaylor@redhat.com> - 0.11.3-1
- Version 0.11.3 - 0.11.2 had a stray file

* Fri Dec  6 2019 Owen Taylor <otaylor@redhat.com> - 0.11.2-1
- Version 0.11.2 - fix finish-args for runtimes

* Wed Oct 23 2019 Owen Taylor <otaylor@redhat.com> - 0.11.1-1
- Version 0.11.1 - compatibility with future versions of Flatpak that
  may generate label-only images

* Thu Oct 17 2019 Fedora <otaylor@redhat.com> - 0.11-1
- Version 0.11 - add standard labels, and allow using labels
  instead of annotations for Flatpak metadata.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Owen Taylor <otaylor@redhat.com> - 0.10.4-2
- Fix requirements

* Wed Jul 24 2019 Owen Taylor <otaylor@redhat.com> - 0.10.4-1
- Version 0.10.4 - fix bugs with libmodulemd v2 api conversion

* Fri Jul 12 2019 Owen Taylor <otaylor@redhat.com> - 0.10.1-1
- Version 0.10.1 - fix compatibility with newer module-build-service
  and avoid flatpak-repair issues.

* Mon Apr  1 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.3-1
- Version 0.9.3 - fix module-build-service and Flatpak compat issues

* Tue Feb  5 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.2-1
- Version 0.9.2 - fix icon validation for Flatpak 1.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 fedora-toolbox <otaylor@redhat.com> - 0.9.1-1
- Version 0.9.1 - bug fixes including systemd-nspawn compatibility

* Tue Jan 22 2019 Owen Taylor <otaylor@redhat.com> - 0.9-1
- Version 0.9 - configurability, fixes for F29 dnf compatibility

* Fri Nov 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-2
- Drop python2 subpackage (#1634652)

* Thu Oct  4 2018 Owen Taylor <otaylor@redhat.com> - 0.8.4-1
- Version 0.8.4 - fix bugs in Flatpak installation

* Tue Oct  2 2018 Owen Taylor <otaylor@redhat.com> - 0.8.3-1
- Version 0.8.3 (bug fixes, add flatpak-module install --koji)

* Mon Sep 10 2018 Owen Taylor <otaylor@redhat.com> - 0.8.2-1
- Version 0.8.2 (Install flatpak-runtime-config with apps making
  included triggers work, support comments in finish-args,
  enable mock dnf cache for local builds.)
- Add dependencies on required tools

* Tue Aug 21 2018 Owen Taylor <otaylor@redhat.com> - 0.8.1-1
- Version 0.8.1 - bug fixes

* Fri Aug 10 2018 Owen Taylor <otaylor@redhat.com> - 0.8-1
- Version 0.8 - bug fixes and command line convenience

* Tue Jul 31 2018 Owen Taylor <otaylor@redhat.com> - 0.6-1
- Version 0.6 (improve container.yaml support)
- Build for Python2 as well
- Split out python<N>-flatpak-module-tools subpackages

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-2
- Rebuilt for Python 3.7

* Fri Jun  1 2018 Owen Taylor <otaylor@redhat.com> - 0.4-1
- Version 0.4 (fix container builds from Koji)

* Thu May 31 2018 Owen Taylor <otaylor@redhat.com> - 0.3-1
- Version 0.3 (minor fixes)

* Tue May 22 2018 Owen W. Taylor <otaylor@fishsoup.net> - 0.2-1
- Initial version
