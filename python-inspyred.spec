%global _description %{expand:
inspyred is a free, open source framework for creating biologically-inspired
computational intelligence algorithms in Python, including evolutionary
computation, swarm intelligence, and immunocomputing. Additionally, inspyred
provides easy-to-use canonical versions of many bio-inspired algorithms for
users who do not need much customization.}

%global forgeurl https://github.com/aarongarrett/inspyred/
%global commit 5fa8224f0c81c74e3c6183457f760af854ad72fb


Name:           python-inspyred
Version:        1.0.1
%forgemeta

Release:        %{autorelease}
Summary:        Library for bio-inspired computational intelligence

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
# Update for the new python packaging system
# https://github.com/aarongarrett/inspyred/pull/22
Patch0:         0001-feat-list-all-packages.patch

BuildArch:      noarch

%description %_description

%package -n python3-inspyred
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core

%description -n python3-inspyred %_description

%prep
%forgeautosetup -S git

# Remove undeeded BRs
sed -i -e '/pip/ d' -e '/bumpversion/ d' -e '/watchdog/ d' -e '/flake8/ d' -e '/coverage/ d' -e '/tox/ e' -e '/Sphinx/ d' requirements_dev.txt
# Add missing BR
echo "matplotlib" >> requirements_dev.txt

# pp is not packaged (nor maintained), so skip its test
# upstream has been informed: https://github.com/aarongarrett/inspyred/pull/21#issue-1061517666
sed -i -e '/test_parallel_evaluation_pp/i \    @unittest.skip("pp unavailable")' tests/evaluator_tests.py

# May fail simply because of randomisation, so we skip it
# https://github.com/aarongarrett/inspyred/blob/d5976ab503cc9d51c6f586cbb7bb601a38c01128/tests/operator_tests.py#L69
sed -i -e '/test_multiprocessing_migration/i \    @unittest.skip("unreliable")' tests/operator_tests.py

%generate_buildrequires
%pyproject_buildrequires -r requirements_dev.txt


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files inspyred

%check
# Doesnt run all tests
%{pytest}
# Run them all
export PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch}
%{python3} setup.py test

%files -n python3-inspyred -f %{pyproject_files}
%doc README.rst HISTORY.rst CONTRIBUTING.rst
%doc examples
%{_bindir}/inspyred

%changelog
%autochangelog
