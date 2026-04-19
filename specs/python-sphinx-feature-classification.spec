%global common_desc %{expand:
This is a Sphinx directive that allows creating matrices of drivers a
project contains and which features they support. The directive takes
an INI file with specific syntax explained in the usage documentation
to generate the matrices, in which projects have the authority to
say what is supported within their own repository.}


Name:             python-sphinx-feature-classification
Version:          2.1.0
Release:          %{autorelease}
Summary:          Generate a matrix of pluggable drivers and their support to an API in Sphinx
Source0:          %{pypi_source sphinx_feature_classification}
License:          Apache-2.0
URL:              https://docs.openstack.org/sphinx-feature-classification
BuildArch:        noarch
BuildRequires:    python3-devel


%description %{common_desc}


%package -n python%{python3_pkgversion}-sphinx-feature-classification
Summary: %{summary}


%description -n python%{python3_pkgversion}-sphinx-feature-classification
%{common_desc}


%prep
%autosetup -n sphinx_feature_classification-%{version}

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    test-requirements.txt


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l sphinx_feature_classification


%check
%tox


%files -n python%{python3_pkgversion}-sphinx-feature-classification -f %{pyproject_files}
%doc README.rst ChangeLog


%changelog
%autochangelog
