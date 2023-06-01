%global pypi_name termcolor
%global sum ANSI Color formatting for output in terminal

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        %autorelease
Summary:        %{sum}

License:        MIT
URL:            https://github.com/termcolor/termcolor
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)

%description
ANSI Color formatting for output in terminal.


%package -n python3-%{pypi_name}
Summary:  %{sum}

%description -n python3-%{pypi_name}
A Python 3 version of ANSI Color formatting for output in terminal.

%prep
%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.md README.md
%license COPYING.txt

%changelog
%autochangelog
