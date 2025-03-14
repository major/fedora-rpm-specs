Name:           python-jaraco-path
Version:        3.7.2
Release:        %autorelease
Summary:        Miscellaneous path functions

License:        MIT
URL:            https://github.com/jaraco/jaraco.path
Source0:        %{pypi_source jaraco_path}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
jaraco.path provides cross platform hidden file detection}

%description %_description

%package -n     python3-jaraco-path
Summary:        %{summary}

%description -n python3-jaraco-path %_description


%prep
%autosetup -p1 -n jaraco_path-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l jaraco


%check
%pytest


%files -n python3-jaraco-path -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
