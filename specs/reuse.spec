Name:           reuse
Version:        6.2.0
Release:        %autorelease
Summary:        A tool for compliance with the REUSE recommendations
# The CC0-1.0 licence applies to json data files, not code.
# CC-BY-SA-4.0 is applied to documentation.
License:        Apache-2.0 AND CC0-1.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later
Url:            https://github.com/fsfe/reuse-tool
Source0:        %pypi_source

Patch: 0001-use-python-file-magic-for-filetype-detection.patch

# Build
BuildRequires:  python3-devel
BuildRequires:  gettext
# Test + patching
BuildRequires:  git-core
BuildRequires:  mercurial
# These are development dependencies in the Poetry config, not build
# dependencies. They are build dependencies for Fedora packaging.
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist freezegun}
BuildRequires:  %{py3_dist furo}
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx-autodoc-typehints}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist sphinxcontrib-apidoc}
Recommends:     git
Recommends:     mercurial
BuildArch:      noarch

%description
A tool for compliance with the REUSE recommendations. Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%prep
%autosetup -n %{name}-%{version} -S git_am

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
PBR_VERSION=%{version} sphinx-build-%{python3_version} . html
PBR_VERSION=%{version} sphinx-build-%{python3_version} -b man . manpages
rm -rf {html,man}/.{doctrees,buildinfo}
popd

%install
%pyproject_install

%pyproject_save_files reuse

install -p -m0644 -Dt "${RPM_BUILD_ROOT}%{_mandir}/man1" docs/manpages/*.1

%check
# Note: just running %%{pytest} does not work, since the path manipulation
# by that macro and `--doctest-modules` confuse the import machinery too much.
# Hence the manual specification of the test directories.
%{pytest} tests/ "${RPM_BUILD_ROOT}/%{python3_sitearch}/reuse/"

%files -n reuse -f %{pyproject_files}
%license LICENSES/*.txt
%doc README.md CHANGELOG.md docs/html/
%{_bindir}/reuse
%{_mandir}/man1/reuse.1*
%{_mandir}/man1/reuse-*.1*

%changelog
%autochangelog
