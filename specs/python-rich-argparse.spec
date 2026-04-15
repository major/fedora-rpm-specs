Name:           python-rich-argparse
Version:        1.7.2
Release:        %autorelease
Summary:        Rich help format helpers for argparse and optparse

License:        MIT
URL:            https://github.com/hamdanal/rich-argparse
Source0:        %{pypi_source rich_argparse}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
rich-argparse improves the look and readability of argparse help while
requiring minimal changes to the code.}


%description %_description


%package -n python3-rich-argparse
Summary:        %{summary}


%description -n python3-rich-argparse %_description


%prep
%autosetup -p1 -n rich_argparse-%{version}

# Remove coverage
sed -i \
    -e 's/coverage\[toml\]//' \
    -e 's/covdefaults//' \
    -e 's/pytest-cov//' \
    tests/requirements.txt


%generate_buildrequires
%pyproject_buildrequires tests/requirements.txt


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l rich_argparse


%check
# Regressions in python3.15a
# TODO: regression in Python 3.15.0a3: https://github.com/python/cpython/issues/142950
# https://github.com/hamdanal/rich-argparse/commit/129fd67f7d92cffb3402422112fde6b3121352f6 
# These tests are really hard for somthing that changes ever so slightly with python
# change and rich module change. Its all just cosmetic.
%pytest -k 'not test_subparsers_usage and not test_rich_renderables'


%files -n python3-rich-argparse -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
