Name:           python-pytest-recording
Version:        0.13.4
Release:        %autorelease
Summary:        A pytest plugin powered by VCR.py to record and replay HTTP traffic

License:        MIT
URL:            https://github.com/kiwicom/pytest-recording
Source:         %{pypi_source pytest_recording}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A pytest plugin powered by VCR.py to record and replay HTTP traffic.}

%description %_description

%package -n     python3-pytest-recording
Summary:        %{summary}

%description -n python3-pytest-recording %_description


%prep
%autosetup -p1 -n pytest_recording-%{version}


%generate_buildrequires
%pyproject_buildrequires -x dev,tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pytest_recording


%check
%pyproject_check_import
# Skip failing tests, need network access
k="${k-}${k+ and }not (test_block_network_with_allowed_hosts[block_marker])"
k="${k-}${k+ and }not (test_block_network_with_allowed_hosts[block_cmd])"
k="${k-}${k+ and }not (test_block_network_with_allowed_hosts[vcr_cfg])"

%pytest -k "${k-}"

%files -n python3-pytest-recording -f %{pyproject_files}
%doc docs/ README.rst

%changelog
%autochangelog
