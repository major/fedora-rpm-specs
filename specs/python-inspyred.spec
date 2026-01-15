%global _description %{expand:
inspyred is a free, open source framework for creating biologically-inspired
computational intelligence algorithms in Python, including evolutionary
computation, swarm intelligence, and immunocomputing. Additionally, inspyred
provides easy-to-use canonical versions of many bio-inspired algorithms for
users who do not need much customization.}


Name:           python-inspyred
Version:        1.0.2

%global forgeurl https://github.com/aarongarrett/inspyred/
%forgemeta

Release:        %{autorelease}
Summary:        Library for bio-inspired computational intelligence

# spdx checked
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%description %_description

%package -n python3-inspyred
Summary:        %{summary}

%description -n python3-inspyred %_description

%prep
%forgeautosetup -p1

# Remove unneeded BRs
sed -e '/flake8/ d' \
    -e '/tox/ d' \
    -e '/coverage/ d' \
    -e '/Sphinx/ d' \
    -i requirements_dev.txt

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
# Make tests that are working discoverable
mv -v tests/example_tests.py tests/test_example.py
mv -v tests/supplemental_tests.py tests/test_supplemental.py
%pytest -v
# Since the tests are bit brittle also run import check
%pyproject_check_import

%files -n python3-inspyred -f %{pyproject_files}
%doc README.rst HISTORY.rst CONTRIBUTING.rst
%doc examples
%{_bindir}/inspyred

%changelog
%autochangelog
