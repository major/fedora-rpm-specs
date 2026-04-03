Name:           python-dict2xml
Version:        1.7.8
Release:        %autorelease
Summary:        Convert a python dictionary into an xml file

License:        MIT
URL:            https://github.com/delfick/python-dict2xml
Source:         %{pypi_source dict2xml}

BuildArch:      noarch
BuildRequires:  python3-devel
# The tests extra pins a precise version of pytest, which we cannot respect; we
# therefore simply list test dependencies manually.
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Super Simple utility to convert a python dictionary into an xml string.}

%description %_description

%package -n     python3-dict2xml
Summary:        %{summary}

%description -n python3-dict2xml %_description


%prep
%autosetup -p1 -n dict2xml-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l dict2xml


%check
%pyproject_check_import
%pytest

%files -n python3-dict2xml -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
