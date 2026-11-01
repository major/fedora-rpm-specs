%global pypi_name omegaconf
%define with_tests 1

Name:          python-%{pypi_name}
Version:       2.3.1
Release:       1%{?dist}
Summary:       A flexible Python configuration system
License:       BSD-3-Clause
URL:           https://github.com/hydra-ecosystem/%{pypi_name}
Source0:       %url/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
# For Fedora specific java locations
Patch0:        omegaconf-system-antlr4.patch

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: antlr4
BuildRequires: java-headless
BuildRequires: python3dist(antlr4-python3-runtime)
# For check
%if 0%{?with_tests}
BuildRequires: python3-pytest
%endif

%global _description %{expand:
A flexible Python configuration system. The last one you will ever need.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf build_helpers/bin/
sed -i 's/antlr4-python3-runtime==4.9.*/antlr4-python3-runtime>=4.9/' requirements/base.txt

%generate_buildrequires
%if 0%{?with_tests}
%pyproject_buildrequires -r
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name} pydevd_plugins

%if 0%{?with_tests}
%check
%pyproject_check_import -e 'pydevd_plugins*'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Thu Sep 24 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Wed Oct 29 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2.3.0-1
- Initial package

