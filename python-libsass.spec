Name:           python-libsass
Version:        0.20.0
Release:        %autorelease
Summary:        Sass for Python: A straightforward binding of libsass for Python

# SPDX
License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source0:        %{url}/archive/%{version}.tar.gz#/libsass-%{version}.tar.gz
# Patch for correct naming of manpages
Patch0:         python-libsass-man.patch
# https://github.com/sass/libsass-python/issues/424
# https://github.com/sass/libsass-python/pull/433 - a bit modified
Patch1:         libsass-python-pr433-sphinx60-remove-deprecated-item.patch
# Add a missing word “to” in the description
# https://github.com/sass/libsass-python/pull/442
# Rebased to 0.20.0
Patch2:         0001-Add-a-missing-word-to-in-the-description.patch
# Replace deprecated license_file with license_files in setup.cfg
# https://github.com/sass/libsass-python/pull/441
Patch3:         %{url}/pull/441.patch
# For libsass 3.6.5 and later; see %%prep
# https://github.com/sass/libsass-python/pull/344
Patch100:       libsass-python-pr344-sass-365.patch

BuildRequires:  python3-devel

# Selected test dependencies from requirements-dev.txt; most entries in that
# file are for linters, code coverage, etc.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  (%{py3_dist werkzeug} with %{py3_dist werkzeug} >= 0.9)

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  libsass-devel

# Needed for building a man page
BuildRequires:  python3-sphinx

%global common_description %{expand:
This package provides a simple Python extension module sass which is binding
LibSass (written in C/C++ by Hampton Catlin and Aaron Leung). It’s very
straightforward and there isn’t any headache related to Python
distribution/deployment. That means you can add just libsass into your
setup.py’s install_requires list or requirements.txt file. No need for Ruby nor
Node.js.}

%description %{common_description}


%package -n python3-libsass
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/
#   #_provides_for_importable_modules
# This package is messy; it occupies quite a few top-level names.
%py_provides python3-sass
%py_provides python3-sassc
%py_provides python3-pysassc
%py_provides python3-sasstests
%py_provides python3-sassutils

%description -n python3-libsass %{common_description}


%prep
%autosetup -n libsass-python-%{version} -N
%autopatch -M 99 -p1
if pkg-config --atleast-version 3.6.5 libsass ; then
%autopatch -m 100 -p1
fi

# While upstream has the executable bit set, we will install this in
# site-packages without executable permissions; therefore, the shebang becomes
# useless, and we should remove it downstream.
sed -r -i '1{/^#!/d}' pysassc.py


%generate_buildrequires
export SYSTEM_SASS='1'
%pyproject_buildrequires


%build
export SYSTEM_SASS='1'
%pyproject_wheel

LIB='lib.%{python3_platform}-cpython-%{python3_version_nodots}'
PYTHONPATH="${PWD}/build/${LIB}" %make_build -C docs man \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'


%install
export SYSTEM_SASS='1'
%pyproject_install
%pyproject_save_files sass sassc pysassc sasstests sassutils _sass

# Collides with libsass. Deprecated; removed in 0.22.0.
rm -v '%{buildroot}%{_bindir}/sassc'

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    docs/_build/man/pysassc.1


%check
%pytest -v sasstests.py


%files -n python3-libsass -f %{pyproject_files}
%doc README.rst
%{_bindir}/pysassc
%{_mandir}/man1/pysassc.1*


%changelog
%autochangelog
