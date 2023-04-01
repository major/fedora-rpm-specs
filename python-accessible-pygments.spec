Name:           python-accessible-pygments
Version:        0.0.4
Release:        %autorelease
Summary:        Accessible pygments themes

BuildArch:      noarch
License:        BSD-3-Clause
URL:            https://quansight-labs.github.io/accessible-pygments/
Source0:        https://github.com/Quansight-Labs/accessible-pygments/archive/v%{version}/accessible-pygments-%{version}.tar.gz

BuildRequires:  python3-devel
# setup.py needs install_requires installed before it can run at all
BuildRequires:  %{py3_dist pygments}

%description
This package includes a collection of accessible themes for pygments
based on different sources.

%package     -n python3-accessible-pygments
Summary:        %{summary}

%py_provides python3-a11y-pygments

%description -n python3-accessible-pygments
This package includes a collection of accessible themes for pygments
based on different sources.

%prep
%autosetup -n accessible-pygments-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files a11y_pygments

%check
# This regenerates the output in test/results.  A successful run means that:
# - The module can be imported; and
# - The module can generate output without errors.
# However, this does not tell us that the output is actually correct.
# We could compare against the original contents of test/results, but those
# can differ due to differences in the version of pygments used.
%{py3_test_envvars} %{python3} test/run_tests.py

%files -n python3-accessible-pygments -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
