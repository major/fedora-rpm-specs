%global _description \
Jinxed is a pure-Python implementation of a subset of the Python curses library\
for all platforms. It includes terminal information for common and popular\
terminals.

Name:           python-jinxed
Version:        2.1.0
Release:        %autorelease
Summary:        Pure-Python implementation of a subset of the Python curses library

# Most of the files in jinxed/terminfo are derived from ncurses and fall under X11
# All applicable files have a note to see the LICENSE.ncurses file in their headers
# All other files fall under the MPL-2.0 License in the LICENSE file.
License:        MPL-2.0 and X11
URL:            https://github.com/Rockhopper-Technologies/jinxed
Source:         %{pypi_source jinxed}

BuildArch:      noarch
BuildRequires:  python3-devel

%description    %{_description}

%package -n     python3-jinxed
Summary:        %{summary}

%description -n python3-jinxed %{_description}

%prep
%autosetup -p1 -n jinxed-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jinxed

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-jinxed -f %{pyproject_files}
%doc doc/*.rst

%changelog
%autochangelog
