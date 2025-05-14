%bcond tests 1

# for github etc. use the forgemacros
# https://docs.fedoraproject.org/en-US/packaging-guidelines/SourceURL/#_using_forges_hosted_revision_control

%global _description %{expand:
versioningit is yet another Python packaging plugin for automatically
determining your package’s version based on your version control repository’s
tags. Unlike others, it allows easy customization of the version format and
even lets you easily override the separate functions used for version
extraction & calculation.

Features:

• Works with both setuptools and Hatch
• Installed & configured through PEP 518’s pyproject.toml
• Supports Git, modern Git archives, and Mercurial
• Formatting of the final version uses format template strings, with fields for
  basic VCS information and separate template strings for distanced vs. dirty
  vs. distanced-and-dirty repository states
• Can optionally write the final version to a file for loading at runtime
• Provides custom hooks for inserting the final version and other details into
  a source file at build time
• The individual methods for VCS querying, tag-to-version calculation, version
  bumping, version formatting, and writing the version to a file can all be
  customized using either functions defined alongside one’s project code or via
  publicly-distributed entry points
• Can alternatively be used as a library for use in setup.py or the like, in
  case you don’t want to or can’t configure it via pyproject.toml
• The only thing it does is calculate your version and optionally write it to a
  file; there’s no overriding of your sdist contents based on what is in your
  Git repository, especially not without a way to turn it off, because that
  would just be rude.}

Name:           python-versioningit
Version:        3.1.3
Release:        %{autorelease}
Summary:        Versioning It with your Version In Git

# SPDX
License:        MIT
URL:            https://pypi.org/pypi/versioningit
Source0:        %{pypi_source versioningit}
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        versioningit.1

BuildArch:      noarch

%description %_description


%package -n python3-versioningit
Summary:        %{summary}

# It calls git and hg so these need to be installed
Recommends:     git-core
Recommends:     mercurial

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  git-core
BuildRequires:  mercurial
%endif

%description -n python3-versioningit %_description


%prep
%autosetup -n versioningit-%{version}

# Tweak build requirements to use what we have in Fedora. For test
# dependencies, we change all semver pins to minimum versions.
sed -r -i 's/~=/>=/g' tox.ini
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*)(pytest-cov|.*--(.*-)?cov)/\1# \2/g' tox.ini
# Do not error on DeprecationWarning; this makes sense for upstream CI, but is
# too strict for downstream builds.
sed -r -i 's/^(filterwarnings = )error/\1default/' tox.ini

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l versioningit

install -p -m 0644 -Dt %{buildroot}%{_mandir}/man1/ %{SOURCE1}


%check
%if %{with tests}
# Editable mode doesn’t work when operating on the system site-packages
k="${k-}${k+ and }not test_editable_mode"
# These require network access.
k="${k-}${k+ and }not test_install_from_git_url"
k="${k-}${k+ and }not test_install_from_zip_url"

%pytest -k "${k-}"
%endif


%files -n python3-versioningit -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{_bindir}/versioningit
%{_mandir}/man1/versioningit.1*


%changelog
%autochangelog
