%global pypi_name pastel

%global common_description %{expand:
Pastel is a simple library to help you colorize strings in your
terminal.

It comes bundled with predefined styles:

- info: green
- comment: yellow
- question: black on cyan
- error: white on red

Features:

- Use predefined styles or add you own.
- Disable colors all together by calling with_colors(False).
- Automatically disables colors if the output is not a TTY.
- Used in cleo.}

Name:           python-%{pypi_name}
Summary:        Bring colors to your terminal
Version:        0.2.1
Release:        %autorelease
License:        MIT

URL:            https://github.com/sdispater/pastel
Source0:        %{pypi_source}

# do not install the "tests" package
Patch0:         00-dont-install-tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1



%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}


%check
%pyproject_check_import

PYTHONPATH=. pytest tests


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE



%changelog
%autochangelog
