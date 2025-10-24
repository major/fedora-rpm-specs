Name:       python-setuptools-git-versioning
Version:    2.1.0
Release:    %autorelease
Summary:    Use git repo data for building a version number according to PEP-440

License:    MIT
URL:        https://setuptools-git-versioning.readthedocs.io/
%global forgeurl https://github.com/dolfinus/setuptools-git-versioning
Source:    %{forgeurl}/archive/v%{version}/setuptools-git-versioning-%{version}.tar.gz

# Fix a small typo in the package description
# https://github.com/dolfinus/setuptools-git-versioning/pull/116
Patch:      %{forgeurl}/pull/116.patch
# Remove test dependency on unmaintained PyPI toml package
# https://github.com/dolfinus/setuptools-git-versioning/pull/117
# https://fedoraproject.org/wiki/Changes/DeprecatePythonToml
Patch:      %{forgeurl}/pull/117.patch
# Downstream-only: patch out coverage-analysis machinery
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:      0001-Downstream-only-patch-out-coverage-analysis-machiner.patch

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:  help2man

%global _description %{expand:
Use git repo data (latest tag, current commit hash, etc) for building a version
number according to PEP 440.

Features:

  • Can be installed & configured through both setup.py and PEP 518’s
    pyproject.toml
  • Does not require to change source code of the project
  • Tag-, file-, and callback-based versioning schemas are supported
  • Templates for tag, dev and dirty versions are separated
  • Templates support a lot of substitutions including git and environment
    information
  • Well-documented

Limitations:

  • Currently the only supported VCS is Git
  • Only Git v2 is supported
  • Only Setuptools build backend is supported (no Poetry & others)
  • Currently does not support automatic exporting of package version to a file
    for runtime use (but you can use setuptools-git-versioning > file redirect
    instead)}

%description %_description

%package -n python3-setuptools-git-versioning
Summary:    %{summary}

%description -n python3-setuptools-git-versioning %_description

%prep
%autosetup -n setuptools-git-versioning-%{version} -S git

# If we make any changes, do them above this line, and then:
# git add --all
# git commit -m 'Downstream changes' --allow-empty

# Needed for correct version metadata (otherwise defaults to 0.0.1,
# https://bugzilla.redhat.com/show_bug.cgi?id=2405588).
git tag v2.1.0

%generate_buildrequires
%pyproject_buildrequires requirements-test.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l setuptools_git_versioning

install -d '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man --no-info --no-discard-stderr \
    --name='%{summary}' --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/setuptools-git-versioning.1' \
    setuptools-git-versioning

%check
%pyproject_check_import

# Tries to install “wheel” from PyPI, even with python3-wheel installed
k="${k-}${k+ and }not test_config_not_used"

%pytest -k "${k-}" -v

%files -n python3-setuptools-git-versioning -f %{pyproject_files}
%{_bindir}/setuptools-git-versioning
%{_mandir}/man1/setuptools-git-versioning.1*

%changelog
%autochangelog
