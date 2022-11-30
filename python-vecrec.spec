# We do not build Sphinx documentation because current versions of
# python-autoclasstoc bring in a large tree of unpackaged dependencies via the
# python-parametrized-from-file test dependency, so we have elected to retire
# rather than upgrade python-autoclasstoc.

Name:           python-vecrec
Version:        0.3.1
Release:        %autorelease
Summary:        2D vector and rectangle library

# SPDX
License:        MIT
URL:            https://github.com/kxgames/vecrec
Source0:        %{pypi_source vecrec}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(pytest)

%global common_description %{expand:
This package provides 2D vector and rectangle classes. These classes were
written to be used in games, so they have some methods that conveniently tie
into pyglet and pygame, but for the most part they are quite general and could
be used for almost anything.}
%description %{common_description}


%package -n python3-vecrec
Summary:        %{summary}

Obsoletes:      python-vecrec-doc < 0.3.1-3

%description -n python3-vecrec %{common_description}


%prep
%autosetup -n vecrec-%{version}

# Remove HTML coverage directory with bundled JavaScript and other cruft
rm -rvf tests/htmlcov
# Patch out coverage dependencies
sed -r -i '/\b(pytest-cov|coveralls)\b/d' pyproject.toml
sed -r -i \
    -e 's/[[:blank:]]--cov[^=[:blank:]]*[= ][^[:blank:]]+//g' \
    -e 's/--no-cov[^[:blank:]]*//g' tests/pytest.ini

# Remove shebangs from modules. These are not script-like, so shebangs are
# useless. The find-then-modify pattern keeps us from discarding mtimes on
# any sources that do not need modification.
find vecrec -type f -exec \
    gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files vecrec


%check
%pytest tests


%files -n python3-vecrec -f %{pyproject_files}
# pyproject-rpm-macros takes care of LICENSE.txt; verify with “rpm -qL -p …”
%doc README.rst


%changelog
%autochangelog
