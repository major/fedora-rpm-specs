Name:           python-logdetective
Version:        0.2.10
Release:        %autorelease
Summary:        Uses LLM AI to search for build/test failure and provide ideas how to fix it

License:        Apache-2.0
URL:            https://pypi.org/project/logdetective/
Source:         %{pypi_source logdetective}

BuildArch:      noarch
BuildRequires:  python3-devel

# this is what llama-cpp is on
ExclusiveArch:  x86_64 aarch64

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
A Python tool to analyze logs using a Language Model (LLM) and Drain template
miner.
}

%description %_description

%package -n     python3-logdetective
Summary:        %{summary}
Provides:       logdetective

%description -n python3-logdetective %_description

%pyproject_extras_subpkg -n python3-logdetective server
%pycached %{python3_sitelib}/logdetective/server.py

%prep
%autosetup -p1 -n logdetective-%{version}


%generate_buildrequires
%pyproject_buildrequires -x server


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'logdetective'


%check
#server is broken for now
%pyproject_check_import -e logdetective.server


%files -n python3-logdetective -f %{pyproject_files}
%{_bindir}/logdetective
%license LICENSE
%doc README.md
%pycached %exclude %{python3_sitelib}/logdetective/server.py

%changelog
%autochangelog
