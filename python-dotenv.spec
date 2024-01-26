Name:           python-dotenv
Version:        1.0.1
Release:        %autorelease
Summary:        Read key-value pairs from a .env file and set them as environment variables

License:        BSD-3-Clause
URL:            https://github.com/theskumar/python-dotenv
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Reads the key/value pair from .env file and adds them to environment variable.


%package -n     python3-dotenv
Summary:        %{summary}
Recommends:     python3-dotenv+cli

%description -n python3-dotenv
Reads the key/value pair from .env file and adds them to environment variable.


%prep
%autosetup

# Get rid of dependency on python-cov, drop --cov... options from pytest
# Downstream-only change, based on Fedora's linters policy
sed -Ei -e "/^  pytest-cov$/d" \
        -e "s/--cov //" \
        -e "s/--cov-[[:alnum:]]+(=| +)[^ ]+ //g" \
    tox.ini

%if 0%{?rhel}
# Avoid IPython dependency in tests only needed for optional integration
sed -i -e '/ipython/d' requirements.txt tox.ini
%endif


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files dotenv


%check
%tox


%files -n python3-dotenv -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-dotenv cli
%{_bindir}/dotenv


%changelog
%autochangelog
