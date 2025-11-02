Name:           python-wurlitzer
Version:        3.1.1
Release:        %autorelease
Summary:        Capture C-level output in context managers

License:        MIT
URL:            https://github.com/minrk/wurlitzer
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/wurlitzer-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l wurlitzer

BuildRequires:  %{py3_dist pytest}

%description
Capture C-level stdout/stderr pipes in Python via os.dup2.

%package -n     python3-wurlitzer
Summary:        %{summary}

%description -n python3-wurlitzer
Capture C-level stdout/stderr pipes in Python via os.dup2.

%prep
%autosetup -n wurlitzer-%{version}

%check
%pytest -v test.py

%files -n python3-wurlitzer -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
