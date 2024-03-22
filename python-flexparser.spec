Name:           python-flexparser
Version:        0.3
Release:        %autorelease
Summary:        Parsing made fun … using typing

License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexparser
Source:         %{pypi_source flexparser}

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
The idea is quite simple. You write a class for every type of content (called
here ParsedStatement) you need to parse. Each class should have a from_string
constructor. We used extensively the typing module to make the output structure
easy to use and less error prone.}

%description %{common_description}


%package -n python3-flexparser
Summary:        %{summary}

%description -n python3-flexparser %{common_description}


%prep
%autosetup -n flexparser-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*)\b(pytest-cov)\b/\1# \2/' requirements.test.txt


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flexparser

# Upstream probably doesn’t want to install flexparser.testsuite, but we don’t
# know how to suggest a fix given “[BUG] options.packages.find.exclude not
# taking effect when include_package_data = True”,
# https://github.com/pypa/setuptools/issues/3260.
#
# Still, we don’t want to install the test suite, so we just remove the files
# manually for now.
rm -rvf '%{buildroot}%{python3_sitelib}/flexparser/testsuite'
sed -r -i '/\/flexparser\/testsuite/d' %{pyproject_files}


%check
%pytest


%files -n python3-flexparser -f %{pyproject_files}
%doc README.rst
%doc CHANGES


%changelog
%autochangelog
