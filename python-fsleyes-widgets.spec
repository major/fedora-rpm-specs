%bcond xvfb_tests 1

%global desc %{expand:
A collection of custom wx widgets and utilities used by FSLeyes.}

Name:           python-fsleyes-widgets
Version:        0.14.3
Release:        %autorelease
Summary:        A collection of custom wx widgets and utilities used by FSLeyes

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/fsleyes-widgets
Source0:        %{pypi_source fsleyes-widgets}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with xvfb_tests}
BuildRequires:  xorg-x11-server-Xvfb
# We BR pytest manually because other dependencies in requirements-dev.txt
# pertain to coverage analysis
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters)
# or to Sphinx documentation (which we do not build).
#
# However, we’re currently trying to run tests without pytest, so this is
# commented out:
BuildRequires:  %{py3_dist pytest}
%endif

%description %{desc}


%package -n python3-fsleyes-widgets
Summary:        %{summary}

%description -n python3-fsleyes-widgets %{desc}

# do not generate docs because sphinx docs bundle js etc. which are very hard to unbundle


%prep
%autosetup -n fsleyes-widgets-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/[[:blank:]]--cov=[^[:blank:]]+//' setup.cfg

# remove unneeded shebangs
find fsleyes_widgets -type f -name '*.py' -exec sed -r -i '1{/^#!/d}' '{}' '+'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fsleyes_widgets


%check
%if %{with xvfb_tests}
# From https://git.fmrib.ox.ac.uk/fsl/fsleyes/widgets/blob/master/.ci/test_template.sh
%global __pytest xvfb-run -a -s '-screen 0 1920x1200x24' pytest
%pytest tests -m 'not dodgy'
%else
%pyproject_check_import
%endif


%files -n python3-fsleyes-widgets -f %{pyproject_files}
# While %%pyproject_files contains LICENSE in .dist-info, we need to add
# COPYRIGHT manually, so we install both files in the same place.
%license LICENSE COPYRIGHT
%doc README.rst


%changelog
%autochangelog
