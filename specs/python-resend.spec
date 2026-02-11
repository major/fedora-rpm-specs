Name:           python-resend
Version:        2.21.0
Release:        %autorelease
Summary:        Resend Python SDK

License:        MIT
URL:            https://github.com/resendlabs/resend-python
Source:         %{pypi_source resend}
Source1:        requirements.txt

BuildSystem:    pyproject
BuildOption(install):  -l resend

BuildArch:      noarch
BuildRequires:  python3-devel
# required for even running generate_buildrequires 
BuildRequires:  python3-typing-extensions
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools

%global _description %{expand:
The best way to reach humans instead of spam folders. Deliver transactional
and marketing emails at scale.

Python API to the service.}

%description %_description

%package -n     python3-resend
Summary:        %{summary}

%description -n python3-resend %_description

%prep -a
# contains deprecated feature
rm setup.cfg
# OMG, this reads requirements.txt but that is not included in tarball
sed -i '1,$s/^install_requires = open.*/install_requires = \[\]/' setup.py


%check
%pyproject_check_import

%files -n python3-resend -f %{pyproject_files}


%changelog
%autochangelog
