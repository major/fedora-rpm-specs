
%global srcname fastprogress

Name: python-%{srcname}
Version: 1.0.0
Release: %autorelease
Summary: Progress bar for Jupyter Notebook and console 

License: Apache-2.0
URL: https://github.com/AnswerDotAI/fastprogress
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
A Python-based, fast and simple progress bar 
for Jupyter Notebook and console.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{srcname}

%check
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
