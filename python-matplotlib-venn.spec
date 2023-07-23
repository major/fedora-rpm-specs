%bcond_without tests

%global pypi_name matplotlib-venn

%global _description %{expand:
Venn diagram plotting routines for Python/Matplotlib. The package
provides four main functions: venn2, venn2_circles, venn3 and
venn3_circles.}


Name:           python-%{pypi_name}
Version:        0.11.7
Release:        6%{?dist}
Summary:        Routines for plotting area-weighted two- and three-circle venn diagrams

License:        MIT
URL:            https://github.com/konstantint/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch:          https://github.com/konstantint/matplotlib-venn/pull/70.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files matplotlib_venn

%check
%if %{with tests}
%pytest
%endif

%files -n python3-matplotlib-venn -f %{pyproject_files}
%doc README.rst DEVELOPER-README.rst CHANGELOG.txt

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 0.11.7-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 20 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11.7-3
- Fix compatibility with Matplotlib 3.6.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.11.7-2
- Rebuilt for Python 3.11

* Wed Apr 6 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.11.7-1
- Initial package
