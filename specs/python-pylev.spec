%global pypi_name pylev

%global common_description %{expand:
A pure Python Levenshtein implementation that’s not freaking GPL’d.

Based off the Wikipedia code samples at
https://en.wikipedia.org/wiki/Levenshtein_distance.}

Name:           python-%{pypi_name}
Summary:        Liberally licensed, pure Python Levenshtein implementation
Version:        1.4.0
Release:        %autorelease
License:        BSD-3-Clause

URL:            http://github.com/toastdriven/pylev
Source0:        %{pypi_source}

BuildArch:      noarch
 
BuildRequires:  python3-devel

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l pylev

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
%autochangelog
