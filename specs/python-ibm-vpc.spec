Name:           python-ibm-vpc
Version:        0.33.0
Release:        %autorelease
Summary:        Python client library for IBM Cloud VPC Services

License:        Apache-2.0
URL:            https://github.com/IBM/vpc-python-sdk
Source0:        %{url}/archive/v%{version}/vpc-python-sdk-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# test dependencies are in requirements-dev.txt but mixed with coverage and linters
# tox configuration uses the same file
BuildRequires:  python3-pytest
BuildRequires:  python3-responses

%global _description %{expand:
Python client library to interact with various IBM Cloud Virtual Private Cloud
(VPC) Service APIs.
}


%description %_description

%package -n     python3-ibm-vpc
Summary:        %{summary}

%description -n python3-ibm-vpc %_description


%prep
%autosetup -p1 -n vpc-python-sdk-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'ibm_vpc'


%check
%pytest -v test/unit


%files -n python3-ibm-vpc -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
