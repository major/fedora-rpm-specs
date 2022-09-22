Name:           python-adafruit-board-toolkit
Version:        1.1.0
Release:        3%{?dist}
Summary:        CircuitPython board identification and information
License:        MIT
URL:            https://github.com/adafruit/Adafruit_Board_Toolkit
Source0:        %{pypi_source adafruit-board-toolkit}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
CircuitPython board identification and information.}

%description %_description

%package -n     python3-adafruit-board-toolkit
Summary:        %{summary}

%description -n python3-adafruit-board-toolkit %_description


%prep
%autosetup -p1 -n adafruit-board-toolkit-%{version}
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.11

* Mon Apr 11 2022 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-1
- Initial package
