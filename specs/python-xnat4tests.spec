%global pypi_name xnat4tests

Name:           python-%{pypi_name}
Version:        0.3.14
Release:        %autorelease
Summary:        Create basic XNAT instance for API tests

%global forgeurl https://github.com/australian-imaging-service/xnat4tests
%global tag v%{version}
%forgemeta

# The entire source is Apache-2.0, except that versioneer.py and the
# _version.py it generates are CC0-1.0, not generally allowed for code in
# Fedora, but OK under the exception for existing uses in Fedora prior to
# 2022-08-01. While these are included in the source RPM, we re-generate
# _version.py using the system python-versioneer, which is a later version
# under Unlicense so the resulting _version.py is also Unlicense.
License:        Apache-2.0 AND Unlicense
URL:            %forgeurl
Source:         %forgesource
# Update Versioneer and fix config.
# Part of the changes are required even if upstream decides not to
# merge the PR fully (e.g. sticking with the current Versioneer version).
# In that case we could use the system installed Versioneer to recreate
# versioneer.py as well as _version.py which are than Unlicense.
# https://github.com/Australian-Imaging-Service/xnat4tests/pull/20
Patch:          0001-Update-Versioneer-and-fix-config.patch

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Xnat4Tests runs a basic XNAT repository instance in a single Docker to
be used for quick demonstrations on your workstation or integrated
within test suites for tools that use XNAT’s REST API.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
Provides:       xnat4tests = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1 -S git

# Remove duplicated entry point
# We'll create a symlink by the same name instead
sed -r -i '/x4t/d' setup.py

# Remove xnat4tests/docker-src/ (part of the test suite)
rm -rvf xnat4tests/docker-src/

# Our tarball is from a commit created dynamically using git archive.
# That means .gitattributes kicks in and replaces placeholders in
# xnat4tests/_version.py with real values like commit sha. We need the
# placeholders or Versioneer goes looking for a tag belonging to a non
# existent commit only in upstream's repo.
%python3 versioneer.py setup

# Above command also modifies xnat4tests/__init__.py, re-adding the code
# defining __version__. It's already in there. Revert.
git restore --staged --worktree xnat4tests/__init__.py

# Versioneer wants a tag to set version
# Make sure this is last in %%prep to avoid dev release
git add --all
git commit --allow-empty -m '[Fedora] Changes for RPM package'
git tag v%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

# Create symlink x4t -> xnat4tests (replacing duplicate entry point)
pushd %{buildroot}%{_bindir}
ln -s xnat4tests x4t
popd


%check
# Unfortunately, the majority of tests require network (docker)
# Run the single test not requiring network...
%pytest -r fEs tests/test_config.py
# ...and run import test and admire the smoke.
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS
%{_bindir}/%{pypi_name}
%{_bindir}/x4t


%changelog
%autochangelog
