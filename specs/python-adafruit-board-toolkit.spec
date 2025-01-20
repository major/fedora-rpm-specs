Name:           python-adafruit-board-toolkit
Version:        1.1.2
Release:        2%{?dist}
Summary:        CircuitPython board identification and information
License:        MIT
URL:            https://github.com/adafruit/Adafruit_Board_Toolkit
Source0:        %{pypi_source adafruit_board_toolkit}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
CircuitPython board identification and information.}

%description %_description

%package -n     python3-adafruit-board-toolkit
Summary:        %{summary}

%description -n python3-adafruit-board-toolkit %_description


%prep
%autosetup -p1 -n adafruit_board_toolkit-%{version}
# Remove bundled files we do not need
rm adafruit_board_toolkit/_list_ports_{osx,windows}.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files adafruit_board_toolkit


%check
%pyproject_check_import


%files -n python3-adafruit-board-toolkit -f %{pyproject_files}
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 Lumír Balhar <lbalhar@redhat.com> - 1.1.2-1
- Update to 1.1.2 (rhbz#2325706)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Lumír Balhar <lbalhar@redhat.com> - 1.1.1-1
- Update to 1.1.1 (rhbz#2153015)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.11

* Mon Apr 11 2022 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-1
- Initial package
