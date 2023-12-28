Name:           python-argparse-dataclass
Version:        2.0.0
Release:        %autorelease
Summary:        Declarative CLIs with argparse and dataclasses

# SPDX
License:        MIT
URL:            https://github.com/mivade/argparse_dataclass
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/%{version}/argparse_dataclass-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# The dev extra and the requirements_dev.txt file both have too many linters
# and other unwanted dependencies; it makes more sense to BR what we need for
# testing manually.
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-argparse-dataclass
Summary:        %{summary}

%description -n python3-argparse-dataclass %{common_description}


%prep
%autosetup -n argparse_dataclass-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l argparse_dataclass


%check
%pytest --doctest-modules -v


%files -n python3-argparse-dataclass -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.rst


%changelog
%autochangelog
