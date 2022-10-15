# Tests works with enabled network. Also possible to run tests in COPR:
# https://download.copr.fedorainfracloud.org/results/atim/buildstream/fedora-35-x86_64/02660103-buildstream/builder-live.log.gz
%bcond_without test

Name:          buildstream
Summary:       Build/integrate software stacks
License:       LGPLv2+
URL:           https://buildstream.build/

Version:       1.6.8
Release:       %autorelease
Source0:       https://github.com/apache/buildstream/archive/%{version}/buildstream-%{version}.tar.gz

BuildRequires: bubblewrap >= 0.1.2
BuildRequires: make
BuildRequires: python3-devel >= 3.5
BuildRequires: python3-pytest-runner
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-sphinx-click

# These from plugin-requirements.in + requirements.in
BuildRequires: fuse-libs
BuildRequires: ostree-libs
BuildRequires: python3-arpy
BuildRequires: python3-click
BuildRequires: python3-gobject
BuildRequires: python3-grpcio >= 1.30
BuildRequires: python3-jinja2 >= 2.10
BuildRequires: python3-pluginbase
BuildRequires: python3-protobuf >= 3.19
BuildRequires: python3-psutil
BuildRequires: python3-ruamel-yaml >= 0.16
BuildRequires: python3-setuptools
BuildRequires: python3-ujson

%if %{with test}
BuildRequires: zip
BuildRequires: tar
BuildRequires: lzip
BuildRequires: git-core
BuildRequires: bzr
BuildRequires: ostree
BuildRequires: python3-pip
# These from dev-requirements.in
BuildRequires: python3-pytest >= 3.7
BuildRequires: python3-pytest-datafiles
BuildRequires: python3-pytest-env
BuildRequires: python3-pytest-timeout
BuildRequires: python3-pytest-xdist
# Not available: pyftpdlib (we skip the associated tests)

# We do not need linters (nor omitted coverage from cov-requirements.in); see:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# BuildRequires: python3-pep8
# BuildRequires: python3-pylint >= 2.10
%endif

Requires:      bubblewrap >= 0.1.2
Requires:      fuse
Requires:      fuse-libs
Requires:      git
Requires:      lzip
Requires:      ostree-libs
Requires:      patch
Requires:      python3-arpy
Requires:      python3-click
Requires:      python3-gobject
Requires:      python3-grpcio >= 1.30
Requires:      python3-jinja2 >= 2.10
Requires:      python3-pluginbase
Requires:      python3-protobuf >= 3.6
Requires:      python3-psutil
Requires:      python3-ruamel-yaml >= 0.16
Requires:      python3-setuptools
Requires:      python3-ujson
Requires:      tar

BuildArch:     noarch

%description
BuildStream is a Free Software tool for building/integrating software stacks.
It takes inspiration, lessons and use-cases from various projects including
OBS, Reproducible Builds, Yocto, Baserock, Buildroot, Aboriginal, GNOME
Continuous, JHBuild, Flatpak Builder and Android repo.

BuildStream supports multiple build-systems (e.g. autotools, cmake, cpan,
distutils, make, meson, qmake), and can create outputs in a range of formats
(e.g. debian packages, flatpak runtimes, sysroots, system images) for multiple
platforms and chipsets.


%package       docs
Summary:       BuildStream documentation

%description   docs
BuildStream is a Free Software tool for building/integrating software stacks.
It takes inspiration, lessons and use-cases from various projects including
OBS, Reproducible Builds, Yocto, Baserock, Buildroot, Aboriginal, GNOME
Continuous, JHBuild, Flatpak Builder and Android repo.

BuildStream supports multiple build-systems (e.g. autotools, cmake, cpan,
distutils, make, meson, qmake), and can create outputs in a range of formats
(e.g. debian packages, flatpak runtimes, sysroots, system images) for multiple
platforms and chipsets.

This package provides the documentation for BuildStream.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%py3_build

pushd doc
make devhelp
popd


%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/gtk-doc/html/
cp -pr doc/build/devhelp %{buildroot}%{_datadir}/gtk-doc/html/BuildStream


%if %{with test}
%check
# The following fail in koji but not in a local mock build; this seems to have
# something to do with sandboxing.
k="${k-}${k+ and }not test_push_pull"
k="${k-}${k+ and }not test_push_pull_all"
k="${k-}${k+ and }not test_pull_secondary_cache"
k="${k-}${k+ and }not test_push_pull_specific_remote"
k="${k-}${k+ and }not test_push_pull_non_strict"
k="${k-}${k+ and }not test_push_pull_track_non_strict"
k="${k-}${k+ and }not test_push_pull_cross_junction"
k="${k-}${k+ and }not test_pull_missing_blob"
k="${k-}${k+ and }not test_pull_access_rights"
k="${k-}${k+ and }not test_push"
k="${k-}${k+ and }not test_push_all"
k="${k-}${k+ and }not test_push_after_pull"
k="${k-}${k+ and }not test_artifact_expires"
k="${k-}${k+ and }not test_artifact_too_large"
k="${k-}${k+ and }not test_recently_pulled_artifact_does_not_expire"
k="${k-}${k+ and }not test_push_cross_junction"
k="${k-}${k+ and }not test_push_already_cached"
# This test expects 'arch' to be 'x86_64' or 'x86_32', so it fails when the
# builder is anything but x86_64. Even 32-bit x86 fails, as 'arch' is 'i686'.
# Since the package is noarch, we just skip it unconditionally.
k="${k-}${k+ and }not test_project_error"
# Ignored tests would require pyftpdlib, which is not packaged
%pytest -vv -k "${k-}" \
    --ignore=tests/testutils/file_server.py \
    --ignore=tests/testutils/ftp_server.py \
    --ignore=tests/sources/remote.py \
    --ignore=tests/sources/tar.py \
    --ignore=tests/sources/zip.py \
    %dnl # Some tests fail probably due new Python 3.11
    %if 0%{?fedora} >= 36
    --ignore=tests/frontend/compose_splits.py \
    --ignore=tests/frontend/overlaps.py \
    --ignore=tests/plugins/filter.py \
    --ignore=tests/sources/deb.py \
    --ignore=tests/sources/pip.py \
    %else
    %endif
%endif


%files
%doc NEWS README.rst
%license COPYING
%{_bindir}/bst*
%{python3_sitelib}/BuildStream-%{version}*.egg-info
%{python3_sitelib}/%{name}/
%{_datadir}/bash-completion/completions/bst
%{_mandir}/man1/*.1*

%files docs
%{_datadir}/gtk-doc


%changelog
%autochangelog
