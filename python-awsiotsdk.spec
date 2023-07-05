%bcond_without  tests

%global         srcname     awsiotsdk

Name:           python-%{srcname}
Version:        1.15.4
Release:        %autorelease
Summary:        AWS IoT SDK based on the AWS Common Runtime

License:        Apache-2.0
URL:            https://github.com/aws/aws-iot-device-sdk-python-v2
Source0:         %{pypi_source %{srcname}}

# Add a license file.
# https://github.com/major/aws-iot-device-sdk-python-v2/pull/2
Source1:        LICENSE

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(pytest)
%endif


%global _description %{expand:
Next generation AWS IoT Client SDK for Python using the AWS Common Runtime.}


%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Add license file.
cp %SOURCE1 .


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files awsiot


%check
%pyproject_check_import

%if %{with tests}
# test_rpc.py has some import issues.
%pytest --ignore=test/test_rpc.py
%endif


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog