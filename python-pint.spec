Name:           python-pint
Version:        0.19.2
Release:        %autorelease
Summary:        Physical quantities module

# The entire source is BSD-3-Clause, except:
#   - pint/_vendor/appdirs.py is MIT, but is unbundled in %%prep
#   - pint/_vendor/flexcache.py is also BSD-3-Clause, but is unbundled in
#     %%prep
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/pint
Source0:        %{pypi_source Pint}

# Fix test as NumPy 1.25 changes the rules for equality operator
# https://github.com/hgrecco/pint/commit/b3b18277ecc682bff7ca1fa9e48992f7ec68e47f
#
# Fixes:
#
# test_equal_zero_nan_NP fails with numpy 1.25.1
# https://github.com/hgrecco/pint/issues/1825
Patch:          %{url}/commit/b3b18277ecc682bff7ca1fa9e48992f7ec68e47f.patch

# add min and max to the array function overrides
# https://github.com/hgrecco/pint/commit/1b2b0592f88a1c9fdf9b5649ebade19fa81adea4
#
# Fixes several failures in TestNumpyUnclassified
#
# Cherry-picked to 0.19.
Patch:          0001-add-min-and-max-to-the-array-function-overrides.patch

BuildArch:      noarch

%global _description %{expand:
Pint is a Python package to define, operate and manipulate physical quantities:
the product of a numerical value and a unit of measurement. It allows
arithmetic operations between them and conversions from and to different units.

It is distributed with a comprehensive list of physical units, prefixes and
constants.}

%description %{_description}

%package -n python3-pint
Summary:        %{summary}

%description -n python3-pint %{_description}

# We omit the “uncertainties” extra because python-uncertainties is not yet
# packaged.
%pyproject_extras_subpkg -n python3-pint numpy

%prep
%autosetup -n Pint-%{version} -p1

# We are not sure where this was bundled from, but we are pretty sure it was
# bundled from somewhere! We are not building HTML documentation, so we do not
# need it.
rm -rvf docs/_themes

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/pytest-cov/d' setup.cfg

# Unbundle python-appdirs
# http://github.com/ActiveState/appdirs
# Provides:       bundled(python3dist(appdirs)) = 1.4.4
rm -vf pint/_vendor/appdirs.py
# Unbundle python-flexcache
# https://github.com/hgrecco/flexcache
# Provides:       bundled(python3dist(flexcache)) = 0.2
rm -vf pint/_vendor/flexcache.py
# Add devendored dependencies back in as regular dependencies
sed -r -i 's/^setup_requires/install_requires = appdirs; flexcache\n&/' \
    setup.cfg
# The find-then-modify pattern keeps us from discarding mtimes on sources that
# do not need modification.
find pint -type f -exec \
    gawk '/^from \.+_vendor import (appdirs|flexcache)/ {
        print FILENAME; nextfile }' '{}' '+' |
  xargs -r -t sed -r -i \
      's/^from \.+_vendor (import (appdirs|flexcache))/\1/'

%generate_buildrequires
# We omit the “uncertainties” extra because python-uncertainties is not yet
# packaged.
%pyproject_buildrequires -x numpy,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pint

%check
%pytest

%files -n python3-pint -f %{pyproject_files}
%{_bindir}/pint-convert

%changelog
%autochangelog
