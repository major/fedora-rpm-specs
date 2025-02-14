# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/alexandrebarachant/pyRiemann

Name:           python-pyriemann
Version:        0.8
Release:        %autorelease
Summary:        Riemannian Geometry for Python
%forgemeta
License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

# This package has had architecture-dependent test failures in the past, e.g.
# “One test failure on s390x”
# https://github.com/pyRiemann/pyRiemann/issues/192, so we make the base
# package arched to ensure the tests run on all architectures. The binary
# packages are all still noarch, and there is no compiled code and therefore no
# debugging symbols.
%global debug_package %{nil}

# Since F40, python-scikit-learn is ExcludeArch: %%{ix86}
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# Required to run tests
BuildRequires:  python3dist(pytest)

# Weak dependencies required for various tests
BuildRequires:  python3dist(seaborn)
BuildRequires:  python3dist(matplotlib)

%global common_description %{expand:
pyRiemann is a Python package for covariance matrices manipulation and
classification through Riemannian geometry.

The primary target is classification of multivariate biosignals, like EEG, MEG
or EMG.}

%description %{common_description}


%package -n python3-pyriemann
Summary:        %{summary}

BuildArch:      noarch

# Weak dependencies (not covered by extras other than “docs”/“tests”).
# See docs/installing.rst “Recommended dependencies”.
Recommends:     python3dist(matplotlib)
Recommends:     python3dist(mne)
Recommends:     python3dist(seaborn)

%description -n python3-pyriemann %{common_description}


%package doc
Summary:        Documentation and examples for pyRiemann

BuildArch:      noarch

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# In general, we can generate PDF documentation as a substitute.
#
# Unfortunately, we can’t build *this* documentation without the MNE sample
# data (https://osf.io/86qa2). The documentation build tries to download it
# from the network; we could perhaps circumvent this and include it as an
# additional source, but we must not do so because the sample data does not
# appear to be provided under a clearly-stated or acceptable license; see
# https://predictablynoisy.com/mne-python/manual/sample_dataset.html.

%description doc %{common_description}

This package contains documentation and examples for pyRiemann.


%prep
%autosetup -n pyRiemann-%{version} -p1

# Remove copybutton.js script bundled from python.org documentation via
# scikit-learn’s Sphinx theme. We will not be building HTML documentation
# anyway.
rm -vf doc/_static/copybutton.js
sed -r -i 's/^([[:blank:]]*)(.*copybutton\.js)/\1# \2/' doc/conf.py
# Remove bundled copy of https://pypi.org/pyroject/sphinx-issues/; again, we
# are not going to use it.
rm -rvf doc/sphinxext/
sed -r -i 's/^([[:blank:]]*)(.*sphinx_issues.,)/\1# \2/' doc/conf.py
# Patch flake8 out of “tests” extra:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/("tests".*), "flake8"/\1/' setup.py


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pyriemann


%check
%pytest ${k:+-k "$k"}


%files -n python3-pyriemann -f %{pyproject_files}


%files doc
%license LICENSE
%doc README.md
%doc examples


%changelog
%autochangelog
