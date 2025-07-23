Name:           pgzero
Version:        1.2.1
Release:        %autorelease
Summary:        A zero-boilerplate 2D games framework

# Automatically converted from old format: LGPLv3 and ASL 2.0 and CC-BY-SA and CC0 and MIT and OFL - review is highly recommended.
License:        LGPL-3.0-only AND Apache-2.0 AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0 AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-OFL
# pgzero module and runner under LGPLv3
# examples/basic/fonts/Cherry_Cream_Soda and Roboto_Condensed under ASL 2.0
# examples/lander/lander.py under CC-BY-SA
# examples/basic/fonts/bubblegum_sans.ttf under CC0
# examples/memory/ under MIT
# examples/basic/fonts/Boogaloo and Bubblegum_Sans under OFL
URL:            http://pypi.python.org/pypi/pgzero
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel

%py_provides    python3-%{name}

%description
Pygame Zero A zero boilerplate games programming framework for Python 3, based
on Pygame. Pygame Zero consists of a runner pgzrun that will run a
Pygame Zero script with a full game loop and a range of useful builtins.

%prep
%autosetup -n %{name}-%{version}
# Remove version limit for pygame dependency
sed -i "s/\(pygame.*\), <2.0.*/\1'/" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name} pgzrun

%check
# Some tests cannot be run in a headles environment without display
rm test/test_screen.py test/test_actor.py test/test_sound_formats.py
%{__python3} -m unittest discover test/

%files -f %{pyproject_files}
%doc README.rst examples
%{_bindir}/pgzrun

%changelog
%autochangelog
