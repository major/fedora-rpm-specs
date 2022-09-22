Name:           python-bids-validator
Version:        1.9.2
Release:        %autorelease
Summary:        Validator for the Brain Imaging Data Structure

License:        MIT
URL:            https://github.com/bids-standard/bids-validator
Source0:        %{pypi_source bids-validator}

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
A library of helper functions written in Python, for use with BIDS compliant
applications written in this language.}

%description %{common_description}


%package -n python3-bids-validator
Summary:        %{summary}

%description -n python3-bids-validator %{common_description}


%prep
%autosetup -n bids-validator-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
# The test module really shouldn’t be installed with the package:
mv -v bids_validator/test_*.py ./
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files bids_validator


%check
# Upstream tests require downloading data, and it's not obvious how we could
# make them work with pre-downloaded data.
%pyproject_check_import


%files -n python3-bids-validator -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
