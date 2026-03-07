%bcond tests 1

# The GitLab archive contains the changelog file, test data, and other things
# that the PyPI sdist lacks.
%global forgeurl https://gitlab.com/obob/pymatreader
%global tag v%{version}
%forgemeta

Name:           python-pymatreader
Version:        1.2.2
Release:        %autorelease
Summary:        Convenient reader for Matlab mat files

License:        BSD-2-Clause
URL:            %{forgeurl}
Source:         %{forgesource}

# We want to test on all architectures, since there is a history of
# architecture-dependent test failures, but the package itself contains no
# compiled code, and the binary RPMs are noarch.
%global debug_package   %{nil}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# https://bugzilla.redhat.com/show_bug.cgi?id=2116690
ExcludeArch:    s390x

BuildRequires:  python3-devel
BuildRequires:  tomcli

%if %{with tests}
# See the [tool.pixi.dependencies] section in pyproject.toml, but note that it
# also contains unwanted documentation, coverage, and linting dependencies.
BuildRequires:  %{py3_dist pytest}
%endif

%global desc %{expand:
A Python module to read Matlab files. This module works with both the old
(< 7.3) and the new (>= 7.3) HDF5 based format. The output should be the same
for both kinds of files.

Documentation can be found here: http://pymatreader.readthedocs.io/en/latest/}

%description %{desc}


%package -n python3-pymatreader
Summary:        %{summary}
BuildArch:      noarch

%description -n python3-pymatreader %{desc}


%prep
%forgesetup

# We don’t want to package python-hatch-regex-commit for versioning. It is
# tedious to manipulate downstream and it does not appear widely used. It is
# easy enough to patch pyproject.toml to use the popular hatch-vcs plugin as a
# version source instead.
tomcli set pyproject.toml lists replace build-system.requires \
    hatch-regex-commit hatch-vcs
tomcli set pyproject.toml str tool.hatch.version.source vcs
tomcli set pyproject.toml del tool.hatch.version.tag_sign


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pymatreader


%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif


%files -n python3-pymatreader -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
