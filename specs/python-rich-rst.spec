Name:           python-rich-rst
Version:        2.1.0
Release:        %autorelease
Summary:        A beautiful reStructuredText renderer for rich
# Main source code is MIT.  The breakdown for other licenses is in
# LICENSES.vendored (renamed from rich_rst/_vendor/LICENSES.txt in the tarball).
License:        BSD-2-Clause AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://wasi-master.github.io/rich-rst
# PyPI tarball is missing tests/conftest.py
# https://github.com/wasi-master/rich-rst/pull/60
Source:         https://github.com/wasi-master/rich-rst/archive/v%{version}/rich-rst-%{version}.tar.gz

# Python:       Python-2.0.1
Source1:        https://docs.python.org/3/objects.inv#/objects-python.inv

# Rich:         MIT
Source2:        https://rich.readthedocs.io/en/stable/objects.inv#/objects-rich.inv

# The modifications applied to this patch are meant to make `make man` works during the build steps.

# - Changes to this patch:
#     * Added a `man_pages` variable to allow sphinx to build correct section for manpages
#     * This patch can be dropped if https://github.com/wasi-master/rich-rst/pull/61 gets merged.
Patch:          patch-docs-conf-for-downstream-build.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  make

# Test dependencies
BuildRequires:  python3-pytest

# Docs dependencies
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-copybutton

# See VENDORED.md in tarball or upstream repo.
Provides:       bundled(python3dist(docutils)) = 0.22.4

%global _description %{expand:
A beautiful reStructuredText renderer for rich.}

%description %_description

%package -n     python3-rich-rst
Summary:        %{summary}

%description -n python3-rich-rst %_description

%prep
%autosetup -p1 -n rich-rst-%{version}

# We don't want any PNG files to be included.
rm -rf *.png

# Change URLs for sphinx docs mapping to local .inv files
sed -E -i \
 -e 's|("https://docs\.python\.org/3",[[:space:]]*)None|\1"%{SOURCE1}"|' \
 -e 's|("https://rich\.readthedocs\.io/en/stable/",[[:space:]]*)None|\1"%{SOURCE2}"|' \
 docs/source/conf.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build manpages
pushd docs
make man
popd

%install
%pyproject_install
%pyproject_save_files -l rich_rst
install -D -m 644 docs/build/man/rich-rst.3 %{buildroot}%{_mandir}/man3/rich-rst.3

%check
%pyproject_check_import
%pytest


%files -n python3-rich-rst -f %{pyproject_files}
%{_mandir}/man3/rich-rst.3*
%doc README.md CHANGELOG.md VENDORED.md SECURITY.md

%changelog
%autochangelog
