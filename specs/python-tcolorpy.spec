Name:          python-tcolorpy
Version:       0.1.3
Release:       8%{?dist}
Summary:       Python library to apply true color for terminal text

License:       MIT
URL:           https://github.com/thombashi/tcolorpy
Source0:       %{pypi_source tcolorpy}

BuildArch:     noarch
BuildRequires: python3-devel

# Missing pytest-md-report, hence manually specifying pytest instead
BuildRequires: python3dist(pytest)

%description
%{summary}.

%package -n python3-tcolorpy
Summary:        %{summary}

%description -n python3-tcolorpy
%{summary}.


%prep
%autosetup -n tcolorpy-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files tcolorpy


%check
%pytest


%files -n python3-tcolorpy -f %{pyproject_files}
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.3-2
- Rebuilt for Python 3.12

* Wed May 10 2023 Jonny Heggheim <hegjon@gmail.com> - 0.1.3-1
- Updated to version 0.1.3

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.11

* Fri Feb 25 2022 Jonny Heggheim <hegjon@gmail.com> - 0.1.1-1
- Initial package
